using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Text.Json;
using System.Threading;
using System.Threading.Tasks;

namespace TikTokShop.Api;

/// <summary>What the authorization page is for.</summary>
public enum AuthorizationType
{
    /// <summary>Authorizes your app for a seller. Needs a service ID.</summary>
    Seller,

    /// <summary>Authorizes your app for a partner. Needs a service ID.</summary>
    Partner,

    /// <summary>Authorizes your app for an affiliate creator.</summary>
    Creator,
}

/// <summary>Which TikTok Shop region hosts the authorization page.</summary>
public enum AuthorizationRegion
{
    /// <summary>The United States host.</summary>
    Us,

    /// <summary>The rest-of-world host.</summary>
    Row,
}

/// <summary>Everything a <see cref="TikTokShopAuth"/> is built from. <see cref="ToString"/> never prints a secret.</summary>
public sealed class TikTokShopAuthOptions
{
    /// <summary>The app key.</summary>
    public string AppKey { get; set; } = "";

    /// <summary>The app secret.</summary>
    public string AppSecret { get; set; } = "";

    /// <summary>Your Partner Center service ID. Needed for seller and partner authorization URLs.</summary>
    public string? ServiceId { get; set; }

    /// <summary>Defaults to <see cref="TikTokShopAuth.DefaultBaseUrl"/>; set it for a test server.</summary>
    public string? BaseUrl { get; set; }

    /// <summary>
    /// The limit for one token request. <c>null</c> means <see cref="TikTokShopClient.DefaultTimeout"/>;
    /// <see cref="TimeSpan.Zero"/> and <see cref="System.Threading.Timeout.InfiniteTimeSpan"/> mean no limit.
    /// </summary>
    public TimeSpan? Timeout { get; set; }

    /// <summary>
    /// The handler that sends the token requests, used as is, except that it must not follow redirects:
    /// the constructor throws for a <see cref="SocketsHttpHandler"/> or <see cref="HttpClientHandler"/> (or one wrapped by
    /// <see cref="DelegatingHandler"/>s) with <c>AllowAutoRedirect</c> true, because the URL holds the app secret and the code.
    /// When <c>null</c>, the SDK uses a shared <see cref="SocketsHttpHandler"/> that never follows redirects.
    /// </summary>
    public HttpMessageHandler? Handler { get; set; }

    /// <inheritdoc/>
    public override string ToString() =>
        $"TikTokShopAuthOptions {{ AppKey = {AppKey}, AppSecret = ***, ServiceId = {ServiceId ?? "null"}, BaseUrl = {BaseUrl ?? "null"}, Timeout = {Timeout?.ToString() ?? "null"}, Handler = {(Handler is null ? "null" : Handler.GetType().Name)} }}";
}

/// <summary>
/// The OAuth helper: authorization URLs, code exchange and token refresh.
/// </summary>
/// <remarks>
/// Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.
/// <para>
/// Every failure is a <see cref="TikTokShopException"/>. Its message and inner exceptions never contain the request URL or the
/// app secret, the code or the refresh token (the token requests carry them in the URL's query).
/// </para>
/// <para>
/// HTTP: by default the SDK uses a shared <see cref="SocketsHttpHandler"/> that never follows redirects, with the system proxy.
/// A handler you pass is used as is (its proxy and TLS settings apply), except that it must not follow redirects, see
/// <see cref="TikTokShopAuthOptions.Handler"/>: a 3xx reply is thrown with code 302 and the redirect target receives nothing.
/// </para>
/// </remarks>
public sealed class TikTokShopAuth
{
    /// <summary>The token endpoints' host.</summary>
    public const string DefaultBaseUrl = "https://auth.tiktok-shops.com";

    private static readonly Lazy<SocketsHttpHandler> SharedHandler = new(TikTokShopClient.CreateDefaultHandler);

    private readonly string _appKey;
    private readonly string _appSecret;
    private readonly string? _serviceId;
    private readonly string _baseUrl;
    private readonly TimeSpan? _timeout;
    private readonly HttpClient _http;

    /// <summary>Creates the helper from options.</summary>
    public TikTokShopAuth(TikTokShopAuthOptions options)
    {
        if (options is null)
        {
            throw new ArgumentNullException(nameof(options));
        }
        _appKey = options.AppKey ?? throw new ArgumentNullException(nameof(options.AppKey));
        _appSecret = options.AppSecret ?? throw new ArgumentNullException(nameof(options.AppSecret));
        _serviceId = string.IsNullOrEmpty(options.ServiceId) ? null : options.ServiceId;
        _baseUrl = (string.IsNullOrEmpty(options.BaseUrl) ? DefaultBaseUrl : options.BaseUrl).TrimEnd('/');
        _timeout = Handlers.ResolveTimeout(options.Timeout, nameof(options.Timeout));
        if (Handlers.FollowsRedirects(options.Handler))
        {
            throw new ArgumentException(
                "The handler follows redirects (AllowAutoRedirect is true). Token requests carry the app secret and the code in the URL, so set AllowAutoRedirect = false.",
                nameof(options.Handler));
        }
        // The HttpClient's own timeout is off: the limit is enforced per call, over the whole exchange.
        _http = new HttpClient(options.Handler ?? SharedHandler.Value, disposeHandler: false)
        {
            Timeout = System.Threading.Timeout.InfiniteTimeSpan,
        };
    }

