package com.isaackogan.tiktok.shop;

import java.io.ByteArrayOutputStream;
import java.nio.charset.StandardCharsets;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Locale;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

/**
 * TikTok Shop request signing: pure functions, no I/O.
 *
 * <p>The string to sign is {@code secret + path + the sorted key+value pairs (without sign and access_token) + the body
 * (unless the body is multipart/form-data) + secret}. The signature is the lowercase hex HMAC-SHA256 of that string, keyed
 * with the app secret.
 */
public final class Signer {
    private Signer() {}

    /** One query parameter with its decoded value, exactly as the server receives it. */
    public static final class Param {
        public final String key;
        public final String value;

        public Param(String key, String value) {
            this.key = key;
            this.value = value;
        }
    }

    /** What the signature covers. */
    public static final class Request {
        /** The request path, e.g. "/order/202309/orders/search". */
        public final String path;
        /** The query, with decoded values. */
        public final List<Param> query;
        /** The Content-Type header, or null. A multipart/form-data body is not signed. */
        public final String contentType;
        /** The exact request body, or null. */
        public final byte[] body;
        public final String appSecret;

        public Request(String path, List<Param> query, String contentType, byte[] body, String appSecret) {
            this.path = path;
            this.query = query;
            this.contentType = contentType;
            this.body = body;
            this.appSecret = appSecret;
        }
    }

    private static final Comparator<Param> BY_KEY_BYTES = (a, b) -> {
        byte[] x = a.key.getBytes(StandardCharsets.UTF_8);
        byte[] y = b.key.getBytes(StandardCharsets.UTF_8);
        int n = Math.min(x.length, y.length);
        for (int i = 0; i < n; i++) {
            int d = (x[i] & 0xff) - (y[i] & 0xff);
            if (d != 0) {
                return d;
            }
        }
        return x.length - y.length;
    };

    static boolean isMultipart(String contentType) {
        return contentType != null && contentType.toLowerCase(Locale.ROOT).startsWith("multipart/form-data");
    }

    private static byte[] bytesToSign(Request r) {
        List<Param> pairs = new ArrayList<>();
        for (Param p : r.query) {
            if (!p.key.equals("sign") && !p.key.equals("access_token")) {
                pairs.add(p);
            }
        }
        pairs.sort(BY_KEY_BYTES); // stable
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        write(out, r.appSecret);
        write(out, r.path);
        for (Param p : pairs) {
            write(out, p.key);
            write(out, p.value);
        }
        if (r.body != null && !isMultipart(r.contentType)) {
            out.write(r.body, 0, r.body.length);
        }
        write(out, r.appSecret);
        return out.toByteArray();
    }

    private static void write(ByteArrayOutputStream out, String s) {
        byte[] b = s.getBytes(StandardCharsets.UTF_8);
        out.write(b, 0, b.length);
    }

    /** The string the signature is computed over. */
    public static String stringToSign(Request r) {
        return new String(bytesToSign(r), StandardCharsets.UTF_8);
    }

    /** The signature: lowercase hex HMAC-SHA256 of {@link #stringToSign}, keyed with the app secret. */
    public static String sign(Request r) {
        try {
            Mac mac = Mac.getInstance("HmacSHA256");
            mac.init(new SecretKeySpec(r.appSecret.getBytes(StandardCharsets.UTF_8), "HmacSHA256"));
            byte[] sig = mac.doFinal(bytesToSign(r));
            StringBuilder hex = new StringBuilder(sig.length * 2);
            for (byte b : sig) {
                hex.append(Character.forDigit((b >> 4) & 0xf, 16)).append(Character.forDigit(b & 0xf, 16));
            }
            return hex.toString();
        } catch (NoSuchAlgorithmException | InvalidKeyException e) {
            throw new IllegalStateException(e); // HmacSHA256 is required of every JRE; an empty key is accepted
        }
    }
}
