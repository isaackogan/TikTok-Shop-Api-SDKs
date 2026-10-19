package com.isaackogan.tiktok.shop

import com.isaackogan.tiktok.shop.generated.apis.AffiliateSellerApi
import com.isaackogan.tiktok.shop.generated.models.GetConversationListRequest
import com.isaackogan.tiktok.shop.generated.models.PredictProductPackageDimensionsAndWeightRequest
import java.io.File
import java.io.IOException
import java.net.InetSocketAddress
import java.net.Proxy
import java.net.ServerSocket
import java.net.URI
import java.time.Duration
import java.util.concurrent.TimeUnit
import kotlin.test.AfterTest
import kotlin.test.BeforeTest
import kotlin.test.Test
import kotlin.test.assertContains
import kotlin.test.assertEquals
import kotlin.test.assertFailsWith
import kotlin.test.assertFalse
import kotlin.test.assertIs
import kotlin.test.assertNotEquals
import kotlin.test.assertNotNull
import kotlin.test.assertNull
import kotlin.test.assertTrue
import mockwebserver3.MockResponse
import mockwebserver3.MockWebServer
import mockwebserver3.RecordedRequest
import mockwebserver3.SocketEffect
import okhttp3.OkHttpClient

class ClientStubTest {
    private val secret = "s3cret"
    lateinit var server: MockWebServer

    @BeforeTest
    fun start() {
        server = MockWebServer()
        server.start()
    }

    @AfterTest
    fun stop() = server.close()

    private fun options(base: String = server.url("/").toString()) =
        TikTokShopOptions(appKey = "key1", appSecret = secret, accessToken = "tok1", shopCipher = "cipher1", baseUrl = base)

    private fun client(base: String = server.url("/").toString()) = TikTokShop(options(base))

    private fun take(): RecordedRequest = assertNotNull(server.takeRequest(5, TimeUnit.SECONDS), "no request arrived")

    private fun reply(body: String) {
        server.enqueue(MockResponse.Builder().setHeader("Content-Type", "application/json").body(body).build())
    }

    private val onlyIds = GetConversationListRequest(onlyNeedConversationId = true)

    @Test
    fun getAuthorizedShopsIsSignedWithTokenAndNoShopCipher() {
        reply("""{"code":0,"message":"Success","request_id":"r1","data":{"shops":[{"id":"1","name":"n"}]}}""")
        val resp = client().authorization.getAuthorizedShops()
        assertEquals("1", resp.data!!.shops!![0].id)

        val r = take()
        assertEquals("GET", r.method)
        assertEquals("/authorization/202309/shops", r.url.encodedPath)
        assertEquals("key1", StubSupport.only(r, "app_key"))
        assertTrue(StubSupport.only(r, "timestamp").toLong() > 1_600_000_000L)
        assertFalse(StubSupport.queryMap(r.url).containsKey("shop_cipher"))
        assertEquals("tok1", r.headers["x-tts-access-token"])
        StubSupport.assertSigned(r, secret)
    }

    @Test
    fun getOrderListSendsShopCipher() {
        reply(StubSupport.OK)
        val resp = client().orders.getOrderList(20L)
        assertEquals(0L, resp.code)
        val r = take()
        assertEquals("cipher1", StubSupport.only(r, "shop_cipher"))
        assertEquals("20", StubSupport.only(r, "page_size"))
        StubSupport.assertSigned(r, secret)
    }

    @Test
    fun noTokenAndNoCipherSendsNeither() {
        reply(StubSupport.OK)
        TikTokShop(TikTokShopOptions(appKey = "key1", appSecret = secret, baseUrl = server.url("/").toString())).orders.getOrderList(1L)
        val r = take()
        assertNull(r.headers["x-tts-access-token"])
        assertFalse(StubSupport.queryMap(r.url).containsKey("shop_cipher"))
        StubSupport.assertSigned(r, secret)
    }

