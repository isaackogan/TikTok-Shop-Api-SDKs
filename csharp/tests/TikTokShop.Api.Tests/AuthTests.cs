using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Text.Json;
using System.Threading;
using System.Threading.Tasks;
using Xunit;

namespace TikTokShop.Api.Tests;

public class AuthTests
{
    private const string AppKey = "123abc";
    private const string AppSecret = "s3cret";
    private const string Code = "CODE123-unique";
    private const string RefreshToken = "TTP_C2XWDN63ON-FOHJSMR0WSG";

    private static readonly JsonElement Vectors = Repo.Json("shared", "test-vectors", "auth.json");

    private static TikTokShopAuth NewAuth(string baseUrl, TimeSpan? timeout = null, HttpMessageHandler? handler = null, string? serviceId = "7123456789") =>
        new(AppKey, AppSecret, serviceId, baseUrl, timeout ?? TimeSpan.FromSeconds(10), handler);

    private static string TokenJson(string dataJson) =>
        "{\"code\":0,\"message\":\"success\",\"request_id\":\"rid\",\"data\":" + dataJson + "}";

    private static string Data(string? access = "\"A\"", string? accessExp = "1", string? refresh = "\"R\"", string? refreshExp = "2", string extra = "")
    {
        var parts = new List<string>();
        if (access is not null) parts.Add("\"access_token\":" + access);
        if (accessExp is not null) parts.Add("\"access_token_expire_in\":" + accessExp);
        if (refresh is not null) parts.Add("\"refresh_token\":" + refresh);
        if (refreshExp is not null) parts.Add("\"refresh_token_expire_in\":" + refreshExp);
        if (extra.Length > 0) parts.Add(extra);
        return "{" + string.Join(",", parts) + "}";
    }

    // ---- authorization URLs ----

    public static IEnumerable<object[]> UrlCases() =>
        Enumerable.Range(0, Vectors.GetProperty("authorizationUrls").GetArrayLength()).Select(i => new object[] { i }).ToList();

    [Theory]
    [MemberData(nameof(UrlCases))]
    public void AuthorizationUrlMatchesTheSharedVectorByteForByte(int index)
    {
        var c = Vectors.GetProperty("authorizationUrls")[index];
        var type = c.GetProperty("type").GetString() switch
        {
            "seller" => AuthorizationType.Seller,
            "partner" => AuthorizationType.Partner,
            _ => AuthorizationType.Creator,
        };
        var region = c.GetProperty("region").GetString() == "us" ? AuthorizationRegion.Us : AuthorizationRegion.Row;
        var auth = new TikTokShopAuth(c.GetProperty("appKey").GetString() ?? "unused", AppSecret, c.GetProperty("serviceId").GetString());

        var url = auth.AuthorizationUrl(type, region, c.GetProperty("state").GetString());

        Assert.Equal(c.GetProperty("url").GetString(), url);
    }

    [Fact]
    public void AnEmptyStateAddsNoStateParameter()
    {
        var auth = new TikTokShopAuth(AppKey, AppSecret, "7123456789");

        Assert.Equal(
            "https://services.tiktokshop.com/open/authorize?service_id=7123456789",
            auth.AuthorizationUrl(AuthorizationType.Seller, AuthorizationRegion.Row, ""));
    }

    [Fact]
    public void ASellerOrPartnerUrlNeedsAServiceId()
    {
        var auth = new TikTokShopAuth(AppKey, AppSecret);

        Assert.Throws<InvalidOperationException>(() => auth.AuthorizationUrl(AuthorizationType.Seller, AuthorizationRegion.Us));
        Assert.Throws<InvalidOperationException>(() => auth.AuthorizationUrl(AuthorizationType.Partner, AuthorizationRegion.Us));
        Assert.Contains("app_key=123abc", auth.AuthorizationUrl(AuthorizationType.Creator, AuthorizationRegion.Us));
    }

    [Fact]
    public void AnUnknownTypeOrRegionIsRejected()
    {
        var auth = new TikTokShopAuth(AppKey, AppSecret, "7123456789");

        Assert.Throws<ArgumentOutOfRangeException>(() => auth.AuthorizationUrl((AuthorizationType)99, AuthorizationRegion.Us));
        Assert.Throws<ArgumentOutOfRangeException>(() => auth.AuthorizationUrl(AuthorizationType.Seller, (AuthorizationRegion)99));
    }

