---
title: Concepts
description: App keys, service IDs, access tokens, shop ciphers, request signing and 64-bit IDs in the TikTok Shop API.
sidebar:
  order: 1
---

Every TikTok Shop API call combines app credentials, a shop's authorization, and a signature. The SDKs handle each part the same way in every language.

## App credentials

Your app is registered in TikTok Shop Partner Center and has:

| Credential | Used for |
| --- | --- |
| App key | Identifies the app. Sent as the `app_key` query parameter on every call. |
| App secret | Signs every request and verifies webhooks. Never send it to a browser or log it. |
| Service ID | Seller and partner authorization URLs. Creator authorization uses the app key instead. |

Every SDK client and OAuth helper takes the app key and app secret. The OAuth helper also takes the service ID.

## Access tokens

A seller, partner or creator authorizes your app through [OAuth](/getting-started/authorization/). In return you get an **access token** and a **refresh token**, each with an expiry time.

- **The access token** is sent with each call in the `x-tts-access-token` header, the spec's `accessToken` security scheme.
- **The refresh token** buys a new pair before the access token expires.
- **The expiry fields are moments, not durations.** They are Unix timestamps in seconds.

## Shop cipher

A seller account can have several shops, and most operations act on one of them. The shop is named by its **shop cipher**: an opaque string from the authorized-shops operation, sent as the `shop_cipher` query parameter.

The spec flags the operations that need one with `x-tts-requires-shop-cipher`. The SDK clients add `shop_cipher` to exactly those operations, so you set the cipher once per client and never pass it as an argument. To work with several shops, every SDK can derive a client per shop that shares the same HTTP connection pool.

## Request signing

Every call carries three query parameters: `app_key`, `timestamp` (Unix seconds) and `sign`. The signature is the lowercase hex HMAC-SHA256, keyed with the app secret, of this string:

```text
app_secret + path + sorted(key + value for each query parameter except sign and access_token) + body + app_secret
```

Query values are decoded before signing, and a multipart body is left out. The SDKs compute this for every request.

Signing follows TikTok's [signing guide](https://partner.tiktokshop.com/docv2/page/678e3a4278f4c20311b8b57e) and the spec's `x-tts-signing` extension, but **has not been verified against the live API yet**. If TikTok rejects a signature, please open an issue at https://github.com/isaackogan/TikTok-Shop-Api-SDKs/issues.

Signing and shop-cipher matching both use the request path. A client's base URL must therefore be an origin, such as `https://host:8443`, with no path prefix.

## Base URLs

| Host | Used for |
| --- | --- |
| `https://open-api.tiktokglobalshop.com` | API calls, the spec's server |
| `https://auth.tiktok-shops.com` | Token exchange and refresh |
| `services.us.tiktokshop.com`, `services.tiktokshop.com` | Seller authorization pages (US, rest of world) |
| `partner.us.tiktokshop.com`, `partner.tiktokshop.com` | Partner authorization pages (US, rest of world) |
| `shop.tiktok.com` | Creator authorization page |

Each client takes a base URL override, for a proxy or a test server.

## Versions in paths

TikTok versions each operation in its path, such as `/order/202309/orders/search`. The spec and the SDKs cover API version 202309 and later. Method names come from the spec's operation IDs, so `getOrderList` is the same operation in every SDK.

## 64-bit IDs

Shop, order, product and other IDs are 64-bit integers. Most languages hold them exactly. JavaScript can't, so the TypeScript SDK reads them as strings in every response and webhook; see [IDs are strings](/sdks/typescript/calling-the-api/#ids-are-strings).

## Scopes

Each operation needs one or more API scopes, granted when the app is configured in Partner Center. They are listed per operation in the [API reference](/openapi/reference/) (`x-tts-scopes` in the spec). A token's granted scopes are in the token response, as `granted_scopes` or the language's equivalent.
