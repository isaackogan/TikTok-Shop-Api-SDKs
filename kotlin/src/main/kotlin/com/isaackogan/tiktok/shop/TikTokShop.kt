package com.isaackogan.tiktok.shop

import com.isaackogan.tiktok.shop.generated.Meta
import com.isaackogan.tiktok.shop.generated.apis.AffiliateCreatorApi
import com.isaackogan.tiktok.shop.generated.apis.AffiliatePartnerApi
import com.isaackogan.tiktok.shop.generated.apis.AffiliateSellerApi
import com.isaackogan.tiktok.shop.generated.apis.AnalyticsApi
import com.isaackogan.tiktok.shop.generated.apis.AuthorizationApi
import com.isaackogan.tiktok.shop.generated.apis.CustomerEngagementApi
import com.isaackogan.tiktok.shop.generated.apis.CustomerServiceApi
import com.isaackogan.tiktok.shop.generated.apis.EventApi
import com.isaackogan.tiktok.shop.generated.apis.FinanceApi
import com.isaackogan.tiktok.shop.generated.apis.FulfilledByTikTokFBTApi
import com.isaackogan.tiktok.shop.generated.apis.FulfillmentApi
import com.isaackogan.tiktok.shop.generated.apis.LogisticsApi
import com.isaackogan.tiktok.shop.generated.apis.OrdersApi
import com.isaackogan.tiktok.shop.generated.apis.ProductsApi
import com.isaackogan.tiktok.shop.generated.apis.PromotionApi
import com.isaackogan.tiktok.shop.generated.apis.ReturnAndRefundApi
import com.isaackogan.tiktok.shop.generated.apis.SellerApi
import com.isaackogan.tiktok.shop.generated.apis.SupplyChainApi
import com.isaackogan.tiktok.shop.generated.apis.ToolsApi
import java.io.IOException
import java.net.InetSocketAddress
import java.net.Proxy
import java.net.ProxySelector
import java.net.SocketAddress
import java.net.URI
import java.net.http.HttpClient
import java.time.Duration
import java.util.Locale
import okhttp3.OkHttpClient

/** The TikTok Shop API's address. */
const val DEFAULT_BASE_URL = "https://open-api.tiktokglobalshop.com"

/** Bounds one request, response body included, unless [TikTokShopOptions.timeout] says otherwise. */
val DEFAULT_TIMEOUT: Duration = Duration.ofSeconds(30)

/** What configures a [TikTokShop]. */
data class TikTokShopOptions(
    val appKey: String,
    val appSecret: String,
    /** Sent as the x-tts-access-token header. Null or empty sends none. */
    val accessToken: String? = null,
    /** Added to the operations that take one. Null or empty adds none. */
    val shopCipher: String? = null,
    /** Overrides [DEFAULT_BASE_URL], e.g. for a test server. */
    val baseUrl: String = DEFAULT_BASE_URL,
    /**
     * Bounds one request, response body included. Without it, [DEFAULT_TIMEOUT] applies to the default HTTP client, and a
     * [httpClient] you supply keeps its own timeouts.
     */
    val timeout: Duration? = null,
    /**
     * Carries the signed requests. Its connection pool, proxy, TLS settings, interceptors and timeouts are used as they are.
     * Without it, a default OkHttp client is used, which honours the JVM's proxy settings and never follows a redirect (a 3xx
     * surfaces as a [TikTokShopException] carrying the status). A client you supply is used as it is, so its redirect policy
     * applies.
     *
     * Three operations (`getConversationList`, `mapTokopediaToTikTokShopProductIDs` and `getShippingTemplateAvailability`)
     * are GETs with a body, which OkHttp cannot send, so they go through the JDK's `java.net.http.HttpClient` instead. For
     * those, only these settings of your client apply: an HTTP proxy (`proxy`, or else `proxySelector`), the connect timeout
     * and the call timeout (or else the read timeout), which bound the whole exchange. Not applied: SOCKS proxies,
     * authenticators, custom `sslSocketFactory`, `hostnameVerifier` and certificate pinner (the JVM's default trust store is
     * used), DNS, redirects (never followed) and interceptors that run after the signing one.
     */
    val httpClient: OkHttpClient? = null,
) {
    /** Never prints the app secret or the access token. */
    override fun toString(): String =
        "TikTokShopOptions(appKey=$appKey, appSecret=***, accessToken=${if (accessToken.isNullOrEmpty()) "null" else "***"}, " +
            "shopCipher=${if (shopCipher.isNullOrEmpty()) "null" else "***"}, baseUrl=$baseUrl, timeout=$timeout, httpClient=${httpClient != null})"
}

