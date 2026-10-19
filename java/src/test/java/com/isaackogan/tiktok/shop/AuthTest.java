package com.isaackogan.tiktok.shop;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import java.io.IOException;
import java.net.ServerSocket;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.time.Duration;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import okhttp3.mockwebserver.MockResponse;
import okhttp3.mockwebserver.MockWebServer;
import okhttp3.mockwebserver.RecordedRequest;
import okhttp3.mockwebserver.SocketPolicy;
import org.junit.jupiter.api.Test;

class AuthTest {
    private static JsonObject vectors() throws IOException {
        String raw = new String(Files.readAllBytes(Paths.get("../shared/test-vectors/auth.json")), StandardCharsets.UTF_8);
        return JsonParser.parseString(raw).getAsJsonObject();
    }

    private static String str(JsonElement e) {
        return e.isJsonNull() ? null : e.getAsString();
    }

    private static TikTokShopAuth.Builder builder(MockWebServer s) {
        return TikTokShopAuth.builder().appKey("123abc").appSecret("s3cret").baseUrl(s.url("/").toString());
    }

    private static final String MIN = "{\"code\":0,\"message\":\"success\",\"request_id\":\"rq\",\"data\":"
            + "{\"access_token\":\"AT\",\"access_token_expire_in\":10,\"refresh_token\":\"RT\",\"refresh_token_expire_in\":20}}";

    private static TokenSet exchange(String body) throws Exception {
        try (MockWebServer s = new MockWebServer()) {
            s.enqueue(new MockResponse().setBody(body));
            s.start();
            return builder(s).build().exchangeCode("C");
        }
    }

    private static TikTokShopException exchangeFails(String body, int status) throws Exception {
        try (MockWebServer s = new MockWebServer()) {
            s.enqueue(new MockResponse().setResponseCode(status).setBody(body));
            s.start();
            return assertThrows(TikTokShopException.class, () -> builder(s).build().exchangeCode("C"));
        }
    }

    @Test
    void everyAuthorizationUrlVector() throws IOException {
        JsonArray cases = vectors().getAsJsonArray("authorizationUrls");
        assertTrue(cases.size() >= 5);
        for (JsonElement el : cases) {
            JsonObject c = el.getAsJsonObject();
            TikTokShopAuth auth = TikTokShopAuth.builder().appKey(c.get("appKey").isJsonNull() ? "unused" : c.get("appKey").getAsString())
                    .appSecret("x").serviceId(str(c.get("serviceId"))).build();
            TikTokShopAuth.AuthType type = TikTokShopAuth.AuthType.valueOf(c.get("type").getAsString().toUpperCase());
            TikTokShopAuth.Region region = TikTokShopAuth.Region.valueOf(c.get("region").getAsString().toUpperCase());
            String state = str(c.get("state"));
            String url = state == null ? auth.authorizationUrl(type, region) : auth.authorizationUrl(type, region, state);
            assertEquals(c.get("url").getAsString(), url);
        }
    }

    @Test
    void emptyStateAddsNoParameter() {
        TikTokShopAuth auth = TikTokShopAuth.builder().appKey("k").appSecret("s").serviceId("1").build();
        assertEquals("https://services.tiktokshop.com/open/authorize?service_id=1",
                auth.authorizationUrl(TikTokShopAuth.AuthType.SELLER, TikTokShopAuth.Region.ROW, ""));
    }

    @Test
    void sellerAndPartnerUrlsNeedAServiceId() {
        TikTokShopAuth auth = TikTokShopAuth.builder().appKey("k").appSecret("s").build();
        assertThrows(IllegalStateException.class, () -> auth.authorizationUrl(TikTokShopAuth.AuthType.SELLER, TikTokShopAuth.Region.US));
        assertThrows(IllegalStateException.class, () -> auth.authorizationUrl(TikTokShopAuth.AuthType.PARTNER, TikTokShopAuth.Region.US));
        assertTrue(auth.authorizationUrl(TikTokShopAuth.AuthType.CREATOR, TikTokShopAuth.Region.US).startsWith("https://shop.tiktok.com/"));
    }

