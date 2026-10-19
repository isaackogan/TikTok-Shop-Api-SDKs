package com.isaackogan.tiktok.shop;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import java.io.IOException;
import java.lang.reflect.Method;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.TreeSet;
import org.junit.jupiter.api.Test;

class WiringTest {
    static final List<String> GROUPS = Arrays.asList("affiliateCreator", "affiliatePartner", "affiliateSeller", "analytics",
            "authorization", "customerEngagement", "customerService", "event", "finance", "fulfilledByTikTok", "fulfillment",
            "logistics", "orders", "products", "promotion", "returnAndRefund", "seller", "supplyChain", "tools");

    static JsonObject read(String path) throws IOException {
        return JsonParser.parseString(new String(Files.readAllBytes(Paths.get(path)), StandardCharsets.UTF_8)).getAsJsonObject();
    }

    @Test
    void groupNamesAreTheCanonicalList() throws IOException {
        // shared/api-groups.json is the source of truth
        JsonObject shared = read("../shared/api-groups.json");
        List<String> fromShared = new ArrayList<>();
        shared.entrySet().forEach(e -> fromShared.add(e.getValue().getAsString()));
        assertEquals(new TreeSet<>(GROUPS), new TreeSet<>(fromShared));

        List<String> getters = new ArrayList<>();
        for (Method m : TikTokShop.class.getDeclaredMethods()) {
            if (java.lang.reflect.Modifier.isPublic(m.getModifiers()) && !java.lang.reflect.Modifier.isStatic(m.getModifiers())
                    && m.getParameterCount() == 0 && m.getReturnType().getName().startsWith("com.isaackogan.tiktok.shop.generated.api.")) {
                getters.add(m.getName());
            }
        }
        assertEquals(new TreeSet<>(GROUPS), new TreeSet<>(getters));
    }

    @Test
    void everyOperationIsAMethodOnItsGroupsConcreteApiClass() throws Exception {
        JsonArray ops = read("build/meta.json").getAsJsonArray("operations");
        assertEquals(320, ops.size());
        for (JsonElement el : ops) {
            JsonObject op = el.getAsJsonObject();
            String group = op.get("group").getAsString();
            Method getter = TikTokShop.class.getMethod(group);
            Class<?> api = getter.getReturnType();
            assertTrue(api.getName().startsWith("com.isaackogan.tiktok.shop.generated.api.") && api.getName().endsWith("Api"),
                    group + " returns the concrete generated API, got " + api.getName());
            String id = op.get("operationId").getAsString();
            boolean found = false;
            for (Method m : api.getMethods()) {
                if (m.getName().equals(id)) {
                    found = true;
                    break;
                }
            }
            assertTrue(found, id + " is a method of " + api.getSimpleName());
            assertNotNull(Class.forName("com.isaackogan.tiktok.shop.generated.Meta"));
        }
    }

    @Test
    void metaMatchesTheSpec() throws Exception {
        JsonArray ops = read("build/meta.json").getAsJsonArray("operations");
        assertEquals(ops.size(), com.isaackogan.tiktok.shop.generated.Meta.OPERATIONS.size());
        long cipher = com.isaackogan.tiktok.shop.generated.Meta.OPERATIONS.stream().filter(o -> o.requiresShopCipher).count();
        assertEquals(233, cipher);
        assertEquals(16, com.isaackogan.tiktok.shop.generated.Meta.EVENT_TYPES.size());
    }
}
