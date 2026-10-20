//! `TikTokShopAuth` against the shared `auth.json` vectors and a wiremock token server.
use serde_json::{json, Value};
use std::time::Duration;
use tiktok_shop_api::{AuthOptions, AuthType, Error, Region, TikTokShopAuth, TokenSet};
use wiremock::matchers::any;
use wiremock::{Mock, MockServer, ResponseTemplate};

fn vectors() -> Value {
    serde_json::from_str(include_str!("../../shared/test-vectors/auth.json")).unwrap()
}

const SECRET: &str = "s3cret";

async fn token_server(status: u16, body: &str) -> MockServer {
    let server = MockServer::start().await;
    Mock::given(any())
        .respond_with(ResponseTemplate::new(status).set_body_raw(body.to_owned(), "application/json"))
        .mount(&server)
        .await;
    server
}

fn auth_for(server: &MockServer) -> TikTokShopAuth {
    TikTokShopAuth::new(AuthOptions::new("123abc", SECRET).base_url(server.uri())).unwrap()
}

fn ok(data: Value) -> String {
    json!({"code": 0, "message": "success", "request_id": "req-1", "data": data}).to_string()
}

fn minimal() -> Value {
    json!({"access_token": "a", "access_token_expire_in": 1, "refresh_token": "r", "refresh_token_expire_in": 2})
}

fn closed_port_url() -> String {
    let l = std::net::TcpListener::bind("127.0.0.1:0").unwrap();
    let port = l.local_addr().unwrap().port();
    drop(l);
    format!("http://127.0.0.1:{port}")
}

fn kind(s: &str) -> AuthType {
    match s {
        "seller" => AuthType::Seller,
        "partner" => AuthType::Partner,
        "creator" => AuthType::Creator,
        other => panic!("{other}"),
    }
}

fn region(s: &str) -> Region {
    if s == "us" {
        Region::Us
    } else {
        Region::Row
    }
}

#[test]
fn authorization_urls_match_the_vectors_byte_for_byte() {
    let v = vectors();
    for case in v["authorizationUrls"].as_array().unwrap() {
        let mut o = AuthOptions::new(case["appKey"].as_str().unwrap_or("123abc"), SECRET);
        if let Some(id) = case["serviceId"].as_str() {
            o = o.service_id(id);
        }
        let auth = TikTokShopAuth::new(o).unwrap();
        let url = auth
            .authorization_url(
                kind(case["type"].as_str().unwrap()),
                region(case["region"].as_str().unwrap()),
                case["state"].as_str(),
            )
            .unwrap();
        assert_eq!(url, case["url"].as_str().unwrap(), "{case}");
    }
}

#[test]
fn a_seller_url_needs_a_service_id() {
    let auth = TikTokShopAuth::new(AuthOptions::new("k", SECRET)).unwrap();
    let err = auth.authorization_url(AuthType::Seller, Region::Us, None).unwrap_err();
    assert!(err.to_string().contains("service_id"), "{err}");
    assert!(auth.authorization_url(AuthType::Creator, Region::Row, None).is_ok());
}

#[tokio::test]
async fn token_requests_are_gets_with_the_pinned_query() {
    let v = vectors();
    for case in v["tokenRequests"].as_array().unwrap() {
        let server = token_server(200, &ok(minimal())).await;
        let auth = auth_for(&server);
        let value = case["value"].as_str().unwrap();
        match case["kind"].as_str().unwrap() {
            "exchange" => auth.exchange_code(value).await.unwrap(),
            _ => auth.refresh(value).await.unwrap(),
        };
        let req = server.received_requests().await.unwrap().pop().unwrap();
        let want = case["url"].as_str().unwrap();
        let (path, query) = want.strip_prefix("https://auth.tiktok-shops.com").unwrap().split_once('?').unwrap();
        assert_eq!(req.method.as_str(), "GET");
        assert_eq!(req.url.path(), path);
        assert_eq!(req.url.query().unwrap(), query);
    }
}

