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
