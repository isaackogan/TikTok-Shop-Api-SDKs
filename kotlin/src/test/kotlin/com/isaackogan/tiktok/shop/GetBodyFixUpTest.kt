package com.isaackogan.tiktok.shop

import java.io.File
import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertFalse
import kotlin.test.assertTrue

/** The generator's own ApiClient drops a GET's body; scripts/generate.ts patches that one line (its tsx tests cover the patcher). */
class GetBodyFixUpTest {
    private val stockLine = "RequestMethod.GET -> Request.Builder().url(url)"
    private val rel = "src/main/kotlin/com/isaackogan/tiktok/shop/generated/infrastructure/ApiClient.kt"

    @Test
    fun theCommittedClientHasNoBodyDroppingGetLine() {
        val fixed = File(rel).readText()
        assertFalse(fixed.lines().any { it.trim() == stockLine }, "the stock GET line is gone")
        assertEquals(1, fixed.lines().count { it.contains("RequestMethod.GET ->") })
    }

    @Test
    fun theCommittedClientCarriesTheBodyAsATagOnTheGet() {
        val fixed = File(rel).readText()
        val line = fixed.lines().single { it.contains("RequestMethod.GET ->") }
        assertTrue(line.contains("tag(RequestBody::class.java, requestBody(requestConfig.body, contentType))"), line)
        assertTrue(line.contains("fix-up"), line)
    }
}
