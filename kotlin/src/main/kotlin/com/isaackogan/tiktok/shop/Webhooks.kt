package com.isaackogan.tiktok.shop

import com.google.gson.JsonArray
import com.google.gson.JsonElement
import com.google.gson.JsonObject
import com.google.gson.JsonParser
import com.google.gson.JsonPrimitive
import com.isaackogan.tiktok.shop.generated.Meta
import com.isaackogan.tiktok.shop.generated.WebhookRequired
import java.security.MessageDigest
import javax.crypto.Mac
import javax.crypto.spec.SecretKeySpec

/** Verifies and parses TikTok Shop webhooks. */
object Webhooks {
    /** Webhook type to event name, e.g. 1 to `ORDER_STATUS_CHANGE`. */
    @JvmField
    val EVENT_TYPES: Map<Int, String> = Meta.EVENT_TYPES

    /**
     * Checks the `Authorization` header: lowercase hex HMAC-SHA256 (key: the app secret) over `appKey + rawBody`, compared in
     * constant time. A null or empty signature is false.
     *
     * @param rawBody the body exactly as received. Never re-serialize it.
     */
    fun verify(appKey: String, appSecret: String, rawBody: ByteArray, signature: String?): Boolean {
        if (signature.isNullOrEmpty()) return false
        val mac = Mac.getInstance("HmacSHA256")
        mac.init(SecretKeySpec(appSecret.toByteArray(Charsets.UTF_8), "HmacSHA256"))
        mac.update(appKey.toByteArray(Charsets.UTF_8))
        mac.update(rawBody)
        val expected = mac.doFinal().joinToString("") { "%02x".format(it) }.toByteArray(Charsets.UTF_8)
        return MessageDigest.isEqual(expected, signature.toByteArray(Charsets.UTF_8))
    }

    /** As [verify], with the body as a string (its UTF-8 bytes are signed). */
    fun verify(appKey: String, appSecret: String, rawBody: String, signature: String?): Boolean =
        verify(appKey, appSecret, rawBody.toByteArray(Charsets.UTF_8), signature)

    /**
     * Parses a body to its event, picked by the integer `type`. A `type` this SDK does not know gives a [WebhookEvent.Unknown].
     * 64-bit IDs keep their exact digits, and unknown fields are accepted.
     *
     * @throws IllegalArgumentException if the body is not a JSON object, its `type` is missing or not an integer (a string,
     *     boolean, null, fraction, or outside the int range), or the body does not fit its model (a required property is missing)
     */
    fun parse(rawBody: ByteArray): WebhookEvent = parse(String(rawBody, Charsets.UTF_8))

    /** As [parse]. */
    fun parse(rawBody: String): WebhookEvent {
        val json: JsonElement =
            try {
                JsonParser.parseString(rawBody)
            } catch (e: RuntimeException) {
                throw IllegalArgumentException("webhook body is not valid JSON", e)
            }
        require(json.isJsonObject) { "webhook body is not a JSON object" }
        val obj = json.asJsonObject
        val type = typeOf(obj["type"])
        val event =
            try {
                webhookEventOf(type, obj)
            } catch (e: RuntimeException) {
                throw IllegalArgumentException("webhook of type $type does not match its model: ${e.message}", e)
            }
        if (event == null) return WebhookEvent.Unknown(type, obj)
        val missing = firstMissing(SCHEMAS.getValue(type), obj, "")
        require(missing == null) { "webhook of type $type does not match its model: required property \"$missing\" is missing" }
        return event
    }

    /**
     * Verifies, then parses.
     *
     * @throws WebhookSignatureException if the signature does not match
     */
    fun verifyAndParse(appKey: String, appSecret: String, rawBody: ByteArray, signature: String?): WebhookEvent {
        if (!verify(appKey, appSecret, rawBody, signature)) throw WebhookSignatureException()
        return parse(rawBody)
    }

    /** As [verifyAndParse]. */
    fun verifyAndParse(appKey: String, appSecret: String, rawBody: String, signature: String?): WebhookEvent =
        verifyAndParse(appKey, appSecret, rawBody.toByteArray(Charsets.UTF_8), signature)

    private fun typeOf(t: JsonElement?): Int {
        require(t is JsonPrimitive && t.isNumber) { "webhook \"type\" is missing or not an integer" }
        val digits = t.asString
        require(Regex("-?\\d+").matches(digits)) { "webhook \"type\" is not an integer: $digits" }
        return digits.toIntOrNull() ?: throw IllegalArgumentException("webhook \"type\" is out of range: $digits")
    }

    private val SCHEMAS: Map<Int, String> = Meta.WEBHOOKS.associate { it.type to it.schema }

    /**
     * gson builds a model without running its constructor, so a required (non-null) property the body lacks stays null, or 0 or
     * false for a primitive, and would surface later in the caller's code as a wrong value. Presence is therefore checked on the
     * parsed JSON, where a missing key and a JSON null both count as missing. Returns the first missing property as a JSON path,
     * or null.
     */
    private fun firstMissing(model: String, json: JsonObject, path: String): String? {
        val m = WebhookRequired.MODELS[model] ?: return null
        for (name in m.required) {
            val v = json[name]
            if (v == null || v.isJsonNull) return path + name
        }
        for ((name, child) in m.children) {
            val v = json[name] ?: continue
            val found = when (child.kind) {
                WebhookRequired.Kind.OBJECT -> (v as? JsonObject)?.let { firstMissing(child.model, it, "$path$name.") }
                WebhookRequired.Kind.LIST -> (v as? JsonArray)?.firstNotNullOfOrNull { (it as? JsonObject)?.let { o -> firstMissing(child.model, o, "$path$name.") } }
                WebhookRequired.Kind.MAP -> (v as? JsonObject)?.entrySet()?.firstNotNullOfOrNull { (_, e) -> (e as? JsonObject)?.let { o -> firstMissing(child.model, o, "$path$name.") } }
            }
            if (found != null) return found
        }
        return null
    }
}
