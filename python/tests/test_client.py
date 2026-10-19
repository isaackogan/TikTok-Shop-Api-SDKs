import asyncio
import json
import socket
import threading
from urllib.parse import unquote

import httpx
import pytest

from tiktok_shop_api import AsyncTikTokShop, Signer, TikTokShop, TikTokShopError

OK = '{"code":0,"message":"Success","request_id":"r0","data":{}}'


class Stub:
    """An httpx.MockTransport handler that records requests and replies as told."""

    def __init__(self):
        self.seen: list[httpx.Request] = []
        self.status = 200
        self.body = OK

    def __call__(self, request: httpx.Request) -> httpx.Response:
        request.read()
        self.seen.append(request)
        return httpx.Response(self.status, content=self.body.encode(), headers={"content-type": "application/json"})

    @property
    def transport(self):
        return httpx.MockTransport(self)


def raw_query(req: httpx.Request) -> str:
    return req.url.raw_path.decode().partition("?")[2]


def decoded_query(req: httpx.Request) -> list[tuple[str, str]]:
    # %-decoding only: a literal "+" in the wire query is a plus, not a space
    out = []
    for p in raw_query(req).split("&"):
        k, _, v = p.partition("=")
        out.append((unquote(k), unquote(v)))
    return out


def q(req, key):
    return next((v for k, v in decoded_query(req) if k == key), None)


def check_signed(req: httpx.Request, secret="s1"):
    pairs = decoded_query(req)
    sent = next(v for k, v in pairs if k == "sign")
    rest = [(k, v) for k, v in pairs if k != "sign"]
    body = req.content or None
    assert sent == Signer.sign(
        path=req.url.path,
        query=rest,
        content_type=req.headers.get("content-type"),
        body=body,
        app_secret=secret,
    )


@pytest.fixture
def stub():
    return Stub()


def make(stub, **extra):
    kw = dict(app_key="k1", app_secret="s1", access_token="tok", shop_cipher="cipher1", transport=stub.transport)
    kw.update(extra)
    return TikTokShop(**kw)


def test_get_authorized_shops_signed_with_token_and_no_cipher(stub):
    make(stub).authorization.get_authorized_shops()
    r = stub.seen[0]
    assert r.url.path == "/authorization/202309/shops"
    assert r.url.host == "open-api.tiktokglobalshop.com"
    assert q(r, "app_key") == "k1"
    assert int(q(r, "timestamp")) > 1_700_000_000
    assert r.headers["x-tts-access-token"] == "tok"
    assert q(r, "shop_cipher") is None
    check_signed(r)


def test_get_order_list_sends_cipher_and_page_token_intact(stub):
    make(stub).orders.get_order_list(page_size=20, page_token="b2Zmc2V0PTEw+/x==")
    r = stub.seen[0]
    assert r.method == "POST"
    assert q(r, "shop_cipher") == "cipher1"
    assert q(r, "page_token") == "b2Zmc2V0PTEw+/x=="
    assert "%2B" in raw_query(r) and "+" not in raw_query(r)
    check_signed(r)


def test_space_in_a_value_is_percent_20_and_signed_decoded(stub):
    make(stub).orders.get_order_list(page_size=1, page_token="a b+c")
    r = stub.seen[0]
    assert "page_token=a%20b%2Bc" in raw_query(r)
    assert q(r, "page_token") == "a b+c"
    check_signed(r)


def test_json_body_is_signed(stub):
    from tiktok_shop_api.generated.models.get_order_list_request import GetOrderListRequest

    body = GetOrderListRequest.from_dict({"order_status": "UNPAID"})
    make(stub).orders.get_order_list(page_size=5, body=body)
    r = stub.seen[0]
    assert b"UNPAID" in r.content
    check_signed(r)


def test_no_token_header_without_access_token(stub):
    make(stub, access_token=None).authorization.get_authorized_shops()
    assert "x-tts-access-token" not in stub.seen[0].headers


def test_hook_drops_caller_supplied_reserved_params(stub):
    c = make(stub)
    c.authorization.get_authorized_shops()
    assert [k for k, _ in decoded_query(stub.seen[0])].count("app_key") == 1