    [Fact]
    public void TheConstructorRejectsNullsAndANegativeTimeout()
    {
        Assert.Throws<ArgumentNullException>(() => new TikTokShopAuth(null!, AppSecret));
        Assert.Throws<ArgumentNullException>(() => new TikTokShopAuth(AppKey, null!));
        Assert.Throws<ArgumentNullException>(() => new TikTokShopAuth((TikTokShopAuthOptions)null!));
        Assert.Throws<ArgumentOutOfRangeException>(() => new TikTokShopAuth(AppKey, AppSecret, timeout: TimeSpan.FromSeconds(-5)));
    }

    // ---- token requests ----

    public static IEnumerable<object[]> TokenRequestCases() =>
        Enumerable.Range(0, Vectors.GetProperty("tokenRequests").GetArrayLength()).Select(i => new object[] { i }).ToList();

    [Theory]
    [MemberData(nameof(TokenRequestCases))]
    public async Task TokenRequestsAreGetsWithTheQueryInThePinnedOrder(int index)
    {
        var c = Vectors.GetProperty("tokenRequests")[index];
        using var server = new RawServer(_ => new RawResponse(200, TokenJson(Data())));
        var auth = new TikTokShopAuth(c.GetProperty("appKey").GetString()!, c.GetProperty("appSecret").GetString()!, baseUrl: server.BaseUrl);
        var value = c.GetProperty("value").GetString()!;

        if (c.GetProperty("kind").GetString() == "exchange")
        {
            await auth.ExchangeCodeAsync(value);
        }
        else
        {
            await auth.RefreshAsync(value);
        }

        var r = server.Single();
        Assert.Equal("GET", r.Method);
        Assert.Empty(r.Body);
        Assert.Equal(new Uri(c.GetProperty("url").GetString()!).PathAndQuery, r.Target);
    }

    [Fact]
    public async Task TokenRequestsPercentEncodeEveryReservedCharacter()
    {
        using var server = new RawServer(_ => new RawResponse(200, TokenJson(Data())));
        var auth = new TikTokShopAuth("k e&y", "p+s/=", baseUrl: server.BaseUrl);

        await auth.ExchangeCodeAsync("a b&c=d+e/f");

        var r = server.Single();
        Assert.Equal("k e&y", r.Param("app_key"));
        Assert.Equal("p+s/=", r.Param("app_secret"));
        Assert.Equal("a b&c=d+e/f", r.Param("auth_code"));
        Assert.Contains("auth_code=a%20b%26c%3Dd%2Be%2Ff&", r.RawQuery);
    }

    [Fact]
    public async Task ABaseUrlWithATrailingSlashIsAccepted()
    {
        using var server = new RawServer(_ => new RawResponse(200, TokenJson(Data())));
        var auth = NewAuth(server.BaseUrl + "/");

        await auth.RefreshAsync(RefreshToken);

        Assert.Equal("/api/v2/token/refresh", server.Single().RawPath);
    }

    [Fact]
    public async Task AnEmptyCodeOrRefreshTokenIsRejectedBeforeAnythingIsSent()
    {
        using var server = new RawServer(_ => new RawResponse(200, TokenJson(Data())));
        var auth = NewAuth(server.BaseUrl);

        await Assert.ThrowsAsync<ArgumentException>(() => auth.ExchangeCodeAsync(""));
        await Assert.ThrowsAsync<ArgumentNullException>(() => auth.RefreshAsync(null!));

        Assert.Empty(server.Requests);
    }

    [Fact]
    public void TheSynchronousCallsWorkToo()
    {
        using var server = new RawServer(_ => new RawResponse(200, TokenJson(Data())));
        var auth = NewAuth(server.BaseUrl);

        Assert.Equal("A", auth.ExchangeCode(Code).AccessToken);
        Assert.Equal("A", auth.Refresh(RefreshToken).AccessToken);
    }

    // ---- token responses ----

    public static IEnumerable<object[]> ResponseCases() =>
        Enumerable.Range(0, Vectors.GetProperty("tokenResponses").GetArrayLength()).Select(i => new object[] { i }).ToList();

