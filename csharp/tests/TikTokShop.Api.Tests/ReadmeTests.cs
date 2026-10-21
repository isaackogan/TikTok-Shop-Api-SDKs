using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
using System.Xml.Linq;
using Xunit;

namespace TikTokShop.Api.Tests;

/// <summary>
/// The package page. Each C# block of README.md is compiled on its own (Readme/SnippetN.cs, built with the tests); these tests
/// check the files still hold exactly what the README shows.
/// </summary>
public class ReadmeTests
{
    private static readonly string Csharp = Path.Combine(Repo.Root, "csharp");
    private static readonly string Readme = File.ReadAllText(Path.Combine(Csharp, "README.md")).Replace("\r\n", "\n");

    private static List<string> Blocks() =>
        Regex.Matches(Readme, "```csharp\n(.*?)```", RegexOptions.Singleline).Select(m => m.Groups[1].Value.TrimEnd('\n')).ToList();

    private static string Region(string text, string name)
    {
        var lines = text.Replace("\r\n", "\n").Split('\n');
        var start = Array.FindIndex(lines, l => l.TrimEnd() == "// readme:" + name);
        Assert.True(start >= 0, $"no // readme:{name} marker");
        var end = Array.FindIndex(lines, start + 1, l => l.TrimEnd() == "// readme:end");
        Assert.True(end > start, $"// readme:{name} is not closed");
        return string.Join("\n", lines[(start + 1)..end]);
    }

    public static IEnumerable<object[]> BlockIndexes() => Enumerable.Range(1, Blocks().Count).Select(i => new object[] { i }).ToList();

    [Fact]
    public void EveryCSharpBlockHasItsOwnCompiledFileAndNoFileIsLeftOver()
    {
        var files = Directory.GetFiles(Path.Combine(Csharp, "tests", "TikTokShop.Api.Tests", "Readme"), "Snippet*.cs")
            .Select(Path.GetFileName)
            .OrderBy(n => n, StringComparer.Ordinal)
            .ToList();

        Assert.NotEmpty(Blocks());
        Assert.Equal(
            Enumerable.Range(1, Blocks().Count).Select(i => $"Snippet{i}.cs").OrderBy(n => n, StringComparer.Ordinal).ToList(),
            files);
    }

    [Theory]
    [MemberData(nameof(BlockIndexes))]
    public void EachBlockIsExactlyItsCompiledFileImportsIncluded(int index)
    {
        var file = File.ReadAllText(Path.Combine(Csharp, "tests", "TikTokShop.Api.Tests", "Readme", $"Snippet{index}.cs"));

        var expected = Region(file, "usings") + "\n\n" + Region(file, "body");

        Assert.Equal(expected.TrimEnd('\n'), Blocks()[index - 1]);
    }

    [Fact]
    public void EveryBlockStartsWithItsOwnUsings()
    {
        foreach (var block in Blocks())
        {
            Assert.StartsWith("using ", block);
        }
    }

    [Fact]
    public void ThePackagePageSaysWhatItMust()
    {
        Assert.Contains("\nUnofficial. Not affiliated with or endorsed by TikTok or ByteDance.\n", Readme);
        Assert.Contains("dotnet add package TikTokShop.Api", Readme);
        Assert.Contains(".NET 8", Readme);
        Assert.Contains("TikTok Shop API", Readme);
        Assert.Contains("https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/.openapi/tiktok-shop.openapi.yaml", Readme);
        Assert.Contains("has not been verified against the live API", Readme);
        Assert.Contains("TikTokShopClient", Readme);
        Assert.Contains("WithShop", Readme);
        Assert.Contains("VerifyAndParse", Readme);
        Assert.Contains("OAuth", Readme);
    }

    [Fact]
    public void ThePackagePageHasNoLogoAndNeverSaysOfficial()
    {
        // No logo: the only images allowed are img.shields.io badges.
        var images = Regex.Matches(Readme, @"!\[").Count;
        var badges = Regex.Matches(Readme, @"!\[[^\]\n]*\]\(https://img\.shields\.io/").Count;
        Assert.True(images == badges, "No logo: the only images allowed are img.shields.io badges.");
        Assert.DoesNotContain("<img", Readme, StringComparison.OrdinalIgnoreCase);
        // "Unofficial" is the only place the word appears.
        Assert.Empty(Regex.Matches(Readme, @"(?<!Un)official", RegexOptions.IgnoreCase));
    }

    [Fact]
    public void TheClientIsNamedTikTokShopClientEverywhere()
    {
        Assert.DoesNotMatch(@"new TikTokShop\(", Readme);
        Assert.Contains(typeof(TikTokShopClient).Name, Readme);
    }

    [Fact]
    public void TheLicenseIsTheRepositorysMit()
    {
        Assert.Equal(
            File.ReadAllText(Path.Combine(Repo.Root, "LICENSE")).Replace("\r\n", "\n"),
            File.ReadAllText(Path.Combine(Csharp, "LICENSE")).Replace("\r\n", "\n"));
    }

    [Fact]
    public void TheProjectCarriesThePackageMetadata()
    {
        var props = XDocument.Load(Path.Combine(Csharp, "src", "TikTokShop.Api", "TikTokShop.Api.csproj"))
            .Descendants("PropertyGroup").Elements().GroupBy(e => e.Name.LocalName).ToDictionary(g => g.Key, g => g.Last().Value);

        Assert.Equal("TikTokShop.Api", props["PackageId"]);
        // Any plain X.Y.Z: release.yml bumps it, so no test may pin a version.
        Assert.Matches(@"^\d+\.\d+\.\d+$", props["Version"]);
        Assert.Equal("MIT", props["PackageLicenseExpression"]);
        Assert.Equal("README.md", props["PackageReadmeFile"]);
        Assert.Equal("Isaac Kogan", props["Authors"]);
        Assert.Equal("tiktok;tiktok-shop;tiktok-shop-api;ecommerce;sdk;openapi", props["PackageTags"]);
        Assert.Equal("https://github.com/isaackogan/TikTok-Shop-Api-SDKs", props["RepositoryUrl"]);
        Assert.Equal("git", props["RepositoryType"]);
        Assert.Equal("true", props["PublishRepositoryUrl"]);
        Assert.Equal("true", props["GenerateDocumentationFile"]);
        // NuGet shows the description, not the README.
        Assert.EndsWith("Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.", props["Description"]);
        Assert.Contains("has not been verified against the live API", props["PackageReleaseNotes"]);
        Assert.DoesNotContain("First release", props["PackageReleaseNotes"]);
        // The User-Agent carries the package version.
        Assert.Equal("tiktok-shop-api-csharp/" + props["Version"], TikTokShopClient.UserAgent);
        Assert.NotEmpty(props["PackageProjectUrl"]);
        // The XML docs ship; the missing-docs warning stays silenced for the generated models.
        Assert.Contains("CS1591", props["NoWarn"]);
    }
}
