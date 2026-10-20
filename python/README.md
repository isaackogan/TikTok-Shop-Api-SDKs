# tiktok-shop-api: TikTok Shop API client for Python

A typed Python client for the **TikTok Shop API** (the TikTok Shop Partner API). It covers over 300 operations across orders, products, fulfillment, logistics, finance, affiliate, customer service and more, with a sync client and an async client.

It signs requests for you, handles OAuth, works with many shops at once, and verifies and types TikTok Shop webhooks.

> **Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.**
>
> Request signing follows TikTok's documentation and has not been verified against the live API. If TikTok rejects a signature, please open an issue at https://github.com/isaackogan/TikTok-Shop-Api-SDKs/issues.

The client is generated from an OpenAPI spec that is itself built from the TikTok Shop Partner Center docs: [tiktok-shop.openapi.yaml](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/.openapi/tiktok-shop.openapi.yaml).

## Install

```sh
pip install tiktok-shop-api
```

Requires **Python 3.11 or newer**. Its dependencies are `httpx` and `attrs`.

## OAuth: get an access token

```python
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
```

`AsyncTikTokShopAuth` has the same methods as coroutines. A non-zero `code` in TikTok's response raises a `TikTokShopError` with `code`, `message` and `request_id` (see [Errors](#errors)).

## Make your first call

```python
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
```

The async client mirrors it, with `await` on every call:

```python
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
```

One attribute per API area hangs off the client (`orders`, `products`, `fulfillment`, `finance`, `affiliate_seller`, and so on). Every call is signed, timestamped and sent with your access token. The `shop_cipher` query parameter is added for you on the endpoints that need it.

## Many shops

`with_shop` returns a client for another shop. It shares the HTTP transport and your app credentials, so you can keep one per shop. Arguments you leave out keep the original's values, and the original is never changed:

```python
import os

from tiktok_shop_api import TikTokShop

client = TikTokShop(os.environ["TTS_APP_KEY"], os.environ["TTS_APP_SECRET"])
token_a, cipher_a = os.environ["TOKEN_A"], os.environ["CIPHER_A"]
token_b, cipher_b = os.environ["TOKEN_B"], os.environ["CIPHER_B"]

shop_a = client.with_shop(access_token=token_a, shop_cipher=cipher_a)
shop_b = client.with_shop(access_token=token_b, shop_cipher=cipher_b)
```

## Webhooks

Verify the signature against the **raw** request body, then parse it into a typed event. This example uses Flask; any framework that gives you the unmodified bytes works:

```python
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
```

- Never re-serialize the body before verifying. Changed whitespace or key order makes the signature fail.
- A webhook type this SDK does not know comes back as `UnknownWebhookEvent(type, raw)`. Known events are the generated model for that webhook, so `isinstance` narrows them.
- Parsing is strict. `parse` raises `ValueError` for a body that is not a JSON object, a `type` that is missing or not an integer, or a known type with a required field missing or null: a known type missing a required field is a parse error.
- `EVENT_TYPES` maps a type number to its name (`1` is `ORDER_STATUS_CHANGE`).

## Options

- `base_url` (on the clients and the auth helpers) must be an origin such as `https://host:8443`, with no path prefix: signing and shop-cipher matching use the request path.
- `timeout` (on all four) is in seconds and defaults to 30. `None` or `0` means no limit; you can also pass an `httpx.Timeout`.
- Requests carry the User-Agent `tiktok-shop-api-python/<version>`.
- Token calls send `app_secret`, `auth_code` and `refresh_token` in the URL query, and httpx logs every request URL at INFO. Importing `tiktok_shop_api` adds a filter to the `httpx` logger that replaces those three values with `***`, so a service logging at INFO never writes them. Keep the filter if you reconfigure that logger.

## Errors

Every failed call raises `TikTokShopError`, with `code`, `message`, `request_id`, `http_status` and the original exception as `__cause__`:

| What happened | `code` | `http_status` |
|---|---|---|
| TikTok's reply has a non-zero `code`, even on HTTP 200 | TikTok's code | the status |
| A non-2xx reply | TikTok's non-zero code if the body has one, else the HTTP status | the status |
| A 2xx reply that can't be read: not a JSON object, a `code` that isn't an integer, a body that doesn't fit its model, or a token reply without `data` | -1 | the status |
| No HTTP response at all: connection refused, DNS, TLS, or a timeout | -1 | `None` |

## About

This is the Python package of a set of generated TikTok Shop API SDKs. The OpenAPI spec and the other languages live in [isaackogan/TikTok-Shop-Api-SDKs](https://github.com/isaackogan/TikTok-Shop-Api-SDKs).

MIT licensed. Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.