#[tokio::test]
async fn token_responses_match_the_vectors() {
    let v = vectors();
    for case in v["tokenResponses"].as_array().unwrap() {
        let server = token_server(200, case["body"].as_str().unwrap()).await;
        let result = auth_for(&server).exchange_code("c").await;
        if let Some(code) = case["errorCode"].as_i64() {
            let err = result.unwrap_err();
            assert_eq!(err.code(), Some(code), "{case}");
            assert_eq!(err.request_id(), Some("r2"));
            continue;
        }
        let t = result.unwrap();
        let e = &case["expected"];
        assert_eq!(t.access_token, e["accessToken"].as_str().unwrap());
        assert_eq!(t.access_token_expire_in, e["accessTokenExpireIn"].as_i64().unwrap());
        assert_eq!(t.refresh_token, e["refreshToken"].as_str().unwrap());
        assert_eq!(t.refresh_token_expire_in, e["refreshTokenExpireIn"].as_i64().unwrap());
        assert_eq!(t.open_id.as_deref(), e["openId"].as_str());
        assert_eq!(t.seller_name.as_deref(), e["sellerName"].as_str());
        assert_eq!(t.seller_base_region.as_deref(), e["sellerBaseRegion"].as_str());
        assert_eq!(t.user_type, e["userType"].as_i64());
        let scopes: Vec<&str> = e["grantedScopes"].as_array().unwrap().iter().map(|s| s.as_str().unwrap()).collect();
        assert_eq!(t.granted_scopes.as_deref().unwrap(), scopes);
    }
}

#[tokio::test]
async fn refresh_hits_the_refresh_endpoint() {
    let server = token_server(200, &ok(minimal())).await;
    auth_for(&server).refresh("rt").await.unwrap();
    let req = server.received_requests().await.unwrap().pop().unwrap();
    assert_eq!(req.url.path(), "/api/v2/token/refresh");
}

#[tokio::test]
async fn a_minimal_four_field_response_succeeds() {
    let server = token_server(200, &ok(minimal())).await;
    let t = auth_for(&server).exchange_code("c").await.unwrap();
    assert_eq!((t.access_token.as_str(), t.refresh_token.as_str()), ("a", "r"));
    assert_eq!((t.access_token_expire_in, t.refresh_token_expire_in), (1, 2));
    assert!(t.open_id.is_none() && t.seller_name.is_none() && t.seller_base_region.is_none());
    assert!(t.user_type.is_none() && t.granted_scopes.is_none());
}

#[tokio::test]
async fn null_optionals_are_none() {
    let mut d = minimal();
    for k in ["open_id", "seller_name", "seller_base_region", "user_type", "granted_scopes"] {
        d[k] = Value::Null;
    }
    let server = token_server(200, &ok(d)).await;
    let t = auth_for(&server).exchange_code("c").await.unwrap();
    assert!(t.open_id.is_none() && t.seller_name.is_none() && t.seller_base_region.is_none());
    assert!(t.user_type.is_none() && t.granted_scopes.is_none());
}

#[tokio::test]
async fn open_id_keeps_its_digits_when_sent_as_a_number() {
    let body = r#"{"code":0,"message":"success","request_id":"r","data":{"access_token":"a","access_token_expire_in":1,"refresh_token":"r","refresh_token_expire_in":2,"open_id":7494049642642441621}}"#;
    let server = token_server(200, body).await;
    let t = auth_for(&server).exchange_code("c").await.unwrap();
    assert_eq!(t.open_id.as_deref(), Some("7494049642642441621"));
}

fn with(field: &str, value: Value) -> Value {
    let mut d = minimal();
    if value == json!("<remove>") {
        d.as_object_mut().unwrap().remove(field);
    } else {
        d[field] = value;
    }
    d
}

