//! OAuth: the authorization URL, and the exchange of an `auth_code` or a refresh token for tokens.
//!
//! The token endpoints take `app_secret`, `auth_code` and `refresh_token` in the URL's query, so no
//! error from this module carries the URL, its query, or any of those values.
use std::fmt;
use std::time::Duration;

use serde_json::Value;

use crate::client::DEFAULT_TIMEOUT;
use crate::error::Error;
use crate::signing::encode;

/// Where the token endpoints live.
pub const DEFAULT_AUTH_BASE_URL: &str = "https://auth.tiktok-shops.com";

const USER_AGENT: &str = concat!("tiktok-shop-api-rust/", env!("CARGO_PKG_VERSION"));

/// Whose authorization page [`TikTokShopAuth::authorization_url`] points at.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum AuthType {
    /// A seller authorizes your app. Needs a service ID.
    Seller,
    /// A partner authorizes your app. Needs a service ID.
    Partner,
    /// An affiliate creator authorizes your app.
    Creator,
}

/// The United States host, or the rest of the world's.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum Region {
    Us,
    Row,
}

/// Settings for [`TikTokShopAuth::new`].
#[derive(Clone)]
pub struct AuthOptions {
    pub app_key: String,
    pub app_secret: String,
    /// Your Partner Center service ID. Needed for seller and partner authorization URLs.
    pub service_id: Option<String>,
    /// Overrides [`DEFAULT_AUTH_BASE_URL`], e.g. for a test server.
    pub base_url: Option<String>,
    /// Bounds one token request. `None` (or zero) means no limit. [`AuthOptions::new`] sets
    /// [`DEFAULT_TIMEOUT`]. Ignored when you pass your own [`http_client`](AuthOptions::http_client).
    pub timeout: Option<Duration>,
    /// Your own HTTP client, used as is. The default follows no redirects, so a redirect reply is an
    /// [`Error::Api`] with its HTTP status and the query (which holds your secret) is never forwarded.
    pub http_client: Option<reqwest::Client>,
}

impl AuthOptions {
    pub fn new(app_key: impl Into<String>, app_secret: impl Into<String>) -> Self {
        Self {
            app_key: app_key.into(),
            app_secret: app_secret.into(),
            service_id: None,
            base_url: None,
            timeout: Some(DEFAULT_TIMEOUT),
            http_client: None,
        }
    }

    pub fn service_id(mut self, id: impl Into<String>) -> Self {
        self.service_id = Some(id.into());
        self
    }

    pub fn base_url(mut self, url: impl Into<String>) -> Self {
        self.base_url = Some(url.into());
        self
    }

    /// `None` means no limit.
    pub fn timeout(mut self, timeout: Option<Duration>) -> Self {
        self.timeout = timeout;
        self
    }

    pub fn http_client(mut self, client: reqwest::Client) -> Self {
        self.http_client = Some(client);
        self
    }
}

impl fmt::Debug for AuthOptions {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("AuthOptions")
            .field("app_key", &self.app_key)
            .field("app_secret", &"[redacted]")
            .field("service_id", &self.service_id)
            .field("base_url", &self.base_url)
            .field("timeout", &self.timeout)
            .field("http_client", &self.http_client.as_ref().map(|_| "<custom>"))
            .finish()
    }
}

/// The result of exchanging a code or refreshing a token.
///
/// Only the four token fields are guaranteed; creator and partner tokens may lack the seller fields.
#[derive(Clone, PartialEq, Eq)]
pub struct TokenSet {
    pub access_token: String,
    /// The Unix time (seconds) at which the access token expires.
    pub access_token_expire_in: i64,
    pub refresh_token: String,
    /// The Unix time (seconds) at which the refresh token expires.
    pub refresh_token_expire_in: i64,
    /// Kept as text: it is an id, exact even when TikTok sends it as a number, up to 64-bit integers (the
    /// reply is parsed to a `serde_json::Value` first, so a wider integer has already lost digits).
    pub open_id: Option<String>,
    pub seller_name: Option<String>,
    pub seller_base_region: Option<String>,
    pub user_type: Option<i64>,
    pub granted_scopes: Option<Vec<String>>,
}

