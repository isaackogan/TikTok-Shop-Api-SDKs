package com.isaackogan.tiktok.shop;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Arrays;
import org.junit.jupiter.api.Test;

/** Lesson 23: no string form of a type that holds a secret prints it. */
class SecretsTest {
    static final String SECRET = "super-secret-value";
    static final String TOKEN = "tok-value-xyz";
    static final String CIPHER = "cipher-value-xyz";
    static final String REFRESH = "refresh-value-xyz";

    private static void assertRedacted(Object o, String... visible) {
        String text = String.valueOf(o);
        for (String secret : Arrays.asList(SECRET, TOKEN, CIPHER, REFRESH)) {
            assertFalse(text.contains(secret), o.getClass().getSimpleName() + " leaked " + secret + ": " + text);
        }
        for (String v : visible) {
            assertTrue(text.contains(v), o.getClass().getSimpleName() + " should show " + v + ": " + text);
        }
    }

    @Test
    void theClientAndItsBuilderNeverPrintSecrets() {
        TikTokShop.Builder b = TikTokShop.builder().appKey("appkey1").appSecret(SECRET).accessToken(TOKEN).shopCipher(CIPHER);
        assertRedacted(b, "appkey1");
        TikTokShop c = b.build();
        assertRedacted(c, "appkey1");
        assertRedacted(c.withShop(TOKEN, CIPHER), "appkey1");
    }

    @Test
    void shopCredentialsNeverPrintTheTokenOrCipher() {
        ShopCredentials.Builder b = ShopCredentials.builder().accessToken(TOKEN).shopCipher(CIPHER);
        assertRedacted(b, "accessToken");
        assertRedacted(b.build(), "accessToken");
    }

    @Test
    void theAuthClientAndItsBuilderNeverPrintTheSecret() {
        TikTokShopAuth.Builder b = TikTokShopAuth.builder().appKey("appkey1").appSecret(SECRET);
        assertRedacted(b, "appkey1");
        assertRedacted(b.build(), "appkey1");
    }

    @Test
    void theTokenSetNeverPrintsItsTokens() {
        TokenSet t = new TokenSet(TOKEN, 1L, REFRESH, 2L, "open1", "shop", "US", 0, Arrays.asList("a"));
        assertRedacted(t, "open1");
    }
}
