# TikTok Shop API SDKs

A complete **OpenAPI 3.1 spec for the TikTok Shop API** (the TikTok Shop Partner API, API version 202309 and later) including webhooks, and the typed SDKs generated from it.

The spec is generated automatically from TikTok Shop's official partner documentation and regenerated whenever the docs change, so it doesn't drift the way hand-written API clients do.

> Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.

## What's here

| Path | Contents | Status |
| --- | --- | --- |
| [`.openapi/tiktok-shop.openapi.yaml`](.openapi/tiktok-shop.openapi.yaml) | The OpenAPI 3.1 spec (also as [JSON](.openapi/tiktok-shop.openapi.json)) | Published, regenerated daily |
| `typescript/`, `python/`, `php/`, `java/`, `kotlin/`, `rust/` | TikTok Shop SDKs generated from the spec | Planned |

## Coverage

Every documented REST endpoint and webhook of the TikTok Shop Partner API, across Products, Orders, Fulfillment, Logistics, Return and refund, Promotion, Finance, Affiliate (creator, partner and seller), Analytics, Authorization, Customer service, Customer engagement, Events, Fulfilled by TikTok (FBT), Seller, Supply chain and Tools.

For each endpoint the spec includes:

- request parameters and body, and response schemas, with types and required fields
- enums and length/range limits stated in the docs
- the OAuth scopes it needs (`x-tts-scopes`) and its error codes (`x-tts-error-codes`)
- a link to the official docs page (`x-tts-docs-url`)

Webhooks are described under the OpenAPI 3.1 `webhooks` section, with a `WebhookEvent` union of every payload.

## Using the spec

Point any OpenAPI 3.1 tool (code generators, API clients, docs viewers) at `.openapi/tiktok-shop.openapi.yaml`. The base URL is `https://open-api.tiktokglobalshop.com`.

Three things apply to most requests and are described once rather than on every operation:

- **Signing.** Every request needs `app_key`, `timestamp` and an HMAC-SHA256 `sign` query parameter. See `x-tts-signing` in the spec and TikTok's [signing guide](https://partner.tiktokshop.com/docv2/page/678e3a4278f4c20311b8b57e).
- **Access token.** Authenticated endpoints need the `x-tts-access-token` header (the `accessToken` security scheme).
- **Shop cipher.** Shop-scoped endpoints need a `shop_cipher` query parameter (the shared `ShopCipher` parameter, flagged with `x-tts-requires-shop-cipher`).

## License

[MIT](LICENSE)
