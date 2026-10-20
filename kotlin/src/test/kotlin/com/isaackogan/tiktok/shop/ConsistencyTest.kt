package com.isaackogan.tiktok.shop

import com.isaackogan.tiktok.shop.generated.models.GetConversationListRequest
import com.isaackogan.tiktok.shop.generated.models.PredictProductPackageDimensionsAndWeightRequest
import java.io.File
import java.io.IOException
import java.net.InetSocketAddress
import java.net.Proxy
import java.net.ServerSocket
import java.time.Duration
import java.util.concurrent.TimeUnit
import kotlin.test.AfterTest
import kotlin.test.BeforeTest
import kotlin.test.Test
import kotlin.test.assertContains
import kotlin.test.assertEquals
import kotlin.test.assertFailsWith
import kotlin.test.assertIs
import kotlin.test.assertNotNull
import kotlin.test.assertNull
import mockwebserver3.MockResponse
import mockwebserver3.MockWebServer
import mockwebserver3.SocketEffect
import okhttp3.OkHttpClient

/** Cross-language rules from the final review: R13c, R13d, R21b, lesson 34 and M22. */
class ConsistencyTest {
    lateinit var server: MockWebServer

    @BeforeTest
    fun start() {
        server = MockWebServer()
        server.start()
    }

    @AfterTest
    fun stop() = server.close()

    private fun client(base: String = server.url("/").toString(), timeout: Duration? = null, http: OkHttpClient? = null) =
        TikTokShop(TikTokShopOptions(appKey = "k", appSecret = "s", accessToken = "t", baseUrl = base, timeout = timeout, httpClient = http))

    private fun auth(timeout: Duration? = null) = TikTokShopAuth(TikTokShopAuthOptions(appKey = "k", appSecret = "s", baseUrl = server.url("/").toString(), timeout = timeout))

    private fun reply(body: String) {
        server.enqueue(MockResponse.Builder().setHeader("Content-Type", "application/json").body(body).build())
    }

    private fun closedPort(): String = ServerSocket(0).use { "http://127.0.0.1:${it.localPort}" }

    private fun assertTransportFailure(e: TikTokShopException) {
        assertEquals(-1, e.code, e.toString())
        assertNull(e.httpStatus)
        assertIs<IOException>(e.cause)
    }

    private val onlyIds = GetConversationListRequest(onlyNeedConversationId = true)
    private val tok = """"access_token":"a","access_token_expire_in":1,"refresh_token":"r","refresh_token_expire_in":2"""

    // --- R13c ---------------------------------------------------------------------------------------------------------

    @Test
    fun anApiCallToAClosedPortIsMinusOneWithNoStatus() {
        val c = client(closedPort())
        assertTransportFailure(assertFailsWith<TikTokShopException> { c.authorization.getAuthorizedShops() })
        assertTransportFailure(assertFailsWith<TikTokShopException> { c.affiliateSeller.getConversationList(10L, getConversationListRequest = onlyIds) })
    }

    @Test
    fun anApiCallTimeoutIsMinusOneWithNoStatus() {
        server.enqueue(MockResponse.Builder().onResponseStart(SocketEffect.Stall).build())
        assertTransportFailure(assertFailsWith<TikTokShopException> { client(timeout = Duration.ofMillis(300)).authorization.getAuthorizedShops() })
    }

    @Test
    fun aTokenCallTimeoutIsMinusOneWithNoStatus() {
        server.enqueue(MockResponse.Builder().onResponseStart(SocketEffect.Stall).build())
        assertTransportFailure(assertFailsWith<TikTokShopException> { auth(Duration.ofMillis(300)).exchangeCode("c") })
    }

    // --- R13d ---------------------------------------------------------------------------------------------------------

    @Test
    fun aWrongTypedFieldIsMinusOneWithStatusRequestIdAndCause() {
        reply("""{"code":0,"message":"Success","request_id":"q9","data":{"shops":"not a list"}}""")
        val e = assertFailsWith<TikTokShopException> { client().authorization.getAuthorizedShops() }
        assertEquals(-1, e.code)
        assertEquals(200, e.httpStatus)
        assertEquals("q9", e.requestId)
        assertNotNull(e.cause)
    }

