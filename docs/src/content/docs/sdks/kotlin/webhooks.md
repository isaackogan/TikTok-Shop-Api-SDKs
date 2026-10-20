---
title: Webhooks
description: Verify TikTok Shop webhook signatures and parse typed webhook events in Kotlin.
sidebar:
  order: 4
---

`Webhooks.verifyAndParse` checks TikTok's signature against the raw request body, then parses the body into a `WebhookEvent` you narrow with `when`. See [webhooks](/getting-started/webhooks/) for how TikTok signs and delivers them.

```kotlin
import com.isaackogan.tiktok.shop.WebhookEvent
import com.isaackogan.tiktok.shop.WebhookSignatureException
import com.isaackogan.tiktok.shop.Webhooks

class WebhookExample {
    /** Call with the body bytes exactly as received, and the Authorization header. */
    fun handle(rawBody: ByteArray, authorizationHeader: String?) {
        val event = try {
            Webhooks.verifyAndParse("YOUR_APP_KEY", "YOUR_APP_SECRET", rawBody, authorizationHeader)
        } catch (e: WebhookSignatureException) {
            return // respond 401
        }

        when (event) {
            is WebhookEvent.OrderStatusChange -> println(event.payload.data?.orderId)
            is WebhookEvent.Unknown -> println("a webhook type this SDK does not know: ${event.type}")
            else -> {}
        }
    }
}
```

`verifyAndParse`, `verify` and `parse` take the body as a `ByteArray` or a `String`.

## Rules

- **Verify the raw body.** Never re-serialize the body before verifying: changed bytes make the signature fail.
- **Parsing is strict.** `parse` throws `IllegalArgumentException` when:
  - the body is not a JSON object;
  - `type` is missing or is not an integer;
  - a known type is missing a required property, or the property is null. A known type missing a required field is always a parse error.
- **Unknown types are kept.** An integer `type` this SDK does not know becomes `WebhookEvent.Unknown(type, raw)`. Unknown fields are ignored.
- **A sealed class.** `WebhookEvent` has one subclass per webhook type (each holds the generated payload model in `payload`) plus `Unknown`. The subclasses are rendered from the spec, so they stay in sync. They live in the generated folder but in the package `com.isaackogan.tiktok.shop`, because a sealed class's subclasses must share its package.
- **Type names.** `Webhooks.EVENT_TYPES` maps a type number to its name; `1` is `ORDER_STATUS_CHANGE`.

## Exceptions

A bad signature throws `WebhookSignatureException`. A body that cannot be read as a webhook throws `IllegalArgumentException`. Answer the first with 401 and the second with 400, so neither is mistaken for success. The README example catches only `WebhookSignatureException`; add a second `catch` for `IllegalArgumentException` in a real handler.
