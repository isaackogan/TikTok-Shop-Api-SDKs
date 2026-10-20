---
title: Python SDK
description: Install tiktok-shop-api, the typed TikTok Shop API client for Python with sync and async clients, and make your first call.
sidebar:
  label: Overview
  order: 1
---

`tiktok-shop-api` is a typed Python client for the TikTok Shop Partner API. It has a sync and an async client, signs requests, handles OAuth, works with many shops at once, and verifies and types webhooks. It is published to [PyPI](https://pypi.org/project/tiktok-shop-api/), and its source is in [`python/`](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/python).

## Install

```sh
pip install tiktok-shop-api
```

Requires Python 3.11 or newer. Its dependencies are `httpx` and `attrs`.

## First call

With an access token from the [OAuth helper](/sdks/python/authorization/), create a client, look up the shop cipher, and call an operation on that shop:

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

Every call is signed, timestamped and sent with your access token. The `shop_cipher` query parameter is added for you on the endpoints that need it. The [async client](/sdks/python/calling-the-api/) mirrors this with `await` on every call.

## In this section

- [Authorization](/sdks/python/authorization/): `TikTokShopAuth` and `AsyncTikTokShopAuth`, authorization URLs, token exchange and refresh.
- [Calling the API](/sdks/python/calling-the-api/): the sync and async clients, API areas, many shops and options.
- [Webhooks](/sdks/python/webhooks/): `Webhooks.verify_and_parse` and typed events.
- [Errors](/sdks/python/errors/): `TikTokShopError` and its codes.
