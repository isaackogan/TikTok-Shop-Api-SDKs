import json
from pathlib import Path

from tiktok_shop_api import AsyncTikTokShop, TikTokShop
from tiktok_shop_api.generated._meta import OPERATIONS


def snake(name: str) -> str:
    import re

    return re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", name.replace("TikTok", "Tiktok")).lower()


def test_every_operation_is_reachable_sync_and_async():
    import inspect

    from openapi_python_client.strings import snake_case

    sync = TikTokShop(app_key="k", app_secret="s")
    asyn = AsyncTikTokShop(app_key="k", app_secret="s")
    assert len(OPERATIONS) == 320
    for op in OPERATIONS:
        name = snake_case(op["operationId"])
        for client in (sync, asyn):
            fn = getattr(getattr(client, snake(op["group"])), name, None)
            assert callable(fn), f"{op['group']}.{op['operationId']}"
        assert not inspect.iscoroutinefunction(getattr(getattr(sync, snake(op["group"])), name))
        assert inspect.iscoroutinefunction(getattr(getattr(asyn, snake(op["group"])), name))


def test_groups_match_shared_api_groups():
    groups = json.loads((Path(__file__).resolve().parents[2] / "shared/api-groups.json").read_text())
    c = TikTokShop(app_key="k", app_secret="s")
    for camel in groups.values():
        assert hasattr(c, snake(camel)), camel


def test_python_group_names():
    expected = [
        "affiliate_creator", "affiliate_partner", "affiliate_seller", "analytics", "authorization",
        "customer_engagement", "customer_service", "event", "finance", "fulfilled_by_tiktok", "fulfillment",
        "logistics", "orders", "products", "promotion", "return_and_refund", "seller", "supply_chain", "tools",
    ]
    from tiktok_shop_api.generated._groups import ASYNC_GROUPS, SYNC_GROUPS

    assert sorted(SYNC_GROUPS) == sorted(expected) == sorted(ASYNC_GROUPS)
    c = TikTokShop(app_key="k", app_secret="s")
    for name in expected:
        assert hasattr(c, name), name
