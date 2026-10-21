# TikTok Shop API for Python (Unofficial)

[TikTok Shop API](https://partner.tiktokshop.com/) Client for Python (Unofficial, Unaffiliated with TikTok or ByteDance Ltd.)

A typed Python client for the TikTok Shop API, also called the TikTok Shop Partner API or Open API. It covers over 300
operations across orders, products, fulfillment, logistics, returns and refunds, finance, promotions, affiliate,
analytics and customer service, for sellers, partners and creators. There is a sync client and an asyncio client.

Every request is signed with HMAC-SHA256 and sent with your access token, and the shop cipher is added wherever an
endpoint needs it. The OAuth helper builds the authorization URL and exchanges and refreshes tokens. One client can
serve many shops, and TikTok Shop webhooks are verified and parsed into typed models. The methods are generated from an
OpenAPI spec built from TikTok's partner documentation, so they track the docs.

Full guides, API reference and documentation: <https://ttspa.docs.isaackogan.com/sdks/python/>

The guides cover [Authorization](https://ttspa.docs.isaackogan.com/sdks/python/authorization/), [Calling the API](https://ttspa.docs.isaackogan.com/sdks/python/calling-the-api/),
[Webhooks](https://ttspa.docs.isaackogan.com/sdks/python/webhooks/) and [Errors](https://ttspa.docs.isaackogan.com/sdks/python/errors/), and the [API reference](https://ttspa.docs.isaackogan.com/openapi/reference/) lists every operation and webhook.

[![PyPI](https://img.shields.io/pypi/v/tiktok-shop-api?style=flat&color=0274b5)](https://pypi.org/project/tiktok-shop-api/)
![Python](https://img.shields.io/pypi/pyversions/tiktok-shop-api?style=flat&color=0274b5)
![Stars](https://img.shields.io/github/stars/isaackogan/TikTok-Shop-Api-SDKs?style=flat&color=0274b5)
![Issues](https://img.shields.io/github/issues/isaackogan/TikTok-Shop-Api-SDKs?style=flat&color=0274b5)
![License](https://img.shields.io/github/license/isaackogan/TikTok-Shop-Api-SDKs?style=flat&color=0274b5)

> [!IMPORTANT]
> Request signing follows TikTok's documentation and has not been verified against the live API. If TikTok rejects a signature, please open an issue at https://github.com/isaackogan/TikTok-Shop-Api-SDKs/issues.

> [!TIP]
> The OpenAPI spec this client is generated from is published at
> [tiktok-shop.openapi.yaml](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/.openapi/tiktok-shop.openapi.yaml).
> Point any OpenAPI 3.1 tool at it.

### Do you prefer other programming languages?

- [TikTok Shop API for TypeScript](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/typescript), `tiktok-shop-api` on npm
- [TikTok Shop API for Go](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/go), `github.com/isaackogan/TikTok-Shop-Api-SDKs/go`
- [TikTok Shop API for Java](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/java), `com.isaackogan:tiktok-shop-api` on Maven Central
- [TikTok Shop API for Kotlin](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/kotlin), `com.isaackogan:tiktok-shop-api-kotlin` on Maven Central
- [TikTok Shop API for PHP](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/php), `isaackogan/tiktok-shop-api` on Packagist
- [TikTok Shop API for Rust](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/rust), `tiktok-shop-api` on crates.io
- [TikTok Shop API for C# and .NET](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/csharp), `TikTokShop.Api` on NuGet

### Table of Contents

- [Getting Started](#getting-started)
- [Params and Options](#params-and-options)
- [Methods](#methods)
- [Examples](#examples)
- [Frequently Asked Questions](#frequently-asked-questions)
- [Contributors](#contributors)
- [License](#license)

## Getting Started

1. Install the package from PyPI

```sh
pip install tiktok-shop-api
```

It needs Python 3.11 or newer. Its dependencies are `httpx` and `attrs`.

2. Authorize a shop with OAuth and get an access token

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

`AsyncTikTokShopAuth` has the same methods as coroutines. A non-zero `code` in TikTok's response raises a
`TikTokShopError` with `code`, `message` and `request_id` (see [Handle errors](#handle-errors)).

3. Make your first call

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

Every call is signed, timestamped and sent with your access token. The `shop_cipher` query parameter is added on the
endpoints that need it.

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

## Params and Options

To create a new client, pass these arguments. `AsyncTikTokShop` takes the same ones.

`TikTokShop(app_key, app_secret, access_token=None, shop_cipher=None, *, base_url=..., timeout=30.0, transport=None)`

| Param Name | Required | Description |
|------------|----------|-------------|
| `app_key` | Yes | Your app key. |
| `app_secret` | Yes | Your app secret. It signs every request. `repr()` of a client hides it. |
| `access_token` | No | The seller's access token, sent as the `x-tts-access-token` header. |
| `shop_cipher` | No | The shop's cipher, added as `shop_cipher` to the operations that need one. `authorization.get_authorized_shops()` returns it. |
| `base_url` | No | Default `https://open-api.tiktokglobalshop.com`. It must be an origin such as `https://host:8443`, with no path prefix: signing and shop-cipher matching use the request path. |
| `timeout` | No | Seconds, default 30. `None` or `0` means no limit. You can also pass an `httpx.Timeout`. |
| `transport` | No | An `httpx.BaseTransport` (`httpx.AsyncBaseTransport` for the async client). Without one, httpx builds its default, which honours `HTTP(S)_PROXY`, `ALL_PROXY`, `NO_PROXY` and `SSL_CERT_FILE`. |

The OAuth helper takes its own arguments. `AsyncTikTokShopAuth` takes the same ones.

`TikTokShopAuth(app_key, app_secret, service_id=None, *, base_url=..., timeout=30.0, transport=None)`

| Param Name | Required | Description |
|------------|----------|-------------|
| `app_key` | Yes | Your app key. |
| `app_secret` | Yes | Your app secret. |
| `service_id` | No | Your Partner Center service ID. Seller and partner authorization URLs need it. |
| `base_url` | No | The token endpoint's origin, with no path prefix. Default `https://auth.tiktok-shops.com`. |
| `timeout` | No | Seconds, default 30. `None` or `0` means no limit, or pass an `httpx.Timeout`. |
| `transport` | No | An httpx transport for the token calls. |

Requests carry the User-Agent `tiktok-shop-api-python/<version>`.

Token calls send `app_secret`, `auth_code` and `refresh_token` in the URL query, and httpx logs every request URL at
INFO. Importing `tiktok_shop_api` adds a filter to the `httpx` logger that replaces those three values with `***`, so a
service logging at INFO never writes them. Keep the filter if you reconfigure that logger.

## Methods

Each API group is an attribute of the client: `affiliate_creator`, `affiliate_partner`, `affiliate_seller`,
`analytics`, `authorization`, `customer_engagement`, `customer_service`, `event`, `finance`, `fulfilled_by_tiktok`,
`fulfillment`, `logistics`, `orders`, `products`, `promotion`, `return_and_refund`, `seller`, `supply_chain` and `tools`.
On `AsyncTikTokShop` every operation is a coroutine.

| Method Name | Description |
|-------------|-------------|
| `client.with_shop(*, access_token, shop_cipher)` | Returns a client for another shop or token. An argument you leave out keeps this client's value, and this client is not changed. See [Many shops](#many-shops). |
| `client.close()` | Closes the HTTP client. `with TikTokShop(...) as client:` calls it on exit. On `AsyncTikTokShop` it is `await client.aclose()`, or `async with`. |
| `auth.authorization_url(*, type, region, state=None)` | Builds the URL to send a seller, partner or creator to. `type` is `"seller"`, `"partner"` or `"creator"`; `region` is `"us"` or `"row"`. An empty `state` is left out. |
| `auth.exchange_code(code)` | Trades the `code` from the redirect for a `TokenSet`. |
| `auth.refresh(refresh_token)` | Trades a refresh token for a new `TokenSet`. |
| `Webhooks.verify(*, app_key, app_secret, raw_body, signature)` | Checks a webhook's `Authorization` header: HMAC-SHA256, keyed with your app secret, over your app key plus the raw body, compared in constant time. Returns `True` or `False`. |
| `Webhooks.parse(raw_body)` | Parses a body into its generated webhook model, or an `UnknownWebhookEvent` for a type this SDK does not know. Raises `ValueError`. |
| `Webhooks.verify_and_parse(*, app_key, app_secret, raw_body, signature)` | Verifies, then parses. Raises `WebhookSignatureError` when the signature does not match. |

A `TokenSet` has `access_token`, `access_token_expire_in`, `refresh_token` and `refresh_token_expire_in` (both expiry
times are Unix timestamps in seconds). When TikTok sends them, it also has `open_id`, `seller_name`,
`seller_base_region`, `user_type` and `granted_scopes`; a field TikTok did not send is `None`. Its `repr` hides both
tokens. `raw_body` is `bytes` or `str`.

## Examples

### Many shops

`with_shop` returns a client for another shop. It keeps your app credentials, base URL and timeout, and shares the
transport if you passed one. Arguments you leave out keep the original's values, and the original is never changed:

```python
import os

from tiktok_shop_api import TikTokShop

client = TikTokShop(os.environ["TTS_APP_KEY"], os.environ["TTS_APP_SECRET"])
token_a, cipher_a = os.environ["TOKEN_A"], os.environ["CIPHER_A"]
token_b, cipher_b = os.environ["TOKEN_B"], os.environ["CIPHER_B"]

shop_a = client.with_shop(access_token=token_a, shop_cipher=cipher_a)
shop_b = client.with_shop(access_token=token_b, shop_cipher=cipher_b)
```

Closing a client made by `with_shop` does not close a shared transport; close the original for that.

### Webhooks

Verify the signature against the raw request body, then parse it into a typed event. This example uses Flask; any
framework that gives you the unmodified bytes works:

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
- A webhook type this SDK does not know comes back as `UnknownWebhookEvent(type, raw)`. Known events are the generated
  model for that webhook, so `isinstance` narrows them.
- Parsing is strict. `parse` raises `ValueError` for a body that is not a JSON object, a `type` that is missing or not
  an integer, or a known type with a required field missing or null: a known type missing a required field is a parse
  error.
- `EVENT_TYPES` maps a type number to its name (`1` is `ORDER_STATUS_CHANGE`).

### Handle errors

Every failed call raises `TikTokShopError`, with `code`, `message`, `request_id`, `http_status` and the original
exception as `__cause__`:

| What happened | `code` | `http_status` |
|---|---|---|
| TikTok's reply has a non-zero `code`, even on HTTP 200 | TikTok's code | the status |
| A non-2xx reply | TikTok's non-zero code if the body has one, else the HTTP status | the status |
| A 2xx reply that can't be read: not a JSON object, a `code` that isn't an integer, a body that doesn't fit its model, or a token reply without `data` | -1 | the status |
| No HTTP response at all: connection refused, DNS, TLS, or a timeout | -1 | `None` |

## Frequently Asked Questions

### How do I get a TikTok Shop access token in Python?

Create a `TikTokShopAuth` with your app key, app secret and service ID, send the seller to `authorization_url()`, then
trade the `code` TikTok sends back with `exchange_code()`. Call `refresh()` before the access token expires. See
[Getting Started](#getting-started).

### What is a shop cipher, and where do I find it?

Most TikTok Shop API endpoints act on one shop and need a `shop_cipher` query parameter. Call
`client.authorization.get_authorized_shops()` with the seller's access token: each shop in the reply has a `cipher`.
Pass it as `shop_cipher` and the client adds it to every endpoint that needs it.

### Does it support asyncio?

Yes. `AsyncTikTokShop` and `AsyncTikTokShopAuth` mirror the sync classes, with every API call as a coroutine.

### How do I verify TikTok Shop webhooks in Flask, Django or FastAPI?

Pass the raw request body and the `Authorization` header to `Webhooks.verify_and_parse`. In Flask that body is
`request.get_data()`; in any framework, use the bytes as received, because re-serialized JSON no longer matches the
signature. See [Webhooks](#webhooks).

### Can one app manage many TikTok Shop sellers?

Yes. Keep one client per shop with `with_shop`. See [Many shops](#many-shops).

### Which TikTok Shop API versions does it cover?

Every endpoint in TikTok's partner documentation, from API version 202309 onwards, and every documented webhook.

### Is this affiliated with TikTok?

No. It is an independent open-source project, built from TikTok's partner documentation.

### Is this available in other languages?

Yes. See [Do you prefer other programming languages?](#do-you-prefer-other-programming-languages) for the TypeScript,
Go, Java, Kotlin, PHP, Rust and C# SDKs.

## Contributors

* **Isaac Kogan** - *Creator & Maintainer* - [isaackogan](https://github.com/isaackogan)

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/LICENSE) file for details.

Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.
