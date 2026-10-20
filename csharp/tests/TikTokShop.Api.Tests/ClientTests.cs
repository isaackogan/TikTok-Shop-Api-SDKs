using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading;
using System.Threading.Tasks;
using TikTokShop.Api.Generated.Client;
using TikTokShop.Api.Generated.Model;
using Xunit;

namespace TikTokShop.Api.Tests;

public class ClientTests
{
    private const string Secret = "secret-for-tests";

    private static TikTokShopClient NewClient(
        string baseUrl,
        string? token = "tok",
        string? cipher = "cipher",
        TimeSpan? timeout = null,
        HttpMessageHandler? handler = null) =>
        new TikTokShopClient(
            appKey: "app123",
            appSecret: Secret,
            accessToken: token,
            shopCipher: cipher,
            baseUrl: baseUrl,
            timeout: timeout ?? TimeSpan.FromSeconds(10),
            handler: handler);

    /// <summary>The sign the server can compute from what it received.</summary>
    private static void AssertSigned(RecordedRequest r)
    {
        var all = r.Query;
        var sign = Assert.Single(all.Where(p => p.Key == "sign")).Value;
        var rest = all.Where(p => p.Key != "sign").ToList();
        var contentType = r.Header("Content-Type");
        byte[]? body = Signer.IsMultipart(contentType) || r.Body.Length == 0 ? null : r.Body;
        Assert.Equal(Signer.Sign(r.RawPath, rest, contentType, body, Secret), sign);
    }

    private static IEnumerable<string> Chain(Exception e)
    {
        for (Exception? x = e; x is not null; x = x.InnerException)
        {
            yield return x.Message;
        }
        yield return e.ToString();
    }

    private static void AssertNoQueryOrSecret(Exception e)
    {
        foreach (var text in Chain(e))
        {
            Assert.DoesNotContain("app_key=", text);
            Assert.DoesNotContain("timestamp=", text);
            Assert.DoesNotContain("sign=", text);
            Assert.DoesNotContain("shop_cipher=", text);
            Assert.DoesNotContain(Secret, text);
        }
    }

    // ---- the request hook ----

    [Fact]
    public async Task AuthorizedShopsIsSignedHasTheTokenAndNoShopCipher()
    {
        using var server = new RawServer(_ => RawResponse.Ok("{\"shops\":[]}"));
        var client = NewClient(server.BaseUrl);

        var reply = await client.Authorization.GetAuthorizedShopsAsync();

        Assert.Equal(0, reply.Code);
        var r = server.Single();
        Assert.Equal("GET", r.Method);
        Assert.Equal("/authorization/202309/shops", r.RawPath);
        Assert.Equal("app123", r.Param("app_key"));
        Assert.True(long.TryParse(r.Param("timestamp"), out var ts));
        Assert.InRange(ts, DateTimeOffset.UtcNow.ToUnixTimeSeconds() - 60, DateTimeOffset.UtcNow.ToUnixTimeSeconds() + 60);
        Assert.Null(r.Param("shop_cipher"));
        Assert.Equal("tok", r.Header("x-tts-access-token"));
        AssertSigned(r);
    }

    [Fact]
    public async Task OrderListSendsTheShopCipher()
    {
        using var server = new RawServer(_ => RawResponse.Ok());
        var client = NewClient(server.BaseUrl);

        await client.Orders.GetOrderListAsync(10);

        var r = server.Single();
        Assert.Equal("POST", r.Method);
        Assert.Equal("/order/202309/orders/search", r.RawPath);
        Assert.Equal("cipher", r.Param("shop_cipher"));
        AssertSigned(r);
    }

    [Fact]
    public async Task NoShopCipherIsSentWhenTheClientHasNone()
    {
        using var server = new RawServer(_ => RawResponse.Ok());
        var client = NewClient(server.BaseUrl, cipher: null);

        await client.Orders.GetOrderListAsync(10);

        Assert.Null(server.Single().Param("shop_cipher"));
    }