    @Test
    void everyTokenRequestVectorIsAGetWithTheQueryInOrder() throws Exception {
        for (JsonElement el : vectors().getAsJsonArray("tokenRequests")) {
            JsonObject c = el.getAsJsonObject();
            try (MockWebServer s = new MockWebServer()) {
                s.enqueue(new MockResponse().setBody(MIN));
                s.start();
                TikTokShopAuth auth = TikTokShopAuth.builder().appKey(c.get("appKey").getAsString())
                        .appSecret(c.get("appSecret").getAsString()).baseUrl(s.url("/").toString()).build();
                TokenSet t = c.get("kind").getAsString().equals("exchange")
                        ? auth.exchangeCode(c.get("value").getAsString()) : auth.refresh(c.get("value").getAsString());
                assertEquals("AT", t.getAccessToken());
                RecordedRequest r = s.takeRequest();
                assertEquals("GET", r.getMethod());
                String expected = c.get("url").getAsString().replace("https://auth.tiktok-shops.com", "");
                assertEquals(expected, r.getPath());
            }
        }
    }

    @Test
    void everyTokenResponseVector() throws Exception {
        for (JsonElement el : vectors().getAsJsonArray("tokenResponses")) {
            JsonObject c = el.getAsJsonObject();
            String body = c.get("body").getAsString();
            if (c.get("expected").isJsonNull()) {
                TikTokShopException ex = exchangeFails(body, 200);
                assertEquals(c.get("errorCode").getAsInt(), ex.getCode());
                assertEquals("r2", ex.getRequestId());
                assertEquals("invalid auth code", ex.getMessage());
                continue;
            }
            JsonObject x = c.getAsJsonObject("expected");
            TokenSet t = exchange(body);
            assertEquals(x.get("accessToken").getAsString(), t.getAccessToken());
            assertEquals(x.get("accessTokenExpireIn").getAsLong(), t.getAccessTokenExpireIn());
            assertEquals(x.get("refreshToken").getAsString(), t.getRefreshToken());
            assertEquals(x.get("refreshTokenExpireIn").getAsLong(), t.getRefreshTokenExpireIn());
            assertEquals(x.get("openId").getAsString(), t.getOpenId());
            assertEquals(x.get("sellerName").getAsString(), t.getSellerName());
            assertEquals(x.get("sellerBaseRegion").getAsString(), t.getSellerBaseRegion());
            assertEquals(Integer.valueOf(x.get("userType").getAsInt()), t.getUserType());
            assertEquals(Arrays.asList("seller.affiliate_collaboration.read", "seller.affiliate_collaboration.write"), t.getGrantedScopes());
        }
    }

    @Test
    void aMinimalFourFieldResponseSucceeds() throws Exception {
        TokenSet t = exchange(MIN);
        assertEquals("AT", t.getAccessToken());
        assertEquals(10L, t.getAccessTokenExpireIn());
        assertEquals("RT", t.getRefreshToken());
        assertEquals(20L, t.getRefreshTokenExpireIn());
        assertNull(t.getOpenId());
        assertNull(t.getSellerName());
        assertNull(t.getSellerBaseRegion());
        assertNull(t.getUserType());
        assertEquals(Collections.<String>emptyList(), t.getGrantedScopes());
    }

    private static String data(String fields) {
        return "{\"code\":0,\"message\":\"success\",\"request_id\":\"rq\",\"data\":{" + fields + "}}";
    }

    private static final String TOK = "\"access_token\":\"AT\",\"access_token_expire_in\":10,\"refresh_token\":\"RT\",\"refresh_token_expire_in\":20";

