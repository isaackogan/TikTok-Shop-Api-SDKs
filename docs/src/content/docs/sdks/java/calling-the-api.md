---
title: Calling the API
description: Build the TikTokShop client, call operations by API group, work with many shops, and configure timeouts and the HTTP client in Java.
sidebar:
  order: 3
---

`TikTokShop` is the API client. Each request it sends gets the following automatically:
- the `app_key`, `timestamp` and `sign` query parameters;
- your access token, in the `x-tts-access-token` header;
- `shop_cipher`, on the operations that need one.

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

## API groups

One getter per API group hangs off the client, matching the spec's tags. Each returns the generated API class, so your IDE completes the operations and models.

| Getter | Area |
| --- | --- |
| `affiliateCreator()`, `affiliatePartner()`, `affiliateSeller()` | Affiliate creator, partner and seller |
| `analytics()` | Analytics |
| `authorization()` | Authorization, including `getAuthorizedShops` |
| `customerEngagement()`, `customerService()` | Customer engagement and customer service |
| `event()` | Event (webhook subscriptions) |
| `finance()` | Finance |
| `fulfilledByTikTok()` | Fulfilled by TikTok (FBT) |
| `fulfillment()`, `logistics()` | Fulfillment and logistics |
| `orders()`, `products()`, `promotion()` | Orders, products and promotion |
| `returnAndRefund()` | Return and refund |
| `seller()`, `supplyChain()`, `tools()` | Seller, supply chain and tools |

Operation and parameter names follow the [API reference](/openapi/reference/), in camel case. Every generated method declares the checked `ApiException`; see [errors](/sdks/java/errors/).

## Many shops

`withShop` returns a client for another shop. It shares the HTTP client and connection pool, and the original is not changed, so you can keep one per shop:

```java
import com.isaackogan.tiktok.shop.TikTokShop;

class ManyShops {
    void run(TikTokShop client) {
        // Same HTTP client and connection pool, different shop. The original is not changed.
        TikTokShop shop = client.withShop("OTHER_ACCESS_TOKEN", "OTHER_SHOP_CIPHER");
    }
}
```

A value you leave out of `withShop(ShopCredentials)` keeps the current one; `null` or `""` clears it. The two-argument `withShop(accessToken, shopCipher)` sets both values.

## Options

Set these on `TikTokShop.builder()`. `appKey` and `appSecret` are required: `build()` throws `IllegalStateException` without them.

| Option | Meaning |
| --- | --- |
| `appKey`, `appSecret` | Your app's credentials. |
| `accessToken` | The seller's access token, sent in `x-tts-access-token`. Null or empty sends none. |
| `shopCipher` | The shop cipher added to operations that need one. Null or empty adds none. |
| `baseUrl` | The API host, an origin such as `https://host:8443` with no path prefix: signing and shop-cipher matching use the request path. Defaults to `https://open-api.tiktokglobalshop.com` (`DEFAULT_BASE_URL`). |
| `timeout` | A `Duration` bounding one request, response body included. Defaults to 30 seconds (`DEFAULT_TIMEOUT`) for the default HTTP client; an `httpClient` you supply keeps its own timeouts. |
| `httpClient` | An `OkHttpClient` to carry the signed requests. Its connection pool, proxy, TLS settings, interceptors and timeouts are used as they are. |

The default client never follows a redirect. A 3xx reply is thrown as a `TikTokShopException` carrying the status, so the access token is never forwarded to another host. An `httpClient` you supply keeps its own redirect policy.

Three operations are GET requests with a body: `getConversationList`, `mapTokopediaToTikTokShopProductIDs` and `getShippingTemplateAvailability`. OkHttp cannot send those, so they go through `java.net.http`. For them only these settings of your `OkHttpClient` apply: an HTTP proxy (`proxy()`, or else `proxySelector()`), the connect timeout, and the call timeout (or else the read timeout). SOCKS proxies, authenticators, custom TLS settings, DNS, and interceptors that run after the signing one do not apply. With a SOCKS proxy configured, those calls fail with a `TikTokShopException` (code -1) instead of going direct.

Requests carry the User-Agent `tiktok-shop-api-java/<version>`. `TikTokShop.requiresShopCipher(method, path)` reports whether an operation takes a `shop_cipher`.

The generated API classes also have `*Async` methods. They are enqueued on the OkHttp client's dispatcher, so async calls honour its `maxRequests` and `maxRequestsPerHost` limits (64 and 5 by default; set them on the `Dispatcher` of a client you pass to `httpClient`). See [errors](/sdks/java/errors/) for how they report failures.
