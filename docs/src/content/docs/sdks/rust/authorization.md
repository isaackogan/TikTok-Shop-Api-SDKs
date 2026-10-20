---
title: Authorization
description: Build TikTok Shop authorization URLs and exchange and refresh tokens with TikTokShopAuth in Rust.
sidebar:
  order: 2
---

`TikTokShopAuth` builds the URL a seller, partner or creator opens to authorize your app, and calls TikTok's token endpoints. See [authorization](/getting-started/authorization/) for the flow itself.

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

`AuthType` is `Seller`, `Partner` or `Creator`; `Region` is `Us` or `Row`. `authorization_url` is synchronous, and returns an error if a seller or partner URL has no `service_id`. `exchange_code` and `refresh` are `async`.

## Options

`AuthOptions::new(app_key, app_secret)` sets the defaults, and builder methods change them:

| Option | Meaning |
| --- | --- |
| `app_key`, `app_secret` | Your app's credentials from Partner Center. |
| `service_id` | Your Partner Center service ID. Required for `Seller` and `Partner` authorization URLs; `Creator` URLs use the app key instead. |
| `base_url` | Token endpoint host, an origin with no path prefix. Defaults to `DEFAULT_AUTH_BASE_URL`, `https://auth.tiktok-shops.com`. |
| `timeout` | Per-request timeout, an `Option<Duration>`. `AuthOptions::new` sets `DEFAULT_TIMEOUT` (30 seconds); `None` or zero means no limit. Ignored when you pass your own `http_client`. |
| `http_client` | A `reqwest::Client` override, used as is. The default never follows a redirect, so the app secret and the code are never forwarded to another host. |

A custom `http_client` follows redirects unless you build it with `redirect::Policy::none()`. Do that for `AuthOptions::http_client`: the token query holds your app secret, and a followed redirect would forward it.

`authorization_url` omits an empty `state`, the same as `None`.

## Tokens

`exchange_code` and `refresh` return a `TokenSet`:

| Field | Meaning |
| --- | --- |
| `access_token`, `refresh_token` | The tokens. Send the access token with API calls; trade the refresh token for a new pair. |
| `access_token_expire_in`, `refresh_token_expire_in` | Unix times in seconds (`i64`) at which each token expires. They are moments, not durations. |
| `open_id`, `seller_name`, `seller_base_region`, `user_type`, `granted_scopes` | Optional, as `Option` values. Creator and partner tokens may lack the seller fields, and an absent `granted_scopes` is `None` rather than an empty list. |

`open_id` is kept as text, exact even when TikTok sends it as a number. `Debug` for `TokenSet`, `AuthOptions` and `TikTokShopAuth` hides the tokens and the app secret.

A non-zero `code` in TikTok's response returns `Error::Api` with `code`, `message` and `request_id`, and so does a token reply without `data`. A transport failure is `Error::Timeout` or `Error::Http`, and neither carries the request URL, whose query holds the secret and the code. See [errors](/sdks/rust/errors/).
