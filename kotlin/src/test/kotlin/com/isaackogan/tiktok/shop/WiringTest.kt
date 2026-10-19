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
        val ops = read("build/meta.json").getAsJsonArray("operations")
        assertEquals(320, ops.size())
        val byGroup = TikTokShop::class.memberProperties.associateBy { it.name }
        val methodsOf = HashMap<String, Set<String>>()
        for (el in ops) {
            val op = el.asJsonObject
            val group = op["group"].asString
            val prop = byGroup[group] ?: error("no property for group $group")
            val api = prop.returnType.classifier as kotlin.reflect.KClass<*>
            assertTrue(api.java.name.startsWith("com.isaackogan.tiktok.shop.generated.apis.") && api.java.name.endsWith("Api"), "$group returns the concrete generated API, got ${api.java.name}")
            val methods = methodsOf.getOrPut(group) { api.memberFunctions.map { it.name }.toSet() }
            assertTrue(op["operationId"].asString in methods, "${op["operationId"].asString} is a method of ${api.simpleName}")
        }
    }

    @Test
    fun metaMatchesTheSpec() {
        val ops = read("build/meta.json").getAsJsonArray("operations")
        assertEquals(ops.size(), Meta.OPERATIONS.size)
        assertEquals(233, Meta.OPERATIONS.count { it.requiresShopCipher })
        assertEquals(16, Meta.EVENT_TYPES.size)
    }
}
