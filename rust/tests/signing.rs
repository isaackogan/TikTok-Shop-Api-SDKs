//! Signer: the shared vectors, and `requires_shop_cipher`.
use serde_json::Value;
use tiktok_shop_api::signing::{requires_shop_cipher, SignRequest, Signer};

fn vectors() -> Vec<Value> {
    let text =
        std::fs::read_to_string(concat!(env!("CARGO_MANIFEST_DIR"), "/../shared/test-vectors/signing.json")).unwrap();
    serde_json::from_str::<Value>(&text).unwrap()["cases"].as_array().unwrap().clone()
}

#[test]
fn every_signing_vector_matches() {
    let cases = vectors();
    assert!(!cases.is_empty());
    for c in cases {
        let name = c["name"].as_str().unwrap();
        let query: Vec<(String, String)> = c["query"]
            .as_array()
            .unwrap()
            .iter()
            .map(|p| (p[0].as_str().unwrap().to_string(), p[1].as_str().unwrap().to_string()))
            .collect();
        let body = c["body"].as_str().map(|b| b.as_bytes().to_vec());
        let req = SignRequest {
            path: c["path"].as_str().unwrap(),
            query: &query,
            content_type: c["contentType"].as_str(),
            body: body.as_deref(),
            app_secret: c["secret"].as_str().unwrap(),
        };
        assert_eq!(Signer::string_to_sign(&req), c["stringToSign"].as_str().unwrap(), "{name}: string to sign");
        assert_eq!(Signer::sign(&req), c["sign"].as_str().unwrap(), "{name}: sign");
    }
}

#[test]
fn shop_cipher_is_required_for_these_operations() {
    assert!(requires_shop_cipher("POST", "/order/202309/orders/search"));
    assert!(!requires_shop_cipher("GET", "/authorization/202309/shops"));
    assert!(requires_shop_cipher("GET", "/product/202309/products/1729507467923261408"));
}

#[test]
fn shop_cipher_lookup_ignores_method_case_and_unknown_paths() {
    assert!(requires_shop_cipher("post", "/order/202309/orders/search"));
    assert!(!requires_shop_cipher("GET", "/no/such/path"));
    // A "{x}" template matches exactly one segment.
    assert!(!requires_shop_cipher("GET", "/product/202309/products/1/2/3"));
}
