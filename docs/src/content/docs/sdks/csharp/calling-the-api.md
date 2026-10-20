---
title: Calling the API
description: Create the TikTokShopClient, call operations by API area, work with many shops, and set the HTTP handler in C#.
sidebar:
  order: 3
---

`TikTokShopClient` is the API client. Create **one** and reuse it for the life of your app: it owns the connection pool. Each request it sends gets the following automatically:
- the `app_key`, `timestamp` and `sign` query parameters;
- your access token, in the `x-tts-access-token` header;
- `shop_cipher`, on the operations that need one.

```csharp
using System;
using TikTokShop.Api;

var client = new TikTokShopClient(
    appKey: "YOUR_APP_KEY",
    appSecret: "YOUR_APP_SECRET",
    accessToken: "THE_SELLER_ACCESS_TOKEN",
    shopCipher: "THE_SHOP_CIPHER");

// Every request is signed, and shop_cipher is added to the operations that take one.
var orders = await client.Orders.GetOrderListAsync(pageSize: 20);
Console.WriteLine($"{orders.Data.TotalCount} orders");
```

## API areas

One property per API area hangs off the client, matching the spec's tags. Each is the concrete generated API class, so your IDE completes the operations and models (in `TikTokShop.Api.Generated.Model`).

| Property | Area |
| --- | --- |
| `AffiliateCreator`, `AffiliatePartner`, `AffiliateSeller` | Affiliate creator, partner and seller |
| `Analytics` | Analytics |
| `Authorization` | Authorization, including `GetAuthorizedShopsAsync` |
| `CustomerEngagement`, `CustomerService` | Customer engagement and customer service |
| `Event` | Event (webhook subscriptions) |
| `Finance` | Finance |
| `FulfilledByTikTok` | Fulfilled by TikTok (FBT) |
| `Fulfillment`, `Logistics` | Fulfillment and logistics |
| `Orders`, `Products`, `Promotion` | Orders, products and promotion |
| `ReturnAndRefund` | Return and refund |
| `Seller`, `SupplyChain`, `Tools` | Seller, supply chain and tools |

## Parameters

Every call is `async` with a `CancellationToken`, and has a synchronous twin. The generated methods take their parameters in the order of the generated signature, ending with an optional `CancellationToken`. The `shop_cipher` parameter is not among them: the client adds it. Method names follow the [API reference](/openapi/reference/), in Pascal case with an `Async` suffix. 64-bit IDs are never rounded.

## Many shops

`WithShop` returns a client for another shop. It shares this client's connections, and the original is not changed, so you can keep one per shop:

```csharp
using TikTokShop.Api;

var client = new TikTokShopClient("YOUR_APP_KEY", "YOUR_APP_SECRET", accessToken: "TOKEN_A", shopCipher: "CIPHER_A");

// Another shop, sharing this client's connections. `client` is not changed.
var other = client.WithShop(accessToken: "TOKEN_B", shopCipher: "CIPHER_B");

// An argument you leave out keeps this client's value; null (or "") clears it.
var sameShopNewToken = client.WithShop(accessToken: "TOKEN_A2");
var noShop = client.WithShop(shopCipher: new Optional<string?>(null));
```

## Options

`TikTokShopClient` takes these named constructor arguments, or a `TikTokShopOptions` object with the same members:

| Option | Meaning |
| --- | --- |
| `appKey`, `appSecret` | Your app's credentials. |
| `accessToken` | The seller's access token, sent in `x-tts-access-token`. |
| `shopCipher` | The shop cipher added to operations that need one. |
| `baseUrl` | The API host, an origin such as `https://host:8443` with no path prefix: signing and shop-cipher matching use the request path. Defaults to `https://open-api.tiktokglobalshop.com` (`DefaultBaseUrl`). |
| `timeout` | A `TimeSpan` for the whole exchange. Defaults to 30 seconds (`DefaultTimeout`); `TimeSpan.Zero` means no limit. |
| `handler` | An `HttpMessageHandler`, used as is for API calls, so its redirect, proxy and certificate settings apply. |

## HTTP client

By default the SDK builds a `SocketsHttpHandler` that never follows redirects, uses the system proxy, and recycles pooled connections every two minutes so DNS changes are picked up. A 3xx reply is a `TikTokShopException` with code 302, so the access token is never forwarded to another host. Pass your own `handler:`; its redirect policy applies to API calls. The OAuth calls never follow redirects: a handler with `AllowAutoRedirect` set to true is refused, because the token URL holds your app secret.

Three operations are GETs with a body: `GetConversationList`, `MapTokopediaToTikTokShopProductIDs` and `GetShippingTemplateAvailability`. The SDK sends the body and signs it.

Requests carry the User-Agent `tiktok-shop-api-csharp/<version>`, exposed as `TikTokShopClient.UserAgent`.
