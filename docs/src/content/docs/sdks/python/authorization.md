---
title: Authorization
description: Build TikTok Shop authorization URLs and exchange and refresh tokens with TikTokShopAuth and AsyncTikTokShopAuth in Python.
sidebar:
  order: 2
---

`TikTokShopAuth` builds the URL a seller, partner or creator opens to authorize your app, and calls TikTok's token endpoints. See [authorization](/getting-started/authorization/) for the flow itself.

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

`AsyncTikTokShopAuth` has the same methods as coroutines. `authorization_url` stays a plain method on both classes, because it does no I/O.

## Options

`TikTokShopAuth` and `AsyncTikTokShopAuth` take `app_key` and `app_secret` as the first two positional arguments, then:

| Option | Meaning |
| --- | --- |
| `service_id` | Your Partner Center service ID. Required for `seller` and `partner` authorization URLs; `creator` URLs use the app key instead. A missing one raises `ValueError`. |
| `base_url` | Token endpoint host, an origin with no path prefix. Defaults to `https://auth.tiktok-shops.com`. |
| `timeout` | Per-request timeout in seconds. Defaults to 30; `None` or `0` means no limit. An `httpx.Timeout` is also accepted. |
| `transport` | An `httpx` transport override (`httpx.BaseTransport` for the sync class, `httpx.AsyncBaseTransport` for the async one). |

`authorization_url` omits an empty `state`, the same as an absent one. An unknown `type` or `region` raises `ValueError`.

## Tokens

`exchange_code` and `refresh` return a `TokenSet`, a frozen dataclass:

| Field | Meaning |
| --- | --- |
| `access_token`, `refresh_token` | The tokens. Send the access token with API calls; trade the refresh token for a new pair. |
| `access_token_expire_in`, `refresh_token_expire_in` | Unix timestamps in seconds at which each token expires. They are moments, not durations. |
| `open_id`, `seller_name`, `seller_base_region`, `user_type`, `granted_scopes` | Optional. Creator and partner tokens may lack the seller fields. An absent field is `None`, and an absent `granted_scopes` is `None` rather than an empty list. |

`repr` of a `TokenSet` hides both tokens. The attributes and `dataclasses.asdict` keep them, so you can serialize a set to store it. Protect wherever you store it.

A non-zero `code` in TikTok's response raises a `TikTokShopError` with `code`, `message` and `request_id`, and so does a token reply without `data`. See [errors](/sdks/python/errors/).

## Secrets in logs

Token calls send `app_secret`, `auth_code` and `refresh_token` in the URL query, and httpx logs every request URL at INFO. Importing `tiktok_shop_api` adds a filter to the `httpx` logger that replaces those three values with `***`. Keep the filter if you reconfigure that logger. The auth helpers' `repr` shows the app secret as `***`.
