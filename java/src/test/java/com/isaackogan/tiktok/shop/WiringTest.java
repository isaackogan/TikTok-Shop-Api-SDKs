package com.isaackogan.tiktok.shop;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.isaackogan.tiktok.shop.generated.Meta;
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
        // Meta is generated from the spec and committed, so this needs no build output.
        assertFalse(Meta.OPERATIONS.isEmpty());
        java.util.Map<String, java.util.Set<String>> methodsOf = new java.util.HashMap<>();
        for (Meta.Operation op : Meta.OPERATIONS) {
            Method getter = TikTokShop.class.getMethod(op.group);
            Class<?> api = getter.getReturnType();
            assertTrue(api.getName().startsWith("com.isaackogan.tiktok.shop.generated.api.") && api.getName().endsWith("Api"),
                    op.group + " returns the concrete generated API, got " + api.getName());
            assertEquals(op.apiClass, api.getSimpleName(), op.group + " is the class Meta names");
            java.util.Set<String> methods = methodsOf.computeIfAbsent(op.group, g -> {
                java.util.Set<String> names = new java.util.HashSet<>();
                for (Method m : api.getMethods()) {
                    names.add(m.getName());
                }
                return names;
            });
            assertTrue(methods.contains(op.operationId), op.operationId + " is a method of " + api.getSimpleName());
        }
        assertEquals(new TreeSet<>(GROUPS), new TreeSet<>(Meta.OPERATIONS.stream().map(o -> o.group).collect(java.util.stream.Collectors.toSet())));
        assertEquals(new TreeSet<>(GROUPS), new TreeSet<>(Meta.GROUPS.stream().map(g -> g.name).collect(java.util.stream.Collectors.toSet())));
    }

    @Test
    void metaIsInternallyConsistent() {
        assertTrue(Meta.OPERATIONS.stream().anyMatch(o -> o.requiresShopCipher));
        assertTrue(Meta.OPERATIONS.stream().anyMatch(o -> !o.requiresShopCipher));
        assertEquals(Meta.OPERATIONS.size(), Meta.OPERATIONS.stream().map(o -> o.operationId).distinct().count(), "operation ids are unique");
        assertFalse(Meta.EVENT_TYPES.isEmpty());
        java.util.Map<Integer, String> fromWebhooks = new java.util.HashMap<>();
        for (Meta.Webhook w : Meta.WEBHOOKS) {
            if (w.eventType != null) {
                fromWebhooks.put(w.type, w.eventType);
            }
        }
        assertEquals(fromWebhooks, Meta.EVENT_TYPES);
        // the matcher agrees with Meta for every operation that has no path parameter
        for (Meta.Operation op : Meta.OPERATIONS) {
            if (!op.path.contains("{")) {
                assertEquals(op.requiresShopCipher, TikTokShop.requiresShopCipher(op.method, op.path), op.operationId);
            }
        }
    }
}
