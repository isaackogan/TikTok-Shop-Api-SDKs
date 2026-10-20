"""Secrets stay out of repr, redirects are never followed, and R13a: a failure without a TikTok code uses the HTTP status."""

import asyncio
import dataclasses
import json

import httpx
import pytest

from tiktok_shop_api import AsyncTikTokShop, AsyncTikTokShopAuth, TikTokShop, TikTokShopAuth, TikTokShopError, TokenSet
from tiktok_shop_api.client import _Credentials

SECRET = "super-secret-value"
TOKEN = "tok-value-xyz"
CIPHER = "cipher-value-xyz"
REFRESH = "refresh-value-xyz"
SECRETS = (SECRET, TOKEN, CIPHER, REFRESH)


def assert_redacted(obj, *visible):
    for text in (repr(obj), str(obj), f"{obj!r:>1}"):
        for s in SECRETS:
            assert s not in text, f"{type(obj).__name__} leaked {s}: {text}"
        for v in visible:
            assert v in text, f"{type(obj).__name__} should show {v}: {text}"


def test_clients_and_credentials_never_repr_secrets():
    client = TikTokShop("appkey1", SECRET, TOKEN, CIPHER)
    assert_redacted(client, "appkey1")
    assert_redacted(client.with_shop(access_token=TOKEN, shop_cipher=CIPHER), "appkey1")
    assert_redacted(client._creds, "appkey1")
    assert_redacted(AsyncTikTokShop("appkey1", SECRET, TOKEN, CIPHER), "appkey1")


def test_auth_helpers_never_repr_the_secret():
    assert_redacted(TikTokShopAuth("appkey1", SECRET, "svc1"), "appkey1")
    assert_redacted(AsyncTikTokShopAuth("appkey1", SECRET, "svc1"), "appkey1")


def test_token_set_repr_hides_tokens_but_asdict_keeps_them():
    ts = TokenSet(TOKEN, 1, REFRESH, 2, open_id="open1", seller_name="shop")
    assert_redacted(ts, "open1")
    d = dataclasses.asdict(ts)
    assert d["access_token"] == TOKEN and d["refresh_token"] == REFRESH
    assert TokenSet(**d) == ts
    assert json.loads(json.dumps(d))["refresh_token"] == REFRESH


# --- redirects -------------------------------------------------------------------------------


class Redirector:
    def __init__(self):
        self.seen: list[httpx.Request] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        request.read()
        self.seen.append(request)
        if request.url.host == "evil.example":
            return httpx.Response(200, json={"code": 0, "message": "Success", "request_id": "r", "data": {}})
        return httpx.Response(302, headers={"location": "https://evil.example/stolen"})


def test_api_redirect_is_not_followed_and_surfaces_as_the_status():
    r = Redirector()
    client = TikTokShop("k", "s", "tok", transport=httpx.MockTransport(r))
    with pytest.raises(TikTokShopError) as e:
        client.authorization.get_authorized_shops()
    assert e.value.code == 302 and e.value.http_status == 302
    assert [x.url.host for x in r.seen] == ["open-api.tiktokglobalshop.com"], "the redirect target got a request"


def test_async_api_redirect_is_not_followed():
    r = Redirector()

    async def go():
        async with AsyncTikTokShop("k", "s", "tok", transport=httpx.MockTransport(r)) as client:
            await client.authorization.get_authorized_shops()

    with pytest.raises(TikTokShopError) as e:
        asyncio.run(go())
    assert e.value.code == 302 and e.value.http_status == 302
    assert len(r.seen) == 1


def test_token_redirect_is_not_followed_and_surfaces_as_the_status():
    r = Redirector()
    with pytest.raises(TikTokShopError) as e:
        TikTokShopAuth("k", "s", transport=httpx.MockTransport(r)).exchange_code("c")
    assert e.value.code == 302 and e.value.http_status == 302
    assert [x.url.host for x in r.seen] == ["auth.tiktok-shops.com"]

    r2 = Redirector()
    with pytest.raises(TikTokShopError) as e2:
        asyncio.run(AsyncTikTokShopAuth("k", "s", transport=httpx.MockTransport(r2)).refresh("r"))
    assert e2.value.code == 302 and len(r2.seen) == 1


# --- R13a ------------------------------------------------------------------------------------


@pytest.mark.parametrize("body", ['{"message":"x"}', '{"code":0}'])
def test_api_non_2xx_without_a_code_uses_the_http_status(body):
    transport = httpx.MockTransport(lambda req: httpx.Response(503, content=body.encode(), headers={"content-type": "application/json"}))
    with pytest.raises(TikTokShopError) as e:
        TikTokShop("k", "s", transport=transport).authorization.get_authorized_shops()
    assert e.value.code == 503 and e.value.http_status == 503


@pytest.mark.parametrize("body", ['{"message":"x"}', '{"code":0}'])
def test_token_non_2xx_without_a_code_uses_the_http_status(body):
    transport = httpx.MockTransport(lambda req: httpx.Response(503, content=body.encode(), headers={"content-type": "application/json"}))
    with pytest.raises(TikTokShopError) as e:
        TikTokShopAuth("k", "s", transport=transport).refresh("r")
    assert e.value.code == 503 and e.value.http_status == 503
    with pytest.raises(TikTokShopError) as e2:
        asyncio.run(AsyncTikTokShopAuth("k", "s", transport=transport).exchange_code("c"))
    assert e2.value.code == 503 and e2.value.http_status == 503


# R13b: a non-2xx has TikTok's non-zero code if the body has one, else the HTTP status; -1 only for an unreadable 2xx.
R13B = [
    (503, '{"message":"x"}', 503),
    (503, '{"code":0}', 503),
    (503, "down", 503),
    (503, "", 503),
    (503, "[1]", 503),
    (302, "", 302),
    (503, '{"code":12345,"message":"m"}', 12345),
    (200, "<html>", -1),
    (200, "[1]", -1),
]


@pytest.mark.parametrize("status,body,want", R13B)
def test_r13b_api_codes(status, body, want):
    transport = httpx.MockTransport(lambda req: httpx.Response(status, content=body.encode()))
    with pytest.raises(TikTokShopError) as e:
        TikTokShop("k", "s", transport=transport).authorization.get_authorized_shops()
    assert (e.value.code, e.value.http_status) == (want, status)
    with pytest.raises(TikTokShopError) as e2:
        async def go():
            async with AsyncTikTokShop("k", "s", transport=httpx.MockTransport(lambda req: httpx.Response(status, content=body.encode()))) as c:
                await c.authorization.get_authorized_shops()
        asyncio.run(go())
    assert (e2.value.code, e2.value.http_status) == (want, status)


@pytest.mark.parametrize("status,body,want", R13B)
def test_r13b_token_codes(status, body, want):
    transport = httpx.MockTransport(lambda req: httpx.Response(status, content=body.encode()))
    with pytest.raises(TikTokShopError) as e:
        TikTokShopAuth("k", "s", transport=transport).refresh("r")
    assert (e.value.code, e.value.http_status) == (want, status)
    with pytest.raises(TikTokShopError) as e2:
        asyncio.run(AsyncTikTokShopAuth("k", "s", transport=transport).exchange_code("c"))
    assert (e2.value.code, e2.value.http_status) == (want, status)


def test_token_code_zero_without_data_on_a_2xx_is_minus_one():
    transport = httpx.MockTransport(lambda req: httpx.Response(200, json={"code": 0, "request_id": "r"}))
    with pytest.raises(TikTokShopError) as e:
        TikTokShopAuth("k", "s", transport=transport).refresh("r")
    assert e.value.code == -1