    [Fact]
    public async Task AGetWithABodySendsTheBodyAndSignsIt()
    {
        using var server = new RawServer(_ => RawResponse.Ok());
        var client = NewClient(server.BaseUrl);

        await client.AffiliateSeller.GetConversationListAsync(
            20,
            getConversationListRequest: new GetConversationListRequest(onlyNeedConversationId: true));

        var r = server.Single();
        Assert.Equal("GET", r.Method);
        Assert.Equal("/affiliate_seller/202412/conversations", r.RawPath);
        Assert.NotEmpty(r.Body);
        // The re-created content kept its Content-Type, so the server and the sign both see application/json.
        Assert.StartsWith("application/json", r.Header("Content-Type"));
        using var json = JsonDocument.Parse(r.Body);
        Assert.True(json.RootElement.GetProperty("only_need_conversation_id").GetBoolean());
        // The sign covers exactly those bytes.
        AssertSigned(r);
        var withoutBody = Signer.Sign(r.RawPath, r.Query.Where(p => p.Key != "sign").ToList(), r.Header("Content-Type"), null, Secret);
        Assert.NotEqual(withoutBody, r.Param("sign"));
    }

    [Fact]
    public async Task APageTokenWithPlusSlashAndEqualsArrivesIntactAndSigned()
    {
        const string token = "b2Zmc2V0PTEw+/x==";
        using var server = new RawServer(_ => RawResponse.Ok());
        var client = NewClient(server.BaseUrl);

        await client.AffiliateSeller.GetConversationListAsync(20, pageToken: token);

        var r = server.Single();
        Assert.Equal(token, r.Param("page_token"));
        Assert.Contains("page_token=b2Zmc2V0PTEw%2B%2Fx%3D%3D", r.RawQuery);
        AssertSigned(r);
    }

    [Fact]
    public async Task ReservedParametersAreReplacedByTheClientsOwn()
    {
        using var server = new RawServer(_ => RawResponse.Ok());
        var creds = new ShopCredentials("app123", Secret, "tok", "cipher");
        using var http = new HttpClient(new SigningHandler(creds, new SocketsHttpHandler { AllowAutoRedirect = false }));

        using var response = await http.PostAsync(
            server.BaseUrl + "/order/202309/orders/search?app_key=evil&sign=x&timestamp=1&shop_cipher=bad&page_size=5",
            new StringContent("{}", Encoding.UTF8, "application/json"));

        Assert.True(response.IsSuccessStatusCode);
        var r = server.Single();
        foreach (var name in new[] { "app_key", "sign", "timestamp", "shop_cipher" })
        {
            Assert.Single(r.Query.Where(p => p.Key == name));
        }
        Assert.Equal("app123", r.Param("app_key"));
        Assert.Equal("cipher", r.Param("shop_cipher"));
        Assert.NotEqual("1", r.Param("timestamp"));
        Assert.NotEqual("x", r.Param("sign"));
        Assert.Equal("5", r.Param("page_size"));
        AssertSigned(r);
    }

    [Fact]
    public async Task AMultipartUploadArrivesIntactAndIsSignedWithoutItsBody()
    {
        using var server = new RawServer(_ => RawResponse.Ok());
        var client = NewClient(server.BaseUrl);
        var bytes = Encoding.ASCII.GetBytes("PNGDATA-unique-marker");

        await client.Products.UploadProductImageAsync(new FileParameter("a.png", "image/png", new MemoryStream(bytes)), "MAIN_IMAGE");

        var r = server.Single();
        Assert.Equal("POST", r.Method);
        var contentType = r.Header("Content-Type")!;
        Assert.StartsWith("multipart/form-data; boundary=", contentType);
        var boundary = contentType[(contentType.IndexOf("boundary=", StringComparison.Ordinal) + "boundary=".Length)..].Trim('"');
        var text = r.BodyText;
        Assert.Contains("--" + boundary, text);
        Assert.EndsWith("--" + boundary + "--\r\n", text);
        Assert.Contains("PNGDATA-unique-marker", text);
        Assert.Contains("a.png", text);
        // Signed as if there were no body.
        var rest = r.Query.Where(p => p.Key != "sign").ToList();
        Assert.Equal(Signer.Sign(r.RawPath, rest, contentType, null, Secret), r.Param("sign"));
    }

    // ---- the response hook ----

