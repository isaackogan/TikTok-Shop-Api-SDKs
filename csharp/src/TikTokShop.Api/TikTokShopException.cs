using System;

namespace TikTokShop.Api;

/// <summary>
/// Every failure of an API call: a reply with a non-zero TikTok <c>code</c>, a non-2xx status, a 2xx reply that is not
/// understood, and a transport failure (connect refused, timeout, TLS, DNS).
/// </summary>
/// <remarks>
/// <see cref="Code"/> is: TikTok's non-zero code when the reply has one; otherwise the HTTP status for a non-2xx reply;
/// -1 for a 2xx reply that cannot be understood (not a JSON object, a <c>code</c> that is not an integer, or a body that
/// does not decode into its model, with the decoder's exception as <see cref="Exception.InnerException"/>) and for a
/// transport failure.
/// <see cref="HttpStatus"/> is <c>null</c> when no HTTP response arrived at all.
/// The message and the <see cref="Exception.InnerException"/> chain never contain the request's query string or any secret.
/// </remarks>
public class TikTokShopException : Exception
{
    /// <summary>Creates the exception.</summary>
    public TikTokShopException(string message, long code, string requestId = "", int? httpStatus = null, Exception? innerException = null)
        : base(message, innerException)
    {
        Code = code;
        RequestId = requestId;
        HttpStatus = httpStatus;
    }

    /// <summary>TikTok's error code, or the HTTP status, or -1, see the class remarks.</summary>
    public long Code { get; }

    /// <summary>The <c>message</c> from TikTok's reply, or a description when the reply had none.</summary>
    public string TikTokMessage => Message;

    /// <summary>The <c>request_id</c> from TikTok's reply, or an empty string.</summary>
    public string RequestId { get; }

    /// <summary>The HTTP status, or <c>null</c> when no response arrived.</summary>
    public int? HttpStatus { get; }

    /// <summary>
    /// R13d: a 2xx body that does not decode into its generated model. Called by the generated <c>ApiClient</c> (an asserted
    /// fix-up in <c>scripts/generate.ts</c>).
    /// </summary>
    internal static TikTokShopException DecodeFailure(int status, string? body, Exception decoderError)
    {
        var requestId = "";
        try
        {
            using var doc = System.Text.Json.JsonDocument.Parse(body ?? "");
            if (doc.RootElement.ValueKind == System.Text.Json.JsonValueKind.Object
                && doc.RootElement.TryGetProperty("request_id", out var r)
                && r.ValueKind == System.Text.Json.JsonValueKind.String)
            {
                requestId = r.GetString() ?? "";
            }
        }
        catch (System.Text.Json.JsonException)
        {
            // not JSON: no request ID
        }
        return new TikTokShopException($"Response does not match its model: {decoderError.Message}", -1, requestId, status, decoderError);
    }
}
