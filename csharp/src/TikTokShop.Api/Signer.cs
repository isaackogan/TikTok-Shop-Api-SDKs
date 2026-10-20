using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;

namespace TikTokShop.Api;

/// <summary>TikTok Shop request signing. Pure: no state, no I/O.</summary>
public static class Signer
{
    /// <summary>
    /// <c>secret + path + sorted key+value pairs + body (not multipart) + secret</c>, as text.
    /// </summary>
    /// <param name="path">The request path.</param>
    /// <param name="query">Decoded key and value pairs, in any order. <c>sign</c> and <c>access_token</c> are skipped.</param>
    /// <param name="contentType">The request's content type, or <c>null</c>. A multipart body is not signed.</param>
    /// <param name="body">The exact body bytes, or <c>null</c> for none.</param>
    /// <param name="appSecret">The app secret.</param>
    public static string StringToSign(
        string path,
        IEnumerable<KeyValuePair<string, string>> query,
        string? contentType,
        byte[]? body,
        string appSecret) =>
        Encoding.UTF8.GetString(Build(path, query, contentType, body, appSecret));

    /// <summary>Lowercase hex HMAC-SHA256 of <see cref="StringToSign"/>, keyed with the app secret.</summary>
    public static string Sign(
        string path,
        IEnumerable<KeyValuePair<string, string>> query,
        string? contentType,
        byte[]? body,
        string appSecret)
    {
        var hash = HMACSHA256.HashData(Encoding.UTF8.GetBytes(appSecret), Build(path, query, contentType, body, appSecret));
        return Convert.ToHexString(hash).ToLowerInvariant();
    }

    /// <summary>Whether the media type is <c>multipart/form-data</c>, ignoring parameters such as the boundary.</summary>
    public static bool IsMultipart(string? contentType) =>
        contentType is not null && contentType.TrimStart().StartsWith("multipart/form-data", StringComparison.OrdinalIgnoreCase);

    private static byte[] Build(
        string path,
        IEnumerable<KeyValuePair<string, string>> query,
        string? contentType,
        byte[]? body,
        string appSecret)
    {
        // OrderBy is stable, so repeated keys keep their order.
        var pairs = query
            .Where(p => p.Key != "sign" && p.Key != "access_token")
            .OrderBy(p => p.Key, StringComparer.Ordinal);

        var head = new StringBuilder();
        head.Append(appSecret).Append(path);
        foreach (var p in pairs)
        {
            head.Append(p.Key).Append(p.Value);
        }

        using var ms = new System.IO.MemoryStream();
        var headBytes = Encoding.UTF8.GetBytes(head.ToString());
        ms.Write(headBytes, 0, headBytes.Length);
        if (!IsMultipart(contentType) && body is not null)
        {
            ms.Write(body, 0, body.Length);
        }
        var tail = Encoding.UTF8.GetBytes(appSecret);
        ms.Write(tail, 0, tail.Length);
        return ms.ToArray();
    }
}
