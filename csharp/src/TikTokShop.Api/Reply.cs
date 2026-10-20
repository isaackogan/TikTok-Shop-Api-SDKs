using System;
using System.Globalization;
using System.Text.Json;

namespace TikTokShop.Api;

/// <summary>
/// A reply read the one way both the API calls and the token calls read it (R13b): the exception it stands for, or, for a
/// 2xx reply with <c>code</c> 0 (or none), its parsed JSON object.
/// </summary>
internal sealed class Reply : IDisposable
{
    private readonly JsonDocument? _document;

    private Reply(JsonDocument? document, TikTokShopException? error, string requestId, int status)
    {
        _document = document;
        Error = error;
        RequestId = requestId;
        Status = status;
    }

    /// <summary>What the reply stands for when it is a failure; <c>null</c> for a good reply.</summary>
    public TikTokShopException? Error { get; }

    /// <summary>The <c>request_id</c> of the reply, or an empty string.</summary>
    public string RequestId { get; }

    /// <summary>The HTTP status.</summary>
    public int Status { get; }

    /// <summary>The JSON object of a good reply.</summary>
    public JsonElement Root => _document!.RootElement;

    /// <summary>Whether <paramref name="raw"/> (a number's text) is a plain integer: no fraction, no exponent.</summary>
    public static bool IsIntegerLiteral(string raw)
    {
        if (raw.Length == 0)
        {
            return false;
        }
        var start = raw[0] == '-' ? 1 : 0;
        if (start == raw.Length)
        {
            return false;
        }
        for (var i = start; i < raw.Length; i++)
        {
            if (raw[i] is < '0' or > '9')
            {
                return false;
            }
        }
        return true;
    }

    /// <summary>A JSON number that is an integer fitting 64 bits.</summary>
    public static bool TryGetInteger(JsonElement element, out long value)
    {
        value = 0;
        return element.ValueKind == JsonValueKind.Number
            && IsIntegerLiteral(element.GetRawText())
            && long.TryParse(element.GetRawText(), NumberStyles.AllowLeadingSign, CultureInfo.InvariantCulture, out value);
    }

    /// <summary>
    /// Reads a reply.
    /// A non-2xx reply is an error whose code is TikTok's non-zero <c>code</c> if the body has one, else the status.
    /// A 2xx reply is an error with TikTok's code when that is non-zero, and with -1 when it cannot be understood: not a JSON
    /// object, or a <c>code</c> that is not an integer.
    /// </summary>
    /// <param name="status">The HTTP status.</param>
    /// <param name="reason">The reason phrase, used as the message of a non-2xx reply that has none.</param>
    /// <param name="payload">The body.</param>
    /// <param name="what">"Response" or "Token response", for messages.</param>
    public static Reply Read(int status, string? reason, byte[] payload, string what)
    {
        var ok = status is >= 200 and < 300;

        JsonDocument? doc = null;
        Exception? parseError = null;
        try
        {
            doc = JsonDocument.Parse(payload, new JsonDocumentOptions { MaxDepth = 1024 });
        }
        catch (JsonException e)
        {
            parseError = e;
        }

        var isObject = doc is not null && doc.RootElement.ValueKind == JsonValueKind.Object;
        if (ok && !isObject)
        {
            doc?.Dispose();
            return new Reply(null, new TikTokShopException($"{what} is not a JSON object (HTTP {status})", -1, "", status, parseError), "", status);
        }

        long? code = null;
        var codeUnreadable = false;
        string? message = null;
        var requestId = "";
        if (isObject)
        {
            var root = doc!.RootElement;
            if (root.TryGetProperty("code", out var c) && c.ValueKind != JsonValueKind.Null)
            {
                if (TryGetInteger(c, out var ci))
                {
                    code = ci;
                }
                else
                {
                    codeUnreadable = true;
                }
            }
            if (root.TryGetProperty("message", out var m) && m.ValueKind == JsonValueKind.String)
            {
                message = m.GetString();
            }
            if (root.TryGetProperty("request_id", out var r) && r.ValueKind == JsonValueKind.String)
            {
                requestId = r.GetString() ?? "";
            }
        }

        TikTokShopException? error = null;
        if (!ok)
        {
            error = new TikTokShopException(
                message ?? (!string.IsNullOrEmpty(reason) ? reason : $"HTTP {status}"),
                code.HasValue && code.Value != 0 ? code.Value : status,
                requestId,
                status);
        }
        else if (codeUnreadable)
        {
            error = new TikTokShopException(message ?? $"{what} has a code that is not an integer", -1, requestId, status);
        }
        else if (code.HasValue && code.Value != 0)
        {
            error = new TikTokShopException(message ?? "", code.Value, requestId, status);
        }

        if (error is not null)
        {
            doc?.Dispose();
            return new Reply(null, error, requestId, status);
        }
        return new Reply(doc, null, requestId, status);
    }

    /// <inheritdoc/>
    public void Dispose() => _document?.Dispose();
}
