# TikTok Shop API for C# and .NET (Unofficial)

[TikTok Shop API](https://partner.tiktokshop.com/) Client for C# and .NET (Unofficial, Unaffiliated with TikTok or ByteDance Ltd.)

A .NET client for the TikTok Shop API, also called the TikTok Shop Partner API or Open API. It covers every endpoint in
the published spec, over 300 operations across orders, products, fulfillment, logistics, returns and refunds, finance,
promotions, affiliate, analytics and customer service, grouped like TikTok's own docs. Every call is `async` with a
`CancellationToken`, and has a synchronous twin.

Every request is signed with HMAC-SHA256 and sent with your access token, and the shop cipher is added wherever an
endpoint needs it. The OAuth helper builds the authorization URL and exchanges and refreshes tokens. One client can
serve many shops, and TikTok Shop webhooks are verified and parsed into typed event classes you narrow with pattern
matching. Requests and responses are C# classes generated from the OpenAPI spec, and 64-bit IDs are never rounded. It
targets .NET 8+, is nullable-annotated, and ships its XML docs in the package.

Full guides, API reference and documentation: <https://ttspa.docs.isaackogan.com/sdks/csharp/>

The guides cover [Authorization](https://ttspa.docs.isaackogan.com/sdks/csharp/authorization/), [Calling the API](https://ttspa.docs.isaackogan.com/sdks/csharp/calling-the-api/),
[Webhooks](https://ttspa.docs.isaackogan.com/sdks/csharp/webhooks/) and [Errors](https://ttspa.docs.isaackogan.com/sdks/csharp/errors/), and the [API reference](https://ttspa.docs.isaackogan.com/openapi/reference/) lists every operation and webhook.

[![NuGet](https://img.shields.io/nuget/v/TikTokShop.Api?style=flat&color=0274b5)](https://www.nuget.org/packages/TikTokShop.Api)
![.NET](https://img.shields.io/badge/.NET-8%2B-0274b5?style=flat)
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

- [TikTok Shop API for TypeScript](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/typescript), `tiktok-shop-api` on npm
- [TikTok Shop API for Python](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/python), `tiktok-shop-api` on PyPI
- [TikTok Shop API for Go](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/go), `github.com/isaackogan/TikTok-Shop-Api-SDKs/go`
- [TikTok Shop API for Java](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/java), `com.isaackogan:tiktok-shop-api` on Maven Central
- [TikTok Shop API for Kotlin](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/kotlin), `com.isaackogan:tiktok-shop-api-kotlin` on Maven Central
- [TikTok Shop API for PHP](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/php), `isaackogan/tiktok-shop-api` on Packagist
- [TikTok Shop API for Rust](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/rust), `tiktok-shop-api` on crates.io

### Table of Contents

- [Getting Started](#getting-started)
- [Params and Options](#params-and-options)
- [Methods](#methods)
- [Examples](#examples)
- [Frequently Asked Questions](#frequently-asked-questions)
- [Contributors](#contributors)
- [License](#license)

## Getting Started

1. Install the package from NuGet

```bash
dotnet add package TikTokShop.Api
```

It needs .NET 8 or newer. The package depends on Newtonsoft.Json, Polly and JsonSubTypes (the generated models use
them).

2. Authorize a shop with OAuth and get an access token

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

`TokenSet.ToString()` prints `***` for both tokens (so does the auth object's and the options' `ToString()` for the
app secret), and System.Text.Json and Newtonsoft.Json both round-trip it with the real values. A seller's `OpenId`
keeps its exact digits.

3. Make your first call

Create one `TikTokShopClient` and reuse it for the life of your app: it owns the connection pool.

```csharp
using System;
using TikTokShop.Api;

var client = new TikTokShopClient(
    appKey: "YOUR_APP_KEY",
    appSecret: "YOUR_APP_SECRET",
    accessToken: "THE_SELLER_ACCESS_TOKEN");

// The shop cipher comes from the authorized-shops call.
var shops = await client.Authorization.GetAuthorizedShopsAsync();
foreach (var shop in shops.Data.Shops)
{
    Console.WriteLine($"{shop.Name} {shop.Region} {shop.Cipher}");
}
```

With a shop cipher, the operations that need one (most of them) work:

```csharp
using System;
using TikTokShop.Api;

var client = new TikTokShopClient(
    appKey: "YOUR_APP_KEY",
    appSecret: "YOUR_APP_SECRET",
    accessToken: "THE_SELLER_ACCESS_TOKEN",
    shopCipher: "THE_SHOP_CIPHER");

// Every request is signed, and shop_cipher is added to the operations that take one.
var orders = await client.Orders.GetOrderListAsync(pageSize: 20);
Console.WriteLine($"{orders.Data.TotalCount} orders");
```

The generated methods take their parameters in the order of the generated signature, ending with an optional
`CancellationToken`. The `shop_cipher` parameter is not among them: the client adds it.

## Params and Options

To create a new `TikTokShopClient`, pass these named arguments, or the same values as a `TikTokShopOptions`.

`new TikTokShopClient(appKey, appSecret, accessToken: ..., shopCipher: ..., ...)`

| Param Name | Required | Description |
|------------|----------|-------------|
| `appKey` | Yes | Your app key. |
| `appSecret` | Yes | Your app secret. It signs every request. |
| `accessToken` | No | The seller's access token, sent as the `x-tts-access-token` header. |
| `shopCipher` | No | The shop's cipher, added as `shop_cipher` to the operations that take one. `client.Authorization.GetAuthorizedShopsAsync()` returns it. |
| `baseUrl` | No | Default `TikTokShopClient.DefaultBaseUrl` (`https://open-api.tiktokglobalshop.com`). It must be an origin such as `https://host:8443`, with no path prefix: signing and shop-cipher matching use the request path. |
| `timeout` | No | The limit for the whole exchange. `null` means `TikTokShopClient.DefaultTimeout` (30 seconds); `TimeSpan.Zero` and `Timeout.InfiniteTimeSpan` mean no limit. |
| `handler` | No | Your own `HttpMessageHandler`, used as is for API calls, so its redirect, proxy and certificate settings apply. By default the SDK builds a `SocketsHttpHandler` that never follows redirects (a 3xx reply becomes a `TikTokShopException`), uses the system proxy, and recycles pooled connections every two minutes so DNS changes are picked up. |

The OAuth helper takes these named arguments, or a `TikTokShopAuthOptions`.

`new TikTokShopAuth(appKey, appSecret, serviceId: ..., ...)`

| Param Name | Required | Description |
|------------|----------|-------------|
| `appKey` | Yes | Your app key. |
| `appSecret` | Yes | Your app secret. |
| `serviceId` | No | Your Partner Center service ID. Seller and partner authorization URLs need it. |
| `baseUrl` | No | Default `TikTokShopAuth.DefaultBaseUrl` (`https://auth.tiktok-shops.com`). An origin, with no path prefix. |
| `timeout` | No | The limit for one token request. `null` means `TikTokShopClient.DefaultTimeout`; `TimeSpan.Zero` and `Timeout.InfiniteTimeSpan` mean no limit. |
| `handler` | No | Your own `HttpMessageHandler` for the token calls. They never follow redirects: a handler with `AllowAutoRedirect` set to true is refused, because the token URL holds your app secret. |

Requests carry the User-Agent `tiktok-shop-api-csharp/<version>` (`TikTokShopClient.UserAgent`).

## Methods

Each API group is a property of the client: `AffiliateCreator`, `AffiliatePartner`, `AffiliateSeller`, `Analytics`,
`Authorization`, `CustomerEngagement`, `CustomerService`, `Event`, `Finance`, `FulfilledByTikTok`, `Fulfillment`,
`Logistics`, `Orders`, `Products`, `Promotion`, `ReturnAndRefund`, `Seller`, `SupplyChain` and `Tools`. Each is the
concrete generated API class, so your IDE completes the operations and models (in `TikTokShop.Api.Generated.Model`).

| Method Name | Description |
|-------------|-------------|
| `client.WithShop(accessToken: ..., shopCipher: ...)` | Returns a client for another shop or token that shares this client's handler and connections. An argument you leave out keeps this client's value; `null` or `""` clears it. See [Several shops](#several-shops-withshop). |
| `auth.AuthorizationUrl(type, region, state: ...)` | Builds the URL to send a seller, partner or creator to. `type` is `AuthorizationType.Seller`, `Partner` or `Creator`; `region` is `AuthorizationRegion.Us` or `Row`. |
| `auth.ExchangeCodeAsync(code)` | Trades the `code` from the redirect for a `TokenSet`. `ExchangeCode` is the synchronous twin. |
| `auth.RefreshAsync(refreshToken)` | Trades a refresh token for a new `TokenSet`. `Refresh` is the synchronous twin. |
| `Webhooks.Verify(appKey, appSecret, rawBody, signature)` | Checks a webhook's `Authorization` header against the raw body. Returns `true` or `false`. |
| `Webhooks.Parse(rawBody)` | Parses a body into its event class, or an `UnknownWebhookEvent`. Throws `WebhookParseException` for a body it cannot read. |
| `Webhooks.VerifyAndParse(appKey, appSecret, rawBody, signature)` | Verifies, then parses. Throws `WebhookSignatureException` when the signature does not match. |

A `TokenSet` has `AccessToken`, `AccessTokenExpireIn`, `RefreshToken` and `RefreshTokenExpireIn`, plus `OpenId`,
`SellerName`, `SellerBaseRegion`, `UserType` and `GrantedScopes` when TikTok sends them.

## Examples

### Several shops (`WithShop`)

```csharp
using TikTokShop.Api;

var client = new TikTokShopClient("YOUR_APP_KEY", "YOUR_APP_SECRET", accessToken: "TOKEN_A", shopCipher: "CIPHER_A");

// Another shop, sharing this client's connections. `client` is not changed.
var other = client.WithShop(accessToken: "TOKEN_B", shopCipher: "CIPHER_B");

// An argument you leave out keeps this client's value; null (or "") clears it.
var sameShopNewToken = client.WithShop(accessToken: "TOKEN_A2");
var noShop = client.WithShop(shopCipher: new Optional<string?>(null));
```

### Handle errors

```csharp
using System;
using TikTokShop.Api;

var client = new TikTokShopClient("YOUR_APP_KEY", "YOUR_APP_SECRET", accessToken: "THE_SELLER_ACCESS_TOKEN");

try
{
    await client.Authorization.GetAuthorizedShopsAsync();
}
catch (TikTokShopException e)
{
    // TikTok's code (or the HTTP status), its message, its request ID for support, and the HTTP status (null if no reply came).
    Console.WriteLine($"{e.Code} {e.TikTokMessage} {e.RequestId} {e.HttpStatus}");
}
```

Every failure is a `TikTokShopException`:

| What happened | `Code` | `HttpStatus` |
|---|---|---|
| TikTok's reply has a non-zero `code`, even on HTTP 200 | TikTok's code | the status |
| A non-2xx reply | TikTok's non-zero code if the body has one, else the HTTP status | the status |
| A 2xx reply that can't be read: not a JSON object, a `code` that isn't an integer, a body that doesn't decode into its model (the decoder's exception is the `InnerException`), or a token reply without `data` | -1 | the status |
| No HTTP response at all: connection refused, DNS, TLS, or a timeout | -1 | `null` |

Messages and inner exceptions never contain the request URL or any secret, so a logged exception does not leak the
signature or the app secret. The OAuth calls follow the same rules.

### Webhooks

```csharp
using System;
using TikTokShop.Api;

static void HandleWebhook(string rawBody, string? authorizationHeader)
{
    // rawBody is the request body exactly as received (never re-serialize it);
    // authorizationHeader is the request's Authorization header.
    WebhookEvent webhook;
    try
    {
        webhook = Webhooks.VerifyAndParse("YOUR_APP_KEY", "YOUR_APP_SECRET", rawBody, authorizationHeader);
    }
    catch (WebhookSignatureException)
    {
        return; // answer 401
    }
    catch (WebhookParseException)
    {
        return; // answer 400: not a webhook this SDK can read
    }

    switch (webhook)
    {
        case OrderStatusChangeEvent order:
            Console.WriteLine($"{order.Payload.Data.OrderId} is now {order.Payload.Data.OrderStatus}");
            break;
        case SellerDeauthorizationEvent revoked:
            Console.WriteLine($"shop {revoked.Payload.ShopId} revoked access");
            break;
        case UnknownWebhookEvent unknown:
            Console.WriteLine($"unhandled webhook type {unknown.Type}");
            break;
    }
}
```

- `Webhooks.Parse` returns one sealed event class per webhook type (`OrderStatusChangeEvent`, `PackageUpdateEvent`, and
  the rest, rendered from the spec), each with a typed `Payload`, or an `UnknownWebhookEvent`. Narrow with `switch` and
  pattern matching. All of them extend `WebhookEvent`, which has `Type` and `Raw` (the parsed JSON, unknown fields
  included).
- Verify against the raw body as received: re-serializing the JSON changes the signature. `Verify`, `Parse` and
  `VerifyAndParse` take a `string` or the raw bytes (`byte[]` or `ReadOnlySpan<byte>`).
- Parsing is strict. A body that is not a JSON object, a `type` that is missing or not an integer, or a known type with
  a required property missing or null (the message names it) throws `WebhookParseException`: a known type missing a
  required field is a parse error. An integer `type` this SDK does not know becomes `UnknownWebhookEvent`. Unknown
  fields are accepted.
- 64-bit IDs keep their exact digits: a `shop_id` sent as the JSON number `7494049642642441621` arrives as the string
  `"7494049642642441621"`.
- `Webhooks.EventTypes` maps a type to its name, for example `1` to `ORDER_STATUS_CHANGE`.

### GET requests with a body

Three operations are GETs with a body (`GetConversationList`, `MapTokopediaToTikTokShopProductIDs`,
`GetShippingTemplateAvailability`). The SDK sends the body and signs it.

## Frequently Asked Questions

### How do I get a TikTok Shop access token in C#?

Create a `TikTokShopAuth` with your app key, app secret and service ID, send the seller to `AuthorizationUrl`, then
trade the `code` TikTok sends back with `ExchangeCodeAsync`. Call `RefreshAsync` before the access token expires. See
[Getting Started](#getting-started).

### What is a shop cipher, and where do I find it?

Most TikTok Shop API endpoints act on one shop and need a `shop_cipher` query parameter. Call
`client.Authorization.GetAuthorizedShopsAsync()` with the seller's access token: each shop in the reply has a `Cipher`.
Pass it as `shopCipher:` and the client adds it to every endpoint that needs it.

### How do I verify TikTok Shop webhooks in ASP.NET Core?

Read the request body as received, as a `string` or as bytes, and pass it with the `Authorization` header to
`Webhooks.VerifyAndParse`. Don't bind it to a model first, because re-serialized JSON no longer matches the signature.
See [Webhooks](#webhooks).

### Should I create one client per request?

No. Create one `TikTokShopClient` and reuse it: it owns the connection pool. For other shops, derive clients with
`WithShop`, which share its connections.

### Which TikTok Shop API versions does it cover?

Every endpoint in TikTok's partner documentation, from API version 202309 onwards, and every documented webhook.

### Is this affiliated with TikTok?

No. It is an independent open-source project, built from TikTok's partner documentation.

### Is this available in other languages?

Yes. See [Do you prefer other programming languages?](#do-you-prefer-other-programming-languages) for the TypeScript,
Python, Go, Java, Kotlin, PHP and Rust SDKs.

## Contributors

* **Isaac Kogan** - *Creator & Maintainer* - [isaackogan](https://github.com/isaackogan)

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/LICENSE) file for details.

Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.
