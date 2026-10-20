"""Cross-language rules from the final review: R13c, R13d, lesson 34, I5 and the minors that align Python with the
other seven SDKs."""

import asyncio
import json
import logging
import socket
import threading
import tomllib
from pathlib import Path

import httpx
import pytest

from tiktok_shop_api import AsyncTikTokShop, AsyncTikTokShopAuth, TikTokShop, TikTokShopAuth, TikTokShopError
from tiktok_shop_api.generated.models import PredictProductPackageDimensionsAndWeightRequest

USER_AGENT = "tiktok-shop-api-python/" + tomllib.loads((Path(__file__).parents[1] / "pyproject.toml").read_text())["project"]["version"]
TOKEN_DATA = {"access_token": "a", "access_token_expire_in": 1, "refresh_token": "r", "refresh_token_expire_in": 2}


def _closed_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


class Silent:
    """A TCP server that accepts connections and never answers."""

    def __enter__(self):
        self.sock = socket.socket()
        self.sock.bind(("127.0.0.1", 0))
        self.sock.listen(5)
        self.url = f"http://127.0.0.1:{self.sock.getsockname()[1]}"
        self.conns = []
        threading.Thread(target=self._run, daemon=True).start()
        return self

    def _run(self):
        try:
            while True:
                self.conns.append(self.sock.accept()[0])
        except OSError:
            pass

    def __exit__(self, *a):
        self.sock.close()
        for c in self.conns:
            c.close()


class Reply:
    """A MockTransport handler that replies with a fixed status and body, recording requests."""

    def __init__(self, body: str, status: int = 200):
        self.body, self.status, self.seen = body, status, []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        request.read()
        self.seen.append(request)
        return httpx.Response(self.status, content=self.body.encode(), headers={"content-type": "application/json"})

    @property
    def transport(self):
        return httpx.MockTransport(self)


def assert_transport_error(e: TikTokShopError):
    assert e.code == -1
    assert e.http_status is None
    assert e.__cause__ is not None


# --- R13c: a transport failure is code -1 with no http_status, on API and token calls --------------------------------


def test_api_closed_port_is_minus_one():
    c = TikTokShop(app_key="k", app_secret="s", base_url=f"http://127.0.0.1:{_closed_port()}")
    with pytest.raises(TikTokShopError) as e:
        c.authorization.get_authorized_shops()
    assert_transport_error(e.value)


def test_api_timeout_is_minus_one():
    with Silent() as srv:
        c = TikTokShop(app_key="k", app_secret="s", base_url=srv.url, timeout=0.2)
        with pytest.raises(TikTokShopError) as e:
            c.authorization.get_authorized_shops()
    assert_transport_error(e.value)
    assert "timed out" in e.value.message


def test_async_api_closed_port_and_timeout_are_minus_one():
    async def go(url, **kw):
        await AsyncTikTokShop(app_key="k", app_secret="s", base_url=url, **kw).authorization.get_authorized_shops()

    with pytest.raises(TikTokShopError) as e:
        asyncio.run(go(f"http://127.0.0.1:{_closed_port()}"))
    assert_transport_error(e.value)
    with Silent() as srv:
        with pytest.raises(TikTokShopError) as e:
            asyncio.run(go(srv.url, timeout=0.2))
    assert_transport_error(e.value)


def _token_calls(base_url: str, **kw):
    auth = TikTokShopAuth("k", "s", base_url=base_url, **kw)
    aauth = AsyncTikTokShopAuth("k", "s", base_url=base_url, **kw)
    return [
        lambda: auth.exchange_code("c"),
        lambda: auth.refresh("r"),
        lambda: asyncio.run(aauth.exchange_code("c")),
        lambda: asyncio.run(aauth.refresh("r")),
    ]


def test_token_closed_port_is_minus_one():
    for call in _token_calls(f"http://127.0.0.1:{_closed_port()}"):
        with pytest.raises(TikTokShopError) as e:
            call()
        assert_transport_error(e.value)


def test_token_timeout_is_minus_one():
    with Silent() as srv:
        for call in _token_calls(srv.url, timeout=0.2):
            with pytest.raises(TikTokShopError) as e:
                call()
            assert_transport_error(e.value)
            assert "timed out" in e.value.message


# --- R13d: a 2xx envelope that does not fit its model is code -1 with http_status and request_id -----------------------


def test_decode_failure_is_minus_one_with_status_and_request_id():
    stub = Reply('{"code":0,"message":"Success","request_id":"q9","data":{"shops":"not a list"}}')
    c = TikTokShop(app_key="k", app_secret="s", transport=stub.transport)
    with pytest.raises(TikTokShopError) as e:
        c.authorization.get_authorized_shops()
    assert (e.value.code, e.value.http_status, e.value.request_id) == (-1, 200, "q9")
    assert e.value.__cause__ is not None


