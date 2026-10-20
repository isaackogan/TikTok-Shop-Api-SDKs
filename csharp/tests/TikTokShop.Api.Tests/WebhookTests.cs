using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Text.Json;
using Newtonsoft.Json.Linq;
using TikTokShop.Api.Generated;
using TikTokShop.Api.Generated.Model;
using Xunit;

namespace TikTokShop.Api.Tests;

public class WebhookTests
{
    private static readonly JsonElement Vectors = Repo.Json("shared", "test-vectors", "webhooks.json");

    private const string AppKey = "abcdef";
    private const string AppSecret = "123";

    private const string OrderBody =
        "{\"type\":1,\"tts_notification_id\":\"7380066284010030890\",\"shop_id\":\"7495540735365777507\",\"timestamp\":1718305585,"
        + "\"data\":{\"is_on_hold_order\":true,\"order_id\":\"576653688135258178\",\"order_status\":\"UNPAID\",\"update_time\":1718305585}}";

    // ---- verify ----

    public static IEnumerable<object[]> VerifyCases() =>
        Enumerable.Range(0, Vectors.GetProperty("verify").GetArrayLength()).Select(i => new object[] { i }).ToList();

    [Theory]
    [MemberData(nameof(VerifyCases))]
    public void VerifyMatchesTheSharedVector(int index)
    {
        var c = Vectors.GetProperty("verify")[index];
        var body = c.GetProperty("rawBody").GetString()!;
        var expected = c.GetProperty("valid").GetBoolean();

        Assert.Equal(expected, Webhooks.Verify(c.GetProperty("appKey").GetString()!, c.GetProperty("appSecret").GetString()!, body, c.GetProperty("signature").GetString()));
        Assert.Equal(expected, Webhooks.Verify(c.GetProperty("appKey").GetString()!, c.GetProperty("appSecret").GetString()!, Encoding.UTF8.GetBytes(body), c.GetProperty("signature").GetString()));
    }

    [Fact]
    public void ANullSignatureOrALengthMismatchIsFalse()
    {
        Assert.False(Webhooks.Verify(AppKey, AppSecret, OrderBody, null));
        Assert.False(Webhooks.Verify(AppKey, AppSecret, OrderBody, "5dec"));
        Assert.False(Webhooks.Verify(AppKey, AppSecret, OrderBody, "5dec0f11ec2f6783b8deee53c9ffbf8d024302f7c7e7fa55a35d17629031ac05ff"));
    }

    [Fact]
    public void TheBodyIsHashedAsReceivedNotReserialized()
    {
        var signature = "5dec0f11ec2f6783b8deee53c9ffbf8d024302f7c7e7fa55a35d17629031ac05";

        Assert.True(Webhooks.Verify(AppKey, AppSecret, OrderBody, signature));
        Assert.False(Webhooks.Verify(AppKey, AppSecret, OrderBody + " ", signature));
    }

    // ---- parse: the shared vectors ----

    public static IEnumerable<object[]> ParseCases() =>
        Enumerable.Range(0, Vectors.GetProperty("parse").GetArrayLength()).Select(i => new object[] { i }).ToList();

    [Theory]
    [MemberData(nameof(ParseCases))]
    public void ParseMatchesTheSharedVector(int index)
    {
        var c = Vectors.GetProperty("parse")[index];

        var e = Webhooks.Parse(c.GetProperty("rawBody").GetString()!);

        Assert.Equal(c.GetProperty("type").GetInt32(), e.Type);
        if (c.GetProperty("known").GetBoolean())
        {
            var schema = c.GetProperty("schema").GetString()!;
            Assert.IsNotType<UnknownWebhookEvent>(e);
            Assert.Equal(schema, e.GetType().GetProperty("Payload")!.PropertyType.Name);
        }
        else
        {
            Assert.IsType<UnknownWebhookEvent>(e);
        }
        Assert.Equal(c.GetProperty("type").GetInt32(), (int)e.Raw["type"]!);
    }

    [Fact]
    public void ACallerNarrowsTheResultWithPatternMatching()
    {
        var e = Webhooks.Parse(OrderBody);

        string seen;
        switch (e)
        {
            case OrderStatusChangeEvent order:
                seen = order.Payload.Data.OrderId + "/" + order.Payload.Data.OrderStatus + "/" + order.Payload.ShopId;
                Assert.Equal(OrderStatusChangeWebhook.TypeEnum.NUMBER_1, order.Payload.Type);
                Assert.Equal(1718305585, order.Payload.Timestamp);
                Assert.True(order.Payload.Data.IsOnHoldOrder);
                break;
            default:
                seen = "other";
                break;
        }

        Assert.Equal("576653688135258178/UNPAID/7495540735365777507", seen);
        Assert.Equal(1, e.Type);
    }

    [Fact]
    public void AnUnknownTypeIsTheGenericEventWithTheRawJson()
    {
        var e = Webhooks.Parse("{\"type\":9999,\"shop_id\":\"1\",\"data\":{\"x\":[1,2]}}");

        var unknown = Assert.IsType<UnknownWebhookEvent>(e);
        Assert.Equal(9999, unknown.Type);
        Assert.Equal("1", (string?)unknown.Raw["shop_id"]);
        Assert.Equal(2, ((JArray)unknown.Raw["data"]!["x"]!).Count);
    }

