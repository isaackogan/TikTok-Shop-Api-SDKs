package com.isaackogan.tiktok.shop

import com.google.gson.JsonObject
import com.google.gson.JsonParser
import java.io.IOException
import java.net.ServerSocket
import java.nio.file.Files
import java.nio.file.Paths
import java.time.Duration
import java.util.concurrent.TimeUnit
import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertFailsWith
import kotlin.test.assertFalse
import kotlin.test.assertIs
import kotlin.test.assertNotNull
import kotlin.test.assertNull
import kotlin.test.assertTrue
import mockwebserver3.MockResponse
import mockwebserver3.MockWebServer
import mockwebserver3.SocketEffect

class AuthTest {
    private fun vectors(): JsonObject =
        JsonParser.parseString(String(Files.readAllBytes(Paths.get("../shared/test-vectors/auth.json")), Charsets.UTF_8)).asJsonObject

    private fun str(e: com.google.gson.JsonElement): String? = if (e.isJsonNull) null else e.asString

    private fun auth(s: MockWebServer, timeout: Duration? = null) =
        TikTokShopAuth(TikTokShopAuthOptions(appKey = "123abc", appSecret = "s3cret", baseUrl = s.url("/").toString(), timeout = timeout))

    private val min = """{"code":0,"message":"success","request_id":"rq","data":{"access_token":"AT","access_token_expire_in":10,"refresh_token":"RT","refresh_token_expire_in":20}}"""

    private fun exchange(body: String, status: Int = 200): TokenSet =
        MockWebServer().use { s ->
            s.enqueue(MockResponse.Builder().code(status).body(body).build())
            s.start()
            auth(s).exchangeCode("C")
        }

    private fun exchangeFails(body: String, status: Int = 200): TikTokShopException =
        MockWebServer().use { s ->
            s.enqueue(MockResponse.Builder().code(status).body(body).build())
            s.start()
            assertFailsWith<TikTokShopException> { auth(s).exchangeCode("C") }
        }

    @Test
    fun everyAuthorizationUrlVector() {
        val cases = vectors().getAsJsonArray("authorizationUrls")
        assertTrue(cases.size() >= 5)
        for (el in cases) {
            val c = el.asJsonObject
            val a = TikTokShopAuth(
                TikTokShopAuthOptions(appKey = str(c["appKey"]) ?: "unused", appSecret = "x", serviceId = str(c["serviceId"])),
            )
            val type = TikTokShopAuth.AuthType.valueOf(c["type"].asString.uppercase())
            val region = TikTokShopAuth.Region.valueOf(c["region"].asString.uppercase())
            assertEquals(c["url"].asString, a.authorizationUrl(type, region, str(c["state"])))
        }
    }

    @Test
    fun emptyStateAddsNoParameter() {
        val a = TikTokShopAuth(TikTokShopAuthOptions("k", "s", serviceId = "1"))
        assertEquals("https://services.tiktokshop.com/open/authorize?service_id=1", a.authorizationUrl(TikTokShopAuth.AuthType.SELLER, TikTokShopAuth.Region.ROW, ""))
    }

    @Test
    fun sellerAndPartnerUrlsNeedAServiceId() {
        val a = TikTokShopAuth(TikTokShopAuthOptions("k", "s"))
        assertFailsWith<IllegalStateException> { a.authorizationUrl(TikTokShopAuth.AuthType.SELLER, TikTokShopAuth.Region.US) }
        assertFailsWith<IllegalStateException> { a.authorizationUrl(TikTokShopAuth.AuthType.PARTNER, TikTokShopAuth.Region.US) }
        assertTrue(a.authorizationUrl(TikTokShopAuth.AuthType.CREATOR, TikTokShopAuth.Region.US).startsWith("https://shop.tiktok.com/"))
    }

