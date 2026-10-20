package com.isaackogan.tiktok.shop;

import static com.isaackogan.tiktok.shop.StubSupport.OK;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertInstanceOf;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import com.isaackogan.tiktok.shop.generated.model.GetAuthorizedShopsResponse;
import com.isaackogan.tiktok.shop.generated.model.GetConversationListRequest;
import com.isaackogan.tiktok.shop.generated.model.GetOrderListResponse;
import java.io.File;
import java.io.IOException;
import java.net.ServerSocket;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.time.Duration;
import java.util.concurrent.TimeUnit;
import okhttp3.HttpUrl;
import okhttp3.OkHttpClient;
import okhttp3.mockwebserver.MockResponse;
import okhttp3.mockwebserver.MockWebServer;
import okhttp3.mockwebserver.RecordedRequest;
import okhttp3.mockwebserver.SocketPolicy;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class ClientStubTest {
    static final String SECRET = "s3cret";
    MockWebServer server;

    @BeforeEach
    void start() throws IOException {
        server = new MockWebServer();
        server.start();
    }

    @AfterEach
    void stop() throws IOException {
        server.shutdown();
    }

    TikTokShop.Builder builder() {
        return TikTokShop.builder().appKey("key1").appSecret(SECRET).accessToken("tok1").shopCipher("cipher1")
                .baseUrl(server.url("/").toString());
    }

    RecordedRequest take() throws InterruptedException {
        RecordedRequest r = server.takeRequest(5, TimeUnit.SECONDS);
        assertNotNull(r, "no request arrived");
        return r;
    }

    void reply(String body) {
        server.enqueue(new MockResponse().setHeader("Content-Type", "application/json").setBody(body));
    }

    @Test
    void getAuthorizedShopsIsSignedWithTokenAndNoShopCipher() throws Exception {
        reply("{\"code\":0,\"message\":\"Success\",\"request_id\":\"r1\",\"data\":{\"shops\":[{\"id\":\"1\",\"name\":\"n\"}]}}");
        GetAuthorizedShopsResponse resp = builder().build().authorization().getAuthorizedShops();
        assertEquals("1", resp.getData().getShops().get(0).getId());

        RecordedRequest r = take();
        assertEquals("GET", r.getMethod());
        assertEquals("/authorization/202309/shops", r.getRequestUrl().encodedPath());
        assertEquals("key1", StubSupport.only(r, "app_key"));
        assertTrue(Long.parseLong(StubSupport.only(r, "timestamp")) > 1_600_000_000L);
        assertFalse(StubSupport.queryMap(r).containsKey("shop_cipher"));
        assertEquals("tok1", r.getHeader("x-tts-access-token"));
        StubSupport.assertSigned(r, SECRET);
    }

    @Test
    void getOrderListSendsShopCipher() throws Exception {
        reply(OK);
        GetOrderListResponse resp = builder().build().orders().getOrderList(20L, null, null, null, null);
        assertEquals(0L, resp.getCode());
        RecordedRequest r = take();
        assertEquals("cipher1", StubSupport.only(r, "shop_cipher"));
        assertEquals("20", StubSupport.only(r, "page_size"));
        StubSupport.assertSigned(r, SECRET);
    }

    @Test
    void aStatusValueTheSpecDoesNotListIsKept() throws Exception {
        reply("{\"code\":0,\"message\":\"ok\",\"request_id\":\"r\",\"data\":{\"orders\":[{\"id\":\"1\",\"status\":\"SOME_NEW_STATUS\"}]}}");
        GetOrderListResponse resp = builder().build().orders().getOrderList(1L, null, null, null, null);
        assertEquals("SOME_NEW_STATUS", resp.getData().getOrders().get(0).getStatus());
    }

    @Test
    void noTokenAndNoCipherSendsNeither() throws Exception {
        reply(OK);
        TikTokShop.builder().appKey("key1").appSecret(SECRET).baseUrl(server.url("/").toString()).build()
                .orders().getOrderList(1L, null, null, null, null);
        RecordedRequest r = take();
        assertNull(r.getHeader("x-tts-access-token"));
        assertFalse(StubSupport.queryMap(r).containsKey("shop_cipher"));
        StubSupport.assertSigned(r, SECRET);
    }

    @Test
    void pageTokenWithPlusSlashEqualsRoundTrips() throws Exception {
        reply(OK);
        String token = "b2Zmc2V0PTEw+/x==";
        builder().build().orders().getOrderList(10L, null, token, null, null);
        RecordedRequest r = take();
        assertEquals(token, StubSupport.only(r, "page_token"), "decoded value arrives intact");
        assertTrue(r.getPath().contains("page_token=b2Zmc2V0PTEw%2B%2Fx%3D%3D"), r.getPath());
        StubSupport.assertSigned(r, SECRET);
    }

    @Test
    void getWithBodyIsSentAndSigned() throws Exception {
        try (RawServer raw = new RawServer()) {
            GetConversationListRequest body = new GetConversationListRequest().onlyNeedConversationId(true);
            TikTokShop.builder().appKey("key1").appSecret(SECRET).accessToken("tok1").shopCipher("cipher1").baseUrl(raw.baseUrl())
                    .build().affiliateSeller().getConversationList(10L, "p+/=", null, null, body);
            RawServer.Received r = raw.take();
            assertEquals("GET", r.method);
            assertEquals("{\"only_need_conversation_id\":true}", new String(r.body, StandardCharsets.UTF_8));
            assertEquals("p+/=", StubSupport.only(r.url(), "page_token"));
            assertEquals("cipher1", StubSupport.only(r.url(), "shop_cipher"));
            assertEquals("tok1", r.headers.get("x-tts-access-token"));
            assertTrue(r.headers.get("content-type").startsWith("application/json"));
            StubSupport.assertSigned(r, SECRET);
            // the signature covers the body: a signature over no body differs
            String noBody = Signer.sign(new Signer.Request(r.url().encodedPath(), StubSupport.query(r.url()), null, null, SECRET));
            assertTrue(!noBody.equals(StubSupport.only(r.url(), "sign")));
        }
    }

    @Test
    void theGeneratedClientAloneDropsTheGetBody() throws Exception {
        // Why TikTokApiClient exists: the stock generated ApiClient sends no body with a GET.
        reply(OK);
        com.isaackogan.tiktok.shop.generated.ApiClient stock = new com.isaackogan.tiktok.shop.generated.ApiClient();
        stock.setBasePath(server.url("/").toString().replaceAll("/$", ""));
        new com.isaackogan.tiktok.shop.generated.api.AffiliateSellerApi(stock).getConversationList(10L, null, null, null,
                new GetConversationListRequest().onlyNeedConversationId(true));
        assertEquals(0, take().getBodySize());
    }

    @Test
    void getWithBodyFailuresBecomeTheSameException() throws Exception {
        GetConversationListRequest body = new GetConversationListRequest().onlyNeedConversationId(true);
        try (RawServer raw = new RawServer()) {
            raw.respond(500, "{\"code\":77,\"message\":\"bad\",\"request_id\":\"rq\"}");
            TikTokShopException e = assertThrows(TikTokShopException.class, () -> TikTokShop.builder().appKey("key1").appSecret(SECRET)
                    .baseUrl(raw.baseUrl()).build().affiliateSeller().getConversationList(10L, null, null, null, body));
            assertEquals(77, e.getCode());
            assertEquals("rq", e.getRequestId());
            assertEquals(Integer.valueOf(500), e.getHttpStatus());

            raw.respond(200, "{\"code\":5,\"message\":\"nope\",\"request_id\":\"r2\"}");
            assertEquals(5, assertThrows(TikTokShopException.class, () -> TikTokShop.builder().appKey("key1").appSecret(SECRET)
                    .baseUrl(raw.baseUrl()).build().affiliateSeller().getConversationList(10L, null, null, null, body)).getCode());
        }
        try (RawServer raw = new RawServer().hang()) {
            TikTokShopException t = assertThrows(TikTokShopException.class, () -> TikTokShop.builder().appKey("key1").appSecret(SECRET)
                    .baseUrl(raw.baseUrl()).timeout(Duration.ofMillis(300)).build().affiliateSeller()
                    .getConversationList(10L, null, null, null, body));
            assertInstanceOf(IOException.class, t.getCause());
            assertFalse(t.getMessage().contains("?"), t.getMessage());
        }
    }

    @Test
    void codeNotZeroRaisesWithCodeMessageAndRequestId() {
        reply("{\"code\":36009003,\"message\":\"invalid\",\"request_id\":\"r1\",\"data\":{}}");
        TikTokShopException e = assertThrows(TikTokShopException.class, () -> builder().build().authorization().getAuthorizedShops());
        assertEquals(36009003, e.getCode());
        assertEquals("invalid", e.getMessage());
        assertEquals("r1", e.getRequestId());
        assertEquals(Integer.valueOf(200), e.getHttpStatus());
    }

    @Test
    void non2xxRaisesWithStatusAndBodyFields() {
        server.enqueue(new MockResponse().setResponseCode(503).setBody("{\"code\":99,\"message\":\"down\",\"request_id\":\"r5\"}"));
        TikTokShopException e = assertThrows(TikTokShopException.class, () -> builder().build().authorization().getAuthorizedShops());
        assertEquals(99, e.getCode());
        assertEquals("down", e.getMessage());
        assertEquals("r5", e.getRequestId());
        assertEquals(Integer.valueOf(503), e.getHttpStatus());

        server.enqueue(new MockResponse().setResponseCode(502).setBody("<html>bad gateway</html>"));
        TikTokShopException h = assertThrows(TikTokShopException.class, () -> builder().build().authorization().getAuthorizedShops());
        assertEquals(502, h.getCode());
        assertEquals(Integer.valueOf(502), h.getHttpStatus());
    }

    @Test
    void non2xxHtmlBodyWithNoCodeStillRaises() {
        server.enqueue(new MockResponse().setResponseCode(404).setBody("not json at all"));
        TikTokShopException e = assertThrows(TikTokShopException.class, () -> builder().build().authorization().getAuthorizedShops());
        assertEquals(Integer.valueOf(404), e.getHttpStatus());
    }

    @Test
    void nonJson2xxRaises() {
        server.enqueue(new MockResponse().setBody("<html>hello</html>"));
        TikTokShopException e = assertThrows(TikTokShopException.class, () -> builder().build().authorization().getAuthorizedShops());
        assertEquals(Integer.valueOf(200), e.getHttpStatus());
        assertTrue(e.getMessage().contains("not valid JSON"), e.getMessage());
    }

    @Test
    void closedPortRaisesWithIoCauseAndNoQueryInMessage() throws IOException {
        int port;
        try (ServerSocket s = new ServerSocket(0)) {
            port = s.getLocalPort();
        }
        TikTokShop client = TikTokShop.builder().appKey("key1").appSecret(SECRET).accessToken("tok1")
                .baseUrl("http://127.0.0.1:" + port).build();
        TikTokShopException e = assertThrows(TikTokShopException.class, () -> client.authorization().getAuthorizedShops());
        assertInstanceOf(IOException.class, e.getCause());
        assertFalse(e.getMessage().contains("?") || e.getMessage().contains("sign="), e.getMessage());
    }

    @Test
    void timeoutRaisesWithIoCause() {
        server.enqueue(new MockResponse().setSocketPolicy(SocketPolicy.NO_RESPONSE));
        TikTokShop client = builder().timeout(Duration.ofMillis(300)).build();
        long start = System.nanoTime();
        TikTokShopException e = assertThrows(TikTokShopException.class, () -> client.authorization().getAuthorizedShops());
        assertInstanceOf(IOException.class, e.getCause());
        assertTrue(Duration.ofNanos(System.nanoTime() - start).toSeconds() < 10);
        assertFalse(e.getMessage().contains("?") || e.getMessage().contains("sign="), e.getMessage());
    }

    @Test
    void reservedParamsOnTheOutgoingRequestAreReplacedByTheClientsValues() throws Exception {
        reply(OK);
        OkHttpClient injecting = new OkHttpClient.Builder().addInterceptor(chain -> {
            HttpUrl evil = chain.request().url().newBuilder()
                    .addQueryParameter("app_key", "evil").addQueryParameter("sign", "x")
                    .addQueryParameter("timestamp", "1").addQueryParameter("shop_cipher", "bad").build();
            return chain.proceed(chain.request().newBuilder().url(evil).build());
        }).build();
        builder().httpClient(injecting).build().orders().getOrderList(5L, null, null, null, null);
        RecordedRequest r = take();
        assertEquals("key1", StubSupport.only(r, "app_key"));
        assertEquals("cipher1", StubSupport.only(r, "shop_cipher"));
        assertNotNull(StubSupport.only(r, "sign"));
        assertTrue(!"x".equals(StubSupport.only(r, "sign")));
        assertTrue(!"1".equals(StubSupport.only(r, "timestamp")));
        assertEquals("5", StubSupport.only(r, "page_size"));
        StubSupport.assertSigned(r, SECRET);
    }

    @Test
    void multipartUploadIsSignedWithoutItsBody() throws Exception {
        reply("{\"code\":0,\"message\":\"ok\",\"request_id\":\"r\",\"data\":{\"uri\":\"u\"}}");
        File f = File.createTempFile("img", ".png");
        f.deleteOnExit();
        byte[] content = "FAKE-PNG-BYTES-\u0001\u0002".getBytes(StandardCharsets.UTF_8);
        Files.write(f.toPath(), content);

        builder().build().products().uploadProductImage(f, "MAIN_IMAGE");
        RecordedRequest r = take();
        assertEquals("POST", r.getMethod());
        String ct = r.getHeader("Content-Type");
        assertTrue(ct.startsWith("multipart/form-data; boundary="), ct);
        String boundary = ct.substring(ct.indexOf("boundary=") + 9);
        String body = r.getBody().readString(StandardCharsets.UTF_8);
        assertTrue(body.startsWith("--" + boundary), "multipart body intact");
        assertTrue(body.contains("FAKE-PNG-BYTES-"));
        assertTrue(body.trim().endsWith("--" + boundary + "--"));
        // signed as if there were no body, whatever the boundary
        String expected = Signer.sign(new Signer.Request(r.getRequestUrl().encodedPath(), StubSupport.query(r), ct, null, SECRET));
        assertEquals(expected, StubSupport.only(r, "sign"));
        String withBodySign = Signer.sign(new Signer.Request(r.getRequestUrl().encodedPath(), StubSupport.query(r), "application/json",
                body.getBytes(StandardCharsets.UTF_8), SECRET));
        assertTrue(!withBodySign.equals(expected));
    }

    @Test
    void unknownFieldsAreAcceptedAtDataLevelAndInsideNestedModels() throws Exception {
        reply("{\"code\":0,\"message\":\"ok\",\"request_id\":\"r\",\"brand_new\":1,"
                + "\"data\":{\"extra_data\":{\"a\":[1]},\"shops\":[{\"id\":\"9\",\"name\":\"n\",\"region\":\"US\",\"shiny\":true}]}}");
        GetAuthorizedShopsResponse resp = builder().build().authorization().getAuthorizedShops();
        assertEquals("9", resp.getData().getShops().get(0).getId());

        reply("{\"code\":0,\"message\":\"ok\",\"request_id\":\"r\",\"data\":{\"next_page_token\":\"t\",\"zzz\":\"new\","
                + "\"orders\":[{\"id\":\"1\",\"unknown_nested\":{\"x\":1},\"line_items\":[{\"id\":\"2\",\"nope\":1}]}]}}");
        GetOrderListResponse orders = builder().build().orders().getOrderList(1L, null, null, null, null);
        assertEquals("t", orders.getData().getNextPageToken());
        assertEquals("1", orders.getData().getOrders().get(0).getId());
    }

    @Test
    void unknownFieldsInNestedModelsWithRequiredPropertiesStillDecode() throws Exception {
        // PackageDimension requires height, length, unit, width; PackageWeight requires unit, value.
        reply("{\"code\":0,\"message\":\"ok\",\"request_id\":\"r\",\"data\":{\"surprise\":1,"
                + "\"package_dimensions\":{\"height\":3,\"length\":4,\"width\":5,\"unit\":\"CENTIMETER\",\"new_field\":{\"a\":1}},"
                + "\"package_weight\":{\"value\":\"1.5\",\"unit\":\"KILOGRAM\",\"another\":[1,2]}}}");
        com.isaackogan.tiktok.shop.generated.model.PredictProductPackageDimensionsAndWeightResponse resp = builder().build().products()
                .predictProductPackageDimensionsAndWeight(
                        new com.isaackogan.tiktok.shop.generated.model.PredictProductPackageDimensionsAndWeightRequest());
        com.isaackogan.tiktok.shop.generated.model.PredictProductPackageDimensionsAndWeightResponseDataPackageDimension d =
                resp.getData().getPackageDimensions();
        assertEquals(3L, d.getHeight());
        assertEquals(4L, d.getLength());
        assertEquals(5L, d.getWidth());
        assertEquals("CENTIMETER", d.getUnit());
        assertEquals("1.5", resp.getData().getPackageWeight().getValue());
        assertEquals("KILOGRAM", resp.getData().getPackageWeight().getUnit());
    }

    @Test
    void getWithBodyTimeoutBoundsASlowDrippedBody() throws Exception {
        try (RawServer raw = new RawServer().drip()) {
            long start = System.nanoTime();
            TikTokShopException e = assertThrows(TikTokShopException.class, () -> TikTokShop.builder().appKey("key1").appSecret(SECRET)
                    .baseUrl(raw.baseUrl()).timeout(Duration.ofMillis(700)).build().affiliateSeller()
                    .getConversationList(10L, null, null, null, new GetConversationListRequest().onlyNeedConversationId(true)));
            assertInstanceOf(IOException.class, e.getCause());
            assertTrue(Duration.ofNanos(System.nanoTime() - start).toSeconds() < 10);
        }
    }

    @Test
    void getWithBodyHonoursAnExplicitHttpProxy() throws Exception {
        try (RawServer proxy = new RawServer()) {
            int port = Integer.parseInt(proxy.baseUrl().substring(proxy.baseUrl().lastIndexOf(':') + 1));
            OkHttpClient viaProxy = new OkHttpClient.Builder()
                    .proxy(new java.net.Proxy(java.net.Proxy.Type.HTTP, new java.net.InetSocketAddress("127.0.0.1", port))).build();
            TikTokShop client = TikTokShop.builder().appKey("key1").appSecret(SECRET).baseUrl("http://target.invalid")
                    .httpClient(viaProxy).build();
            assertEquals(java.net.Proxy.Type.HTTP,
                    client.jdkClient().proxy().get().select(java.net.URI.create("http://target.invalid")).get(0).type());
            client.affiliateSeller().getConversationList(10L, null, null, null, new GetConversationListRequest().onlyNeedConversationId(true));
            RawServer.Received r = proxy.take();
            assertTrue(r.target.startsWith("http://target.invalid/"), r.target);
            assertEquals("{\"only_need_conversation_id\":true}", new String(r.body, StandardCharsets.UTF_8));
        }
    }

    private static GetConversationListRequest onlyIds() {
        return new GetConversationListRequest().onlyNeedConversationId(true);
    }

    @Test
    void zeroOkHttpTimeoutsMeanNoLimitOnTheGetWithBodyPath() throws Exception {
        try (RawServer raw = new RawServer()) {
            OkHttpClient noLimits = new OkHttpClient.Builder().connectTimeout(Duration.ZERO).readTimeout(Duration.ZERO)
                    .callTimeout(Duration.ZERO).build();
            TikTokShop.builder().appKey("key1").appSecret(SECRET).baseUrl(raw.baseUrl()).httpClient(noLimits).build()
                    .affiliateSeller().getConversationList(10L, null, null, null, onlyIds());
            assertEquals("GET", raw.take().method);
        }
    }

    @Test
    void zeroReadAndCallTimeoutsWithADefaultConnectTimeoutStillComplete() throws Exception {
        try (RawServer raw = new RawServer()) {
            OkHttpClient c = new OkHttpClient.Builder().readTimeout(Duration.ZERO).callTimeout(Duration.ZERO).build();
            TikTokShop.builder().appKey("key1").appSecret(SECRET).baseUrl(raw.baseUrl()).httpClient(c).build()
                    .affiliateSeller().getConversationList(10L, null, null, null, onlyIds());
            assertEquals("GET", raw.take().method);
        }
    }

    @Test
    void anExplicitDirectProxyMeansNoProxyForTheJdkClientAndSocksIsRefused() {
        TikTokShop c = TikTokShop.builder().appKey("k").appSecret("s")
                .httpClient(new OkHttpClient.Builder().proxy(java.net.Proxy.NO_PROXY).build()).build();
        assertEquals(java.net.Proxy.Type.DIRECT,
                c.jdkClient().proxy().get().select(java.net.URI.create("http://example.com")).get(0).type());
        TikTokShop socks = TikTokShop.builder().appKey("k").appSecret("s").httpClient(new OkHttpClient.Builder()
                .proxy(new java.net.Proxy(java.net.Proxy.Type.SOCKS, new java.net.InetSocketAddress("127.0.0.1", 9))).build()).build();
        assertEquals(-1, assertThrows(TikTokShopException.class, socks::jdkClient).getCode());
    }

    @Test
    void theJdkClientIsOnlyBuiltByAGetWithBody() throws Exception {
        try (RawServer raw = new RawServer()) {
            reply(StubSupport.OK);
            TikTokShop c = builder().build();
            assertFalse(c.jdkClientBuilt(), "built with the client");
            c.authorization().getAuthorizedShops();
            assertFalse(c.jdkClientBuilt(), "built by an ordinary call");
            assertFalse(c.withShop("t2", "c2").jdkClientBuilt(), "built by withShop");
            TikTokShop g = TikTokShop.builder().appKey("key1").appSecret(SECRET).baseUrl(raw.baseUrl()).build();
            g.affiliateSeller().getConversationList(10L, null, null, null, onlyIds());
            assertTrue(g.jdkClientBuilt(), "not built by a GET with a body");
        }
    }

    @Test
    void aRedirectIsNotFollowedAndSurfacesAsTheErrorWithItsStatus() throws Exception {
        try (MockWebServer target = new MockWebServer()) {
            target.start();
            server.enqueue(new MockResponse().setResponseCode(302).setHeader("Location", target.url("/stolen").toString()));
            TikTokShopException e = assertThrows(TikTokShopException.class, () -> builder().build().authorization().getAuthorizedShops());
            assertEquals(302, e.getCode());
            assertEquals(Integer.valueOf(302), e.getHttpStatus());
            assertEquals(0, target.getRequestCount(), "the redirect target got a request");
        }
    }

    @Test
    void aRedirectOnTheGetWithBodyPathIsNotFollowedEither() throws Exception {
        try (MockWebServer target = new MockWebServer(); RawServer raw = new RawServer()) {
            target.start();
            raw.respond(302, "").location(target.url("/stolen").toString());
            TikTokShopException e = assertThrows(TikTokShopException.class, () -> TikTokShop.builder().appKey("key1").appSecret(SECRET)
                    .accessToken("tok1").baseUrl(raw.baseUrl()).build().affiliateSeller().getConversationList(10L, null, null, null, onlyIds()));
            assertEquals(302, e.getCode());
            assertEquals(Integer.valueOf(302), e.getHttpStatus());
            assertEquals(0, target.getRequestCount());
        }
    }

    @Test
    void aSuppliedHttpClientIsUsedAsIsSoItsRedirectPolicyApplies() throws Exception {
        try (MockWebServer target = new MockWebServer()) {
            target.start();
            target.enqueue(new MockResponse().setHeader("Content-Type", "application/json").setBody(OK));
            server.enqueue(new MockResponse().setResponseCode(302).setHeader("Location", target.url("/followed").toString()));
            builder().httpClient(new OkHttpClient.Builder().followRedirects(true).build()).build().authorization().getAuthorizedShops();
            assertEquals(1, target.getRequestCount());
        }
    }

    @Test
    void non2xxWithCodeZeroOrNoCodeUsesTheHttpStatusAsTheCode() {
        for (String body : new String[] {"{\"message\":\"x\"}", "{\"code\":0}"}) {
            server.enqueue(new MockResponse().setResponseCode(503).setBody(body));
            TikTokShopException e = assertThrows(TikTokShopException.class, () -> builder().build().authorization().getAuthorizedShops());
            assertEquals(503, e.getCode(), body);
            assertEquals(Integer.valueOf(503), e.getHttpStatus(), body);
        }
    }

    /** R13b: non-2xx -> TikTok's non-zero code else the HTTP status; an unreadable 2xx -> -1. */
    @Test
    void r13bApiCodes() {
        Object[][] cases = {
            {503, "{\"message\":\"x\"}", 503}, {503, "{\"code\":0}", 503}, {503, "down", 503}, {503, "", 503}, {503, "[1]", 503},
            {302, "", 302}, {503, "{\"code\":12345,\"message\":\"m\"}", 12345}, {200, "<html>", -1}, {200, "[1]", -1},
        };
        for (Object[] c : cases) {
            server.enqueue(new MockResponse().setResponseCode((Integer) c[0]).setBody((String) c[1]));
            TikTokShopException e = assertThrows(TikTokShopException.class, () -> builder().build().authorization().getAuthorizedShops());
            assertEquals((Integer) c[2], e.getCode(), c[0] + " " + c[1]);
            assertEquals(c[0], e.getHttpStatus(), c[0] + " " + c[1]);
        }
    }
}