    [Fact]
    public void TheRawJsonOfAKnownEventKeepsEveryField()
    {
        var e = Webhooks.Parse(OrderBody.Replace("\"timestamp\"", "\"brand_new\":true,\"timestamp\""));

        Assert.True((bool)e.Raw["brand_new"]!);
    }

    // ---- exact 64-bit ids ----

    [Theory]
    [InlineData("7494049642642441621", "7494049642642441621")]
    [InlineData("18446744073709551615", "18446744073709551615")] // beyond long, uint64 max
    [InlineData("99999999999999999999", "99999999999999999999")] // beyond 64 bits
    [InlineData("-7494049642642441621", "-7494049642642441621")]
    [InlineData("\"7494049642642441621\"", "7494049642642441621")]
    public void ANineteenDigitShopIdSentAsAJsonNumberKeepsItsExactValueAsAString(string json, string expected)
    {
        var e = Webhooks.Parse("{\"type\":1,\"tts_notification_id\":\"n\",\"shop_id\":" + json + ",\"timestamp\":1,\"data\":{\"order_id\":\"576653688135258178\"}}");

        var order = Assert.IsType<OrderStatusChangeEvent>(e);
        Assert.Equal(expected, order.Payload.ShopId);
    }

    [Fact]
    public void AnIdSentAsAnIntegerNumberIsExactEvenInATenDigitOrderId()
    {
        var e = Webhooks.Parse("{\"type\":1,\"shop_id\":7494049642642441621,\"data\":{\"order_id\":576653688135258178}}");

        var order = Assert.IsType<OrderStatusChangeEvent>(e);
        Assert.Equal("7494049642642441621", order.Payload.ShopId);
        Assert.Equal("576653688135258178", order.Payload.Data.OrderId);
    }

    // ---- the type field ----

    [Theory]
    [InlineData("{\"shop_id\":\"1\"}")]
    [InlineData("{\"type\":\"1\",\"shop_id\":\"1\"}")]
    [InlineData("{\"type\":true}")]
    [InlineData("{\"type\":false}")]
    [InlineData("{\"type\":null}")]
    [InlineData("{\"type\":1.0}")]
    [InlineData("{\"type\":1.5}")]
    [InlineData("{\"type\":1e0}")]
    [InlineData("{\"type\":[1]}")]
    [InlineData("{\"type\":{\"a\":1}}")]
    [InlineData("{\"type\":\"\"}")]
    [InlineData("{\"type\":99999999999}")]
    [InlineData("{\"type\":99999999999999999999}")]
    [InlineData("[1,2]")]
    [InlineData("\"text\"")]
    [InlineData("null")]
    [InlineData("12")]
    [InlineData("")]
    [InlineData("not json")]
    [InlineData("{\"type\":1} trailing")]
    [InlineData("{\"type\":1")]
    public void AMissingOrNonIntegerTypeIsRejected(string body)
    {
        var e = Assert.Throws<WebhookParseException>(() => Webhooks.Parse(body));

        Assert.False(string.IsNullOrWhiteSpace(e.Message));
    }

    [Fact]
    public void ANullBodyIsAnArgumentNullException()
    {
        Assert.Throws<ArgumentNullException>(() => Webhooks.Parse((string)null!));
    }

    [Fact]
    public void AByteBodyParsesLikeAStringBody()
    {
        var e = Webhooks.Parse(Encoding.UTF8.GetBytes(OrderBody));

        Assert.IsType<OrderStatusChangeEvent>(e);
        Assert.Throws<WebhookParseException>(() => Webhooks.Parse(new byte[] { 0xff, 0xfe, 0x7b }));
    }

    // ---- unknown fields ----

    [Fact]
    public void AWebhookWithUnknownFieldsStillParses()
    {
        const string body =
            "{\"type\":1,\"brand_new_top\":{\"a\":1},\"tts_notification_id\":\"n\",\"shop_id\":\"s\",\"timestamp\":1,"
            + "\"data\":{\"new_in_data\":[1],\"order_id\":\"o\",\"order_status\":\"PAID\",\"is_on_hold_order\":false,\"update_time\":2}}";

        var order = Assert.IsType<OrderStatusChangeEvent>(Webhooks.Parse(body));

        Assert.Equal("o", order.Payload.Data.OrderId);
        Assert.True(order.Payload.AdditionalProperties.ContainsKey("brand_new_top"));
        Assert.True(order.Payload.Data.AdditionalProperties.ContainsKey("new_in_data"));
    }

    // ---- a known type that does not fit its model ----

    private static int TypeOf(string schema) => Meta.Webhooks.Single(w => w.Schema == schema).Type;

