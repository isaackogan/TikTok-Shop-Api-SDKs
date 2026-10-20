---
title: Calling the API
description: Create the TikTokShop client, call operations by API area, work with many shops, and set the Guzzle HTTP client in PHP.
sidebar:
  order: 3
---

`TikTokShop` is the API client. Each request it sends gets the following automatically:
- the `app_key`, `timestamp` and `sign` query parameters;
- your access token, in the `x-tts-access-token` header;
- `shop_cipher`, on the operations that need one.

```php
use TikTokShop\Api\TikTokShop;

$shop = new TikTokShop(
    appKey: 'YOUR_APP_KEY',
    appSecret: 'YOUR_APP_SECRET',
    accessToken: 'THE_SELLER_ACCESS_TOKEN',
    shopCipher: 'THE_SHOP_CIPHER',
);

// Every request is signed, and shop_cipher is added to the operations that take one.
$orders = $shop->orders->getOrderList(20);
foreach ($orders->getData()->getOrders() as $order) {
    echo $order->getId(), PHP_EOL;
}
```

Without a shop cipher, `$shop->authorization->getAuthorizedShops()` returns the shops, and each has a cipher; see the [overview](/sdks/php/).

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

## Parameters

The generated methods take their parameters positionally, in the order of the generated signature. The `shop_cipher` parameter is not among them: the client adds it. Method names follow the [API reference](/openapi/reference/), in camel case. Responses and request bodies are PHP classes with getters and setters, and 64-bit IDs are never rounded.

## Many shops

`withShop` returns a client for another shop. It shares the HTTP client, and the original is not changed, so you can keep one per shop:

```php
use TikTokShop\Api\TikTokShop;

$shop = new TikTokShop(appKey: 'YOUR_APP_KEY', appSecret: 'YOUR_APP_SECRET', accessToken: 'TOKEN_A', shopCipher: 'CIPHER_A');

// Another shop, sharing the HTTP client. $shop is not changed.
$other = $shop->withShop(accessToken: 'TOKEN_B', shopCipher: 'CIPHER_B');

// An argument you leave out keeps this client's value; null (or '') clears it.
$sameShopNewToken = $shop->withShop(accessToken: 'TOKEN_A2');
$noShop = $shop->withShop(shopCipher: null);
```

## Options

`TikTokShop` takes these named constructor arguments:

| Option | Meaning |
| --- | --- |
| `appKey`, `appSecret` | Your app's credentials. |
| `accessToken` | The seller's access token, sent in `x-tts-access-token`. |
| `shopCipher` | The shop cipher added to operations that need one. |
| `baseUrl` | The API host, an origin such as `https://host:8443` with no path prefix: signing and shop-cipher matching use the request path. Defaults to `https://open-api.tiktokglobalshop.com`. |
| `timeout` | Seconds for the whole request, for the client the SDK builds. Defaults to 30 (`DEFAULT_TIMEOUT`); 0 means no limit. A negative value throws `InvalidArgumentException`. |
| `httpClient` | A Guzzle `ClientInterface`, used as is. |

## HTTP client

By default the SDK builds a Guzzle client that never follows redirects, with a 30 second timeout and Guzzle's default proxy behaviour. A 3xx reply is thrown as a `TikTokShopException` carrying the status, so the access token is never forwarded to another host. Pass your own with `httpClient:`; it is used as is, so its redirect policy applies. The OAuth token calls are the exception: they never follow redirects, even on your client, because their URL holds your app secret.

Three operations are GETs with a body: `getConversationList`, `mapTokopediaToTikTokShopProductIDs` and `getShippingTemplateAvailability`. The SDK sends the body and signs it.

Requests carry the User-Agent `tiktok-shop-api-php/<version>`, which `TikTokShop::userAgent()` returns.
