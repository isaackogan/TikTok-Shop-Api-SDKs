"""OAuth helper: authorization URLs and token exchange/refresh, with a sync and an async class."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Literal
from urllib.parse import quote

import httpx

from .errors import TikTokShopError

DEFAULT_AUTH_BASE_URL = "https://auth.tiktok-shops.com"
DEFAULT_TIMEOUT = 30.0

AuthType = Literal["seller", "partner", "creator"]
Region = Literal["us", "row"]

_HOSTS = {
    "seller": {"us": "https://services.us.tiktokshop.com", "row": "https://services.tiktokshop.com", "path": "/open/authorize"},
    "partner": {"us": "https://partner.us.tiktokshop.com", "row": "https://partner.tiktokshop.com", "path": "/open/authorize"},
    "creator": {"us": "https://shop.tiktok.com", "row": "https://shop.tiktok.com", "path": "/alliance/creator/auth"},
}


def _enc(s: str) -> str:
    """RFC 3986: only unreserved characters stay."""
    return quote(s, safe="")


@dataclass(frozen=True)
class TokenSet:
    """The result of exchanging an auth code or refreshing a token.

    It holds secrets. ``repr`` hides both tokens, but ``dataclasses.asdict`` and the attributes keep them, so you can
    serialise a set to store it: protect wherever you store it.
    """

    access_token: str = field(repr=False)
    #: Unix timestamp (seconds) at which the access token expires.
    access_token_expire_in: int
    refresh_token: str = field(repr=False)
    #: Unix timestamp (seconds) at which the refresh token expires.
    refresh_token_expire_in: int
    #: Everything below is optional: creator and partner tokens may lack the seller fields.
    #: A field TikTok did not send is ``None`` (``granted_scopes`` is ``None``, not ``[]``, when absent).
    open_id: str | None = None
    seller_name: str | None = None
    seller_base_region: str | None = None
    user_type: int | None = None
    granted_scopes: list[str] | None = None


def _timeout(value: float | httpx.Timeout | None) -> httpx.Timeout:
    return value if isinstance(value, httpx.Timeout) else httpx.Timeout(value)


class _AuthBase:
    def __init__(self, app_key: str, app_secret: str, service_id: str | None, base_url: str) -> None:
        self._app_key = app_key
        self._app_secret = app_secret
        self._service_id = service_id
        self._base_url = base_url.rstrip("/")

    def __repr__(self) -> str:
        return f"{type(self).__name__}(app_key={self._app_key!r}, app_secret='***', service_id={self._service_id!r}, base_url={self._base_url!r})"

    def authorization_url(self, *, type: AuthType, region: Region, state: str | None = None) -> str:
        """The URL to send the seller (or partner, or creator) to. ``state`` is echoed back to your redirect URL."""
        h = _HOSTS.get(type)
        if h is None:
            raise ValueError(f"Unknown authorization type: {type!r}")
        host = h.get(region) if region in ("us", "row") else None
        if host is None:
            raise ValueError(f"Unknown region: {region!r}")
        if type == "creator":
            first = f"app_key={_enc(self._app_key)}"
        else:
            if not self._service_id:
                raise ValueError(f"service_id is required for {type} authorization URLs")
            first = f"service_id={_enc(self._service_id)}"
        return f"{host}{h['path']}?{first}" + ("" if state is None else f"&state={_enc(state)}")

    def _url(self, endpoint: str, extra: list[tuple[str, str]]) -> str:
        params = [("app_key", self._app_key), ("app_secret", self._app_secret), *extra]
        return f"{self._base_url}/api/v2/token/{endpoint}?" + "&".join(f"{k}={_enc(v)}" for k, v in params)

    def _exchange_url(self, code: str) -> str:
        return self._url("get", [("auth_code", code), ("grant_type", "authorized_code")])

    def _refresh_url(self, refresh_token: str) -> str:
        return self._url("refresh", [("refresh_token", refresh_token), ("grant_type", "refresh_token")])


def _transport_error(e: httpx.HTTPError | httpx.InvalidURL) -> TikTokShopError:
    kind = "Request timed out" if isinstance(e, httpx.TimeoutException) else "Request failed"
    return TikTokShopError(f"{kind}: {e}")


def _no_code(status: int) -> int:
    """R13b: the code of a reply with no readable TikTok code: the HTTP status if it is non-2xx (a redirect included,
    since it is never followed), -1 only for an unreadable 2xx."""
    return -1 if 200 <= status < 300 else status


def _to_token_set(response: httpx.Response) -> TokenSet:
    status = response.status_code
    ok = 200 <= status < 300
    try:
        env: Any = json.loads(response.content)
    except ValueError as e:
        raise TikTokShopError(f"Unparseable token response (HTTP {status})", code=_no_code(status), http_status=status) from e
    if not isinstance(env, dict):
        raise TikTokShopError(f"Unexpected token response (HTTP {status})", code=_no_code(status), http_status=status)
    request_id = str(env.get("request_id") or "")
    code = env.get("code")
    if not isinstance(code, int) or isinstance(code, bool):
        code = -1 if ok else status
    if code != 0 or not ok:
        if code == 0:
            code = status  # R13a: a failure that carries no TikTok code uses the HTTP status
        raise TikTokShopError(
            str(env.get("message") or f"HTTP {status}"),
            code=code,
            request_id=request_id,
            http_status=None if ok else status,
        )
    d = env.get("data")
    if not isinstance(d, dict):
        raise TikTokShopError("Token response has no data", code=-1, request_id=request_id)
    for k in ("access_token", "refresh_token"):
        v = d.get(k)
        if not isinstance(v, str) or v == "":
            raise TikTokShopError(f"Token response is missing {k}", code=-1, request_id=request_id)
    for k in ("access_token_expire_in", "refresh_token_expire_in"):
        v = d.get(k)
        if not isinstance(v, int) or isinstance(v, bool):
            raise TikTokShopError(f"Token response is missing {k}", code=-1, request_id=request_id)
    try:
        return TokenSet(
            access_token=d["access_token"],
            access_token_expire_in=d["access_token_expire_in"],
            refresh_token=d["refresh_token"],
            refresh_token_expire_in=d["refresh_token_expire_in"],
            open_id=None if d.get("open_id") is None else str(d["open_id"]),
            seller_name=d.get("seller_name"),
            seller_base_region=d.get("seller_base_region"),
            user_type=d.get("user_type"),
            granted_scopes=None if d.get("granted_scopes") is None else list(d["granted_scopes"]),
        )
    except KeyError as e:
        raise TikTokShopError(f"Token response is missing {e}", code=-1, request_id=request_id) from e


class TikTokShopAuth(_AuthBase):
    """Synchronous OAuth helper."""

    def __init__(
        self,
        app_key: str,
        app_secret: str,
        service_id: str | None = None,
        *,
        base_url: str = DEFAULT_AUTH_BASE_URL,
        timeout: float | httpx.Timeout | None = DEFAULT_TIMEOUT,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        super().__init__(app_key, app_secret, service_id, base_url)
        self._timeout = _timeout(timeout)
        self._transport = transport

    def exchange_code(self, code: str) -> TokenSet:
        """Trade the ``code`` from the redirect for tokens."""
        return self._get(self._exchange_url(code))

    def refresh(self, refresh_token: str) -> TokenSet:
        """Trade a refresh token for new tokens."""
        return self._get(self._refresh_url(refresh_token))

    def _get(self, url: str) -> TokenSet:
        try:
            with httpx.Client(timeout=self._timeout, transport=self._transport) as c:
                response = c.get(url)
        except (httpx.HTTPError, httpx.InvalidURL) as e:
            raise _transport_error(e) from e
        return _to_token_set(response)


class AsyncTikTokShopAuth(_AuthBase):
    """Asynchronous OAuth helper: ``exchange_code`` and ``refresh`` are coroutines."""

    def __init__(
        self,
        app_key: str,
        app_secret: str,
        service_id: str | None = None,
        *,
        base_url: str = DEFAULT_AUTH_BASE_URL,
        timeout: float | httpx.Timeout | None = DEFAULT_TIMEOUT,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        super().__init__(app_key, app_secret, service_id, base_url)
        self._timeout = _timeout(timeout)
        self._transport = transport

    async def exchange_code(self, code: str) -> TokenSet:
        return await self._get(self._exchange_url(code))

    async def refresh(self, refresh_token: str) -> TokenSet:
        return await self._get(self._refresh_url(refresh_token))

    async def _get(self, url: str) -> TokenSet:
        try:
            async with httpx.AsyncClient(timeout=self._timeout, transport=self._transport) as c:
                response = await c.get(url)
        except (httpx.HTTPError, httpx.InvalidURL) as e:
            raise _transport_error(e) from e
        return _to_token_set(response)
