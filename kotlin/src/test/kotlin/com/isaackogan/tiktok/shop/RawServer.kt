package com.isaackogan.tiktok.shop

import java.io.ByteArrayOutputStream
import java.io.Closeable
import java.io.IOException
import java.io.InputStream
import java.net.ServerSocket
import java.net.Socket
import java.util.concurrent.LinkedBlockingQueue
import java.util.concurrent.TimeUnit
import okhttp3.HttpUrl
import okhttp3.HttpUrl.Companion.toHttpUrl

/**
 * A minimal HTTP/1.1 server that accepts a request body on any method. MockWebServer refuses a GET that has a body, and
 * sending such a GET is exactly what the stub test has to observe.
 */
class RawServer : Closeable {
    class Received {
        lateinit var method: String
        lateinit var target: String
        val headers = HashMap<String, String>() // names lower-cased
        var body = ByteArray(0)

        fun url(): HttpUrl = "http://localhost$target".toHttpUrl()
    }

    private val socket = ServerSocket(0)
    private val received = LinkedBlockingQueue<Received>()

    @Volatile private var status = 200

    @Volatile private var reply = StubSupport.OK

    @Volatile private var hang = false

    @Volatile private var drip = false

    init {
        Thread(::loop, "raw-server").apply { isDaemon = true }.start()
    }

    fun baseUrl() = "http://127.0.0.1:${socket.localPort}"

    fun respond(status: Int, body: String): RawServer {
        this.status = status
        reply = body
        hang = false
        return this
    }

    /** Sends the headers, then trickles the body one byte at a time, far slower than any test timeout. */
    fun drip(): RawServer {
        drip = true
        return this
    }

    /** Reads the request and never answers. */
    fun hang(): RawServer {
        hang = true
        return this
    }

    fun take(): Received = received.poll(5, TimeUnit.SECONDS) ?: throw AssertionError("no request arrived")

    private fun loop() {
        while (!socket.isClosed) {
            try {
                val s = socket.accept()
                Thread { handle(s) }.apply { isDaemon = true }.start()
            } catch (e: IOException) {
                return
            }
        }
    }

    private fun handle(s: Socket) {
        try {
            s.use { sock ->
                val input = sock.getInputStream()
                val r = Received()
                val parts = line(input).split(" ")
                r.method = parts[0]
                r.target = parts[1]
                var l = line(input)
                while (l.isNotEmpty()) {
                    val i = l.indexOf(':')
                    r.headers[l.substring(0, i).trim().lowercase()] = l.substring(i + 1).trim()
                    l = line(input)
                }
                r.body = input.readNBytes((r.headers["content-length"] ?: "0").toInt())
                received.add(r)
                val out = sock.getOutputStream()
                if (hang) {
                    Thread.sleep(60_000)
                    return
                }
                if (drip) {
                    out.write("HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: 100\r\n\r\n".toByteArray())
                    out.flush()
                    repeat(100) {
                        out.write(' '.code)
                        out.flush()
                        Thread.sleep(500)
                    }
                    return
                }
                val body = reply.toByteArray()
                out.write("HTTP/1.1 $status X\r\nContent-Type: application/json\r\nContent-Length: ${body.size}\r\nConnection: close\r\n\r\n".toByteArray())
                out.write(body)
                out.flush()
            }
        } catch (_: IOException) {
            // the client went away
        } catch (_: InterruptedException) {
        }
    }

    private fun line(input: InputStream): String {
        val b = ByteArrayOutputStream()
        var c = input.read()
        while (c != '\n'.code && c != -1) {
            if (c != '\r'.code) b.write(c)
            c = input.read()
        }
        return b.toString("UTF-8")
    }

    override fun close() = socket.close()
}
