// This file is compiled so the README's example is known to build. ReadmeTests compares the two marked regions with
// README.md (usings, a blank line, then the body), so edit both together.
// readme:usings
using System;
using TikTokShop.Api;
// readme:end

namespace TikTokShop.Api.Tests.Readme;

internal static class Snippet4
{
    internal static async System.Threading.Tasks.Task Run()
    {
// readme:body
var client = new TikTokShopClient(
    appKey: "YOUR_APP_KEY",
    appSecret: "YOUR_APP_SECRET",
    accessToken: "THE_SELLER_ACCESS_TOKEN",
    shopCipher: "THE_SHOP_CIPHER");

// Every request is signed, and shop_cipher is added to the operations that take one.
var orders = await client.Orders.GetOrderListAsync(pageSize: 20);
Console.WriteLine($"{orders.Data.TotalCount} orders");
// readme:end
    }
}
