using System;
using Newtonsoft.Json.Linq;

namespace TikTokShop.Api;

/// <summary>
/// A parsed webhook. <see cref="Webhooks.Parse(string)"/> returns one of the generated event classes (one per webhook type, for
/// example <c>OrderStatusChangeEvent</c>, each with a typed <c>Payload</c>) or an <see cref="UnknownWebhookEvent"/>.
/// Narrow it with pattern matching: <c>case OrderStatusChangeEvent e:</c>.
/// </summary>
public abstract class WebhookEvent
{
    /// <summary>Creates the event.</summary>
    protected WebhookEvent(int type, JObject raw)
    {
        Type = type;
        Raw = raw ?? throw new ArgumentNullException(nameof(raw));
    }

    /// <summary>The webhook's integer <c>type</c>.</summary>
    public int Type { get; }

    /// <summary>
    /// The body as parsed JSON, with every field TikTok sent, including those this SDK's models do not know. Do not modify it.
    /// </summary>
    public JObject Raw { get; }
}

/// <summary>A webhook whose <c>type</c> this SDK does not know: its type and its raw JSON.</summary>
public sealed class UnknownWebhookEvent : WebhookEvent
{
    /// <summary>Creates the event.</summary>
    public UnknownWebhookEvent(int type, JObject raw) : base(type, raw)
    {
    }
}

/// <summary>The signature of a webhook did not match.</summary>
public sealed class WebhookSignatureException : Exception
{
    /// <summary>Creates the exception.</summary>
    public WebhookSignatureException() : base("The webhook signature does not match the body.")
    {
    }
}

/// <summary>
/// A webhook body that cannot be parsed: not a JSON object, a <c>type</c> that is missing or not an integer, or a body that
/// does not fit the model of its type (the message names the field).
/// </summary>
public sealed class WebhookParseException : FormatException
{
    /// <summary>Creates the exception.</summary>
    public WebhookParseException(string message, Exception? innerException = null) : base(message, innerException)
    {
    }
}
