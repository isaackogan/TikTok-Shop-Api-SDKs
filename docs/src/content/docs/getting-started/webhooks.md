---
title: Webhooks
description: Verify TikTok Shop webhook signatures against the raw body and parse webhooks into typed events.
sidebar:
  order: 3
---

TikTok Shop sends webhooks as HTTP POST requests with a JSON body. The spec describes 44 webhooks under the OpenAPI 3.1 `webhooks` section. Each has a numeric `type`, for example `1` for an order status change. Every SDK verifies the signature and parses the body into that type's generated model.

## Signature

Every webhook carries an `Authorization` header. It is not a bearer token. It holds the lowercase hex HMAC-SHA256, keyed with your app secret, of your app key followed by the raw request body:

```text
Authorization: hex(HMAC-SHA256(key = app_secret, message = app_key + raw_body))
```

The SDKs compare signatures in constant time. The signature covers the exact bytes TikTok sent, so:
- **Verify before parsing.** Pass the body as bytes or a string exactly as received.
- **Never re-serialize it.** Don't parse and re-encode the body, or let a framework's JSON middleware consume it, before verifying. Changed whitespace or key order makes the signature fail.

## Payload

The top-level fields are `type`, `tts_notification_id`, `shop_id`, `timestamp` and `data`. `data` depends on the type. The [API reference](/openapi/reference/) has every webhook's schema, under Webhooks.

## Parsing rules

Parsing is strict, and identical in every SDK. The body is a parse error when:
- it isn't a JSON object;
- its `type` is missing or isn't an integer (a string, boolean, null or float all fail);
- it is a known type with a required field missing or null, at any depth. A known type missing a required field is always a parse error;
- a field that should hold a model isn't a JSON object, at any depth.

A `type` the SDK doesn't know is not an error. It comes back as an unknown-event value holding the type and the raw JSON, so a webhook TikTok adds later doesn't fail your endpoint before you upgrade.

Respond with a 2xx status quickly, and do slow work after acknowledging. Answer a bad signature with 401 and a parse error with 400, so neither looks like success.

## By language

| SDK | Verify and parse | Signature error | Parse error |
| --- | --- | --- | --- |
| [TypeScript](/sdks/typescript/webhooks/) | `Webhooks.verifyAndParse` | `WebhookSignatureError` | `WebhookParseError` |
| [Python](/sdks/python/webhooks/) | `Webhooks.verify_and_parse` | `WebhookSignatureError` | `ValueError` |
| [Go](/sdks/go/webhooks/) | `tiktokshop.Webhooks.VerifyAndParse` | `ErrWebhookSignature` | a returned `error` |
| [Java](/sdks/java/webhooks/) | `Webhooks.verifyAndParse` | `WebhookSignatureException` | `IllegalArgumentException` |
| [Kotlin](/sdks/kotlin/webhooks/) | `Webhooks.verifyAndParse` | `WebhookSignatureException` | `IllegalArgumentException` |
| [PHP](/sdks/php/webhooks/) | `Webhooks::verifyAndParse` | `WebhookSignatureException` | `InvalidArgumentException` |
| [Rust](/sdks/rust/webhooks/) | `webhooks::verify_and_parse` | `Error::WebhookSignature` | `Error::Webhook` |
| [C#](/sdks/csharp/webhooks/) | `Webhooks.VerifyAndParse` | `WebhookSignatureException` | `WebhookParseException` |

Each SDK also has separate verify and parse functions, for when you verify in middleware and parse later.
