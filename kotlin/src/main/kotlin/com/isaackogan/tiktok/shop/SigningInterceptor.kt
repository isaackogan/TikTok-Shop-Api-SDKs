package com.isaackogan.tiktok.shop

import com.google.gson.JsonObject
import com.google.gson.JsonParseException
import com.google.gson.JsonParser
import java.io.IOException
import java.io.InterruptedIOException
import java.math.BigDecimal
import java.net.URI
import java.net.http.HttpClient
import java.net.http.HttpRequest
import java.net.http.HttpResponse
import java.net.http.HttpTimeoutException
import java.time.Duration
import java.util.concurrent.CompletableFuture
import java.util.concurrent.ExecutionException
import java.util.concurrent.TimeUnit
import java.util.concurrent.TimeoutException
import okhttp3.Interceptor
import okhttp3.MediaType
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.Protocol
import okhttp3.Request
import okhttp3.RequestBody
import okhttp3.Response
import okhttp3.ResponseBody.Companion.toResponseBody
import okio.Buffer

/** The values one client signs with. A null or empty token or cipher means none. */
internal class Credentials(val appKey: String, val appSecret: String, accessToken: String?, shopCipher: String?) {
    val accessToken: String? = accessToken?.ifEmpty { null }
    val shopCipher: String? = shopCipher?.ifEmpty { null }
}

/**
 * The request and response hook. It signs every request and turns every failure into a [TikTokShopException]. It never
 * modifies the request it is given.
 *
 * A GET that has a body carries it as a [RequestBody] tag (see the fix-up in `scripts/generate.ts`), because OkHttp cannot
 * send one; such a request goes through the JDK's `java.net.http.HttpClient` instead.
 */
internal class SigningInterceptor(private val creds: Credentials, private val jdk: () -> HttpClient) : Interceptor {
    override fun intercept(chain: Interceptor.Chain): Response {
        val req = chain.request()
        val getBody: RequestBody? = if (req.method == "GET") req.tag(RequestBody::class.java) else null

        var contentType = req.header("Content-Type")
        var body: ByteArray? = null
        val carried = getBody ?: req.body
        if (carried != null) {
            if (contentType == null) contentType = carried.contentType()?.toString()
            if (getBody != null || !Signer.isMultipart(contentType)) {
                val buf = Buffer()
                carried.writeTo(buf)
                body = buf.readByteArray()
            }
        }

        val url = req.url
        val query = ArrayList<Param>()
        for (i in 0 until url.querySize) {
            val k = url.queryParameterName(i)
            if (k !in RESERVED) query.add(Param(k, url.queryParameterValue(i) ?: ""))
        }
        if (creds.shopCipher != null && requiresShopCipher(req.method, url.encodedPath)) query.add(Param("shop_cipher", creds.shopCipher))
        query.add(Param("app_key", creds.appKey))
        query.add(Param("timestamp", (System.currentTimeMillis() / 1000).toString()))
        val sign = Signer.sign(SignRequest(url.encodedPath, query, contentType, body, creds.appSecret))
        query.add(Param("sign", sign))

        val encodedQuery = query.joinToString("&") { encode(it.key) + "=" + encode(it.value) }
        val signed = req.newBuilder().url(url.newBuilder().encodedQuery(encodedQuery).build())
        if (creds.accessToken != null) signed.header("x-tts-access-token", creds.accessToken)
        if (req.header("User-Agent") == null) signed.header("User-Agent", USER_AGENT)
        val out = signed.build()

        val status: Int
        val data: ByteArray
        val response: Response
        try {
            if (getBody != null) {
                val r = sendWithJdk(chain, out, body!!, contentType)
                status = r.statusCode()
                data = r.body()
                response = Response.Builder().request(out).protocol(Protocol.HTTP_1_1).code(status).message("")
                    .body(data.toResponseBody(null)).build()
            } else {
                val r = chain.proceed(out)
                status = r.code
                data = r.use { it.body.bytes() }
                response = r
            }
        } catch (e: IOException) {
            // Only the exception's class: its message can carry the request URL.
            throw TikTokShopException(0, "request failed: " + e.javaClass.simpleName, "", null, e)
        }

        checkResponse(status, data)
        // The envelope is JSON whatever Content-Type it arrived with; the generated client decodes by that header.
        return response.newBuilder().header("Content-Type", JSON).body(data.toResponseBody(JSON.toMediaType())).build()
    }

