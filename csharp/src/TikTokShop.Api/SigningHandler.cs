using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace TikTokShop.Api;

/// <summary>
/// A <see cref="DelegatingHandler"/> that signs every request and turns every failure into a <see cref="TikTokShopException"/>.
/// </summary>
/// <remarks>
/// Request hook, in order:
/// <list type="number">
/// <item>drop any <c>app_key</c>, <c>timestamp</c>, <c>sign</c> and <c>shop_cipher</c> from the query;</item>
/// <item>add <c>shop_cipher</c> when the operation takes one and the credentials have one;</item>
/// <item>add <c>app_key</c> and <c>timestamp</c>;</item>
/// <item>set <c>x-tts-access-token</c> when the credentials have a token;</item>
/// <item>sign the final path, decoded query, content type and exact body bytes (a multipart body is never read);</item>
/// <item>add <c>sign</c>. The query is rebuilt by hand with RFC 3986 percent-encoding, so <c>+</c> and <c>/</c> survive.</item>
/// </list>
/// Response hook: a 2xx reply with <c>code</c> 0 passes through; anything else throws, see <see cref="TikTokShopException"/>.
/// The timeout is enforced here, over the whole exchange including reading the reply.
/// </remarks>
public sealed class SigningHandler : DelegatingHandler
{
    private static readonly HashSet<string> Reserved = new(StringComparer.Ordinal) { "app_key", "timestamp", "sign", "shop_cipher" };

    private readonly ShopCredentials _credentials;
    private readonly TimeSpan? _timeout;

    /// <summary>Creates the handler.</summary>
    /// <param name="credentials">What to sign with.</param>
    /// <param name="innerHandler">The handler that sends the request.</param>
    /// <param name="timeout">
    /// The limit for one request. <c>null</c> means <see cref="TikTokShopClient.DefaultTimeout"/>;
    /// <see cref="TimeSpan.Zero"/> and <see cref="System.Threading.Timeout.InfiniteTimeSpan"/> mean no limit.
    /// </param>
    public SigningHandler(ShopCredentials credentials, HttpMessageHandler innerHandler, TimeSpan? timeout = null)
        : base(innerHandler)
    {
        _credentials = credentials ?? throw new ArgumentNullException(nameof(credentials));
        _timeout = Handlers.ResolveTimeout(timeout, nameof(timeout));
    }

    /// <inheritdoc/>
    protected override HttpResponseMessage Send(HttpRequestMessage request, CancellationToken cancellationToken) =>
        SendAsync(request, cancellationToken).GetAwaiter().GetResult();

    /// <inheritdoc/>
    protected override async Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
    {
        var uri = request.RequestUri ?? throw new InvalidOperationException("The request has no URI.");
        await PrepareAsync(request, uri, cancellationToken).ConfigureAwait(false);

        using var cts = CancellationTokenSource.CreateLinkedTokenSource(cancellationToken);
        if (_timeout is { } limit)
        {
            cts.CancelAfter(limit);
        }

        HttpResponseMessage response;
        byte[] payload;
        try
        {
            response = await base.SendAsync(request, cts.Token).ConfigureAwait(false);
            try
            {
                payload = await response.Content.ReadAsByteArrayAsync(cts.Token).ConfigureAwait(false);
            }
            catch
            {
                response.Dispose();
                throw;
            }
        }
        catch (TikTokShopException)
        {
            throw;
        }
        catch (OperationCanceledException) when (cancellationToken.IsCancellationRequested)
        {
            throw; // the caller cancelled: not a failure of the call
        }
        catch (Exception e)
        {
            throw Failure(e, request.RequestUri ?? uri);
        }

        using (var reply = Reply.Read((int)response.StatusCode, response.ReasonPhrase, payload, "Response"))
        {
            if (reply.Error is not null)
            {
                response.Dispose();
                throw reply.Error;
            }
        }

        // The body was consumed: hand the caller a fresh content with the same headers.
        var old = response.Content;
        var fresh = new ByteArrayContent(payload);
        foreach (var h in old.Headers)
        {
            if (!string.Equals(h.Key, "Content-Length", StringComparison.OrdinalIgnoreCase))
            {
                fresh.Headers.TryAddWithoutValidation(h.Key, h.Value);
            }
        }
        response.Content = fresh;
        old.Dispose();
        return response;
    }

    private async Task PrepareAsync(HttpRequestMessage request, Uri uri, CancellationToken cancellationToken)
    {
        var c = _credentials;
        var path = uri.AbsolutePath;

        // 1. drop reserved parameters
        var query = ParseQuery(uri.Query).Where(p => !Reserved.Contains(p.Key)).ToList();
        // 2. shop_cipher
        if (c.ShopCipher is not null && Operations.RequiresShopCipher(request.Method.Method, path))
        {
            query.Add(new("shop_cipher", c.ShopCipher));
        }
        // 3. app_key, timestamp
        query.Add(new("app_key", c.AppKey));
        query.Add(new("timestamp", DateTimeOffset.UtcNow.ToUnixTimeSeconds().ToString(System.Globalization.CultureInfo.InvariantCulture)));
        // 4. access token
        request.Headers.Remove("x-tts-access-token");
        if (c.AccessToken is not null)
        {
            request.Headers.TryAddWithoutValidation("x-tts-access-token", c.AccessToken);
        }
        // 5. sign over the final path, decoded query and body bytes
        var contentType = request.Content?.Headers.ContentType?.ToString();
        byte[]? bytes = null;
        if (request.Content is { } content && !Signer.IsMultipart(contentType))
        {
            // Read the exact bytes and hand back a fresh content, so the transport sends what was signed.
            bytes = await content.ReadAsByteArrayAsync(cancellationToken).ConfigureAwait(false);
            var fresh = new ByteArrayContent(bytes);
            foreach (var h in content.Headers)
            {
                if (!string.Equals(h.Key, "Content-Length", StringComparison.OrdinalIgnoreCase))
                {
                    fresh.Headers.TryAddWithoutValidation(h.Key, h.Value);
                }
            }
            request.Content = fresh;
            content.Dispose();
        }
        // 6. sign
        query.Add(new("sign", Signer.Sign(path, query, contentType, bytes, c.AppSecret)));

        var encoded = string.Join("&", query.Select(p => Uri.EscapeDataString(p.Key) + "=" + Uri.EscapeDataString(p.Value)));
        request.RequestUri = new Uri(uri.GetLeftPart(UriPartial.Path) + "?" + encoded);
    }

    /// <summary>Parse a raw query string (with or without the leading <c>?</c>) into decoded pairs. A literal <c>+</c> stays a <c>+</c>.</summary>
    private static List<KeyValuePair<string, string>> ParseQuery(string raw)
    {
        var result = new List<KeyValuePair<string, string>>();
        foreach (var part in raw.TrimStart('?').Split('&', StringSplitOptions.RemoveEmptyEntries))
        {
            var i = part.IndexOf('=');
            result.Add(i < 0
                ? new(Uri.UnescapeDataString(part), "")
                : new(Uri.UnescapeDataString(part[..i]), Uri.UnescapeDataString(part[(i + 1)..])));
        }
        return result;
    }

    /// <summary>R13c and R15: no response at all. The original exception is not kept, as it can hold the URL.</summary>
    private TikTokShopException Failure(Exception e, Uri uri) =>
        ErrorScrub.Failure("Request", e, uri, new[] { _credentials.AppSecret, _credentials.AccessToken, _credentials.ShopCipher });
}
