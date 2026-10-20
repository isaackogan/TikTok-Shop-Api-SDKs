// This file is compiled so the README's example is known to build. ReadmeTests compares the two marked regions with
// README.md (usings, a blank line, then the body), so edit both together.
// readme:usings
using System.Text.Json;
using TikTokShop.Api;
// readme:end

namespace TikTokShop.Api.Tests.Readme;

internal static class Snippet2
{
    internal static async System.Threading.Tasks.Task Run()
    {
// readme:body
var auth = new TikTokShopAuth(appKey: "YOUR_APP_KEY", appSecret: "YOUR_APP_SECRET");

// What ExchangeCodeAsync gave you. Serializing a TokenSet writes the real tokens, so encrypt it at rest.
var tokens = new TokenSet("ACCESS_TOKEN", 1700000000, "REFRESH_TOKEN", 1700600000);
string stored = JsonSerializer.Serialize(tokens);

// Later: refresh before the access token expires.
TokenSet loaded = JsonSerializer.Deserialize<TokenSet>(stored)!;
TokenSet fresh = await auth.RefreshAsync(loaded.RefreshToken);
// readme:end
    }
}