    @Test
    fun pageTokenWithPlusSlashEqualsRoundTrips() {
        reply(StubSupport.OK)
        val token = "b2Zmc2V0PTEw+/x=="
        client().orders.getOrderList(10L, pageToken = token)
        val r = take()
        assertEquals(token, StubSupport.only(r, "page_token"), "decoded value arrives intact")
        assertContains(r.target, "page_token=b2Zmc2V0PTEw%2B%2Fx%3D%3D")
        StubSupport.assertSigned(r, secret)
    }

    @Test
    fun getWithBodyIsSentAndSigned() {
        RawServer().use { raw ->
            client(raw.baseUrl()).affiliateSeller.getConversationList(10L, pageToken = "p+/=", getConversationListRequest = onlyIds)
            val r = raw.take()
            assertEquals("GET", r.method)
            assertEquals("""{"only_need_conversation_id":true}""", String(r.body, Charsets.UTF_8))
            assertEquals("p+/=", StubSupport.only(r, "page_token"))
            assertEquals("cipher1", StubSupport.only(r, "shop_cipher"))
            assertEquals("tok1", r.headers["x-tts-access-token"])
            assertTrue(r.headers.getValue("content-type").startsWith("application/json"))
            StubSupport.assertSigned(r, secret)
            // the signature covers the body: a signature over no body differs
            val noBody = Signer.sign(SignRequest(r.url().encodedPath, StubSupport.query(r.url()), null, null, secret))
            assertNotEquals(noBody, StubSupport.only(r, "sign"))
        }
    }

    @Test
    fun aGetWithABodyReachesTheInterceptorAsATagAndNothingElseWouldSendIt() {
        // The generated GET carries its body only as a tag (the fix-up in scripts/generate.ts): a plain OkHttpClient without
        // our interceptor sends no body, which is why the interceptor sends it.
        reply(StubSupport.OK)
        val api = AffiliateSellerApi(server.url("/").toString().trimEnd('/'), OkHttpClient())
        api.getConversationList(10L, getConversationListRequest = onlyIds)
        val r = take()
        assertEquals("GET", r.method)
        assertEquals(0, r.bodySize)
    }

    @Test
    fun getWithBodyFailuresBecomeTheSameException() {
        RawServer().use { raw ->
            raw.respond(500, """{"code":77,"message":"bad","request_id":"rq"}""")
            val e = assertFailsWith<TikTokShopException> { client(raw.baseUrl()).affiliateSeller.getConversationList(10L, getConversationListRequest = onlyIds) }
            assertEquals(77, e.code)
            assertEquals("rq", e.requestId)
            assertEquals(500, e.httpStatus)

            raw.respond(200, """{"code":5,"message":"nope","request_id":"r2"}""")
            val e2 = assertFailsWith<TikTokShopException> { client(raw.baseUrl()).affiliateSeller.getConversationList(10L, getConversationListRequest = onlyIds) }
            assertEquals(5, e2.code)
        }
        RawServer().hang().use { raw ->
            val c = TikTokShop(options(raw.baseUrl()).copy(timeout = Duration.ofMillis(300)))
            val t = assertFailsWith<TikTokShopException> { c.affiliateSeller.getConversationList(10L, getConversationListRequest = onlyIds) }
            assertIs<IOException>(t.cause)
            assertFalse(t.message!!.contains("?"), t.message)
        }
    }

    @Test
    fun codeNotZeroRaisesWithCodeMessageAndRequestId() {
        reply("""{"code":36009003,"message":"invalid","request_id":"r1","data":{}}""")
        val e = assertFailsWith<TikTokShopException> { client().authorization.getAuthorizedShops() }
        assertEquals(36009003, e.code)
        assertEquals("invalid", e.message)
        assertEquals("r1", e.requestId)
        assertEquals(200, e.httpStatus)
    }

    @Test
    fun non2xxRaisesWithStatusAndBodyFields() {
        server.enqueue(MockResponse.Builder().code(503).body("""{"code":99,"message":"down","request_id":"r5"}""").build())
        val e = assertFailsWith<TikTokShopException> { client().authorization.getAuthorizedShops() }
        assertEquals(99, e.code)
        assertEquals("down", e.message)
        assertEquals("r5", e.requestId)
        assertEquals(503, e.httpStatus)

        server.enqueue(MockResponse.Builder().code(502).body("<html>bad gateway</html>").build())
        val h = assertFailsWith<TikTokShopException> { client().authorization.getAuthorizedShops() }
        assertEquals(502, h.code)
        assertEquals(502, h.httpStatus)
    }

