// This file is compiled so the README's example is known to build. ReadmeTests compares the two marked regions with
// README.md (usings, a blank line, then the body), so edit both together.
// readme:usings
using System;
using TikTokShop.Api;
// readme:end

namespace TikTokShop.Api.Tests.Readme;

internal static class Snippet6
{
    internal static async System.Threading.Tasks.Task Run()
    {
// readme:body
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
// readme:end
    }
}
