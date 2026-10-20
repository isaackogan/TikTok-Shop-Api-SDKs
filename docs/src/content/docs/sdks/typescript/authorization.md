---
title: Authorization
description: Build TikTok Shop authorization URLs and exchange and refresh tokens with TikTokShopAuth in TypeScript.
sidebar:
  order: 2
---

`TikTokShopAuth` builds the URL a seller, partner or creator opens to authorize your app, and calls TikTok's token endpoints. See [authorization](/getting-started/authorization/) for the flow itself.

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

## Options

| Option | Meaning |
| --- | --- |
| `appKey`, `appSecret` | Your app's credentials from Partner Center. |
| `serviceId` | Your Partner Center service ID. Required for `seller` and `partner` authorization URLs; `creator` URLs use the app key instead. |
| `baseUrl` | Token endpoint host, an origin with no path prefix. Defaults to `https://auth.tiktok-shops.com`. |
| `timeoutMs` | Per-request timeout. Defaults to 30 seconds (`DEFAULT_TIMEOUT_MS`); 0 means no limit. |
| `fetch` | An HTTP client override. The default never follows a redirect, so the app secret and the code are never forwarded to another host; a `fetch` you supply keeps its own redirect policy. |

`authorizationUrl` omits an empty `state`, the same as an absent one.

## Tokens

`exchangeCode` and `refresh` return a `TokenSet`:

| Field | Meaning |
| --- | --- |
| `accessToken`, `refreshToken` | The tokens. Send the access token with API calls; trade the refresh token for a new pair. |
| `accessTokenExpireIn`, `refreshTokenExpireIn` | Unix timestamps in seconds at which each token expires. They are moments, not durations. |
| `openId`, `sellerName`, `sellerBaseRegion`, `userType`, `grantedScopes` | Optional. Creator and partner tokens may lack the seller fields, and an absent `grantedScopes` is left unset rather than an empty list. |

A non-zero `code` in TikTok's response throws a `TikTokShopError` with `code`, `message` and `requestId`, and so does a token reply without `data`. See [errors](/sdks/typescript/errors/).
