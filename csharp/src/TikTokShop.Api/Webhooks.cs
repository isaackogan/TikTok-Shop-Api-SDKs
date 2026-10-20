using System;
using System.Collections.Generic;
using System.IO;
using System.Numerics;
using System.Security.Cryptography;
using System.Text;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using Newtonsoft.Json.Serialization;
using TikTokShop.Api.Generated;

namespace TikTokShop.Api;

/// <summary>
/// Verifies and parses TikTok Shop webhooks.
/// </summary>
/// <remarks>
/// Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.
/// <code>
/// var e = Webhooks.VerifyAndParse(appKey, appSecret, rawBody, authorizationHeader);
/// if (e is OrderStatusChangeEvent order) { var id = order.Payload.Data.OrderId; }
/// </code>
/// </remarks>
public static class Webhooks
{
    private static readonly UTF8Encoding StrictUtf8 = new(false, true);

    // The generated client's own settings (ApiClient.SerializerSettings): its models rely on them.
    private static readonly JsonSerializer Serializer = JsonSerializer.Create(new JsonSerializerSettings
    {
        ConstructorHandling = ConstructorHandling.AllowNonPublicDefaultConstructor,
        ContractResolver = new DefaultContractResolver
        {
            NamingStrategy = new CamelCaseNamingStrategy { OverrideSpecifiedNames = false },
        },
    });

    /// <summary>Webhook type to event name, for example <c>1</c> to <c>ORDER_STATUS_CHANGE</c>.</summary>
    public static IReadOnlyDictionary<int, string> EventTypes => Meta.EventTypes;

    /// <summary>
    /// Checks the <c>Authorization</c> header: lowercase hex HMAC-SHA256 (key: the app secret) over the app key followed by the
    /// body, compared in constant time. A null or empty signature is false.
    /// </summary>
    /// <param name="appKey">Your app key.</param>
    /// <param name="appSecret">Your app secret.</param>
    /// <param name="rawBody">The body exactly as received (as UTF-8). Never re-serialize it.</param>
    /// <param name="signature">The <c>Authorization</c> header value.</param>
    public static bool Verify(string appKey, string appSecret, string rawBody, string? signature)
    {
        if (rawBody is null)
        {
            throw new ArgumentNullException(nameof(rawBody));
        }
        return Verify(appKey, appSecret, Encoding.UTF8.GetBytes(rawBody), signature);
    }

    /// <inheritdoc cref="Verify(string, string, string, string)"/>
    public static bool Verify(string appKey, string appSecret, ReadOnlySpan<byte> rawBody, string? signature)
    {
        if (appKey is null)
        {
            throw new ArgumentNullException(nameof(appKey));
        }
        if (appSecret is null)
        {
            throw new ArgumentNullException(nameof(appSecret));
        }
        if (string.IsNullOrEmpty(signature))
        {
            return false;
        }

        var key = Encoding.UTF8.GetBytes(appKey);
        var data = new byte[key.Length + rawBody.Length];
        key.CopyTo(data, 0);
        rawBody.CopyTo(data.AsSpan(key.Length));
        var expected = Convert.ToHexString(HMACSHA256.HashData(Encoding.UTF8.GetBytes(appSecret), data)).ToLowerInvariant();

        return CryptographicOperations.FixedTimeEquals(Encoding.UTF8.GetBytes(expected), Encoding.UTF8.GetBytes(signature));
    }

    /// <summary>
    /// Parses a body to its event, picked by the integer <c>type</c>. A <c>type</c> this SDK does not know gives an
    /// <see cref="UnknownWebhookEvent"/>. 64-bit IDs keep their exact digits, and unknown fields are accepted.
    /// Narrow the result with pattern matching, for example <c>case OrderStatusChangeEvent e:</c>, then read <c>e.Payload</c>.
    /// </summary>
    /// <param name="rawBody">The body.</param>
    /// <exception cref="WebhookParseException">
    /// The body is not a JSON object, its <c>type</c> is missing or not an integer (a string, boolean, null, fraction or array),
    /// or it does not fit the model of its type (a required property is missing).
    /// </exception>
    public static WebhookEvent Parse(string rawBody)
    {
        if (rawBody is null)
        {
            throw new ArgumentNullException(nameof(rawBody));
        }

        JToken token;
        try
        {
            using var text = new StringReader(rawBody);
            using var reader = new JsonTextReader(text) { DateParseHandling = DateParseHandling.None };
            token = JToken.ReadFrom(reader);
            while (reader.Read())
            {
                if (reader.TokenType != JsonToken.Comment)
                {
                    throw new JsonReaderException("Additional text found after the JSON value.");
                }
            }
        }
        catch (JsonException e)
        {
            throw new WebhookParseException("webhook body is not valid JSON: " + e.Message, e);
        }
        if (token is not JObject raw)
        {
            throw new WebhookParseException("webhook body is not a JSON object");
        }

        if (!raw.TryGetValue("type", out var typeToken) || typeToken is not JValue { Type: JTokenType.Integer } typeValue)
        {
            throw new WebhookParseException("webhook \"type\" is missing or not an integer");
        }
        var type = typeValue.Value switch
        {
            long l when l >= int.MinValue && l <= int.MaxValue => (int)l,
            long or BigInteger => throw new WebhookParseException($"webhook \"type\" is out of range: {typeValue}"),
            _ => throw new WebhookParseException("webhook \"type\" is missing or not an integer"),
        };

        try
        {
            return WebhookEvents.Create(type, raw, Serializer) ?? new UnknownWebhookEvent(type, raw);
        }
        catch (Exception e) when (e is JsonException or FormatException or InvalidCastException or OverflowException)
        {
            var schema = "";
            foreach (var w in Meta.Webhooks)
            {
                if (w.Type == type)
                {
                    schema = " (" + w.Schema + ")";
                }
            }
            throw new WebhookParseException($"webhook of type {type}{schema} does not match its model: {e.Message}", e);
        }
    }

    /// <inheritdoc cref="Parse(string)"/>
    /// <param name="rawBody">The body, as UTF-8.</param>
    public static WebhookEvent Parse(ReadOnlySpan<byte> rawBody)
    {
        string text;
        try
        {
            text = StrictUtf8.GetString(rawBody);
        }
        catch (DecoderFallbackException e)
        {
            throw new WebhookParseException("webhook body is not valid UTF-8", e);
        }
        return Parse(text.Length > 0 && text[0] == '\uFEFF' ? text[1..] : text);
    }

    /// <summary>Verifies, then parses.</summary>
    /// <exception cref="WebhookSignatureException">The signature does not match.</exception>
    /// <exception cref="WebhookParseException">As <see cref="Parse(string)"/>.</exception>
    public static WebhookEvent VerifyAndParse(string appKey, string appSecret, string rawBody, string? signature)
    {
        if (!Verify(appKey, appSecret, rawBody, signature))
        {
            throw new WebhookSignatureException();
        }
        return Parse(rawBody);
    }

    /// <inheritdoc cref="VerifyAndParse(string, string, string, string)"/>
    public static WebhookEvent VerifyAndParse(string appKey, string appSecret, ReadOnlySpan<byte> rawBody, string? signature)
    {
        if (!Verify(appKey, appSecret, rawBody, signature))
        {
            throw new WebhookSignatureException();
        }
        return Parse(rawBody);
    }
}