    [Theory]
    [MemberData(nameof(ResponseCases))]
    public async Task TokenResponsesMatchTheSharedVectors(int index)
    {
        var c = Vectors.GetProperty("tokenResponses")[index];
        using var server = new RawServer(_ => new RawResponse(200, c.GetProperty("body").GetString()!));
        var auth = NewAuth(server.BaseUrl);

        if (c.GetProperty("errorCode").ValueKind == JsonValueKind.Number)
        {
            var e = await Assert.ThrowsAsync<TikTokShopException>(() => auth.ExchangeCodeAsync(Code));
            Assert.Equal(c.GetProperty("errorCode").GetInt64(), e.Code);
            Assert.Equal("r2", e.RequestId);
            Assert.Equal(200, e.HttpStatus);
            return;
        }

        var t = await auth.ExchangeCodeAsync(Code);
        var x = c.GetProperty("expected");
        Assert.Equal(x.GetProperty("accessToken").GetString(), t.AccessToken);
        Assert.Equal(x.GetProperty("accessTokenExpireIn").GetInt64(), t.AccessTokenExpireIn);
        Assert.Equal(x.GetProperty("refreshToken").GetString(), t.RefreshToken);
        Assert.Equal(x.GetProperty("refreshTokenExpireIn").GetInt64(), t.RefreshTokenExpireIn);
        Assert.Equal(x.GetProperty("openId").GetString(), t.OpenId);
        Assert.Equal(x.GetProperty("sellerName").GetString(), t.SellerName);
        Assert.Equal(x.GetProperty("sellerBaseRegion").GetString(), t.SellerBaseRegion);
        Assert.Equal(x.GetProperty("userType").GetInt32(), t.UserType);
        Assert.Equal(x.GetProperty("grantedScopes").EnumerateArray().Select(s => s.GetString()).ToArray(), t.GrantedScopes);
    }

    [Fact]
    public async Task AMinimalFourFieldResponseSucceeds()
    {
        using var server = new RawServer(_ => new RawResponse(200, TokenJson(Data())));

        var t = await NewAuth(server.BaseUrl).ExchangeCodeAsync(Code);

        Assert.Equal("A", t.AccessToken);
        Assert.Equal(1, t.AccessTokenExpireIn);
        Assert.Equal("R", t.RefreshToken);
        Assert.Equal(2, t.RefreshTokenExpireIn);
        Assert.Null(t.OpenId);
        Assert.Null(t.SellerName);
        Assert.Null(t.SellerBaseRegion);
        Assert.Null(t.UserType);
        Assert.Empty(t.GrantedScopes);
    }

    [Fact]
    public async Task NullOptionalFieldsBecomeNull()
    {
        const string extra = "\"open_id\":null,\"seller_name\":null,\"seller_base_region\":null,\"user_type\":null,\"granted_scopes\":null";
        using var server = new RawServer(_ => new RawResponse(200, TokenJson(Data(extra: extra))));

        var t = await NewAuth(server.BaseUrl).ExchangeCodeAsync(Code);

        Assert.Null(t.OpenId);
        Assert.Null(t.SellerName);
        Assert.Null(t.SellerBaseRegion);
        Assert.Null(t.UserType);
        Assert.Empty(t.GrantedScopes);
    }

    [Theory]
    [InlineData("7494049642642441621", "7494049642642441621")]
    [InlineData("99999999999999999999", "99999999999999999999")] // beyond 64 bits
    [InlineData("\"7010736057180325637\"", "7010736057180325637")]
    public async Task AnOpenIdSentAsANumberKeepsItsExactDigits(string json, string expected)
    {
        using var server = new RawServer(_ => new RawResponse(200, TokenJson(Data(extra: "\"open_id\":" + json))));

        var t = await NewAuth(server.BaseUrl).ExchangeCodeAsync(Code);

        Assert.Equal(expected, t.OpenId);
    }

    [Fact]
    public async Task AnOptionalFieldOfTheWrongTypeIsTreatedAsAbsent()
    {
        const string extra = "\"open_id\":true,\"seller_name\":5,\"seller_base_region\":[],\"user_type\":\"x\",\"granted_scopes\":[\"a\",1,\"b\"]";
        using var server = new RawServer(_ => new RawResponse(200, TokenJson(Data(extra: extra))));

        var t = await NewAuth(server.BaseUrl).ExchangeCodeAsync(Code);

        Assert.Null(t.OpenId);
        Assert.Null(t.SellerName);
        Assert.Null(t.SellerBaseRegion);
        Assert.Null(t.UserType);
        Assert.Equal(new[] { "a", "b" }, t.GrantedScopes);
    }

