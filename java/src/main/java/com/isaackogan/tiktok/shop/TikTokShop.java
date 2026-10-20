package com.isaackogan.tiktok.shop;

import com.isaackogan.tiktok.shop.generated.ApiClient;
import com.isaackogan.tiktok.shop.generated.Meta;
import com.isaackogan.tiktok.shop.generated.api.AffiliateCreatorApi;
import com.isaackogan.tiktok.shop.generated.api.AffiliatePartnerApi;
import com.isaackogan.tiktok.shop.generated.api.AffiliateSellerApi;
import com.isaackogan.tiktok.shop.generated.api.AnalyticsApi;
import com.isaackogan.tiktok.shop.generated.api.AuthorizationApi;
import com.isaackogan.tiktok.shop.generated.api.CustomerEngagementApi;
import com.isaackogan.tiktok.shop.generated.api.CustomerServiceApi;
import com.isaackogan.tiktok.shop.generated.api.EventApi;
import com.isaackogan.tiktok.shop.generated.api.FinanceApi;
import com.isaackogan.tiktok.shop.generated.api.FulfilledByTikTokFbtApi;
import com.isaackogan.tiktok.shop.generated.api.FulfillmentApi;
import com.isaackogan.tiktok.shop.generated.api.LogisticsApi;
import com.isaackogan.tiktok.shop.generated.api.OrdersApi;
import com.isaackogan.tiktok.shop.generated.api.ProductsApi;
import com.isaackogan.tiktok.shop.generated.api.PromotionApi;
import com.isaackogan.tiktok.shop.generated.api.ReturnAndRefundApi;
import com.isaackogan.tiktok.shop.generated.api.SellerApi;
import com.isaackogan.tiktok.shop.generated.api.SupplyChainApi;
import com.isaackogan.tiktok.shop.generated.api.ToolsApi;
import java.net.ProxySelector;
import java.net.http.HttpClient;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Locale;
import java.util.regex.Pattern;
import okhttp3.OkHttpClient;

/**
 * A client for the TikTok Shop API: one getter per API group, each returning the concrete generated API class, e.g.
 * {@code client.orders().getOrderList(20L, null, null, null, null)}.
 *
 * <p>Every request is signed, carries the access token and (where the operation takes one) the shop cipher, and every
 * failure is a {@link TikTokShopException}.
 *
 * <pre>{@code
 * TikTokShop client = TikTokShop.builder()
 *     .appKey("APP_KEY").appSecret("APP_SECRET")
 *     .accessToken("ACCESS_TOKEN").shopCipher("SHOP_CIPHER")
 *     .build();
 * }</pre>
 */
public final class TikTokShop {
    /** The TikTok Shop API's address. */
    public static final String DEFAULT_BASE_URL = "https://open-api.tiktokglobalshop.com";
    /** Bounds one request, response body included, unless {@link Builder#timeout} says otherwise. */
    public static final Duration DEFAULT_TIMEOUT = Duration.ofSeconds(30);
    /** Sent on every API and token call. {@code scripts/bump-version.ts} keeps it in step with the pom. */
    static final String USER_AGENT = "tiktok-shop-api-java/0.1.0";

    private final Shared shared;
    private final SigningInterceptor.Credentials creds;

    private final AffiliateCreatorApi affiliateCreator;
    private final AffiliatePartnerApi affiliatePartner;
    private final AffiliateSellerApi affiliateSeller;
    private final AnalyticsApi analytics;
    private final AuthorizationApi authorization;
    private final CustomerEngagementApi customerEngagement;
    private final CustomerServiceApi customerService;
    private final EventApi event;
    private final FinanceApi finance;
    private final FulfilledByTikTokFbtApi fulfilledByTikTok;
    private final FulfillmentApi fulfillment;
    private final LogisticsApi logistics;
    private final OrdersApi orders;
    private final ProductsApi products;
    private final PromotionApi promotion;
    private final ReturnAndRefundApi returnAndRefund;
    private final SellerApi seller;
    private final SupplyChainApi supplyChain;
    private final ToolsApi tools;

