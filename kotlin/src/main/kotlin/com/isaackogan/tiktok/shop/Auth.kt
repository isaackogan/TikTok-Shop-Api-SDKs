package com.isaackogan.tiktok.shop

import com.google.gson.JsonElement
import com.google.gson.JsonObject
import com.google.gson.JsonParser
import com.google.gson.JsonPrimitive
import java.io.IOException
import java.time.Duration
import okhttp3.HttpUrl
import okhttp3.HttpUrl.Companion.toHttpUrlOrNull
import okhttp3.OkHttpClient
import okhttp3.Request

/** The host of the token endpoints. */
const val DEFAULT_AUTH_BASE_URL = "https://auth.tiktok-shops.com"

/** Bounds one token request unless [TikTokShopAuthOptions.timeout] says otherwise. */
val DEFAULT_AUTH_TIMEOUT: Duration = Duration.ofSeconds(30)

/** What configures a [TikTokShopAuth]. */
class TikTokShopAuthOptions(
    val appKey: String,
    val appSecret: String,
    /** Your Partner Center service ID. Needed for [TikTokShopAuth.AuthType.SELLER] and [TikTokShopAuth.AuthType.PARTNER] URLs. */
    val serviceId: String? = null,
    /** Overrides [DEFAULT_AUTH_BASE_URL], e.g. for a test server. */
    val baseUrl: String = DEFAULT_AUTH_BASE_URL,
    /** Bounds one token request. Without it, [DEFAULT_AUTH_TIMEOUT] applies unless you supply an [httpClient]. */
    val timeout: Duration? = null,
    /** Carries the requests (proxy, TLS, ...). Redirects are never followed, whatever this client says. */
    val httpClient: OkHttpClient? = null,
) {
    /** Never prints the app secret. */
    override fun toString(): String =
        "TikTokShopAuthOptions(appKey=$appKey, appSecret=***, serviceId=$serviceId, baseUrl=$baseUrl, timeout=$timeout, httpClient=${httpClient != null})"
}

/** The OAuth helper: authorization URLs, code exchange and token refresh. */
class TikTokShopAuth(options: TikTokShopAuthOptions) {
    /** Whose authorization page [authorizationUrl] points at. */
    enum class AuthType(internal val us: String, internal val row: String, internal val path: String) {
        /** Authorizes your app for a seller. Needs a service ID. */
        SELLER("https://services.us.tiktokshop.com", "https://services.tiktokshop.com", "/open/authorize"),

        /** Authorizes your app for a partner. Needs a service ID. */
        PARTNER("https://partner.us.tiktokshop.com", "https://partner.tiktokshop.com", "/open/authorize"),

        /** Authorizes your app for an affiliate creator. */
        CREATOR("https://shop.tiktok.com", "https://shop.tiktok.com", "/alliance/creator/auth"),
    }

    /** The United States or the rest-of-world TikTok Shop host. */
    enum class Region { US, ROW }

    private val appKey = options.appKey
    private val appSecret = options.appSecret
    private val serviceId = options.serviceId
    private val baseUrl = options.baseUrl.ifEmpty { DEFAULT_AUTH_BASE_URL }.trimEnd('/')
    private val http: OkHttpClient =
        (options.httpClient?.newBuilder() ?: OkHttpClient.Builder()).apply {
            val t = options.timeout ?: (if (options.httpClient == null) DEFAULT_AUTH_TIMEOUT else null)
            if (t != null) connectTimeout(t).readTimeout(t).writeTimeout(t).callTimeout(t)
            // A redirect would send the app secret and the code to wherever it points.
            followRedirects(false).followSslRedirects(false)
        }.build()

    /**
     * The page to send the seller (or partner, or creator) to.
     *
     * @param state echoed back to your redirect URL. Null or empty adds no state parameter.
     * @throws IllegalStateException for a seller or partner URL when no service ID was set
     */
    fun authorizationUrl(type: AuthType, region: Region, state: String? = null): String {
        val u = StringBuilder(if (region == Region.US) type.us else type.row).append(type.path).append('?')
        if (type == AuthType.CREATOR) {
            u.append("app_key=").append(enc(appKey))
        } else {
            check(!serviceId.isNullOrEmpty()) { "serviceId is required for $type authorization URLs" }
            u.append("service_id=").append(enc(serviceId))
        }
        if (!state.isNullOrEmpty()) u.append("&state=").append(enc(state))
        return u.toString()
    }

    /**
     * Trades the `auth_code` from your redirect URL for tokens.
     *
     * @throws TikTokShopException for every failure; its message and cause never contain the request URL or its query
     */
    fun exchangeCode(code: String): TokenSet = token("get", "auth_code", code, "authorized_code")

    /**
     * Trades a refresh token for new tokens.
     *
     * @throws TikTokShopException for every failure; its message and cause never contain the request URL or its query
     */
    fun refresh(refreshToken: String): TokenSet = token("refresh", "refresh_token", refreshToken, "refresh_token")

