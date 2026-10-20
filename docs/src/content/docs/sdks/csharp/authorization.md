---
title: Authorization
description: Build TikTok Shop authorization URLs, exchange and refresh tokens, and store a TokenSet with TikTokShopAuth in C#.
sidebar:
  order: 2
---

`TikTokShopAuth` builds the URL a seller, partner or creator opens to authorize your app, and calls TikTok's token endpoints. See [authorization](/getting-started/authorization/) for the flow itself.

```csharp
using System;
using TikTokShop.Api;

var auth = new TikTokShopAuth(appKey: "YOUR_APP_KEY", appSecret: "YOUR_APP_SECRET", serviceId: "YOUR_SERVICE_ID");

// 1. Send the seller to this page. Use AuthorizationType.Partner or Creator for the other kinds,
//    and AuthorizationRegion.Row outside the United States.
string url = auth.AuthorizationUrl(AuthorizationType.Seller, AuthorizationRegion.Us, state: "a-random-csrf-token");
Console.WriteLine(url);

// 2. TikTok redirects back to your redirect URL with ?code=...
TokenSet tokens = await auth.ExchangeCodeAsync("CODE_FROM_THE_REDIRECT");

Console.WriteLine($"{tokens.SellerName} ({tokens.SellerBaseRegion}), access token expires at {tokens.AccessTokenExpireIn}");
```

Refresh the tokens, and store them:

```csharp
using System.Text.Json;
using TikTokShop.Api;

var auth = new TikTokShopAuth(appKey: "YOUR_APP_KEY", appSecret: "YOUR_APP_SECRET");

// What ExchangeCodeAsync gave you. Serializing a TokenSet writes the real tokens, so encrypt it at rest.
var tokens = new TokenSet("ACCESS_TOKEN", 1700000000, "REFRESH_TOKEN", 1700600000);
string stored = JsonSerializer.Serialize(tokens);

// Later: refresh before the access token expires.
TokenSet loaded = JsonSerializer.Deserialize<TokenSet>(stored)!;
TokenSet fresh = await auth.RefreshAsync(loaded.RefreshToken);
```

`ExchangeCode` and `Refresh` are the synchronous twins of `ExchangeCodeAsync` and `RefreshAsync`; the async methods take an optional `CancellationToken`.

## Options

`TikTokShopAuth` takes these named constructor arguments, or a `TikTokShopAuthOptions` object with the same members:

| Option | Meaning |
| --- | --- |
| `appKey`, `appSecret` | Your app's credentials from Partner Center. |
| `serviceId` | Your Partner Center service ID. Needed for seller and partner authorization URLs; creator URLs use the app key instead. |
| `baseUrl` | Token endpoint host, an origin with no path prefix. Defaults to `https://auth.tiktok-shops.com` (`DefaultBaseUrl`). |
| `timeout` | A `TimeSpan` for one token request. Defaults to 30 seconds; `TimeSpan.Zero` means no limit. |
| `handler` | An `HttpMessageHandler` for the token requests, used as is, except that it must not follow redirects: the constructor throws for a `SocketsHttpHandler` or `HttpClientHandler` (or one wrapped by `DelegatingHandler`s) with `AllowAutoRedirect` true, because the token URL holds the app secret and the code. |

`AuthorizationUrl` takes an `AuthorizationType` (`Seller`, `Partner` or `Creator`) and an `AuthorizationRegion` (`Us` or `Row`), and an optional `state`.

## Tokens

`ExchangeCodeAsync` and `RefreshAsync` return a `TokenSet`, an immutable record:

| Property | Meaning |
| --- | --- |
| `AccessToken`, `RefreshToken` | The tokens. Send the access token with API calls; trade the refresh token for a new pair. |
| `AccessTokenExpireIn`, `RefreshTokenExpireIn` | Unix timestamps in seconds at which each token expires, as `long`. They are moments, not durations. |
| `OpenId`, `SellerName`, `SellerBaseRegion`, `UserType`, `GrantedScopes` | Nullable: `null` when TikTok sends none. Creator and partner tokens may lack the seller fields. `OpenId` keeps its exact digits. |

## Storing a TokenSet

`TokenSet.ToString()` prints `***` for both tokens, so a logged `TokenSet` does not leak them. The type stays serializable: System.Text.Json and Newtonsoft.Json both round-trip it with the real token values, as in the second example above. Encrypt what you store, and keep it out of logs.

## Errors

Every failure throws `TikTokShopException`. A non-zero `code` in TikTok's response is one, and so is a token reply without `data`. A 3xx reply is one too, with code 302, because token calls never follow redirects. Messages and inner exceptions never contain the request URL or any secret, including the app secret, authorization code and refresh token. See [errors](/sdks/csharp/errors/).
