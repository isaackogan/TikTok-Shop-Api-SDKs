// This file is compiled so the README's example is known to build. ReadmeTests compares the two marked regions with
// README.md (usings, a blank line, then the body), so edit both together.
// readme:usings
using System;
using TikTokShop.Api;
// readme:end

namespace TikTokShop.Api.Tests.Readme;

internal static class Snippet3
{
    internal static async System.Threading.Tasks.Task Run()
    {
// readme:body
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
// readme:end
    }
}