impl fmt::Debug for TokenSet {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("TokenSet")
            .field("access_token", &"[redacted]")
            .field("access_token_expire_in", &self.access_token_expire_in)
            .field("refresh_token", &"[redacted]")
            .field("refresh_token_expire_in", &self.refresh_token_expire_in)
            .field("open_id", &self.open_id)
            .field("seller_name", &self.seller_name)
            .field("seller_base_region", &self.seller_base_region)
            .field("user_type", &self.user_type)
            .field("granted_scopes", &self.granted_scopes)
            .finish()
    }
}

/// The OAuth helper: authorization URLs, code exchange and token refresh.
pub struct TikTokShopAuth {
    options: AuthOptions,
    base: String,
    http: reqwest::Client,
}

impl TikTokShopAuth {
    /// Builds the helper. Fails only if the HTTP client cannot be built (e.g. the TLS backend cannot start).
    pub fn new(mut options: AuthOptions) -> Result<Self, Error> {
        let http = match options.http_client.take() {
            Some(c) => c,
            None => {
                // No redirects: the query holds the app secret and must never be forwarded.
                let mut b =
                    reqwest::Client::builder().redirect(reqwest::redirect::Policy::none()).user_agent(USER_AGENT);
                if let Some(t) = options.timeout.filter(|t| !t.is_zero()) {
                    b = b.timeout(t);
                }
                b.build().map_err(Error::from_reqwest)?
            }
        };
        let base = options.base_url.as_deref().unwrap_or(DEFAULT_AUTH_BASE_URL).trim_end_matches('/').to_owned();
        Ok(Self { options, base, http })
    }

    /// The page to send the seller (or partner, or creator) to. `state` is echoed back to your redirect URL.
    pub fn authorization_url(&self, kind: AuthType, region: Region, state: Option<&str>) -> Result<String, Error> {
        let (us, row, path) = match kind {
            AuthType::Seller => {
                ("https://services.us.tiktokshop.com", "https://services.tiktokshop.com", "/open/authorize")
            }
            AuthType::Partner => {
                ("https://partner.us.tiktokshop.com", "https://partner.tiktokshop.com", "/open/authorize")
            }
            AuthType::Creator => ("https://shop.tiktok.com", "https://shop.tiktok.com", "/alliance/creator/auth"),
        };
        let host = if region == Region::Us { us } else { row };
        let first = match kind {
            AuthType::Creator => format!("app_key={}", encode(&self.options.app_key)),
            _ => match self.options.service_id.as_deref().filter(|s| !s.is_empty()) {
                Some(id) => format!("service_id={}", encode(id)),
                None => {
                    return Err(Error::Other(format!(
                        "service_id is required for {kind:?} authorization URLs (AuthOptions::service_id)"
                    )))
                }
            },
        };
        let mut url = format!("{host}{path}?{first}");
        if let Some(state) = state.filter(|s| !s.is_empty()) {
            url.push_str("&state=");
            url.push_str(&encode(state));
        }
        Ok(url)
    }

    /// Trades the `auth_code` from your redirect URL for tokens.
    pub async fn exchange_code(&self, auth_code: &str) -> Result<TokenSet, Error> {
        self.token("get", [("auth_code", auth_code), ("grant_type", "authorized_code")]).await
    }

    /// Trades a refresh token for new tokens.
    pub async fn refresh(&self, refresh_token: &str) -> Result<TokenSet, Error> {
        self.token("refresh", [("refresh_token", refresh_token), ("grant_type", "refresh_token")]).await
    }

    async fn token(&self, endpoint: &str, extra: [(&str, &str); 2]) -> Result<TokenSet, Error> {
        let query = [("app_key", self.options.app_key.as_str()), ("app_secret", self.options.app_secret.as_str())]
            .into_iter()
            .chain(extra)
            .map(|(k, v)| format!("{k}={}", encode(v)))
            .collect::<Vec<_>>()
            .join("&");
        let url = format!("{}/api/v2/token/{endpoint}?{query}", self.base);
        // reqwest's errors are stripped of the URL (Error::from_reqwest), which holds the secret and the code.
        let response = self.http.get(url).send().await.map_err(Error::from_reqwest)?;
        let status = response.status().as_u16();
        let body = response.bytes().await.map_err(Error::from_reqwest)?;
        to_token_set(status, &body)
    }
}

