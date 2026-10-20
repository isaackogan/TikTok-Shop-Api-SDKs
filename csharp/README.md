# TikTok Shop API client for .NET

A .NET client for the **TikTok Shop API** (the TikTok Shop Partner API / Open API). It covers every endpoint in the published spec, signs every request, ships an OAuth helper, and parses webhooks into typed event classes you narrow with pattern matching.

Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.

- **Every TikTok Shop API endpoint**, grouped like TikTok's own docs: `client.Orders`, `client.Products`, `client.Fulfillment`, `client.Finance`, and 15 more. Every call is `async` with a `CancellationToken`, and has a synchronous twin.
- **Typed models.** Generated from the [OpenAPI spec](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/.openapi/tiktok-shop.openapi.yaml), so requests and responses are C# classes. 64-bit IDs are never rounded.
- **Request signing** (HMAC-SHA256), `app_key`, `timestamp`, `shop_cipher` and the `x-tts-access-token` header added for you.
- **OAuth helper** for the authorization URL, code exchange and token refresh.
- **Webhooks**: verify the signature, then get a typed event class for any of the webhook types.
- **.NET 8+**, nullable-annotated, with the XML docs shipped in the package.

> Request signing follows TikTok's documentation and has not been verified against the live API.

## Install

```bash
dotnet add package TikTokShop.Api
```

Needs .NET 8 or newer. The package depends on Newtonsoft.Json, Polly and JsonSubTypes (the generated models use them).

## Authorize a shop (OAuth)

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

`TokenSet.ToString()` prints `***` for both tokens (so does the auth object's and the options' `ToString()` for the app secret), and System.Text.Json and Newtonsoft.Json both round-trip it with the real values. A seller's `OpenId` keeps its exact digits.

## Make your first call

Create **one** `TikTokShopClient` and reuse it for the life of your app: it owns the connection pool.

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

The generated methods take their parameters in the order of the generated signature, ending with an optional `CancellationToken`. The `shop_cipher` parameter is not among them: the client adds it.

## Several shops (`WithShop`)

```csharp
using TikTokShop.Api;

var client = new TikTokShopClient("YOUR_APP_KEY", "YOUR_APP_SECRET", accessToken: "TOKEN_A", shopCipher: "CIPHER_A");

// Another shop, sharing this client's connections. `client` is not changed.
var other = client.WithShop(accessToken: "TOKEN_B", shopCipher: "CIPHER_B");

// An argument you leave out keeps this client's value; null (or "") clears it.
var sameShopNewToken = client.WithShop(accessToken: "TOKEN_A2");
var noShop = client.WithShop(shopCipher: new Optional<string?>(null));
```

## Errors

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

Every failure is a `TikTokShopException`: a non-zero `code` in a 200 reply, a non-2xx status, a reply that is not understood, and network errors and timeouts (`Code` -1, no `HttpStatus`). Messages and inner exceptions never contain the request URL or any secret, so a logged exception does not leak the signature or the app secret. The OAuth calls follow the same rules.

## Webhooks

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

- `Webhooks.Parse` returns one sealed event class per webhook type (`OrderStatusChangeEvent`, `PackageUpdateEvent`, and the rest, rendered from the spec), each with a typed `Payload`, or an `UnknownWebhookEvent`. Narrow with `switch` and pattern matching. All of them extend `WebhookEvent`, which has `Type` and `Raw` (the parsed JSON, unknown fields included).
- Verify against the **raw body** as received: re-serializing the JSON changes the signature. `Verify`, `Parse` and `VerifyAndParse` take a `string` or the raw bytes (`byte[]` or `ReadOnlySpan<byte>`).
- A body whose `type` is missing or not an integer, or whose payload lacks a property its model requires (the message names it), throws `WebhookParseException`. An integer `type` this SDK does not know becomes `UnknownWebhookEvent`. Unknown fields are accepted.
- 64-bit IDs keep their exact digits: a `shop_id` sent as the JSON number `7494049642642441621` arrives as the string `"7494049642642441621"`.
- `Webhooks.EventTypes` maps a type to its name, for example `1` to `ORDER_STATUS_CHANGE`.

## API surface

The client's properties are the API groups: `AffiliateCreator`, `AffiliatePartner`, `AffiliateSeller`, `Analytics`, `Authorization`, `CustomerEngagement`, `CustomerService`, `Event`, `Finance`, `FulfilledByTikTok`, `Fulfillment`, `Logistics`, `Orders`, `Products`, `Promotion`, `ReturnAndRefund`, `Seller`, `SupplyChain`, `Tools`. Each is the concrete generated API class, so your IDE completes the operations and models (in `TikTokShop.Api.Generated.Model`).

## HTTP client

By default the SDK builds a `SocketsHttpHandler` that never follows redirects (a 3xx reply is a `TikTokShopException` with code 302), uses the system proxy, and recycles pooled connections every two minutes so DNS changes are picked up. The timeout is 30 seconds for the whole exchange (`timeout:`, `TimeSpan.Zero` for none). Pass your own `handler:`; it is used as is for API calls, so its redirect, proxy and certificate settings apply. The OAuth calls never follow redirects: a handler with `AllowAutoRedirect` set to true is refused, because the token URL holds your app secret.

## Notes

- Generated from [the spec](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/.openapi/tiktok-shop.openapi.yaml) in the [TikTok-Shop-Api-SDKs](https://github.com/isaackogan/TikTok-Shop-Api-SDKs) repository, which also has SDKs for TypeScript, Python, Go, Java, Kotlin, PHP and Rust.
- Three operations are GETs with a body (`GetConversationList`, `MapTokopediaToTikTokShopProductIDs`, `GetShippingTemplateAvailability`). The SDK sends the body and signs it.
- If you import `TikTokShop.Api.Generated.Model` too, its generated `WebhookEvent` model has the same name as this package's `WebhookEvent`: write `TikTokShop.Api.WebhookEvent` (or an alias) where you need the base class.

## License

MIT
