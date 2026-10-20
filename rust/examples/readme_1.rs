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
