# TikTok Shop API for TypeScript (Unofficial)

[TikTok Shop API](https://partner.tiktokshop.com/) Client for TypeScript and Node.js (Unofficial, Unaffiliated with TikTok or ByteDance Ltd.)

A typed client for the TikTok Shop API, also called the TikTok Shop Partner API or Open API. It covers over 300
operations across orders, products, fulfillment, logistics, returns and refunds, finance, promotions, affiliate,
analytics and customer service, for sellers, partners and creators.

Every request is signed with HMAC-SHA256 and sent with your access token, and the shop cipher is added wherever an
endpoint needs it. The OAuth helper builds the
authorization URL and exchanges and refreshes tokens. One client can serve many shops, and TikTok Shop webhooks are
verified and parsed into typed events. The methods are generated from an OpenAPI spec built from TikTok's partner
documentation, so they track the docs.

Full guides, API reference and documentation: <https://ttspa.docs.isaackogan.com/sdks/typescript/>

The guides cover [Authorization](https://ttspa.docs.isaackogan.com/sdks/typescript/authorization/), [Calling the API](https://ttspa.docs.isaackogan.com/sdks/typescript/calling-the-api/),
[Webhooks](https://ttspa.docs.isaackogan.com/sdks/typescript/webhooks/) and [Errors](https://ttspa.docs.isaackogan.com/sdks/typescript/errors/), and the [API reference](https://ttspa.docs.isaackogan.com/openapi/reference/) lists every operation and webhook.

[![npm](https://img.shields.io/npm/v/tiktok-shop-api?style=flat&color=0274b5)](https://www.npmjs.com/package/tiktok-shop-api)
![Node](https://img.shields.io/node/v/tiktok-shop-api?style=flat&color=0274b5)
![Stars](https://img.shields.io/github/stars/isaackogan/TikTok-Shop-Api-SDKs?style=flat&color=0274b5)
![Issues](https://img.shields.io/github/issues/isaackogan/TikTok-Shop-Api-SDKs?style=flat&color=0274b5)
![License](https://img.shields.io/github/license/isaackogan/TikTok-Shop-Api-SDKs?style=flat&color=0274b5)

> [!IMPORTANT]
> Request signing follows TikTok's documentation and has not been verified against the live API. If TikTok rejects a signature, please open an issue at https://github.com/isaackogan/TikTok-Shop-Api-SDKs/issues.

> [!TIP]
> The OpenAPI spec this client is generated from is published at
> [tiktok-shop.openapi.yaml](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/.openapi/tiktok-shop.openapi.yaml).
> Point any OpenAPI 3.1 tool at it.

### Do you prefer other programming languages?

- [TikTok Shop API for Python](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/python), `tiktok-shop-api` on PyPI
- [TikTok Shop API for Go](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/go), `github.com/isaackogan/TikTok-Shop-Api-SDKs/go`
- [TikTok Shop API for Java](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/java), `com.isaackogan:tiktok-shop-api` on Maven Central
- [TikTok Shop API for Kotlin](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/kotlin), `com.isaackogan:tiktok-shop-api-kotlin` on Maven Central
- [TikTok Shop API for PHP](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/php), `isaackogan/tiktok-shop-api` on Packagist
- [TikTok Shop API for Rust](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/rust), `tiktok-shop-api` on crates.io
- [TikTok Shop API for C# and .NET](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/csharp), `TikTokShop.Api` on NuGet

### Table of Contents

- [Getting Started](#getting-started)
- [Params and Options](#params-and-options)
- [Methods](#methods)
- [Examples](#examples)
- [Frequently Asked Questions](#frequently-asked-questions)
- [Contributors](#contributors)
- [License](#license)

## Getting Started

1. Install the package from npm

```sh
npm install tiktok-shop-api
```

It needs Node.js 22 or newer and has no runtime dependencies.

2. Authorize a shop with OAuth and get an access token

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

A non-zero `code` in TikTok's response throws a `TikTokShopError` with `code`, `message` and `requestId` (see
[Handle errors](#handle-errors)).

3. Make your first call

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

Every call is signed, timestamped and sent with your access token. The `shop_cipher` query parameter is added on the
endpoints that need it.

## Params and Options

To create a new `TikTokShop` client, pass these options.

`new TikTokShop(options)`

| Param Name | Required | Description |
|------------|----------|-------------|
| `appKey` | Yes | Your app key. |
| `appSecret` | Yes | Your app secret. It signs every request. The options are kept in a private field, so the secret stays out of `console.log` and `JSON.stringify`. |
| `accessToken` | No | The seller's access token, sent as the `x-tts-access-token` header. |
| `shopCipher` | No | The shop's cipher, added as `shop_cipher` to the operations that need one. `authorization.getAuthorizedShops()` returns it. |
| `baseUrl` | No | Default `https://open-api.tiktokglobalshop.com`. It must be an origin such as `https://host:8443`, with no path prefix: signing and shop-cipher matching use the request path. |
| `timeoutMs` | No | The per-request timeout in milliseconds. Default 30000 (`DEFAULT_TIMEOUT_MS`); 0 means no limit. |
| `fetch` | No | Your own `fetch`, used as is, so its redirect policy applies. The default uses the global `fetch` and never follows a redirect: a 3xx reply throws a `TikTokShopError` whose `code` and `httpStatus` are the status, so the access token is never forwarded to another host. A GET with a body, which `fetch` refuses, is sent with `node:http` or `node:https`. |

The OAuth helper takes its own options.

`new TikTokShopAuth(options)`

| Param Name | Required | Description |
|------------|----------|-------------|
| `appKey` | Yes | Your app key. |
| `appSecret` | Yes | Your app secret. |
| `serviceId` | No | Your Partner Center service ID. Seller and partner authorization URLs need it. |
| `baseUrl` | No | The token endpoint's origin, with no path prefix. Default `https://auth.tiktok-shops.com`. |
| `timeoutMs` | No | The per-request timeout in milliseconds. Default 30000; 0 means no limit. |
| `fetch` | No | Your own `fetch`, used as is. The default never follows a redirect, so the app secret and the code are never forwarded to another host. |

Requests carry the User-Agent `tiktok-shop-api-typescript/<version>`.

## Methods

Each API group is a property of the client: `affiliateCreator`, `affiliatePartner`, `affiliateSeller`, `analytics`,
`authorization`, `customerEngagement`, `customerService`, `event`, `finance`, `fulfilledByTikTok`, `fulfillment`,
`logistics`, `orders`, `products`, `promotion`, `returnAndRefund`, `seller`, `supplyChain` and `tools`. Each one is the
generated API class, so your editor completes its operations and models.

| Method Name | Description |
|-------------|-------------|
| `client.withShop({ accessToken, shopCipher })` | Returns a client for another shop or token. It shares your app credentials and HTTP client. A field you leave out keeps this client's value. See [Many shops](#many-shops). |
| `auth.authorizationUrl({ type, region, state })` | Builds the URL to send a seller, partner or creator to. `type` is `'seller'`, `'partner'` or `'creator'`; `region` is `'us'` or `'row'`. An empty `state` is left out. |
| `auth.exchangeCode(code)` | Trades the `code` from the redirect for a `TokenSet`. |
| `auth.refresh(refreshToken)` | Trades a refresh token for a new `TokenSet`. |
| `Webhooks.verify({ appKey, appSecret, rawBody, signature })` | Checks a webhook's `Authorization` header: HMAC-SHA256, keyed with your app secret, over your app key plus the raw body, compared in constant time. Returns `true` or `false`. |
| `Webhooks.parse(rawBody)` | Parses a body into its typed webhook model, or `{ type, raw }` for a type this SDK does not know. Throws `WebhookParseError`. |
| `Webhooks.verifyAndParse({ appKey, appSecret, rawBody, signature })` | Verifies, then parses. Throws `WebhookSignatureError` when the signature does not match. |
| `isUnknownWebhookEvent(event)` | `true` for the `{ type, raw }` result of an unknown webhook type. |

A `TokenSet` has `accessToken`, `accessTokenExpireIn`, `refreshToken` and `refreshTokenExpireIn` (both expiry times are
Unix timestamps in seconds). When TikTok sends them, it also has `openId`, `sellerName`, `sellerBaseRegion`, `userType`
and `grantedScopes`. `rawBody` is a `string` or a `Uint8Array`.

## Examples

### Many shops

`withShop` returns a client for another shop. It shares the HTTP client and your app credentials, so you can keep one per shop:

```ts
const shopA = client.withShop({ accessToken: tokenA, shopCipher: cipherA });
const shopB = client.withShop({ accessToken: tokenB, shopCipher: cipherB });
```

### Webhooks

Verify the signature against the raw request body, then parse it into a typed event:

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
- Parsing is strict. A body that is not a JSON object, or whose `type` is missing or not an integer, throws
  `WebhookParseError`. So does a known type with a required field missing or null, or with a model field that isn't a
  JSON object, at any depth: a known type missing a required field is a parse error.
- A webhook type this SDK does not know comes back as `{ type, raw }`. Known events never have a `raw` property, so
  `'raw' in event` (or `isUnknownWebhookEvent(event)`) separates the two. After that, `event.type` narrows to the
  specific webhook model.
- `EVENT_TYPES` maps a type number to its name (`1` is `ORDER_STATUS_CHANGE`).

### Handle errors

Every failed call throws `TikTokShopError`, with `code`, `message`, `requestId`, `httpStatus` and the original error as
`cause`:

| What happened | `code` | `httpStatus` |
|---|---|---|
| TikTok's reply has a non-zero `code`, even on HTTP 200 | TikTok's code | the status |
| A non-2xx reply | TikTok's non-zero code if the body has one, else the HTTP status | the status |
| A 2xx reply that can't be read: not a JSON object, a `code` that isn't an integer, a body that doesn't fit its model, or a token reply without `data` | -1 | the status |
| No HTTP response at all: connection refused, DNS, TLS, or a timeout | -1 | unset |

The generated models copy scalar fields as sent, without checking their type. A field that should hold a model but
isn't a JSON object, or should hold a list of models but isn't a list, is the -1 error above, at any depth.

## Frequently Asked Questions

### How do I get a TikTok Shop access token in Node.js?

Create a `TikTokShopAuth` with your app key, app secret and service ID, send the seller to `authorizationUrl()`, then
trade the `code` TikTok sends back with `exchangeCode()`. Call `refresh()` before the access token expires. See
[Getting Started](#getting-started).

### What is a shop cipher, and where do I find it?

Most TikTok Shop API endpoints act on one shop and need a `shop_cipher` query parameter. Call
`client.authorization.getAuthorizedShops()` with the seller's access token: each shop in the reply has a `cipher`.
Pass it as `shopCipher` and the client adds it to every endpoint that needs it.

### How do I verify TikTok Shop webhooks?

Pass the raw request body and the `Authorization` header to `Webhooks.verifyAndParse`. Read the body as bytes and
don't parse it first, because re-serialized JSON no longer matches the signature. See [Webhooks](#webhooks).

### Why are TikTok Shop IDs strings in JavaScript?

TikTok Shop IDs (`shop_id`, `order_id`, `product_id`, ...) are 64-bit integers, which JavaScript numbers cannot hold
exactly. This client reads them as strings in every response and webhook, and sends them back as the numbers TikTok
expects. For example, `7494049642642441621` stays `"7494049642642441621"`.

### Can one app manage many TikTok Shop sellers?

Yes. Keep one client per shop with `withShop`. Each shares the HTTP client and your app credentials. See
[Many shops](#many-shops).

### Which TikTok Shop API versions does it cover?

Every endpoint in TikTok's partner documentation, from API version 202309 onwards, and every documented webhook.

### Is this affiliated with TikTok?

No. It is an independent open-source project, built from TikTok's partner documentation.

### Is this available in other languages?

Yes. See [Do you prefer other programming languages?](#do-you-prefer-other-programming-languages) for the Python, Go,
Java, Kotlin, PHP, Rust and C# SDKs.

## Contributors

* **Isaac Kogan** - *Creator & Maintainer* - [isaackogan](https://github.com/isaackogan)

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/LICENSE) file for details.

Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.
