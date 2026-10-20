# TikTok Shop API client for Rust

A typed Rust client for the **TikTok Shop API** (the TikTok Shop Partner API): 320 operations across 19 API groups, request signing, OAuth token helpers and typed webhooks. The API methods are generated from a machine-readable OpenAPI v3 spec built from TikTok's partner documentation, so they track the docs.

Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.

> Request signing follows TikTok's documentation and has not been verified against the live API. The OpenAPI spec this client is generated from is published at <https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/.openapi/tiktok-shop.openapi.yaml>.

## Install

Requires Rust 1.82 or newer.

```sh
cargo add tiktok-shop-api
```

The calls are `async` and run on [tokio](https://tokio.rs), so add it too (`cargo add tokio --features macros,rt-multi-thread`). TLS is native-tls by default; to use rustls instead:

```toml
[dependencies]
tiktok-shop-api = { version = "0.1", default-features = false, features = ["rustls"] }
```

The crate is `tiktok_shop_api`. Models are in `tiktok_shop_api::generated::models`.

## Authorize a shop (OAuth)

Send the seller to the authorization URL. TikTok redirects back to your app with a `code`, which you trade for an access token. Refresh before the access token expires.

```rust
use tiktok_shop_api::{AuthOptions, AuthType, Region, TikTokShopAuth};

#[tokio::main]
async fn main() -> Result<(), tiktok_shop_api::Error> {
    let auth = TikTokShopAuth::new(AuthOptions::new("APP_KEY", "APP_SECRET").service_id("SERVICE_ID"))?;

    // Send the seller here; TikTok redirects back to your app with ?code=...
    let url = auth.authorization_url(AuthType::Seller, Region::Us, Some("my-csrf-token"))?;
    println!("send the seller to {url}");

    let tokens = auth.exchange_code("CODE_FROM_THE_REDIRECT").await?;
    println!("{:?} {:?}", tokens.open_id, tokens.granted_scopes);

    // Refresh before the access token expires. `Debug` hides the tokens themselves.
    let tokens = auth.refresh(&tokens.refresh_token).await?;
    println!("expires at {}", tokens.access_token_expire_in);
    Ok(())
}
```

## Make a call

Every API group is a field of the client (`orders`, `products`, `fulfillment`, `finance`, ...). Signing, `app_key`, `timestamp`, the `x-tts-access-token` header and `shop_cipher` are added for you.

```rust
use tiktok_shop_api::{Options, TikTokShop};

#[tokio::main]
async fn main() -> Result<(), tiktok_shop_api::Error> {
    let client =
        TikTokShop::new(Options::new("APP_KEY", "APP_SECRET").access_token("ACCESS_TOKEN").shop_cipher("SHOP_CIPHER"))?;

    // page_size, then sort_order, page_token, sort_field and the request body, all optional.
    let orders = client.orders.get_order_list(20, None, None, None, None).await?;
    if let Some(data) = orders.data {
        println!("{:?} orders; request {:?}", data.total_count, orders.request_id);
    }
    Ok(())
}
```

Every failure is a `tiktok_shop_api::Error`: `Error::Api` for an envelope with a non-zero `code` (even on HTTP 200), a non-2xx reply or a body that is not JSON; `Error::Timeout`; `Error::Http` for a network failure. Errors never contain the request URL.

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

## Several shops: `with_shop`

`with_shop` returns a client for another shop that shares the HTTP client. A value you leave out keeps this client's value; clearing it is explicit. The original is never changed.

```rust
use tiktok_shop_api::{Options, Shop, TikTokShop};

fn main() -> Result<(), tiktok_shop_api::Error> {
    let client = TikTokShop::new(Options::new("APP_KEY", "APP_SECRET").access_token("ACCESS_TOKEN"))?;

    // Another shop, same HTTP client. What you do not name keeps this client's value.
    let other = client.with_shop(Shop::new().access_token("OTHER_ACCESS_TOKEN").shop_cipher("OTHER_SHOP_CIPHER"));

    // `clear_access_token()` and `clear_shop_cipher()` remove a value. `client` is never changed.
    let _no_cipher = other.with_shop(Shop::new().clear_shop_cipher());
    Ok(())
}
```

## Webhooks

`webhooks::verify_and_parse` checks the signature (HMAC-SHA256 over the app key plus the raw body) and returns a `WebhookEvent`, an enum with one variant per webhook holding that webhook's generated model. Pass the body exactly as received: never re-serialize it. A type this SDK does not know comes back as `WebhookEvent::Unknown`.

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

IDs such as `shop_id` keep every digit whether TikTok sends them as strings or as JSON numbers. `webhooks::EVENT_TYPES` maps a webhook type to its event name (`1` is `ORDER_STATUS_CHANGE`).

## Notes

- Query values are signed decoded, exactly as the server receives them.
- The default HTTP client honours `HTTP_PROXY`/`HTTPS_PROXY`/`NO_PROXY`, follows no redirects and times out after 30 seconds. Pass your own `reqwest::Client` with `Options::http_client` (or `AuthOptions::http_client`) to change that.
- `Options::base_url` and `AuthOptions::base_url` can point at a test server.
- `Debug` for `Options`, `AuthOptions`, `TokenSet` and the clients hides every secret.

## License

MIT. See [LICENSE](LICENSE).
