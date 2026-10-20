---
title: Webhooks
description: Verify TikTok Shop webhook signatures and parse typed webhook events in C#.
sidebar:
  order: 4
---

`Webhooks.VerifyAndParse` checks TikTok's signature against the raw request body, then parses the body into a typed event you narrow with pattern matching. See [webhooks](/getting-started/webhooks/) for how TikTok signs and delivers them.

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

## Rules

- **Verify the raw body.** Never re-serialize the body before verifying: changed bytes make the signature fail. `Verify`, `Parse` and `VerifyAndParse` take a `string` or the raw bytes (`byte[]` or `ReadOnlySpan<byte>`).
- **Parsing is strict.** `Parse` throws `WebhookParseException` when:
  - the body is not a JSON object;
  - `type` is missing or is not an integer;
  - a known type is missing a required property, or the property is null (the message names it). A known type missing a required field is always a parse error.
- **Unknown types are kept.** An integer `type` this SDK does not know becomes an `UnknownWebhookEvent`. Unknown fields are accepted.
- **Narrow the event.** `Webhooks.Parse` returns one sealed event class per webhook type (`OrderStatusChangeEvent`, `PackageUpdateEvent`, and the rest, rendered from the spec), each with a typed `Payload`, or an `UnknownWebhookEvent`. Narrow with `switch` and pattern matching. All of them extend `WebhookEvent`, which has `Type` and `Raw` (the parsed JSON, unknown fields included).
- **Type names.** `Webhooks.EventTypes` maps a type number to its name; `1` is `ORDER_STATUS_CHANGE`.
- **IDs keep their digits.** 64-bit IDs keep their exact digits: a `shop_id` sent as the JSON number `7494049642642441621` arrives as the string `"7494049642642441621"`.

## Exceptions

A bad signature throws `WebhookSignatureException`. A body that cannot be read as a webhook throws `WebhookParseException`, which derives from `FormatException`. Answer the first with 401 and the second with 400, so neither is mistaken for success.
