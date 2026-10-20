package com.isaackogan.tiktok.shop;

import java.io.ByteArrayOutputStream;
import java.io.Closeable;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.TimeUnit;
import okhttp3.HttpUrl;

/**
 * A minimal HTTP/1.1 server that accepts a request body on any method. MockWebServer refuses a GET that has a body ("Request
 * must not have a body"), and sending such a GET is exactly what the stub test has to observe.
 */
final class RawServer implements Closeable {
    /** What arrived. */
    static final class Received {
        String method;
        String target;
        final Map<String, String> headers = new HashMap<>(); // names lower-cased
        byte[] body = new byte[0];

        HttpUrl url() {
            return HttpUrl.parse("http://localhost" + target);
        }
    }

    private final ServerSocket socket;
    private final BlockingQueue<Received> received = new LinkedBlockingQueue<>();
    private volatile int status = 200;
    private volatile String reply = StubSupport.OK;
    private volatile boolean hang;
    private volatile boolean drip;
    private volatile String location;

    RawServer() throws IOException {
        socket = new ServerSocket(0);
        Thread t = new Thread(this::loop, "raw-server");
        t.setDaemon(true);
        t.start();
    }

    String baseUrl() {
        return "http://127.0.0.1:" + socket.getLocalPort();
    }

    RawServer respond(int status, String body) {
        this.status = status;
        this.reply = body;
        this.hang = false;
        return this;
    }

    /** Adds a Location header to the reply. */
    RawServer location(String url) {
        this.location = url;
        return this;
    }

    /** Sends the headers, then trickles the body one byte at a time, far slower than any test timeout. */
    RawServer drip() {
        this.drip = true;
        return this;
    }

    /** Reads the request and never answers. */
    RawServer hang() {
        this.hang = true;
        return this;
    }

    Received take() throws InterruptedException {
        Received r = received.poll(5, TimeUnit.SECONDS);
        if (r == null) {
            throw new AssertionError("no request arrived");
        }
        return r;
    }

    private void loop() {
        while (!socket.isClosed()) {
            try {
                Socket s = socket.accept();
                Thread h = new Thread(() -> handle(s));
                h.setDaemon(true);
                h.start();
            } catch (IOException e) {
                return;
            }
        }
    }

    private void handle(Socket s) {
        try (Socket sock = s) {
            InputStream in = sock.getInputStream();
            Received r = new Received();
            String requestLine = line(in);
            String[] parts = requestLine.split(" ");
            r.method = parts[0];
            r.target = parts[1];
            for (String l = line(in); !l.isEmpty(); l = line(in)) {
                int i = l.indexOf(':');
                r.headers.put(l.substring(0, i).trim().toLowerCase(), l.substring(i + 1).trim());
            }
            int n = Integer.parseInt(r.headers.getOrDefault("content-length", "0"));
            r.body = in.readNBytes(n);
            received.add(r);
            if (hang) {
                Thread.sleep(60_000);
                return;
            }
            if (drip) {
                OutputStream o = sock.getOutputStream();
                o.write("HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: 100\r\n\r\n".getBytes(StandardCharsets.UTF_8));
                o.flush();
                for (int i = 0; i < 100; i++) {
                    o.write(' ');
                    o.flush();
                    Thread.sleep(500);
                }
                return;
            }
            byte[] body = reply.getBytes(StandardCharsets.UTF_8);
            OutputStream out = sock.getOutputStream();
            out.write(("HTTP/1.1 " + status + " X\r\nContent-Type: application/json\r\n"
                    + (location == null ? "" : "Location: " + location + "\r\n") + "Content-Length: " + body.length
                    + "\r\nConnection: close\r\n\r\n").getBytes(StandardCharsets.UTF_8));
            out.write(body);
            out.flush();
        } catch (IOException | InterruptedException e) {
            // the client went away
        }
    }

    private static String line(InputStream in) throws IOException {
        ByteArrayOutputStream b = new ByteArrayOutputStream();
        for (int c = in.read(); c != '\n' && c != -1; c = in.read()) {
            if (c != '\r') {
                b.write(c);
            }
        }
        return b.toString("UTF-8");
    }

    @Override
    public void close() throws IOException {
        socket.close();
    }
}
