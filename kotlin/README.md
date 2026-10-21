# TikTok Shop API for Kotlin (Unofficial)

[TikTok Shop API](https://partner.tiktokshop.com/) Client for Kotlin and the JVM (Unofficial, Unaffiliated with TikTok or ByteDance Ltd.)

A Kotlin client for the TikTok Shop API, also called the TikTok Shop Partner API or Open API. It covers every endpoint
in the published spec, over 300 operations across orders, products, fulfillment, logistics, returns and refunds,
finance, promotions, affiliate, analytics and customer service, grouped like TikTok's own docs.

Every request is signed with HMAC-SHA256 and sent with your access token, and the shop cipher is added wherever an
endpoint needs it. The OAuth helper builds the authorization URL and exchanges and refreshes tokens. One client can
serve many shops, and TikTok Shop webhooks are verified and parsed into a sealed class you narrow with `when`.
Requests and responses are Kotlin data classes generated from the OpenAPI spec, and 64-bit IDs are `Long` or `String`,
never rounded. It runs on JVM 11+, on OkHttp and gson, with no other runtime dependencies.

Full guides, API reference and documentation: <https://ttspa.docs.isaackogan.com/sdks/kotlin/>

The guides cover [Authorization](https://ttspa.docs.isaackogan.com/sdks/kotlin/authorization/), [Calling the API](https://ttspa.docs.isaackogan.com/sdks/kotlin/calling-the-api/),
[Webhooks](https://ttspa.docs.isaackogan.com/sdks/kotlin/webhooks/) and [Errors](https://ttspa.docs.isaackogan.com/sdks/kotlin/errors/), and the [API reference](https://ttspa.docs.isaackogan.com/openapi/reference/) lists every operation and webhook.

[![Maven Central](https://img.shields.io/maven-central/v/com.isaackogan/tiktok-shop-api-kotlin?style=flat&color=0274b5)](https://central.sonatype.com/artifact/com.isaackogan/tiktok-shop-api-kotlin)
![JVM](https://img.shields.io/badge/jvm-11%2B-0274b5?style=flat)
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
- [TikTok Shop API for Python](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/python), `tiktok-shop-api` on PyPI
- [TikTok Shop API for Go](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/go), `github.com/isaackogan/TikTok-Shop-Api-SDKs/go`
- [TikTok Shop API for Java](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/java), `com.isaackogan:tiktok-shop-api` on Maven Central
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

1. Add the dependency from Maven Central

Gradle (Kotlin DSL):

```kts
dependencies {
    implementation("com.isaackogan:tiktok-shop-api-kotlin:0.1.0")
}
```

Maven:

```xml
<dependency>
  <groupId>com.isaackogan</groupId>
  <artifactId>tiktok-shop-api-kotlin</artifactId>
  <version>0.1.0</version>
</dependency>
```

It needs JVM 11 or newer.

2. Authorize a shop with OAuth and get an access token

```kotlin
import com.isaackogan.tiktok.shop.TikTokShopAuth
import com.isaackogan.tiktok.shop.TikTokShopAuthOptions

class OAuthExample {
    fun run() {
        val auth = TikTokShopAuth(
            TikTokShopAuthOptions(appKey = "YOUR_APP_KEY", appSecret = "YOUR_APP_SECRET", serviceId = "YOUR_SERVICE_ID"),
        )

        // 1. Send the seller to this page.
        val url = auth.authorizationUrl(TikTokShopAuth.AuthType.SELLER, TikTokShopAuth.Region.US, state = "my-state")

        // 2. TikTok redirects back with ?code=...; trade it for tokens.
        val tokens = auth.exchangeCode("CODE_FROM_THE_REDIRECT")

        // 3. Later, trade the refresh token for new tokens.
        val fresh = auth.refresh(tokens.refreshToken)
    }
}
```

`AuthType` is `SELLER`, `PARTNER` or `CREATOR`; `Region` is `US` or `ROW`. Seller and partner URLs need your
`serviceId`. Token requests never follow redirects and never put your secret in an error message.

3. Make your first call

```kotlin
import com.isaackogan.tiktok.shop.TikTokShop
import com.isaackogan.tiktok.shop.TikTokShopException
import com.isaackogan.tiktok.shop.TikTokShopOptions

class FirstCall {
    fun run() {
        val client = TikTokShop(
            TikTokShopOptions(appKey = "YOUR_APP_KEY", appSecret = "YOUR_APP_SECRET", accessToken = "ACCESS_TOKEN"),
        )

        try {
            val shops = client.authorization.getAuthorizedShops()
            println(shops.data?.shops?.firstOrNull()?.cipher)
        } catch (e: TikTokShopException) {
            println("TikTok said ${e.code}: ${e.message} (request ${e.requestId})")
        }
    }
}
```

Pass `shopCipher = "..."` in the options and every operation that needs one gets it.

## Params and Options

To create a new client, pass a `TikTokShopOptions`.

`TikTokShop(TikTokShopOptions(...))`

| Param Name | Required | Description |
|------------|----------|-------------|
| `appKey` | Yes | Your app key. |
| `appSecret` | Yes | Your app secret. It signs every request. |
| `accessToken` | No | The seller's access token, sent as the `x-tts-access-token` header. Null or empty sends none. |
| `shopCipher` | No | The shop's cipher, added to the operations that take one. Null or empty adds none. `authorization.getAuthorizedShops()` returns it. |
| `baseUrl` | No | Default `DEFAULT_BASE_URL` (`https://open-api.tiktokglobalshop.com`). It must be an origin such as `https://host:8443`, with no path prefix: signing and shop-cipher matching use the request path. |
| `timeout` | No | A `Duration` that bounds one request, response body included. Without it, `DEFAULT_TIMEOUT` (30 seconds) applies to the default HTTP client, and a client you supply keeps its own timeouts. |
| `httpClient` | No | Your own `OkHttpClient`, used as is: its connection pool, proxy, TLS settings, interceptors, timeouts and redirect policy apply. The default honours the JVM's proxy settings and never follows a redirect (a 3xx surfaces as a `TikTokShopException` carrying the status). |

The OAuth helper takes a `TikTokShopAuthOptions`.

`TikTokShopAuth(TikTokShopAuthOptions(...))`

| Param Name | Required | Description |
|------------|----------|-------------|
| `appKey` | Yes | Your app key. |
| `appSecret` | Yes | Your app secret. |
| `serviceId` | No | Your Partner Center service ID. `SELLER` and `PARTNER` URLs need it. |
| `baseUrl` | No | Default `DEFAULT_AUTH_BASE_URL` (`https://auth.tiktok-shops.com`). An origin, with no path prefix. |
| `timeout` | No | Bounds one token request. Without it, `DEFAULT_AUTH_TIMEOUT` (30 seconds) applies unless you supply an `httpClient`. |
| `httpClient` | No | Carries the token requests (proxy, TLS, ...). Even on your client, token calls never follow a redirect, because the URL holds the app secret and the code: a 3xx is a `TikTokShopException` whose code is the status. |

Requests carry the User-Agent `tiktok-shop-api-kotlin/<version>`.

## Methods

Each API group is a property of the client: `affiliateCreator`, `affiliatePartner`, `affiliateSeller`, `analytics`,
`authorization`, `customerEngagement`, `customerService`, `event`, `finance`, `fulfilledByTikTok`, `fulfillment`,
`logistics`, `orders`, `products`, `promotion`, `returnAndRefund`, `seller`, `supplyChain` and `tools`. Each is the
concrete generated API class, so your IDE completes the operations and models.

| Method Name | Description |
|-------------|-------------|
| `client.withShop(accessToken, shopCipher)` | Returns a client for another shop or token that shares the HTTP client and connection pool. An argument you leave out keeps this client's value; one you pass as `null` clears it. See [Many shops](#many-shops). |
| `auth.authorizationUrl(type, region, state = null)` | Builds the URL to send a seller, partner or creator to. |
| `auth.exchangeCode(code)` | Trades the `code` from the redirect for a `TokenSet`. |
| `auth.refresh(refreshToken)` | Trades a refresh token for a new `TokenSet`. |
| `Webhooks.verify(appKey, appSecret, rawBody, signature)` | Checks a webhook's `Authorization` header against the raw body (`ByteArray` or `String`). Returns `true` or `false`. |
| `Webhooks.parse(rawBody)` | Parses a body into a `WebhookEvent`. Throws `IllegalArgumentException` for a body it cannot read. |
| `Webhooks.verifyAndParse(appKey, appSecret, rawBody, signature)` | Verifies, then parses. Throws `WebhookSignatureException` when the signature does not match. |

A `TokenSet` holds `accessToken`, `refreshToken`, their expiry times, and (when TikTok sends them) `openId`,
`sellerName`, `sellerBaseRegion`, `userType` and `grantedScopes`. Its `toString()` hides the tokens.

## Examples

### Handle errors

Every failure is a `TikTokShopException` with `code`, `message`, `requestId`, `httpStatus` and the original exception
as `cause`:

| What happened | `code` | `httpStatus` |
|---|---|---|
| TikTok's reply has a non-zero `code`, even on HTTP 200 | TikTok's code | the status |
| A non-2xx reply | TikTok's non-zero code if the body has one, else the HTTP status | the status |
| A 2xx reply that can't be read: not a JSON object, a `code` that isn't an integer, a body gson can't decode into its model, or a token reply without `data` | -1 | the status |
| No HTTP response at all: connection refused, DNS, TLS, or a timeout | -1 | `null` |

gson does not check required properties of a response model: one TikTok leaves out arrives as `null` even where the
Kotlin type is non-null.

### Many shops

```kotlin
import com.isaackogan.tiktok.shop.TikTokShop

class ManyShops {
    fun run(client: TikTokShop) {
        // Same HTTP client and connection pool, different shop. The original is not changed.
        val shop = client.withShop(accessToken = "OTHER_ACCESS_TOKEN", shopCipher = "OTHER_SHOP_CIPHER")
    }
}
```

An argument you leave out keeps this client's value; one you pass as `null` clears it.

### Webhooks

```kotlin
import com.isaackogan.tiktok.shop.WebhookEvent
import com.isaackogan.tiktok.shop.WebhookSignatureException
import com.isaackogan.tiktok.shop.Webhooks

class WebhookExample {
    /** Call with the body bytes exactly as received, and the Authorization header. */
    fun handle(rawBody: ByteArray, authorizationHeader: String?) {
        val event = try {
            Webhooks.verifyAndParse("YOUR_APP_KEY", "YOUR_APP_SECRET", rawBody, authorizationHeader)
        } catch (e: WebhookSignatureException) {
            return // respond 401
        }

        when (event) {
            is WebhookEvent.OrderStatusChange -> println(event.payload.data?.orderId)
            is WebhookEvent.Unknown -> println("a webhook type this SDK does not know: ${event.type}")
            else -> {}
        }
    }
}
```

- `WebhookEvent` is a sealed class with one subclass per webhook type (each holds the generated payload model in
  `payload`) plus `Unknown(type, raw)`. The subclasses are rendered from the spec, so they stay in sync. They live in the
  generated folder but in the package `com.isaackogan.tiktok.shop`, because a sealed class's subclasses must share its
  package.
- Verify against the raw bytes as received: re-serializing the JSON changes the signature.
- Parsing is strict. A body that is not a JSON object, a `type` that is missing or not an integer, or a known type with
  a required property missing or null throws `IllegalArgumentException`: a known type missing a required field is a
  parse error. Answer that with 400, and a `WebhookSignatureException` with 401. An integer `type` this SDK does not
  know becomes `WebhookEvent.Unknown`. Unknown fields are ignored.
- `Webhooks.EVENT_TYPES` maps a type to its name, for example `1` to `ORDER_STATUS_CHANGE`.

### GET requests with a body

Three operations are GETs with a body (`getConversationList`, `mapTokopediaToTikTokShopProductIDs`,
`getShippingTemplateAvailability`). OkHttp cannot send those, so they go through the JDK's HTTP client; see
`TikTokShopOptions.httpClient` for which of your client's settings apply. The JDK client cannot use a SOCKS proxy: with
one set on your `OkHttpClient`, those three calls fail with a `TikTokShopException` (code -1) instead of going direct.

## Frequently Asked Questions

### How do I get a TikTok Shop access token in Kotlin?

Create a `TikTokShopAuth` with your app key, app secret and service ID, send the seller to `authorizationUrl()`, then
trade the `code` TikTok sends back with `exchangeCode()`. Call `refresh()` before the access token expires. See
[Getting Started](#getting-started).

### What is a shop cipher, and where do I find it?

Most TikTok Shop API endpoints act on one shop and need a `shop_cipher` query parameter. Call
`client.authorization.getAuthorizedShops()` with the seller's access token: each shop in the reply has a `cipher`. Pass
it as `shopCipher` in `TikTokShopOptions` and the client adds it to every endpoint that needs it.

### How do I verify TikTok Shop webhooks in Ktor or Spring?

Read the request body as a `ByteArray`, exactly as received, and pass it with the `Authorization` header to
`Webhooks.verifyAndParse`. Don't deserialize it first, because re-serialized JSON no longer matches the signature. See
[Webhooks](#webhooks).

### Can one app manage many TikTok Shop sellers?

Yes. Keep one client per shop with `withShop`. They share one HTTP client and connection pool. See
[Many shops](#many-shops).

### Which TikTok Shop API versions does it cover?

Every endpoint in TikTok's partner documentation, from API version 202309 onwards, and every documented webhook.

### Is this affiliated with TikTok?

No. It is an independent open-source project, built from TikTok's partner documentation.

### Is this available in other languages?

Yes. See [Do you prefer other programming languages?](#do-you-prefer-other-programming-languages) for the TypeScript,
Python, Go, Java, PHP, Rust and C# SDKs.

## Contributors

* **Isaac Kogan** - *Creator & Maintainer* - [isaackogan](https://github.com/isaackogan)

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/LICENSE) file for details.

Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.
