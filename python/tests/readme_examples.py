# pyright: reportUnnecessaryTypeIgnoreComment=true
# Type-checked copy of the README's code: every README line (imports included) appears here verbatim,
# one function per README block. `tests/test_readme.py` fails if the two drift apart; pyright checks this file.
from typing import assert_type

from tiktok_shop_api import UnknownWebhookEvent, WebhookEvent, Webhooks
from tiktok_shop_api.generated.models import OrderStatusChangeWebhook


def block_oauth() -> None:
    import os

    from tiktok_shop_api import TikTokShopAuth

    code_from_redirect = "the ?code= value from your redirect URL"

    auth = TikTokShopAuth(
        os.environ["TTS_APP_KEY"],
        os.environ["TTS_APP_SECRET"],
        service_id=os.environ["TTS_SERVICE_ID"],  # seller and partner flows
    )

    # 1. Send the seller here. `type` is "seller", "partner" or "creator"; `region` is "us" or "row".
    url = auth.authorization_url(type="seller", region="us", state="csrf-token")

    # 2. TikTok redirects back with ?code=...; exchange it.
    tokens = auth.exchange_code(code_from_redirect)
    # tokens.access_token, tokens.refresh_token, tokens.open_id, tokens.granted_scopes, ...

    # 3. Before the access token expires (access_token_expire_in is a Unix timestamp):
    renewed = auth.refresh(tokens.refresh_token)


def block_first_call() -> None:
    import os

    from tiktok_shop_api import TikTokShop

    access_token = os.environ["TTS_ACCESS_TOKEN"]

    with TikTokShop(os.environ["TTS_APP_KEY"], os.environ["TTS_APP_SECRET"], access_token=access_token) as client:
        # Find the shop cipher
        shops = client.authorization.get_authorized_shops()
        assert shops is not None
        shop_cipher = shops.to_dict()["data"]["shops"][0]["cipher"]

        seller = client.with_shop(access_token=access_token, shop_cipher=shop_cipher)
        orders = seller.orders.get_order_list(page_size=20)


def block_async() -> None:
    import asyncio
    import os

    from tiktok_shop_api import AsyncTikTokShop

    access_token = os.environ["TTS_ACCESS_TOKEN"]

    async def main() -> None:
        async with AsyncTikTokShop(os.environ["TTS_APP_KEY"], os.environ["TTS_APP_SECRET"], access_token=access_token) as client:
            shops = await client.authorization.get_authorized_shops()
            assert shops is not None
            seller = client.with_shop(shop_cipher=shops.to_dict()["data"]["shops"][0]["cipher"])
            orders = await seller.orders.get_order_list(page_size=20)

    asyncio.run(main())


def block_many_shops() -> None:
    import os

    from tiktok_shop_api import TikTokShop

    client = TikTokShop(os.environ["TTS_APP_KEY"], os.environ["TTS_APP_SECRET"])
    token_a, cipher_a = os.environ["TOKEN_A"], os.environ["CIPHER_A"]
    token_b, cipher_b = os.environ["TOKEN_B"], os.environ["CIPHER_B"]

    shop_a = client.with_shop(access_token=token_a, shop_cipher=cipher_a)
    shop_b = client.with_shop(access_token=token_b, shop_cipher=cipher_b)


def block_webhooks() -> None:
    import os

    from flask import Flask, request

    from tiktok_shop_api import UnknownWebhookEvent, WebhookSignatureError, Webhooks
    from tiktok_shop_api.generated.models import OrderStatusChangeWebhook

    app = Flask(__name__)

    @app.post("/webhooks/tiktok-shop")
    def tiktok_shop_webhook():
        try:
            event = Webhooks.verify_and_parse(
                app_key=os.environ["TTS_APP_KEY"],
                app_secret=os.environ["TTS_APP_SECRET"],
                raw_body=request.get_data(),  # exactly as received
                signature=request.headers.get("Authorization", ""),
            )
        except WebhookSignatureError:
            return "", 401
        except ValueError:  # not a webhook this SDK can read
            return "", 400
        if isinstance(event, UnknownWebhookEvent):
            print("unknown webhook type", event.type, event.raw)
        elif isinstance(event, OrderStatusChangeWebhook):
            print(event.shop_id, event.data)
        return "", 200


def narrowing(body: bytes) -> None:
    """Not in the README: proves `parse` is typed, so `isinstance` narrows and unnarrowed use is an error."""
    event = Webhooks.parse(body)
    assert_type(event, WebhookEvent)
    event.raw  # pyright: ignore[reportAttributeAccessIssue]
    if isinstance(event, UnknownWebhookEvent):
        assert_type(event.type, int)
        assert_type(event.raw, dict[str, object])  # pyright: ignore[reportAssertTypeFailure]
    elif isinstance(event, OrderStatusChangeWebhook):
        assert_type(event, OrderStatusChangeWebhook)
        assert_type(event.type_, int)  # pyright: ignore[reportAssertTypeFailure]
    else:
        event.raw  # pyright: ignore[reportAttributeAccessIssue]
