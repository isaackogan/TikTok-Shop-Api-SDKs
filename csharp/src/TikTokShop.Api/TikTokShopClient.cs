using System;
using System.Net;
using System.Net.Http;
using System.Threading;
using TikTokShop.Api.Generated.Client;

namespace TikTokShop.Api;

/// <summary>Everything a <see cref="TikTokShopClient"/> is built from. <see cref="ToString"/> never prints a secret.</summary>
public sealed class TikTokShopOptions
{
    /// <summary>The app key.</summary>
    public string AppKey { get; set; } = "";

    /// <summary>The app secret.</summary>
    public string AppSecret { get; set; } = "";

    /// <summary>Sent as <c>x-tts-access-token</c>.</summary>
    public string? AccessToken { get; set; }

    /// <summary>Added as <c>shop_cipher</c> to the operations that take one.</summary>
    public string? ShopCipher { get; set; }

    /// <summary>Defaults to <see cref="TikTokShopClient.DefaultBaseUrl"/>.</summary>
    public string? BaseUrl { get; set; }

    /// <summary>
    /// The limit for one request, for the whole exchange. <c>null</c> means <see cref="TikTokShopClient.DefaultTimeout"/>;
    /// <see cref="TimeSpan.Zero"/> and <see cref="System.Threading.Timeout.InfiniteTimeSpan"/> mean no limit.
    /// </summary>
    public TimeSpan? Timeout { get; set; }

    /// <summary>
    /// The handler that sends the requests, used as is: its own redirect, proxy, certificate and cookie settings apply.
    /// When <c>null</c>, the SDK builds a <see cref="SocketsHttpHandler"/> that never follows redirects and uses the
    /// system proxy.
    /// </summary>
    public HttpMessageHandler? Handler { get; set; }

    /// <inheritdoc/>
    public override string ToString() =>
        $"TikTokShopOptions {{ AppKey = {AppKey}, AppSecret = ***, AccessToken = {(AccessToken is null ? "null" : "***")}, ShopCipher = {(ShopCipher is null ? "null" : "***")}, BaseUrl = {BaseUrl ?? "null"}, Timeout = {Timeout?.ToString() ?? "null"}, Handler = {(Handler is null ? "null" : Handler.GetType().Name)} }}";
}

/// <summary>
/// The TikTok Shop API client: one property per API group, each the generated <c>*Api</c> class for that tag.
/// </summary>
/// <remarks>
/// Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.
/// <para>
/// Create one client and reuse it for the life of your app: it owns a connection pool, and <see cref="WithShop"/> shares it.
/// </para>
/// <para>
/// Every request is signed, and every failure is a <see cref="TikTokShopException"/>. A reply that does not decode into
/// the generated model surfaces as the generator's own <c>ApiException</c>.
/// </para>
/// <para>
/// HTTP: by default the SDK builds a <see cref="SocketsHttpHandler"/> that never follows redirects (a 3xx reply is thrown as a
/// <see cref="TikTokShopException"/> with code 302 and the redirect target receives nothing), with the system proxy.
/// A <see cref="TikTokShopOptions.Handler"/> you pass is used as is, so its own redirect, timeout and proxy settings apply.
/// The SDK enforces <see cref="TikTokShopOptions.Timeout"/> itself.
/// </para>
/// </remarks>
public sealed class TikTokShopClient
{
    /// <summary>The API's base URL.</summary>
    public const string DefaultBaseUrl = "https://open-api.tiktokglobalshop.com";

    /// <summary>Used when no timeout is given.</summary>
    public static readonly TimeSpan DefaultTimeout = TimeSpan.FromSeconds(30);

    private readonly ShopCredentials _credentials;
    private readonly string _baseUrl;
    private readonly TimeSpan? _timeout;
    private readonly HttpMessageHandler _handler;

    /// <summary>The <c>Affiliate creator</c> operations.</summary>
    public Generated.Api.AffiliateCreatorApi AffiliateCreator { get; }

    /// <summary>The <c>Affiliate partner</c> operations.</summary>
    public Generated.Api.AffiliatePartnerApi AffiliatePartner { get; }

    /// <summary>The <c>Affiliate seller</c> operations.</summary>
    public Generated.Api.AffiliateSellerApi AffiliateSeller { get; }

    /// <summary>The <c>Analytics</c> operations.</summary>
    public Generated.Api.AnalyticsApi Analytics { get; }

    /// <summary>The <c>Authorization</c> operations.</summary>
    public Generated.Api.AuthorizationApi Authorization { get; }

    /// <summary>The <c>Customer engagement</c> operations.</summary>
    public Generated.Api.CustomerEngagementApi CustomerEngagement { get; }

    /// <summary>The <c>Customer service</c> operations.</summary>
    public Generated.Api.CustomerServiceApi CustomerService { get; }

    /// <summary>The <c>Event</c> operations.</summary>
    public Generated.Api.EventApi Event { get; }

    /// <summary>The <c>Finance</c> operations.</summary>
    public Generated.Api.FinanceApi Finance { get; }

    /// <summary>The <c>Fulfilled by TikTok (FBT)</c> operations.</summary>
    public Generated.Api.FulfilledByTikTokFBTApi FulfilledByTikTok { get; }

    /// <summary>The <c>Fulfillment</c> operations.</summary>
    public Generated.Api.FulfillmentApi Fulfillment { get; }

    /// <summary>The <c>Logistics</c> operations.</summary>
    public Generated.Api.LogisticsApi Logistics { get; }

    /// <summary>The <c>Orders</c> operations.</summary>
    public Generated.Api.OrdersApi Orders { get; }

    /// <summary>The <c>Products</c> operations.</summary>
    public Generated.Api.ProductsApi Products { get; }