    @Test
    fun everyTokenRequestVectorIsAGetWithTheQueryInOrder() {
        for (el in vectors().getAsJsonArray("tokenRequests")) {
            val c = el.asJsonObject
            MockWebServer().use { s ->
                s.enqueue(MockResponse.Builder().body(min).build())
                s.start()
                val a = TikTokShopAuth(TikTokShopAuthOptions(c["appKey"].asString, c["appSecret"].asString, baseUrl = s.url("/").toString()))
                val t = if (c["kind"].asString == "exchange") a.exchangeCode(c["value"].asString) else a.refresh(c["value"].asString)
                assertEquals("AT", t.accessToken)
                val r = assertNotNull(s.takeRequest(5, TimeUnit.SECONDS))
                assertEquals("GET", r.method)
                assertEquals(c["url"].asString.replace("https://auth.tiktok-shops.com", ""), r.target)
            }
        }
    }

    @Test
    fun everyTokenResponseVector() {
        for (el in vectors().getAsJsonArray("tokenResponses")) {
            val c = el.asJsonObject
            val body = c["body"].asString
            if (c["expected"].isJsonNull) {
                val ex = exchangeFails(body)
                assertEquals(c["errorCode"].asInt, ex.code)
                assertEquals("r2", ex.requestId)
                assertEquals("invalid auth code", ex.message)
                continue
            }
            val x = c["expected"].asJsonObject
            val t = exchange(body)
            assertEquals(x["accessToken"].asString, t.accessToken)
            assertEquals(x["accessTokenExpireIn"].asLong, t.accessTokenExpireIn)
            assertEquals(x["refreshToken"].asString, t.refreshToken)
            assertEquals(x["refreshTokenExpireIn"].asLong, t.refreshTokenExpireIn)
            assertEquals(x["openId"].asString, t.openId)
            assertEquals(x["sellerName"].asString, t.sellerName)
            assertEquals(x["sellerBaseRegion"].asString, t.sellerBaseRegion)
            assertEquals(x["userType"].asInt, t.userType)
            assertEquals(listOf("seller.affiliate_collaboration.read", "seller.affiliate_collaboration.write"), t.grantedScopes)
        }
    }

    @Test
    fun aMinimalFourFieldResponseSucceeds() {
        val t = exchange(min)
        assertEquals("AT", t.accessToken)
        assertEquals(10L, t.accessTokenExpireIn)
        assertEquals("RT", t.refreshToken)
        assertEquals(20L, t.refreshTokenExpireIn)
        assertNull(t.openId)
        assertNull(t.sellerName)
        assertNull(t.sellerBaseRegion)
        assertNull(t.userType)
        assertNull(t.grantedScopes)
    }

    private fun data(fields: String) = """{"code":0,"message":"success","request_id":"rq","data":{$fields}}"""

    private val tok = """"access_token":"AT","access_token_expire_in":10,"refresh_token":"RT","refresh_token_expire_in":20"""

    @Test
    fun optionalFieldsThatAreNullOrIllTypedBecomeNull() {
        val t = exchange(data("""$tok,"open_id":null,"seller_name":null,"seller_base_region":7,"user_type":"x","granted_scopes":null"""))
        assertNull(t.openId)
        assertNull(t.sellerName)
        assertNull(t.sellerBaseRegion)
        assertNull(t.userType)
        assertNull(t.grantedScopes)
        assertNull(exchange(data("""$tok,"granted_scopes":["a",1,null,"b"]""")).grantedScopes, "a list with a non-string is ill-typed, so absent")
    }

    @Test
    fun aNumericOpenIdKeepsItsExactDigits() {
        assertEquals("7494049642642441621", exchange(data("""$tok,"open_id":7494049642642441621""")).openId)
    }

