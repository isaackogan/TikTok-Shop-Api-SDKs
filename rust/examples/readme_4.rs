use tiktok_shop_api::{Options, Shop, TikTokShop};

fn main() -> Result<(), tiktok_shop_api::Error> {
    let client = TikTokShop::new(Options::new("APP_KEY", "APP_SECRET").access_token("ACCESS_TOKEN"))?;

    // Another shop, same HTTP client. What you do not name keeps this client's value.
    let other = client.with_shop(Shop::new().access_token("OTHER_ACCESS_TOKEN").shop_cipher("OTHER_SHOP_CIPHER"));

    // `clear_access_token()` and `clear_shop_cipher()` remove a value. `client` is never changed.
    let _no_cipher = other.with_shop(Shop::new().clear_shop_cipher());
    Ok(())
}