    /// <summary>The <c>Promotion</c> operations.</summary>
    public Generated.Api.PromotionApi Promotion { get; }

    /// <summary>The <c>Return and refund</c> operations.</summary>
    public Generated.Api.ReturnAndRefundApi ReturnAndRefund { get; }

    /// <summary>The <c>Seller</c> operations.</summary>
    public Generated.Api.SellerApi Seller { get; }

    /// <summary>The <c>Supply chain</c> operations.</summary>
    public Generated.Api.SupplyChainApi SupplyChain { get; }

    /// <summary>The <c>Tools</c> operations.</summary>
    public Generated.Api.ToolsApi Tools { get; }

    /// <summary>Creates a client from options.</summary>
    public TikTokShopClient(TikTokShopOptions options)
        : this(
            new ShopCredentials(Required(options).AppKey, options.AppSecret, options.AccessToken, options.ShopCipher),
            options.BaseUrl,
            options.Timeout,
            options.Handler ?? CreateDefaultHandler())
    {
    }

    /// <summary>Creates a client.</summary>
    /// <param name="appKey">The app key.</param>
    /// <param name="appSecret">The app secret.</param>
    /// <param name="accessToken">Sent as <c>x-tts-access-token</c>.</param>
    /// <param name="shopCipher">Added as <c>shop_cipher</c> to the operations that take one.</param>
    /// <param name="baseUrl">Defaults to <see cref="DefaultBaseUrl"/>.</param>
    /// <param name="timeout">See <see cref="TikTokShopOptions.Timeout"/>.</param>
    /// <param name="handler">See <see cref="TikTokShopOptions.Handler"/>.</param>
    public TikTokShopClient(
        string appKey,
        string appSecret,
        string? accessToken = null,
        string? shopCipher = null,
        string? baseUrl = null,
        TimeSpan? timeout = null,
        HttpMessageHandler? handler = null)
        : this(new ShopCredentials(appKey, appSecret, accessToken, shopCipher), baseUrl, timeout, handler ?? CreateDefaultHandler())
    {
    }

    private TikTokShopClient(ShopCredentials credentials, string? baseUrl, TimeSpan? timeout, HttpMessageHandler handler)
    {
        _credentials = credentials;
        _baseUrl = (string.IsNullOrEmpty(baseUrl) ? DefaultBaseUrl : baseUrl).TrimEnd('/');
        _timeout = timeout;
        _handler = handler;

        // The signing handler carries this shop's credentials; the inner handler (and its connections) is shared by WithShop.
        // The HttpClient's own timeout is off: SigningHandler enforces the limit and tells a timeout from the caller's cancel.
        var http = new HttpClient(new SigningHandler(credentials, handler, timeout), disposeHandler: false)
        {
            Timeout = System.Threading.Timeout.InfiniteTimeSpan,
        };
        var configuration = new Configuration
        {
            BasePath = _baseUrl,
            // The generated client would otherwise apply its own 100 s limit.
            Timeout = TimeSpan.Zero,
            UserAgent = "TikTokShop.Api-csharp",
        };
        AffiliateCreator = new Generated.Api.AffiliateCreatorApi(http, configuration);
        AffiliatePartner = new Generated.Api.AffiliatePartnerApi(http, configuration);
        AffiliateSeller = new Generated.Api.AffiliateSellerApi(http, configuration);
        Analytics = new Generated.Api.AnalyticsApi(http, configuration);
        Authorization = new Generated.Api.AuthorizationApi(http, configuration);
        CustomerEngagement = new Generated.Api.CustomerEngagementApi(http, configuration);
        CustomerService = new Generated.Api.CustomerServiceApi(http, configuration);
        Event = new Generated.Api.EventApi(http, configuration);
        Finance = new Generated.Api.FinanceApi(http, configuration);
        FulfilledByTikTok = new Generated.Api.FulfilledByTikTokFBTApi(http, configuration);
        Fulfillment = new Generated.Api.FulfillmentApi(http, configuration);
        Logistics = new Generated.Api.LogisticsApi(http, configuration);
        Orders = new Generated.Api.OrdersApi(http, configuration);
        Products = new Generated.Api.ProductsApi(http, configuration);
        Promotion = new Generated.Api.PromotionApi(http, configuration);
        ReturnAndRefund = new Generated.Api.ReturnAndRefundApi(http, configuration);
        Seller = new Generated.Api.SellerApi(http, configuration);
        SupplyChain = new Generated.Api.SupplyChainApi(http, configuration);
        Tools = new Generated.Api.ToolsApi(http, configuration);
    }

    /// <summary>
    /// A client for another shop or token that shares this client's HTTP handler and connections. This client is not changed.
    /// </summary>
    /// <remarks>An argument you leave out keeps this client's value; <c>null</c> or <c>""</c> clears it.</remarks>
    public TikTokShopClient WithShop(Optional<string?> accessToken = default, Optional<string?> shopCipher = default) =>
        new(_credentials.With(accessToken, shopCipher), _baseUrl, _timeout, _handler);

    /// <inheritdoc/>
    public override string ToString() => $"TikTokShopClient {{ BaseUrl = {_baseUrl}, Credentials = {_credentials} }}";

    private static TikTokShopOptions Required(TikTokShopOptions? options) =>
        options ?? throw new ArgumentNullException(nameof(options));

    /// <summary>How long a pooled connection is reused before it is closed, so a long-lived client picks up DNS changes.</summary>
    internal static readonly TimeSpan PooledConnectionLifetime = TimeSpan.FromMinutes(2);

    internal static SocketsHttpHandler CreateDefaultHandler() => new()
    {
        AllowAutoRedirect = false,
        UseCookies = false,
        AutomaticDecompression = DecompressionMethods.All,
        PooledConnectionLifetime = PooledConnectionLifetime,
    };
}
