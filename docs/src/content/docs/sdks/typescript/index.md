---
title: TypeScript SDK
description: Install tiktok-shop-api, the typed TikTok Shop API client for TypeScript and Node.js, and make your first call.
sidebar:
  label: Overview
  order: 1
---

`tiktok-shop-api` is a typed TypeScript and Node.js client for the TikTok Shop Partner API. It signs requests, handles OAuth, works with many shops at once, and verifies and types webhooks. It is published to [npm](https://www.npmjs.com/package/tiktok-shop-api), and its source is in [`typescript/`](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/typescript).

## Install

```sh
npm install tiktok-shop-api
```

Requires Node.js 22 or newer. The package is ESM-only and has no runtime dependencies.

## First call

With an access token from the [OAuth helper](/sdks/typescript/authorization/), create a client, look up the shop cipher, and call an operation on that shop:

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

Every call is signed, timestamped and sent with your access token. The `shop_cipher` query parameter is added for you on the endpoints that need it.

## In this section

- [Authorization](/sdks/typescript/authorization/): `TikTokShopAuth`, authorization URLs, token exchange and refresh.
- [Calling the API](/sdks/typescript/calling-the-api/): the client, API areas, many shops, 64-bit IDs and options.
- [Webhooks](/sdks/typescript/webhooks/): `Webhooks.verifyAndParse` and typed events.
- [Errors](/sdks/typescript/errors/): `TikTokShopError` and its codes.