    private TikTokShop(Shared shared, SigningInterceptor.Credentials creds) {
        this.shared = shared;
        this.creds = creds;
        // newBuilder shares the base client's connection pool and dispatcher; only the signing interceptor differs.
        OkHttpClient http = shared.http.newBuilder().addInterceptor(new SigningInterceptor(creds, shared::jdk)).build();
        ApiClient api = new TikTokApiClient(http);
        api.setBasePath(shared.baseUrl);
        api.setUserAgent(USER_AGENT);
        this.affiliateCreator = new AffiliateCreatorApi(api);
        this.affiliatePartner = new AffiliatePartnerApi(api);
        this.affiliateSeller = new AffiliateSellerApi(api);
        this.analytics = new AnalyticsApi(api);
        this.authorization = new AuthorizationApi(api);
        this.customerEngagement = new CustomerEngagementApi(api);
        this.customerService = new CustomerServiceApi(api);
        this.event = new EventApi(api);
        this.finance = new FinanceApi(api);
        this.fulfilledByTikTok = new FulfilledByTikTokFbtApi(api);
        this.fulfillment = new FulfillmentApi(api);
        this.logistics = new LogisticsApi(api);
        this.orders = new OrdersApi(api);
        this.products = new ProductsApi(api);
        this.promotion = new PromotionApi(api);
        this.returnAndRefund = new ReturnAndRefundApi(api);
        this.seller = new SellerApi(api);
        this.supplyChain = new SupplyChainApi(api);
        this.tools = new ToolsApi(api);
    }

    /** Never prints the app secret, the access token or the shop cipher. */
    @Override
    public String toString() {
        return "TikTokShop{appKey=" + creds.appKey + ", appSecret=***, accessToken=" + (creds.accessToken == null || creds.accessToken.isEmpty() ? "null" : "***") + ", shopCipher=" + (creds.shopCipher == null || creds.shopCipher.isEmpty() ? "null" : "***")
                + ", baseUrl=" + shared.baseUrl + "}";
    }

    /** Starts a client. */
    public static Builder builder() {
        return new Builder();
    }

    /** The affiliateCreator API group. */
    public AffiliateCreatorApi affiliateCreator() {
        return affiliateCreator;
    }

    /** The affiliatePartner API group. */
    public AffiliatePartnerApi affiliatePartner() {
        return affiliatePartner;
    }

    /** The affiliateSeller API group. */
    public AffiliateSellerApi affiliateSeller() {
        return affiliateSeller;
    }

    /** The analytics API group. */
    public AnalyticsApi analytics() {
        return analytics;
    }

    /** The authorization API group. */
    public AuthorizationApi authorization() {
        return authorization;
    }

    /** The customerEngagement API group. */
    public CustomerEngagementApi customerEngagement() {
        return customerEngagement;
    }

    /** The customerService API group. */
    public CustomerServiceApi customerService() {
        return customerService;
    }

    /** The event API group. */
    public EventApi event() {
        return event;
    }

    /** The finance API group. */
    public FinanceApi finance() {
        return finance;
    }

    /** The fulfilledByTikTok API group. */
    public FulfilledByTikTokFbtApi fulfilledByTikTok() {
        return fulfilledByTikTok;
    }

    /** The fulfillment API group. */
    public FulfillmentApi fulfillment() {
        return fulfillment;
    }

    /** The logistics API group. */
    public LogisticsApi logistics() {
        return logistics;
    }

    /** The orders API group. */
    public OrdersApi orders() {
        return orders;
    }

    /** The products API group. */
    public ProductsApi products() {
        return products;
    }

    /** The promotion API group. */
    public PromotionApi promotion() {
        return promotion;
    }

    /** The returnAndRefund API group. */
    public ReturnAndRefundApi returnAndRefund() {
        return returnAndRefund;
    }

    /** The seller API group. */
    public SellerApi seller() {
        return seller;
    }

    /** The supplyChain API group. */
    public SupplyChainApi supplyChain() {
        return supplyChain;
    }

    /** The tools API group. */
    public ToolsApi tools() {
        return tools;
    }

    /**
     * Returns a client for another shop or token that shares this client's HTTP client, base URL and timeout. A value
     * {@code shop} does not set keeps this client's value; one it sets to {@code null} or empty clears it. This client is not
     * changed.
     */
    public TikTokShop withShop(ShopCredentials shop) {
        return new TikTokShop(shared, new SigningInterceptor.Credentials(creds.appKey, creds.appSecret,
                shop.isAccessTokenSet() ? shop.accessToken() : creds.accessToken,
                shop.isShopCipherSet() ? shop.shopCipher() : creds.shopCipher));
    }

