import json
from pathlib import Path

import pytest

from tiktok_shop_api import EVENT_TYPES, UnknownWebhookEvent, WebhookSignatureError, Webhooks
from tiktok_shop_api.generated.models import OrderStatusChangeWebhook

VECTORS = json.loads((Path(__file__).parents[2] / "shared/test-vectors/webhooks.json").read_text())


@pytest.mark.parametrize("c", VECTORS["verify"], ids=lambda c: c["name"])
def test_verify(c):
    kw = dict(app_key=c["appKey"], app_secret=c["appSecret"], signature=c["signature"])
    assert Webhooks.verify(raw_body=c["rawBody"], **kw) is c["valid"]
    assert Webhooks.verify(raw_body=c["rawBody"].encode(), **kw) is c["valid"]
    if c["valid"]:
        assert Webhooks.verify_and_parse(raw_body=c["rawBody"], **kw)
    else:
        with pytest.raises(WebhookSignatureError):
            Webhooks.verify_and_parse(raw_body=c["rawBody"], **kw)


def test_verify_uses_raw_bytes_not_text():
    import hashlib
    import hmac

    body = b'{"type":1,"x":"\xff"}'  # not valid UTF-8
    sig = hmac.new(b"sec", b"key" + body, hashlib.sha256).hexdigest()
    assert Webhooks.verify(app_key="key", app_secret="sec", raw_body=body, signature=sig)


@pytest.mark.parametrize("c", VECTORS["parse"], ids=lambda c: c["name"])
def test_parse(c):
    for body in (c["rawBody"], c["rawBody"].encode()):
        ev = Webhooks.parse(body)
        if c["known"]:
            assert type(ev).__name__ == c["schema"]
            assert isinstance(ev, OrderStatusChangeWebhook)
            assert ev.type_ == c["type"]
        else:
            assert isinstance(ev, UnknownWebhookEvent)
            assert ev.type == c["type"]
            assert ev.raw == json.loads(c["rawBody"])


def test_numeric_shop_id_is_exact():
    ev = Webhooks.parse('{"type":1,"shop_id":7494049642642441621,"data":{"order_id":"1"}}')
    assert isinstance(ev, OrderStatusChangeWebhook)
    assert ev.shop_id == 7494049642642441621
    unk = Webhooks.parse('{"type":424242,"shop_id":7494049642642441621}')
    assert isinstance(unk, UnknownWebhookEvent) and unk.raw["shop_id"] == 7494049642642441621


def test_event_types():
    assert len(EVENT_TYPES) == 16
    assert EVENT_TYPES[1] == "ORDER_STATUS_CHANGE"
    assert Webhooks.EVENT_TYPES is EVENT_TYPES


def test_every_known_type_resolves_to_a_model():
    from tiktok_shop_api.generated._meta import WEBHOOKS
    from tiktok_shop_api.webhooks import _model

    assert len(WEBHOOKS) == 44
    for w in WEBHOOKS:
        assert _model(w["schema"]).__name__ == w["schema"]


def test_known_type_with_missing_required_fields_raises_value_error():
    # AppealCompletedWebhook requires shop_id; the generated model's KeyError must not leak
    t = next(w["type"] for w in __import__("tiktok_shop_api.generated._meta", fromlist=["x"]).WEBHOOKS if w["schema"] == "AppealCompletedWebhook")
    with pytest.raises(ValueError, match="AppealCompletedWebhook"):
        Webhooks.parse(json.dumps({"type": t}))


def test_malformed_body_raises_value_error():
    with pytest.raises(ValueError):
        Webhooks.parse("not json")
    with pytest.raises(ValueError):
        Webhooks.parse("[1]")