    @Test
    void optionalFieldsThatAreNullOrIllTypedBecomeNull() throws Exception {
        TokenSet t = exchange(data(TOK + ",\"open_id\":null,\"seller_name\":null,\"seller_base_region\":7,\"user_type\":\"x\",\"granted_scopes\":null"));
        assertNull(t.getOpenId());
        assertNull(t.getSellerName());
        assertNull(t.getSellerBaseRegion());
        assertNull(t.getUserType());
        assertTrue(t.getGrantedScopes().isEmpty());
        TokenSet u = exchange(data(TOK + ",\"granted_scopes\":[\"a\",1,null,\"b\"]"));
        assertEquals(Arrays.asList("a", "b"), u.getGrantedScopes());
    }

    @Test
    void aNumericOpenIdKeepsItsExactDigits() throws Exception {
        assertEquals("7494049642642441621", exchange(data(TOK + ",\"open_id\":7494049642642441621")).getOpenId());
    }

    @Test
    void missingNullOrIllTypedRequiredFieldsAreRejectedWithCodeMinusOneAndTheRequestId() throws Exception {
        List<String> bad = Arrays.asList(
                "\"access_token_expire_in\":10,\"refresh_token\":\"RT\",\"refresh_token_expire_in\":20",
                "\"access_token\":null,\"access_token_expire_in\":10,\"refresh_token\":\"RT\",\"refresh_token_expire_in\":20",
                "\"access_token\":\"\",\"access_token_expire_in\":10,\"refresh_token\":\"RT\",\"refresh_token_expire_in\":20",
                "\"access_token\":5,\"access_token_expire_in\":10,\"refresh_token\":\"RT\",\"refresh_token_expire_in\":20",
                "\"access_token\":\"AT\",\"access_token_expire_in\":true,\"refresh_token\":\"RT\",\"refresh_token_expire_in\":20",
                "\"access_token\":\"AT\",\"access_token_expire_in\":\"10\",\"refresh_token\":\"RT\",\"refresh_token_expire_in\":20",
                "\"access_token\":\"AT\",\"access_token_expire_in\":1.5,\"refresh_token\":\"RT\",\"refresh_token_expire_in\":20",
                "\"access_token\":\"AT\",\"access_token_expire_in\":10,\"refresh_token\":\"\",\"refresh_token_expire_in\":20",
                "\"access_token\":\"AT\",\"access_token_expire_in\":10,\"refresh_token\":\"RT\",\"refresh_token_expire_in\":null",
                "\"access_token\":\"AT\",\"access_token_expire_in\":10,\"refresh_token\":\"RT\",\"refresh_token_expire_in\":false",
                "\"access_token\":\"AT\",\"access_token_expire_in\":10,\"refresh_token\":\"RT\"");
        for (String fields : bad) {
            TikTokShopException ex = exchangeFails(data(fields), 200);
            assertEquals(-1, ex.getCode(), fields);
            assertEquals("rq", ex.getRequestId(), fields);
        }
    }

    @Test
    void successWithoutDataOrWithNonObjectDataIsRejected() throws Exception {
        for (String body : Arrays.asList("{\"code\":0,\"request_id\":\"rq\"}", "{\"code\":0,\"request_id\":\"rq\",\"data\":null}",
                "{\"code\":0,\"request_id\":\"rq\",\"data\":[1]}", "{\"code\":0,\"request_id\":\"rq\",\"data\":\"x\"}")) {
            TikTokShopException ex = exchangeFails(body, 200);
            assertEquals(-1, ex.getCode(), body);
            assertEquals("rq", ex.getRequestId());
        }
    }

    @Test
    void nonJsonBodiesUseCodeMinusOne() throws Exception {
        for (int status : new int[] {200, 502}) {
            TikTokShopException ex = exchangeFails("<html>nope</html>", status);
            assertEquals(-1, ex.getCode());
            assertEquals(Integer.valueOf(status), ex.getHttpStatus());
        }
        assertEquals(-1, exchangeFails("[1]", 200).getCode());
    }

