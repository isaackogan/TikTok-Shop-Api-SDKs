// This file is compiled so the README's example is known to build. ReadmeTests compares the two marked regions with
// README.md (usings, a blank line, then the body), so edit both together.
// readme:usings
using System;
using TikTokShop.Api;
// readme:end

namespace TikTokShop.Api.Tests.Readme;

internal static class Snippet7
{
// readme:body
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
// readme:end
}
