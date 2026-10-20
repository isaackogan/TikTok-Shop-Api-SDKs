# TikTok Shop API for Kotlin

A Kotlin client for the **TikTok Shop API** (the TikTok Shop Partner API / Open API). It covers every endpoint in the published spec, signs every request, ships an OAuth helper, and parses webhooks into a sealed class you narrow with `when`.

Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.

- **Every TikTok Shop API endpoint**, grouped like TikTok's own docs: `client.orders`, `client.products`, `client.fulfillment`, `client.finance`, and 15 more.
- **Typed models.** Generated from the [OpenAPI spec](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/.openapi/tiktok-shop.openapi.yaml), so requests and responses are Kotlin data classes. 64-bit IDs are `Long` or `String`, never rounded.
- **Request signing** (HMAC-SHA256), `app_key`, `timestamp`, `shop_cipher` and the `x-tts-access-token` header added for you.
- **OAuth helper** for the authorization URL, code exchange and token refresh.
- **Webhooks**: verify the signature, then get a `WebhookEvent` for any of the webhook types.
- **JVM 11+**, on OkHttp and gson. No other runtime dependencies.

> Request signing follows TikTok's documentation and has not been verified against the live API.

## Install

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

Needs JVM 11 or newer.

## Authorize a shop (OAuth)

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

`AuthType` is `SELLER`, `PARTNER` or `CREATOR`; `Region` is `US` or `ROW`. Seller and partner URLs need your `serviceId`. A `TokenSet` holds `accessToken`, `refreshToken`, their expiry times, and (when TikTok sends them) `openId`, `sellerName`, `sellerBaseRegion`, `userType` and `grantedScopes`. Its `toString()` hides the tokens. Token requests never follow redirects and never put your secret in an error message.

## Make your first call

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

Pass `shopCipher = "..."` in the options and every operation that needs one gets it. Every failure is a `TikTokShopException` with `code`, `message`, `requestId` and (for HTTP errors) `httpStatus`: an envelope with `code != 0`, a non-2xx status, a body that is not JSON, a network error or a timeout. `TikTokShopOptions` also takes `baseUrl`, `timeout` and your own `OkHttpClient`.

## Many shops

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

## Webhooks

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

- `WebhookEvent` is a sealed class with one subclass per webhook type (each holds the generated payload model in `payload`) plus `Unknown(type, raw)`. The subclasses are rendered from the spec, so they stay in sync. They live in the generated folder but in the package `com.isaackogan.tiktok.shop`, because a sealed class's subclasses must share its package.
- Verify against the **raw bytes** as received: re-serializing the JSON changes the signature.
- A body whose `type` is missing or not an integer, or whose payload lacks a property its model requires, throws `IllegalArgumentException`. An integer `type` this SDK does not know becomes `WebhookEvent.Unknown`. Unknown fields are ignored.
- `Webhooks.EVENT_TYPES` maps a type to its name, for example `1` to `ORDER_STATUS_CHANGE`.

## API surface

The client's properties are the API groups: `affiliateCreator`, `affiliatePartner`, `affiliateSeller`, `analytics`, `authorization`, `customerEngagement`, `customerService`, `event`, `finance`, `fulfilledByTikTok`, `fulfillment`, `logistics`, `orders`, `products`, `promotion`, `returnAndRefund`, `seller`, `supplyChain`, `tools`. Each is the concrete generated API class, so your IDE completes the operations and models.

## Notes

- Generated from [the spec](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/.openapi/tiktok-shop.openapi.yaml) in the [TikTok-Shop-Api-SDKs](https://github.com/isaackogan/TikTok-Shop-Api-SDKs) repository, which also has SDKs for TypeScript, Python, Go, Java, PHP, Rust and C#.
- Three operations are GETs with a body (`getConversationList`, `mapTokopediaToTikTokShopProductIDs`, `getShippingTemplateAvailability`). OkHttp cannot send those, so they go through the JDK's HTTP client; see `TikTokShopOptions.httpClient` for which of your client's settings apply.

## License

MIT
