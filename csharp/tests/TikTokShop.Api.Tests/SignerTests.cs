using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json;
using Xunit;

namespace TikTokShop.Api.Tests;

public class SignerTests
{
    private static readonly JsonElement Cases = Repo.Json("shared", "test-vectors", "signing.json").GetProperty("cases");

    public static IEnumerable<object[]> CaseNames() =>
        Cases.EnumerateArray().Select(c => new object[] { c.GetProperty("name").GetString()! }).ToList();

    [Fact]
    public void ThereAreVectors() => Assert.NotEmpty(Cases.EnumerateArray());

    [Theory]
    [MemberData(nameof(CaseNames))]
    public void MatchesTheSharedVector(string name)
    {
        var c = Cases.EnumerateArray().Single(x => x.GetProperty("name").GetString() == name);
        var query = c.GetProperty("query").EnumerateArray()
            .Select(p => new KeyValuePair<string, string>(p[0].GetString()!, p[1].GetString()!))
            .ToList();
        var contentType = c.GetProperty("contentType").GetString();
        var bodyText = c.GetProperty("body").GetString();
        var body = bodyText is null ? null : Encoding.UTF8.GetBytes(bodyText);
        var secret = c.GetProperty("secret").GetString()!;
        var path = c.GetProperty("path").GetString()!;

        Assert.Equal(c.GetProperty("stringToSign").GetString(), Signer.StringToSign(path, query, contentType, body, secret));
        Assert.Equal(c.GetProperty("sign").GetString(), Signer.Sign(path, query, contentType, body, secret));
    }

    [Theory]
    [InlineData("POST", "/order/202309/orders/search", true)]
    [InlineData("post", "/order/202309/orders/search", true)]
    [InlineData("GET", "/authorization/202309/shops", false)]
    [InlineData("GET", "/product/202309/products/1729507467923261408", true)]
    [InlineData("GET", "/no/such/path", false)]
    public void RequiresShopCipher(string method, string path, bool expected) =>
        Assert.Equal(expected, Operations.RequiresShopCipher(method, path));

    [Fact]
    public void RequiresShopCipherAgreesWithEveryOperationInTheRenderedMeta()
    {
        foreach (var op in Generated.Meta.Operations)
        {
            var concrete = System.Text.RegularExpressions.Regex.Replace(op.Path, @"\{[^}]+\}", "zz9");
            Assert.True(
                op.RequiresShopCipher == Operations.RequiresShopCipher(op.HttpMethod, concrete),
                $"{op.OperationId}: {op.HttpMethod} {op.Path}");
        }
    }
}
