using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Net.Sockets;
using System.Text;
using System.Text.Json;
using System.Threading;
using System.Threading.Tasks;
using Xunit;

namespace TikTokShop.Api.Tests;

/// <summary>Finds the repo's committed shared files. Tests never read gitignored build output.</summary>
internal static class Repo
{
    public static string Root { get; } = FindRoot();

    private static string FindRoot()
    {
        for (var dir = new DirectoryInfo(AppContext.BaseDirectory); dir is not null; dir = dir.Parent)
        {
            if (File.Exists(Path.Combine(dir.FullName, "shared", "test-vectors", "signing.json")))
            {
                return dir.FullName;
            }
        }
        throw new InvalidOperationException("shared/test-vectors/signing.json not found above " + AppContext.BaseDirectory);
    }

    public static JsonElement Json(params string[] relative) =>
        JsonDocument.Parse(File.ReadAllText(Path.Combine(new[] { Root }.Concat(relative).ToArray()))).RootElement;
}

/// <summary>One request as it arrived on the wire.</summary>
internal sealed record RecordedRequest(string Method, string Target, IReadOnlyDictionary<string, string> Headers, byte[] Body)
{
    public string RawPath => Target.Contains('?') ? Target[..Target.IndexOf('?')] : Target;

    public string RawQuery => Target.Contains('?') ? Target[(Target.IndexOf('?') + 1)..] : "";

    /// <summary>The query as the server decodes it: percent-decoding only, a <c>+</c> stays a <c>+</c>.</summary>
    public List<KeyValuePair<string, string>> Query => RawQuery
        .Split('&', StringSplitOptions.RemoveEmptyEntries)
        .Select(part =>
        {
            var i = part.IndexOf('=');
            return new KeyValuePair<string, string>(Uri.UnescapeDataString(part[..i]), Uri.UnescapeDataString(part[(i + 1)..]));
        })
        .ToList();

    public string? Param(string name) => Query.Where(p => p.Key == name).Select(p => p.Value).SingleOrDefault();

    public string? Header(string name) => Headers.TryGetValue(name, out var v) ? v : null;

    public string BodyText => Encoding.UTF8.GetString(Body);
}

internal sealed record RawResponse(int Status, string Body, string ContentType = "application/json", string? Location = null)
{
    public static RawResponse Ok(string dataJson = "{}") =>
        new(200, "{\"code\":0,\"message\":\"Success\",\"request_id\":\"r1\",\"data\":" + dataJson + "}");
}

/// <summary>A real HTTP listener on loopback that records the raw requests it gets.</summary>
internal sealed class RawServer : IDisposable
{
    private readonly TcpListener _listener = new(IPAddress.Loopback, 0);
    private readonly Func<RecordedRequest, RawResponse?> _respond;
    private readonly CancellationTokenSource _stop = new();
    private readonly List<TcpClient> _clients = new();

    /// <param name="respond">The reply for a request; <c>null</c> holds the connection open and never answers.</param>
    public RawServer(Func<RecordedRequest, RawResponse?> respond)
    {
        _respond = respond;
        _listener.Start();
        _ = AcceptLoop();
    }

    public ConcurrentQueue<RecordedRequest> Requests { get; } = new();

    public int Port => ((IPEndPoint)_listener.LocalEndpoint).Port;

    public string BaseUrl => $"http://127.0.0.1:{Port}";

    public static int FreePort()
    {
        var l = new TcpListener(IPAddress.Loopback, 0);
        l.Start();
        var port = ((IPEndPoint)l.LocalEndpoint).Port;
        l.Stop();
        return port;
    }

    public RecordedRequest Single() => Assert.Single(Requests);

    private async Task AcceptLoop()
    {
        while (!_stop.IsCancellationRequested)
        {
            TcpClient client;
            try
            {
                client = await _listener.AcceptTcpClientAsync(_stop.Token);
            }
            catch
            {
                return;
            }
            lock (_clients)
            {
                _clients.Add(client);
            }
            _ = Task.Run(() => Handle(client));
        }
    }

