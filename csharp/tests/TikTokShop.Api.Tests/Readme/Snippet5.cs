// This file is compiled so the README's example is known to build. ReadmeTests compares the two marked regions with
// README.md (usings, a blank line, then the body), so edit both together.
// readme:usings
using TikTokShop.Api;
// readme:end

namespace TikTokShop.Api.Tests.Readme;

internal static class Snippet5
{
    internal static async System.Threading.Tasks.Task Run()
    {
// readme:body
var client = new TikTokShopClient("YOUR_APP_KEY", "YOUR_APP_SECRET", accessToken: "TOKEN_A", shopCipher: "CIPHER_A");

// Another shop, sharing this client's connections. `client` is not changed.
var other = client.WithShop(accessToken: "TOKEN_B", shopCipher: "CIPHER_B");

// An argument you leave out keeps this client's value; null (or "") clears it.
var sameShopNewToken = client.WithShop(accessToken: "TOKEN_A2");
var noShop = client.WithShop(shopCipher: new Optional<string?>(null));
// readme:end
    }
}
