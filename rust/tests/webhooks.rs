//! Webhook verification and parsing against the shared `webhooks.json` vectors.
use serde_json::{json, Value};
use tiktok_shop_api::generated::meta::{EVENT_TYPES as META_EVENT_TYPES, WEBHOOKS};
use tiktok_shop_api::generated::models;
use tiktok_shop_api::webhooks::{self, EVENT_TYPES};
use tiktok_shop_api::{Error, WebhookEvent};

fn vectors() -> Value {
    serde_json::from_str(include_str!("../../shared/test-vectors/webhooks.json")).unwrap()
}

#[test]
fn verify_matches_every_vector() {
    for c in vectors()["verify"].as_array().unwrap() {
        let got = webhooks::verify(
            c["appKey"].as_str().unwrap(),
            c["appSecret"].as_str().unwrap(),
            c["rawBody"].as_str().unwrap().as_bytes(),
            c["signature"].as_str().unwrap(),
        );
        assert_eq!(got, c["valid"].as_bool().unwrap(), "{}", c["name"]);
    }
}

#[test]
fn verify_rejects_a_wrong_length_and_non_hex_signature() {
    let c = &vectors()["verify"][0];
    let (k, s, b) = (c["appKey"].as_str().unwrap(), c["appSecret"].as_str().unwrap(), c["rawBody"].as_str().unwrap());
    let sig = c["signature"].as_str().unwrap();
    assert!(webhooks::verify(k, s, b.as_bytes(), sig));
    assert!(!webhooks::verify(k, s, b.as_bytes(), &sig[..sig.len() - 2]));
    assert!(!webhooks::verify(k, s, b.as_bytes(), &format!("{sig}00")));
    assert!(!webhooks::verify(k, s, b.as_bytes(), &format!("zz{}", &sig[2..])));
    assert!(!webhooks::verify("other", s, b.as_bytes(), sig));
}

#[test]
fn parse_matches_every_vector() {
    for c in vectors()["parse"].as_array().unwrap() {
        let ev = webhooks::parse(c["rawBody"].as_str().unwrap().as_bytes()).unwrap();
        assert_eq!(ev.event_type(), c["type"].as_i64().unwrap(), "{}", c["name"]);
        match (c["known"].as_bool().unwrap(), &ev) {
            (true, WebhookEvent::Unknown { .. }) => panic!("{} should be known", c["name"]),
            (false, WebhookEvent::Unknown { raw, .. }) => assert_eq!(raw["type"], c["type"]),
            (false, other) => panic!("{} should be unknown: {other:?}", c["name"]),
            (true, _) => {}
        }
    }
}

#[test]
fn an_order_status_change_narrows_to_its_model() {
    let body = vectors()["parse"][0]["rawBody"].as_str().unwrap().to_owned();
    match webhooks::parse(body.as_bytes()).unwrap() {
        WebhookEvent::OrderStatusChange(m) => {
            let m: &models::OrderStatusChangeWebhook = &m;
            assert_eq!(m.shop_id.as_deref(), Some("7495540735365777507"));
            let data = m.data.as_ref().unwrap();
            assert_eq!(data.order_id.as_deref(), Some("576653688135258178"));
            assert_eq!(data.order_status.as_deref(), Some("UNPAID"));
        }
        other => panic!("{other:?}"),
    }
}

#[test]
fn verify_and_parse_checks_the_signature_first() {
    let c = &vectors()["verify"][0];
    let (k, s, b, sig) = (
        c["appKey"].as_str().unwrap(),
        c["appSecret"].as_str().unwrap(),
        c["rawBody"].as_str().unwrap().as_bytes(),
        c["signature"].as_str().unwrap(),
    );
    assert!(matches!(webhooks::verify_and_parse(k, s, b, sig), Ok(WebhookEvent::OrderStatusChange(_))));
    let err = webhooks::verify_and_parse(k, s, b, "0".repeat(64).as_str()).unwrap_err();
    assert!(matches!(err, Error::WebhookSignature), "{err:?}");
    // A bad signature on a bad body is still a signature error.
    let err = webhooks::verify_and_parse(k, s, b"not json", "x").unwrap_err();
    assert!(matches!(err, Error::WebhookSignature));
}

#[test]
fn a_shop_id_sent_as_a_number_keeps_its_exact_value() {
    let body = br#"{"type":1,"tts_notification_id":"1","shop_id":7494049642642441621,"timestamp":1,"data":{"order_id":576653688135258178,"order_status":"UNPAID"}}"#;
    let WebhookEvent::OrderStatusChange(m) = webhooks::parse(body).unwrap() else { panic!() };
    assert_eq!(m.shop_id.as_deref(), Some("7494049642642441621"));
    assert_eq!(m.data.unwrap().order_id.as_deref(), Some("576653688135258178"), "a nested id too");
}

/// For every webhook, every array path in the rendered table: a number at each element becomes its text.
#[test]
fn numbers_in_string_fields_are_fitted_inside_arrays() {
    let mut checked = 0;
    for w in WEBHOOKS {
        for path in webhooks::string_paths(w.webhook_type).iter().filter(|p| p.contains(&"[]")) {
            let mut leaf = json!(7494049642642441621u64);
            for seg in path.iter().rev() {
                leaf = if *seg == "[]" { json!([leaf.clone(), leaf]) } else { json!({ *seg: leaf }) };
            }
            let fitted = webhooks::fit(w.webhook_type, leaf);
            let mut cur = &fitted;
            for seg in *path {
                cur = if *seg == "[]" {
                    assert_eq!(cur.as_array().unwrap().len(), 2);
                    &cur[1]
                } else {
                    &cur[*seg]
                };
            }
            assert_eq!(cur, &json!("7494049642642441621"), "{} {:?}", w.schema, path);
            checked += 1;
        }
    }
    assert!(checked > 0, "no webhook model has a string inside an array");
}