    @Test
    void nonSuccessStatusesRaiseEvenWithCodeZero() throws Exception {
        TikTokShopException ex = exchangeFails(MIN, 500);
        assertEquals(500, ex.getCode());
        assertEquals(Integer.valueOf(500), ex.getHttpStatus());
        TikTokShopException withCode = exchangeFails("{\"code\":36004004,\"message\":\"bad\",\"request_id\":\"r9\"}", 400);
        assertEquals(36004004, withCode.getCode());
        assertEquals("r9", withCode.getRequestId());
        assertEquals(Integer.valueOf(400), withCode.getHttpStatus());
    }

    @Test
    void refreshWorksToo() throws Exception {
        try (MockWebServer s = new MockWebServer()) {
            s.enqueue(new MockResponse().setBody(MIN));
            s.start();
            TokenSet t = builder(s).build().refresh("RTOK");
            assertEquals("AT", t.getAccessToken());
            assertTrue(s.takeRequest().getPath().startsWith("/api/v2/token/refresh?"));
        }
    }

    private static void assertNoSecrets(Throwable t) {
        for (Throwable c = t; c != null; c = c.getCause()) {
            String all = c + " " + c.getMessage();
            for (String secret : new String[] {"s3cret", "CODE-SECRET", "REFRESH-SECRET", "app_secret", "auth_code", "refresh_token", "?app_key"}) {
                assertFalse(all.contains(secret), "leaked " + secret + " in: " + all);
            }
        }
    }

    private static String closedPort() throws IOException {
        try (ServerSocket ss = new ServerSocket(0)) {
            return "http://127.0.0.1:" + ss.getLocalPort() + "/";
        }
    }

    @Test
    void aClosedPortLeaksNoSecretsOnExchangeOrRefresh() throws Exception {
        TikTokShopAuth auth = TikTokShopAuth.builder().appKey("123abc").appSecret("s3cret").baseUrl(closedPort()).build();
        TikTokShopException a = assertThrows(TikTokShopException.class, () -> auth.exchangeCode("CODE-SECRET"));
        TikTokShopException b = assertThrows(TikTokShopException.class, () -> auth.refresh("REFRESH-SECRET"));
        for (TikTokShopException ex : Arrays.asList(a, b)) {
            assertNoSecrets(ex);
            assertTrue(ex.getCause() instanceof IOException);
            assertEquals(-1, ex.getCode());
            assertNull(ex.getHttpStatus());
        }
    }

    @Test
    void aTimeoutLeaksNoSecretsOnExchangeOrRefresh() throws Exception {
        try (MockWebServer s = new MockWebServer()) {
            s.enqueue(new MockResponse().setSocketPolicy(SocketPolicy.NO_RESPONSE));
            s.enqueue(new MockResponse().setSocketPolicy(SocketPolicy.NO_RESPONSE));
            s.start();
            TikTokShopAuth auth = builder(s).timeout(Duration.ofMillis(300)).build();
            TikTokShopException a = assertThrows(TikTokShopException.class, () -> auth.exchangeCode("CODE-SECRET"));
            TikTokShopException b = assertThrows(TikTokShopException.class, () -> auth.refresh("REFRESH-SECRET"));
            for (TikTokShopException ex : Arrays.asList(a, b)) {
                assertNoSecrets(ex);
                assertTrue(ex.getCause() instanceof IOException);
                assertEquals(-1, ex.getCode());
            }
        }
    }

    @Test
    void aBadBaseUrlLeaksNoSecrets() {
        TikTokShopAuth auth = TikTokShopAuth.builder().appKey("k").appSecret("s3cret").baseUrl("not a url").build();
        TikTokShopException ex = assertThrows(TikTokShopException.class, () -> auth.exchangeCode("CODE-SECRET"));
        assertNoSecrets(ex);
    }
}
