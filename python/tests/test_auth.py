import asyncio
import json
from pathlib import Path

import httpx
import pytest

from tiktok_shop_api import AsyncTikTokShopAuth, TikTokShopAuth, TikTokShopError, TokenSet

VECTORS = json.loads((Path(__file__).parents[2] / "shared/test-vectors/auth.json").read_text())


def stub(status: int, body: str, seen: list | None = None):
    def handler(request: httpx.Request) -> httpx.Response:
        if seen is not None:
            seen.append(request)
        return httpx.Response(status, content=body.encode(), headers={"content-type": "application/json"})

    return httpx.MockTransport(handler)


@pytest.mark.parametrize("c", VECTORS["authorizationUrls"], ids=lambda c: f'{c["type"]}-{c["region"]}-{c["state"]}')
def test_authorization_urls(c):
    auth = TikTokShopAuth(c["appKey"] or "k", "s", service_id=c["serviceId"])
    if c["appKey"]:
        auth = TikTokShopAuth(c["appKey"], "s")
    kwargs = {} if c["state"] is None else {"state": c["state"]}
    assert auth.authorization_url(type=c["type"], region=c["region"], **kwargs) == c["url"]


def test_authorization_url_needs_service_id_for_seller():
    with pytest.raises(ValueError, match="service_id"):
        TikTokShopAuth("k", "s").authorization_url(type="seller", region="us")


def test_authorization_url_rejects_unknown_type_and_region():
    auth = TikTokShopAuth("k", "s", service_id="1")
    with pytest.raises(ValueError):
        auth.authorization_url(type="nope", region="us")  # type: ignore[arg-type]
    with pytest.raises(ValueError):
        auth.authorization_url(type="seller", region="eu")  # type: ignore[arg-type]


@pytest.mark.parametrize("c", VECTORS["tokenRequests"], ids=lambda c: c["kind"])
def test_token_request_urls_sync_and_async(c):
    ok = '{"code":0,"message":"success","request_id":"r","data":{"access_token":"a","access_token_expire_in":1,"refresh_token":"r","refresh_token_expire_in":2,"open_id":"o","seller_name":"n","seller_base_region":"US","user_type":0}}'
    seen: list[httpx.Request] = []
    auth = TikTokShopAuth(c["appKey"], c["appSecret"], transport=stub(200, ok, seen))
    (auth.exchange_code if c["kind"] == "exchange" else auth.refresh)(c["value"])

    aseen: list[httpx.Request] = []

    async def handler(request: httpx.Request) -> httpx.Response:
        aseen.append(request)
        return httpx.Response(200, content=ok.encode())

    aauth = AsyncTikTokShopAuth(c["appKey"], c["appSecret"], transport=httpx.MockTransport(handler))
    asyncio.run((aauth.exchange_code if c["kind"] == "exchange" else aauth.refresh)(c["value"]))
    for got in (seen, aseen):
        assert len(got) == 1
        assert got[0].method == "GET"
        assert str(got[0].url) == c["url"]


def test_base_url_is_overridable():
    seen: list[httpx.Request] = []
    auth = TikTokShopAuth("k", "s", base_url="http://localhost:1234/", transport=stub(200, '{"code":0,"data":{"access_token":"a","access_token_expire_in":1,"refresh_token":"r","refresh_token_expire_in":2,"open_id":"o","seller_name":"n","seller_base_region":"US","user_type":0}}', seen))
    auth.exchange_code("c")
    assert str(seen[0].url).startswith("http://localhost:1234/api/v2/token/get?app_key=k")


@pytest.mark.parametrize("c", VECTORS["tokenResponses"], ids=lambda c: c["name"])
def test_token_responses(c):
    for is_async in (False, True):
        if is_async:
            aauth = AsyncTikTokShopAuth("k", "s", transport=_async_stub(200, c["body"]))
            call = lambda: asyncio.run(aauth.exchange_code("x"))  # noqa: E731
        else:
            auth = TikTokShopAuth("k", "s", transport=stub(200, c["body"]))
            call = lambda: auth.exchange_code("x")  # noqa: E731
        if c["errorCode"] is not None:
            with pytest.raises(TikTokShopError) as ei:
                call()
            assert ei.value.code == c["errorCode"]
            assert ei.value.request_id == "r2"
            assert ei.value.message == "invalid auth code"
        else:
            e = c["expected"]
            assert call() == TokenSet(
                access_token=e["accessToken"],
                access_token_expire_in=e["accessTokenExpireIn"],
                refresh_token=e["refreshToken"],
                refresh_token_expire_in=e["refreshTokenExpireIn"],
                open_id=e["openId"],
                seller_name=e["sellerName"],
                seller_base_region=e["sellerBaseRegion"],
                user_type=e["userType"],
                granted_scopes=e["grantedScopes"],
            )


def _async_stub(status: int, body: str):
    async def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(status, content=body.encode())

    return httpx.MockTransport(handler)


@pytest.mark.parametrize("body", ['{"code":0,"message":"success","request_id":"r9"}', '{"code":0,"request_id":"r9","data":[1]}', '{"code":0,"request_id":"r9","data":"x"}'])
def test_code_zero_without_object_data_is_an_error(body):
    with pytest.raises(TikTokShopError) as ei:
        TikTokShopAuth("k", "s", transport=stub(200, body)).exchange_code("x")
    assert ei.value.request_id == "r9"
    with pytest.raises(TikTokShopError):
        asyncio.run(AsyncTikTokShopAuth("k", "s", transport=_async_stub(200, body)).refresh("x"))


