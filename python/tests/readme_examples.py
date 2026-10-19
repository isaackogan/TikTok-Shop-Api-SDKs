# Type-checked copy of the README's code (the statements are verbatim; imports point at the package).
# `tests/test_readme.py` fails if the README and this file drift apart, and pyright checks this file.
import asyncio
import os

from flask import Flask, request

from tiktok_shop_api import (
    AsyncTikTokShop,
    TikTokShop,
    TikTokShopAuth,
    UnknownWebhookEvent,
    WebhookSignatureError,
    Webhooks,
)
from tiktok_shop_api.generated.models import OrderStatusChangeWebhook


def oauth_and_calls(code_from_redirect: str, token_a: str, token_b: str, cipher_a: str, cipher_b: str) -> None:
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

    with TikTokShop(os.environ["TTS_APP_KEY"], os.environ["TTS_APP_SECRET"], access_token=tokens.access_token) as client:
        # Find the shop cipher
        shops = client.authorization.get_authorized_shops()
        assert shops is not None
        shop_cipher = shops.to_dict()["data"]["shops"][0]["cipher"]

        seller = client.with_shop(access_token=tokens.access_token, shop_cipher=shop_cipher)
        orders = seller.orders.get_order_list(page_size=20)

        shop_a = client.with_shop(access_token=token_a, shop_cipher=cipher_a)
        shop_b = client.with_shop(access_token=token_b, shop_cipher=cipher_b)

    async def main() -> None:
        async with AsyncTikTokShop(os.environ["TTS_APP_KEY"], os.environ["TTS_APP_SECRET"], access_token=tokens.access_token) as client:
            shops = await client.authorization.get_authorized_shops()
            assert shops is not None
            seller = client.with_shop(shop_cipher=shops.to_dict()["data"]["shops"][0]["cipher"])
            orders = await seller.orders.get_order_list(page_size=20)

    asyncio.run(main())


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
    if isinstance(event, UnknownWebhookEvent):
        print("unknown webhook type", event.type, event.raw)
    elif isinstance(event, OrderStatusChangeWebhook):
        print(event.shop_id, event.data)
    return "", 200
