# tiktok-shop-api: TikTok Shop API client for TypeScript

A typed TypeScript and Node.js client for the **TikTok Shop API** (the TikTok Shop Partner API). It covers over 300 operations across orders, products, fulfillment, logistics, finance, affiliate, customer service and more.

It signs requests for you, handles OAuth, works with many shops at once, and verifies and types TikTok Shop webhooks.

> **Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.**
>
> Request signing follows TikTok's documentation and has not been verified against the live API. If TikTok rejects a signature, please open an issue at https://github.com/isaackogan/TikTok-Shop-Api-SDKs/issues.

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

A non-zero `code` in TikTok's response throws a `TikTokShopError` with `code`, `message` and `requestId` (see [Errors](#errors)).

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
import { WebhookParseError, Webhooks, WebhookSignatureError } from 'tiktok-shop-api';

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
    res.writeHead(e instanceof WebhookSignatureError ? 401 : e instanceof WebhookParseError ? 400 : 500).end();
  }
}).listen(3000);
```

- Never re-serialize the body before verifying. Changed whitespace or key order makes the signature fail.
- Parsing is strict. A body that is not a JSON object, or whose `type` is missing or not an integer, throws `WebhookParseError`. So does a known type with a required field missing or null, or with a model field that isn't a JSON object, at any depth: a known type missing a required field is a parse error.
- A webhook type this SDK does not know comes back as `{ type, raw }`. Known events never have a `raw` property, so `'raw' in event` (or `isUnknownWebhookEvent(event)`) separates the two. After that, `event.type` narrows to the specific webhook model.
- `EVENT_TYPES` maps a type number to its name (`1` is `ORDER_STATUS_CHANGE`).

## IDs are strings

TikTok Shop IDs (`shop_id`, `order_id`, `product_id`, ...) are 64-bit integers, which JavaScript numbers cannot hold exactly. This client reads them as **strings** in every response and webhook, and sends them back as the numbers TikTok expects. For example, `7494049642642441621` stays `"7494049642642441621"`.

## Options

- `baseUrl` (on `TikTokShop` and `TikTokShopAuth`) must be an origin such as `https://host:8443`, with no path prefix: signing and shop-cipher matching use the request path.
- `timeoutMs` (on both) is the per-request timeout. It defaults to 30 seconds (`DEFAULT_TIMEOUT_MS`); 0 means no limit.
- Requests carry the User-Agent `tiktok-shop-api-typescript/<version>`.

## Errors

Every failed call throws `TikTokShopError`, with `code`, `message`, `requestId`, `httpStatus` and the original error as `cause`:

| What happened | `code` | `httpStatus` |
|---|---|---|
| TikTok's reply has a non-zero `code`, even on HTTP 200 | TikTok's code | the status |
| A non-2xx reply | TikTok's non-zero code if the body has one, else the HTTP status | the status |
| A 2xx reply that can't be read: not a JSON object, a `code` that isn't an integer, a body that doesn't fit its model, or a token reply without `data` | -1 | the status |
| No HTTP response at all: connection refused, DNS, TLS, or a timeout | -1 | unset |

The generated models copy scalar fields as sent, without checking their type. A field that should hold a model but isn't a JSON object, or should hold a list of models but isn't a list, is the -1 error above, at any depth.

## About

This is the TypeScript package of a set of generated TikTok Shop API SDKs. The OpenAPI spec and the other languages live in [isaackogan/TikTok-Shop-Api-SDKs](https://github.com/isaackogan/TikTok-Shop-Api-SDKs).

MIT licensed. Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.
