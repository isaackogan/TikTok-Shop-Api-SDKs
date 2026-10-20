package com.isaackogan.tiktok.shop

import com.google.gson.JsonParser
import com.isaackogan.tiktok.shop.generated.Meta
import java.nio.file.Files
import java.nio.file.Paths
import javax.crypto.Mac
import javax.crypto.spec.SecretKeySpec
import kotlin.reflect.full.primaryConstructor
import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertFailsWith
import kotlin.test.assertFalse
import kotlin.test.assertIs
import kotlin.test.assertNotNull
import kotlin.test.assertTrue

class WebhooksTest {
    private fun vectors() =
        JsonParser.parseString(String(Files.readAllBytes(Paths.get("../shared/test-vectors/webhooks.json")), Charsets.UTF_8)).asJsonObject

    private fun sign(appKey: String, secret: String, body: ByteArray): String {
        val mac = Mac.getInstance("HmacSHA256")
        mac.init(SecretKeySpec(secret.toByteArray(), "HmacSHA256"))
        mac.update(appKey.toByteArray())
        mac.update(body)
        return mac.doFinal().joinToString("") { "%02x".format(it) }
    }

    @Test
    fun everyVerifyVector() {
        val cases = vectors().getAsJsonArray("verify")
        assertTrue(cases.size() >= 5)
        for (el in cases) {
            val c = el.asJsonObject
            val name = c["name"].asString
            val body = c["rawBody"].asString
            val expected = c["valid"].asBoolean
            val key = c["appKey"].asString
            val secret = c["appSecret"].asString
            val sig = c["signature"].asString
            assertEquals(expected, Webhooks.verify(key, secret, body, sig), "$name (String)")
            assertEquals(expected, Webhooks.verify(key, secret, body.toByteArray(), sig), "$name (bytes)")
            if (!expected) assertFailsWith<WebhookSignatureException>(name) { Webhooks.verifyAndParse(key, secret, body, sig) }
        }
    }

    @Test
    fun nullSignatureIsFalseNotAnException() {
        assertFalse(Webhooks.verify("k", "s", "{}", null))
        assertFalse(Webhooks.verify("k", "s", "{}", ""))
    }

    @Test
    fun everyParseVector() {
        for (el in vectors().getAsJsonArray("parse")) {
            val c = el.asJsonObject
            val e = Webhooks.parse(c["rawBody"].asString)
            assertEquals(c["type"].asInt, e.type, c["name"].asString)
            if (c["known"].asBoolean) {
                assertFalse(e is WebhookEvent.Unknown)
                val payload = e.javaClass.getMethod("getPayload").returnType.simpleName
                assertEquals(c["schema"].asString, payload, c["name"].asString)
            } else {
                assertIs<WebhookEvent.Unknown>(e)
                assertEquals(9999, e.raw["type"].asInt)
            }
        }
    }

    @Test
    fun narrowsWithWhenToTheConcreteType() {
        val body = """{"type":1,"tts_notification_id":"7380066284010030890","shop_id":"7495540735365777507","timestamp":1718305585,"data":{"is_on_hold_order":true,"order_id":"576653688135258178","order_status":"UNPAID","update_time":1718305585}}"""
        val e = Webhooks.parse(body)
        val id = when (e) {
            is WebhookEvent.OrderStatusChange -> e.payload.data?.orderId
            is WebhookEvent.Unknown -> "unknown"
            else -> "other"
        }
        assertEquals("576653688135258178", id)
        assertEquals(1718305585L, (e as WebhookEvent.OrderStatusChange).payload.timestamp)
        assertEquals(1, e.raw["type"].asInt, "raw is kept")
    }

    @Test
    fun aNineteenDigitShopIdSentAsANumberKeepsItsValue() {
        val body = """{"type":1,"shop_id":7494049642642441621,"tts_notification_id":7380066284010030890,"timestamp":1718305585,"data":{"order_id":576653688135258178,"order_status":"UNPAID"}}"""
        val w = (Webhooks.parse(body) as WebhookEvent.OrderStatusChange).payload
        assertEquals("7494049642642441621", w.shopId)
        assertEquals("7380066284010030890", w.ttsNotificationId)
        assertEquals("576653688135258178", w.data?.orderId)
    }

