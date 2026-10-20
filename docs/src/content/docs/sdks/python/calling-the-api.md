---
title: Calling the API
description: Create the TikTokShop and AsyncTikTokShop clients, call operations by API area, and work with many shops in Python.
sidebar:
  order: 3
---

`TikTokShop` is the API client, and `AsyncTikTokShop` is its async twin. Each request they send gets the following automatically:
- the `app_key`, `timestamp` and `sign` query parameters;
- your access token, in the `x-tts-access-token` header;
- `shop_cipher`, on the operations that need one.

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

## Async

The async client mirrors the sync one, with `await` on every call. Use it with `async with`; it closes with `aclose()`.

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

## API areas

One attribute per API area hangs off the client, matching the spec's tags. Both clients have the same attributes:

| Attribute | Area |
| --- | --- |
| `affiliate_creator`, `affiliate_partner`, `affiliate_seller` | Affiliate creator, partner and seller |
| `analytics` | Analytics |
| `authorization` | Authorization, including `get_authorized_shops` |
| `customer_engagement`, `customer_service` | Customer engagement and customer service |
| `event` | Event (webhook subscriptions) |
| `finance` | Finance |
| `fulfilled_by_tiktok` | Fulfilled by TikTok (FBT) |
| `fulfillment`, `logistics` | Fulfillment and logistics |
| `orders`, `products`, `promotion` | Orders, products and promotion |
| `return_and_refund` | Return and refund |
| `seller`, `supply_chain`, `tools` | Seller, supply chain and tools |

Method and parameter names follow the [API reference](/openapi/reference/), in snake case. Responses are typed models; `to_dict()` gives the plain dictionary.

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

Closing a client returned by `with_shop` does not close the shared transport. Close the original for that.

## Options

`TikTokShop` and `AsyncTikTokShop` take `app_key`, `app_secret`, `access_token` and `shop_cipher` as positional arguments, then keyword options:

| Option | Meaning |
| --- | --- |
| `app_key`, `app_secret` | Your app's credentials. |
| `access_token` | The seller's access token, sent in `x-tts-access-token`. |
| `shop_cipher` | The shop cipher added to operations that need one. |
| `base_url` | The API host, an origin such as `https://host:8443` with no path prefix: signing and shop-cipher matching use the request path. Defaults to `https://open-api.tiktokglobalshop.com`. |
| `timeout` | Per-request timeout in seconds. Defaults to 30; `None` or `0` means no limit. An `httpx.Timeout` is also accepted. |
| `transport` | An `httpx` transport override: `httpx.BaseTransport` for `TikTokShop`, `httpx.AsyncBaseTransport` for `AsyncTikTokShop`. |

When you pass no `transport`, httpx builds its default, which honours `HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`, `NO_PROXY` and `SSL_CERT_FILE`.

Requests carry the User-Agent `tiktok-shop-api-python/<version>`, exported as `USER_AGENT`. `repr` of a client shows the app key and base URL, with the secrets hidden.