    public static IEnumerable<object[]> BadRequiredFields() => new[]
    {
        new object[] { Data(access: null) },
        new object[] { Data(access: "null") },
        new object[] { Data(access: "\"\"") },
        new object[] { Data(access: "5") },
        new object[] { Data(access: "true") },
        new object[] { Data(access: "[\"A\"]") },
        new object[] { Data(refresh: null) },
        new object[] { Data(refresh: "null") },
        new object[] { Data(refresh: "\"\"") },
        new object[] { Data(refresh: "7") },
        new object[] { Data(accessExp: null) },
        new object[] { Data(accessExp: "null") },
        new object[] { Data(accessExp: "\"1\"") },
        new object[] { Data(accessExp: "true") },
        new object[] { Data(accessExp: "1.5") },
        new object[] { Data(accessExp: "1.0") },
        new object[] { Data(accessExp: "1e3") },
        new object[] { Data(accessExp: "99999999999999999999") },
        new object[] { Data(refreshExp: null) },
        new object[] { Data(refreshExp: "null") },
        new object[] { Data(refreshExp: "\"2\"") },
        new object[] { Data(refreshExp: "false") },
        new object[] { Data(refreshExp: "2.5") },
    };

    [Theory]
    [MemberData(nameof(BadRequiredFields))]
    public async Task AMissingOrIllTypedRequiredFieldIsCodeMinusOneAndKeepsTheRequestId(string data)
    {
        using var server = new RawServer(_ => new RawResponse(200, TokenJson(data)));

        var e = await Assert.ThrowsAsync<TikTokShopException>(() => NewAuth(server.BaseUrl).ExchangeCodeAsync(Code));

        Assert.Equal(-1, e.Code);
        Assert.Equal("rid", e.RequestId);
        Assert.Equal(200, e.HttpStatus);
    }

    [Fact]
    public async Task ABigExpiryBeyondInt32IsKept()
    {
        using var server = new RawServer(_ => new RawResponse(200, TokenJson(Data(accessExp: "4102444800", refreshExp: "9007199254740993"))));

        var t = await NewAuth(server.BaseUrl).ExchangeCodeAsync(Code);

        Assert.Equal(4102444800L, t.AccessTokenExpireIn);
        Assert.Equal(9007199254740993L, t.RefreshTokenExpireIn);
    }

    // ---- error codes: R13b ----

    [Theory]
    [InlineData(503, "{\"message\":\"x\"}", 503, "x", "")]
    [InlineData(503, "{\"code\":0}", 503, "Service Unavailable", "")]
    [InlineData(503, "this is not json", 503, "Service Unavailable", "")]
    [InlineData(503, "", 503, "Service Unavailable", "")]
    [InlineData(503, "{\"code\":12345,\"message\":\"m\",\"request_id\":\"q\"}", 12345, "m", "q")]
    [InlineData(200, "this is not json", -1, "Token response is not a JSON object (HTTP 200)", "")]
    [InlineData(200, "[1,2]", -1, "Token response is not a JSON object (HTTP 200)", "")]
    [InlineData(200, "{\"code\":0,\"message\":\"ok\",\"request_id\":\"q\"}", -1, "Token response has no data", "q")]
    [InlineData(200, "{\"code\":0,\"message\":\"ok\",\"request_id\":\"q\",\"data\":[]}", -1, "Token response has no data", "q")]
    [InlineData(200, "{\"code\":0,\"message\":\"ok\",\"request_id\":\"q\",\"data\":null}", -1, "Token response has no data", "q")]
    [InlineData(200, "{\"code\":99999999999,\"message\":\"big\",\"request_id\":\"q\"}", 99999999999, "big", "q")]
    [InlineData(200, "{\"code\":\"7\",\"message\":\"odd\",\"request_id\":\"q\"}", -1, "odd", "q")]
    public async Task ErrorCodesFollowR13bOnBothTokenEndpoints(int status, string body, long code, string message, string requestId)
    {
        using var server = new RawServer(_ => new RawResponse(status, body));
        var auth = NewAuth(server.BaseUrl);

        foreach (var call in new Func<Task<TokenSet>>[] { () => auth.ExchangeCodeAsync(Code), () => auth.RefreshAsync(RefreshToken) })
        {
            var e = await Assert.ThrowsAsync<TikTokShopException>(call);

            Assert.Equal(code, e.Code);
            Assert.Equal(message, e.TikTokMessage);
            Assert.Equal(requestId, e.RequestId);
            Assert.Equal(status, e.HttpStatus);
        }
    }

