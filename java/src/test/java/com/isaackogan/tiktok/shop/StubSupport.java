package com.isaackogan.tiktok.shop;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import okhttp3.HttpUrl;
import okhttp3.mockwebserver.RecordedRequest;

/** Helpers shared by the stub-server tests. */
final class StubSupport {
    private StubSupport() {}

    static final String OK = "{\"code\":0,\"message\":\"Success\",\"request_id\":\"r0\",\"data\":{}}";

    /** The decoded query pairs of a received request, in arrival order. */
    static List<Signer.Param> query(RecordedRequest r) {
        return query(r.getRequestUrl());
    }

    static List<Signer.Param> query(HttpUrl url) {
        List<Signer.Param> out = new ArrayList<>();
        for (int i = 0; i < url.querySize(); i++) {
            out.add(new Signer.Param(url.queryParameterName(i), url.queryParameterValue(i)));
        }
        return out;
    }

    static Map<String, List<String>> queryMap(RecordedRequest r) {
        return queryMap(r.getRequestUrl());
    }

    static Map<String, List<String>> queryMap(HttpUrl url) {
        Map<String, List<String>> m = new TreeMap<>();
        for (Signer.Param p : query(url)) {
            m.computeIfAbsent(p.key, k -> new ArrayList<>()).add(p.value);
        }
        return m;
    }

    static String only(RecordedRequest r, String key) {
        return only(r.getRequestUrl(), key);
    }

    static String only(HttpUrl url, String key) {
        List<String> v = queryMap(url).get(key);
        if (v == null || v.size() != 1) {
            throw new AssertionError(key + " should appear exactly once, got " + v);
        }
        return v.get(0);
    }

    /** The signature the server would compute for what it received. */
    static String expectedSign(RecordedRequest r, String secret) {
        byte[] body = r.getBody().clone().readByteArray();
        return Signer.sign(new Signer.Request(r.getRequestUrl().encodedPath(), query(r), r.getHeader("Content-Type"),
                body.length == 0 ? null : body, secret));
    }

    static String expectedSign(RawServer.Received r, String secret) {
        return Signer.sign(new Signer.Request(r.url().encodedPath(), query(r.url()), r.headers.get("content-type"),
                r.body.length == 0 ? null : r.body, secret));
    }

    static void assertSigned(RawServer.Received r, String secret) {
        assertEquals(expectedSign(r, secret), only(r.url(), "sign"), "sign matches what was received");
    }

    static void assertSigned(RecordedRequest r, String secret) {
        assertEquals(expectedSign(r, secret), only(r, "sign"), "sign matches what was received");
    }
}
