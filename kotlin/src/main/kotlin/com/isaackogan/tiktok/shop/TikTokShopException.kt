package com.isaackogan.tiktok.shop

/**
 * Thrown for every failed call:
 *
 *  - an envelope with `code != 0`, even on HTTP 200;
 *  - a non-2xx response ([httpStatus] is always set; [code] is TikTok's non-zero code from the body, or the HTTP status when the
 *    body has none, whatever the body is);
 *  - a 2xx response that cannot be understood, i.e. whose body is not a JSON object ([code] is -1; a token reply with `code` 0 but
 *    no `data` is -1 too);
 *  - a network error or timeout ([cause] is the `IOException`, [httpStatus] is null).
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
            append(javaClass.name).append(": ").append(message).append(" (code ").append(code)
            if (requestId.isNotEmpty()) append(", request_id ").append(requestId)
            append(')')
        }
}