    /** Shorthand for {@code withShop} with both values set; {@code null} or empty clears one. */
    public TikTokShop withShop(String accessToken, String shopCipher) {
        return withShop(ShopCredentials.builder().accessToken(accessToken).shopCipher(shopCipher).build());
    }

    /** The JDK client used for GET requests with a body. */
    HttpClient jdkClient() {
        return shared.jdk();
    }

    /** Reports whether the JDK client has been built yet. */
    boolean jdkClientBuilt() {
        return shared.jdkBuilt();
    }

    /** What a client and the clients {@code withShop} derives from it share. */
    private static final class Shared {
        /** Answers every {@code select} with {@link java.net.Proxy#NO_PROXY}, never the JVM default. */
        private static final ProxySelector NO_PROXY = new ProxySelector() {
            @Override
            public List<java.net.Proxy> select(java.net.URI uri) {
                return Collections.singletonList(java.net.Proxy.NO_PROXY);
            }

            @Override
            public void connectFailed(java.net.URI uri, java.net.SocketAddress sa, java.io.IOException ioe) {}
        };

        final OkHttpClient http;
        final String baseUrl;
        private volatile HttpClient jdk;

        Shared(OkHttpClient http, String baseUrl) {
            this.http = http;
            this.baseUrl = baseUrl;
        }

        boolean jdkBuilt() {
            return jdk != null;
        }

        /**
         * For the GET requests that carry a body, which OkHttp cannot send. Built on first use, so a client that never makes
         * one never starts the JDK client's selector thread. HTTP/1.1 only: no h2c upgrade headers.
         */
        HttpClient jdk() {
            HttpClient c = jdk;
            if (c == null) {
                synchronized (this) {
                    c = jdk;
                    if (c == null) {
                        c = buildJdk();
                        jdk = c;
                    }
                }
            }
            return c;
        }

        private HttpClient buildJdk() {
            HttpClient.Builder j = HttpClient.newBuilder().version(HttpClient.Version.HTTP_1_1);
            // OkHttp: 0 means no timeout. The JDK client has no connect timeout unless one is set.
            if (http.connectTimeoutMillis() > 0) {
                j.connectTimeout(Duration.ofMillis(http.connectTimeoutMillis()));
            }
            java.net.Proxy proxy = http.proxy();
            if (proxy == null) {
                j.proxy(http.proxySelector() == null ? ProxySelector.getDefault() : http.proxySelector());
            } else if (proxy.type() == java.net.Proxy.Type.HTTP && proxy.address() instanceof java.net.InetSocketAddress) {
                j.proxy(ProxySelector.of((java.net.InetSocketAddress) proxy.address()));
            } else if (proxy.type() == java.net.Proxy.Type.SOCKS) {
                // java.net.http cannot use a SOCKS proxy. Fail rather than silently send the request direct.
                throw new TikTokShopException(-1, "a GET with a body is sent with java.net.http, which cannot use the configured"
                        + " SOCKS proxy; configure an HTTP proxy or none", "", null, null);
            } else {
                j.proxy(NO_PROXY); // an explicit DIRECT: none, never the JVM default
            }
            return j.build();
        }
    }

    /** Configures a {@link TikTokShop}. */
    public static final class Builder {
        private String appKey;
        private String appSecret;
        private String accessToken;
        private String shopCipher;
        private String baseUrl = DEFAULT_BASE_URL;
        private Duration timeout;
        private OkHttpClient httpClient;

        private Builder() {}

        /** Never prints the app secret, the access token or the shop cipher. */
        @Override
        public String toString() {
            return "TikTokShop.Builder{appKey=" + appKey + ", appSecret=" + (appSecret == null ? "null" : "***") + ", accessToken=" + (accessToken == null || accessToken.isEmpty() ? "null" : "***")
                    + ", shopCipher=" + (shopCipher == null || shopCipher.isEmpty() ? "null" : "***") + ", baseUrl=" + baseUrl + ", timeout=" + timeout + ", httpClient=" + (httpClient != null) + "}";
        }

        public Builder appKey(String appKey) {
            this.appKey = appKey;
            return this;
        }

        public Builder appSecret(String appSecret) {
            this.appSecret = appSecret;
            return this;
        }

        /** Sent as the x-tts-access-token header. Null or empty sends none. */
        public Builder accessToken(String accessToken) {
            this.accessToken = accessToken;
            return this;
        }

        /** Added to the operations that take one. Null or empty adds none. */
        public Builder shopCipher(String shopCipher) {
            this.shopCipher = shopCipher;
            return this;
        }

