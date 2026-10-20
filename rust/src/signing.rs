//! Request signing: the pure [`Signer`], [`requires_shop_cipher`], and the middleware that applies both.
use std::sync::Arc;
use std::time::{SystemTime, UNIX_EPOCH};

use hmac::{Hmac, Mac};
use reqwest::header::{HeaderValue, CONTENT_TYPE};
use reqwest::{Request, Response};
use reqwest_middleware::{Middleware, Next};
use serde_json::Value;
use sha2::Sha256;

use crate::error::Error;
use crate::generated::meta::OPERATIONS;

/// What a signature covers.
#[derive(Debug, Clone, Copy)]
pub struct SignRequest<'a> {
    /// The request path, e.g. `/order/202309/orders/search`.
    pub path: &'a str,
    /// Query parameters with their decoded values, as the server reads them.
    pub query: &'a [(String, String)],
    /// The `Content-Type` header. A `multipart/form-data` body is not signed.
    pub content_type: Option<&'a str>,
    /// The exact request body.
    pub body: Option<&'a [u8]>,
    pub app_secret: &'a str,
}

/// The pure signing functions.
pub struct Signer;

fn is_multipart(content_type: Option<&str>) -> bool {
    content_type.and_then(|c| c.split(';').next()).is_some_and(|m| m.trim().eq_ignore_ascii_case("multipart/form-data"))
}

impl Signer {
    fn bytes_to_sign(r: &SignRequest) -> Vec<u8> {
        let mut pairs: Vec<&(String, String)> =
            r.query.iter().filter(|(k, _)| k != "sign" && k != "access_token").collect();
        pairs.sort_by(|a, b| a.0.cmp(&b.0));
        let mut out = Vec::new();
        out.extend_from_slice(r.app_secret.as_bytes());
        out.extend_from_slice(r.path.as_bytes());
        for (k, v) in pairs {
            out.extend_from_slice(k.as_bytes());
            out.extend_from_slice(v.as_bytes());
        }
        if !is_multipart(r.content_type) {
            if let Some(b) = r.body {
                out.extend_from_slice(b);
            }
        }
        out.extend_from_slice(r.app_secret.as_bytes());
        out
    }

    /// `secret + path + sorted key+value pairs (without sign and access_token) + body (unless multipart) + secret`.
    pub fn string_to_sign(r: &SignRequest) -> String {
        String::from_utf8_lossy(&Self::bytes_to_sign(r)).into_owned()
    }

    /// The lowercase hex HMAC-SHA256 of the string to sign, keyed with the app secret.
    pub fn sign(r: &SignRequest) -> String {
        let mut mac = Hmac::<Sha256>::new_from_slice(r.app_secret.as_bytes()).expect("HMAC accepts any key length");
        mac.update(&Self::bytes_to_sign(r));
        hex::encode(mac.finalize().into_bytes())
    }
}

/// Whether the operation matching `method` and `path` takes a `shop_cipher` query parameter. A `{x}` in a
/// path template matches exactly one segment; the template with the most literal segments wins.
pub fn requires_shop_cipher(method: &str, path: &str) -> bool {
    let segments: Vec<&str> = path.split('/').collect();
    let mut best: Option<(usize, bool)> = None;
    for op in OPERATIONS.iter().filter(|o| o.http_method.eq_ignore_ascii_case(method)) {
        let template: Vec<&str> = op.path.split('/').collect();
        if template.len() != segments.len() {
            continue;
        }
        let mut literals = 0;
        let matches = template.iter().zip(&segments).all(|(t, s)| {
            if t.starts_with('{') && t.ends_with('}') {
                !s.is_empty()
            } else {
                literals += 1;
                t == s
            }
        });
        if matches && best.is_none_or(|(l, _)| literals > l) {
            best = Some((literals, op.requires_shop_cipher));
        }
    }
    best.is_some_and(|(_, needs)| needs)
}

const UNRESERVED: &[u8] = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~";

/// RFC 3986 percent-encoding: everything but the unreserved characters.
pub(crate) fn encode(s: &str) -> String {
    let mut out = String::with_capacity(s.len());
    for &b in s.as_bytes() {
        if UNRESERVED.contains(&b) {
            out.push(b as char);
        } else {
            out.push_str(&format!("%{b:02X}"));
        }
    }
    out
}

const RESERVED: [&str; 4] = ["app_key", "timestamp", "sign", "shop_cipher"];

struct Credentials {
    app_key: String,
    app_secret: String,
    access_token: Option<String>,
    shop_cipher: Option<String>,
}

/// The request and response hook. It signs every request and turns every failed reply into an [`Error`]
/// (boxed in the middleware error; the group wrappers unbox it).
pub struct SigningMiddleware {
    creds: Arc<Credentials>,
}

impl SigningMiddleware {
    /// An empty `access_token` or `shop_cipher` counts as none.
    pub fn new(
        app_key: impl Into<String>,
        app_secret: impl Into<String>,
        access_token: Option<String>,
        shop_cipher: Option<String>,
    ) -> Self {
        let non_empty = |v: Option<String>| v.filter(|s| !s.is_empty());
        Self {
            creds: Arc::new(Credentials {
                app_key: app_key.into(),
                app_secret: app_secret.into(),
                access_token: non_empty(access_token),
                shop_cipher: non_empty(shop_cipher),
            }),
        }
    }