    [Fact]
    public void AKnownTypeMissingARequiredFieldIsRejectedNamingTheField()
    {
        var type = TypeOf("AppealCompletedWebhook");
        var body = "{\"type\":" + type + ",\"shop_id\":\"1\",\"tts_notification_id\":\"n\",\"timestamp\":1}";

        var e = Assert.Throws<WebhookParseException>(() => Webhooks.Parse(body));

        Assert.Contains("data", e.Message);
        Assert.Contains("AppealCompletedWebhook", e.Message);
        Assert.NotNull(e.InnerException);
    }

    [Fact]
    public void ARequiredFieldMissingInANestedModelIsRejectedNamingTheField()
    {
        var type = TypeOf("AppealCompletedWebhook");
        var body = "{\"type\":" + type + ",\"shop_id\":\"1\",\"tts_notification_id\":\"n\",\"timestamp\":1,\"data\":{\"product_id\":\"9\"}}";

        var e = Assert.Throws<WebhookParseException>(() => Webhooks.Parse(body));

        Assert.Contains("appeal_task", e.Message);
    }

    [Fact]
    public void AFieldOfTheWrongTypeIsRejectedAsAParseError()
    {
        var e = Assert.Throws<WebhookParseException>(() => Webhooks.Parse("{\"type\":1,\"timestamp\":\"not a number\"}"));

        Assert.Contains("timestamp", e.Message);
    }

    // ---- verifyAndParse ----

    [Fact]
    public void VerifyAndParseReturnsTheEventForAValidSignature()
    {
        var signature = "5dec0f11ec2f6783b8deee53c9ffbf8d024302f7c7e7fa55a35d17629031ac05";

        Assert.IsType<OrderStatusChangeEvent>(Webhooks.VerifyAndParse(AppKey, AppSecret, OrderBody, signature));
        Assert.IsType<OrderStatusChangeEvent>(Webhooks.VerifyAndParse(AppKey, AppSecret, Encoding.UTF8.GetBytes(OrderBody), signature));
    }

    [Theory]
    [InlineData(null)]
    [InlineData("")]
    [InlineData("0000")]
    [InlineData("5DEC0F11EC2F6783B8DEEE53C9FFBF8D024302F7C7E7FA55A35D17629031AC05")]
    public void VerifyAndParseThrowsWebhookSignatureExceptionOtherwise(string? signature)
    {
        Assert.Throws<WebhookSignatureException>(() => Webhooks.VerifyAndParse(AppKey, AppSecret, OrderBody, signature));
        Assert.Throws<WebhookSignatureException>(() => Webhooks.VerifyAndParse(AppKey, AppSecret, Encoding.UTF8.GetBytes(OrderBody), signature));
    }

    // ---- event types and the generated events ----

    [Fact]
    public void EventTypesIsTheSpecsMap()
    {
        var fromMeta = Meta.Webhooks.Where(w => w.EventType is not null).ToDictionary(w => w.Type, w => w.EventType!);

        Assert.Equal(fromMeta.OrderBy(p => p.Key), Webhooks.EventTypes.OrderBy(p => p.Key));
        Assert.Equal("ORDER_STATUS_CHANGE", Webhooks.EventTypes[1]);
    }

    private static IEnumerable<Type> EventClasses() =>
        typeof(WebhookEvent).Assembly.GetTypes().Where(t => t.IsSubclassOf(typeof(WebhookEvent)) && t != typeof(UnknownWebhookEvent));

    [Fact]
    public void ThereIsOneSealedEventClassPerWebhookWithATypedPayload()
    {
        var classes = EventClasses().ToList();
        Assert.Equal(Meta.Webhooks.Count, classes.Count);

        foreach (var w in Meta.Webhooks)
        {
            var name = w.Schema[..^"Webhook".Length] + "Event";
            var type = typeof(WebhookEvent).Assembly.GetType("TikTokShop.Api." + name);
            Assert.True(type is not null, $"{name} is missing");
            Assert.True(type!.IsPublic && type.IsSealed, $"{name} should be public and sealed");
            Assert.True(type.IsSubclassOf(typeof(WebhookEvent)));
            var payload = type.GetProperty("Payload", BindingFlags.Public | BindingFlags.Instance);
            Assert.NotNull(payload);
            Assert.Equal(typeof(OrderStatusChangeWebhook).Assembly.GetType("TikTokShop.Api.Generated.Model." + w.Schema), payload!.PropertyType);
            Assert.Equal(w.Type, (int)type.GetField("TypeCode", BindingFlags.Public | BindingFlags.Static)!.GetRawConstantValue()!);
        }
    }

    [Fact]
    public void EveryWebhookTypeParsesToItsOwnEventOrNamesAMissingField()
    {
        foreach (var w in Meta.Webhooks)
        {
            var body = "{\"type\":" + w.Type + "}";
            try
            {
                var e = Webhooks.Parse(body);
                Assert.Equal(w.Type, e.Type);
                Assert.Equal(w.Schema[..^"Webhook".Length] + "Event", e.GetType().Name);
            }
            catch (WebhookParseException ex)
            {
                // Only a required property may stop a bare body; never "unknown type".
                Assert.Contains("Required property", ex.Message);
            }
        }
    }
}
