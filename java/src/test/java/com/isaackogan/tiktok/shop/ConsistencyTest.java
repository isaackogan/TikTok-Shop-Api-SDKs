package com.isaackogan.tiktok.shop;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertInstanceOf;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import com.isaackogan.tiktok.shop.generated.ApiCallback;
import com.isaackogan.tiktok.shop.generated.ApiException;
import com.isaackogan.tiktok.shop.generated.model.GetAuthorizedShopsResponse;
import com.isaackogan.tiktok.shop.generated.model.GetConversationListRequest;
import com.isaackogan.tiktok.shop.generated.model.PredictProductPackageDimensionsAndWeightRequest;
import com.isaackogan.tiktok.shop.generated.model.SearchCreatorsInCreatorMarketplaceResponse;
import java.io.IOException;
import java.net.ServerSocket;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicReference;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import okhttp3.OkHttpClient;
import okhttp3.mockwebserver.MockResponse;
import okhttp3.mockwebserver.MockWebServer;
import okhttp3.mockwebserver.RecordedRequest;
import okhttp3.mockwebserver.SocketPolicy;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

/** Cross-language rules from the final review: R13c, R13d, lesson 34, I6 and M22. */
class ConsistencyTest {
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
        return TikTokShop.builder().appKey("k").appSecret("s").accessToken("t").baseUrl(server.url("/").toString());
    }

    TikTokShopAuth auth() {
        return TikTokShopAuth.builder().appKey("k").appSecret("s").baseUrl(server.url("/").toString()).build();
    }

    void reply(String body) {
        server.enqueue(new MockResponse().setHeader("Content-Type", "application/json").setBody(body));
    }

    static String closedPort() throws IOException {
        try (ServerSocket s = new ServerSocket(0)) {
            return "http://127.0.0.1:" + s.getLocalPort();
        }
    }

    static void assertTransportFailure(TikTokShopException e) {
        assertEquals(-1, e.getCode(), e.toString());
        assertNull(e.getHttpStatus());
        assertInstanceOf(IOException.class, e.getCause());
    }

    static GetConversationListRequest onlyIds() {
        return new GetConversationListRequest().onlyNeedConversationId(true);
    }

    // --- R13c ---------------------------------------------------------------------------------------------------------

    @Test
    void anApiCallToAClosedPortIsMinusOneWithNoStatus() throws IOException {
        TikTokShop c = TikTokShop.builder().appKey("k").appSecret("s").baseUrl(closedPort()).build();
        assertTransportFailure(assertThrows(TikTokShopException.class, () -> c.authorization().getAuthorizedShops()));
        assertTransportFailure(assertThrows(TikTokShopException.class,
                () -> c.affiliateSeller().getConversationList(10L, null, null, null, onlyIds())));
    }

    @Test
    void anApiCallTimeoutIsMinusOneWithNoStatus() {
        server.enqueue(new MockResponse().setSocketPolicy(SocketPolicy.NO_RESPONSE));
        TikTokShop c = builder().timeout(Duration.ofMillis(300)).build();
        assertTransportFailure(assertThrows(TikTokShopException.class, () -> c.authorization().getAuthorizedShops()));
    }

    @Test
    void aTokenCallTimeoutIsMinusOneWithNoStatus() {
        server.enqueue(new MockResponse().setSocketPolicy(SocketPolicy.NO_RESPONSE));
        TikTokShopAuth a = TikTokShopAuth.builder().appKey("k").appSecret("s").baseUrl(server.url("/").toString())
                .timeout(Duration.ofMillis(300)).build();
        assertTransportFailure(assertThrows(TikTokShopException.class, () -> a.exchangeCode("c")));
    }

    // --- R13d ---------------------------------------------------------------------------------------------------------

    @Test
    void aWrongTypedFieldIsMinusOneWithStatusRequestIdAndCause() {
        reply("{\"code\":0,\"message\":\"Success\",\"request_id\":\"q9\",\"data\":{\"shops\":\"not a list\"}}");
        TikTokShopException e = assertThrows(TikTokShopException.class, () -> builder().build().authorization().getAuthorizedShops());
        assertEquals(-1, e.getCode());
        assertEquals(Integer.valueOf(200), e.getHttpStatus());
        assertEquals("q9", e.getRequestId());
        assertNotNull(e.getCause());
    }

    @Test
    void aMissingRequiredFieldInANestedResponseModelIsMinusOne() {
        // package_weight requires unit and value: the generated validateJsonElement throws IllegalArgumentException.
        reply("{\"code\":0,\"request_id\":\"q10\",\"data\":{\"package_weight\":{\"unit\":\"GRAM\"}}}");
        TikTokShopException e = assertThrows(TikTokShopException.class, () -> builder().build().products()
                .predictProductPackageDimensionsAndWeight(new PredictProductPackageDimensionsAndWeightRequest().categoryId("1")));
        assertEquals(-1, e.getCode());
        assertEquals("q10", e.getRequestId());
        assertInstanceOf(IllegalArgumentException.class, e.getCause());
    }

    // --- I6: async errors -----------------------------------------------------------------------------------------------

    static final class Captured<T> implements ApiCallback<T> {
        final CountDownLatch done = new CountDownLatch(1);
        final AtomicReference<ApiException> failure = new AtomicReference<>();
        final AtomicReference<T> success = new AtomicReference<>();

        @Override
        public void onFailure(ApiException e, int statusCode, Map<String, List<String>> responseHeaders) {
            failure.set(e);
            done.countDown();
        }

        @Override
        public void onSuccess(T result, int statusCode, Map<String, List<String>> responseHeaders) {
            success.set(result);
            done.countDown();
        }

        @Override
        public void onUploadProgress(long bytesWritten, long contentLength, boolean done) {}

        @Override
        public void onDownloadProgress(long bytesRead, long contentLength, boolean done) {}

        void await() throws InterruptedException {
            assertTrue(done.await(10, TimeUnit.SECONDS), "callback never called");
        }
    }

    /** Runs an async call and fails if any thread dies with an uncaught exception meanwhile. */
    static <T> Captured<T> runAsync(ThrowingStart<T> start) throws Exception {
        List<Throwable> uncaught = Collections.synchronizedList(new ArrayList<>());
        Thread.UncaughtExceptionHandler before = Thread.getDefaultUncaughtExceptionHandler();
        Thread.setDefaultUncaughtExceptionHandler((t, e) -> uncaught.add(e));
        try {
            Captured<T> cb = new Captured<>();
            start.start(cb);
            cb.await();
            Thread.sleep(300); // OkHttp 4 rethrows on the dispatcher thread after the callback
            assertEquals(Collections.emptyList(), uncaught, "uncaught exceptions on a dispatcher thread");
            return cb;
        } finally {
            Thread.setDefaultUncaughtExceptionHandler(before);
        }
    }

    interface ThrowingStart<T> {
        void start(ApiCallback<T> cb) throws Exception;
    }

    @Test
    void anAsyncEnvelopeErrorReachesOnFailureWithTheTikTokShopExceptionAsCause() throws Exception {
        reply("{\"code\":36009003,\"message\":\"invalid\",\"request_id\":\"r1\",\"data\":{}}");
        TikTokShop c = builder().build();
        Captured<GetAuthorizedShopsResponse> cb = runAsync(c.authorization()::getAuthorizedShopsAsync);
        TikTokShopException e = assertInstanceOf(TikTokShopException.class, cb.failure.get().getCause());
        assertEquals(36009003, e.getCode());
        assertEquals("r1", e.getRequestId());
        assertEquals(200, cb.failure.get().getCode());
    }

    @Test
    void anAsyncTransportErrorReachesOnFailureWithTheTikTokShopExceptionAsCause() throws Exception {
        TikTokShop c = TikTokShop.builder().appKey("k").appSecret("s").baseUrl(closedPort()).build();
        Captured<GetAuthorizedShopsResponse> cb = runAsync(c.authorization()::getAuthorizedShopsAsync);
        assertTransportFailure(assertInstanceOf(TikTokShopException.class, cb.failure.get().getCause()));
    }

    @Test
    void anAsyncSuccessStillReachesOnSuccess() throws Exception {
        reply("{\"code\":0,\"message\":\"Success\",\"request_id\":\"r1\",\"data\":{\"shops\":[{\"id\":\"7\"}]}}");
        Captured<GetAuthorizedShopsResponse> cb = runAsync(builder().build().authorization()::getAuthorizedShopsAsync);
        assertNull(cb.failure.get());
        assertEquals("7", cb.success.get().getData().getShops().get(0).getId());
    }

    // --- lesson 34 ------------------------------------------------------------------------------------------------------

    @Test
    void aNonIntegerCodeOnA2xxIsMinusOne() throws Exception {
        for (String code : Arrays.asList("\"0\"", "1.5", "true", "null", "{}")) {
            reply("{\"code\":" + code + ",\"message\":\"m\",\"request_id\":\"q5\",\"data\":{}}");
            TikTokShopException e = assertThrows(TikTokShopException.class, () -> builder().build().authorization().getAuthorizedShops(), code);
            assertEquals(-1, e.getCode(), code);
            assertEquals(Integer.valueOf(200), e.getHttpStatus(), code);
            assertEquals("q5", e.getRequestId(), code);
            reply("{\"code\":" + code + ",\"request_id\":\"q6\",\"data\":{\"access_token\":\"a\",\"access_token_expire_in\":1,"
                    + "\"refresh_token\":\"r\",\"refresh_token_expire_in\":2}}");
            TikTokShopException t = assertThrows(TikTokShopException.class, () -> auth().exchangeCode("c"), code);
            assertEquals(-1, t.getCode(), code);
            assertEquals(Integer.valueOf(200), t.getHttpStatus(), code);
        }
        reply("{\"request_id\":\"q\",\"data\":{}}");
        assertNotNull(builder().build().authorization().getAuthorizedShops(), "no code at all is a success");
    }

    static String version() throws IOException {
        String pom = new String(Files.readAllBytes(Paths.get("pom.xml")), StandardCharsets.UTF_8);
        Matcher m = Pattern.compile("</modelVersion>[\\s\\S]*?<version>([^<]+)</version>").matcher(pom);
        assertTrue(m.find());
        return m.group(1);
    }

    @Test
    void theUserAgentIsSentOnApiAndTokenCalls() throws Exception {
        String ua = "tiktok-shop-api-java/" + version();
        reply(StubSupport.OK);
        builder().build().authorization().getAuthorizedShops();
        assertEquals(ua, server.takeRequest(5, TimeUnit.SECONDS).getHeader("User-Agent"));
        reply("{\"code\":0,\"request_id\":\"r\",\"data\":{\"access_token\":\"a\",\"access_token_expire_in\":1,\"refresh_token\":\"r\",\"refresh_token_expire_in\":2}}");
        auth().refresh("r");
        assertEquals(ua, server.takeRequest(5, TimeUnit.SECONDS).getHeader("User-Agent"));
    }

    @Test
    void grantedScopesAbsentNullOrIllTypedIsNull() throws Exception {
        String tok = "\"access_token\":\"a\",\"access_token_expire_in\":1,\"refresh_token\":\"r\",\"refresh_token_expire_in\":2";
        for (String extra : Arrays.asList("", ",\"granted_scopes\":null", ",\"granted_scopes\":\"x\"", ",\"granted_scopes\":[\"a\",1]")) {
            reply("{\"code\":0,\"request_id\":\"r\",\"data\":{" + tok + extra + "}}");
            assertNull(auth().exchangeCode("c").getGrantedScopes(), extra);
        }
        reply("{\"code\":0,\"request_id\":\"r\",\"data\":{" + tok + ",\"granted_scopes\":[\"a\",\"b\"]}}");
        assertEquals(Arrays.asList("a", "b"), auth().exchangeCode("c").getGrantedScopes());
    }

    // --- R21b -----------------------------------------------------------------------------------------------------------

    @Test
    void anIntegerEnumValueTheSpecDoesNotListStillDecodes() throws Exception {
        reply("{\"code\":0,\"request_id\":\"r\",\"data\":{\"creators\":[{\"creator_profile\":{\"user_type_tag\":[1,3]}}]}}");
        SearchCreatorsInCreatorMarketplaceResponse r = builder().build().affiliateSeller().searchCreatorsInCreatorMarketplace(1L, null, null);
        assertEquals(Arrays.asList(1L, 3L), r.getData().getCreators().get(0).getCreatorProfile().getUserTypeTag());
    }

    // --- M22 ------------------------------------------------------------------------------------------------------------

    @Test
    void aGetWithABodyThroughASocksProxyFailsFast() throws Exception {
        OkHttpClient socks = new OkHttpClient.Builder()
                .proxy(new java.net.Proxy(java.net.Proxy.Type.SOCKS, new java.net.InetSocketAddress("127.0.0.1", 9))).build();
        TikTokShop c = builder().httpClient(socks).build();
        TikTokShopException e = assertThrows(TikTokShopException.class,
                () -> c.affiliateSeller().getConversationList(10L, null, null, null, onlyIds()));
        assertEquals(-1, e.getCode());
        assertNull(e.getHttpStatus());
        assertTrue(e.getMessage().contains("SOCKS"), e.getMessage());
        RecordedRequest none = server.takeRequest(200, TimeUnit.MILLISECONDS);
        assertNull(none, "nothing may go out directly");
    }

    // --- R28 ------------------------------------------------------------------------------------------------------------

    @Test
    void aKnownWebhookWithANullOrMissingRequiredFieldIsAParseError() {
        String ok = "{\"type\":66,\"shop_id\":\"1\",\"tts_notification_id\":\"n\",\"timestamp\":1,\"data\":{\"product_id\":5,"
                + "\"appeal_task\":{\"appeal_audit_result\":[{\"indicator_type\":\"A\",\"status\":\"S\"}]}}}";
        assertNotNull(Webhooks.parse(ok));
        for (String bad : Arrays.asList(
                ok.replace("\"shop_id\":\"1\"", "\"shop_id\":null"),
                ok.replace("\"timestamp\":1", "\"timestamp\":null"),
                ok.replace("\"product_id\":5,", "\"product_id\":null,"),
                ok.replace("\"product_id\":5,", ""),
                ok.replace("\"status\":\"S\"", "\"status\":null"),
                ok.replace("\"indicator_type\":\"A\",", ""),
                "{\"type\":66,\"shop_id\":\"1\",\"tts_notification_id\":\"n\",\"timestamp\":1,\"data\":null}")) {
            assertThrows(IllegalArgumentException.class, () -> Webhooks.parse(bad), bad);
        }
    }
}
