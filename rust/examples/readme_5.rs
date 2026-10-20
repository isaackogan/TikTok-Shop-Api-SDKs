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
