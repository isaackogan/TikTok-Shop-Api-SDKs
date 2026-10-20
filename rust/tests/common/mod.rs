#![allow(dead_code)]
//! Shared helpers: a wiremock server, and a recompute-the-signature check on what it received.
use tiktok_shop_api::signing::{SignRequest, Signer};
use tiktok_shop_api::{Options, TikTokShop};
use wiremock::matchers::any;
use wiremock::{Mock, MockServer, Request, ResponseTemplate};

pub const OK_BODY: &str = r#"{"code":0,"message":"Success","request_id":"r0","data":{}}"#;
pub const SECRET: &str = "s3cr3t-app-secret";
pub const TOKEN: &str = "tok-access-1";
pub const CIPHER: &str = "cipher-1";

pub async fn stub_with(template: ResponseTemplate) -> MockServer {
    let server = MockServer::start().await;
    Mock::given(any()).respond_with(template).mount(&server).await;
    server
}

pub async fn stub() -> MockServer {
    stub_with(ResponseTemplate::new(200).set_body_raw(OK_BODY, "application/json")).await
}

pub fn options(server: &MockServer) -> Options {
    Options::new("k1", SECRET).access_token(TOKEN).shop_cipher(CIPHER).base_url(server.uri())
}

pub fn client(server: &MockServer) -> TikTokShop {
    TikTokShop::new(options(server)).unwrap()
}

/// The decoded query, as a server would read it.
pub fn decoded_query(req: &Request) -> Vec<(String, String)> {
    url::form_urlencoded::parse(req.url.query().unwrap_or("").as_bytes()).into_owned().collect()
}

pub fn values<'a>(q: &'a [(String, String)], key: &str) -> Vec<&'a str> {
    q.iter().filter(|(k, _)| k == key).map(|(_, v)| v.as_str()).collect()
}

pub fn one<'a>(q: &'a [(String, String)], key: &str) -> &'a str {
    let v = values(q, key);
    assert_eq!(v.len(), 1, "{key} should appear exactly once in {q:?}");
    v[0]
}

/// Recompute `sign` from what the server received, with an explicit body (`None`: unsigned or empty).
pub fn expected_sign(req: &Request, body: Option<&[u8]>) -> String {
    let q = decoded_query(req);
    let rest: Vec<(String, String)> = q.into_iter().filter(|(k, _)| k != "sign").collect();
    let content_type = req.headers.get("content-type").map(|v| v.to_str().unwrap().to_string());
    Signer::sign(&SignRequest {
        path: req.url.path(),
        query: &rest,
        content_type: content_type.as_deref(),
        body,
        app_secret: SECRET,
    })
}

pub fn assert_signed(req: &Request) {
    let sent = one(&decoded_query(req), "sign").to_string();
    let body = if req.body.is_empty() { None } else { Some(req.body.as_slice()) };
    assert_eq!(sent, expected_sign(req, body), "sign does not match the request as received");
}

pub async fn last_request(server: &MockServer) -> Request {
    server.received_requests().await.unwrap().pop().expect("the stub saw no request")
}

/// No body arrived (not even `null`), no content type, and the sign is the empty-body form.
pub fn assert_signed_without_body(req: &Request) {
    assert!(req.body.is_empty(), "unexpected body: {:?}", String::from_utf8_lossy(&req.body));
    assert!(req.headers.get("content-type").is_none(), "unexpected content-type");
    assert_eq!(one(&decoded_query(req), "sign"), expected_sign(req, None));
}