#[tokio::test]
async fn a_missing_or_ill_typed_required_field_is_code_minus_one_with_the_request_id() {
    let mut bad = vec![];
    for field in ["access_token", "access_token_expire_in", "refresh_token", "refresh_token_expire_in"] {
        bad.push(with(field, json!("<remove>")));
        bad.push(with(field, Value::Null));
        bad.push(with(field, json!(true)));
        bad.push(with(field, json!([])));
    }
    for field in ["access_token", "refresh_token"] {
        bad.push(with(field, json!("")));
        bad.push(with(field, json!(12)));
    }
    for field in ["access_token_expire_in", "refresh_token_expire_in"] {
        bad.push(with(field, json!(1.5)));
        bad.push(with(field, json!("123")));
    }
    for data in bad {
        let server = token_server(200, &ok(data.clone())).await;
        let err = auth_for(&server).exchange_code("c").await.unwrap_err();
        match err {
            Error::Api { code, request_id, .. } => {
                assert_eq!(code, -1, "{data}");
                assert_eq!(request_id, "req-1", "{data}");
            }
            other => panic!("{data}: {other:?}"),
        }
    }
}

#[tokio::test]
async fn code_zero_without_object_data_is_code_minus_one() {
    for body in [
        r#"{"code":0,"message":"success","request_id":"req-1"}"#,
        r#"{"code":0,"message":"success","request_id":"req-1","data":null}"#,
        r#"{"code":0,"message":"success","request_id":"req-1","data":[1]}"#,
        r#"{"code":0,"message":"success","request_id":"req-1","data":"x"}"#,
    ] {
        let server = token_server(200, body).await;
        let err = auth_for(&server).refresh("r").await.unwrap_err();
        assert_eq!((err.code(), err.request_id()), (Some(-1), Some("req-1")), "{body}");
    }
}

#[tokio::test]
async fn unreadable_2xx_replies_use_minus_one() {
    for (status, body) in [(200, "<html>no</html>"), (200, "[]"), (200, "")] {
        let server = token_server(status, body).await;
        let err = auth_for(&server).exchange_code("c").await.unwrap_err();
        match err {
            Error::Api { code, http_status, .. } => {
                assert_eq!(code, -1, "{status} {body}");
                assert_eq!(http_status, Some(status));
            }
            other => panic!("{other:?}"),
        }
    }
}

