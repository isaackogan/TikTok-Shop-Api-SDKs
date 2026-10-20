//! The client against an in-process HTTP stub.
mod common;

use common::*;
use std::time::Duration;
use tiktok_shop_api::generated::models;
use tiktok_shop_api::signing::SigningMiddleware;
use tiktok_shop_api::{Error, Options, Shop, TikTokShop};
use wiremock::ResponseTemplate;

#[tokio::test]
async fn authorized_shops_is_signed_with_the_token_and_no_shop_cipher() {
    let server = stub().await;
    client(&server).authorization.get_authorized_shops().await.unwrap();
    let req = last_request(&server).await;
    let q = decoded_query(&req);
    assert_eq!(req.url.path(), "/authorization/202309/shops");
    assert_eq!(one(&q, "app_key"), "k1");
    assert!(one(&q, "timestamp").parse::<u64>().unwrap() > 1_600_000_000);
    assert!(values(&q, "shop_cipher").is_empty(), "no shop_cipher for this operation");
    assert_eq!(req.headers.get("x-tts-access-token").unwrap(), TOKEN);
    assert_signed(&req);
}

#[tokio::test]
async fn order_list_sends_the_shop_cipher() {
    let server = stub().await;
    client(&server).orders.get_order_list(20, None, None, None, None).await.unwrap();
    let req = last_request(&server).await;
    let q = decoded_query(&req);
    assert_eq!(one(&q, "shop_cipher"), CIPHER);
    assert_eq!(one(&q, "page_size"), "20");
    assert_signed(&req);
}

#[tokio::test]
async fn no_token_and_no_cipher_send_neither() {
    let server = stub().await;
    let c = TikTokShop::new(Options::new("k1", SECRET).base_url(server.uri())).unwrap();
    c.orders.get_order_list(20, None, None, None, None).await.unwrap();
    let req = last_request(&server).await;
    assert!(req.headers.get("x-tts-access-token").is_none());
    assert!(values(&decoded_query(&req), "shop_cipher").is_empty());
    assert_signed(&req);
}

