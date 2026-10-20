using System;
using System.Collections.Generic;
using System.Linq;
using TikTokShop.Api.Generated;

namespace TikTokShop.Api;

/// <summary>Looks up API operations by HTTP method and path.</summary>
public static class Operations
{
    private sealed record Matcher(string Method, string[] Segments, int Literals, bool NeedsShopCipher);

    private static readonly Lazy<IReadOnlyList<Matcher>> Matchers = new(() =>
        Meta.Operations
            .Select(o =>
            {
                var segments = o.Path.Split('/');
                return new Matcher(
                    o.HttpMethod.ToUpperInvariant(),
                    segments,
                    segments.Count(s => !IsParameter(s)),
                    o.RequiresShopCipher);
            })
            .ToList());

    /// <summary>
    /// Whether the operation matching <paramref name="method"/> and <paramref name="path"/> takes a <c>shop_cipher</c>
    /// query parameter. <c>{x}</c> in a path template matches exactly one segment, the method compare is
    /// case-insensitive, and the template with the most literal segments wins.
    /// </summary>
    public static bool RequiresShopCipher(string method, string path)
    {
        var m = method.ToUpperInvariant();
        var parts = path.Split('/');
        Matcher? best = null;
        foreach (var x in Matchers.Value)
        {
            if (x.Method == m && Matches(x.Segments, parts) && (best is null || x.Literals > best.Literals))
            {
                best = x;
            }
        }
        return best is not null && best.NeedsShopCipher;
    }

    private static bool IsParameter(string segment) => segment.Length > 2 && segment[0] == '{' && segment[^1] == '}';

    private static bool Matches(string[] template, string[] actual)
    {
        if (template.Length != actual.Length)
        {
            return false;
        }
        for (var i = 0; i < template.Length; i++)
        {
            if (IsParameter(template[i]))
            {
                if (actual[i].Length == 0)
                {
                    return false;
                }
            }
            else if (template[i] != actual[i])
            {
                return false;
            }
        }
        return true;
    }
}
