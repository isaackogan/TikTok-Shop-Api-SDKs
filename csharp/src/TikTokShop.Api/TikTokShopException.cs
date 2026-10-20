using System;

namespace TikTokShop.Api;

/// <summary>
/// Every failure of an API call: a reply with a non-zero TikTok <c>code</c>, a non-2xx status, a 2xx reply that is not
/// understood, and a transport failure (connect refused, timeout, TLS, DNS).
/// </summary>
/// <remarks>
/// <see cref="Code"/> is: TikTok's non-zero code when the reply has one; otherwise the HTTP status for a non-2xx reply;
/// -1 for a 2xx reply that is not a JSON object and for a transport failure.
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
}