def test_get_with_body_sends_body_and_signs_it(stub):
    from tiktok_shop_api.generated.models.get_conversation_list_request import GetConversationListRequest

    body = GetConversationListRequest.from_dict({"only_need_conversation_id": True})
    make(stub).affiliate_seller.get_conversation_list(page_size=10, body=body)
    r = stub.seen[0]
    assert r.method == "GET"
    assert r.url.path == "/affiliate_seller/202412/conversations"
    assert r.content == b'{"only_need_conversation_id":true}'
    assert r.headers["content-type"] == "application/json"
    assert q(r, "shop_cipher") == "cipher1"
    check_signed(r)


def test_code_not_zero_raises_with_http_200(stub):
    stub.body = '{"code":36009003,"message":"invalid","request_id":"r1","data":{}}'
    with pytest.raises(TikTokShopError) as e:
        make(stub).authorization.get_authorized_shops()
    assert e.value.code == 36009003
    assert e.value.message == "invalid"
    assert e.value.request_id == "r1"
    assert str(e.value) == "invalid"


def test_non_2xx_raises_with_http_status(stub):
    stub.status = 500
    stub.body = '{"code":1,"message":"boom","request_id":"r2"}'
    with pytest.raises(TikTokShopError) as e:
        make(stub).authorization.get_authorized_shops()
    assert (e.value.http_status, e.value.code, e.value.message, e.value.request_id) == (500, 1, "boom", "r2")


def test_non_2xx_without_envelope(stub):
    stub.status = 502
    stub.body = "<html>bad gateway</html>"
    with pytest.raises(TikTokShopError) as e:
        make(stub).authorization.get_authorized_shops()
    assert e.value.http_status == 502
    assert e.value.code == 502


def test_2xx_non_json_raises_with_cause(stub):
    stub.body = "<html>nope</html>"
    with pytest.raises(TikTokShopError) as e:
        make(stub).authorization.get_authorized_shops()
    assert e.value.http_status == 200
    assert e.value.__cause__ is not None


def test_success_returns_the_parsed_model(stub):
    stub.body = '{"code":0,"message":"Success","request_id":"r0","data":{"shops":[{"id":"7","name":"n"}]}}'
    res = make(stub).authorization.get_authorized_shops()
    assert res.request_id == "r0"
    assert res.data.shops[0].id == "7"


def _closed_port() -> int:
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def test_closed_port_raises_with_cause():
    c = TikTokShop(app_key="k", app_secret="s", base_url=f"http://127.0.0.1:{_closed_port()}")
    with pytest.raises(TikTokShopError) as e:
        c.authorization.get_authorized_shops()
    assert e.value.__cause__ is not None
    assert e.value.http_status is None


class Silent:
    """A TCP server that accepts connections and never answers."""

    def __enter__(self):
        self.sock = socket.socket()
        self.sock.bind(("127.0.0.1", 0))
        self.sock.listen(5)
        self.port = self.sock.getsockname()[1]
        self.conns = []
        self.t = threading.Thread(target=self._run, daemon=True)
        self.t.start()
        return self

    def _run(self):
        try:
            while True:
                c, _ = self.sock.accept()
                self.conns.append(c)
        except OSError:
            pass

    def __exit__(self, *a):
        self.sock.close()
        for c in self.conns:
            c.close()


def test_timeout_raises():
    with Silent() as srv:
        c = TikTokShop(app_key="k", app_secret="s", base_url=f"http://127.0.0.1:{srv.port}", timeout=0.2)
        with pytest.raises(TikTokShopError) as e:
            c.authorization.get_authorized_shops()
    assert "timed out" in e.value.message
    assert isinstance(e.value.__cause__, httpx.TimeoutException)


def test_with_shop_does_not_touch_the_original(stub):
    a = make(stub)
    b = a.with_shop(access_token="tok2", shop_cipher="cipher2")
    b.orders.get_order_list(page_size=1)
    a.orders.get_order_list(page_size=1)
    assert stub.seen[0].headers["x-tts-access-token"] == "tok2"
    assert q(stub.seen[0], "shop_cipher") == "cipher2"
    assert stub.seen[1].headers["x-tts-access-token"] == "tok"
    assert q(stub.seen[1], "shop_cipher") == "cipher1"
    check_signed(stub.seen[0])