/**
 * A client for the TikTok Shop API: one property per API group, each the concrete generated API class, e.g.
 * `client.orders.getOrderList(20L)`.
 *
 * Every request is signed, carries the access token and (where the operation takes one) the shop cipher, and every failure is
 * a [TikTokShopException].
 *
 * ```
 * val client = TikTokShop(TikTokShopOptions(appKey = "APP_KEY", appSecret = "APP_SECRET", accessToken = "ACCESS_TOKEN", shopCipher = "SHOP_CIPHER"))
 * ```
 */
class TikTokShop private constructor(private val shared: Shared, private val creds: Credentials) {
    constructor(options: TikTokShopOptions) : this(Shared.of(options), Credentials(options.appKey, options.appSecret, options.accessToken, options.shopCipher))

    /** The JDK client used for GET requests with a body. */
    internal val jdkClient: HttpClient get() = shared.jdk

    private val api = shared.http.newBuilder() // newBuilder shares the base client's pool and dispatcher; only the interceptor differs
        .addInterceptor(SigningInterceptor(creds) { shared.jdk }).build()

    val affiliateCreator: AffiliateCreatorApi = AffiliateCreatorApi(shared.baseUrl, api)
    val affiliatePartner: AffiliatePartnerApi = AffiliatePartnerApi(shared.baseUrl, api)
    val affiliateSeller: AffiliateSellerApi = AffiliateSellerApi(shared.baseUrl, api)
    val analytics: AnalyticsApi = AnalyticsApi(shared.baseUrl, api)
    val authorization: AuthorizationApi = AuthorizationApi(shared.baseUrl, api)
    val customerEngagement: CustomerEngagementApi = CustomerEngagementApi(shared.baseUrl, api)
    val customerService: CustomerServiceApi = CustomerServiceApi(shared.baseUrl, api)
    val event: EventApi = EventApi(shared.baseUrl, api)
    val finance: FinanceApi = FinanceApi(shared.baseUrl, api)
    val fulfilledByTikTok: FulfilledByTikTokFBTApi = FulfilledByTikTokFBTApi(shared.baseUrl, api)
    val fulfillment: FulfillmentApi = FulfillmentApi(shared.baseUrl, api)
    val logistics: LogisticsApi = LogisticsApi(shared.baseUrl, api)
    val orders: OrdersApi = OrdersApi(shared.baseUrl, api)
    val products: ProductsApi = ProductsApi(shared.baseUrl, api)
    val promotion: PromotionApi = PromotionApi(shared.baseUrl, api)
    val returnAndRefund: ReturnAndRefundApi = ReturnAndRefundApi(shared.baseUrl, api)
    val seller: SellerApi = SellerApi(shared.baseUrl, api)
    val supplyChain: SupplyChainApi = SupplyChainApi(shared.baseUrl, api)
    val tools: ToolsApi = ToolsApi(shared.baseUrl, api)

