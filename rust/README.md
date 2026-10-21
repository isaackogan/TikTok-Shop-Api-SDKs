# TikTok Shop API for Rust (Unofficial)

[TikTok Shop API](https://partner.tiktokshop.com/) Client for Rust (Unofficial, Unaffiliated with TikTok or ByteDance Ltd.)

A typed, async Rust client for the TikTok Shop API, also called the TikTok Shop Partner API or Open API. It covers
every operation in TikTok's partner documentation, grouped as the documentation groups them: orders, products,
fulfillment, logistics, returns and refunds, finance, promotions, affiliate, analytics, customer service and more.

Every request is signed with HMAC-SHA256 and sent with your access token, and the shop cipher is added wherever an
endpoint needs it. The OAuth helper builds the authorization URL and exchanges and refreshes tokens. One client can
serve many shops, and TikTok Shop webhooks are verified and parsed into a typed enum. The API methods are generated
from a machine-readable OpenAPI v3 spec built from TikTok's partner documentation, so they track the docs.

Full guides, API reference and documentation: <https://ttspa.docs.isaackogan.com/sdks/rust/>

The guides cover [Authorization](https://ttspa.docs.isaackogan.com/sdks/rust/authorization/), [Calling the API](https://ttspa.docs.isaackogan.com/sdks/rust/calling-the-api/),
[Webhooks](https://ttspa.docs.isaackogan.com/sdks/rust/webhooks/) and [Errors](https://ttspa.docs.isaackogan.com/sdks/rust/errors/), and the [API reference](https://ttspa.docs.isaackogan.com/openapi/reference/) lists every operation and webhook.

[![crates.io](https://img.shields.io/crates/v/tiktok-shop-api?style=flat&color=0274b5)](https://crates.io/crates/tiktok-shop-api)
[![docs.rs](https://img.shields.io/docsrs/tiktok-shop-api?style=flat)](https://docs.rs/tiktok-shop-api)
![MSRV](https://img.shields.io/crates/msrv/tiktok-shop-api?style=flat&color=0274b5)
![Stars](https://img.shields.io/github/stars/isaackogan/TikTok-Shop-Api-SDKs?style=flat&color=0274b5)
![Issues](https://img.shields.io/github/issues/isaackogan/TikTok-Shop-Api-SDKs?style=flat&color=0274b5)
![License](https://img.shields.io/github/license/isaackogan/TikTok-Shop-Api-SDKs?style=flat&color=0274b5)

> [!IMPORTANT]
> Request signing follows TikTok's documentation and has not been verified against the live API. If TikTok rejects a signature, please open an issue at https://github.com/isaackogan/TikTok-Shop-Api-SDKs/issues.

> [!TIP]
> The OpenAPI spec this client is generated from is published at
> <https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/.openapi/tiktok-shop.openapi.yaml>.
> Point any OpenAPI 3.1 tool at it.

### Do you prefer other programming languages?

- [TikTok Shop API for TypeScript](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/typescript), `tiktok-shop-api` on npm
- [TikTok Shop API for Python](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/python), `tiktok-shop-api` on PyPI
- [TikTok Shop API for Go](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/go), `github.com/isaackogan/TikTok-Shop-Api-SDKs/go`
- [TikTok Shop API for Java](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/java), `com.isaackogan:tiktok-shop-api` on Maven Central
- [TikTok Shop API for Kotlin](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/kotlin), `com.isaackogan:tiktok-shop-api-kotlin` on Maven Central
- [TikTok Shop API for PHP](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/php), `isaackogan/tiktok-shop-api` on Packagist
- [TikTok Shop API for C# and .NET](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/csharp), `TikTokShop.Api` on NuGet

### Table of Contents

- [Getting Started](#getting-started)
- [Params and Options](#params-and-options)
- [Methods](#methods)
- [Examples](#examples)
- [Frequently Asked Questions](#frequently-asked-questions)
- [Contributors](#contributors)
- [License](#license)

## Getting Started

1. Add the crate

```sh
cargo add tiktok-shop-api
```

It needs Rust 1.88 or newer. The calls are `async` and run on [tokio](https://tokio.rs), so add it too
(`cargo add tokio --features macros,rt-multi-thread`). TLS is native-tls by default; to use rustls instead:

```toml
[dependencies]
tiktok-shop-api = { version = "0.1", default-features = false, features = ["rustls"] }
```

The crate is `tiktok_shop_api`. Models are in `tiktok_shop_api::generated::models`.

2. Authorize a shop with OAuth

Send the seller to the authorization URL. TikTok redirects back to your app with a `code`, which you trade for an
access token. Refresh before the access token expires.

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

3. Make your first call

Every API group is a field of the client (`orders`, `products`, `fulfillment`, `finance`, ...). Signing, `app_key`,
`timestamp` and the `x-tts-access-token` header are added to every call, and `shop_cipher` to the operations that take
one.

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

## Params and Options

To create a new client, build an `Options` and pass it to `TikTokShop::new`, which returns a `Result`.

`TikTokShop::new(Options::new(app_key, app_secret)...)`

| Param Name | Required | Description |
|------------|----------|-------------|
| `app_key` | Yes | Your app key, the first argument of `Options::new`. |
| `app_secret` | Yes | Your app secret, the second argument. It signs every request. |
| `.access_token(...)` | No | The seller's access token, sent as the `x-tts-access-token` header. Empty sends none. |
| `.shop_cipher(...)` | No | The shop's cipher, added to the operations that take one. Empty adds none. `authorization.get_authorized_shops` returns it. |
| `.base_url(...)` | No | Default `DEFAULT_BASE_URL` (`https://open-api.tiktokglobalshop.com`). It can point at a test server, and must be an origin such as `https://host:8443`, with no path prefix: signing and shop-cipher matching use the request path. |
| `.timeout(...)` | No | An `Option<Duration>` that bounds one request, response body included. `Options::new` sets `DEFAULT_TIMEOUT` (30 seconds); `None` means no limit. Ignored when you pass your own `http_client`. |
| `.http_client(...)` | No | Your own `reqwest::Client` (proxy, TLS roots, its own timeout, redirect policy, ...), used as is. The default honours `HTTP_PROXY`/`HTTPS_PROXY`/`NO_PROXY` and follows no redirects, so a redirect reply is an `Error::Api` with its HTTP status. |

The OAuth helper takes an `AuthOptions`, built the same way, and `TikTokShopAuth::new` also returns a `Result`.

`TikTokShopAuth::new(AuthOptions::new(app_key, app_secret)...)`

| Param Name | Required | Description |
|------------|----------|-------------|
| `app_key` | Yes | Your app key. |
| `app_secret` | Yes | Your app secret. |
| `.service_id(...)` | No | Your Partner Center service ID. Seller and partner authorization URLs need it. |
| `.base_url(...)` | No | Default `https://auth.tiktok-shops.com`. An origin, with no path prefix. |
| `.timeout(...)` | No | Bounds one token request. `AuthOptions::new` sets `DEFAULT_TIMEOUT`; `None` means no limit. |
| `.http_client(...)` | No | Your own `reqwest::Client`. Build it with `redirect::Policy::none()`: the token query holds your app secret, and a followed redirect would forward it. |

Requests carry the User-Agent `tiktok-shop-api-rust/<version>`. `Debug` for `Options`, `AuthOptions`, `TokenSet` and
the clients hides every secret.

## Methods

Each API group is a field of the client: `affiliate_creator`, `affiliate_partner`, `affiliate_seller`, `analytics`,
`authorization`, `customer_engagement`, `customer_service`, `event`, `finance`, `fulfilled_by_tiktok`, `fulfillment`,
`logistics`, `orders`, `products`, `promotion`, `return_and_refund`, `seller`, `supply_chain` and `tools`. Their
operations are `async` and take their parameters positionally, with `None` for the optional ones.

| Method Name | Description |
|-------------|-------------|
| `client.with_shop(Shop)` | Returns a client for another shop or token that shares this client's HTTP client, base URL and timeout. Build the `Shop` with `.access_token(...)`, `.shop_cipher(...)`, `.clear_access_token()` and `.clear_shop_cipher()`. See [Several shops](#several-shops-with_shop). |
| `auth.authorization_url(kind, region, state)` | Builds the URL to send a seller, partner or creator to. `kind` is `AuthType::Seller`, `Partner` or `Creator`; `region` is `Region::Us` or `Row`. |
| `auth.exchange_code(code).await` | Trades the `code` from the redirect for a `TokenSet`. |
| `auth.refresh(refresh_token).await` | Trades a refresh token for a new `TokenSet`. |
| `webhooks::verify(app_key, app_secret, raw_body, signature)` | Checks a webhook's `Authorization` header against the raw body. Returns a `bool`. |
| `webhooks::parse(raw_body)` | Parses a body into a `WebhookEvent`, or `Error::Webhook` for a body it cannot read. |
| `webhooks::verify_and_parse(app_key, app_secret, raw_body, signature)` | Verifies, then parses. A bad signature is `Error::WebhookSignature`. |
| `error.code()`, `error.request_id()` | TikTok's error code and request ID, when the error is an `Error::Api`. |

A `TokenSet` has `access_token`, `access_token_expire_in`, `refresh_token` and `refresh_token_expire_in` (both expiry
times are Unix times in seconds). Creator and partner tokens may lack the seller fields: `open_id`, `seller_name`,
`seller_base_region`, `user_type` and `granted_scopes` are `Option`s.

## Examples

### Handle errors

Every failure is a `tiktok_shop_api::Error`. Errors never contain the request URL.

- `Error::Api` for an envelope with a non-zero `code`, even on HTTP 200 (TikTok's code); a non-2xx reply (TikTok's
  non-zero code if the body has one, else the HTTP status); or a 2xx reply that can't be read, such as a body that is
  not a JSON object or a `code` that isn't an integer (code -1). `http_status` is always set.
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

### Several shops: `with_shop`

`with_shop` returns a client for another shop that shares the HTTP client. A value you leave out keeps this client's
value; clearing it is explicit. The original is never changed.

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

### Webhooks

`webhooks::verify_and_parse` checks the signature (HMAC-SHA256 over the app key plus the raw body) and returns a
`WebhookEvent`, an enum with one variant per webhook holding that webhook's generated model. Pass the body exactly as
received: never re-serialize it. A type this SDK does not know comes back as `WebhookEvent::Unknown`.

Parsing is strict: a body that is not a JSON object, a `type` that is missing or not an integer, or a known type with a
required field missing or null is an `Error::Webhook`. In short, a known type missing a required field is a parse error.

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

IDs such as `shop_id` keep every digit whether TikTok sends them as strings or as JSON numbers.
`webhooks::EVENT_TYPES` maps a webhook type to its event name (`1` is `ORDER_STATUS_CHANGE`).

### Signing and redirects

- Query values are signed decoded, exactly as the server receives them.
- A custom `http_client` follows redirects unless you build it with `redirect::Policy::none()`. Do that for
  `AuthOptions::http_client`: the token query holds your app secret, and a followed redirect would forward it.

## Frequently Asked Questions

### How do I get a TikTok Shop access token in Rust?

Create a `TikTokShopAuth` from `AuthOptions::new(app_key, app_secret).service_id(...)`, send the seller to
`authorization_url`, then trade the `code` TikTok sends back with `exchange_code`. Call `refresh` before the access
token expires. See [Getting Started](#getting-started).

### What is a shop cipher, and where do I find it?

Most TikTok Shop API endpoints act on one shop and need a `shop_cipher` query parameter. Call
`client.authorization.get_authorized_shops` with the seller's access token: each shop in the reply has a cipher. Set it
with `.shop_cipher(...)` on the `Options` and the client adds it to every endpoint that needs it.

### How do I verify TikTok Shop webhooks in axum or actix-web?

Take the body as raw bytes and pass it, with the `Authorization` header, to `webhooks::verify_and_parse`. Don't
deserialize it into a struct first, because re-serialized JSON no longer matches the signature. See
[Webhooks](#webhooks).

### Can I use rustls instead of native-tls?

Yes. Turn off the default features and enable `rustls`, as shown in [Getting Started](#getting-started).

### Can one app manage many TikTok Shop sellers?

Yes. Keep one client per shop with `with_shop`. They share one HTTP client. See
[Several shops](#several-shops-with_shop).

### Which TikTok Shop API versions does it cover?

Every endpoint in TikTok's partner documentation, from API version 202309 onwards, and every documented webhook.

### Is this affiliated with TikTok?

No. It is an independent open-source project, built from TikTok's partner documentation.

### Is this available in other languages?

Yes. See [Do you prefer other programming languages?](#do-you-prefer-other-programming-languages) for the TypeScript,
Python, Go, Java, Kotlin, PHP and C# SDKs.

## Contributors

* **Isaac Kogan** - *Creator & Maintainer* - [isaackogan](https://github.com/isaackogan)

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/LICENSE) file for details.

Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.