#[tokio::test]
async fn a_non_2xx_with_a_tiktok_code_keeps_it_and_zero_becomes_the_status() {
    let server = token_server(401, r#"{"code":36004004,"message":"nope","request_id":"r9"}"#).await;
    let err = auth_for(&server).exchange_code("c").await.unwrap_err();
    assert_eq!((err.code(), err.request_id()), (Some(36004004), Some("r9")));
    let server = token_server(500, r#"{"code":0,"message":"boom","request_id":"r9"}"#).await;
    let err = auth_for(&server).exchange_code("c").await.unwrap_err();
    assert_eq!(err.code(), Some(500));
}

fn assert_no_secrets(err: &Error) {
    let secrets = [SECRET, "AUTHCODE-xyz", "REFRESH-xyz", "app_secret", "auth_code", "refresh_token", "http://", "?"];
    let mut texts = vec![err.to_string(), format!("{err:?}"), format!("{err:#?}")];
    let mut src = std::error::Error::source(err);
    while let Some(e) = src {
        texts.push(format!("{e} {e:?}"));
        src = e.source();
    }
    for t in texts {
        for s in secrets {
            assert!(!t.contains(s), "{s:?} in {t}");
        }
    }
}

#[tokio::test]
async fn a_closed_port_leaks_no_secret_on_exchange_or_refresh() {
    let auth = TikTokShopAuth::new(AuthOptions::new("123abc", SECRET).base_url(closed_port_url())).unwrap();
    let e1 = auth.exchange_code("AUTHCODE-xyz").await.unwrap_err();
    let e2 = auth.refresh("REFRESH-xyz").await.unwrap_err();
    for e in [e1, e2] {
        assert!(matches!(e, Error::Http(_)), "{e:?}");
        assert_no_secrets(&e);
    }
}

#[tokio::test]
async fn a_timeout_leaks_no_secret_on_exchange_or_refresh() {
    let server = MockServer::start().await;
    Mock::given(any()).respond_with(ResponseTemplate::new(200).set_delay(Duration::from_secs(10))).mount(&server).await;
    let auth = TikTokShopAuth::new(
        AuthOptions::new("123abc", SECRET).base_url(server.uri()).timeout(Some(Duration::from_millis(200))),
    )
    .unwrap();
    let e1 = auth.exchange_code("AUTHCODE-xyz").await.unwrap_err();
    let e2 = auth.refresh("REFRESH-xyz").await.unwrap_err();
    for e in [e1, e2] {
        assert!(matches!(e, Error::Timeout), "{e:?}");
        assert_no_secrets(&e);
    }
}

#[tokio::test]
async fn an_invalid_base_url_leaks_no_secret() {
    let auth = TikTokShopAuth::new(AuthOptions::new("123abc", SECRET).base_url("not a url")).unwrap();
    let e = auth.exchange_code("AUTHCODE-xyz").await.unwrap_err();
    assert_no_secrets(&e);
}

#[tokio::test]
async fn a_redirect_is_not_followed() {
    let elsewhere = MockServer::start().await;
    Mock::given(any())
        .respond_with(ResponseTemplate::new(200).set_body_raw(ok(minimal()), "application/json"))
        .mount(&elsewhere)
        .await;
    let server = MockServer::start().await;
    Mock::given(any())
        .respond_with(ResponseTemplate::new(302).insert_header("location", format!("{}/steal", elsewhere.uri())))
        .mount(&server)
        .await;
    let err = auth_for(&server).exchange_code("AUTHCODE-xyz").await.unwrap_err();
    match &err {
        Error::Api { http_status, .. } => assert_eq!(*http_status, Some(302)),
        other => panic!("{other:?}"),
    }
    assert!(elsewhere.received_requests().await.unwrap().is_empty(), "the redirect target was contacted");
}

#[test]
fn debug_output_redacts_every_secret() {
    let o = AuthOptions::new("123abc", "APPSECRET-1").service_id("svc-1").base_url("http://x");
    let auth = TikTokShopAuth::new(o.clone()).unwrap();
    let t = TokenSet {
        access_token: "ACCESS-TOKEN-1".into(),
        access_token_expire_in: 1,
        refresh_token: "REFRESH-TOKEN-1".into(),
        refresh_token_expire_in: 2,
        open_id: Some("open-1".into()),
        seller_name: None,
        seller_base_region: None,
        user_type: None,
        granted_scopes: None,
    };
    for text in [
        format!("{o:?}"),
        format!("{o:#?}"),
        format!("{auth:?}"),
        format!("{auth:#?}"),
        format!("{t:?}"),
        format!("{t:#?}"),
    ] {
        for secret in ["APPSECRET-1", "ACCESS-TOKEN-1", "REFRESH-TOKEN-1"] {
            assert!(!text.contains(secret), "{secret} in {text}");
        }
    }
    assert!(format!("{o:?}").contains("123abc"), "the app key is not a secret");
}

/// R13b: any non-2xx without a non-zero TikTok code uses the HTTP status; -1 is only for an unreadable 2xx or code 0 without data.
#[tokio::test]
async fn r13b_token_codes() {
    let cases: [(u16, &str, i64); 9] = [
        (503, r#"{"message":"x"}"#, 503),
        (503, r#"{"code":0}"#, 503),
        (503, "down", 503),
        (503, "", 503),
        (503, "[1]", 503),
        (302, "", 302),
        (503, r#"{"code":12345,"message":"m"}"#, 12345),
        (200, "<html>", -1),
        (200, r#"{"code":0,"request_id":"r"}"#, -1),
    ];
    for (status, body, want) in cases {
        let server = token_server(status, body).await;
        for refresh in [false, true] {
            let a = auth_for(&server);
            let err = if refresh { a.refresh("r").await } else { a.exchange_code("c").await }.unwrap_err();
            match err {
                Error::Api { code, http_status, .. } => {
                    assert_eq!((code, http_status), (want, Some(status)), "{status} {body:?}");
                }
                other => panic!("{other:?}"),
            }
        }
    }
}