    [Fact]
    public async Task ACodeThatIsNotZeroOnHttp200IsATikTokShopException()
    {
        using var server = new RawServer(_ => new RawResponse(200, "{\"code\":36009003,\"message\":\"invalid\",\"request_id\":\"r1\",\"data\":{}}"));
        var client = NewClient(server.BaseUrl);

        var e = await Assert.ThrowsAsync<TikTokShopException>(() => client.Authorization.GetAuthorizedShopsAsync());

        Assert.Equal(36009003, e.Code);
        Assert.Equal("invalid", e.TikTokMessage);
        Assert.Equal("r1", e.RequestId);
        Assert.Equal(200, e.HttpStatus);
    }

    [Fact]
    public void TheSynchronousCallsThrowTheSameException()
    {
        using var server = new RawServer(_ => new RawResponse(200, "{\"code\":7,\"message\":\"nope\",\"request_id\":\"r9\"}"));
        var client = NewClient(server.BaseUrl);

        var e = Assert.Throws<TikTokShopException>(() => client.Authorization.GetAuthorizedShops());

        Assert.Equal(7, e.Code);
        Assert.Equal("r9", e.RequestId);
    }

    [Theory]
    [InlineData(503, "{\"message\":\"x\"}", 503, "x", "")]
    [InlineData(503, "{\"code\":0}", 503, "Service Unavailable", "")]
    [InlineData(503, "this is not json", 503, "Service Unavailable", "")]
    [InlineData(503, "", 503, "Service Unavailable", "")]
    [InlineData(503, "{\"code\":12345,\"message\":\"m\",\"request_id\":\"q\"}", 12345, "m", "q")]
    [InlineData(200, "this is not json", -1, "Response is not a JSON object (HTTP 200)", "")]
    [InlineData(200, "[1,2]", -1, "Response is not a JSON object (HTTP 200)", "")]
    public async Task ErrorCodesFollowR13b(int status, string body, int code, string message, string requestId)
    {
        using var server = new RawServer(_ => new RawResponse(status, body));
        var client = NewClient(server.BaseUrl);

        var e = await Assert.ThrowsAsync<TikTokShopException>(() => client.Authorization.GetAuthorizedShopsAsync());

        Assert.Equal(code, e.Code);
        Assert.Equal(message, e.TikTokMessage);
        Assert.Equal(requestId, e.RequestId);
        Assert.Equal(status, e.HttpStatus);
    }

    [Fact]
    public async Task ARedirectIsNotFollowedAndSurfacesAsCode302()
    {
        using var target = new RawServer(_ => RawResponse.Ok());
        using var server = new RawServer(_ => new RawResponse(302, "", Location: target.BaseUrl + "/elsewhere"));
        var client = NewClient(server.BaseUrl);

        var e = await Assert.ThrowsAsync<TikTokShopException>(() => client.Authorization.GetAuthorizedShopsAsync());

        Assert.Equal(302, e.Code);
        Assert.Equal(302, e.HttpStatus);
        Assert.Empty(target.Requests);
    }

    [Fact]
    public async Task UnknownFieldsAtDataLevelAndInANestedModelWithRequiredPropertiesStillDecode()
    {
        const string reply =
            "{\"code\":0,\"message\":\"Success\",\"request_id\":\"r1\",\"brand_new_top\":1,"
            + "\"data\":{\"new_in_data\":true,"
            + "\"package_dimensions\":{\"height\":1,\"length\":2,\"unit\":\"CENTIMETER\",\"width\":3,\"extra_dim\":\"x\"},"
            + "\"package_weight\":{\"unit\":\"GRAM\",\"value\":\"5\",\"extra_weight\":{\"a\":1}}}}";
        using var server = new RawServer(_ => new RawResponse(200, reply));
        var client = NewClient(server.BaseUrl);

        var result = await client.Products.PredictProductPackageDimensionsAndWeightAsync(
            new PredictProductPackageDimensionsAndWeightRequest(categoryId: "1"));

        Assert.Equal(1, result.Data.PackageDimensions.Height);
        Assert.Equal("GRAM", result.Data.PackageWeight.Unit);
        Assert.True(result.AdditionalProperties.ContainsKey("brand_new_top"));
        Assert.True(result.Data.AdditionalProperties.ContainsKey("new_in_data"));
        Assert.True(result.Data.PackageDimensions.AdditionalProperties.ContainsKey("extra_dim"));
        Assert.True(result.Data.PackageWeight.AdditionalProperties.ContainsKey("extra_weight"));
    }

    // ---- transport failures ----