def test_async_decode_failure_is_minus_one():
    stub = Reply('{"code":0,"request_id":"q10","data":{"shops":[{"id":{"nested":1}, "name": []}], "x": 1}}')

    async def handler(request):
        return stub(request)

    async def go():
        await AsyncTikTokShop(app_key="k", app_secret="s", transport=httpx.MockTransport(handler)).products.predict_product_package_dimensions_and_weight(
            body=PredictProductPackageDimensionsAndWeightRequest(category_id="1")
        )

    stub.body = '{"code":0,"request_id":"q10","data":{"package_weight":{"unit":"GRAM"}}}'
    with pytest.raises(TikTokShopError) as e:
        asyncio.run(go())
    assert (e.value.code, e.value.http_status, e.value.request_id) == (-1, 200, "q10")


# --- R12: unknown response fields decode ------------------------------------------------------------------------------


def test_unknown_fields_at_data_level_and_in_a_nested_model_with_required_properties():
    stub = Reply(
        '{"code":0,"request_id":"r","data":{"brand_new":1,'
        '"package_weight":{"unit":"GRAM","value":"5","future":[1]},"package_dimensions":{"height":"1","length":"2","unit":"CM","width":"3","x":{}}}}'
    )
    c = TikTokShop(app_key="k", app_secret="s", transport=stub.transport)
    res = c.products.predict_product_package_dimensions_and_weight(body=PredictProductPackageDimensionsAndWeightRequest(category_id="1"))
    assert res is not None
    assert res.data.package_weight.value == "5"
    assert res.data.package_dimensions.width == "3"


# --- M1: timeout=0 means no limit -------------------------------------------------------------------------------------


def test_zero_timeout_means_no_limit():
    assert TikTokShop(app_key="k", app_secret="s", timeout=0)._client.get_httpx_client().timeout == httpx.Timeout(None)
    assert AsyncTikTokShop(app_key="k", app_secret="s", timeout=0)._client.get_async_httpx_client().timeout == httpx.Timeout(None)
    stub = Reply(json.dumps({"code": 0, "request_id": "r", "data": TOKEN_DATA}))
    # A zero-second limit would fail every call; no limit succeeds.
    assert TikTokShopAuth("k", "s", timeout=0, transport=stub.transport).exchange_code("c").access_token == "a"
    assert TikTokShopAuth("k", "s", timeout=0)._timeout == httpx.Timeout(None)
    assert AsyncTikTokShopAuth("k", "s", timeout=0)._timeout == httpx.Timeout(None)
    assert TikTokShop(app_key="k", app_secret="s")._client.get_httpx_client().timeout == httpx.Timeout(30.0)


# --- M2: a 2xx envelope error on a token call carries http_status 200 --------------------------------------------------


@pytest.mark.parametrize(
    "body",
    [
        '{"code":36004004,"message":"bad","request_id":"q2"}',
        '{"code":0,"request_id":"q2"}',
        json.dumps({"code": 0, "request_id": "q2", "data": {**TOKEN_DATA, "access_token": ""}}),
    ],
)
def test_token_2xx_errors_carry_http_status(body):
    with pytest.raises(TikTokShopError) as e:
        TikTokShopAuth("k", "s", transport=Reply(body).transport).exchange_code("c")
    assert (e.value.http_status, e.value.request_id) == (200, "q2")


# --- M20 (lesson 34): a 2xx whose code is present but not an integer is -1 ---------------------------------------------


@pytest.mark.parametrize("code", ['"0"', "1.5", "true", "null", "{}"])
def test_non_integer_code_on_a_2xx_is_minus_one(code):
    stub = Reply(f'{{"code":{code},"message":"m","request_id":"q5","data":{{}}}}')
    with pytest.raises(TikTokShopError) as e:
        TikTokShop(app_key="k", app_secret="s", transport=stub.transport).authorization.get_authorized_shops()
    assert (e.value.code, e.value.http_status, e.value.request_id) == (-1, 200, "q5")
    token = Reply(json.dumps({"code": json.loads(code), "request_id": "q6", "data": TOKEN_DATA}))
    with pytest.raises(TikTokShopError) as e:
        TikTokShopAuth("k", "s", transport=token.transport).exchange_code("c")
    assert (e.value.code, e.value.http_status) == (-1, 200)


def test_a_2xx_without_a_code_is_still_a_success():
    stub = Reply('{"request_id":"q","data":{}}')
    assert TikTokShop(app_key="k", app_secret="s", transport=stub.transport).authorization.get_authorized_shops() is not None


# --- M18 (lesson 34): User-Agent ---------------------------------------------------------------------------------------