    fn sign_request(&self, req: &mut Request) -> Result<(), Error> {
        let c = &self.creds;
        let mut query: Vec<(String, String)> = req
            .url()
            .query_pairs()
            .map(|(k, v)| (k.into_owned(), v.into_owned()))
            .filter(|(k, _)| !RESERVED.contains(&k.as_str()))
            .collect();
        if let Some(cipher) = &c.shop_cipher {
            if requires_shop_cipher(req.method().as_str(), req.url().path()) {
                query.push(("shop_cipher".into(), cipher.clone()));
            }
        }
        let now = SystemTime::now().duration_since(UNIX_EPOCH).map(|d| d.as_secs()).unwrap_or(0);
        query.push(("app_key".into(), c.app_key.clone()));
        query.push(("timestamp".into(), now.to_string()));

        match c.access_token.as_deref().map(HeaderValue::from_str) {
            Some(Ok(mut v)) => {
                v.set_sensitive(true);
                req.headers_mut().insert("x-tts-access-token", v);
            }
            // The message never includes the token.
            Some(Err(_)) => return Err(Error::Other("the access token is not a valid HTTP header value".into())),
            None => {
                req.headers_mut().remove("x-tts-access-token");
            }
        }

        // The generated functions serialize an absent optional body as the JSON `null`. No body is meant.
        if req.body().and_then(|b| b.as_bytes()) == Some(b"null") {
            *req.body_mut() = None;
            req.headers_mut().remove(CONTENT_TYPE);
            req.headers_mut().remove(reqwest::header::CONTENT_LENGTH);
        }

        // A streaming body (a multipart upload) has no bytes to read, and multipart is never signed anyway.
        let body = req.body().and_then(|b| b.as_bytes());
        let content_type = req.headers().get(CONTENT_TYPE).and_then(|v| v.to_str().ok());
        let sign = Signer::sign(&SignRequest {
            path: req.url().path(),
            query: &query,
            content_type,
            body,
            app_secret: &c.app_secret,
        });
        query.push(("sign".into(), sign));

        let raw = query.iter().map(|(k, v)| format!("{}={}", encode(k), encode(v))).collect::<Vec<_>>().join("&");
        req.url_mut().set_query(Some(&raw));
        Ok(())
    }
}

impl std::fmt::Debug for SigningMiddleware {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.debug_struct("SigningMiddleware").field("app_key", &self.creds.app_key).finish_non_exhaustive()
    }
}

#[async_trait::async_trait]
impl Middleware for SigningMiddleware {
    async fn handle(
        &self,
        mut req: Request,
        extensions: &mut http::Extensions,
        next: Next<'_>,
    ) -> reqwest_middleware::Result<Response> {
        self.sign_request(&mut req).map_err(reqwest_middleware::Error::middleware)?;
        let resp = next.run(req, extensions).await?;

        let status = resp.status();
        let version = resp.version();
        let headers = resp.headers().clone();
        let data = resp.bytes().await.map_err(reqwest_middleware::Error::Reqwest)?;
        if let Err(e) = check_response(status.as_u16(), status.canonical_reason(), &data) {
            return Err(reqwest_middleware::Error::middleware(e));
        }
        let mut rebuilt = http::Response::builder().status(status).version(version);
        if let Some(h) = rebuilt.headers_mut() {
            *h = headers;
        }
        let rebuilt =
            rebuilt.body(data).map_err(|e| reqwest_middleware::Error::middleware(Error::Other(e.to_string())))?;
        Ok(Response::from(rebuilt))
    }
}

/// The response hook: `Ok` for a successful envelope, otherwise the [`Error::Api`].
pub(crate) fn check_response(status: u16, reason: Option<&str>, data: &[u8]) -> Result<(), Error> {
    let ok = (200..300).contains(&status);
    let parsed: Result<Value, _> = serde_json::from_slice(data);
    if ok && !matches!(parsed, Ok(Value::Object(_))) {
        return Err(Error::Api {
            code: -1,
            message: format!("Response is not valid JSON (HTTP {status})"),
            request_id: String::new(),
            http_status: Some(status),
        });
    }
    let env = parsed.ok();
    let field = |name: &str| env.as_ref().and_then(|v| v.get(name));
    let code = field("code").and_then(Value::as_i64);
    let message = field("message").and_then(Value::as_str).map(str::to_owned);
    let request_id = field("request_id").and_then(Value::as_str).unwrap_or_default().to_owned();
    if !ok {
        return Err(Error::Api {
            code: code.filter(|c| *c != 0).unwrap_or(i64::from(status)),
            message: message.or_else(|| reason.map(str::to_owned)).unwrap_or_else(|| format!("HTTP {status}")),
            request_id,
            http_status: Some(status),
        });
    }
    match code {
        Some(c) if c != 0 => {
            Err(Error::Api { code: c, message: message.unwrap_or_default(), request_id, http_status: Some(status) })
        }
        _ => Ok(()),
    }
}
