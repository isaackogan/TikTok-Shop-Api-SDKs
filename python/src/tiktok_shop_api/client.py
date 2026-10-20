from __future__ import annotations

import json
import time
from collections.abc import Generator
from dataclasses import dataclass, field, replace
from typing import Any
from urllib.parse import parse_qsl, quote

import httpx

from .errors import TikTokShopError
from .generated._groups import (
    ASYNC_GROUPS,
    SYNC_GROUPS,
    AffiliateCreatorApi,
    AsyncAffiliateCreatorApi,
    AffiliatePartnerApi,
    AsyncAffiliatePartnerApi,
    AffiliateSellerApi,
    AsyncAffiliateSellerApi,
    AnalyticsApi,
    AsyncAnalyticsApi,
    AuthorizationApi,
    AsyncAuthorizationApi,
    CustomerEngagementApi,
    AsyncCustomerEngagementApi,
    CustomerServiceApi,
    AsyncCustomerServiceApi,
    EventApi,
    AsyncEventApi,
    FinanceApi,
    AsyncFinanceApi,
    FulfilledByTikTokApi,
    AsyncFulfilledByTikTokApi,
    FulfillmentApi,
    AsyncFulfillmentApi,
    LogisticsApi,
    AsyncLogisticsApi,
    OrdersApi,
    AsyncOrdersApi,
    ProductsApi,
    AsyncProductsApi,
    PromotionApi,
    AsyncPromotionApi,
    ReturnAndRefundApi,
    AsyncReturnAndRefundApi,
    SellerApi,
    AsyncSellerApi,
    SupplyChainApi,
    AsyncSupplyChainApi,
    ToolsApi,
    AsyncToolsApi,
)
from .generated.client import Client
from .signing import Signer, requires_shop_cipher

DEFAULT_BASE_URL = "https://open-api.tiktokglobalshop.com"
DEFAULT_TIMEOUT = 30.0

_RESERVED = frozenset({"app_key", "timestamp", "sign", "shop_cipher"})


@dataclass(frozen=True)
class _Credentials:
    app_key: str
    app_secret: str = field(repr=False)
    access_token: str | None = field(default=None, repr=False)
    shop_cipher: str | None = field(default=None, repr=False)


def _encode(s: str) -> str:
    """RFC 3986 percent-encoding: everything but the unreserved characters."""
    return quote(s, safe="")


class _SigningAuth(httpx.Auth):
    """The request hook: shop cipher, app key, timestamp, access token header, then the signature."""

    requires_request_body = True

    def __init__(self, creds: _Credentials) -> None:
        self._creds = creds

    def auth_flow(self, request: httpx.Request) -> Generator[httpx.Request, httpx.Response, None]:
        c = self._creds
        path_bytes, _, query_bytes = request.url.raw_path.partition(b"?")
        path = path_bytes.decode("ascii")
        # httpx wrote the query with urlencode (space -> "+", a literal plus -> "%2B"), so this
        # recovers the exact values the caller passed.
        query = [(k, v) for k, v in parse_qsl(query_bytes.decode("ascii"), keep_blank_values=True) if k not in _RESERVED]
        method = request.method.upper()
        if c.shop_cipher and requires_shop_cipher(method, path):
            query.append(("shop_cipher", c.shop_cipher))
        query.append(("app_key", c.app_key))
        query.append(("timestamp", str(int(time.time()))))
        if c.access_token:
            request.headers["x-tts-access-token"] = c.access_token
        body = request.content or None
        query.append(
            (
                "sign",
                Signer.sign(
                    path=path,
                    query=query,
                    content_type=request.headers.get("content-type"),
                    body=body,
                    app_secret=c.app_secret,
                ),
            )
        )
        qs = "&".join(f"{_encode(k)}={_encode(v)}" for k, v in query)
        request.url = request.url.copy_with(raw_path=path_bytes + b"?" + qs.encode("ascii"))
        yield request


