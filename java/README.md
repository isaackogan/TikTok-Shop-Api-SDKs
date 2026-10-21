# TikTok Shop API for Java (Unofficial)

[TikTok Shop API](https://partner.tiktokshop.com/) Client for Java (Unofficial, Unaffiliated with TikTok or ByteDance Ltd.)

A typed Java client for the TikTok Shop API, also called the TikTok Shop Partner API or Open API. It covers over 300
operations across orders, products, fulfillment, logistics, returns and refunds, finance, promotions, affiliate,
analytics and customer service, for sellers, partners and creators.

Every request is signed with HMAC-SHA256 and sent with your access token, and the shop cipher is added wherever an
endpoint needs it. The OAuth helper builds the authorization URL and exchanges and refreshes tokens. One client can
serve many shops, and TikTok Shop webhooks are verified and parsed into typed events. The client is generated from an
OpenAPI v3 spec built from TikTok's partner documentation, so it tracks the docs.

Full guides, API reference and documentation: <https://ttspa.docs.isaackogan.com/sdks/java/>

The guides cover [Authorization](https://ttspa.docs.isaackogan.com/sdks/java/authorization/), [Calling the API](https://ttspa.docs.isaackogan.com/sdks/java/calling-the-api/),
[Webhooks](https://ttspa.docs.isaackogan.com/sdks/java/webhooks/) and [Errors](https://ttspa.docs.isaackogan.com/sdks/java/errors/), and the [API reference](https://ttspa.docs.isaackogan.com/openapi/reference/) lists every operation and webhook.

[![Maven Central](https://img.shields.io/maven-central/v/com.isaackogan/tiktok-shop-api?style=flat&color=0274b5)](https://central.sonatype.com/artifact/com.isaackogan/tiktok-shop-api)
![Java](https://img.shields.io/badge/java-11%2B-0274b5?style=flat)
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

1. Add the dependency from Maven Central

Version `0.1.0` needs Java 11 or newer.

Maven:

```xml
<dependency>
  <groupId>com.isaackogan</groupId>
  <artifactId>tiktok-shop-api</artifactId>
  <version>0.1.0</version>
</dependency>
```

Gradle:

```groovy
implementation 'com.isaackogan:tiktok-shop-api:0.1.0'
```

2. Authorize a shop with OAuth and get an access token

```java
import com.isaackogan.tiktok.shop.TikTokShopAuth;
import com.isaackogan.tiktok.shop.TokenSet;

class OAuthExample {
    void run() {
        TikTokShopAuth auth = TikTokShopAuth.builder()
                .appKey("YOUR_APP_KEY")
                .appSecret("YOUR_APP_SECRET")
                .serviceId("YOUR_SERVICE_ID")
                .build();

        // 1. Send the seller to this page.
        String url = auth.authorizationUrl(TikTokShopAuth.AuthType.SELLER, TikTokShopAuth.Region.US, "my-state");

        // 2. TikTok redirects back with ?code=...; trade it for tokens.
        TokenSet tokens = auth.exchangeCode("CODE_FROM_THE_REDIRECT");

        // 3. Later, trade the refresh token for new tokens.
        TokenSet fresh = auth.refresh(tokens.getRefreshToken());
    }
}
```

`TikTokShopAuth.AuthType` is `SELLER`, `PARTNER` or `CREATOR`; `Region` is `US` or `ROW`. Failures raise
`TikTokShopException`, and its message never contains your app secret, auth code or refresh token.

3. Make your first call

```java
import com.isaackogan.tiktok.shop.TikTokShop;
import com.isaackogan.tiktok.shop.generated.ApiException;
import com.isaackogan.tiktok.shop.generated.model.GetAuthorizedShopsResponse;

class FirstCall {
    void run() throws ApiException {
        TikTokShop client = TikTokShop.builder()
                .appKey("YOUR_APP_KEY")
                .appSecret("YOUR_APP_SECRET")
                .accessToken("ACCESS_TOKEN")
                .build();

        GetAuthorizedShopsResponse shops = client.authorization().getAuthorizedShops();
        System.out.println(shops.getData().getShops().get(0).getCipher());
    }
}
```

Signing, `app_key`, `timestamp` and the `x-tts-access-token` header are added to every call, and `shop_cipher` to the
operations that take one.

## Params and Options

To create a new client, use the builder. `build()` throws `IllegalStateException` without an app key and app secret.

`TikTokShop.builder()...build()`

| Param Name | Required | Description |
|------------|----------|-------------|
| `appKey` | Yes | Your app key. |
| `appSecret` | Yes | Your app secret. It signs every request. |
| `accessToken` | No | The seller's access token, sent as the `x-tts-access-token` header. Null or empty sends none. |
| `shopCipher` | No | The shop's cipher, added to the operations that take one. Null or empty adds none. `authorization().getAuthorizedShops()` returns it. |
| `baseUrl` | No | Default `TikTokShop.DEFAULT_BASE_URL` (`https://open-api.tiktokglobalshop.com`). It must be an origin such as `https://host:8443`, with no path prefix: signing and shop-cipher matching use the request path. |
| `timeout` | No | A `Duration` that bounds one request, response body included. Without it, `DEFAULT_TIMEOUT` (30 seconds) applies to the default HTTP client, and a client you supply keeps its own timeouts. |
| `httpClient` | No | Your own `OkHttpClient`, used as is: its connection pool, proxy, TLS settings, interceptors, timeouts and redirect policy apply. The default honours the JVM's proxy settings and never follows a redirect (a 3xx surfaces as a `TikTokShopException` carrying the status). |

The OAuth helper has its own builder.

`TikTokShopAuth.builder()...build()`

| Param Name | Required | Description |
|------------|----------|-------------|
| `appKey` | Yes | Your app key. |
| `appSecret` | Yes | Your app secret. |
| `serviceId` | No | Your Partner Center service ID. `SELLER` and `PARTNER` URLs need it. |
| `baseUrl` | No | Default `TikTokShopAuth.DEFAULT_BASE_URL` (`https://auth.tiktok-shops.com`). An origin, with no path prefix. |
| `timeout` | No | Bounds one token request. Without it, `DEFAULT_TIMEOUT` (30 seconds) applies unless you supply an `httpClient`. |
| `httpClient` | No | Carries the token requests (proxy, TLS, ...). Redirects are never followed, whatever this client says. |

Requests carry the User-Agent `tiktok-shop-api-java/<version>`.

## Methods

Each API group is a getter on the client: `affiliateCreator()`, `affiliatePartner()`, `affiliateSeller()`,
`analytics()`, `authorization()`, `customerEngagement()`, `customerService()`, `event()`, `finance()`,
`fulfilledByTikTok()`, `fulfillment()`, `logistics()`, `orders()`, `products()`, `promotion()`, `returnAndRefund()`,
`seller()`, `supplyChain()` and `tools()`. Each returns the generated API class.

| Method Name | Description |
|-------------|-------------|
| `client.withShop(accessToken, shopCipher)` | Returns a client for another shop or token that shares this client's HTTP client, base URL and timeout. `null` or `""` clears a value. See [Many shops](#many-shops). |
| `client.withShop(ShopCredentials)` | The same, but a value you leave out of the `ShopCredentials` keeps this client's value. |
| `auth.authorizationUrl(type, region[, state])` | Builds the URL to send a seller, partner or creator to. |
| `auth.exchangeCode(code)` | Trades the `code` from the redirect for a `TokenSet`. |
| `auth.refresh(refreshToken)` | Trades a refresh token for a new `TokenSet`. |
| `Webhooks.verify(appKey, appSecret, rawBody, signature)` | Checks a webhook's `Authorization` header against the raw body (`byte[]` or `String`). Returns `true` or `false`. |
| `Webhooks.parse(rawBody)` | Parses a body into a `WebhookEvent`. Throws `IllegalArgumentException` for a body it cannot read. |
| `Webhooks.verifyAndParse(appKey, appSecret, rawBody, signature)` | Verifies, then parses. Throws `WebhookSignatureException` when the signature does not match. |
| `event.accept(visitor)` | Dispatches a `WebhookEvent` to a `WebhookEventVisitor`, as an alternative to `instanceof`. |

A `TokenSet` has `getAccessToken()`, `getAccessTokenExpireIn()`, `getRefreshToken()` and `getRefreshTokenExpireIn()`,
plus `getOpenId()`, `getSellerName()`, `getSellerBaseRegion()`, `getUserType()` and `getGrantedScopes()` when TikTok
sends them.

## Examples

### Many shops

```java
import com.isaackogan.tiktok.shop.TikTokShop;

class ManyShops {
    void run(TikTokShop client) {
        // Same HTTP client and connection pool, different shop. The original is not changed.
        TikTokShop shop = client.withShop("OTHER_ACCESS_TOKEN", "OTHER_SHOP_CIPHER");
    }
}
```

A value you leave out of `withShop(ShopCredentials)` keeps the current one; `null` or `""` clears it.

### Webhooks

```java
import com.isaackogan.tiktok.shop.WebhookEvent;
import com.isaackogan.tiktok.shop.WebhookSignatureException;
import com.isaackogan.tiktok.shop.Webhooks;
import com.isaackogan.tiktok.shop.generated.event.OrderStatusChangeEvent;
import com.isaackogan.tiktok.shop.generated.model.OrderStatusChangeWebhook;

class WebhookExample {
    /** Call with the body bytes exactly as received, and the Authorization header. */
    void handle(byte[] rawBody, String authorizationHeader) {
        WebhookEvent event;
        try {
            event = Webhooks.verifyAndParse("YOUR_APP_KEY", "YOUR_APP_SECRET", rawBody, authorizationHeader);
        } catch (WebhookSignatureException e) {
            return; // respond 401
        }

        if (event instanceof OrderStatusChangeEvent) {
            OrderStatusChangeWebhook order = ((OrderStatusChangeEvent) event).getPayload();
            System.out.println(order.getData().getOrderId());
        }
    }
}
```

`parse` picks the model from the integer `type`, so a `WebhookEvent` is one of the generated event classes
(`OrderStatusChangeEvent`, ...), each with `getPayload()`, or an `UnknownWebhookEvent` (`getType()`, `getRaw()`) for a
type this SDK does not know. Use `instanceof`, or `event.accept(visitor)` with a `WebhookEventVisitor`. Parsing is
strict: a body that is not a JSON object, a `type` that is missing or not an integer, or a known type with a required
field missing or null is rejected with an `IllegalArgumentException`. In short, a known type missing a required field
is a parse error. Answer that with 400, and a `WebhookSignatureException` with 401.

Verify against the raw body: re-serializing it changes the bytes and the signature will not match. Big IDs such as
`shop_id` keep their exact digits. `Webhooks.EVENT_TYPES` maps a type number to its event name.

### Handle errors

Every failed call raises the unchecked `TikTokShopException` (`getCode()`, `getMessage()`, `getRequestId()`,
`getHttpStatus()`, and the original exception as `getCause()`):

| What happened | `getCode()` | `getHttpStatus()` |
|---|---|---|
| TikTok's reply has a non-zero `code`, even on HTTP 200 | TikTok's code | the status |
| A non-2xx reply | TikTok's non-zero code if the body has one, else the HTTP status | the status |
| A 2xx reply that can't be read: not a JSON object, a `code` that isn't an integer, a body that doesn't fit its model, or a token reply without `data` | -1 | the status |
| No HTTP response at all: connection refused, DNS, TLS, or a timeout | -1 | `null` |

The generated methods also declare the checked `ApiException`, which can still surface for client-side problems such as
a missing required parameter, so catch or declare both.

### Async calls

The `*Async` methods report every failure to `ApiCallback.onFailure` as an `ApiException` whose `getCause()` is the
`TikTokShopException` (its `getCode()` is the HTTP status, 0 when no response arrived). They are enqueued on the OkHttp
client's dispatcher, so async calls honour its `maxRequests` and `maxRequestsPerHost` limits (64 and 5 by default; set
them on the `Dispatcher` of a client you pass to `httpClient`).

### GET requests with a body

Three operations (`getConversationList`, `mapTokopediaToTikTokShopProductIDs` and `getShippingTemplateAvailability`) are
GETs with a body, which OkHttp cannot send, so they go through `java.net.http` instead. It cannot use a SOCKS proxy:
with one configured on your `OkHttpClient`, those calls fail with a `TikTokShopException` (code -1) instead of going
direct.

## Frequently Asked Questions

### How do I get a TikTok Shop access token in Java?

Build a `TikTokShopAuth` with your app key, app secret and service ID, send the seller to `authorizationUrl()`, then
trade the `code` TikTok sends back with `exchangeCode()`. Call `refresh()` before the access token expires. See
[Getting Started](#getting-started).

### What is a shop cipher, and where do I find it?

Most TikTok Shop API endpoints act on one shop and need a `shop_cipher` query parameter. Call
`client.authorization().getAuthorizedShops()` with the seller's access token: each shop in the reply has a cipher. Set
it with `shopCipher(...)` on the builder and the client adds it to every endpoint that needs it.

### How do I verify TikTok Shop webhooks in Spring Boot or another Java framework?

Read the request body as a `byte[]`, exactly as received, and pass it with the `Authorization` header to
`Webhooks.verifyAndParse`. Don't bind it to an object first, because re-serialized JSON no longer matches the signature.
See [Webhooks](#webhooks).

### Can one app manage many TikTok Shop sellers?

Yes. Keep one client per shop with `withShop`. They share one HTTP client and connection pool. See
[Many shops](#many-shops).

### Which TikTok Shop API versions does it cover?

Every endpoint in TikTok's partner documentation, from API version 202309 onwards, and every documented webhook.

### Is this affiliated with TikTok?

No. It is an independent open-source project, built from TikTok's partner documentation.

### Is this available in other languages?

Yes. See [Do you prefer other programming languages?](#do-you-prefer-other-programming-languages) for the TypeScript,
Python, Go, Kotlin, PHP, Rust and C# SDKs.

## Contributors

* **Isaac Kogan** - *Creator & Maintainer* - [isaackogan](https://github.com/isaackogan)

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/LICENSE) file for details.

Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.