    [Fact]
    public async Task ARefusedConnectionIsCodeMinusOneWithNoStatusAndNoQuery()
    {
        var client = NewClient($"http://127.0.0.1:{RawServer.FreePort()}");

        var e = await Assert.ThrowsAsync<TikTokShopException>(() => client.Orders.GetOrderListAsync(10));

        Assert.Equal(-1, e.Code);
        Assert.Null(e.HttpStatus);
        Assert.NotNull(e.InnerException);
        AssertNoQueryOrSecret(e);
    }

    [Fact]
    public async Task ATimeoutIsCodeMinusOneWithNoStatusAndNoQuery()
    {
        using var server = new RawServer(_ => null);
        var client = NewClient(server.BaseUrl, timeout: TimeSpan.FromMilliseconds(300));

        var e = await Assert.ThrowsAsync<TikTokShopException>(() => client.Orders.GetOrderListAsync(10));

        Assert.Equal(-1, e.Code);
        Assert.Null(e.HttpStatus);
        Assert.IsType<TimeoutException>(e.InnerException);
        Assert.Contains("timed out", e.Message);
        AssertNoQueryOrSecret(e);
    }

    [Fact]
    public async Task AnHttpClientTimeoutInAUserSuppliedHandlerIsAlsoCodeMinusOne()
    {
        // A user handler that gives up by itself, as HttpClient.Timeout does: a TaskCanceledException the caller did not ask for.
        var handler = new ThrowingHandler(() => new TaskCanceledException("The request was canceled due to the configured HttpClient.Timeout of 1 seconds elapsing."));
        var client = NewClient("http://127.0.0.1:1", handler: handler);

        var e = await Assert.ThrowsAsync<TikTokShopException>(() => client.Orders.GetOrderListAsync(10));

        Assert.Equal(-1, e.Code);
        Assert.Null(e.HttpStatus);
    }

    [Fact]
    public async Task TheCallersCancellationIsNotAFailureOfTheCall()
    {
        using var server = new RawServer(_ => null);
        var client = NewClient(server.BaseUrl);
        using var cts = new CancellationTokenSource(TimeSpan.FromMilliseconds(200));

        await Assert.ThrowsAnyAsync<OperationCanceledException>(() => client.Orders.GetOrderListAsync(10, cancellationToken: cts.Token));
    }

    [Theory]
    [InlineData(0)]
    [InlineData(-1)] // Timeout.InfiniteTimeSpan
    public async Task ZeroAndInfiniteTimeoutsMeanNoLimit(int milliseconds)
    {
        using var server = new RawServer(_ =>
        {
            Thread.Sleep(700);
            return RawResponse.Ok();
        });
        var client = NewClient(server.BaseUrl, timeout: TimeSpan.FromMilliseconds(milliseconds));

        var reply = await client.Orders.GetOrderListAsync(10);

        Assert.Equal(0, reply.Code);
    }

    [Theory]
    [InlineData("{\"code\":99999999999,\"message\":\"big\",\"request_id\":\"q\"}", 99999999999L, "big")]
    [InlineData("{\"code\":-99999999999,\"message\":\"neg\",\"request_id\":\"q\"}", -99999999999L, "neg")]
    [InlineData("{\"code\":\"7\",\"message\":\"odd\",\"request_id\":\"q\"}", -1L, "odd")]
    [InlineData("{\"code\":1.5,\"message\":\"odd\",\"request_id\":\"q\"}", -1L, "odd")]
    public async Task ACodeThatIsOutOfIntRangeOrNotAnIntegerIsAnErrorNotSuccess(string body, long code, string message)
    {
        using var server = new RawServer(_ => new RawResponse(200, body));
        var client = NewClient(server.BaseUrl);

        var e = await Assert.ThrowsAsync<TikTokShopException>(() => client.Authorization.GetAuthorizedShopsAsync());

        Assert.Equal(code, e.Code);
        Assert.Equal(message, e.TikTokMessage);
        Assert.Equal("q", e.RequestId);
        Assert.Equal(200, e.HttpStatus);
    }