    /// <summary>Creates the helper.</summary>
    /// <param name="appKey">The app key.</param>
    /// <param name="appSecret">The app secret.</param>
    /// <param name="serviceId">Your Partner Center service ID. Needed for seller and partner authorization URLs.</param>
    /// <param name="baseUrl">Overrides <see cref="DefaultBaseUrl"/>, for example for a test server.</param>
    /// <param name="timeout">See <see cref="TikTokShopAuthOptions.Timeout"/>.</param>
    /// <param name="handler">See <see cref="TikTokShopAuthOptions.Handler"/>.</param>
    public TikTokShopAuth(
        string appKey,
        string appSecret,
        string? serviceId = null,
        string? baseUrl = null,
        TimeSpan? timeout = null,
        HttpMessageHandler? handler = null)
        : this(new TikTokShopAuthOptions
        {
            AppKey = appKey,
            AppSecret = appSecret,
            ServiceId = serviceId,
            BaseUrl = baseUrl,
            Timeout = timeout,
            Handler = handler,
        })
    {
    }

    /// <summary>
    /// The page to send the seller (or partner, or creator) to.
    /// </summary>
    /// <param name="type">What the page authorizes.</param>
    /// <param name="region">Which region's host.</param>
    /// <param name="state">Echoed back to your redirect URL. <c>null</c> or empty adds no <c>state</c> parameter.</param>
    /// <exception cref="ArgumentOutOfRangeException">An unknown type or region.</exception>
    /// <exception cref="InvalidOperationException">A seller or partner URL without a service ID.</exception>
    public string AuthorizationUrl(AuthorizationType type, AuthorizationRegion region, string? state = null)
    {
        var (us, row, path) = type switch
        {
            AuthorizationType.Seller => ("https://services.us.tiktokshop.com", "https://services.tiktokshop.com", "/open/authorize"),
            AuthorizationType.Partner => ("https://partner.us.tiktokshop.com", "https://partner.tiktokshop.com", "/open/authorize"),
            AuthorizationType.Creator => ("https://shop.tiktok.com", "https://shop.tiktok.com", "/alliance/creator/auth"),
            _ => throw new ArgumentOutOfRangeException(nameof(type), type, "Unknown authorization type (seller, partner or creator)."),
        };
        var host = region switch
        {
            AuthorizationRegion.Us => us,
            AuthorizationRegion.Row => row,
            _ => throw new ArgumentOutOfRangeException(nameof(region), region, "Unknown region (us or row)."),
        };

        string first;
        if (type == AuthorizationType.Creator)
        {
            first = "app_key=" + Uri.EscapeDataString(_appKey);
        }
        else
        {
            if (_serviceId is null)
            {
                throw new InvalidOperationException($"A service ID is required for {type} authorization URLs.");
            }
            first = "service_id=" + Uri.EscapeDataString(_serviceId);
        }
        var url = host + path + "?" + first;
        if (!string.IsNullOrEmpty(state))
        {
            url += "&state=" + Uri.EscapeDataString(state);
        }
        return url;
    }

    /// <summary>Trades the <c>auth_code</c> from your redirect URL for tokens.</summary>
    /// <exception cref="TikTokShopException">Every failure.</exception>
    public Task<TokenSet> ExchangeCodeAsync(string code, CancellationToken cancellationToken = default) =>
        TokenAsync("get", "auth_code", code, "authorized_code", nameof(code), cancellationToken);

    /// <summary>Trades the <c>auth_code</c> from your redirect URL for tokens.</summary>
    /// <exception cref="TikTokShopException">Every failure.</exception>
    public TokenSet ExchangeCode(string code) => ExchangeCodeAsync(code).GetAwaiter().GetResult();

    /// <summary>Trades a refresh token for new tokens.</summary>
    /// <exception cref="TikTokShopException">Every failure.</exception>
    public Task<TokenSet> RefreshAsync(string refreshToken, CancellationToken cancellationToken = default) =>
        TokenAsync("refresh", "refresh_token", refreshToken, "refresh_token", nameof(refreshToken), cancellationToken);

