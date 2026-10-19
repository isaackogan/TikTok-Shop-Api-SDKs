package com.isaackogan.tiktok.shop;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.isaackogan.tiktok.shop.generated.Meta;
import com.isaackogan.tiktok.shop.generated.event.OrderStatusChangeEvent;
import com.isaackogan.tiktok.shop.generated.event.WebhookEventVisitor;
import com.isaackogan.tiktok.shop.generated.model.OrderStatusChangeWebhook;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import org.junit.jupiter.api.Test;

class WebhooksTest {
    private static JsonObject vectors() throws IOException {
        String raw = new String(Files.readAllBytes(Paths.get("../shared/test-vectors/webhooks.json")), StandardCharsets.UTF_8);
        return JsonParser.parseString(raw).getAsJsonObject();
    }

    private static String sign(String appKey, String secret, byte[] body) throws Exception {
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(new SecretKeySpec(secret.getBytes(StandardCharsets.UTF_8), "HmacSHA256"));
        mac.update(appKey.getBytes(StandardCharsets.UTF_8));
        mac.update(body);
        StringBuilder sb = new StringBuilder();
        for (byte b : mac.doFinal()) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }

    @Test
    void everyVerifyVector() throws IOException {
        JsonArray cases = vectors().getAsJsonArray("verify");
        assertTrue(cases.size() >= 5);
        for (JsonElement el : cases) {
            JsonObject c = el.getAsJsonObject();
            String name = c.get("name").getAsString();
            String body = c.get("rawBody").getAsString();
            boolean expected = c.get("valid").getAsBoolean();
            String key = c.get("appKey").getAsString();
            String secret = c.get("appSecret").getAsString();
            String sig = c.get("signature").getAsString();
            assertEquals(expected, Webhooks.verify(key, secret, body, sig), name + " (String)");
            assertEquals(expected, Webhooks.verify(key, secret, body.getBytes(StandardCharsets.UTF_8), sig), name + " (bytes)");
            if (!expected) {
                assertThrows(WebhookSignatureException.class, () -> Webhooks.verifyAndParse(key, secret, body, sig), name);
            }
        }
    }

    @Test
    void nullSignatureOrBodyIsFalseNotAnException() {
        assertFalse(Webhooks.verify("k", "s", "{}", null));
        assertFalse(Webhooks.verify("k", "s", (byte[]) null, "abc"));
    }

    @Test
    void everyParseVector() throws IOException {
        for (JsonElement el : vectors().getAsJsonArray("parse")) {
            JsonObject c = el.getAsJsonObject();
            WebhookEvent e = Webhooks.parse(c.get("rawBody").getAsString());
            assertEquals(c.get("type").getAsInt(), e.getType(), c.get("name").getAsString());
            if (c.get("known").getAsBoolean()) {
                assertFalse(e instanceof UnknownWebhookEvent);
                assertEquals(c.get("schema").getAsString(), payloadClass(e), c.get("name").getAsString());
            } else {
                assertTrue(e instanceof UnknownWebhookEvent);
                assertEquals(9999, ((UnknownWebhookEvent) e).getRaw().get("type").getAsInt());
            }
        }
    }

    private static String payloadClass(WebhookEvent e) {
        try {
            return e.getClass().getMethod("getPayload").getReturnType().getSimpleName();
        } catch (ReflectiveOperationException ex) {
            throw new AssertionError(ex);
        }
    }

    @Test
    void narrowsToTheConcreteType() {
        String body = "{\"type\":1,\"tts_notification_id\":\"7380066284010030890\",\"shop_id\":\"7495540735365777507\",\"timestamp\":1718305585,"
                + "\"data\":{\"is_on_hold_order\":true,\"order_id\":\"576653688135258178\",\"order_status\":\"UNPAID\",\"update_time\":1718305585}}";
        WebhookEvent e = Webhooks.parse(body);
        assertTrue(e instanceof OrderStatusChangeEvent);
        OrderStatusChangeWebhook w = ((OrderStatusChangeEvent) e).getPayload();
        assertEquals("576653688135258178", w.getData().getOrderId());
        assertEquals("UNPAID", w.getData().getOrderStatus().getValue());
        assertEquals(1718305585L, w.getTimestamp());
        assertEquals(1, e.getRaw().get("type").getAsInt(), "raw is kept");
    }

    @Test
    void visitorReachesTheRightMethod() {
        WebhookEvent known = Webhooks.parse("{\"type\":1,\"shop_id\":\"1\",\"data\":{\"order_id\":\"5\"}}");
        WebhookEvent unknown = Webhooks.parse("{\"type\":9999,\"data\":{}}");
        WebhookEventVisitor<String> v = new WebhookEventVisitor<String>() {
            @Override
            public String visitOrderStatusChange(OrderStatusChangeEvent event) {
                return "order " + event.getPayload().getData().getOrderId();
            }

            @Override
            public String visitUnknown(UnknownWebhookEvent event) {
                return "unknown " + event.getType();
            }
        };
        assertEquals("order 5", known.accept(v));
        assertEquals("unknown 9999", unknown.accept(v));
    }

