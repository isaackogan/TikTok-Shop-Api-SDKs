//! Verifying and parsing TikTok Shop webhooks.
//!
//! [`verify`] checks the `Authorization` header against the raw body; [`parse`] turns a body into a
//! [`WebhookEvent`], one variant per webhook type; [`verify_and_parse`] does both.
//!
//! Numbers in `String` fields (TikTok sends IDs such as `shop_id` as numbers) become their exact text, up to
//! 64-bit integers; see [`fit`].
//!
//! Always verify the body exactly as it arrived. Re-serializing it (whitespace, key order) changes the
//! bytes and fails the check.
use hmac::{Hmac, Mac};
use serde::de::DeserializeOwned;
use serde_json::Value;
use sha2::Sha256;

use crate::error::Error;
pub use crate::generated::meta::EVENT_TYPES;
pub use crate::generated::webhooks::{string_paths, WebhookEvent};

/// Whether `signature` (the `Authorization` header, lowercase hex) is the HMAC-SHA256, keyed with
/// `app_secret`, of `app_key` followed by `raw_body`. The comparison takes constant time.
pub fn verify(app_key: &str, app_secret: &str, raw_body: &[u8], signature: &str) -> bool {
    let well_formed = signature.len() == 64 && signature.bytes().all(|b| matches!(b, b'0'..=b'9' | b'a'..=b'f'));
    if !well_formed {
        return false;
    }
    let Ok(expected) = hex::decode(signature) else { return false };
    let Ok(mut mac) = Hmac::<Sha256>::new_from_slice(app_secret.as_bytes()) else { return false };
    mac.update(app_key.as_bytes());
    mac.update(raw_body);
    mac.verify_slice(&expected).is_ok()
}

/// Parses a webhook body.
///
/// The integer `type` selects the variant. A `type` that is missing, or not an integer (a string, a bool,
/// null, a float, ...), is an [`Error::Webhook`]. An integer `type` this SDK does not know gives
/// [`WebhookEvent::Unknown`]. Fields the models do not know are ignored. A known type whose fields do not
/// fit its model is an [`Error::Webhook`] that names the field.
pub fn parse(raw_body: &[u8]) -> Result<WebhookEvent, Error> {
    let raw: Value =
        serde_json::from_slice(raw_body).map_err(|e| Error::Webhook(format!("the body is not JSON: {e}")))?;
    if !raw.is_object() {
        return Err(Error::Webhook("the body is not a JSON object".into()));
    }
    let event_type = raw
        .get("type")
        .and_then(Value::as_i64)
        .ok_or_else(|| Error::Webhook("the body has no integer `type`".into()))?;
    crate::generated::webhooks::decode(event_type, raw)
}

/// [`verify`], then [`parse`]. A mismatch is [`Error::WebhookSignature`], whatever the body holds.
pub fn verify_and_parse(
    app_key: &str,
    app_secret: &str,
    raw_body: &[u8],
    signature: &str,
) -> Result<WebhookEvent, Error> {
    if !verify(app_key, app_secret, raw_body, signature) {
        return Err(Error::WebhookSignature);
    }
    parse(raw_body)
}

/// Turns a JSON number at each of `event_type`'s string-typed paths into its exact text.
///
/// TikTok sends ids such as `shop_id` as numbers in some payloads, and serde refuses a number for a
/// `String`. This is what [`parse`] does before decoding a known type; it is public (but hidden) only so
/// the table behind it can be tested.
///
/// Exactness holds up to 64 bits: the body is parsed to a `serde_json::Value` first, so an integer wider
/// than `u64`/`i64` has already become a float by now.
#[doc(hidden)]
pub fn fit(event_type: i64, mut raw: Value) -> Value {
    for path in string_paths(event_type) {
        fit_at(&mut raw, path);
    }
    raw
}

fn fit_at(v: &mut Value, path: &[&str]) {
    match path.split_first() {
        None => {
            if let Value::Number(n) = v {
                *v = Value::String(n.to_string());
            }
        }
        Some((&"*", rest)) => {
            if let Value::Object(map) = v {
                for child in map.values_mut() {
                    fit_at(child, rest);
                }
            }
        }
        Some((&"[]", rest)) => {
            if let Value::Array(items) = v {
                for item in items {
                    fit_at(item, rest);
                }
            }
        }
        Some((key, rest)) => {
            if let Value::Object(map) = v {
                if let Some(child) = map.get_mut(*key) {
                    fit_at(child, rest);
                }
            }
        }
    }
}

/// Used by the generated `decode`: fits the body, decodes it as `T`, wraps it.
pub(crate) fn known<T: DeserializeOwned>(
    event_type: i64,
    raw: Value,
    wrap: fn(Box<T>) -> WebhookEvent,
) -> Result<WebhookEvent, Error> {
    serde_json::from_value::<T>(fit(event_type, raw))
        .map(|model| wrap(Box::new(model)))
        .map_err(|e| Error::Webhook(format!("type {event_type}: {e}")))
}

#[cfg(test)]
mod tests {
    use super::fit_at;
    use serde_json::json;

    #[test]
    fn a_wildcard_segment_fits_every_value_of_a_map() {
        let mut v = json!({"labels": {"a": 7494049642642441621u64, "b": "x", "c": null}, "n": 1});
        fit_at(&mut v, &["labels", "*"]);
        assert_eq!(v, json!({"labels": {"a": "7494049642642441621", "b": "x", "c": null}, "n": 1}));
    }
}