    @Test
    fun unknownFieldsStillParse() {
        val body = """{"type":1,"shop_id":"1","brand_new":{"x":1},"data":{"order_id":"5","order_status":"UNPAID","extra":[1]}}"""
        assertEquals("5", (Webhooks.parse(body) as WebhookEvent.OrderStatusChange).payload.data?.orderId)
    }

    @Test
    fun missingOrNonIntegerTypeIsRejected() {
        for (body in listOf("{}", """{"type":null}""", """{"type":"1"}""", """{"type":true}""", """{"type":1.5}""", """{"type":1.0}""", """{"type":[1]}""", """{"type":99999999999}""", "[1]", "\"x\"", "null", "not json", "")) {
            val ex = assertFailsWith<IllegalArgumentException>(body) { Webhooks.parse(body) }
            assertNotNull(ex.message)
        }
    }

    @Test
    fun anIllTypedKnownPayloadIsRejectedClearly() {
        assertFailsWith<IllegalArgumentException> { Webhooks.parse("""{"type":1,"data":"nope"}""") }
    }

    @Test
    fun aKnownTypeMissingARequiredFieldIsRejectedClearly() {
        // WebhookRequired says which properties are non-null; gson would otherwise leave them null.
        val ex = assertFailsWith<IllegalArgumentException> { Webhooks.parse("""{"type":66,"shop_id":"1"}""") }
        assertTrue(ex.message!!.contains("type 66"), ex.message)
        assertTrue(ex.message!!.contains("missing"), ex.message)
    }

    @Test
    fun aMissingRequiredFieldInsideANestedModelIsRejectedToo() {
        val type = Meta.WEBHOOKS.single { it.schema == "AppealCompletedWebhook" }.type
        val whole = """{"type":$type,"shop_id":"1","tts_notification_id":"2","timestamp":3,"data":{"product_id":"5","appeal_task":{"appeal_audit_result":[{"indicator_type":"X","status":"Y"}]}}}"""
        val ok = Webhooks.parse(whole)
        assertEquals(type, ok.type)
        val ex = assertFailsWith<IllegalArgumentException> {
            Webhooks.parse("""{"type":$type,"shop_id":"1","tts_notification_id":"2","timestamp":3,"data":{"product_id":"5","appeal_task":{}}}""")
        }
        assertTrue(ex.message!!.contains("data.appeal_task.appeal_audit_result"), ex.message)
        val inList = assertFailsWith<IllegalArgumentException> {
            Webhooks.parse("""{"type":$type,"shop_id":"1","tts_notification_id":"2","timestamp":3,"data":{"product_id":"5","appeal_task":{"appeal_audit_result":[{"status":"Y"}]}}}""")
        }
        assertTrue(inList.message!!.contains("data.appeal_task.appeal_audit_result.indicator_type"), inList.message)
    }

    // type 71: required Long properties at the top level, in a nested object and inside a list element.
    private val inventory = """{"type":71,"tts_notification_id":"1","shop_id":"2","timestamp":3,"data":{"event_id":"e","occurred_at":"2025-01-01T00:00:00Z","shop_id":4,"product_id":5,"sku_id":6,
        "quantity_snapshot_after_change":{"total_quantity":1,"total_available_quantity":1,"total_committed_quantity":1,"in_shop_quantity":1,"campaign_locked_quantity":1,"creator_locked_quantity":1},
        "change_detail":[{"idempotency_key":"k","trigger_source":"s","occurred_at":"2025-01-01T00:00:00Z","total_quantity_delta":1,"available_quantity_delta":1,"committed_quantity_delta":1,"in_shop_quantity_delta":1,"campaign_locked_quantity_delta":1,"creator_locked_quantity_delta":1}]}}"""

