package com.isaackogan.tiktok.shop

import java.io.File
import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertFalse
import kotlin.test.assertTrue

/** The generator's own ApiClient drops a GET's body; scripts/generate.ts patches that one line, and only that one. */
class GetBodyFixUpTest {
    private val stockLine = "RequestMethod.GET -> Request.Builder().url(url)"
    private val rel = "src/main/kotlin/com/isaackogan/tiktok/shop/generated/infrastructure/ApiClient.kt"

    @Test
    fun theStockGeneratorOutputBuildsAGetWithoutItsBody() {
        val stock = File("build/out/$rel").readText()
        assertEquals(1, stock.split(stockLine).size - 1, "the stock GET line appears exactly once")
        assertFalse(stock.contains("tag(RequestBody::class.java"), "the stock client never looks at the body")
    }

    @Test
    fun theCommittedClientCarriesTheBodyAsATagOnTheGet() {
        val fixed = File(rel).readText()
        val line = fixed.lines().single { it.contains("RequestMethod.GET ->") }
        assertTrue(line.contains("tag(RequestBody::class.java, requestBody(requestConfig.body, contentType))"), line)
        assertTrue(line.contains("fix-up"), line)
    }
}