impl fmt::Debug for TikTokShopAuth {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("TikTokShopAuth").field("options", &self.options).finish_non_exhaustive()
    }
}

fn to_token_set(status: u16, body: &[u8]) -> Result<TokenSet, Error> {
    let ok = (200..300).contains(&status);
    let api = |code: i64, message: String, request_id: String| Error::Api {
        code,
        message,
        request_id,
        http_status: Some(status),
    };
    let env = match serde_json::from_slice::<Value>(body) {
        Ok(v @ Value::Object(_)) => v,
        // R13b: a non-2xx reply has the HTTP status as its code whatever the body; only an unreadable 2xx is -1.
        _ => {
            let code = if ok { -1 } else { i64::from(status) };
            return Err(api(code, format!("unparseable token response (HTTP {status})"), String::new()));
        }
    };
    let text = |name: &str| env.get(name).and_then(Value::as_str).unwrap_or_default().to_owned();
    let request_id = text("request_id");
    let mut code = env.get("code").and_then(Value::as_i64).unwrap_or(if ok { -1 } else { i64::from(status) });
    if code != 0 || !ok {
        if code == 0 {
            code = i64::from(status);
        }
        let message = Some(text("message")).filter(|m| !m.is_empty()).unwrap_or_else(|| format!("HTTP {status}"));
        return Err(api(code, message, request_id));
    }
    let fail = |message: String| api(-1, message, request_id.clone());
    let Some(data) = env.get("data").and_then(Value::as_object) else {
        return Err(fail("token response has no data".into()));
    };

    // The messages name fields, never values: the values are tokens.
    let token = |name: &str| match data.get(name) {
        Some(Value::String(s)) if !s.is_empty() => Ok(s.clone()),
        _ => Err(fail(format!("token response has a missing or invalid `{name}`"))),
    };
    let expiry = |name: &str| match data.get(name) {
        Some(Value::Number(n)) if n.as_i64().is_some() => Ok(n.as_i64().unwrap_or_default()),
        _ => Err(fail(format!("token response has a missing or invalid `{name}`"))),
    };
    let bad = |name: &str| fail(format!("token response has an invalid `{name}`"));
    let optional_string = |name: &str| match data.get(name) {
        None | Some(Value::Null) => Ok(None),
        Some(Value::String(s)) => Ok(Some(s.clone())),
        Some(_) => Err(bad(name)),
    };

    let access_token = token("access_token")?;
    let access_token_expire_in = expiry("access_token_expire_in")?;
    let refresh_token = token("refresh_token")?;
    let refresh_token_expire_in = expiry("refresh_token_expire_in")?;
    // An id: keep its digits whether TikTok sends a string or a number.
    let open_id = match data.get("open_id") {
        None | Some(Value::Null) => None,
        Some(Value::String(s)) => Some(s.clone()),
        Some(Value::Number(n)) => Some(n.to_string()),
        Some(_) => return Err(bad("open_id")),
    };
    let user_type = match data.get("user_type") {
        None | Some(Value::Null) => None,
        Some(Value::Number(n)) if n.as_i64().is_some() => n.as_i64(),
        Some(_) => return Err(bad("user_type")),
    };
    let granted_scopes = match data.get("granted_scopes") {
        None | Some(Value::Null) => None,
        Some(Value::Array(items)) => Some(
            items
                .iter()
                .map(|s| s.as_str().map(str::to_owned).ok_or_else(|| bad("granted_scopes")))
                .collect::<Result<Vec<_>, _>>()?,
        ),
        Some(_) => return Err(bad("granted_scopes")),
    };
    Ok(TokenSet {
        access_token,
        access_token_expire_in,
        refresh_token,
        refresh_token_expire_in,
        open_id,
        seller_name: optional_string("seller_name")?,
        seller_base_region: optional_string("seller_base_region")?,
        user_type,
        granted_scopes,
    })
}