    @Test
    fun missingNullOrIllTypedRequiredFieldsAreRejectedWithCodeMinusOneAndTheRequestId() {
        val bad = listOf(
            """"access_token_expire_in":10,"refresh_token":"RT","refresh_token_expire_in":20""",
            """"access_token":null,"access_token_expire_in":10,"refresh_token":"RT","refresh_token_expire_in":20""",
            """"access_token":"","access_token_expire_in":10,"refresh_token":"RT","refresh_token_expire_in":20""",
            """"access_token":5,"access_token_expire_in":10,"refresh_token":"RT","refresh_token_expire_in":20""",
            """"access_token":"AT","access_token_expire_in":true,"refresh_token":"RT","refresh_token_expire_in":20""",
            """"access_token":"AT","access_token_expire_in":"10","refresh_token":"RT","refresh_token_expire_in":20""",
            """"access_token":"AT","access_token_expire_in":1.5,"refresh_token":"RT","refresh_token_expire_in":20""",
            """"access_token":"AT","access_token_expire_in":10,"refresh_token":"","refresh_token_expire_in":20""",
            """"access_token":"AT","access_token_expire_in":10,"refresh_token":"RT","refresh_token_expire_in":null""",
            """"access_token":"AT","access_token_expire_in":10,"refresh_token":"RT","refresh_token_expire_in":false""",
            """"access_token":"AT","access_token_expire_in":10,"refresh_token":"RT"""",
        )
        for (fields in bad) {
            val ex = exchangeFails(data(fields))
            assertEquals(-1, ex.code, fields)
            assertEquals("rq", ex.requestId, fields)
        }
    }

    @Test
    fun successWithoutDataOrWithNonObjectDataIsRejected() {
        for (body in listOf("""{"code":0,"request_id":"rq"}""", """{"code":0,"request_id":"rq","data":null}""", """{"code":0,"request_id":"rq","data":[1]}""", """{"code":0,"request_id":"rq","data":"x"}""")) {
            val ex = exchangeFails(body)
            assertEquals(-1, ex.code, body)
            assertEquals("rq", ex.requestId)
        }
    }

    @Test
    fun nonJsonBodiesUseMinusOneOn2xxAndTheStatusOtherwise() {
        for (status in listOf(200, 502)) {
            val ex = exchangeFails("<html>nope</html>", status)
            assertEquals(if (status == 200) -1 else status, ex.code)
            assertEquals(status, ex.httpStatus)
        }
        assertEquals(-1, exchangeFails("[1]").code)
    }

    @Test
    fun nonSuccessStatusesRaiseEvenWithCodeZero() {
        val ex = exchangeFails(min, 500)
        assertEquals(500, ex.code)
        assertEquals(500, ex.httpStatus)
        val withCode = exchangeFails("""{"code":36004004,"message":"bad","request_id":"r9"}""", 400)
        assertEquals(36004004, withCode.code)
        assertEquals("r9", withCode.requestId)
        assertEquals(400, withCode.httpStatus)
    }

    @Test
    fun refreshWorksToo() {
        MockWebServer().use { s ->
            s.enqueue(MockResponse.Builder().body(min).build())
            s.start()
            assertEquals("AT", auth(s).refresh("RTOK").accessToken)
            assertTrue(assertNotNull(s.takeRequest(5, TimeUnit.SECONDS)).target.startsWith("/api/v2/token/refresh?"))
        }
    }

    @Test
    fun aRedirectIsNeverFollowed() {
        MockWebServer().use { evil ->
            evil.start()
            MockWebServer().use { s ->
                s.enqueue(MockResponse.Builder().code(302).setHeader("Location", evil.url("/steal").toString()).build())
                s.start()
                val ex = assertFailsWith<TikTokShopException> { auth(s).exchangeCode("CODE-SECRET") }
                assertEquals(302, ex.httpStatus)
                assertEquals(0, evil.requestCount, "the redirect target received nothing")
            }
        }
    }

    private fun assertNoSecrets(t: Throwable) {
        var c: Throwable? = t
        while (c != null) {
            val all = "$c ${c.message}"
            for (secret in listOf("s3cret", "CODE-SECRET", "REFRESH-SECRET", "app_secret", "auth_code", "refresh_token", "?app_key")) {
                assertFalse(all.contains(secret), "leaked $secret in: $all")
            }
            c = c.cause
        }
    }