def test_non_2xx_and_non_json():
    with pytest.raises(TikTokShopError) as ei:
        TikTokShopAuth("k", "s", transport=stub(502, "bad gateway")).exchange_code("x")
    assert ei.value.http_status == 502
    with pytest.raises(TikTokShopError) as ei:
        TikTokShopAuth("k", "s", transport=stub(500, '{"code":5,"message":"boom","request_id":"q"}')).refresh("x")
    assert (ei.value.http_status, ei.value.code, ei.value.message, ei.value.request_id) == (500, 5, "boom", "q")
    with pytest.raises(TikTokShopError):
        TikTokShopAuth("k", "s", transport=stub(200, "<html>")).exchange_code("x")


def test_network_errors_are_wrapped():
    def boom(request):
        raise httpx.ConnectError("refused")

    with pytest.raises(TikTokShopError) as ei:
        TikTokShopAuth("k", "s", transport=httpx.MockTransport(boom)).exchange_code("x")
    assert isinstance(ei.value.__cause__, httpx.ConnectError)

    async def aboom(request):
        raise httpx.ReadTimeout("slow")

    with pytest.raises(TikTokShopError, match="timed out"):
        asyncio.run(AsyncTikTokShopAuth("k", "s", transport=httpx.MockTransport(aboom)).exchange_code("x"))


def test_numeric_open_id_stays_exact():
    body = '{"code":0,"request_id":"r","data":{"access_token":"a","access_token_expire_in":1,"refresh_token":"r","refresh_token_expire_in":2,"open_id":7494049642642441621,"seller_name":"n","seller_base_region":"US","user_type":0}}'
    t = TikTokShopAuth("k", "s", transport=stub(200, body)).exchange_code("x")
    assert t.open_id == "7494049642642441621"


def test_missing_token_field_is_a_tiktokshop_error():
    with pytest.raises(TikTokShopError, match="access_token_expire_in"):
        TikTokShopAuth("k", "s", transport=stub(200, '{"code":0,"request_id":"q","data":{"access_token":"a"}}')).exchange_code("x")


MINIMAL_BODY = '{"code":0,"request_id":"r","data":{"access_token":"a","access_token_expire_in":1,"refresh_token":"r","refresh_token_expire_in":2}}'


def test_minimal_token_response_succeeds_with_optional_fields_none():
    for t in (
        TikTokShopAuth("k", "s", transport=stub(200, MINIMAL_BODY)).exchange_code("x"),
        asyncio.run(AsyncTikTokShopAuth("k", "s", transport=_async_stub(200, MINIMAL_BODY)).refresh("x")),
    ):
        assert (t.access_token, t.access_token_expire_in, t.refresh_token, t.refresh_token_expire_in) == ("a", 1, "r", 2)
        assert t.open_id is None
        assert t.seller_name is None
        assert t.seller_base_region is None
        assert t.user_type is None
        assert t.granted_scopes is None


@pytest.mark.parametrize("missing", ["access_token", "access_token_expire_in", "refresh_token", "refresh_token_expire_in"])
def test_each_required_token_field_is_enforced(missing):
    data = {"access_token": "a", "access_token_expire_in": 1, "refresh_token": "r", "refresh_token_expire_in": 2}
    del data[missing]
    body = json.dumps({"code": 0, "request_id": "q", "data": data})
    with pytest.raises(TikTokShopError, match=missing):
        TikTokShopAuth("k", "s", transport=stub(200, body)).exchange_code("x")


SECRETS = ("SECRET-app-secret-9f3", "SECRET-auth-code-7c1", "SECRET-refresh-tok-2b8")


def _chain_text(err: BaseException) -> str:
    parts, seen, stack = [], set(), [err]
    while stack:
        e = stack.pop()
        if e is None or id(e) in seen:
            continue
        seen.add(id(e))
        parts += [str(e), repr(e), repr(e.args)]
        stack += [e.__cause__, e.__context__]
    return "\n".join(parts)


def _free_port() -> int:
    import socket

    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def _calls(auth, aauth):
    return [
        lambda: auth.exchange_code(SECRETS[1]),
        lambda: auth.refresh(SECRETS[2]),
        lambda: asyncio.run(aauth.exchange_code(SECRETS[1])),
        lambda: asyncio.run(aauth.refresh(SECRETS[2])),
    ]


def test_errors_never_contain_secrets_closed_port():
    base = f"http://127.0.0.1:{_free_port()}"
    for call in _calls(TikTokShopAuth("k", SECRETS[0], base_url=base), AsyncTikTokShopAuth("k", SECRETS[0], base_url=base)):
        with pytest.raises(TikTokShopError) as ei:
            call()
        text = _chain_text(ei.value)
        assert "refused" in text.lower() or "connect" in text.lower()
        for secret in SECRETS:
            assert secret not in text


def test_errors_never_contain_secrets_timeout():
    def slow(request):
        raise httpx.ReadTimeout("timed out")

    async def aslow(request):
        raise httpx.ReadTimeout("timed out")

    auth = TikTokShopAuth("k", SECRETS[0], transport=httpx.MockTransport(slow))
    aauth = AsyncTikTokShopAuth("k", SECRETS[0], transport=httpx.MockTransport(aslow))
    for call in _calls(auth, aauth):
        with pytest.raises(TikTokShopError, match="timed out") as ei:
            call()
        text = _chain_text(ei.value)
        for secret in SECRETS:
            assert secret not in text
