package com.isaackogan.tiktok.shop;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertNotSame;
import static org.junit.jupiter.api.Assertions.assertNull;

import java.io.IOException;
import java.util.concurrent.TimeUnit;
import okhttp3.mockwebserver.MockResponse;
import okhttp3.mockwebserver.MockWebServer;
import okhttp3.mockwebserver.RecordedRequest;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class WithShopTest {
    MockWebServer server;
    TikTokShop base;

    @BeforeEach
    void start() throws IOException {
        server = new MockWebServer();
        server.start();
        base = TikTokShop.builder().appKey("k").appSecret("s").accessToken("t1").shopCipher("c1")
                .baseUrl(server.url("/").toString()).build();
    }

    @AfterEach
    void stop() throws IOException {
        server.shutdown();
    }

    RecordedRequest call(TikTokShop c) throws Exception {
        server.enqueue(new MockResponse().setBody(StubSupport.OK));
        c.orders().getOrderList(1L, null, null, null, null);
        RecordedRequest r = server.takeRequest(5, TimeUnit.SECONDS);
        assertNotNull(r);
        return r;
    }

    @Test
    void omittedValuesAreKept() throws Exception {
        TikTokShop other = base.withShop(ShopCredentials.builder().accessToken("t2").build());
        assertNotSame(base, other);
        RecordedRequest r = call(other);
        assertEquals("t2", r.getHeader("x-tts-access-token"));
        assertEquals("c1", StubSupport.only(r, "shop_cipher"));
    }

    @Test
    void valuesAreReplaced() throws Exception {
        RecordedRequest r = call(base.withShop(ShopCredentials.builder().accessToken("t2").shopCipher("c2").build()));
        assertEquals("t2", r.getHeader("x-tts-access-token"));
        assertEquals("c2", StubSupport.only(r, "shop_cipher"));
        StubSupport.assertSigned(r, "s");
        RecordedRequest r2 = call(base.withShop("t3", "c3"));
        assertEquals("t3", r2.getHeader("x-tts-access-token"));
        assertEquals("c3", StubSupport.only(r2, "shop_cipher"));
    }

    @Test
    void explicitNullOrEmptyClears() throws Exception {
        RecordedRequest r = call(base.withShop(ShopCredentials.builder().shopCipher(null).build()));
        assertFalse(StubSupport.queryMap(r).containsKey("shop_cipher"));
        assertEquals("t1", r.getHeader("x-tts-access-token"));

        RecordedRequest r2 = call(base.withShop(ShopCredentials.builder().accessToken("").build()));
        assertNull(r2.getHeader("x-tts-access-token"));
        assertEquals("c1", StubSupport.only(r2, "shop_cipher"));

        RecordedRequest r3 = call(base.withShop(null, null));
        assertNull(r3.getHeader("x-tts-access-token"));
        assertFalse(StubSupport.queryMap(r3).containsKey("shop_cipher"));
    }

    @Test
    void theOriginalIsUnchanged() throws Exception {
        base.withShop(ShopCredentials.builder().accessToken("t2").shopCipher("c2").build());
        base.withShop(null, null);
        RecordedRequest r = call(base);
        assertEquals("t1", r.getHeader("x-tts-access-token"));
        assertEquals("c1", StubSupport.only(r, "shop_cipher"));
    }
}
