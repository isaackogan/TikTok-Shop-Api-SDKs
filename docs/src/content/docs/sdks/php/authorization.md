---
title: Authorization
description: Build TikTok Shop authorization URLs, exchange and refresh tokens, and store a TokenSet with TikTokShopAuth in PHP.
sidebar:
  order: 2
---

`TikTokShopAuth` builds the URL a seller, partner or creator opens to authorize your app, and calls TikTok's token endpoints. See [authorization](/getting-started/authorization/) for the flow itself.

```php
use TikTokShop\Api\TikTokShopAuth;

$auth = new TikTokShopAuth(appKey: 'YOUR_APP_KEY', appSecret: 'YOUR_APP_SECRET', serviceId: 'YOUR_SERVICE_ID');

// 1. Send the seller to this page. Use TikTokShopAuth::PARTNER or CREATOR for the other kinds,
//    and TikTokShopAuth::ROW outside the United States.
$url = $auth->authorizationUrl(TikTokShopAuth::SELLER, TikTokShopAuth::US, state: 'a-random-csrf-token');
header('Location: ' . $url);

// 2. TikTok redirects back to your redirect URL with ?code=...
$tokens = $auth->exchangeCode($_GET['code']);

echo $tokens->getAccessToken(), ' expires at ', $tokens->accessTokenExpireIn, PHP_EOL;
echo $tokens->sellerName, ' (', $tokens->sellerBaseRegion, ')', PHP_EOL;
```

Refresh the tokens, and store them:

```php
use TikTokShop\Api\TikTokShopAuth;
use TikTokShop\Api\TokenSet;

$auth = new TikTokShopAuth(appKey: 'YOUR_APP_KEY', appSecret: 'YOUR_APP_SECRET');

// Store the tokens: toArray() holds the real values, so encrypt it at rest.
$stored = json_encode($tokens->toArray());

// Later: refresh before the access token expires.
$tokens = TokenSet::fromArray(json_decode($stored, true));
$tokens = $auth->refresh($tokens->getRefreshToken());
```

## Options

`TikTokShopAuth` takes these named constructor arguments:

| Option | Meaning |
| --- | --- |
| `appKey`, `appSecret` | Your app's credentials from Partner Center. |
| `serviceId` | Your Partner Center service ID. Required for `SELLER` and `PARTNER` authorization URLs; `CREATOR` URLs use the app key instead. An empty string counts as none. |
| `baseUrl` | Token endpoint host, an origin with no path prefix. Defaults to `https://auth.tiktok-shops.com`. |
| `timeout` | Seconds for one request, for the client the SDK builds. Defaults to 30 (`DEFAULT_TIMEOUT`); 0 means no limit. A negative value throws `InvalidArgumentException`. |
| `httpClient` | A Guzzle `ClientInterface`, used as is, except that token calls never follow redirects even on your client, because their URL holds your app secret. |

`authorizationUrl` takes `TikTokShopAuth::SELLER`, `PARTNER` or `CREATOR` and `TikTokShopAuth::US` or `ROW`, and omits a null or empty `state`. It throws `InvalidArgumentException` for an unknown type or region, or for a seller or partner URL without a service ID.

## Tokens

`exchangeCode` and `refresh` return a `TokenSet`:

| Member | Meaning |
| --- | --- |
| `getAccessToken()`, `getRefreshToken()` | The tokens. Send the access token with API calls; trade the refresh token for a new pair. |
| `accessTokenExpireIn`, `refreshTokenExpireIn` | Unix timestamps in seconds at which each token expires, as `int` properties. They are moments, not durations. |
| `openId`, `sellerName`, `sellerBaseRegion`, `userType`, `grantedScopes` | Optional properties, `null` when TikTok sends none. Creator and partner tokens may lack the seller fields. |

## How TokenSet hides its tokens

`TokenSet` holds secrets. The access and refresh tokens are not properties, so they stay out of dumps and logs:
- `var_dump` and `print_r` show `***`;
- `var_export` and `(array)` show neither token;
- `serialize()` refuses, and `clone` throws, because a `TokenSet` is immutable.

Read the tokens with `getAccessToken()` and `getRefreshToken()`. To store a `TokenSet`, use `toArray()` or `json_encode()`, which give the real values under camelCase keys, and restore it with `TokenSet::fromArray()`. Encrypt what you store, and keep it out of logs. `fromArray` throws `InvalidArgumentException` if a token or an expiry is missing or has the wrong type.

## Errors

Every failure throws `TikTokShopException`. A non-zero `code` in TikTok's response is one, and so is a token reply without `data`. A 3xx reply is one too, with the status as its code, because token calls never follow redirects. Messages and previous exceptions never contain your app secret, authorization code or refresh token, and the secrets passed to the OAuth helper are hidden from stack traces with `#[\SensitiveParameter]`. See [errors](/sdks/php/errors/).
