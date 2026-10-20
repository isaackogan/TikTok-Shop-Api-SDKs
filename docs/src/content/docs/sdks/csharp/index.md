---
title: C# SDK
description: Install TikTokShop.Api, the typed TikTok Shop API client for .NET, from NuGet and make your first call.
sidebar:
  label: Overview
  order: 1
---

`TikTokShop.Api` is a typed .NET client for the TikTok Shop Partner API. It signs requests, handles OAuth, works with many shops at once, and verifies and types webhooks. It is published to [NuGet](https://www.nuget.org/packages/TikTokShop.Api), and its source is in [`csharp/`](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/csharp).

## Install

```bash
dotnet add package TikTokShop.Api
```

Needs .NET 8 or newer. The package depends on Newtonsoft.Json, Polly and JsonSubTypes (the generated models use them). It is nullable-annotated and ships its XML docs.

## First call

With an access token from the [OAuth helper](/sdks/csharp/authorization/), create **one** `TikTokShopClient` and reuse it for the life of your app: it owns the connection pool.

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

Every call is `async` with a `CancellationToken`, and has a synchronous twin. Every request is signed, timestamped and sent with your access token.

## In this section

- [Authorization](/sdks/csharp/authorization/): `TikTokShopAuth`, authorization URLs, token exchange, refresh and storing a `TokenSet`.
- [Calling the API](/sdks/csharp/calling-the-api/): the client, API areas, many shops and the HTTP handler.
- [Webhooks](/sdks/csharp/webhooks/): `Webhooks.VerifyAndParse` and typed events.
- [Errors](/sdks/csharp/errors/): `TikTokShopException` and its codes.
