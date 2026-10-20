---
title: Calling the API
description: Create the TikTokShop client, call operations by API area, work with many shops, and handle 64-bit IDs in TypeScript.
sidebar:
  order: 3
---

`TikTokShop` is the API client. Each request it sends gets the following automatically:
- the `app_key`, `timestamp` and `sign` query parameters;
- your access token, in the `x-tts-access-token` header;
- `shop_cipher`, on the operations that need one.

```ts
import { TikTokShop } from 'tiktok-shop-api';

const client = new TikTokShop({
  appKey: process.env.TTS_APP_KEY!,
  appSecret: process.env.TTS_APP_SECRET!,
  accessToken: tokens.accessToken,
});

// Find the shop cipher
const shops = await client.authorization.getAuthorizedShops();
const shopCipher = shops.data?.shops?.[0]?.cipher;

const seller = client.withShop({ accessToken: tokens.accessToken, shopCipher });
const orders = await seller.orders.getOrderList({ pageSize: 20 });
```

## API areas

One property per API area hangs off the client, matching the spec's tags:

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

Each method takes one object with the operation's parameters and request body, and resolves with the response envelope (`code`, `message`, `requestId`, `data`). Method and parameter names follow the [API reference](/openapi/reference/), in camel case.

## Many shops

`withShop` returns a client for another shop. It shares the HTTP client and your app credentials, so you can keep one per shop:

```ts
const shopA = client.withShop({ accessToken: tokenA, shopCipher: cipherA });
const shopB = client.withShop({ accessToken: tokenB, shopCipher: cipherB });
```

## IDs are strings

TikTok Shop IDs (`shop_id`, `order_id`, `product_id`, ...) are 64-bit integers, which JavaScript numbers cannot hold exactly. This client reads them as **strings** in every response and webhook, and sends them back as the numbers TikTok expects. For example, `7494049642642441621` stays `"7494049642642441621"`.

## Options

| Option | Meaning |
| --- | --- |
| `appKey`, `appSecret` | Your app's credentials. |
| `accessToken` | The seller's access token, sent in `x-tts-access-token`. |
| `shopCipher` | The shop cipher added to operations that need one. |
| `baseUrl` | The API host, an origin such as `https://host:8443` with no path prefix: signing and shop-cipher matching use the request path. Defaults to `https://open-api.tiktokglobalshop.com`. |
| `timeoutMs` | Per-request timeout. Defaults to 30 seconds (`DEFAULT_TIMEOUT_MS`); 0 means no limit. |
| `fetch` | An HTTP client override, defaulting to the global `fetch`. |

The default client never follows a redirect. A 3xx reply is thrown as a `TikTokShopError` whose `code` and `httpStatus` are the status, so the access token is never forwarded to another host. A `fetch` you supply keeps its own redirect policy.

Some operations are GET requests with a JSON body, which `fetch` refuses. The client sends those with `node:http` or `node:https` instead.

Requests carry the User-Agent `tiktok-shop-api-typescript/<version>`, exported as `USER_AGENT`. The signing functions are exported too (`sign`, `stringToSign` and `requiresShopCipher`), for checking a signature by hand.
