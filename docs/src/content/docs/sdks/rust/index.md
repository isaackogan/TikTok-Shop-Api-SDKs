---
title: Rust SDK
description: Install tiktok-shop-api, the typed async TikTok Shop API client for Rust, and make your first call.
sidebar:
  label: Overview
  order: 1
---

`tiktok-shop-api` is a typed Rust client for the TikTok Shop Partner API. Its calls are `async` and run on tokio. It signs requests, handles OAuth, works with many shops at once, and verifies and types webhooks. It is published to [crates.io](https://crates.io/crates/tiktok-shop-api), and its source is in [`rust/`](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/rust).

## Install

```sh
cargo add tiktok-shop-api
```

Requires Rust 1.88 or newer. The calls are `async` and run on [tokio](https://tokio.rs), so add it too (`cargo add tokio --features macros,rt-multi-thread`). TLS is native-tls by default; to use rustls instead:

```toml
[dependencies]
tiktok-shop-api = { version = "0.1", default-features = false, features = ["rustls"] }
```

The crate is `tiktok_shop_api`. Models are in `tiktok_shop_api::generated::models`.

## First call

With an access token from the [OAuth helper](/sdks/rust/authorization/), create a client and call an operation:

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

Every call is signed, timestamped and sent with your access token. The `shop_cipher` query parameter is added for you on the endpoints that need it.

## In this section

- [Authorization](/sdks/rust/authorization/): `TikTokShopAuth`, authorization URLs, token exchange and refresh.
- [Calling the API](/sdks/rust/calling-the-api/): the client, API areas, many shops and options.
- [Webhooks](/sdks/rust/webhooks/): `webhooks::verify_and_parse` and typed events.
- [Errors](/sdks/rust/errors/): the `Error` enum and its variants.
