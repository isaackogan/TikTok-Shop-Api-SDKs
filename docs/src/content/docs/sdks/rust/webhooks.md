---
title: Webhooks
description: Verify TikTok Shop webhook signatures and parse typed webhook events in Rust.
sidebar:
  order: 4
---

`webhooks::verify_and_parse` checks the signature (HMAC-SHA256 over the app key plus the raw body) and returns a `WebhookEvent`, an enum with one variant per webhook holding that webhook's generated model. See [webhooks](/getting-started/webhooks/) for how TikTok signs and delivers them.

```rust
use tiktok_shop_api::{webhooks, Error, WebhookEvent};

/// Call this with the request body exactly as received and the `Authorization` header.
fn handle(raw_body: &[u8], authorization: &str) -> u16 {
    match webhooks::verify_and_parse("APP_KEY", "APP_SECRET", raw_body, authorization) {
        Err(Error::WebhookSignature) => 401,
        Err(_) => 400,
        Ok(WebhookEvent::OrderStatusChange(e)) => {
            if let Some(data) = &e.data {
                println!("order {:?} is now {:?} in shop {:?}", data.order_id, data.order_status, e.shop_id);
            }
            200
        }
        Ok(WebhookEvent::ReturnStatusChange(e)) => {
            println!("return in order {:?}", e.data.and_then(|d| d.order_id));
            200
        }
        Ok(WebhookEvent::Unknown { event_type, .. }) => {
            println!("unhandled webhook type {event_type}");
            200
        }
        // WebhookEvent is non_exhaustive: new webhook types arrive with new releases.
        Ok(_) => 200,
    }
}

fn main() {
    println!("{}", handle(br#"{"type":9999}"#, "signature"));
}
```

## Rules

- **Verify the raw body.** Pass the body exactly as received. Never re-serialize it: changed whitespace or key order makes the signature fail.
- **Parsing is strict.** `webhooks::parse` returns `Error::Webhook` when the body is not a JSON object, `type` is missing or is not an integer, or a known type is missing a required field or has it null. A known type missing a required field is a parse error.
- **Unknown types are kept.** A type this SDK does not know comes back as `WebhookEvent::Unknown`. Because `WebhookEvent` is `non_exhaustive`, end your `match` with a catch-all arm.
- **Type names.** `webhooks::EVENT_TYPES` maps a type number to its name; `1` is `ORDER_STATUS_CHANGE`.
- **IDs keep every digit.** IDs such as `shop_id` are exact whether TikTok sends them as strings or as JSON numbers.

A bad signature is `Error::WebhookSignature`, whatever the body holds. Answer it with 401 and a parse failure (`Error::Webhook`) with 400, so neither is mistaken for success. `webhooks::verify` returns a plain `bool` if you want to check the signature without parsing.
