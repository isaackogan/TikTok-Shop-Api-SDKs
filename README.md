# TikTok Shop API SDKs

A complete **OpenAPI 3.1 spec for the TikTok Shop API** (the TikTok Shop Partner API, API version 202309 and later) including webhooks, and the typed SDKs generated from it.

The spec is generated automatically from TikTok Shop's official partner documentation and regenerated whenever the docs change, so it doesn't drift the way hand-written API clients do.

> Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.

**Documentation:** [ttspa.docs.isaackogan.com](https://ttspa.docs.isaackogan.com/): Getting Started in every language, a section per SDK, and a browsable reference for every operation and webhook.

## What's here

| Path | Contents | Install |
| --- | --- | --- |
| [`.openapi/tiktok-shop.openapi.yaml`](.openapi/tiktok-shop.openapi.yaml) | The OpenAPI 3.1 spec (also as [JSON](.openapi/tiktok-shop.openapi.json)), regenerated daily | |
| [`typescript/`](typescript) | TypeScript SDK, [npm](https://www.npmjs.com/package/tiktok-shop-api) | `npm install tiktok-shop-api` |
| [`python/`](python) | Python SDK, [PyPI](https://pypi.org/project/tiktok-shop-api/) | `pip install tiktok-shop-api` |
| [`go/`](go) | Go SDK, [Go modules](https://pkg.go.dev/github.com/isaackogan/TikTok-Shop-Api-SDKs/go) | `go get github.com/isaackogan/TikTok-Shop-Api-SDKs/go` |
| [`java/`](java) | Java SDK, [Maven Central](https://central.sonatype.com/artifact/com.isaackogan/tiktok-shop-api) | Maven `com.isaackogan:tiktok-shop-api` |
| [`kotlin/`](kotlin) | Kotlin SDK, [Maven Central](https://central.sonatype.com/artifact/com.isaackogan/tiktok-shop-api-kotlin) | `com.isaackogan:tiktok-shop-api-kotlin` |
| [`php/`](php) | PHP SDK, [Packagist](https://packagist.org/packages/isaackogan/tiktok-shop-api) | `composer require isaackogan/tiktok-shop-api` |
| [`rust/`](rust) | Rust SDK, [crates.io](https://crates.io/crates/tiktok-shop-api) | `cargo add tiktok-shop-api` |
| [`csharp/`](csharp) | C# SDK, [NuGet](https://www.nuget.org/packages/TikTokShop.Api) | `dotnet add package TikTokShop.Api` |

Every SDK is generated from the spec and adds the parts a generator can't: request signing, shop cipher handling, an OAuth helper (authorization URL, token exchange and refresh) and typed webhooks. Request signing follows TikTok's documentation and has not been verified against the live API yet. If TikTok rejects a signature, please open an issue at https://github.com/isaackogan/TikTok-Shop-Api-SDKs/issues. Releases are cut with the button described in [RELEASING.md](RELEASING.md).

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
