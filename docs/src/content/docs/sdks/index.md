---
title: Choose an SDK
description: TikTok Shop API SDKs for TypeScript, Python, Go, Java, Kotlin, PHP, Rust and C#, with package names, requirements and links.
---

Every SDK is generated from the same [OpenAPI spec](/openapi/), and each adds the same hand-written parts:
- request signing and shop cipher handling;
- an OAuth helper;
- strict, typed webhook parsing;
- one error type with the same codes.

Pick the language your integration is written in. The behavior is the same in all eight.

| SDK | Package | Install | Requires |
| --- | --- | --- | --- |
| [TypeScript](/sdks/typescript/) | [`tiktok-shop-api`](https://www.npmjs.com/package/tiktok-shop-api) on npm | `npm install tiktok-shop-api` | Node.js 22 |
| [Python](/sdks/python/) | [`tiktok-shop-api`](https://pypi.org/project/tiktok-shop-api/) on PyPI | `pip install tiktok-shop-api` | Python 3.11 |
| [Go](/sdks/go/) | [`github.com/isaackogan/TikTok-Shop-Api-SDKs/go`](https://pkg.go.dev/github.com/isaackogan/TikTok-Shop-Api-SDKs/go) | `go get github.com/isaackogan/TikTok-Shop-Api-SDKs/go` | Go 1.22 |
| [Java](/sdks/java/) | [`com.isaackogan:tiktok-shop-api`](https://central.sonatype.com/artifact/com.isaackogan/tiktok-shop-api) on Maven Central | Maven or Gradle | Java 11 |
| [Kotlin](/sdks/kotlin/) | [`com.isaackogan:tiktok-shop-api-kotlin`](https://central.sonatype.com/artifact/com.isaackogan/tiktok-shop-api-kotlin) on Maven Central | Gradle or Maven | JVM 11 |
| [PHP](/sdks/php/) | [`isaackogan/tiktok-shop-api`](https://packagist.org/packages/isaackogan/tiktok-shop-api) on Packagist | `composer require isaackogan/tiktok-shop-api` | PHP 8.2 |
| [Rust](/sdks/rust/) | [`tiktok-shop-api`](https://crates.io/crates/tiktok-shop-api) on crates.io | `cargo add tiktok-shop-api` | Rust 1.88 |
| [C#](/sdks/csharp/) | [`TikTokShop.Api`](https://www.nuget.org/packages/TikTokShop.Api) on NuGet | `dotnet add package TikTokShop.Api` | .NET 8 |

Each SDK's section has the same five pages: an overview with install and a first call, authorization, calling the API, webhooks, and errors.

## What every SDK does

- **Signs every request.** It adds `app_key`, `timestamp` and `sign`, and sends the access token in `x-tts-access-token`.
- **Adds `shop_cipher`** to exactly the operations that need it. The cipher is set once per client, and each SDK can derive a client for another shop that shares the connection pool.
- **Has an OAuth helper** that builds authorization URLs for sellers, partners and creators in the US and the rest of the world, and exchanges and refreshes tokens.
- **Verifies webhooks** against the raw body in constant time, and parses each into its generated model. Unknown types are kept rather than rejected.
- **Raises one error type** with TikTok's code, message and request ID, the HTTP status, and -1 for unreadable replies and network failures.
- **Keeps credentials where they belong.** The HTTP clients it builds never follow a redirect, so credentials are never forwarded to another host. Token-call errors never contain the app secret, the authorization code or the refresh token.
- **Leaves its own code alone.** Generated code lives in a `generated` folder inside each SDK and is never edited by hand. The hand-written code is beside it, so regenerating never overwrites it.

Each SDK is versioned and released on its own, so upgrading one language never forces a release of another.
