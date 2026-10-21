# TikTok Shop API SDKs (Unofficial)

[TikTok Shop API](https://partner.tiktokshop.com/) SDKs for TypeScript, Python, Go, Java, Kotlin, PHP, Rust and C# (Unofficial, Unaffiliated with TikTok or ByteDance Ltd.)

A complete OpenAPI 3.1 spec for the TikTok Shop API, also called the TikTok Shop Partner API, covering API version
202309 and later with webhooks included, and the eight typed SDKs generated from it. It spans orders, products,
fulfillment, logistics, returns and refunds, finance, promotions, affiliate, analytics, customer service and every
other documented area, for sellers, partners and creators.

The spec is generated automatically from TikTok Shop's partner documentation and regenerated whenever the docs change,
so it doesn't drift the way hand-written API clients do. Each SDK adds the parts a generator can't: request signing,
shop cipher handling, an OAuth helper (authorization URL, token exchange and refresh) and typed webhooks.

Full guides, API reference and documentation: <https://ttspa.docs.isaackogan.com/>

The docs have [Getting Started](https://ttspa.docs.isaackogan.com/) in every language, a section per SDK, guides to
[authorization](https://ttspa.docs.isaackogan.com/getting-started/authorization/), [webhooks](https://ttspa.docs.isaackogan.com/getting-started/webhooks/)
and [errors](https://ttspa.docs.isaackogan.com/getting-started/errors/), and an [API reference](https://ttspa.docs.isaackogan.com/openapi/reference/)
for every operation and webhook.

![Stars](https://img.shields.io/github/stars/isaackogan/TikTok-Shop-Api-SDKs?style=flat&color=0274b5)
![Issues](https://img.shields.io/github/issues/isaackogan/TikTok-Shop-Api-SDKs?style=flat&color=0274b5)
![License](https://img.shields.io/github/license/isaackogan/TikTok-Shop-Api-SDKs?style=flat&color=0274b5)
![OpenAPI](https://img.shields.io/badge/OpenAPI-3.1-0274b5?style=flat)

> [!IMPORTANT]
> Request signing follows TikTok's documentation and has not been verified against the live API yet. If TikTok rejects a signature, please open an issue at https://github.com/isaackogan/TikTok-Shop-Api-SDKs/issues.

### Table of Contents

- [SDKs](#sdks)
- [The OpenAPI Spec](#the-openapi-spec)
- [Getting Started](#getting-started)
- [Coverage](#coverage)
- [Frequently Asked Questions](#frequently-asked-questions)
- [Contributors](#contributors)
- [License](#license)

## SDKs

| Language | Registry | Install |
|----------|----------|---------|
| [TypeScript](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/typescript) | [npm](https://www.npmjs.com/package/tiktok-shop-api) | `npm install tiktok-shop-api` |
| [Python](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/python) | [PyPI](https://pypi.org/project/tiktok-shop-api/) | `pip install tiktok-shop-api` |
| [Go](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/go) | [Go modules](https://pkg.go.dev/github.com/isaackogan/TikTok-Shop-Api-SDKs/go) | `go get github.com/isaackogan/TikTok-Shop-Api-SDKs/go` |
| [Java](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/java) | [Maven Central](https://central.sonatype.com/artifact/com.isaackogan/tiktok-shop-api) | Maven or Gradle, `com.isaackogan:tiktok-shop-api` |
| [Kotlin](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/kotlin) | [Maven Central](https://central.sonatype.com/artifact/com.isaackogan/tiktok-shop-api-kotlin) | Gradle or Maven, `com.isaackogan:tiktok-shop-api-kotlin` |
| [PHP](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/php) | [Packagist](https://packagist.org/packages/isaackogan/tiktok-shop-api) | `composer require isaackogan/tiktok-shop-api` |
| [Rust](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/rust) | [crates.io](https://crates.io/crates/tiktok-shop-api) | `cargo add tiktok-shop-api` |
| [C#](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/csharp) | [NuGet](https://www.nuget.org/packages/TikTokShop.Api) | `dotnet add package TikTokShop.Api` |

Each SDK is versioned and released on its own. The PHP package is mirrored to
[isaackogan/TikTok-Shop-Api-PHP](https://github.com/isaackogan/TikTok-Shop-Api-PHP) for Packagist; please open issues
here.

## The OpenAPI Spec

The spec is one OpenAPI 3.1 document, in [`.openapi/`](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/.openapi)
as [YAML](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/.openapi/tiktok-shop.openapi.yaml) and
[JSON](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/.openapi/tiktok-shop.openapi.json), regenerated
daily. The docs' [OpenAPI section](https://ttspa.docs.isaackogan.com/openapi/) describes it in full, including every
vendor extension.

Point any OpenAPI 3.1 tool (code generators, API clients, docs viewers) at `.openapi/tiktok-shop.openapi.yaml`. The base
URL is `https://open-api.tiktokglobalshop.com`.

Three things apply to most requests, so the spec describes each one once rather than on every operation:

- Every request needs `app_key`, `timestamp` and an HMAC-SHA256 `sign` query parameter. See `x-tts-signing` in the spec
  and TikTok's [signing guide](https://partner.tiktokshop.com/docv2/page/678e3a4278f4c20311b8b57e).
- Authenticated endpoints need the `x-tts-access-token` header (the `accessToken` security scheme).
- Shop-scoped endpoints need a `shop_cipher` query parameter (the shared `ShopCipher` parameter, flagged with
  `x-tts-requires-shop-cipher`).

If you generate your own client, implement signing yourself (OpenAPI can't express it), add `shop_cipher` on the
flagged operations, and strip the `webhooks` section if your generator doesn't support it.

## Getting Started

1. Pick your language from the [SDK table](#sdks) and install the package.

2. Authorize a shop with OAuth. Every SDK has a helper that builds the authorization URL for sellers, partners and
   creators, then exchanges the `code` for an access token and refreshes it. The
   [authorization guide](https://ttspa.docs.isaackogan.com/getting-started/authorization/) explains the flow.

3. Make your first call. Each SDK's README has a numbered Getting Started with the code for that language:
   - [TypeScript](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/typescript#getting-started)
   - [Python](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/python#getting-started)
   - [Go](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/go#getting-started)
   - [Java](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/java#getting-started)
   - [Kotlin](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/kotlin#getting-started)
   - [PHP](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/php#getting-started)
   - [Rust](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/rust#getting-started)
   - [C#](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/csharp#getting-started)

## Coverage

Every documented REST endpoint and webhook of the TikTok Shop Partner API, across Products, Orders, Fulfillment,
Logistics, Return and refund, Promotion, Finance, Affiliate (creator, partner and seller), Analytics, Authorization,
Customer service, Customer engagement, Events, Fulfilled by TikTok (FBT), Seller, Supply chain and Tools.

For each endpoint the spec includes:

- request parameters and body, and response schemas, with types and required fields;
- enums and length/range limits stated in the docs;
- the OAuth scopes it needs (`x-tts-scopes`) and its error codes (`x-tts-error-codes`);
- a link to its page in TikTok's docs (`x-tts-docs-url`).

Webhooks are described under the OpenAPI 3.1 `webhooks` section, with a `WebhookEvent` union of every payload.

## Frequently Asked Questions

### Is there a TikTok Shop API SDK for my language?

There are SDKs for TypeScript (Node.js), Python, Go, Java, Kotlin, PHP, Rust and C# (.NET). For any other language,
generate a client from the [OpenAPI spec](#the-openapi-spec) and add request signing yourself.

### Where can I download the TikTok Shop API OpenAPI spec?

From [`.openapi/`](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/.openapi) in this repository, as YAML
or JSON, or from the [docs site](https://ttspa.docs.isaackogan.com/openapi/).

### How do I get a TikTok Shop access token?

Send the seller to the authorization URL, then trade the `code` TikTok redirects back with for an access token and a
refresh token. Every SDK has an OAuth helper for this, and the
[authorization guide](https://ttspa.docs.isaackogan.com/getting-started/authorization/) walks through it.

### What is a shop cipher?

A value that identifies one of the seller's shops. Shop-scoped endpoints need it as the `shop_cipher` query parameter.
Get it from the authorized-shops call; each SDK then adds it to the endpoints that need it.

### How are TikTok Shop webhooks verified?

TikTok signs each delivery in the `Authorization` header: HMAC-SHA256 over your app key plus the raw body, keyed with
your app secret, in lowercase hex. Every SDK verifies it and parses the body into a typed event. See the
[webhooks guide](https://ttspa.docs.isaackogan.com/getting-started/webhooks/).

### How current is the spec?

It is regenerated from TikTok's partner documentation whenever the docs change, and the SDKs are regenerated with it.

### Is this affiliated with TikTok?

No. It is an independent open-source project, built from TikTok's partner documentation.

## Contributors

* **Isaac Kogan** - *Creator & Maintainer* - [isaackogan](https://github.com/isaackogan)

Releases are cut with the button described in [RELEASING.md](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/RELEASING.md).

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/LICENSE) file for details.

Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.