    @Test
    fun aClosedPortLeaksNoSecretsOnExchangeOrRefresh() {
        val port = ServerSocket(0).use { it.localPort }
        val a = TikTokShopAuth(TikTokShopAuthOptions("123abc", "s3cret", baseUrl = "http://127.0.0.1:$port/"))
        val x = assertFailsWith<TikTokShopException> { a.exchangeCode("CODE-SECRET") }
        val y = assertFailsWith<TikTokShopException> { a.refresh("REFRESH-SECRET") }
        for (ex in listOf(x, y)) {
            assertNoSecrets(ex)
            assertIs<IOException>(ex.cause)
            assertEquals(-1, ex.code)
            assertNull(ex.httpStatus)
        }
    }

    @Test
    fun aTimeoutLeaksNoSecretsOnExchangeOrRefresh() {
        MockWebServer().use { s ->
            s.enqueue(MockResponse.Builder().onResponseStart(SocketEffect.Stall).build())
            s.enqueue(MockResponse.Builder().onResponseStart(SocketEffect.Stall).build())
            s.start()
            val a = auth(s, Duration.ofMillis(300))
            val x = assertFailsWith<TikTokShopException> { a.exchangeCode("CODE-SECRET") }
            val y = assertFailsWith<TikTokShopException> { a.refresh("REFRESH-SECRET") }
            for (ex in listOf(x, y)) {
                assertNoSecrets(ex)
                assertIs<IOException>(ex.cause)
                assertEquals(-1, ex.code)
            }
        }
    }

    @Test
    fun aBadBaseUrlLeaksNoSecrets() {
        val a = TikTokShopAuth(TikTokShopAuthOptions("k", "s3cret", baseUrl = "not a url"))
        assertNoSecrets(assertFailsWith<TikTokShopException> { a.exchangeCode("CODE-SECRET") })
    }

    @Test
    fun tokenSetAndAuthOptionsNeverPrintSecrets() {
        val t = exchange(data("""$tok,"open_id":"OID","seller_name":"Shop","granted_scopes":["s.read"]"""))
        val s = t.toString()
        assertFalse(Regex("\\bAT\\b|\\bRT\\b").containsMatchIn(s), s)
        assertTrue(s.contains("OID") && s.contains("Shop"), s)
        val o = TikTokShopAuthOptions(appKey = "pubkey", appSecret = "SEKRET-VALUE", serviceId = "123").toString()
        assertFalse(o.contains("SEKRET-VALUE"), o)
        assertTrue(o.contains("pubkey"), o)
        val a = TikTokShopAuth(TikTokShopAuthOptions(appKey = "pubkey", appSecret = "SEKRET-VALUE")).toString()
        assertFalse(a.contains("SEKRET-VALUE"), a)
    }

    @Test
    fun aTokenRedirectIsNotFollowedAndSurfacesAsItsStatus() {
        MockWebServer().use { target ->
            target.start()
            MockWebServer().use { s ->
                s.enqueue(MockResponse.Builder().code(302).setHeader("Location", target.url("/stolen").toString()).build())
                s.start()
                val ex = assertFailsWith<TikTokShopException> { auth(s).exchangeCode("C") }
                assertEquals(302, ex.code)
                assertEquals(302, ex.httpStatus)
                assertEquals(0, target.requestCount)
            }
        }
    }

    /** R13b: non-2xx -> TikTok's non-zero code else the HTTP status; an unreadable 2xx, or code 0 without data -> -1. */
    @Test
    fun r13bTokenCodes() {
        val cases = listOf(
            Triple(503, """{"message":"x"}""", 503), Triple(503, """{"code":0}""", 503), Triple(503, "down", 503), Triple(503, "", 503),
            Triple(503, "[1]", 503), Triple(302, "", 302), Triple(503, """{"code":12345,"message":"m"}""", 12345),
            Triple(200, "<html>", -1), Triple(200, """{"code":0,"request_id":"r"}""", -1),
        )
        for ((status, body, want) in cases) {
            val ex = exchangeFails(body, status)
            assertEquals(want, ex.code, "$status $body")
            assertEquals(status, ex.httpStatus, "$status $body")
        }
    }
}