    @Test
    void aNineteenDigitShopIdSentAsANumberKeepsItsValue() {
        String body = "{\"type\":1,\"shop_id\":7494049642642441621,\"tts_notification_id\":7380066284010030890,\"timestamp\":1718305585,"
                + "\"data\":{\"order_id\":576653688135258178,\"order_status\":\"UNPAID\"}}";
        OrderStatusChangeWebhook w = ((OrderStatusChangeEvent) Webhooks.parse(body)).getPayload();
        assertEquals("7494049642642441621", w.getShopId());
        assertEquals("7380066284010030890", w.getTtsNotificationId());
        assertEquals("576653688135258178", w.getData().getOrderId());
    }

    @Test
    void unknownFieldsStillParse() {
        String body = "{\"type\":1,\"shop_id\":\"1\",\"brand_new\":{\"x\":1},\"data\":{\"order_id\":\"5\",\"order_status\":\"UNPAID\",\"extra\":[1]}}";
        WebhookEvent e = Webhooks.parse(body);
        assertEquals("5", ((OrderStatusChangeEvent) e).getPayload().getData().getOrderId());
    }

    @Test
    void missingOrNonIntegerTypeIsRejected() {
        for (String body : Arrays.asList("{}", "{\"type\":null}", "{\"type\":\"1\"}", "{\"type\":true}", "{\"type\":1.5}",
                "{\"type\":1.0}", "{\"type\":[1]}", "{\"type\":99999999999}", "[1]", "\"x\"", "null", "not json", "")) {
            IllegalArgumentException ex = assertThrows(IllegalArgumentException.class, () -> Webhooks.parse(body), body);
            assertNotNull(ex.getMessage());
        }
    }

    @Test
    void anIllTypedKnownPayloadIsRejectedClearly() {
        assertThrows(IllegalArgumentException.class, () -> Webhooks.parse("{\"type\":1,\"data\":\"nope\"}"));
    }

    @Test
    void verifyAndParseRoundTripsWithBytesAsReceived() throws Exception {
        byte[] body = "{ \"type\" : 9999 ,\n \"data\": {} }".getBytes(StandardCharsets.UTF_8);
        String sig = sign("key", "secret", body);
        assertTrue(Webhooks.verifyAndParse("key", "secret", body, sig) instanceof UnknownWebhookEvent);
        byte[] reserialized = "{\"type\":9999,\"data\":{}}".getBytes(StandardCharsets.UTF_8);
        assertThrows(WebhookSignatureException.class, () -> Webhooks.verifyAndParse("key", "secret", reserialized, sig));
    }

    @Test
    void nonAsciiBodiesVerifyByTheirBytes() throws Exception {
        byte[] body = "{\"type\":9999,\"name\":\"café ☃\"}".getBytes(StandardCharsets.UTF_8);
        String sig = sign("k", "s", body);
        assertTrue(Webhooks.verify("k", "s", body, sig));
        assertTrue(Webhooks.verify("k", "s", new String(body, StandardCharsets.UTF_8), sig));
    }

    @Test
    void eventTypesAreExposed() {
        assertEquals("ORDER_STATUS_CHANGE", Webhooks.EVENT_TYPES.get(1));
        assertEquals(16, Webhooks.EVENT_TYPES.size());
        assertEquals(Meta.EVENT_TYPES, Webhooks.EVENT_TYPES);
    }

    @Test
    void everyMetaWebhookHasAnEventClassWiredToItsType() throws Exception {
        assertEquals(44, Meta.WEBHOOKS.size());
        for (Meta.Webhook w : Meta.WEBHOOKS) {
            Class<?> cls = Class.forName("com.isaackogan.tiktok.shop.generated.event." + w.schema.replaceAll("Webhook$", "Event"));
            assertTrue(WebhookEvent.class.isAssignableFrom(cls), w.schema);
            assertEquals(w.type, cls.getField("TYPE").getInt(null), w.schema);
            assertEquals(w.schema, cls.getMethod("getPayload").getReturnType().getSimpleName());
            // Dispatch reaches that model: a bare body either parses to the event, or the model rejects it for a missing field.
            try {
                WebhookEvent e = Webhooks.parse("{\"type\":" + w.type + "}");
                assertEquals(cls, e.getClass(), w.schema);
            } catch (IllegalArgumentException e) {
                assertTrue(e.getMessage().startsWith("webhook of type " + w.type + " does not match its model"), e.getMessage());
            }
        }
    }

    @Test
    void aKnownTypeMissingARequiredFieldIsRejectedClearly() {
        IllegalArgumentException ex = assertThrows(IllegalArgumentException.class, () -> Webhooks.parse("{\"type\":66,\"shop_id\":\"1\"}"));
        assertTrue(ex.getMessage().contains("type 66"), ex.getMessage());
    }
}