/// A required `String` field (AppealCompleted: shop_id) and one inside an array element, through `parse`.
#[test]
fn required_and_array_string_fields_accept_numbers_through_parse() {
    let body = br#"{"type":66,"tts_notification_id":1,"shop_id":7494049642642441621,"timestamp":1,
        "data":{"product_id":3,"appeal_task":{"appeal_audit_result":[{"indicator_type":5,"status":6}]}}}"#;
    let WebhookEvent::AppealCompleted(m) = webhooks::parse(body).unwrap() else { panic!() };
    assert_eq!(m.shop_id, "7494049642642441621");
    assert_eq!(m.tts_notification_id, "1");
    let r = &m.data.appeal_task.appeal_audit_result[0];
    assert_eq!((r.indicator_type.as_str(), r.status.as_str()), ("5", "6"));
}

#[test]
fn unknown_fields_still_parse() {
    let body = br#"{"type":1,"brand_new":{"a":1},"shop_id":"1","data":{"order_id":"2","also_new":[1,2]}}"#;
    assert!(matches!(webhooks::parse(body), Ok(WebhookEvent::OrderStatusChange(_))));
}

#[test]
fn an_unknown_type_is_the_generic_event_with_the_raw_body() {
    let body = br#"{"type":9999,"shop_id":7494049642642441621,"data":{}}"#;
    match webhooks::parse(body).unwrap() {
        WebhookEvent::Unknown { event_type, raw } => {
            assert_eq!(event_type, 9999);
            assert_eq!(raw["shop_id"].as_u64(), Some(7494049642642441621), "digits kept in raw");
        }
        other => panic!("{other:?}"),
    }
}

#[test]
fn a_missing_or_non_integer_type_is_rejected() {
    for body in [
        r#"{"shop_id":"1"}"#,
        r#"{"type":"1"}"#,
        r#"{"type":true}"#,
        r#"{"type":null}"#,
        r#"{"type":1.5}"#,
        r#"{"type":1.0}"#,
        r#"{"type":[1]}"#,
        r#"{"type":{"a":1}}"#,
        r#"[1]"#,
        r#""x""#,
        "not json",
        "",
    ] {
        let err = webhooks::parse(body.as_bytes()).unwrap_err();
        assert!(matches!(err, Error::Webhook(_)), "{body}: {err:?}");
    }
}

#[test]
fn a_known_type_missing_a_required_field_names_it() {
    let err = webhooks::parse(br#"{"type":66,"tts_notification_id":"1","timestamp":1,"data":{"product_id":1,"appeal_task":{"appeal_audit_result":[]}}}"#)
        .unwrap_err();
    let text = err.to_string();
    assert!(matches!(err, Error::Webhook(_)), "{err:?}");
    assert!(text.contains("shop_id"), "{text}");
    // A wrongly typed field is an error too, not a silent default.
    assert!(webhooks::parse(br#"{"type":1,"timestamp":"soon"}"#).is_err());
}

#[test]
fn event_types_cover_the_named_webhooks() {
    assert_eq!(EVENT_TYPES.iter().find(|(t, _)| *t == 1).map(|(_, n)| *n), Some("ORDER_STATUS_CHANGE"));
    assert_eq!(EVENT_TYPES, META_EVENT_TYPES);
    assert!(!EVENT_TYPES.is_empty());
    let named = WEBHOOKS.iter().filter(|w| w.event_type.is_some()).count();
    assert_eq!(EVENT_TYPES.len(), named);
}

#[test]
fn every_webhook_in_the_spec_has_a_variant() {
    for w in WEBHOOKS {
        let body = json!({"type": w.webhook_type});
        let ev = webhooks::parse(body.to_string().as_bytes());
        match ev {
            Ok(WebhookEvent::Unknown { .. }) => panic!("{} has no variant", w.schema),
            Ok(e) => assert_eq!(e.event_type(), w.webhook_type),
            // A model with required fields rejects the empty body, which proves the type is known.
            Err(Error::Webhook(m)) => assert!(m.starts_with(&format!("type {}:", w.webhook_type)), "{}: {m}", w.schema),
            Err(e) => panic!("{}: {e}", w.schema),
        }
    }
}

#[test]
fn the_rendered_table_has_the_expected_paths_for_real_models() {
    let has = |ty: i64, path: &[&str]| webhooks::string_paths(ty).iter().any(|p| *p == path);
    assert!(has(1, &["shop_id"]));
    assert!(has(1, &["tts_notification_id"]));
    assert!(has(1, &["data", "order_id"]));
    assert!(has(66, &["data", "appeal_task", "appeal_audit_result", "[]", "indicator_type"]));
    assert!(!has(1, &["timestamp"]), "an integer field is not in the table");
    assert!(!has(1, &["type"]), "the integer type is not in the table");
    assert!(!has(1, &["data"]), "an object is not in the table");
    assert!(webhooks::string_paths(9999).is_empty());
}