#[tokio::test]
async fn a_get_with_a_body_sends_the_body_and_signs_it() {
    let server = stub().await;
    let body = models::GetConversationListRequest { only_need_conversation_id: Some(true) };
    client(&server).affiliate_seller.get_conversation_list(10, None, None, None, Some(body)).await.unwrap();
    let req = last_request(&server).await;
    assert_eq!(req.method.as_str(), "GET");
    assert_eq!(std::str::from_utf8(&req.body).unwrap(), r#"{"only_need_conversation_id":true}"#);
    assert_eq!(req.headers.get("content-type").unwrap(), "application/json");
    assert_signed(&req);
    // The body is part of the signature: signing without it must differ.
    assert_ne!(one(&decoded_query(&req), "sign"), expected_sign(&req, None));
}

#[tokio::test]
async fn a_page_token_with_plus_slash_and_equals_round_trips_and_signs_decoded() {
    let server = stub().await;
    let token = "b2Zmc2V0PTEw+/x==";
    client(&server).affiliate_seller.get_conversation_list(10, Some(token), None, None, None).await.unwrap();
    let req = last_request(&server).await;
    let q = decoded_query(&req);
    assert_eq!(one(&q, "page_token"), token);
    // On the wire it is RFC 3986 encoded, never a form-encoded "+".
    let raw = req.url.query().unwrap();
    assert!(raw.contains("page_token=b2Zmc2V0PTEw%2B%2Fx%3D%3D"), "raw query: {raw}");
    assert_signed(&req);
}

#[tokio::test]
async fn a_space_in_a_value_is_percent_20_and_signed_as_a_space() {
    let server = stub().await;
    client(&server).affiliate_seller.get_conversation_list(10, Some("a b&c"), None, None, None).await.unwrap();
    let req = last_request(&server).await;
    assert_eq!(one(&decoded_query(&req), "page_token"), "a b&c");
    assert!(req.url.query().unwrap().contains("page_token=a%20b%26c"));
    assert_signed(&req);
}

#[tokio::test]
async fn an_error_envelope_with_http_200_is_an_api_error_with_the_request_id() {
    let server = stub_with(
        ResponseTemplate::new(200)
            .set_body_raw(r#"{"code":36009003,"message":"invalid","request_id":"r1","data":{}}"#, "application/json"),
    )
    .await;
    let err = client(&server).orders.get_order_list(20, None, None, None, None).await.unwrap_err();
    match err {
        Error::Api { code, message, request_id, http_status } => {
            assert_eq!(code, 36009003);
            assert_eq!(message, "invalid");
            assert_eq!(request_id, "r1");
            assert_eq!(http_status, Some(200));
        }
        other => panic!("expected Error::Api, got {other:?}"),
    }
}

#[tokio::test]
async fn a_non_2xx_response_is_an_api_error_with_the_status() {
    let server = stub_with(
        ResponseTemplate::new(500)
            .set_body_raw(r#"{"code":98765,"message":"boom","request_id":"r9"}"#, "application/json"),
    )
    .await;
    let err = client(&server).orders.get_order_list(20, None, None, None, None).await.unwrap_err();
    match err {
        Error::Api { code, message, request_id, http_status } => {
            assert_eq!((code, message.as_str(), request_id.as_str(), http_status), (98765, "boom", "r9", Some(500)));
        }
        other => panic!("expected Error::Api, got {other:?}"),
    }
}

#[tokio::test]
async fn a_non_2xx_response_without_a_code_uses_the_status() {
    let server = stub_with(ResponseTemplate::new(502).set_body_raw("<html>Bad Gateway</html>", "text/html")).await;
    let err = client(&server).orders.get_order_list(20, None, None, None, None).await.unwrap_err();
    match err {
        Error::Api { code, http_status, .. } => assert_eq!((code, http_status), (502, Some(502))),
        other => panic!("expected Error::Api, got {other:?}"),
    }
}

#[tokio::test]
async fn a_2xx_response_that_is_not_json_is_an_api_error() {
    let server = stub_with(ResponseTemplate::new(200).set_body_raw("<html>maintenance</html>", "text/html")).await;
    let err = client(&server).orders.get_order_list(20, None, None, None, None).await.unwrap_err();
    match err {
        Error::Api { code, message, http_status, .. } => {
            assert_eq!(code, -1);
            assert!(message.contains("not valid JSON"), "{message}");
            assert_eq!(http_status, Some(200));
        }
        other => panic!("expected Error::Api, got {other:?}"),
    }
}

/// A port that was just free and has no listener.
fn closed_port_url() -> String {
    let l = std::net::TcpListener::bind("127.0.0.1:0").unwrap();
    let port = l.local_addr().unwrap().port();
    drop(l);
    format!("http://127.0.0.1:{port}")
}

#[tokio::test]
async fn a_closed_port_is_an_http_error_that_leaks_neither_url_nor_secrets() {
    let c =
        TikTokShop::new(Options::new("k1", SECRET).access_token(TOKEN).shop_cipher(CIPHER).base_url(closed_port_url()))
            .unwrap();
    let err = c.orders.get_order_list(20, None, Some("pagetoken-xyz"), None, None).await.unwrap_err();
    assert!(matches!(err, Error::Http(_)), "got {err:?}");
    for text in [err.to_string(), format!("{err:?}"), format!("{err:#?}")] {
        assert!(!text.contains('?'), "query in {text}");
        assert!(!text.contains("http://") && !text.contains("/order/"), "URL in {text}");
        for secret in [SECRET, TOKEN, CIPHER, "pagetoken-xyz", "sign=", "app_key"] {
            assert!(!text.contains(secret), "{secret} in {text}");
        }
    }
    // The whole source chain too.
    let mut src = std::error::Error::source(&err);
    while let Some(e) = src {
        let t = format!("{e} {e:?}");
        assert!(!t.contains('?') && !t.contains("http://") && !t.contains("sign="), "source leaks: {t}");
        src = e.source();
    }
}

#[tokio::test]
async fn a_server_that_never_answers_times_out() {
    let server = stub_with(
        ResponseTemplate::new(200).set_body_raw(OK_BODY, "application/json").set_delay(Duration::from_secs(10)),
    )
    .await;
    let c = TikTokShop::new(options(&server).timeout(Some(Duration::from_millis(200)))).unwrap();
    let started = std::time::Instant::now();
    let err = c.orders.get_order_list(20, None, None, None, None).await.unwrap_err();
    assert!(matches!(err, Error::Timeout), "got {err:?}");
    assert!(started.elapsed() < Duration::from_secs(5));
}

#[tokio::test]
async fn no_timeout_means_no_limit() {
    let server = stub_with(
        ResponseTemplate::new(200).set_body_raw(OK_BODY, "application/json").set_delay(Duration::from_millis(400)),
    )
    .await;
    for timeout in [None, Some(Duration::ZERO)] {
        let c = TikTokShop::new(options(&server).timeout(timeout)).unwrap();
        c.orders.get_order_list(20, None, None, None, None).await.unwrap_or_else(|e| panic!("{timeout:?}: {e}"));
    }
}

#[tokio::test]
async fn reserved_query_parameters_are_replaced_by_the_clients_values() {
    let server = stub().await;
    let mw = SigningMiddleware::new("k1", SECRET, Some(TOKEN.into()), Some(CIPHER.into()));
    let http = reqwest_middleware::ClientBuilder::new(reqwest::Client::new()).with(mw).build();
    http.post(format!(
        "{}/order/202309/orders/search?app_key=evil&sign=x&timestamp=1&shop_cipher=bad&ids=5",
        server.uri()
    ))
    .send()
    .await
    .unwrap();
    let req = last_request(&server).await;
    let q = decoded_query(&req);
    assert_eq!(one(&q, "app_key"), "k1");
    assert_eq!(one(&q, "shop_cipher"), CIPHER);
    assert_ne!(one(&q, "timestamp"), "1");
    assert_ne!(one(&q, "sign"), "x");
    assert_eq!(one(&q, "ids"), "5");
    assert_signed(&req);
}

#[tokio::test]
async fn multipart_upload_arrives_intact_and_is_signed_without_the_body() {
    let server = stub().await;
    let path = std::env::temp_dir().join(format!("tiktok-shop-api-upload-{}.png", std::process::id()));
    let payload: Vec<u8> = (0u8..=255).collect();
    std::fs::write(&path, &payload).unwrap();
    client(&server).products.upload_product_image(path.clone(), Some("MAIN_IMAGE")).await.unwrap();
    let _ = std::fs::remove_file(&path);

    let req = last_request(&server).await;
    let ct = req.headers.get("content-type").unwrap().to_str().unwrap().to_string();
    assert!(ct.starts_with("multipart/form-data; boundary="), "{ct}");
    let boundary = ct.split("boundary=").nth(1).unwrap();
    let find = |hay: &[u8], needle: &[u8]| hay.windows(needle.len()).any(|w| w == needle);
    assert!(find(&req.body, format!("--{boundary}").as_bytes()), "opening boundary");
    assert!(find(&req.body, format!("--{boundary}--").as_bytes()), "closing boundary");
    assert!(find(&req.body, b"name=\"data\""));
    assert!(find(&req.body, b"name=\"use_case\""));
    assert!(find(&req.body, b"MAIN_IMAGE"));
    assert!(find(&req.body, &payload), "the file's bytes arrive intact");

    let q = decoded_query(&req);
    assert_eq!(one(&q, "sign"), expected_sign(&req, None));
    // ...and a different body would not have changed it, since multipart is never signed.
    assert_eq!(expected_sign(&req, None), expected_sign(&req, Some(&req.body)));
}

const PREDICT_REPLY: &str = r#"{"code":0,"message":"Success","request_id":"r5","zz_top":1,
 "data":{"zz_data":{"a":1},
  "package_dimensions":{"height":1,"length":2,"unit":"CENTIMETER","width":3,"zz_dim":"x"},
  "package_weight":{"unit":"KILOGRAM","value":"1.5","zz_weight":[1]}}}"#;

#[tokio::test]
async fn unknown_response_fields_are_ignored_at_data_level_and_inside_required_models() {
    let server = stub_with(ResponseTemplate::new(200).set_body_raw(PREDICT_REPLY, "application/json")).await;
    let reply = client(&server)
        .products
        .predict_product_package_dimensions_and_weight(models::PredictProductPackageDimensionsAndWeightRequest::new(
            "1".into(),
        ))
        .await
        .unwrap();
    let data = reply.data.unwrap();
    let dim = data.package_dimensions.unwrap();
    assert_eq!((dim.height, dim.length, dim.width, dim.unit.as_str()), (1, 2, 3, "CENTIMETER"));
    let w = data.package_weight.unwrap();
    assert_eq!(w.unit, "KILOGRAM");
    assert_eq!(w.value, "1.5");
}

#[tokio::test]
async fn a_malformed_data_section_is_a_decode_error() {
    let server = stub_with(
        ResponseTemplate::new(200)
            .set_body_raw(r#"{"code":0,"message":"ok","request_id":"r","data":"nope"}"#, "application/json"),
    )
    .await;
    let err = client(&server)
        .products
        .predict_product_package_dimensions_and_weight(models::PredictProductPackageDimensionsAndWeightRequest::new(
            "1".into(),
        ))
        .await
        .unwrap_err();
    assert!(matches!(err, Error::Decode(_)), "got {err:?}");
}

#[tokio::test]
async fn nineteen_digit_ids_in_a_response_stay_exact() {
    let reply =
        r#"{"code":0,"message":"ok","request_id":"r","data":{"shops":[{"id":"7494049642642441621","cipher":"c"}]}}"#;
    let server = stub_with(ResponseTemplate::new(200).set_body_raw(reply, "application/json")).await;
    let r = client(&server).authorization.get_authorized_shops().await.unwrap();
    assert_eq!(r.data.unwrap().shops.unwrap()[0].id.as_deref(), Some("7494049642642441621"));
}

async fn seen_by(server: &wiremock::MockServer) -> (Option<String>, Option<String>) {
    let req = last_request(server).await;
    let token = req.headers.get("x-tts-access-token").map(|v| v.to_str().unwrap().to_string());
    let cipher = values(&decoded_query(&req), "shop_cipher").first().map(|s| s.to_string());
    assert_signed(&req);
    (token, cipher)
}

#[tokio::test]
async fn with_shop_keeps_replaces_and_clears_and_never_mutates_the_original() {
    let server = stub().await;
    let base = client(&server);

    // Keep: nothing named, nothing changes.
    let kept = base.with_shop(Shop::new());
    kept.orders.get_order_list(1, None, None, None, None).await.unwrap();
    assert_eq!(seen_by(&server).await, (Some(TOKEN.into()), Some(CIPHER.into())));

    // Replace one and keep the other.
    let only_token = base.with_shop(Shop::new().access_token("t2"));
    only_token.orders.get_order_list(1, None, None, None, None).await.unwrap();
    assert_eq!(seen_by(&server).await, (Some("t2".into()), Some(CIPHER.into())));

    // Replace both.
    let both = base.with_shop(Shop::new().access_token("t3").shop_cipher("c3"));
    both.orders.get_order_list(1, None, None, None, None).await.unwrap();
    assert_eq!(seen_by(&server).await, (Some("t3".into()), Some("c3".into())));

    // Clear: explicitly, or by passing an empty value.
    let cleared = base.with_shop(Shop::new().clear_shop_cipher().clear_access_token());
    cleared.orders.get_order_list(1, None, None, None, None).await.unwrap();
    assert_eq!(seen_by(&server).await, (None, None));
    let empty = base.with_shop(Shop::new().access_token("").shop_cipher(""));
    empty.orders.get_order_list(1, None, None, None, None).await.unwrap();
    assert_eq!(seen_by(&server).await, (None, None));

    // The original is untouched.
    base.orders.get_order_list(1, None, None, None, None).await.unwrap();
    assert_eq!(seen_by(&server).await, (Some(TOKEN.into()), Some(CIPHER.into())));
}

#[tokio::test]
async fn with_shop_shares_the_http_client_and_settings() {
    let server = stub_with(
        ResponseTemplate::new(200).set_body_raw(OK_BODY, "application/json").set_delay(Duration::from_secs(10)),
    )
    .await;
    let base = TikTokShop::new(options(&server).timeout(Some(Duration::from_millis(200)))).unwrap();
    let other = base.with_shop(Shop::new().shop_cipher("c2"));
    let err = other.orders.get_order_list(1, None, None, None, None).await.unwrap_err();
    assert!(matches!(err, Error::Timeout), "the timeout carries over: {err:?}");
}

#[tokio::test]
async fn a_caller_supplied_http_client_is_used_and_not_given_our_timeout() {
    let server = stub_with(
        ResponseTemplate::new(200).set_body_raw(OK_BODY, "application/json").set_delay(Duration::from_millis(300)),
    )
    .await;
    // Our default timeout is 30 s; the caller's client has its own 100 ms limit, which must win.
    let own = reqwest::Client::builder().timeout(Duration::from_millis(100)).build().unwrap();
    let c = TikTokShop::new(options(&server).http_client(own)).unwrap();
    let err = c.orders.get_order_list(1, None, None, None, None).await.unwrap_err();
    assert!(matches!(err, Error::Timeout), "got {err:?}");
}

#[test]
fn debug_output_redacts_every_secret() {
    let o = Options::new("app-key-visible", SECRET).access_token(TOKEN).shop_cipher(CIPHER);
    let c = TikTokShop::new(o.clone()).unwrap();
    for text in [format!("{o:?}"), format!("{o:#?}"), format!("{c:?}"), format!("{c:#?}"), format!("{:?}", c.orders)] {
        for secret in [SECRET, TOKEN, CIPHER] {
            assert!(!text.contains(secret), "{secret} leaked in {text}");
        }
    }
    assert!(format!("{o:?}").contains("app-key-visible"), "the app key is not a secret");
    assert!(format!("{o:?}").contains("[redacted]"));
}
