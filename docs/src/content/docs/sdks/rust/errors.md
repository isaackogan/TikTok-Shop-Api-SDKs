---
title: Errors
description: The Rust Error enum and how Api, Decode, Timeout and Http errors report each kind of failure.
sidebar:
  order: 5
---

Every failure is a `tiktok_shop_api::Error`, an enum. Unlike the other SDKs, it does not use one error type with a -1 code for decode and transport failures: a failure that reached TikTok is `Error::Api`, and the others have their own variants. The same classification applies in all eight SDKs; see [errors](/getting-started/errors/).

- `Error::Api { code, message, request_id, http_status }` for an envelope with a non-zero `code`, even on HTTP 200 (TikTok's code); a non-2xx reply (TikTok's non-zero code if the body has one, else the HTTP status); or a 2xx reply that can't be read, such as a body that is not a JSON object or a `code` that isn't an integer (code -1). `http_status` is always set.
- `Error::Decode` for a 2xx envelope whose `data` doesn't fit its generated model.
- `Error::Timeout`, and `Error::Http` for a network failure with no response.

```rust
use tiktok_shop_api::{Error, Options, TikTokShop};

#[tokio::main]
async fn main() {
    let client = TikTokShop::new(Options::new("APP_KEY", "APP_SECRET")).unwrap();

    match client.orders.get_order_list(20, None, None, None, None).await {
        Ok(_) => {}
        Err(Error::Api { code, message, request_id, http_status }) => {
            println!("TikTok said {code}: {message} (request {request_id}, HTTP {http_status:?})");
        }
        Err(Error::Timeout) => println!("timed out"),
        Err(other) => println!("{other}"),
    }
}
```

| What happened | Variant | `code` | `http_status` |
|---|---|---|---|
| TikTok's reply has a non-zero `code`, even on HTTP 200 | `Error::Api` | TikTok's code | the status |
| A non-2xx reply | `Error::Api` | TikTok's non-zero code if the body has one, else the HTTP status | the status |
| A 2xx reply that isn't a JSON object, or has a `code` that isn't an integer | `Error::Api` | -1 | the status |
| A 2xx reply whose `data` doesn't fit its model | `Error::Decode` | none | none |
| A timeout | `Error::Timeout` | none | none |
| No HTTP response at all: connection refused, DNS or TLS | `Error::Http` | none | none |

`Error` is `non_exhaustive`, so end a `match` with a catch-all arm. It also has variants for webhooks (`WebhookSignature`, `Webhook`), file reads (`Io`) and anything else (`Other`). See [webhooks](/sdks/rust/webhooks/).

- **Look up TikTok's code.** Each operation's error codes are listed in the [API reference](/openapi/reference/) (`x-tts-error-codes` in the spec). `Error::code()` returns it for an `Error::Api`.
- **Keep the `request_id`.** TikTok's support asks for it. `Error::request_id()` returns it for an `Error::Api` that has one; the field is empty when the reply had none.
- **Redirects are errors.** With the default HTTP client, a 3xx reply is an `Error::Api` whose `code` and `http_status` are the status, and the client does not follow it.
- **Secrets stay out of errors.** Errors never contain the request URL, so the app secret, the authorization code and the refresh token in a token call's query never reach an error message.