    @Test
    fun aWrongTypedNestedFieldIsMinusOneToo() {
        reply("""{"code":0,"request_id":"q10","data":{"package_weight":{"unit":["GRAM"],"value":"1"}}}""")
        val e = assertFailsWith<TikTokShopException> {
            client().products.predictProductPackageDimensionsAndWeight(PredictProductPackageDimensionsAndWeightRequest(categoryId = "1"))
        }
        assertEquals(-1, e.code)
        assertEquals("q10", e.requestId)
    }

    // --- lesson 34 ------------------------------------------------------------------------------------------------------

    @Test
    fun aNonIntegerCodeOnA2xxIsMinusOne() {
        for (code in listOf("\"0\"", "1.5", "true", "null", "{}")) {
            reply("""{"code":$code,"message":"m","request_id":"q5","data":{}}""")
            val e = assertFailsWith<TikTokShopException>(code) { client().authorization.getAuthorizedShops() }
            assertEquals(-1, e.code, code)
            assertEquals(200, e.httpStatus, code)
            assertEquals("q5", e.requestId, code)
            reply("""{"code":$code,"request_id":"q6","data":{$tok}}""")
            val t = assertFailsWith<TikTokShopException>(code) { auth().exchangeCode("c") }
            assertEquals(-1, t.code, code)
            assertEquals(200, t.httpStatus, code)
        }
        reply("""{"request_id":"q","data":{}}""")
        assertNotNull(client().authorization.getAuthorizedShops(), "no code at all is a success")
    }

    @Test
    fun theUserAgentIsSentOnApiAndTokenCalls() {
        val version = Regex("""(?m)^version\s*=\s*"([^"]+)"""").find(File("build.gradle.kts").readText())!!.groupValues[1]
        val ua = "tiktok-shop-api-kotlin/$version"
        reply("""{"code":0,"request_id":"r","data":{}}""")
        client().authorization.getAuthorizedShops()
        assertEquals(ua, server.takeRequest(5, TimeUnit.SECONDS)!!.headers["User-Agent"])
        reply("""{"code":0,"request_id":"r","data":{$tok}}""")
        auth().refresh("r")
        assertEquals(ua, server.takeRequest(5, TimeUnit.SECONDS)!!.headers["User-Agent"])
    }

    @Test
    fun grantedScopesAbsentNullOrIllTypedIsNull() {
        for (extra in listOf("", ""","granted_scopes":null""", ""","granted_scopes":"x"""", ""","granted_scopes":["a",1]""")) {
            reply("""{"code":0,"request_id":"r","data":{$tok$extra}}""")
            assertNull(auth().exchangeCode("c").grantedScopes, extra)
        }
        reply("""{"code":0,"request_id":"r","data":{$tok,"granted_scopes":["a","b"]}}""")
        assertEquals(listOf("a", "b"), auth().exchangeCode("c").grantedScopes)
    }

    // --- R21b -----------------------------------------------------------------------------------------------------------

    @Test
    fun anIntegerEnumValueTheSpecDoesNotListStillDecodes() {
        reply("""{"code":0,"request_id":"r","data":{"creators":[{"creator_profile":{"user_type_tag":[1,3]}}]}}""")
        val r = client().affiliateSeller.searchCreatorsInCreatorMarketplace(1L)
        assertEquals<List<Any?>?>(listOf(1L, 3L), r.data?.creators?.get(0)?.creatorProfile?.userTypeTag)
    }

    // --- M22 ------------------------------------------------------------------------------------------------------------

    @Test
    fun aGetWithABodyThroughASocksProxyFailsFast() {
        val socks = OkHttpClient.Builder().proxy(Proxy(Proxy.Type.SOCKS, InetSocketAddress("127.0.0.1", 9))).build()
        val e = assertFailsWith<TikTokShopException> {
            client(http = socks).affiliateSeller.getConversationList(10L, getConversationListRequest = onlyIds)
        }
        assertEquals(-1, e.code)
        assertNull(e.httpStatus)
        assertContains(e.message!!, "SOCKS")
        assertNull(server.takeRequest(200, TimeUnit.MILLISECONDS), "nothing may go out directly")
    }
}
