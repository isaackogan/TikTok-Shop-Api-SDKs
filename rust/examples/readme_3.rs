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