    private fun sendWithJdk(chain: Interceptor.Chain, out: Request, body: ByteArray, contentType: String?): HttpResponse<ByteArray> {
        val nanos = chain.call().timeout().timeoutNanos()
        // OkHttp: 0 means no limit, here as there.
        val timeout: Duration? = when {
            nanos > 0 -> Duration.ofNanos(nanos)
            chain.readTimeoutMillis() > 0 -> Duration.ofMillis(chain.readTimeoutMillis().toLong())
            else -> null
        }
        val b = HttpRequest.newBuilder(URI.create(out.url.toString())).apply { if (timeout != null) timeout(timeout) }
            .method("GET", HttpRequest.BodyPublishers.ofByteArray(body))
        for (name in out.headers.names()) {
            if (name.lowercase() !in JDK_RESTRICTED && !name.equals("Content-Type", ignoreCase = true)) {
                for (v in out.headers(name)) b.header(name, v)
            }
        }
        if (contentType != null) b.header("Content-Type", contentType)
        // HttpRequest.timeout only covers the wait for the headers; bound the whole exchange, body included.
        val f: CompletableFuture<HttpResponse<ByteArray>> = jdk().sendAsync(b.build(), HttpResponse.BodyHandlers.ofByteArray())
        try {
            return if (timeout == null) f.get() else f.get(timeout.toMillis(), TimeUnit.MILLISECONDS)
        } catch (e: TimeoutException) {
            f.cancel(true)
            throw HttpTimeoutException("timeout")
        } catch (e: ExecutionException) {
            val c = e.cause
            throw if (c is IOException) c else IOException(c)
        } catch (e: InterruptedException) {
            f.cancel(true)
            Thread.currentThread().interrupt()
            throw InterruptedIOException("interrupted")
        }
    }

    companion object {
        const val USER_AGENT = "tiktok-shop-api-kotlin/0.1.0"
        private const val JSON = "application/json"
        private val RESERVED = setOf("app_key", "timestamp", "sign", "shop_cipher")
        private val JDK_RESTRICTED = setOf("connection", "content-length", "expect", "host", "upgrade", "transfer-encoding")
        private const val UNRESERVED = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~"

        /** RFC 3986 percent-encoding: everything but the unreserved characters. */
        fun encode(s: String): String {
            val b = StringBuilder()
            for (x in s.toByteArray(Charsets.UTF_8)) {
                val c = x.toInt() and 0xff
                if (x >= 0 && UNRESERVED.indexOf(c.toChar()) >= 0) {
                    b.append(c.toChar())
                } else {
                    b.append('%').append("0123456789ABCDEF"[c shr 4]).append("0123456789ABCDEF"[c and 0xf])
                }
            }
            return b.toString()
        }

        /** The response hook: returns for a successful envelope, otherwise throws the [TikTokShopException]. */
        fun checkResponse(status: Int, data: ByteArray) {
            val ok = status in 200..299
            var env: JsonObject? = null
            var parseError: JsonParseException? = null
            try {
                val el = JsonParser.parseString(String(data, Charsets.UTF_8))
                if (el.isJsonObject) env = el.asJsonObject
            } catch (e: JsonParseException) {
                parseError = e
            }
            if (ok && env == null) {
                // R13b: -1 only for a 2xx reply that cannot be understood (not a JSON object).
                throw TikTokShopException(-1, "Response is not valid JSON (HTTP $status)", "", status, parseError)
            }
            var code: Long? = null
            var message: String? = null
            var requestId = ""
            if (env != null) {
                code = longOf(env, "code")
                message = stringOf(env, "message")
                requestId = stringOf(env, "request_id") ?: ""
            }
            if (!ok) {
                // R13a: a body without a code, or with code 0, still failed, so the HTTP status is the code.
                val c = if (code != null && code != 0L && code in Int.MIN_VALUE..Int.MAX_VALUE) code.toInt() else status
                throw TikTokShopException(c, message ?: "HTTP $status", requestId, status)
            }
            if (code != null && code != 0L) {
                val c = if (code in Int.MIN_VALUE..Int.MAX_VALUE) code.toInt() else -1
                throw TikTokShopException(c, message ?: "", requestId, status)
            }
        }

        private fun stringOf(o: JsonObject, key: String): String? {
            val e = o.get(key)
            return if (e != null && e.isJsonPrimitive && e.asJsonPrimitive.isString) e.asString else null
        }

        private fun longOf(o: JsonObject, key: String): Long? {
            val e = o.get(key)
            if (e == null || !e.isJsonPrimitive || !e.asJsonPrimitive.isNumber) return null
            return try {
                BigDecimal(e.asString).longValueExact()
            } catch (_: ArithmeticException) {
                null
            } catch (_: NumberFormatException) {
                null
            }
        }
    }
}