    private fun token(endpoint: String, name: String, value: String, grantType: String): TokenSet {
        val where = "token request to /api/v2/token/$endpoint"
        val url = "$baseUrl/api/v2/token/$endpoint".toHttpUrlOrNull()
            ?: throw TikTokShopException(-1, "$where failed: the base URL is invalid")
        // The query is built by hand (RFC 3986, in the pinned order); HttpUrl would re-encode it.
        val full: HttpUrl = url.newBuilder()
            .addEncodedQueryParameter("app_key", enc(appKey))
            .addEncodedQueryParameter("app_secret", enc(appSecret))
            .addEncodedQueryParameter(name, enc(value))
            .addEncodedQueryParameter("grant_type", enc(grantType))
            .build()
        val status: Int
        val body: String
        try {
            http.newCall(Request.Builder().url(full).get().build()).execute().use { res ->
                status = res.code
                body = res.body.string()
            }
        } catch (e: IOException) {
            // The URL's query holds the app secret and the code, so only the exception's class goes in the message.
            throw TikTokShopException(-1, "$where failed: ${e.javaClass.simpleName}", cause = e)
        } catch (e: RuntimeException) {
            throw TikTokShopException(-1, "$where failed: ${e.javaClass.simpleName}", cause = e)
        }
        return toTokenSet(status, body)
    }

    private fun toTokenSet(status: Int, body: String): TokenSet {
        val ok = status in 200..299
        val env: JsonObject =
            try {
                val json = JsonParser.parseString(body)
                require(json.isJsonObject) { "body is not a JSON object" }
                json.asJsonObject
            } catch (e: RuntimeException) {
                // No TikTok code at all: -1, except a redirect, which is never followed and so is reported by its status.
                throw TikTokShopException(if (status in 300..399) status else -1, "unparseable token response (HTTP $status)", httpStatus = status, cause = e)
            }
        val requestId = str(env["request_id"]) ?: ""
        val message = str(env["message"])
        var code: Long = integer(env["code"]) ?: if (ok) -1 else status.toLong()
        if (code != 0L || !ok) {
            if (code == 0L) code = status.toLong()
            throw TikTokShopException(code.toInt(), if (message.isNullOrEmpty()) "HTTP $status" else message, requestId, status)
        }
        val data = env["data"]?.takeIf { it.isJsonObject }?.asJsonObject
            ?: throw TikTokShopException(-1, "token response has no data", requestId, status)
        val access = nonEmpty(data["access_token"])
        val accessExp = integer(data["access_token_expire_in"])
        val refresh = nonEmpty(data["refresh_token"])
        val refreshExp = integer(data["refresh_token_expire_in"])
        if (access == null || accessExp == null || refresh == null || refreshExp == null) {
            throw TikTokShopException(-1, "token response is missing a token field, or one has the wrong type", requestId, status)
        }
        // Optional fields: anything of the wrong type is treated as absent. open_id is an ID, so a number keeps its digits.
        val o = data["open_id"]
        val openId = if (o is JsonPrimitive && (o.isString || o.isNumber)) o.asString else null
        val userType = integer(data["user_type"])?.takeIf { it in Int.MIN_VALUE..Int.MAX_VALUE }?.toInt()
        val scopes = (data["granted_scopes"] as? com.google.gson.JsonArray)?.mapNotNull { str(it) } ?: emptyList()
        return TokenSet(access, accessExp, refresh, refreshExp, openId, str(data["seller_name"]), str(data["seller_base_region"]), userType, scopes)
    }

    private companion object {
        /** A JSON string, or null for anything else. */
        fun str(e: JsonElement?): String? = if (e is JsonPrimitive && e.isString) e.asString else null

        fun nonEmpty(e: JsonElement?): String? = str(e)?.takeIf { it.isNotEmpty() }

        /** A JSON number with no fraction or exponent that fits a long, or null. */
        fun integer(e: JsonElement?): Long? {
            if (e !is JsonPrimitive || !e.isNumber) return null
            val digits = e.asString
            return if (INTEGER.matches(digits)) digits.toLongOrNull() else null
        }

        val INTEGER = Regex("-?\\d+")

        /** RFC 3986 percent-encoding: only unreserved characters stay, a space becomes %20. */
        fun enc(s: String): String {
            val out = StringBuilder()
            for (b in s.toByteArray(Charsets.UTF_8)) {
                val c = b.toInt() and 0xff
                if (c in 'A'.code..'Z'.code || c in 'a'.code..'z'.code || c in '0'.code..'9'.code || c == '-'.code || c == '.'.code || c == '_'.code || c == '~'.code) {
                    out.append(c.toChar())
                } else {
                    out.append('%').append("0123456789ABCDEF"[c shr 4]).append("0123456789ABCDEF"[c and 15])
                }
            }
            return out.toString()
        }
    }

    override fun toString(): String = "TikTokShopAuth(appKey=$appKey, appSecret=***, baseUrl=$baseUrl)"
}