def test_with_shop_keeps_unspecified_values(stub):
    b = make(stub).with_shop(shop_cipher="c9")
    b.orders.get_order_list(page_size=1)
    assert stub.seen[0].headers["x-tts-access-token"] == "tok"


def test_closing_a_child_leaves_the_parent_usable(stub):
    a = make(stub)
    b = a.with_shop(shop_cipher="c9")
    b.close()
    a.authorization.get_authorized_shops()
    assert len(stub.seen) == 1


def test_context_manager(stub):
    with make(stub) as c:
        c.authorization.get_authorized_shops()
    assert len(stub.seen) == 1


# ---- async ----------------------------------------------------------------------------------


def amake(stub, **extra):
    kw = dict(app_key="k1", app_secret="s1", access_token="tok", shop_cipher="cipher1", transport=stub.transport)
    kw.update(extra)
    return AsyncTikTokShop(**kw)


def test_async_signed_request_and_page_token(stub):
    async def go():
        async with amake(stub) as c:
            await c.orders.get_order_list(page_size=2, page_token="b2Zmc2V0PTEw+/x==")

    asyncio.run(go())
    r = stub.seen[0]
    assert q(r, "page_token") == "b2Zmc2V0PTEw+/x=="
    assert q(r, "shop_cipher") == "cipher1"
    assert r.headers["x-tts-access-token"] == "tok"
    check_signed(r)


def test_async_get_with_body(stub):
    from tiktok_shop_api.generated.models.get_conversation_list_request import GetConversationListRequest

    body = GetConversationListRequest.from_dict({"only_need_conversation_id": True})

    async def go():
        await amake(stub).affiliate_seller.get_conversation_list(page_size=10, body=body)

    asyncio.run(go())
    r = stub.seen[0]
    assert r.method == "GET" and r.content == b'{"only_need_conversation_id":true}'
    check_signed(r)


def test_async_code_not_zero(stub):
    stub.body = '{"code":36009003,"message":"invalid","request_id":"r1","data":{}}'

    async def go():
        await amake(stub).authorization.get_authorized_shops()

    with pytest.raises(TikTokShopError) as e:
        asyncio.run(go())
    assert (e.value.code, e.value.request_id) == (36009003, "r1")


def test_async_non_2xx_and_non_json(stub):
    async def go():
        await amake(stub).authorization.get_authorized_shops()

    stub.status, stub.body = 500, '{"code":1,"message":"boom","request_id":"r2"}'
    with pytest.raises(TikTokShopError) as e:
        asyncio.run(go())
    assert e.value.http_status == 500
    stub.status, stub.body = 200, "nope"
    with pytest.raises(TikTokShopError) as e:
        asyncio.run(go())
    assert e.value.__cause__ is not None


def test_async_network_error_and_timeout():
    async def go(url, **kw):
        await AsyncTikTokShop(app_key="k", app_secret="s", base_url=url, **kw).authorization.get_authorized_shops()

    with pytest.raises(TikTokShopError) as e:
        asyncio.run(go(f"http://127.0.0.1:{_closed_port()}"))
    assert e.value.__cause__ is not None
    with Silent() as srv:
        with pytest.raises(TikTokShopError) as e:
            asyncio.run(go(f"http://127.0.0.1:{srv.port}", timeout=0.2))
    assert "timed out" in e.value.message


def test_async_with_shop(stub):
    async def go():
        a = amake(stub)
        b = a.with_shop(access_token="tok2", shop_cipher="cipher2")
        await b.orders.get_order_list(page_size=1)
        await a.orders.get_order_list(page_size=1)

    asyncio.run(go())
    assert stub.seen[0].headers["x-tts-access-token"] == "tok2"
    assert stub.seen[1].headers["x-tts-access-token"] == "tok"
    assert q(stub.seen[1], "shop_cipher") == "cipher1"