    /**
     * Returns a client for another shop or token that shares this client's HTTP client, base URL and timeout. This client is
     * not changed.
     *
     * An argument you omit keeps this client's value; one you pass as `null` or an empty string clears it:
     *
     * ```
     * client.withShop(accessToken = "t2")                  // new token, same cipher
     * client.withShop(accessToken = "t2", shopCipher = "c2")
     * client.withShop(shopCipher = null)                   // same token, no cipher
     * ```
     */
    fun withShop(accessToken: String? = KEEP, shopCipher: String? = KEEP): TikTokShop =
        TikTokShop(
            shared,
            Credentials(
                creds.appKey,
                creds.appSecret,
                if (accessToken === KEEP) creds.accessToken else accessToken,
                if (shopCipher === KEEP) creds.shopCipher else shopCipher,
            ),
        )

    /** What a client and the clients [withShop] derives from it share. */
    internal class Shared(val http: OkHttpClient, val baseUrl: String) {
        // For the GET requests that carry a body, which OkHttp cannot send. Built on first use, so a client that never makes one
        // never starts the JDK client's selector thread. HTTP/1.1 only: no h2c upgrade headers.
        val jdk: HttpClient by lazy {
            HttpClient.newBuilder().version(HttpClient.Version.HTTP_1_1)
                .apply {
                    // OkHttp: 0 means no timeout. The JDK client has no connect timeout unless one is set.
                    if (http.connectTimeoutMillis > 0) connectTimeout(Duration.ofMillis(http.connectTimeoutMillis.toLong()))
                    val proxy = http.proxy
                    val address = proxy?.address()
                    if (proxy == null) {
                        proxy(http.proxySelector)
                    } else if (proxy.type() == Proxy.Type.HTTP && address is InetSocketAddress) {
                        proxy(ProxySelector.of(address))
                    } else {
                        proxy(NO_PROXY) // an explicit DIRECT: none; SOCKS cannot be expressed: none, never the JVM default
                    }
                }.build()
        }

        companion object {
            private val NO_PROXY = object : ProxySelector() {
                override fun select(uri: URI?): List<Proxy> = listOf(Proxy.NO_PROXY)

                override fun connectFailed(uri: URI?, sa: SocketAddress?, ioe: IOException?) {}
            }

            fun of(options: TikTokShopOptions): Shared {
                // The default client never follows a redirect: a followed cross-host redirect would forward the x-tts-access-token
                // header. A client you supply is used as it is.
                val http = (options.httpClient?.newBuilder() ?: OkHttpClient.Builder().followRedirects(false).followSslRedirects(false)).apply {
                    val t = options.timeout ?: (if (options.httpClient == null) DEFAULT_TIMEOUT else null)
                    if (t != null) connectTimeout(t).readTimeout(t).writeTimeout(t).callTimeout(t)
                }.build()
                val base = options.baseUrl.ifEmpty { DEFAULT_BASE_URL }.trimEnd('/')
                return Shared(http, base)
            }
        }
    }

    private companion object {
        /** Compared by identity: a value no caller can pass by accident, not even `""`. */
        val KEEP: String = String(CharArray(0))
    }
}

private class Matcher(val op: Meta.Operation, val literals: Int, val re: Regex)

private val MATCHERS: List<Matcher> = Meta.OPERATIONS.map { op ->
    var literals = 0
    val re = op.path.split("/").joinToString("/") { seg ->
        if (seg.startsWith("{") && seg.endsWith("}")) {
            "[^/]+"
        } else {
            literals++
            Regex.escape(seg)
        }
    }
    Matcher(op, literals, Regex("^$re$"))
}

/**
 * Reports whether the operation matching [method] and [path] takes a `shop_cipher` query parameter. A `{x}` in a path
 * template matches exactly one segment, the method is compared case-insensitively, and the template with the most literal
 * segments wins.
 */
fun requiresShopCipher(method: String, path: String): Boolean {
    val m = method.uppercase(Locale.ROOT)
    return MATCHERS.filter { it.op.method == m && it.re.matches(path) }.maxByOrNull { it.literals }?.op?.requiresShopCipher ?: false
}
