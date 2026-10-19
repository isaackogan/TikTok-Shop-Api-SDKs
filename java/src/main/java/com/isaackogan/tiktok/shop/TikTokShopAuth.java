package com.isaackogan.tiktok.shop;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.google.gson.JsonPrimitive;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.List;
import okhttp3.HttpUrl;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

/** The OAuth helper: authorization URLs, code exchange and token refresh. */
public final class TikTokShopAuth {
    /** The host of the token endpoints. */
    public static final String DEFAULT_BASE_URL = "https://auth.tiktok-shops.com";

    /** Bounds one token request unless {@link Builder#timeout} says otherwise. */
    public static final Duration DEFAULT_TIMEOUT = Duration.ofSeconds(30);

    /** Whose authorization page {@link #authorizationUrl} points at. */
    public enum AuthType {
        /** Authorizes your app for a seller. Needs a service ID. */
        SELLER("https://services.us.tiktokshop.com", "https://services.tiktokshop.com", "/open/authorize"),
        /** Authorizes your app for a partner. Needs a service ID. */
        PARTNER("https://partner.us.tiktokshop.com", "https://partner.tiktokshop.com", "/open/authorize"),
        /** Authorizes your app for an affiliate creator. */
        CREATOR("https://shop.tiktok.com", "https://shop.tiktok.com", "/alliance/creator/auth");

        private final String us;
        private final String row;
        private final String path;

        AuthType(String us, String row, String path) {
            this.us = us;
            this.row = row;
            this.path = path;
        }
    }

    /** The United States or the rest-of-world TikTok Shop host. */
    public enum Region {
        US,
        ROW
    }

    private final String appKey;
    private final String appSecret;
    private final String serviceId;
    private final String baseUrl;
    private final OkHttpClient http;

    private TikTokShopAuth(Builder b) {
        this.appKey = b.appKey;
        this.appSecret = b.appSecret;
        this.serviceId = b.serviceId;
        String base = b.baseUrl == null || b.baseUrl.isEmpty() ? DEFAULT_BASE_URL : b.baseUrl;
        while (base.endsWith("/")) {
            base = base.substring(0, base.length() - 1);
        }
        this.baseUrl = base;
        OkHttpClient.Builder http = b.httpClient != null ? b.httpClient.newBuilder() : new OkHttpClient.Builder();
        Duration t = b.timeout != null ? b.timeout : (b.httpClient == null ? DEFAULT_TIMEOUT : null);
        if (t != null) {
            http.connectTimeout(t).readTimeout(t).writeTimeout(t).callTimeout(t);
        }
        // A redirect would send the app secret and the code to wherever it points.
        this.http = http.followRedirects(false).followSslRedirects(false).build();
    }

    public static Builder builder() {
        return new Builder();
    }

    /** The page to send the seller (or partner, or creator) to, with no {@code state}. */
    public String authorizationUrl(AuthType type, Region region) {
        return authorizationUrl(type, region, null);
    }

    /**
     * The page to send the seller (or partner, or creator) to.
     *
     * @param state echoed back to your redirect URL. Null or empty adds no state parameter.
     * @throws IllegalStateException for a seller or partner URL when no service ID was set
     */
    public String authorizationUrl(AuthType type, Region region, String state) {
        StringBuilder u = new StringBuilder(region == Region.US ? type.us : type.row).append(type.path).append('?');
        if (type == AuthType.CREATOR) {
            u.append("app_key=").append(enc(appKey));
        } else {
            if (serviceId == null || serviceId.isEmpty()) {
                throw new IllegalStateException("serviceId is required for " + type + " authorization URLs");
            }
            u.append("service_id=").append(enc(serviceId));
        }
        if (state != null && !state.isEmpty()) {
            u.append("&state=").append(enc(state));
        }
        return u.toString();
    }

    /**
     * Trades the {@code auth_code} from your redirect URL for tokens.
     *
     * @throws TikTokShopException for every failure; its message and cause never contain the request URL or its query
     */
    public TokenSet exchangeCode(String code) {
        return token("get", "auth_code", code, "authorized_code");
    }

    /**
     * Trades a refresh token for new tokens.
     *
     * @throws TikTokShopException for every failure; its message and cause never contain the request URL or its query
     */
    public TokenSet refresh(String refreshToken) {
        return token("refresh", "refresh_token", refreshToken, "refresh_token");
    }

    private TokenSet token(String endpoint, String name, String value, String grantType) {
        String where = "token request to /api/v2/token/" + endpoint;
        HttpUrl url = HttpUrl.parse(baseUrl + "/api/v2/token/" + endpoint);
        if (url == null) {
            throw new TikTokShopException(-1, where + " failed: the base URL is invalid", "", null, null);
        }
        // The query is built by hand (RFC 3986, in the pinned order); HttpUrl would re-encode it.
        HttpUrl.Builder q = url.newBuilder();
        q.addEncodedQueryParameter("app_key", enc(appKey));
        q.addEncodedQueryParameter("app_secret", enc(appSecret));
        q.addEncodedQueryParameter(name, enc(value));
        q.addEncodedQueryParameter("grant_type", enc(grantType));
        int status;
        String body;
        try (Response res = http.newCall(new Request.Builder().url(q.build()).get().build()).execute()) {
            status = res.code();
            body = res.body() == null ? "" : res.body().string();
        } catch (IOException | RuntimeException e) {
            // The URL's query holds the app secret and the code, so only the exception's class goes in the message.
            throw new TikTokShopException(-1, where + " failed: " + e.getClass().getSimpleName(), "", null, e);
        }
        return toTokenSet(status, body);
    }