def _check_response(response: httpx.Response) -> None:
    """The response hook (body already read): raise TikTokShopError unless it is a successful envelope."""
    status = response.status_code
    ok = 200 <= status < 300
    envelope: Any = None
    parse_error: Exception | None = None
    try:
        envelope = json.loads(response.content)
    except ValueError as e:
        parse_error = e
    is_obj = isinstance(envelope, dict)
    # R13b: -1 only for a 2xx reply that cannot be understood (not a JSON object).
    if ok and not is_obj:
        raise TikTokShopError(f"Response is not valid JSON (HTTP {status})", code=-1, http_status=status) from parse_error
    code = envelope.get("code") if is_obj else None
    message = envelope.get("message") if is_obj else None
    request_id = envelope.get("request_id") if is_obj else None
    code = code if isinstance(code, int) and not isinstance(code, bool) else None
    message = message if isinstance(message, str) else None
    request_id = request_id if isinstance(request_id, str) else ""
    if not ok:
        raise TikTokShopError(
            message if message is not None else (response.reason_phrase or f"HTTP {status}"),
            # R13a: a body with no code, or code 0, still failed, so the HTTP status is the code.
            code=code if code else status,
            request_id=request_id,
            http_status=status,
        )
    if code is not None and code != 0:
        raise TikTokShopError(message or "", code=code, request_id=request_id, http_status=status)


def _sync_hook(response: httpx.Response) -> None:
    response.read()
    _check_response(response)


async def _async_hook(response: httpx.Response) -> None:
    await response.aread()
    _check_response(response)


class _SharedTransport(httpx.BaseTransport):
    """Lends a transport to another client without letting that client close it."""

    def __init__(self, inner: httpx.BaseTransport) -> None:
        self._inner = inner

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        return self._inner.handle_request(request)

    def close(self) -> None:
        pass


class _SharedAsyncTransport(httpx.AsyncBaseTransport):
    def __init__(self, inner: httpx.AsyncBaseTransport) -> None:
        self._inner = inner

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        return await self._inner.handle_async_request(request)

    async def aclose(self) -> None:
        pass


class _Keep:
    def __repr__(self) -> str:
        return "<keep>"


_KEEP: Any = _Keep()


def _timeout(value: float | httpx.Timeout | None) -> httpx.Timeout:
    return value if isinstance(value, httpx.Timeout) else httpx.Timeout(value)


