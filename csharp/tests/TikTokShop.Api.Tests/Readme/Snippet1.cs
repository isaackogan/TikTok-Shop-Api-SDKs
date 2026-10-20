// This file is compiled so the README's example is known to build. ReadmeTests compares the two marked regions with
// README.md (usings, a blank line, then the body), so edit both together.
// readme:usings
using System;
using TikTokShop.Api;
// readme:end

namespace TikTokShop.Api.Tests.Readme;

internal static class Snippet1
{
    internal static async System.Threading.Tasks.Task Run()
    {
// readme:body
var auth = new TikTokShopAuth(appKey: "YOUR_APP_KEY", appSecret: "YOUR_APP_SECRET", serviceId: "YOUR_SERVICE_ID");

// 1. Send the seller to this page. Use AuthorizationType.Partner or Creator for the other kinds,
//    and AuthorizationRegion.Row outside the United States.
string url = auth.AuthorizationUrl(AuthorizationType.Seller, AuthorizationRegion.Us, state: "a-random-csrf-token");
Console.WriteLine(url);

// 2. TikTok redirects back to your redirect URL with ?code=...
TokenSet tokens = await auth.ExchangeCodeAsync("CODE_FROM_THE_REDIRECT");

Console.WriteLine($"{tokens.SellerName} ({tokens.SellerBaseRegion}), access token expires at {tokens.AccessTokenExpireIn}");
// readme:end
    }
}