    private async Task Handle(TcpClient client)
    {
        try
        {
            var stream = client.GetStream();
            var reader = new LineReader(stream);
            var requestLine = await reader.ReadLineAsync();
            if (requestLine is null)
            {
                return;
            }
            var parts = requestLine.Split(' ');
            var headers = new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);
            string? line;
            while (!string.IsNullOrEmpty(line = await reader.ReadLineAsync()))
            {
                var i = line.IndexOf(':');
                headers[line[..i].Trim()] = line[(i + 1)..].Trim();
            }

            byte[] body = Array.Empty<byte>();
            if (headers.TryGetValue("Transfer-Encoding", out var te) && te.Contains("chunked", StringComparison.OrdinalIgnoreCase))
            {
                using var ms = new MemoryStream();
                while (true)
                {
                    var sizeLine = (await reader.ReadLineAsync()) ?? "0";
                    var size = Convert.ToInt32(sizeLine.Split(';')[0].Trim(), 16);
                    if (size == 0)
                    {
                        while (!string.IsNullOrEmpty(await reader.ReadLineAsync())) { }
                        break;
                    }
                    var chunk = await reader.ReadExactAsync(size);
                    ms.Write(chunk, 0, chunk.Length);
                    await reader.ReadLineAsync();
                }
                body = ms.ToArray();
            }
            else if (headers.TryGetValue("Content-Length", out var cl))
            {
                body = await reader.ReadExactAsync(int.Parse(cl));
            }

            var recorded = new RecordedRequest(parts[0], parts[1], headers, body);
            Requests.Enqueue(recorded);

            var response = _respond(recorded);
            if (response is null)
            {
                await Task.Delay(Timeout.Infinite, _stop.Token);
                return;
            }
            var payload = Encoding.UTF8.GetBytes(response.Body);
            var head = $"HTTP/1.1 {response.Status} {Reason(response.Status)}\r\n"
                + $"Content-Type: {response.ContentType}\r\nContent-Length: {payload.Length}\r\nConnection: close\r\n"
                + (response.Location is null ? "" : $"Location: {response.Location}\r\n")
                + "\r\n";
            var headBytes = Encoding.ASCII.GetBytes(head);
            await stream.WriteAsync(headBytes);
            await stream.WriteAsync(payload);
            await stream.FlushAsync();
        }
        catch
        {
            // a client that went away
        }
        finally
        {
            client.Close();
        }
    }

    private static string Reason(int status) => status switch
    {
        200 => "OK",
        302 => "Found",
        503 => "Service Unavailable",
        _ => "Status",
    };

    public void Dispose()
    {
        _stop.Cancel();
        _listener.Stop();
        lock (_clients)
        {
            foreach (var c in _clients)
            {
                c.Close();
            }
        }
    }

    private sealed class LineReader
    {
        private readonly Stream _stream;
        private readonly byte[] _buffer = new byte[4096];
        private int _pos;
        private int _len;

        public LineReader(Stream stream) => _stream = stream;

        private async Task<int> ReadByteAsync()
        {
            if (_pos == _len)
            {
                _len = await _stream.ReadAsync(_buffer, 0, _buffer.Length);
                _pos = 0;
                if (_len == 0)
                {
                    return -1;
                }
            }
            return _buffer[_pos++];
        }

        public async Task<string?> ReadLineAsync()
        {
            var line = new List<byte>();
            while (true)
            {
                var b = await ReadByteAsync();
                if (b < 0)
                {
                    return line.Count == 0 ? null : Encoding.Latin1.GetString(line.ToArray());
                }
                if (b == '\n')
                {
                    if (line.Count > 0 && line[^1] == '\r')
                    {
                        line.RemoveAt(line.Count - 1);
                    }
                    return Encoding.Latin1.GetString(line.ToArray());
                }
                line.Add((byte)b);
            }
        }

        public async Task<byte[]> ReadExactAsync(int count)
        {
            var result = new byte[count];
            for (var i = 0; i < count; i++)
            {
                var b = await ReadByteAsync();
                if (b < 0)
                {
                    throw new EndOfStreamException();
                }
                result[i] = (byte)b;
            }
            return result;
        }
    }
}

/// <summary>A handler that fails every request with the exception the factory makes from it (it may print the request URI).</summary>
internal sealed class FailingHandler : HttpMessageHandler
{
    private readonly Func<HttpRequestMessage, Exception> _make;

    public FailingHandler(Func<HttpRequestMessage, Exception> make) => _make = make;

    protected override Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken) =>
        Task.FromException<HttpResponseMessage>(_make(request));
}

/// <summary>A pass-through <see cref="DelegatingHandler"/>, to put around another handler.</summary>
internal sealed class PassThroughHandler : DelegatingHandler
{
    public PassThroughHandler(HttpMessageHandler inner) : base(inner)
    {
    }
}

internal static class ErrorAssert
{
    /// <summary>Every message in the chain, then the full <c>ToString()</c>.</summary>
    public static IEnumerable<string> Texts(Exception e)
    {
        for (Exception? x = e; x is not null; x = x.InnerException)
        {
            yield return x.Message;
            yield return x.ToString();
        }
    }

    /// <summary>No secret, and no query-string fragment, anywhere in the message, <c>ToString()</c> or any inner exception.</summary>
    public static void NoneOf(Exception e, IEnumerable<string> forbidden)
    {
        var all = forbidden.ToList();
        foreach (var text in Texts(e))
        {
            foreach (var f in all)
            {
                Assert.DoesNotContain(f, text);
            }
        }
    }
}
