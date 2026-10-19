package com.isaackogan.tiktok.shop

import java.util.concurrent.TimeUnit
import kotlin.test.AfterTest
import kotlin.test.BeforeTest
import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertFalse
import kotlin.test.assertNotNull
import kotlin.test.assertNotSame
import kotlin.test.assertNull
import mockwebserver3.MockResponse
import mockwebserver3.MockWebServer
import mockwebserver3.RecordedRequest

class WithShopTest {
    lateinit var server: MockWebServer
    lateinit var base: TikTokShop

    @BeforeTest
    fun start() {
        server = MockWebServer()
        server.start()
        base = TikTokShop(TikTokShopOptions(appKey = "k", appSecret = "s", accessToken = "t1", shopCipher = "c1", baseUrl = server.url("/").toString()))
    }

    @AfterTest
    fun stop() = server.close()

    private fun call(c: TikTokShop): RecordedRequest {
        server.enqueue(MockResponse.Builder().body(StubSupport.OK).build())
        c.orders.getOrderList(1L)
        return assertNotNull(server.takeRequest(5, TimeUnit.SECONDS))
    }

    @Test
    fun omittedValuesAreKept() {
        val other = base.withShop(accessToken = "t2")
        assertNotSame(base, other)
        val r = call(other)
        assertEquals("t2", r.headers["x-tts-access-token"])
        assertEquals("c1", StubSupport.only(r, "shop_cipher"))

        val r2 = call(base.withShop(shopCipher = "c9"))
        assertEquals("t1", r2.headers["x-tts-access-token"])
        assertEquals("c9", StubSupport.only(r2, "shop_cipher"))
    }

    @Test
    fun valuesAreReplaced() {
        val r = call(base.withShop(accessToken = "t2", shopCipher = "c2"))
        assertEquals("t2", r.headers["x-tts-access-token"])
        assertEquals("c2", StubSupport.only(r, "shop_cipher"))
        StubSupport.assertSigned(r, "s")
    }

    @Test
    fun explicitNullOrEmptyClears() {
        val r = call(base.withShop(shopCipher = null))
        assertFalse(StubSupport.queryMap(r.url).containsKey("shop_cipher"))
        assertEquals("t1", r.headers["x-tts-access-token"])

        val r2 = call(base.withShop(accessToken = ""))
        assertNull(r2.headers["x-tts-access-token"])
        assertEquals("c1", StubSupport.only(r2, "shop_cipher"))

        val r3 = call(base.withShop(accessToken = null, shopCipher = null))
        assertNull(r3.headers["x-tts-access-token"])
        assertFalse(StubSupport.queryMap(r3.url).containsKey("shop_cipher"))
    }

    @Test
    fun theOriginalIsUnchanged() {
        base.withShop(accessToken = "t2", shopCipher = "c2")
        base.withShop(accessToken = null, shopCipher = null)
        val r = call(base)
        assertEquals("t1", r.headers["x-tts-access-token"])
        assertEquals("c1", StubSupport.only(r, "shop_cipher"))
    }
}
