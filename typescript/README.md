# tiktok-shop-api: TikTok Shop API client for TypeScript

A typed TypeScript and Node.js client for the **TikTok Shop API** (the TikTok Shop Partner API). It covers 320 operations across orders, products, fulfillment, logistics, finance, affiliate, customer service and more.

It signs requests for you, handles OAuth, works with many shops at once, and verifies and types TikTok Shop webhooks.

> **Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.**
>
> Request signing follows TikTok's documentation and has not been verified against the live API.

The client is generated from an OpenAPI spec that is itself built from the TikTok Shop Partner Center docs: [tiktok-shop.openapi.yaml](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/.openapi/tiktok-shop.openapi.yaml).

## Install

```sh
npm install tiktok-shop-api
```

Requires **Node.js 22 or newer**. It has no runtime dependencies.

## OAuth: get an access token

```ts
import { TikTokShopAuth } from 'tiktok-shop-api';

const auth = new TikTokShopAuth({
  appKey: process.env.TTS_APP_KEY!,
  appSecret: process.env.TTS_APP_SECRET!,
  serviceId: process.env.TTS_SERVICE_ID!, // seller and partner flows
});

// 1. Send the seller here. `type` is 'seller' | 'partner' | 'creator'; `region` is 'us' | 'row'.
const url = auth.authorizationUrl({ type: 'seller', region: 'us', state: 'csrf-token' });

// 2. TikTok redirects back with ?code=...; exchange it.
const code = new URL(callbackUrl).searchParams.get('code')!;
const tokens = await auth.exchangeCode(code);
// tokens.accessToken, tokens.refreshToken, tokens.openId, tokens.grantedScopes, ...

// 3. Before the access token expires (accessTokenExpireIn is a Unix timestamp):
const renewed = await auth.refresh(tokens.refreshToken);
```

A non-zero `code` in TikTok's response throws a `TikTokShopError` with `code`, `message` and `requestId`.

## Make your first call

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

One property per API area hangs off the client (`orders`, `products`, `fulfillment`, `finance`, `affiliateSeller`, and so on). Every call is signed, timestamped and sent with your access token.

The `shop_cipher` query parameter is added for you on the endpoints that need it.

## Many shops

`withShop` returns a client for another shop. It shares the HTTP client and your app credentials, so you can keep one per shop:

```ts
const shopA = client.withShop({ accessToken: tokenA, shopCipher: cipherA });
const shopB = client.withShop({ accessToken: tokenB, shopCipher: cipherB });
```

## Webhooks

Verify the signature against the **raw** request body, then parse it into a typed event:

```ts
import { createServer } from 'node:http';
import { Webhooks, WebhookSignatureError } from 'tiktok-shop-api';

createServer(async (req, res) => {
  const chunks: Buffer[] = [];
  for await (const chunk of req) chunks.push(chunk as Buffer);
  const rawBody = Buffer.concat(chunks); // exactly as received

  try {
    const event = Webhooks.verifyAndParse({
      appKey: process.env.TTS_APP_KEY!,
      appSecret: process.env.TTS_APP_SECRET!,
      rawBody,
      signature: String(req.headers.authorization ?? ''),
    });
    if ('raw' in event) {
      console.log('unknown webhook type', event.type, event.raw);
    } else if (event.type === 1) {
      console.log(event.shopId, event.data?.orderStatus); // OrderStatusChangeWebhook
    }
    res.writeHead(200).end();
  } catch (e) {
    res.writeHead(e instanceof WebhookSignatureError ? 401 : 500).end();
  }
}).listen(3000);
```

- Never re-serialize the body before verifying. Changed whitespace or key order makes the signature fail.
- A webhook type this SDK does not know comes back as `{ type, raw }`. Known events never have a `raw` property, so `'raw' in event` (or `isUnknownWebhookEvent(event)`) separates the two. After that, `event.type` narrows to the specific webhook model.
- `EVENT_TYPES` maps a type number to its name (`1` is `ORDER_STATUS_CHANGE`).

## IDs are strings

TikTok Shop IDs (`shop_id`, `order_id`, `product_id`, ...) are 64-bit integers, which JavaScript numbers cannot hold exactly. This client reads them as **strings** in every response and webhook, and sends them back as the numbers TikTok expects. For example, `7494049642642441621` stays `"7494049642642441621"`.

## Errors

A response with `code != 0`, or a non-2xx status, throws `TikTokShopError` with `code`, `message`, `requestId` and (for HTTP failures) `httpStatus`.

## About

This is the TypeScript package of a set of generated TikTok Shop API SDKs. The OpenAPI spec and the other languages live in [isaackogan/TikTok-Shop-Api-SDKs](https://github.com/isaackogan/TikTok-Shop-Api-SDKs).

MIT licensed. Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.