    [Theory]
    [InlineData("{\"code\":null,\"message\":\"odd\",\"request_id\":\"q\"}")]
    [InlineData("{\"code\":true,\"message\":\"odd\",\"request_id\":\"q\"}")]
    [InlineData("{\"code\":{},\"message\":\"odd\",\"request_id\":\"q\"}")]
    public async Task ANullOrNonNumericCodeOnA2xxIsMinusOne(string body)
    {
        using var server = new RawServer(_ => new RawResponse(200, body));
        var client = NewClient(server.BaseUrl);

        var e = await Assert.ThrowsAsync<TikTokShopException>(() => client.Authorization.GetAuthorizedShopsAsync());

        Assert.Equal(-1, e.Code);
        Assert.Equal("q", e.RequestId);
        Assert.Equal(200, e.HttpStatus);
    }

    [Fact]
    public async Task A2xxBodyThatDoesNotFitItsModelIsMinusOneWithStatusRequestIdAndInner()
    {
        using var server = new RawServer(_ => new RawResponse(200, "{\"code\":0,\"message\":\"Success\",\"request_id\":\"q9\",\"data\":{\"shops\":\"not a list\"}}"));
        var client = NewClient(server.BaseUrl);

        var e = await Assert.ThrowsAsync<TikTokShopException>(() => client.Authorization.GetAuthorizedShopsAsync());

        Assert.Equal(-1, e.Code);
        Assert.Equal(200, e.HttpStatus);
        Assert.Equal("q9", e.RequestId);
        Assert.NotNull(e.InnerException);
        Assert.IsNotType<ApiException>(e.InnerException);
    }

    [Fact]
    public async Task TheUserAgentIsSentOnApiCalls()
    {
        using var server = new RawServer(_ => new RawResponse(200, "{\"code\":0,\"message\":\"Success\",\"request_id\":\"r\",\"data\":{}}"));

        await NewClient(server.BaseUrl).Authorization.GetAuthorizedShopsAsync();

        Assert.Matches(@"^tiktok-shop-api-csharp/\d+\.\d+\.\d+$", TikTokShopClient.UserAgent);
        Assert.Equal(TikTokShopClient.UserAgent, Assert.Single(server.Requests).Header("User-Agent"));
    }

    [Fact]
    public async Task AnIntegerEnumValueTheSpecDoesNotListStillDecodes()
    {
        using var server = new RawServer(_ => new RawResponse(200, "{\"code\":0,\"request_id\":\"r\",\"data\":{\"creators\":[{\"creator_profile\":{\"user_type_tag\":[1,3]}}]}}"));

        var result = await NewClient(server.BaseUrl).AffiliateSeller.SearchCreatorsInCreatorMarketplaceAsync(1);

        Assert.Equal(new long[] { 1, 3 }, result.Data.Creators[0].CreatorProfile.UserTypeTag);
    }

    [Fact]
    public async Task AHandlerErrorThatPrintsTheSignedUrlIsScrubbedFromTheMessageToStringAndEveryInnerException()
    {
        // Real transports put the request URI, query and all, in their messages. This one prints it, twice.
        string? printed = null;
        var handler = new FailingHandler(request =>
        {
            printed = request.RequestUri!.ToString();
            return new HttpRequestException($"An error occurred sending the request to {request.RequestUri} (again: {printed})",
                new InvalidOperationException($"inner {request.RequestUri}"));
        });
        var client = NewClient("http://127.0.0.1:1", handler: handler);

        var e = await Assert.ThrowsAsync<TikTokShopException>(() => client.Orders.GetOrderListAsync(10));

        Assert.Equal(-1, e.Code);
        Assert.Null(e.HttpStatus);
        // The failing handler really did see a signed URL with a query.
        var query = printed![(printed.IndexOf('?') + 1)..];
        Assert.Contains("sign=", query);
        ErrorAssert.NoneOf(e, new[] { query, "sign=", "app_key=", "timestamp=", "shop_cipher=", Secret });
        Assert.Contains("/order/202309/orders/search", e.Message);
    }

    [Fact]
    public void TheConstructorRejectsNullOptions()
    {
        Assert.Throws<ArgumentNullException>(() => new TikTokShopClient((TikTokShopOptions)null!));
    }

    [Fact]
    public void TheDefaultHandlerRecyclesPooledConnectionsAndNeverFollowsRedirects()
    {
        var client = new TikTokShopClient(new TikTokShopOptions { AppKey = "k", AppSecret = "s" });

        var handler = Assert.IsType<SocketsHttpHandler>(
            typeof(TikTokShopClient).GetField("_handler", System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance)!.GetValue(client));

        Assert.Equal(TimeSpan.FromMinutes(2), handler.PooledConnectionLifetime);
        Assert.False(handler.AllowAutoRedirect);
    }