        /** Overrides {@link #DEFAULT_BASE_URL}, e.g. for a test server. */
        public Builder baseUrl(String baseUrl) {
            this.baseUrl = baseUrl;
            return this;
        }

        /**
         * Bounds one request, response body included. Without it, {@link #DEFAULT_TIMEOUT} applies to the default HTTP
         * client, and a client you supply keeps its own timeouts.
         */
        public Builder timeout(Duration timeout) {
            this.timeout = timeout;
            return this;
        }

        /**
         * Carries the signed requests. Its connection pool, proxy, TLS settings, interceptors and timeouts are used as they are.
         * Without it, a default OkHttp client is used, which honours the JVM's proxy settings and never follows a redirect
         * (a 3xx surfaces as a {@link TikTokShopException} carrying the status). A client you supply is used as it is,
         * so its redirect policy applies.
         *
         * <p>Three operations ({@code getConversationList}, {@code mapTokopediaToTikTokShopProductIDs} and
         * {@code getShippingTemplateAvailability}) are GETs with a body, which OkHttp cannot send, so they go through the JDK's
         * {@code java.net.http.HttpClient} instead. For those, only these settings of your client apply: an HTTP proxy
         * ({@code proxy()}, or else {@code proxySelector()}), the connect timeout and the call timeout (or else the read
         * timeout), which bound the whole exchange. Not applied: SOCKS proxies, authenticators, custom
         * {@code sslSocketFactory}, {@code hostnameVerifier} and certificate pinner (the JVM's default trust store is used),
         * DNS, redirects (never followed) and interceptors that run after the signing one.
         */
        public Builder httpClient(OkHttpClient httpClient) {
            this.httpClient = httpClient;
            return this;
        }

        public TikTokShop build() {
            if (appKey == null || appSecret == null) {
                throw new IllegalStateException("appKey and appSecret are required");
            }
            // The default client never follows a redirect: a followed cross-host redirect would forward the x-tts-access-token
            // header. A client you supply is used as it is.
            OkHttpClient.Builder http = httpClient != null ? httpClient.newBuilder()
                    : new OkHttpClient.Builder().followRedirects(false).followSslRedirects(false);
            Duration t = timeout != null ? timeout : (httpClient == null ? DEFAULT_TIMEOUT : null);
            if (t != null) {
                http.connectTimeout(t).readTimeout(t).writeTimeout(t).callTimeout(t);
            }
            String base = baseUrl == null || baseUrl.isEmpty() ? DEFAULT_BASE_URL : baseUrl;
            while (base.endsWith("/")) {
                base = base.substring(0, base.length() - 1);
            }
            return new TikTokShop(new Shared(http.build(), base), new SigningInterceptor.Credentials(appKey, appSecret, accessToken, shopCipher));
        }
    }

    private static final class Matcher {
        final Meta.Operation op;
        final int literals;
        final Pattern re;

        Matcher(Meta.Operation op, int literals, Pattern re) {
            this.op = op;
            this.literals = literals;
            this.re = re;
        }
    }

    private static final List<Matcher> MATCHERS = new ArrayList<>();

    static {
        for (Meta.Operation op : Meta.OPERATIONS) {
            StringBuilder re = new StringBuilder("^");
            int literals = 0;
            for (String seg : op.path.split("/", -1)) {
                if (re.length() > 1) {
                    re.append('/');
                }
                if (seg.startsWith("{") && seg.endsWith("}")) {
                    re.append("[^/]+");
                } else {
                    re.append(Pattern.quote(seg));
                    literals++;
                }
            }
            MATCHERS.add(new Matcher(op, literals, Pattern.compile(re.append('$').toString())));
        }
    }

    /**
     * Reports whether the operation matching {@code method} and {@code path} takes a {@code shop_cipher} query parameter. A
     * {@code {x}} in a path template matches exactly one segment, the method is compared case-insensitively, and the
     * template with the most literal segments wins.
     */
    public static boolean requiresShopCipher(String method, String path) {
        String m = method.toUpperCase(Locale.ROOT);
        Matcher best = null;
        for (Matcher x : MATCHERS) {
            if (x.op.method.equals(m) && x.re.matcher(path).matches() && (best == null || x.literals > best.literals)) {
                best = x;
            }
        }
        return best != null && best.op.requiresShopCipher;
    }
}
