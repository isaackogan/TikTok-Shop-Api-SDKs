package com.isaackogan.tiktok.shop

import com.google.gson.JsonParser
import java.nio.file.Files
import java.nio.file.Paths
import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertFalse
import kotlin.test.assertTrue

class SignerTest {
    @Test
    fun everySigningVector() {
        val raw = String(Files.readAllBytes(Paths.get("../shared/test-vectors/signing.json")), Charsets.UTF_8)
        val cases = JsonParser.parseString(raw).asJsonObject.getAsJsonArray("cases")
        assertTrue(cases.size() >= 6, "expected the shared vectors")
        for (el in cases) {
            val c = el.asJsonObject
            val query = c.getAsJsonArray("query").map { Param(it.asJsonArray[0].asString, it.asJsonArray[1].asString) }
            val contentType = if (c["contentType"].isJsonNull) null else c["contentType"].asString
            val body = if (c["body"].isJsonNull) null else c["body"].asString.toByteArray(Charsets.UTF_8)
            val req = SignRequest(c["path"].asString, query, contentType, body, c["secret"].asString)
            val name = c["name"].asString
            assertEquals(c["stringToSign"].asString, Signer.stringToSign(req), "$name: stringToSign")
            assertEquals(c["sign"].asString, Signer.sign(req), "$name: sign")
        }
    }

    @Test
    fun requiresShopCipherMatchesTheOperationTemplates() {
        assertTrue(requiresShopCipher("POST", "/order/202309/orders/search"))
        assertFalse(requiresShopCipher("GET", "/authorization/202309/shops"))
        assertTrue(requiresShopCipher("GET", "/product/202309/products/1729507467923261408"))
        assertTrue(requiresShopCipher("post", "/order/202309/orders/search"), "method is case-insensitive")
        assertFalse(requiresShopCipher("GET", "/nothing/here"))
    }
}