    // ---- withShop ----

    [Fact]
    public async Task WithShopKeepsReplacesAndClears()
    {
        using var server = new RawServer(_ => RawResponse.Ok());
        var original = NewClient(server.BaseUrl);

        async Task<RecordedRequest> Call(TikTokShopClient c)
        {
            await c.Orders.GetOrderListAsync(10);
            return server.Requests.Last();
        }

        // keep
        var keep = await Call(original.WithShop());
        Assert.Equal("tok", keep.Header("x-tts-access-token"));
        Assert.Equal("cipher", keep.Param("shop_cipher"));

        // replace one, keep the other
        var replaceToken = await Call(original.WithShop(accessToken: "tok2"));
        Assert.Equal("tok2", replaceToken.Header("x-tts-access-token"));
        Assert.Equal("cipher", replaceToken.Param("shop_cipher"));

        var replaceCipher = await Call(original.WithShop(shopCipher: "cipher2"));
        Assert.Equal("tok", replaceCipher.Header("x-tts-access-token"));
        Assert.Equal("cipher2", replaceCipher.Param("shop_cipher"));

        // clear: an explicit null, or an empty string
        var clearCipher = await Call(original.WithShop(shopCipher: new Optional<string?>(null)));
        Assert.Equal("tok", clearCipher.Header("x-tts-access-token"));
        Assert.Null(clearCipher.Param("shop_cipher"));

        var clearToken = await Call(original.WithShop(accessToken: ""));
        Assert.Null(clearToken.Header("x-tts-access-token"));
        Assert.Equal("cipher", clearToken.Param("shop_cipher"));
        AssertSigned(clearToken);

        // the original is untouched
        var again = await Call(original);
        Assert.Equal("tok", again.Header("x-tts-access-token"));
        Assert.Equal("cipher", again.Param("shop_cipher"));
    }

    [Fact]
    public async Task WithShopSharesTheHttpHandler()
    {
        using var server = new RawServer(_ => RawResponse.Ok());
        var counting = new CountingHandler(new SocketsHttpHandler { AllowAutoRedirect = false });
        var original = NewClient(server.BaseUrl, handler: counting);
        var other = original.WithShop(accessToken: "tok2", shopCipher: "cipher2");

        await original.Orders.GetOrderListAsync(10);
        await other.Orders.GetOrderListAsync(10);

        Assert.Equal(2, counting.Count);
        Assert.Equal(new[] { "tok", "tok2" }, server.Requests.Select(r => r.Header("x-tts-access-token")).ToArray());
    }

    // ---- secrets in string forms ----

    [Fact]
    public void StringFormsNeverPrintASecret()
    {
        const string secret = "SECRET-xyz-1";
        const string token = "TOKEN-xyz-2";
        const string cipher = "CIPHER-xyz-3";
        var options = new TikTokShopOptions
        {
            AppKey = "key-visible",
            AppSecret = secret,
            AccessToken = token,
            ShopCipher = cipher,
        };
        var client = new TikTokShopClient(options);
        var credentials = new ShopCredentials("key-visible", secret, token, cipher);

        foreach (var text in new[]
                 {
                     options.ToString(), client.ToString(), credentials.ToString(),
                     client.WithShop(accessToken: "TOKEN-xyz-9").ToString(),
                     $"{options}", $"{client}", $"{credentials}",
                 })
        {
            Assert.DoesNotContain(secret, text);
            Assert.DoesNotContain(token, text);
            Assert.DoesNotContain(cipher, text);
            Assert.DoesNotContain("TOKEN-xyz-9", text);
        }
    }

    private sealed class CountingHandler : DelegatingHandler
    {
        private int _count;

        public CountingHandler(HttpMessageHandler inner) : base(inner)
        {
        }

        public int Count => _count;

        protected override Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
        {
            Interlocked.Increment(ref _count);
            return base.SendAsync(request, cancellationToken);
        }
    }

    private sealed class ThrowingHandler : HttpMessageHandler
    {
        private readonly Func<Exception> _make;

        public ThrowingHandler(Func<Exception> make) => _make = make;

        protected override Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken) =>
            Task.FromException<HttpResponseMessage>(_make());
    }
}
