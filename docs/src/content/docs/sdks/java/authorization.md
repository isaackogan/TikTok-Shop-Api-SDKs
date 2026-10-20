---
title: Authorization
description: Build TikTok Shop authorization URLs and exchange and refresh tokens with TikTokShopAuth in Java.
sidebar:
  order: 2
---

`TikTokShopAuth` builds the URL a seller, partner or creator opens to authorize your app, and calls TikTok's token endpoints. See [authorization](/getting-started/authorization/) for the flow itself.

```java
import com.isaackogan.tiktok.shop.TikTokShopAuth;
import com.isaackogan.tiktok.shop.TokenSet;

class OAuthExample {
    void run() {
        TikTokShopAuth auth = TikTokShopAuth.builder()
                .appKey("YOUR_APP_KEY")
                .appSecret("YOUR_APP_SECRET")
                .serviceId("YOUR_SERVICE_ID")
                .build();

        // 1. Send the seller to this page.
        String url = auth.authorizationUrl(TikTokShopAuth.AuthType.SELLER, TikTokShopAuth.Region.US, "my-state");

        // 2. TikTok redirects back with ?code=...; trade it for tokens.
        TokenSet tokens = auth.exchangeCode("CODE_FROM_THE_REDIRECT");

        // 3. Later, trade the refresh token for new tokens.
        TokenSet fresh = auth.refresh(tokens.getRefreshToken());
    }
}
```

`TikTokShopAuth.AuthType` is `SELLER`, `PARTNER` or `CREATOR`; `Region` is `US` or `ROW`.

## Options

Set these on `TikTokShopAuth.builder()`. `appKey` and `appSecret` are required: `build()` throws `IllegalStateException` without them.

| Option | Meaning |
| --- | --- |
| `appKey`, `appSecret` | Your app's credentials from Partner Center. |
| `serviceId` | Your Partner Center service ID. Required for `SELLER` and `PARTNER` authorization URLs; without it `authorizationUrl` throws `IllegalStateException`. `CREATOR` URLs use the app key instead. |
| `baseUrl` | Token endpoint host, an origin with no path prefix. Defaults to `https://auth.tiktok-shops.com` (`DEFAULT_BASE_URL`). |
| `timeout` | A `Duration` bounding one request. Defaults to 30 seconds (`DEFAULT_TIMEOUT`) unless you supply an `httpClient`, which keeps its own timeouts. |
| `httpClient` | An `OkHttpClient` to carry the requests (proxy, TLS, ...). Token calls never follow a redirect, whatever this client says, so the app secret and the code are never forwarded to another host. |

`authorizationUrl` omits a null or empty `state`.

## Tokens

`exchangeCode` and `refresh` return a `TokenSet`:

| Getter | Meaning |
| --- | --- |
| `getAccessToken()`, `getRefreshToken()` | The tokens. Send the access token with API calls; trade the refresh token for a new pair. |
| `getAccessTokenExpireIn()`, `getRefreshTokenExpireIn()` | Unix timestamps in seconds at which each token expires, as `long`. They are moments, not durations. |
| `getOpenId()`, `getSellerName()`, `getSellerBaseRegion()`, `getUserType()`, `getGrantedScopes()` | Optional, and `null` when TikTok sends none. Creator and partner tokens may lack the seller fields. `getOpenId()` keeps its exact digits, and `getGrantedScopes()` is `null` rather than an empty list. |

`TokenSet` is immutable. Its `toString()` prints the open ID, seller name and scopes, and `tokens redacted` in place of the tokens.

## Errors

Every failure raises the unchecked `TikTokShopException`, and its message never contains your app secret, auth code or refresh token. A non-zero `code` in TikTok's response is one, and so is a token reply without `data`. A 3xx reply is one too, with the status as its `getCode()`, because the redirect is not followed. See [errors](/sdks/java/errors/).

The token methods do not declare `ApiException`: they are not generated code and have no async variant.
