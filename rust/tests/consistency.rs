//! Cross-language rules from the final review: lesson 34 (a non-integer `code`), R21b (integer enums) and R28 (strict
//! webhook parsing, nulls included).
mod common;

use common::*;
use serde_json::{json, Value};
use tiktok_shop_api::webhooks;
use tiktok_shop_api::{AuthOptions, Error, TikTokShopAuth};
use wiremock::ResponseTemplate;

#[tokio::test]
async fn a_non_integer_code_on_a_2xx_is_minus_one() {
    for code in [r#""0""#, "1.5", "true", "null", "{}"] {
        let body = format!(r#"{{"code":{code},"message":"m","request_id":"q5","data":{{}}}}"#);
        let server = stub_with(ResponseTemplate::new(200).set_body_raw(body, "application/json")).await;
        let err = client(&server).authorization.get_authorized_shops().await.unwrap_err();
        match err {
            Error::Api { code: c, request_id, http_status, .. } => {
                assert_eq!((c, request_id.as_str(), http_status), (-1, "q5", Some(200)), "API code {code}")
            }
            other => panic!("API code {code}: {other:?}"),
        }
        let body = format!(
            r#"{{"code":{code},"request_id":"q6","data":{{"access_token":"a","access_token_expire_in":1,"refresh_token":"r","refresh_token_expire_in":2}}}}"#
        );
        let server = stub_with(ResponseTemplate::new(200).set_body_raw(body, "application/json")).await;
        let auth = TikTokShopAuth::new(AuthOptions::new("k", SECRET).base_url(server.uri())).unwrap();
        match auth.exchange_code("c").await.unwrap_err() {
            Error::Api { code: c, http_status, .. } => {
                assert_eq!((c, http_status), (-1, Some(200)), "token code {code}")
            }
            other => panic!("token code {code}: {other:?}"),
        }
    }
    let server =
        stub_with(ResponseTemplate::new(200).set_body_raw(r#"{"request_id":"q","data":{}}"#, "application/json")).await;
    client(&server).authorization.get_authorized_shops().await.expect("no code at all is a success");
}

#[tokio::test]
async fn an_integer_enum_value_the_spec_does_not_list_still_decodes() {
    let body = r#"{"code":0,"request_id":"r","data":{"creators":[{"creator_profile":{"user_type_tag":[1,3]}}]}}"#;
    let server = stub_with(ResponseTemplate::new(200).set_body_raw(body, "application/json")).await;
    let res = client(&server).affiliate_seller.search_creators_in_creator_marketplace(1, None, None).await.unwrap();
    let v: Value = serde_json::to_value(&res).unwrap();
    assert_eq!(v["data"]["creators"][0]["creator_profile"]["user_type_tag"], json!([1, 3]));
}

/// A named edit of a webhook body.
type Edit = (&'static str, fn(&mut Value));

fn appeal() -> Value {
    json!({
        "type": 66, "shop_id": "1", "tts_notification_id": "n1", "timestamp": 1,
        "data": {"product_id": 5, "appeal_task": {"appeal_audit_result": [{"indicator_type": "A", "status": "S"}]}}
    })
}

#[test]
fn a_known_webhook_with_a_null_or_missing_required_field_is_a_parse_error() {
    webhooks::parse(appeal().to_string().as_bytes()).expect("the complete event parses");
    let edits: [Edit; 7] = [
        ("null shop_id", |v| v["shop_id"] = Value::Null),
        ("null timestamp", |v| v["timestamp"] = Value::Null),
        ("null data", |v| v["data"] = Value::Null),
        ("null product_id", |v| v["data"]["product_id"] = Value::Null),
        ("missing product_id", |v| {
            v["data"].as_object_mut().unwrap().remove("product_id");
        }),
        ("null status in a list", |v| v["data"]["appeal_task"]["appeal_audit_result"][0]["status"] = Value::Null),
        ("missing indicator_type in a list", |v| {
            v["data"]["appeal_task"]["appeal_audit_result"][0].as_object_mut().unwrap().remove("indicator_type");
        }),
    ];
    for (name, edit) in edits {
        let mut v = appeal();
        edit(&mut v);
        let err = webhooks::parse(v.to_string().as_bytes()).expect_err(name);
        assert!(matches!(err, Error::Webhook(_)), "{name}: {err:?}");
    }
}