    // ---- redirects: lesson 28 ----

    [Fact]
    public async Task ARedirectIsNotFollowedWithTheDefaultHandler()
    {
        using var target = new RawServer(_ => new RawResponse(200, TokenJson(Data())));
        using var server = new RawServer(_ => new RawResponse(302, "", Location: target.BaseUrl + "/elsewhere"));

        var e = await Assert.ThrowsAsync<TikTokShopException>(() => NewAuth(server.BaseUrl).ExchangeCodeAsync(Code));

        Assert.Equal(302, e.Code);
        Assert.Equal(302, e.HttpStatus);
        Assert.Empty(target.Requests);
        ErrorAssert.NoneOf(e, new[] { AppSecret, Code });
    }

    [Fact]
    public async Task ARedirectIsNotFollowedWithASuppliedHandlerThatDoesNotFollow()
    {
        using var target = new RawServer(_ => new RawResponse(200, TokenJson(Data())));
        using var server = new RawServer(_ => new RawResponse(302, "", Location: target.BaseUrl + "/elsewhere"));
        var handler = new PassThroughHandler(new SocketsHttpHandler { AllowAutoRedirect = false });

        var e = await Assert.ThrowsAsync<TikTokShopException>(() => NewAuth(server.BaseUrl, handler: handler).RefreshAsync(RefreshToken));

        Assert.Equal(302, e.Code);
        Assert.Empty(target.Requests);
    }

    [Fact]
    public void ASuppliedHandlerThatFollowsRedirectsIsRefusedBeforeAnythingIsSent()
    {
        using var target = new RawServer(_ => new RawResponse(200, TokenJson(Data())));
        using var server = new RawServer(_ => new RawResponse(302, "", Location: target.BaseUrl + "/elsewhere"));

        foreach (HttpMessageHandler handler in new HttpMessageHandler[]
                 {
                     new SocketsHttpHandler { AllowAutoRedirect = true },
                     new HttpClientHandler { AllowAutoRedirect = true },
                     new PassThroughHandler(new PassThroughHandler(new SocketsHttpHandler { AllowAutoRedirect = true })),
                 })
        {
            var e = Assert.Throws<ArgumentException>(() => NewAuth(server.BaseUrl, handler: handler));
            Assert.Contains("AllowAutoRedirect", e.Message);
        }

        Assert.Empty(server.Requests);
        Assert.Empty(target.Requests);
    }

    // ---- transport failures: R13c and R15 ----

    private static readonly string[] Forbidden =
    {
        AppSecret, Code, RefreshToken, "app_secret=", "auth_code=", "refresh_token=", "grant_type=", "app_key=",
    };

    private static async Task AssertBothCallsFail(TikTokShopAuth auth, Action<TikTokShopException> check)
    {
        var exchange = await Assert.ThrowsAsync<TikTokShopException>(() => auth.ExchangeCodeAsync(Code));
        var refresh = await Assert.ThrowsAsync<TikTokShopException>(() => auth.RefreshAsync(RefreshToken));
        foreach (var e in new[] { exchange, refresh })
        {
            Assert.Equal(-1, e.Code);
            Assert.Null(e.HttpStatus);
            Assert.NotNull(e.InnerException);
            ErrorAssert.NoneOf(e, Forbidden);
            check(e);
        }
    }

    [Fact]
    public async Task ARefusedConnectionIsCodeMinusOneWithNoSecretAnywhere()
    {
        var auth = NewAuth($"http://127.0.0.1:{RawServer.FreePort()}");

        await AssertBothCallsFail(auth, _ => { });
    }

    [Fact]
    public async Task ATimeoutIsCodeMinusOneWithNoSecretAnywhere()
    {
        using var server = new RawServer(_ => null);
        var auth = NewAuth(server.BaseUrl, timeout: TimeSpan.FromMilliseconds(300));

        await AssertBothCallsFail(auth, e =>
        {
            Assert.IsType<TimeoutException>(e.InnerException);
            Assert.Contains("timed out", e.Message);
        });
    }

