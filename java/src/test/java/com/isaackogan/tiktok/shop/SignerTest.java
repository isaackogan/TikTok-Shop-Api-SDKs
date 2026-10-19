package com.isaackogan.tiktok.shop;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import org.junit.jupiter.api.Test;

class SignerTest {
    @Test
    void everySigningVector() throws IOException {
        String raw = new String(Files.readAllBytes(Paths.get("../shared/test-vectors/signing.json")), StandardCharsets.UTF_8);
        JsonArray cases = JsonParser.parseString(raw).getAsJsonObject().getAsJsonArray("cases");
        assertTrue(cases.size() >= 6, "expected the shared vectors");
        for (JsonElement el : cases) {
            JsonObject c = el.getAsJsonObject();
            List<Signer.Param> query = new ArrayList<>();
            for (JsonElement p : c.getAsJsonArray("query")) {
                query.add(new Signer.Param(p.getAsJsonArray().get(0).getAsString(), p.getAsJsonArray().get(1).getAsString()));
            }
            String contentType = c.get("contentType").isJsonNull() ? null : c.get("contentType").getAsString();
            byte[] body = c.get("body").isJsonNull() ? null : c.get("body").getAsString().getBytes(StandardCharsets.UTF_8);
            Signer.Request req = new Signer.Request(c.get("path").getAsString(), query, contentType, body, c.get("secret").getAsString());
            String name = c.get("name").getAsString();
            assertEquals(c.get("stringToSign").getAsString(), Signer.stringToSign(req), name + ": stringToSign");
            assertEquals(c.get("sign").getAsString(), Signer.sign(req), name + ": sign");
        }
    }

    @Test
    void requiresShopCipher() {
        assertTrue(TikTokShop.requiresShopCipher("POST", "/order/202309/orders/search"));
        assertFalse(TikTokShop.requiresShopCipher("GET", "/authorization/202309/shops"));
        assertTrue(TikTokShop.requiresShopCipher("GET", "/product/202309/products/1729507467923261408"));
        assertTrue(TikTokShop.requiresShopCipher("post", "/order/202309/orders/search"), "method is case-insensitive");
        assertFalse(TikTokShop.requiresShopCipher("GET", "/nothing/here"));
    }
}
