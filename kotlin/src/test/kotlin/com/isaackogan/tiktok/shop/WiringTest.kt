package com.isaackogan.tiktok.shop

import com.google.gson.JsonObject
import com.google.gson.JsonParser
import com.isaackogan.tiktok.shop.generated.Meta
import java.nio.file.Files
import java.nio.file.Paths
import kotlin.reflect.full.memberFunctions
import kotlin.reflect.full.memberProperties
import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertTrue

class WiringTest {
    private val groups = listOf(
        "affiliateCreator", "affiliatePartner", "affiliateSeller", "analytics", "authorization", "customerEngagement",
        "customerService", "event", "finance", "fulfilledByTikTok", "fulfillment", "logistics", "orders", "products",
        "promotion", "returnAndRefund", "seller", "supplyChain", "tools",
    )

    private fun read(path: String): JsonObject = JsonParser.parseString(String(Files.readAllBytes(Paths.get(path)), Charsets.UTF_8)).asJsonObject

    @Test
    fun groupNamesAreTheCanonicalList() {
        // shared/api-groups.json is the source of truth
        val shared = read("../shared/api-groups.json").entrySet().map { it.value.asString }
        assertEquals(groups.sorted(), shared.sorted())
        val props = TikTokShop::class.java.declaredMethods
            .filter { java.lang.reflect.Modifier.isPublic(it.modifiers) && it.parameterCount == 0 && it.returnType.name.startsWith("com.isaackogan.tiktok.shop.generated.apis.") }
            .map { it.name.removePrefix("get").replaceFirstChar { c -> c.lowercase() } }
        assertEquals(groups.sorted(), props.sorted())
    }

    @Test
    fun everyOperationIsAMethodOnItsGroupsConcreteApiClass() {
        // Meta is generated from the spec and committed, so this needs no build output.
        assertTrue(Meta.OPERATIONS.isNotEmpty())
        val byGroup = TikTokShop::class.memberProperties.associateBy { it.name }
        val methodsOf = HashMap<String, Set<String>>()
        for (op in Meta.OPERATIONS) {
            val prop = byGroup[op.group] ?: error("no property for group ${op.group}")
            val api = prop.returnType.classifier as kotlin.reflect.KClass<*>
            assertTrue(api.java.name.startsWith("com.isaackogan.tiktok.shop.generated.apis.") && api.java.name.endsWith("Api"), "${op.group} returns the concrete generated API, got ${api.java.name}")
            assertEquals(op.apiClass, api.simpleName, "${op.group} is the class Meta names")
            val methods = methodsOf.getOrPut(op.group) { api.memberFunctions.map { it.name }.toSet() }
            assertTrue(op.operationId in methods, "${op.operationId} is a method of ${api.simpleName}")
        }
        assertEquals(groups.sorted(), Meta.OPERATIONS.map { it.group }.distinct().sorted())
        assertEquals(groups.sorted(), Meta.GROUPS.map { it.name }.sorted())
    }

    @Test
    fun metaIsInternallyConsistent() {
        assertTrue(Meta.OPERATIONS.any { it.requiresShopCipher } && Meta.OPERATIONS.any { !it.requiresShopCipher })
        assertEquals(Meta.OPERATIONS.size, Meta.OPERATIONS.map { it.operationId }.toSet().size, "operation ids are unique")
        assertTrue(Meta.EVENT_TYPES.isNotEmpty())
        assertEquals(Meta.WEBHOOKS.mapNotNull { w -> w.eventType?.let { w.type to it } }.toMap(), Meta.EVENT_TYPES)
        // the matcher agrees with Meta for every operation that has no path parameter
        for (op in Meta.OPERATIONS.filter { !it.path.contains('{') }) {
            assertEquals(op.requiresShopCipher, requiresShopCipher(op.method, op.path), op.operationId)
        }
    }
}