    [Fact]
    public async Task AHandlerErrorThatPrintsTheUrlIsScrubbed()
    {
        // Real transports (and wrappers) put the request URI, query and all, in their messages.
        var handler = new FailingHandler(request =>
            new HttpRequestException($"An error occurred sending the request to {request.RequestUri} (and {Uri.EscapeDataString(Code)})"));
        var auth = NewAuth("http://127.0.0.1:1", handler: handler);

        await AssertBothCallsFail(auth, e => Assert.Contains("/api/v2/token/", e.Message));
    }

    [Fact]
    public async Task TheCallersCancellationIsNotAFailureOfTheCall()
    {
        using var server = new RawServer(_ => null);
        using var cts = new CancellationTokenSource(TimeSpan.FromMilliseconds(200));

        await Assert.ThrowsAnyAsync<OperationCanceledException>(() => NewAuth(server.BaseUrl).ExchangeCodeAsync(Code, cts.Token));
    }

    [Theory]
    [InlineData(0)]
    [InlineData(-1)] // Timeout.InfiniteTimeSpan
    public async Task ZeroAndInfiniteTimeoutsMeanNoLimit(int milliseconds)
    {
        using var server = new RawServer(_ =>
        {
            Thread.Sleep(700);
            return new RawResponse(200, TokenJson(Data()));
        });

        var t = await NewAuth(server.BaseUrl, timeout: TimeSpan.FromMilliseconds(milliseconds)).ExchangeCodeAsync(Code);

        Assert.Equal("A", t.AccessToken);
    }

    // ---- secrets in string forms; TokenSet stays serializable ----

    [Fact]
    public void TheAuthOptionsAndTheAuthObjectNeverPrintASecret()
    {
        var options = new TikTokShopAuthOptions { AppKey = "key-visible", AppSecret = "SECRET-xyz-1", ServiceId = "svc" };
        var auth = new TikTokShopAuth(options);

        foreach (var text in new[] { options.ToString(), $"{options}", auth.ToString(), $"{auth}" })
        {
            Assert.DoesNotContain("SECRET-xyz-1", text);
            Assert.Contains("key-visible", text);
        }
    }

    private static TokenSet SampleTokens() => new(
        "ACCESS-xyz-1", 1660556783, "REFRESH-xyz-2", 1691487031, "7010736057180325637", "Test Seller", "US", 0, new[] { "a.read", "b.write" });

    [Fact]
    public void ATokenSetNeverPrintsATokenInAnyStringForm()
    {
        var t = SampleTokens();

        foreach (var text in new[] { t.ToString(), $"{t}", string.Format("{0}", t), (t with { OpenId = "1" }).ToString() })
        {
            Assert.DoesNotContain("ACCESS-xyz-1", text);
            Assert.DoesNotContain("REFRESH-xyz-2", text);
        }
    }

    [Fact]
    public void ATokenSetRoundTripsThroughSystemTextJsonWithTheRealValues()
    {
        var t = SampleTokens();

        var json = JsonSerializer.Serialize(t);
        Assert.Contains("ACCESS-xyz-1", json);
        Assert.Contains("REFRESH-xyz-2", json);
        var back = JsonSerializer.Deserialize<TokenSet>(json)!;

        Assert.Equal(t.AccessToken, back.AccessToken);
        Assert.Equal(t.RefreshToken, back.RefreshToken);
        Assert.Equal(t.AccessTokenExpireIn, back.AccessTokenExpireIn);
        Assert.Equal(t.RefreshTokenExpireIn, back.RefreshTokenExpireIn);
        Assert.Equal(t.OpenId, back.OpenId);
        Assert.Equal(t.UserType, back.UserType);
        Assert.Equal(t.GrantedScopes, back.GrantedScopes);
    }

    [Fact]
    public void ATokenSetRoundTripsThroughNewtonsoftWithTheRealValues()
    {
        var t = SampleTokens();

        var json = Newtonsoft.Json.JsonConvert.SerializeObject(t);
        Assert.Contains("ACCESS-xyz-1", json);
        Assert.Contains("REFRESH-xyz-2", json);
        var back = Newtonsoft.Json.JsonConvert.DeserializeObject<TokenSet>(json)!;

        Assert.Equal(t.AccessToken, back.AccessToken);
        Assert.Equal(t.RefreshToken, back.RefreshToken);
        Assert.Equal(t.AccessTokenExpireIn, back.AccessTokenExpireIn);
        Assert.Equal(t.OpenId, back.OpenId);
        Assert.Equal(t.GrantedScopes, back.GrantedScopes);
    }
}
