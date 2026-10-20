package com.isaackogan.tiktok.shop

/**
 * Thrown for every failed call:
 *
 *  - an envelope with `code != 0`, even on HTTP 200: TikTok's code, with [httpStatus] set;
 *  - a non-2xx response ([httpStatus] is always set; [code] is TikTok's non-zero code from the body, or the HTTP status when the
 *    body has none, whatever the body is);
 *  - a 2xx response that cannot be understood ([code] is -1, [httpStatus] is set): a body that is not a JSON object, a `code`
 *    that is not an integer, a body gson cannot decode into its model (the gson exception is the [cause]), or a token reply
 *    with `code` 0 but no `data`;
 *  - a transport failure with no response at all: connection refused, DNS, TLS, timeout ([code] is -1, [cause] is the
 *    `IOException`, [httpStatus] is null).
 *
 * The message never contains the request URL or its query.
 */
class TikTokShopException(
    /** TikTok's error code. */
    val code: Int,
    message: String,
    /** TikTok's request_id, or an empty string when the response had none. */
    val requestId: String = "",
    /** The HTTP status, or null when no response arrived. */
    val httpStatus: Int? = null,
    cause: Throwable? = null,
) : RuntimeException(message, cause) {
    override fun toString(): String =
        buildString {
            append(this@TikTokShopException.javaClass.name).append(": ").append(message).append(" (code ").append(code)
            if (requestId.isNotEmpty()) append(", request_id ").append(requestId)
            append(')')
        }
}

/**
 * R13d: a 2xx body that gson cannot decode into its model. Called from the generated `ApiClient.responseBody` (an asserted
 * fix-up in `scripts/fix-decode.ts`); `@PublishedApi` because that function is a public inline one.
 */
@PublishedApi
internal fun decodeFailure(status: Int, body: String, cause: Throwable): TikTokShopException {
    val requestId =
        try {
            val el = com.google.gson.JsonParser.parseString(body)
            val r = if (el.isJsonObject) el.asJsonObject.get("request_id") else null
            if (r != null && r.isJsonPrimitive && r.asJsonPrimitive.isString) r.asString else ""
        } catch (_: RuntimeException) {
            ""
        }
    return TikTokShopException(-1, "response does not match its model: ${cause.javaClass.simpleName}: ${cause.message}", requestId, status, cause)
}