    @Test
    fun non2xxBodyWithNoCodeStillRaises() {
        server.enqueue(MockResponse.Builder().code(404).body("not json at all").build())
        assertEquals(404, assertFailsWith<TikTokShopException> { client().authorization.getAuthorizedShops() }.httpStatus)
    }

    @Test
    fun nonJson2xxRaises() {
        server.enqueue(MockResponse.Builder().body("<html>hello</html>").build())
        val e = assertFailsWith<TikTokShopException> { client().authorization.getAuthorizedShops() }
        assertEquals(200, e.httpStatus)
        assertContains(e.message!!, "not valid JSON")
    }

    @Test
    fun aJsonEnvelopeIsDecodedWhateverContentTypeItArrivesWith() {
        server.enqueue(MockResponse.Builder().setHeader("Content-Type", "text/plain").body(StubSupport.OK).build())
        assertEquals(0L, client().orders.getOrderList(1L).code)
    }

    @Test
    fun closedPortRaisesWithIoCauseAndNoQueryInMessage() {
        val port = ServerSocket(0).use { it.localPort }
        val e = assertFailsWith<TikTokShopException> { client("http://127.0.0.1:$port").authorization.getAuthorizedShops() }
        assertIs<IOException>(e.cause)
        assertFalse(e.message!!.contains("?") || e.message!!.contains("sign="), e.message)
    }

    @Test
    fun timeoutRaisesWithIoCause() {
        server.enqueue(MockResponse.Builder().onResponseStart(SocketEffect.Stall).build())
        val c = TikTokShop(options().copy(timeout = Duration.ofMillis(300)))
        val start = System.nanoTime()
        val e = assertFailsWith<TikTokShopException> { c.authorization.getAuthorizedShops() }
        assertIs<IOException>(e.cause)
        assertTrue(Duration.ofNanos(System.nanoTime() - start).seconds < 10)
        assertFalse(e.message!!.contains("?") || e.message!!.contains("sign="), e.message)
    }

    @Test
    fun reservedParamsOnTheOutgoingRequestAreReplacedByTheClientsValues() {
        reply(StubSupport.OK)
        val injecting = OkHttpClient.Builder().addInterceptor { chain ->
            val evil = chain.request().url.newBuilder()
                .addQueryParameter("app_key", "evil").addQueryParameter("sign", "x")
                .addQueryParameter("timestamp", "1").addQueryParameter("shop_cipher", "bad").build()
            chain.proceed(chain.request().newBuilder().url(evil).build())
        }.build()
        TikTokShop(options().copy(httpClient = injecting)).orders.getOrderList(5L)
        val r = take()
        assertEquals("key1", StubSupport.only(r, "app_key"))
        assertEquals("cipher1", StubSupport.only(r, "shop_cipher"))
        assertNotEquals("x", StubSupport.only(r, "sign"))
        assertNotEquals("1", StubSupport.only(r, "timestamp"))
        assertEquals("5", StubSupport.only(r, "page_size"))
        StubSupport.assertSigned(r, secret)
    }

    @Test
    fun multipartUploadIsSignedWithoutItsBody() {
        reply("""{"code":0,"message":"ok","request_id":"r","data":{"uri":"u"}}""")
        val f = File.createTempFile("img", ".png").apply { deleteOnExit() }
        f.writeBytes("FAKE-PNG-BYTES-\u0001\u0002".toByteArray(Charsets.UTF_8))

        client().products.uploadProductImage(f)
        val r = take()
        assertEquals("POST", r.method)
        val ct = r.headers["Content-Type"]!!
        assertTrue(ct.startsWith("multipart/form-data; boundary="), ct)
        val boundary = ct.substringAfter("boundary=")
        val body = r.body!!.utf8()
        assertTrue(body.startsWith("--$boundary"), "multipart body intact")
        assertContains(body, "FAKE-PNG-BYTES-")
        assertTrue(body.trim().endsWith("--$boundary--"))
        // signed as if there were no body, whatever the boundary
        val expected = Signer.sign(SignRequest(r.url.encodedPath, StubSupport.query(r.url), ct, null, secret))
        assertEquals(expected, StubSupport.only(r, "sign"))
        val withBody = Signer.sign(SignRequest(r.url.encodedPath, StubSupport.query(r.url), "application/json", body.toByteArray(), secret))
        assertNotEquals(withBody, expected)
    }

