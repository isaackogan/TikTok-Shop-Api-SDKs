package com.isaackogan.tiktok.shop;

import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.google.gson.JsonPrimitive;
import com.isaackogan.tiktok.shop.generated.Meta;
import com.isaackogan.tiktok.shop.generated.event.WebhookEvents;
import java.nio.charset.StandardCharsets;
import java.security.GeneralSecurityException;
import java.security.MessageDigest;
import java.util.Map;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

/** Verifies and parses TikTok Shop webhooks. */
public final class Webhooks {
    private Webhooks() {}

    /** Webhook type to event name, e.g. 1 to {@code ORDER_STATUS_CHANGE}. */
    public static final Map<Integer, String> EVENT_TYPES = Meta.EVENT_TYPES;

    /**
     * Checks the {@code Authorization} header: lowercase hex HMAC-SHA256 (key: the app secret) over {@code appKey + rawBody},
     * compared in constant time. A null or empty signature is false.
     *
     * @param rawBody the body exactly as received. Never re-serialize it.
     */
    public static boolean verify(String appKey, String appSecret, byte[] rawBody, String signature) {
        if (signature == null || signature.isEmpty() || rawBody == null) {
            return false;
        }
        try {
            Mac mac = Mac.getInstance("HmacSHA256");
            mac.init(new SecretKeySpec(appSecret.getBytes(StandardCharsets.UTF_8), "HmacSHA256"));
            mac.update(appKey.getBytes(StandardCharsets.UTF_8));
            mac.update(rawBody);
            byte[] expected = hex(mac.doFinal()).getBytes(StandardCharsets.UTF_8);
            return MessageDigest.isEqual(expected, signature.getBytes(StandardCharsets.UTF_8));
        } catch (GeneralSecurityException e) {
            throw new IllegalStateException(e); // HmacSHA256 is part of every JRE
        }
    }

    /** As {@link #verify(String, String, byte[], String)}, with the body as a string (its UTF-8 bytes are signed). */
    public static boolean verify(String appKey, String appSecret, String rawBody, String signature) {
        return rawBody != null && verify(appKey, appSecret, rawBody.getBytes(StandardCharsets.UTF_8), signature);
    }

    /**
     * Parses a body to its event, picked by the integer {@code type}. A {@code type} this SDK does not know gives an
     * {@link UnknownWebhookEvent}. 64-bit IDs keep their exact digits, and unknown fields are accepted.
     *
     * @throws IllegalArgumentException if the body is not a JSON object, its {@code type} is missing or not an integer
     *     (a string, boolean, null, fraction, or outside the int range), or the body does not fit its model
     */
    public static WebhookEvent parse(byte[] rawBody) {
        if (rawBody == null) {
            throw new IllegalArgumentException("webhook body is null");
        }
        return parse(new String(rawBody, StandardCharsets.UTF_8));
    }

    /** As {@link #parse(byte[])}. */
    public static WebhookEvent parse(String rawBody) {
        if (rawBody == null) {
            throw new IllegalArgumentException("webhook body is null");
        }
        JsonElement json;
        try {
            json = JsonParser.parseString(rawBody);
        } catch (RuntimeException e) {
            throw new IllegalArgumentException("webhook body is not valid JSON", e);
        }
        if (!json.isJsonObject()) {
            throw new IllegalArgumentException("webhook body is not a JSON object");
        }
        JsonObject obj = json.getAsJsonObject();
        int type = typeOf(obj.get("type"));
        WebhookEvent event;
        try {
            event = WebhookEvents.fromJson(type, obj);
        } catch (RuntimeException e) {
            throw new IllegalArgumentException("webhook of type " + type + " does not match its model: " + e.getMessage(), e);
        }
        return event != null ? event : new UnknownWebhookEvent(type, obj);
    }

    /**
     * Verifies, then parses.
     *
     * @throws WebhookSignatureException if the signature does not match
     */
    public static WebhookEvent verifyAndParse(String appKey, String appSecret, byte[] rawBody, String signature) {
        if (!verify(appKey, appSecret, rawBody, signature)) {
            throw new WebhookSignatureException();
        }
        return parse(rawBody);
    }

    /** As {@link #verifyAndParse(String, String, byte[], String)}. */
    public static WebhookEvent verifyAndParse(String appKey, String appSecret, String rawBody, String signature) {
        if (!verify(appKey, appSecret, rawBody, signature)) {
            throw new WebhookSignatureException();
        }
        return parse(rawBody);
    }

    private static int typeOf(JsonElement t) {
        if (t == null || !t.isJsonPrimitive() || !((JsonPrimitive) t).isNumber()) {
            throw new IllegalArgumentException("webhook \"type\" is missing or not an integer");
        }
        String digits = t.getAsString();
        if (!digits.matches("-?\\d+")) {
            throw new IllegalArgumentException("webhook \"type\" is not an integer: " + digits);
        }
        try {
            return Integer.parseInt(digits);
        } catch (NumberFormatException e) {
            throw new IllegalArgumentException("webhook \"type\" is out of range: " + digits);
        }
    }

    private static String hex(byte[] bytes) {
        char[] digits = "0123456789abcdef".toCharArray();
        char[] out = new char[bytes.length * 2];
        for (int i = 0; i < bytes.length; i++) {
            out[2 * i] = digits[(bytes[i] >> 4) & 0xf];
            out[2 * i + 1] = digits[bytes[i] & 0xf];
        }
        return new String(out);
    }
}