class TikTokShop:
    """Synchronous TikTok Shop API client. One attribute per API group, e.g. ``client.orders``."""

    affiliate_creator: AffiliateCreatorApi
    affiliate_partner: AffiliatePartnerApi
    affiliate_seller: AffiliateSellerApi
    analytics: AnalyticsApi
    authorization: AuthorizationApi
    customer_engagement: CustomerEngagementApi
    customer_service: CustomerServiceApi
    event: EventApi
    finance: FinanceApi
    fulfilled_by_tiktok: FulfilledByTikTokApi
    fulfillment: FulfillmentApi
    logistics: LogisticsApi
    orders: OrdersApi
    products: ProductsApi
    promotion: PromotionApi
    return_and_refund: ReturnAndRefundApi
    seller: SellerApi
    supply_chain: SupplyChainApi
    tools: ToolsApi

    def __init__(
        self,
        app_key: str,
        app_secret: str,
        access_token: str | None = None,
        shop_cipher: str | None = None,
        *,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float | httpx.Timeout | None = DEFAULT_TIMEOUT,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        self._creds = _Credentials(app_key, app_secret, access_token, shop_cipher)
        self._base_url = base_url.rstrip("/")
        self._timeout = timeout
        self._transport: httpx.BaseTransport | None = transport
        self._init_groups(self._transport)

    def _init_groups(self, transport: httpx.BaseTransport | None) -> None:
        self._client = Client(
            base_url=self._base_url,
            timeout=_timeout(self._timeout),
            httpx_args={
                "auth": _SigningAuth(self._creds),
                # No transport of our own unless the caller gave one: httpx then builds its default,
                # which honours HTTP(S)_PROXY, ALL_PROXY, NO_PROXY and SSL_CERT_FILE.
                **({"transport": transport} if transport is not None else {}),
                "event_hooks": {"response": [_sync_hook]},
            },
        )
        for name, cls in SYNC_GROUPS.items():
            setattr(self, name, cls(self._client))

    def __repr__(self) -> str:
        return f"{type(self).__name__}(app_key={self._creds.app_key!r}, base_url={self._base_url!r}, secrets hidden)"

    def with_shop(self, *, access_token: str | None = _KEEP, shop_cipher: str | None = _KEEP) -> TikTokShop:
        """A client for another shop or token that shares this client's HTTP transport.

        A transport you passed in is shared; otherwise the new client builds its own default httpx client with
        the same base URL and timeout.

        Arguments left out keep this client's values. This client is not changed. Closing the returned
        client does not close the shared transport; close the original for that.
        """
        child = object.__new__(type(self))
        child._creds = replace(
            self._creds,
            access_token=self._creds.access_token if access_token is _KEEP else access_token,
            shop_cipher=self._creds.shop_cipher if shop_cipher is _KEEP else shop_cipher,
        )
        child._base_url = self._base_url
        child._timeout = self._timeout
        child._transport = self._transport
        child._init_groups(None if self._transport is None else _SharedTransport(self._transport))
        return child

    def close(self) -> None:
        self._client.get_httpx_client().close()

    def __enter__(self) -> TikTokShop:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()


class AsyncTikTokShop:
    """Asynchronous TikTok Shop API client. One attribute per API group; every method is a coroutine."""

    affiliate_creator: AsyncAffiliateCreatorApi
    affiliate_partner: AsyncAffiliatePartnerApi
    affiliate_seller: AsyncAffiliateSellerApi
    analytics: AsyncAnalyticsApi
    authorization: AsyncAuthorizationApi
    customer_engagement: AsyncCustomerEngagementApi
    customer_service: AsyncCustomerServiceApi
    event: AsyncEventApi
    finance: AsyncFinanceApi
    fulfilled_by_tiktok: AsyncFulfilledByTikTokApi
    fulfillment: AsyncFulfillmentApi
    logistics: AsyncLogisticsApi
    orders: AsyncOrdersApi
    products: AsyncProductsApi
    promotion: AsyncPromotionApi
    return_and_refund: AsyncReturnAndRefundApi
    seller: AsyncSellerApi
    supply_chain: AsyncSupplyChainApi
    tools: AsyncToolsApi

    def __init__(
        self,
        app_key: str,
        app_secret: str,
        access_token: str | None = None,
        shop_cipher: str | None = None,
        *,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float | httpx.Timeout | None = DEFAULT_TIMEOUT,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        self._creds = _Credentials(app_key, app_secret, access_token, shop_cipher)
        self._base_url = base_url.rstrip("/")
        self._timeout = timeout
        self._transport: httpx.AsyncBaseTransport | None = transport
        self._init_groups(self._transport)

    def _init_groups(self, transport: httpx.AsyncBaseTransport | None) -> None:
        self._client = Client(
            base_url=self._base_url,
            timeout=_timeout(self._timeout),
            httpx_args={
                "auth": _SigningAuth(self._creds),
                # No transport of our own unless the caller gave one: httpx then builds its default,
                # which honours HTTP(S)_PROXY, ALL_PROXY, NO_PROXY and SSL_CERT_FILE.
                **({"transport": transport} if transport is not None else {}),
                "event_hooks": {"response": [_async_hook]},
            },
        )
        for name, cls in ASYNC_GROUPS.items():
            setattr(self, name, cls(self._client))

    def __repr__(self) -> str:
        return f"{type(self).__name__}(app_key={self._creds.app_key!r}, base_url={self._base_url!r}, secrets hidden)"

    def with_shop(self, *, access_token: str | None = _KEEP, shop_cipher: str | None = _KEEP) -> AsyncTikTokShop:
        """A client for another shop or token that shares this client's HTTP transport (see :meth:`TikTokShop.with_shop`)."""
        child = object.__new__(type(self))
        child._creds = replace(
            self._creds,
            access_token=self._creds.access_token if access_token is _KEEP else access_token,
            shop_cipher=self._creds.shop_cipher if shop_cipher is _KEEP else shop_cipher,
        )
        child._base_url = self._base_url
        child._timeout = self._timeout
        child._transport = self._transport
        child._init_groups(None if self._transport is None else _SharedAsyncTransport(self._transport))
        return child

    async def aclose(self) -> None:
        await self._client.get_async_httpx_client().aclose()

    async def __aenter__(self) -> AsyncTikTokShop:
        return self

    async def __aexit__(self, *exc: object) -> None:
        await self.aclose()