    /// <summary>Trades a refresh token for new tokens.</summary>
    /// <exception cref="TikTokShopException">Every failure.</exception>
    public TokenSet Refresh(string refreshToken) => RefreshAsync(refreshToken).GetAwaiter().GetResult();

    /// <inheritdoc/>
    public override string ToString() =>
        $"TikTokShopAuth {{ AppKey = {_appKey}, AppSecret = ***, ServiceId = {_serviceId ?? "null"}, BaseUrl = {_baseUrl} }}";

    private async Task<TokenSet> TokenAsync(
        string endpoint,
        string name,
        string value,
        string grantType,
        string paramName,
        CancellationToken cancellationToken)
    {
        if (value is null)
        {
            throw new ArgumentNullException(paramName);
        }
        if (value.Length == 0)
        {
            throw new ArgumentException("The value must not be empty.", paramName);
        }

        var where = $"Token request to /api/v2/token/{endpoint}";
        // The query is built by hand (RFC 3986, in the pinned order).
        var query = "app_key=" + Uri.EscapeDataString(_appKey)
            + "&app_secret=" + Uri.EscapeDataString(_appSecret)
            + "&" + name + "=" + Uri.EscapeDataString(value)
            + "&grant_type=" + grantType;
        var uri = new Uri($"{_baseUrl}/api/v2/token/{endpoint}?{query}");

        int status;
        string? reason;
        byte[] payload;
        using (var cts = CancellationTokenSource.CreateLinkedTokenSource(cancellationToken))
        {
            if (_timeout is { } limit)
            {
                cts.CancelAfter(limit);
            }
            try
            {
                using var request = new HttpRequestMessage(HttpMethod.Get, uri);
                using var response = await _http.SendAsync(request, cts.Token).ConfigureAwait(false);
                status = (int)response.StatusCode;
                reason = response.ReasonPhrase;
                payload = await response.Content.ReadAsByteArrayAsync(cts.Token).ConfigureAwait(false);
            }
            catch (OperationCanceledException) when (cancellationToken.IsCancellationRequested)
            {
                throw; // the caller cancelled: not a failure of the call
            }
            catch (Exception e)
            {
                throw ErrorScrub.Failure(where, e, uri, new[] { _appSecret, value });
            }
        }

        return ToTokenSet(status, reason, payload);
    }

    /// <summary>R13b, and R14 for the fields.</summary>
    private static TokenSet ToTokenSet(int status, string? reason, byte[] payload)
    {
        using var reply = Reply.Read(status, reason, payload, "Token response");
        if (reply.Error is not null)
        {
            throw reply.Error;
        }
        if (!reply.Root.TryGetProperty("data", out var data) || data.ValueKind != JsonValueKind.Object)
        {
            throw new TikTokShopException("Token response has no data", -1, reply.RequestId, status);
        }

        string? Text(string property) =>
            data.TryGetProperty(property, out var p) && p.ValueKind == JsonValueKind.String ? p.GetString() : null;

        var access = Text("access_token");
        var refresh = Text("refresh_token");
        if (string.IsNullOrEmpty(access)
            || string.IsNullOrEmpty(refresh)
            || !data.TryGetProperty("access_token_expire_in", out var accessExp) || !Reply.TryGetInteger(accessExp, out var accessExpireIn)
            || !data.TryGetProperty("refresh_token_expire_in", out var refreshExp) || !Reply.TryGetInteger(refreshExp, out var refreshExpireIn))
        {
            throw new TikTokShopException(
                "Token response is missing a token field, or one has the wrong type",
                -1,
                reply.RequestId,
                status);
        }

        // Optional fields: anything of the wrong type is treated as absent. open_id is an ID, so a number keeps its digits.
        string? openId = null;
        if (data.TryGetProperty("open_id", out var open))
        {
            if (open.ValueKind == JsonValueKind.String)
            {
                openId = open.GetString();
            }
            else if (open.ValueKind == JsonValueKind.Number && Reply.IsIntegerLiteral(open.GetRawText()))
            {
                openId = open.GetRawText();
            }
        }
        int? userType = null;
        if (data.TryGetProperty("user_type", out var ut) && Reply.TryGetInteger(ut, out var utl) && utl is >= int.MinValue and <= int.MaxValue)
        {
            userType = (int)utl;
        }
        var scopes = new List<string>();
        if (data.TryGetProperty("granted_scopes", out var gs) && gs.ValueKind == JsonValueKind.Array)
        {
            scopes.AddRange(gs.EnumerateArray().Where(s => s.ValueKind == JsonValueKind.String).Select(s => s.GetString()!));
        }

        return new TokenSet(
            access,
            accessExpireIn,
            refresh,
            refreshExpireIn,
            openId,
            Text("seller_name"),
            Text("seller_base_region"),
            userType,
            scopes);
    }
}
