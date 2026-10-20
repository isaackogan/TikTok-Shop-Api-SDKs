package com.isaackogan.tiktok.shop

import java.io.ByteArrayOutputStream
import javax.crypto.Mac
import javax.crypto.spec.SecretKeySpec

/** One query parameter with its decoded value, exactly as the server receives it. */
data class Param(val key: String, val value: String)

/** What the signature covers. */
class SignRequest(
    /** The request path, e.g. "/order/202309/orders/search". */
    val path: String,
    /** The query, with decoded values. */
    val query: List<Param>,
    /** The Content-Type header, or null. A multipart/form-data body is not signed. */
    val contentType: String?,
    /** The exact request body, or null. */
    val body: ByteArray?,
    val appSecret: String,
)

/**
 * TikTok Shop request signing: pure functions, no I/O.
 *
 * The string to sign is `secret + path + the sorted key+value pairs (without sign and access_token) + the body (unless the
 * body is multipart/form-data) + secret`. The signature is the lowercase hex HMAC-SHA256 of that string, keyed with the app
 * secret.
 */
object Signer {
    private val byKeyBytes = Comparator<Param> { a, b ->
        val x = a.key.toByteArray(Charsets.UTF_8)
        val y = b.key.toByteArray(Charsets.UTF_8)
        for (i in 0 until minOf(x.size, y.size)) {
            val d = (x[i].toInt() and 0xff) - (y[i].toInt() and 0xff)
            if (d != 0) return@Comparator d
        }
        x.size - y.size
    }

    internal fun isMultipart(contentType: String?): Boolean =
        contentType != null && contentType.lowercase().startsWith("multipart/form-data")

    private fun bytesToSign(r: SignRequest): ByteArray {
        val pairs = r.query.filter { it.key != "sign" && it.key != "access_token" }.sortedWith(byKeyBytes) // stable
        val out = ByteArrayOutputStream()
        fun write(s: String) = out.write(s.toByteArray(Charsets.UTF_8))
        write(r.appSecret)
        write(r.path)
        for (p in pairs) {
            write(p.key)
            write(p.value)
        }
        if (r.body != null && !isMultipart(r.contentType)) out.write(r.body)
        write(r.appSecret)
        return out.toByteArray()
    }

    /** The string the signature is computed over. */
    fun stringToSign(r: SignRequest): String = String(bytesToSign(r), Charsets.UTF_8)

    /** The signature: lowercase hex HMAC-SHA256 of [stringToSign], keyed with the app secret. */
    fun sign(r: SignRequest): String {
        val mac = Mac.getInstance("HmacSHA256")
        mac.init(SecretKeySpec(r.appSecret.toByteArray(Charsets.UTF_8), "HmacSHA256"))
        return mac.doFinal(bytesToSign(r)).joinToString("") { "%02x".format(it) }
    }
}
