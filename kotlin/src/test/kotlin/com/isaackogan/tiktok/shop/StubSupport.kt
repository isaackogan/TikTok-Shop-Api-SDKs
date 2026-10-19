package com.isaackogan.tiktok.shop

import kotlin.test.assertEquals
import mockwebserver3.RecordedRequest
import okhttp3.HttpUrl

/** Helpers shared by the stub-server tests. */
object StubSupport {
    const val OK = """{"code":0,"message":"Success","request_id":"r0","data":{}}"""

    /** The decoded query pairs of a received request, in arrival order. */
    fun query(url: HttpUrl): List<Param> =
        (0 until url.querySize).map { Param(url.queryParameterName(it), url.queryParameterValue(it) ?: "") }

    fun queryMap(url: HttpUrl): Map<String, List<String>> = query(url).groupBy({ it.key }, { it.value })

    fun only(url: HttpUrl, key: String): String {
        val v = queryMap(url)[key]
        check(v != null && v.size == 1) { "$key should appear exactly once, got $v" }
        return v[0]
    }

    fun only(r: RecordedRequest, key: String): String = only(r.url, key)

    fun only(r: RawServer.Received, key: String): String = only(r.url(), key)

    /** The signature the server would compute for what it received. */
    fun expectedSign(r: RecordedRequest, secret: String): String {
        val body = r.body?.toByteArray() ?: ByteArray(0)
        return Signer.sign(SignRequest(r.url.encodedPath, query(r.url), r.headers["Content-Type"], body.takeIf { it.isNotEmpty() }, secret))
    }

    fun expectedSign(r: RawServer.Received, secret: String): String =
        Signer.sign(SignRequest(r.url().encodedPath, query(r.url()), r.headers["content-type"], r.body.takeIf { it.isNotEmpty() }, secret))

    fun assertSigned(r: RecordedRequest, secret: String) =
        assertEquals(expectedSign(r, secret), only(r, "sign"), "sign matches what was received")

    fun assertSigned(r: RawServer.Received, secret: String) =
        assertEquals(expectedSign(r, secret), only(r, "sign"), "sign matches what was received")
}
