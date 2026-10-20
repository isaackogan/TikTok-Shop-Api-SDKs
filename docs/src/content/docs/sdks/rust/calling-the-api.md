---
title: Calling the API
description: Create the Rust TikTokShop client, call operations by API area, and work with many shops using with_shop.
sidebar:
  order: 3
---

`TikTokShop` is the API client. `TikTokShop::new` takes `Options` and fails only if the HTTP client cannot be built, for example when the TLS backend cannot start. Each request it sends gets the following automatically:
- the `app_key`, `timestamp` and `sign` query parameters;
- your access token, in the `x-tts-access-token` header;
- `shop_cipher`, on the operations that need one.

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

## API areas

One public field per API area hangs off the client, matching the spec's tags:

| Field | Area |
| --- | --- |
| `affiliate_creator`, `affiliate_partner`, `affiliate_seller` | Affiliate creator, partner and seller |
| `analytics` | Analytics |
| `authorization` | Authorization, including `get_authorized_shops` |
| `customer_engagement`, `customer_service` | Customer engagement and customer service |
| `event` | Event (webhook subscriptions) |
| `finance` | Finance |
| `fulfilled_by_tiktok` | Fulfilled by TikTok (FBT) |
| `fulfillment`, `logistics` | Fulfillment and logistics |
| `orders`, `products`, `promotion` | Orders, products and promotion |
| `return_and_refund` | Return and refund |
| `seller`, `supply_chain`, `tools` | Seller, supply chain and tools |

Each method is `async` and takes its parameters as arguments: the required ones first, then the optional ones as `Option` values, then the request body. In the example, `get_order_list(20, None, None, None, None)` passes `page_size` and leaves the rest unset. Method and parameter names follow the [API reference](/openapi/reference/), in snake case. Responses are typed models with `Option` fields.

## Many shops

`with_shop` returns a client for another shop that shares the HTTP client, base URL and timeout. A value you leave out keeps this client's value; clearing it is explicit. The original is never changed.

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

## Options

`Options::new(app_key, app_secret)` sets the defaults, and builder methods change them:

| Option | Meaning |
| --- | --- |
| `app_key`, `app_secret` | Your app's credentials. |
| `access_token` | The seller's access token, sent in `x-tts-access-token`. `None` or empty sends none. |
| `shop_cipher` | The shop cipher added to operations that need one. `None` or empty adds none. |
| `base_url` | The API host, an origin such as `https://host:8443` with no path prefix: signing and shop-cipher matching use the request path. Defaults to `DEFAULT_BASE_URL`, `https://open-api.tiktokglobalshop.com`. |
| `timeout` | Bounds one request, response body included, as an `Option<Duration>`. `Options::new` sets `DEFAULT_TIMEOUT` (30 seconds); `None` or zero means no limit. Ignored when you pass your own `http_client`. |
| `http_client` | A `reqwest::Client` override (proxy, TLS roots, its own timeout, redirect policy), used as is. |

The default HTTP client honours `HTTP_PROXY`, `HTTPS_PROXY` and `NO_PROXY`, follows no redirects and times out after 30 seconds. A redirect reply is an `Error::Api` with its HTTP status, so the access token is never forwarded to another host. A custom `http_client` follows redirects unless you build it with `redirect::Policy::none()`.

Query values are signed decoded, exactly as the server receives them. Requests carry the User-Agent `tiktok-shop-api-rust/<version>`. `Debug` for `Options` and the client hides every secret.