def test_user_agent_on_api_and_token_calls():
    from tiktok_shop_api import USER_AGENT as exported

    assert exported == USER_AGENT
    stub = Reply('{"code":0,"request_id":"r","data":{}}')
    TikTokShop(app_key="k", app_secret="s", transport=stub.transport).authorization.get_authorized_shops()
    TikTokShop(app_key="k", app_secret="s", transport=stub.transport).with_shop(shop_cipher="c").authorization.get_authorized_shops()
    token = Reply(json.dumps({"code": 0, "request_id": "r", "data": TOKEN_DATA}))
    TikTokShopAuth("k", "s", transport=token.transport).exchange_code("c")
    assert [r.headers["user-agent"] for r in stub.seen + token.seen] == [USER_AGENT] * 3

    async def go():
        a = Reply('{"code":0,"request_id":"r","data":{}}')

        async def h(request):
            return a(request)

        await AsyncTikTokShop(app_key="k", app_secret="s", transport=httpx.MockTransport(h)).authorization.get_authorized_shops()
        return a.seen[0].headers["user-agent"]

    assert asyncio.run(go()) == USER_AGENT


# --- M19 (lesson 34): an empty state is omitted ------------------------------------------------------------------------


def test_empty_state_is_omitted():
    a = TikTokShopAuth("ak", "s", service_id="svc")
    assert a.authorization_url(type="seller", region="us", state="") == "https://services.us.tiktokshop.com/open/authorize?service_id=svc"
    assert a.authorization_url(type="creator", region="row", state="") == "https://shop.tiktok.com/alliance/creator/auth?app_key=ak"


# --- M3: wrong-typed optional token fields are absent ------------------------------------------------------------------


def test_wrong_typed_optional_token_fields_are_none():
    data = {**TOKEN_DATA, "open_id": True, "seller_name": 5, "seller_base_region": ["US"], "user_type": "x", "granted_scopes": "scope"}
    t = TikTokShopAuth("k", "s", transport=Reply(json.dumps({"code": 0, "request_id": "q", "data": data})).transport).exchange_code("c")
    assert (t.open_id, t.seller_name, t.seller_base_region, t.user_type, t.granted_scopes) == (None, None, None, None, None)
    data = {**TOKEN_DATA, "granted_scopes": ["a", 1], "user_type": True}
    t = TikTokShopAuth("k", "s", transport=Reply(json.dumps({"code": 0, "request_id": "q", "data": data})).transport).exchange_code("c")
    assert (t.granted_scopes, t.user_type) == (None, None)


def test_well_typed_optional_token_fields_are_kept():
    body = '{"code":0,"request_id":"q","data":{"access_token":"a","access_token_expire_in":1,"refresh_token":"r","refresh_token_expire_in":2,"open_id":7010736057180325637,"seller_name":"S","seller_base_region":"US","user_type":0,"granted_scopes":["x"]}}'
    t = TikTokShopAuth("k", "s", transport=Reply(body).transport).exchange_code("c")
    assert (t.open_id, t.seller_name, t.seller_base_region, t.user_type, t.granted_scopes) == ("7010736057180325637", "S", "US", 0, ["x"])


# --- I5: httpx's INFO request log never carries the token-call secrets -------------------------------------------------

SECRETS = ("SECRET-app-secret-9f3", "SECRET-auth-code-7c1", "SECRET-refresh-tok-2b8")


def test_httpx_info_log_redacts_token_secrets(caplog):
    caplog.set_level(logging.INFO)
    body = json.dumps({"code": 0, "request_id": "r", "data": TOKEN_DATA})
    auth = TikTokShopAuth("k", SECRETS[0], transport=Reply(body).transport)
    auth.exchange_code(SECRETS[1])
    auth.refresh(SECRETS[2])

    async def handler(request):
        return Reply(body)(request)

    aauth = AsyncTikTokShopAuth("k", SECRETS[0], transport=httpx.MockTransport(handler))
    asyncio.run(aauth.exchange_code(SECRETS[1]))
    asyncio.run(aauth.refresh(SECRETS[2]))
    lines = [r.getMessage() for r in caplog.records if r.name == "httpx"]
    assert len(lines) == 4, lines
    text = "\n".join(lines) + "\n" + caplog.text
    for secret in SECRETS:
        assert secret not in text
    assert "app_secret=***" in lines[0] and "auth_code=***" in lines[0]
    assert "refresh_token=***" in lines[1]
    assert "app_key=k" in lines[0]  # only the secret values are redacted


# --- R21b: an integer enum value the spec does not list still decodes ---------------------------------------------------


def test_unlisted_integer_enum_value_decodes():
    stub = Reply('{"code":0,"request_id":"r","data":{"creators":[{"creator_profile":{"user_type_tag":[1,3]}}]}}')
    res = TikTokShop(app_key="k", app_secret="s", transport=stub.transport).affiliate_seller.search_creators_in_creator_marketplace(page_size=1)
    assert res is not None
    assert res.to_dict()["data"]["creators"][0]["creator_profile"]["user_type_tag"] == [1, 3]
