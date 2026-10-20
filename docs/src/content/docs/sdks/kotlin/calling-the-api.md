---
title: Calling the API
description: Create the TikTokShop client, call operations by API area, work with many shops, and set options in Kotlin.
sidebar:
  order: 3
---

`TikTokShop` is the API client. Each request it sends gets the following automatically:
- the `app_key`, `timestamp` and `sign` query parameters;
- your access token, in the `x-tts-access-token` header;
- `shop_cipher`, on the operations that need one.

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

## API areas

One property per API area hangs off the client, matching the spec's tags. Each is the concrete generated API class, so your IDE completes the operations and models.

| Property | Area |
| --- | --- |
| `affiliateCreator`, `affiliatePartner`, `affiliateSeller` | Affiliate creator, partner and seller |
| `analytics` | Analytics |
| `authorization` | Authorization, including `getAuthorizedShops` |
| `customerEngagement`, `customerService` | Customer engagement and customer service |
| `event` | Event (webhook subscriptions) |
| `finance` | Finance |
| `fulfilledByTikTok` | Fulfilled by TikTok (FBT) |
| `fulfillment`, `logistics` | Fulfillment and logistics |
| `orders`, `products`, `promotion` | Orders, products and promotion |
| `returnAndRefund` | Return and refund |
| `seller`, `supplyChain`, `tools` | Seller, supply chain and tools |

Operation and parameter names follow the [API reference](/openapi/reference/), in camel case. 64-bit IDs are `Long` or `String`, never rounded.

## Many shops

`withShop` returns a client for another shop. It shares the HTTP client and connection pool, and the original is not changed, so you can keep one per shop:

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

## Options

`TikTokShopOptions` takes:

| Option | Meaning |
| --- | --- |
| `appKey`, `appSecret` | Your app's credentials. |
| `accessToken` | The seller's access token, sent in `x-tts-access-token`. |
| `shopCipher` | The shop cipher added to operations that need one. |
| `baseUrl` | The API host, an origin such as `https://host:8443` with no path prefix: signing and shop-cipher matching use the request path. Defaults to `https://open-api.tiktokglobalshop.com`. |
| `timeout` | A `Duration` bounding one request, response body included. Defaults to 30 seconds (`DEFAULT_TIMEOUT`) for the default HTTP client; an `httpClient` you supply keeps its own timeouts. |
| `httpClient` | Your own `OkHttpClient`. Its connection pool, proxy, TLS settings, interceptors and timeouts are used as they are. |

The default client never follows a redirect. A 3xx reply is thrown as a `TikTokShopException` carrying the status, so the access token is never forwarded to another host. An `httpClient` you supply keeps its own redirect policy.

Three operations are GET requests with a body: `getConversationList`, `mapTokopediaToTikTokShopProductIDs` and `getShippingTemplateAvailability`. OkHttp cannot send those, so they go through the JDK's HTTP client. For them only these settings of your `OkHttpClient` apply: an HTTP proxy (`proxy`, or else `proxySelector`), the connect timeout, and the call timeout (or else the read timeout). SOCKS proxies, authenticators, custom TLS settings, DNS, and interceptors that run after the signing one do not apply. With a SOCKS proxy set, those calls fail with a `TikTokShopException` (code -1) instead of going direct.

Requests carry the User-Agent `tiktok-shop-api-kotlin/<version>`.
