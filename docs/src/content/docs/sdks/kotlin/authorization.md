---
title: Authorization
description: Build TikTok Shop authorization URLs and exchange and refresh tokens with TikTokShopAuth in Kotlin.
sidebar:
  order: 2
---

`TikTokShopAuth` builds the URL a seller, partner or creator opens to authorize your app, and calls TikTok's token endpoints. See [authorization](/getting-started/authorization/) for the flow itself.

```kotlin
import com.isaackogan.tiktok.shop.TikTokShopAuth
import com.isaackogan.tiktok.shop.TikTokShopAuthOptions

class OAuthExample {
    fun run() {
        val auth = TikTokShopAuth(
            TikTokShopAuthOptions(appKey = "YOUR_APP_KEY", appSecret = "YOUR_APP_SECRET", serviceId = "YOUR_SERVICE_ID"),
        )

        // 1. Send the seller to this page.
        val url = auth.authorizationUrl(TikTokShopAuth.AuthType.SELLER, TikTokShopAuth.Region.US, state = "my-state")

        // 2. TikTok redirects back with ?code=...; trade it for tokens.
        val tokens = auth.exchangeCode("CODE_FROM_THE_REDIRECT")

        // 3. Later, trade the refresh token for new tokens.
        val fresh = auth.refresh(tokens.refreshToken)
    }
}
```

`AuthType` is `SELLER`, `PARTNER` or `CREATOR`; `Region` is `US` or `ROW`.

## Options

`TikTokShopAuthOptions` takes:

| Option | Meaning |
| --- | --- |
| `appKey`, `appSecret` | Your app's credentials from Partner Center. |
| `serviceId` | Your Partner Center service ID. Needed for `SELLER` and `PARTNER` authorization URLs; `CREATOR` URLs use the app key instead. |
| `baseUrl` | Token endpoint host, an origin with no path prefix. Defaults to `https://auth.tiktok-shops.com`. |
| `timeout` | A `Duration` bounding one token request. Defaults to 30 seconds (`DEFAULT_AUTH_TIMEOUT`) unless you supply an `httpClient`, which keeps its own timeouts. |
| `httpClient` | An `OkHttpClient` to carry the requests (proxy, TLS, ...). Unlike the API client's, it never follows a redirect, because the URL holds the app secret and the code. |

`authorizationUrl` takes an optional `state`.

## Tokens

`exchangeCode` and `refresh` return a `TokenSet`:

| Property | Meaning |
| --- | --- |
| `accessToken`, `refreshToken` | The tokens. Send the access token with API calls; trade the refresh token for a new pair. |
| `accessTokenExpireIn`, `refreshTokenExpireIn` | Unix timestamps in seconds at which each token expires, as `Long`. They are moments, not durations. |
| `openId`, `sellerName`, `sellerBaseRegion`, `userType`, `grantedScopes` | Nullable: `null` when TikTok sends none. Creator and partner tokens may lack the seller fields. `openId` keeps its exact digits. |

`TokenSet.toString()` hides the tokens: it prints the open ID, seller name and scopes, and `tokens redacted`.

## Errors

Every failure throws `TikTokShopException`, and its message never contains your app secret, auth code or refresh token. A non-zero `code` in TikTok's response is one, and so is a token reply without `data`. A 3xx reply is one too, with the status as its `code`, because token requests never follow redirects. See [errors](/sdks/kotlin/errors/).