    @Test
    fun unknownFieldsAreAcceptedAtDataLevelAndInsideNestedModels() {
        reply(
            """{"code":0,"message":"ok","request_id":"r","brand_new":1,"data":{"extra_data":{"a":[1]},""" +
                """"shops":[{"id":"9","name":"n","region":"US","shiny":true}]}}""",
        )
        assertEquals("9", client().authorization.getAuthorizedShops().data!!.shops!![0].id)

        reply(
            """{"code":0,"message":"ok","request_id":"r","data":{"next_page_token":"t","zzz":"new",""" +
                """"orders":[{"id":"1","unknown_nested":{"x":1},"line_items":[{"id":"2","nope":1}]}]}}""",
        )
        val orders = client().orders.getOrderList(1L)
        assertEquals("t", orders.data!!.nextPageToken)
        assertEquals("1", orders.data!!.orders!![0].id)
    }

    @Test
    fun unknownFieldsInNestedModelsWithRequiredPropertiesStillDecode() {
        // PackageDimension requires height, length, unit, width; PackageWeight requires unit, value.
        reply(
            """{"code":0,"message":"ok","request_id":"r","data":{"surprise":1,""" +
                """"package_dimensions":{"height":3,"length":4,"width":5,"unit":"CENTIMETER","new_field":{"a":1}},""" +
                """"package_weight":{"value":"1.5","unit":"KILOGRAM","another":[1,2]}}}""",
        )
        val resp = client().products.predictProductPackageDimensionsAndWeight(PredictProductPackageDimensionsAndWeightRequest(categoryId = "1"))
        val d = resp.data!!.packageDimensions!!
        assertEquals(3L, d.height)
        assertEquals(4L, d.length)
        assertEquals(5L, d.width)
        assertEquals("CENTIMETER", d.unit.value)
        assertEquals("1.5", resp.data!!.packageWeight!!.value)
        assertEquals("KILOGRAM", resp.data!!.packageWeight!!.unit.value)
    }

    @Test
    fun getWithBodyTimeoutBoundsASlowDrippedBody() {
        RawServer().drip().use { raw ->
            val start = System.nanoTime()
            val c = TikTokShop(options(raw.baseUrl()).copy(timeout = Duration.ofMillis(700)))
            val e = assertFailsWith<TikTokShopException> { c.affiliateSeller.getConversationList(10L, getConversationListRequest = onlyIds) }
            assertIs<IOException>(e.cause)
            assertTrue(Duration.ofNanos(System.nanoTime() - start).seconds < 10)
        }
    }

    @Test
    fun getWithBodyHonoursAnExplicitHttpProxy() {
        RawServer().use { proxy ->
            val port = proxy.baseUrl().substringAfterLast(':').toInt()
            val viaProxy = OkHttpClient.Builder().proxy(Proxy(Proxy.Type.HTTP, InetSocketAddress("127.0.0.1", port))).build()
            val c = TikTokShop(TikTokShopOptions(appKey = "key1", appSecret = secret, baseUrl = "http://target.invalid", httpClient = viaProxy))
            assertEquals(Proxy.Type.HTTP, c.jdkClient.proxy().get().select(URI.create("http://target.invalid"))[0].type())
            c.affiliateSeller.getConversationList(10L, getConversationListRequest = onlyIds)
            val r = proxy.take()
            assertTrue(r.target.startsWith("http://target.invalid/"), r.target)
            assertEquals("""{"only_need_conversation_id":true}""", String(r.body, Charsets.UTF_8))
        }
    }
}
