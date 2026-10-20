using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text.RegularExpressions;

namespace TikTokShop.Api;

/// <summary>R15: keeps secrets and query strings out of error text.</summary>
internal static class ErrorScrub
{
    /// <summary>Strip the request URL's query, every signing or token parameter, and every secret out of a transport error message.</summary>
    public static string Scrub(string message, Uri? uri, IEnumerable<string?> secrets)
    {
        if (uri is not null)
        {
            var bare = uri.GetLeftPart(UriPartial.Path);
            message = message.Replace(uri.ToString(), bare).Replace(uri.AbsoluteUri, bare);
        }
        message = Regex.Replace(message, @"(\bhttps?://[^\s?#]*)\?[^\s)]*", "$1", RegexOptions.IgnoreCase);
        message = Regex.Replace(message, @"[?&](?:app_key|app_secret|auth_code|refresh_token|grant_type|timestamp|sign|shop_cipher)=[^\s&)]*", "");
        foreach (var secret in secrets)
        {
            if (!string.IsNullOrEmpty(secret))
            {
                message = message.Replace(secret, "***").Replace(Uri.EscapeDataString(secret), "***");
            }
        }
        return message;
    }

    /// <summary>
    /// The exception for a call that got no HTTP response at all (R13c): code -1, no status, and a fresh inner exception with the
    /// scrubbed text, because the original often holds the request URL.
    /// </summary>
    public static TikTokShopException Failure(string what, Exception e, Uri? uri, IEnumerable<string?> secrets)
    {
        var timedOut = e is OperationCanceledException or TimeoutException || e.InnerException is TimeoutException;
        var clean = Scrub(e.Message ?? "", uri, secrets);
        var message = $"{what} {(timedOut ? "timed out" : "failed")} ({e.GetType().Name}): {clean}";
        Exception inner = timedOut ? new TimeoutException(clean) : new HttpRequestException(clean);
        return new TikTokShopException(message, -1, "", null, inner);
    }
}

/// <summary>Checks on a caller-supplied handler.</summary>
internal static class Handlers
{
    /// <summary>
    /// Whether a redirect would be followed inside this handler (or inside any handler it wraps), where the SDK cannot stop it.
    /// </summary>
    public static bool FollowsRedirects(HttpMessageHandler? handler)
    {
        for (var h = handler; h is not null; h = (h as DelegatingHandler)?.InnerHandler)
        {
            switch (h)
            {
                case SocketsHttpHandler s:
                    return s.AllowAutoRedirect;
                case HttpClientHandler c:
                    return c.AllowAutoRedirect;
            }
        }
        return false;
    }

    /// <summary>A timeout as the SDK reads it: <c>null</c> is the default; zero and infinite mean no limit (returned as <c>null</c>).</summary>
    public static TimeSpan? ResolveTimeout(TimeSpan? timeout, string paramName)
    {
        var t = timeout ?? TikTokShopClient.DefaultTimeout;
        if (t == TimeSpan.Zero || t == System.Threading.Timeout.InfiniteTimeSpan)
        {
            return null;
        }
        if (t < TimeSpan.Zero)
        {
            throw new ArgumentOutOfRangeException(paramName, "The timeout must not be negative (zero or Timeout.InfiniteTimeSpan mean no limit).");
        }
        return t;
    }
}