    private static TokenSet toTokenSet(int status, String body) {
        boolean ok = status >= 200 && status < 300;
        JsonObject env;
        try {
            JsonElement json = JsonParser.parseString(body);
            if (!json.isJsonObject()) {
                throw new IllegalArgumentException("body is not a JSON object");
            }
            env = json.getAsJsonObject();
        } catch (RuntimeException e) {
            throw new TikTokShopException(-1, "unparseable token response (HTTP " + status + ")", "", status, e);
        }
        String requestId = str(env.get("request_id"));
        requestId = requestId == null ? "" : requestId;
        String message = str(env.get("message"));
        Long code = integer(env.get("code"));
        long c = code != null ? code : (ok ? -1 : status);
        if (c != 0 || !ok) {
            if (c == 0) {
                c = status;
            }
            throw new TikTokShopException((int) c, message == null || message.isEmpty() ? "HTTP " + status : message, requestId, status, null);
        }

        JsonElement d = env.get("data");
        if (d == null || !d.isJsonObject()) {
            throw fail("token response has no data", requestId, status);
        }
        JsonObject data = d.getAsJsonObject();
        String access = nonEmpty(data.get("access_token"));
        Long accessExp = integer(data.get("access_token_expire_in"));
        String refresh = nonEmpty(data.get("refresh_token"));
        Long refreshExp = integer(data.get("refresh_token_expire_in"));
        if (access == null || accessExp == null || refresh == null || refreshExp == null) {
            throw fail("token response is missing a token field, or one has the wrong type", requestId, status);
        }
        // Optional fields: anything of the wrong type is treated as absent. open_id is an ID, so a number keeps its digits.
        JsonElement o = data.get("open_id");
        String openId = o != null && o.isJsonPrimitive() && (((JsonPrimitive) o).isString() || ((JsonPrimitive) o).isNumber())
                ? o.getAsString() : null;
        JsonElement ut = data.get("user_type");
        Long userType = integer(ut);
        List<String> scopes = new ArrayList<>();
        JsonElement gs = data.get("granted_scopes");
        if (gs != null && gs.isJsonArray()) {
            for (JsonElement s : (JsonArray) gs) {
                String v = str(s);
                if (v != null) {
                    scopes.add(v);
                }
            }
        }
        return new TokenSet(access, accessExp, refresh, refreshExp, openId, str(data.get("seller_name")),
                str(data.get("seller_base_region")),
                userType != null && userType >= Integer.MIN_VALUE && userType <= Integer.MAX_VALUE ? Integer.valueOf(userType.intValue()) : null,
                scopes);
    }

    private static TikTokShopException fail(String message, String requestId, int status) {
        return new TikTokShopException(-1, message, requestId, status, null);
    }

    /** A JSON string, or null for anything else. */
    private static String str(JsonElement e) {
        return e != null && e.isJsonPrimitive() && ((JsonPrimitive) e).isString() ? e.getAsString() : null;
    }

    private static String nonEmpty(JsonElement e) {
        String s = str(e);
        return s == null || s.isEmpty() ? null : s;
    }

    /** A JSON number with no fraction or exponent that fits a long, or null. */
    private static Long integer(JsonElement e) {
        if (e == null || !e.isJsonPrimitive() || !((JsonPrimitive) e).isNumber()) {
            return null;
        }
        String digits = e.getAsString();
        if (!digits.matches("-?\\d+")) {
            return null;
        }
        try {
            return Long.parseLong(digits);
        } catch (NumberFormatException ex) {
            return null;
        }
    }

    /** RFC 3986 percent-encoding: only unreserved characters stay, a space becomes %20. */
    private static String enc(String s) {
        if (s == null) {
            return "";
        }
        StringBuilder out = new StringBuilder();
        for (byte b : s.getBytes(StandardCharsets.UTF_8)) {
            int c = b & 0xff;
            if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z') || (c >= '0' && c <= '9') || c == '-' || c == '.' || c == '_' || c == '~') {
                out.append((char) c);
            } else {
                out.append('%').append("0123456789ABCDEF".charAt(c >> 4)).append("0123456789ABCDEF".charAt(c & 15));
            }
        }
        return out.toString();
    }

    /** Configures a {@link TikTokShopAuth}. */
    public static final class Builder {
        private String appKey;
        private String appSecret;
        private String serviceId;
        private String baseUrl;
        private Duration timeout;
        private OkHttpClient httpClient;

        private Builder() {}

        public Builder appKey(String appKey) {
            this.appKey = appKey;
            return this;
        }

        public Builder appSecret(String appSecret) {
            this.appSecret = appSecret;
            return this;
        }

        /** Your Partner Center service ID. Needed for {@link AuthType#SELLER} and {@link AuthType#PARTNER} URLs. */
        public Builder serviceId(String serviceId) {
            this.serviceId = serviceId;
            return this;
        }

        /** Overrides {@link #DEFAULT_BASE_URL}, e.g. for a test server. */
        public Builder baseUrl(String baseUrl) {
            this.baseUrl = baseUrl;
            return this;
        }

        /** Bounds one token request. Without it, {@link #DEFAULT_TIMEOUT} applies unless you supply an {@link #httpClient}. */
        public Builder timeout(Duration timeout) {
            this.timeout = timeout;
            return this;
        }

        /** Carries the requests (proxy, TLS, ...). Redirects are never followed, whatever this client says. */
        public Builder httpClient(OkHttpClient httpClient) {
            this.httpClient = httpClient;
            return this;
        }

        public TikTokShopAuth build() {
            if (appKey == null || appSecret == null) {
                throw new IllegalStateException("appKey and appSecret are required");
            }
            return new TikTokShopAuth(this);
        }
    }
}
