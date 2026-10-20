# tiktok-shop-api: TikTok Shop API client for Java

A typed Java client for the **TikTok Shop API** (the TikTok Shop Partner API). It covers over 300 operations across orders, products, fulfillment, logistics, finance, affiliate, customer service and more.

It signs requests for you, handles OAuth, works with many shops at once, and verifies and types TikTok Shop webhooks.

> Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.
>
> Request signing follows TikTok's documentation and has not been verified against the live API. If TikTok rejects a signature, please open an issue at https://github.com/isaackogan/TikTok-Shop-Api-SDKs/issues.

The client is generated from an OpenAPI v3 spec built from TikTok's partner documentation, so it tracks the docs: [tiktok-shop.openapi.yaml](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/.openapi/tiktok-shop.openapi.yaml).

## Install

Requires **Java 11 or newer**. Version `0.1.0`.

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

## OAuth: get an access token

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

`TikTokShopAuth.AuthType` is `SELLER`, `PARTNER` or `CREATOR`; `Region` is `US` or `ROW`. Failures raise `TikTokShopException`, and its message never contains your app secret, auth code or refresh token.

## Make your first call

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

Each API group is a getter on the client (`orders()`, `products()`, `fulfillment()`, `finance()`, ...) returning the generated API class. Signing, `app_key`, `timestamp`, the `x-tts-access-token` header and `shop_cipher` are added for you.

## Errors

Every failed call raises the unchecked `TikTokShopException` (`getCode()`, `getMessage()`, `getRequestId()`, `getHttpStatus()`, and the original exception as `getCause()`):

| What happened | `getCode()` | `getHttpStatus()` |
|---|---|---|
| TikTok's reply has a non-zero `code`, even on HTTP 200 | TikTok's code | the status |
| A non-2xx reply | TikTok's non-zero code if the body has one, else the HTTP status | the status |
| A 2xx reply that can't be read: not a JSON object, a `code` that isn't an integer, a body that doesn't fit its model, or a token reply without `data` | -1 | the status |
| No HTTP response at all: connection refused, DNS, TLS, or a timeout | -1 | `null` |

The generated methods also declare the checked `ApiException`, which can still surface for client-side problems such as a missing required parameter, so catch or declare both.

The `*Async` methods report every failure to `ApiCallback.onFailure` as an `ApiException` whose `getCause()` is the `TikTokShopException` (its `getCode()` is the HTTP status, 0 when no response arrived).

## Options

- `baseUrl` (on both builders) must be an origin such as `https://host:8443`, with no path prefix: signing and shop-cipher matching use the request path.
- `timeout` bounds one request, 30 seconds by default.
- Requests carry the User-Agent `tiktok-shop-api-java/<version>`.
- The three GET operations that carry a body are sent with `java.net.http`, which cannot use a SOCKS proxy: with one configured on your `OkHttpClient`, those calls fail with a `TikTokShopException` (code -1) instead of going direct.

## Many shops

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

## Webhooks

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

`parse` picks the model from the integer `type`, so a `WebhookEvent` is one of the generated event classes (`OrderStatusChangeEvent`, ...), each with `getPayload()`, or an `UnknownWebhookEvent` (`getType()`, `getRaw()`) for a type this SDK does not know. Use `instanceof`, or `event.accept(visitor)` with a `WebhookEventVisitor`. Parsing is strict: a body that is not a JSON object, a `type` that is missing or not an integer, or a known type with a required field missing or null is rejected with an `IllegalArgumentException`. In short, a known type missing a required field is a parse error.

Verify against the **raw** body: re-serializing it changes the bytes and the signature will not match. Big IDs such as `shop_id` keep their exact digits. `Webhooks.EVENT_TYPES` maps a type number to its event name.

## About

Unofficial. Not affiliated with or endorsed by TikTok or ByteDance. MIT licensed. Source and issues: <https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/java>.