    private fun without(vararg path: String): String {
        val root = JsonParser.parseString(inventory).asJsonObject
        var o: com.google.gson.JsonElement = root
        for (key in path.dropLast(1)) o = if (key == "[0]") o.asJsonArray[0] else o.asJsonObject[key]
        o.asJsonObject.remove(path.last())
        return root.toString()
    }

    @Test
    fun aMissingRequiredPrimitiveIsRejectedNotReadAsZero() {
        assertEquals(71, Webhooks.parse(inventory).type)
        val cases = mapOf(
            arrayOf("timestamp") to "timestamp",
            arrayOf("data", "shop_id") to "data.shop_id",
            arrayOf("data", "quantity_snapshot_after_change", "in_shop_quantity") to "data.quantity_snapshot_after_change.in_shop_quantity",
            arrayOf("data", "change_detail", "[0]", "total_quantity_delta") to "data.change_detail.total_quantity_delta",
        )
        for ((path, expected) in cases) {
            val ex = assertFailsWith<IllegalArgumentException>(expected) { Webhooks.parse(without(*path)) }
            assertTrue(ex.message!!.contains("\"$expected\""), ex.message)
        }
    }

    @Test
    fun aJsonNullInARequiredPropertyCountsAsMissing() {
        val body = inventory.replace("\"timestamp\":3", "\"timestamp\":null")
        assertTrue(assertFailsWith<IllegalArgumentException> { Webhooks.parse(body) }.message!!.contains("\"timestamp\""))
    }

    @Test
    fun theSealedBasePayloadIsTheTypedModel() {
        val e = Webhooks.parse(inventory)
        assertIs<com.isaackogan.tiktok.shop.generated.models.InventoryChangedByShopWebhook>(e.payload)
    }

    @Test
    fun verifyAndParseRoundTripsWithBytesAsReceived() {
        val body = "{ \"type\" : 9999 ,\n \"data\": {} }".toByteArray()
        val sig = sign("key", "secret", body)
        assertIs<WebhookEvent.Unknown>(Webhooks.verifyAndParse("key", "secret", body, sig))
        assertFailsWith<WebhookSignatureException> { Webhooks.verifyAndParse("key", "secret", "{\"type\":9999,\"data\":{}}".toByteArray(), sig) }
    }

    @Test
    fun nonAsciiBodiesVerifyByTheirBytes() {
        val body = "{\"type\":9999,\"name\":\"café ☃\"}".toByteArray()
        val sig = sign("k", "s", body)
        assertTrue(Webhooks.verify("k", "s", body, sig))
        assertTrue(Webhooks.verify("k", "s", String(body, Charsets.UTF_8), sig))
    }

    @Test
    fun eventTypesAreExposedFromTheCommittedMeta() {
        assertEquals("ORDER_STATUS_CHANGE", Webhooks.EVENT_TYPES[1])
        assertEquals(Meta.EVENT_TYPES, Webhooks.EVENT_TYPES)
        assertTrue(Webhooks.EVENT_TYPES.isNotEmpty())
    }

    @Test
    fun everyMetaWebhookHasASealedSubclassWiredToItsTypeAndModel() {
        val subs = WebhookEvent::class.sealedSubclasses
        assertEquals(Meta.WEBHOOKS.size + 1, subs.size, "one subclass per webhook, plus Unknown")
        for (w in Meta.WEBHOOKS) {
            val cls = subs.single { it.simpleName == w.schema.removeSuffix("Webhook") }
            assertEquals(w.type, cls.java.getField("TYPE").getInt(null), w.schema)
            assertEquals(w.schema, cls.primaryConstructor!!.parameters[0].type.toString().substringAfterLast('.'))
            // Dispatch reaches that model: a bare body either parses to the event, or the model rejects it for a missing field.
            try {
                assertEquals(cls, Webhooks.parse("""{"type":${w.type}}""")::class, w.schema)
            } catch (e: IllegalArgumentException) {
                assertTrue(e.message!!.startsWith("webhook of type ${w.type} does not match its model"), e.message)
            }
        }
    }
}
