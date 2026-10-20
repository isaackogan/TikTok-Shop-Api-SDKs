---
title: Webhooks
description: Verify TikTok Shop webhook signatures and parse typed webhook events in Java.
sidebar:
  order: 4
---

`Webhooks.verifyAndParse` checks TikTok's signature against the raw request body, then parses the body into a typed event. See [webhooks](/getting-started/webhooks/) for how TikTok signs and delivers them.

```java
import com.isaackogan.tiktok.shop.WebhookEvent;
import com.isaackogan.tiktok.shop.WebhookSignatureException;
import com.isaackogan.tiktok.shop.Webhooks;
import com.isaackogan.tiktok.shop.generated.event.OrderStatusChangeEvent;
import com.isaackogan.tiktok.shop.generated.model.OrderStatusChangeWebhook;

class WebhookExample {
    /** Call with the body bytes exactly as received, and the Authorization header. */
    void handle(byte[] rawBody, String authorizationHeader) {
        WebhookEvent event;
        try {
            event = Webhooks.verifyAndParse("YOUR_APP_KEY", "YOUR_APP_SECRET", rawBody, authorizationHeader);
        } catch (WebhookSignatureException e) {
            return; // respond 401
        }

        if (event instanceof OrderStatusChangeEvent) {
            OrderStatusChangeWebhook order = ((OrderStatusChangeEvent) event).getPayload();
            System.out.println(order.getData().getOrderId());
        }
    }
}
```

`verifyAndParse`, `verify` and `parse` take the body as `byte[]` or as a `String` (its UTF-8 bytes are signed).

## Rules

- **Verify the raw body.** Never re-serialize the body before verifying: changed bytes make the signature fail.
- **Parsing is strict.** `parse` throws `IllegalArgumentException` when:
  - the body is not a JSON object;
  - `type` is missing or is not an integer;
  - a known type is missing a required field, or the field is null. A known type missing a required field is always a parse error.
- **Unknown types are kept.** A webhook type this SDK does not know comes back as an `UnknownWebhookEvent`, with `getType()` and `getRaw()`. Unknown fields are accepted.
- **Narrow the event.** A `WebhookEvent` is one of the generated event classes (`OrderStatusChangeEvent`, ...), each with `getPayload()`, or an `UnknownWebhookEvent`. Use `instanceof`, or `event.accept(visitor)` with a `WebhookEventVisitor`. `getType()` and `getRaw()` (the parsed JSON, with every field TikTok sent) are on every event.
- **Type names.** `Webhooks.EVENT_TYPES` maps a type number to its name; `1` is `ORDER_STATUS_CHANGE`.
- **IDs keep their digits.** Big IDs such as `shop_id` keep their exact digits.

## Exceptions

A bad signature throws `WebhookSignatureException`, an unchecked exception. A body that cannot be read as a webhook throws `IllegalArgumentException`. Answer the first with 401 and the second with 400, so neither is mistaken for success. The README example catches only `WebhookSignatureException`; add a second `catch` for `IllegalArgumentException` in a real handler.
