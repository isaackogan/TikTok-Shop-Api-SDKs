//! [`TikTokShop`], its [`Options`], and [`Shop`] for `with_shop`.
use std::fmt;
use std::sync::Arc;
use std::time::Duration;

use reqwest_middleware::ClientBuilder;

use crate::error::Error;
use crate::generated::apis::configuration::Configuration;
use crate::generated::groups::*;
use crate::signing::SigningMiddleware;

/// The TikTok Shop API's address.
pub const DEFAULT_BASE_URL: &str = "https://open-api.tiktokglobalshop.com";
/// How long one request may take, response included, unless [`Options::timeout`] says otherwise.
pub const DEFAULT_TIMEOUT: Duration = Duration::from_secs(30);

const USER_AGENT: &str = concat!("tiktok-shop-api-rust/", env!("CARGO_PKG_VERSION"));

/// Settings for [`TikTokShop::new`].
#[derive(Clone)]
pub struct Options {
    pub app_key: String,
    pub app_secret: String,
    /// Sent as the `x-tts-access-token` header. `None` or empty sends none.
    pub access_token: Option<String>,
    /// Added to the operations that take one. `None` or empty adds none.
    pub shop_cipher: Option<String>,
    /// Overrides [`DEFAULT_BASE_URL`], e.g. for a test server.
    pub base_url: Option<String>,
    /// Bounds one request, response body included. `None` (or zero) means no limit. [`Options::new`] sets
    /// [`DEFAULT_TIMEOUT`]. Ignored when you pass your own [`http_client`](Options::http_client).
    pub timeout: Option<Duration>,
    /// Your own HTTP client (proxy, TLS roots, its own timeout, redirect policy, ...), used as is. The default
    /// honours the proxy environment variables (`HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY`) and follows no
    /// redirects, so a redirect reply is an [`Error::Api`](crate::Error::Api) with its HTTP status.
    pub http_client: Option<reqwest::Client>,
}

impl Options {
    pub fn new(app_key: impl Into<String>, app_secret: impl Into<String>) -> Self {
        Self {
            app_key: app_key.into(),
            app_secret: app_secret.into(),
            access_token: None,
            shop_cipher: None,
            base_url: None,
            timeout: Some(DEFAULT_TIMEOUT),
            http_client: None,
        }
    }

    pub fn access_token(mut self, token: impl Into<String>) -> Self {
        self.access_token = Some(token.into());
        self
    }

    pub fn shop_cipher(mut self, cipher: impl Into<String>) -> Self {
        self.shop_cipher = Some(cipher.into());
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

impl fmt::Debug for Options {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let redact = |v: &Option<String>| v.as_ref().map(|_| "[redacted]");
        f.debug_struct("Options")
            .field("app_key", &self.app_key)
            .field("app_secret", &"[redacted]")
            .field("access_token", &redact(&self.access_token))
            .field("shop_cipher", &redact(&self.shop_cipher))
            .field("base_url", &self.base_url)
            .field("timeout", &self.timeout)
            .field("http_client", &self.http_client.as_ref().map(|_| "<custom>"))
            .finish()
    }
}

#[derive(Clone, Debug, PartialEq, Eq, Default)]
enum Change {
    #[default]
    Keep,
    Set(String),
    Clear,
}

impl Change {
    fn apply(&self, current: &Option<String>) -> Option<String> {
        match self {
            Change::Keep => current.clone(),
            Change::Set(v) if v.is_empty() => None,
            Change::Set(v) => Some(v.clone()),
            Change::Clear => None,
        }
    }
}

/// What [`TikTokShop::with_shop`] changes. A value you do not name is kept; naming it with an empty
/// string, or with `clear_*`, removes it.
///
/// ```
/// use tiktok_shop_api::Shop;
/// let replace_both = Shop::new().access_token("token-2").shop_cipher("cipher-2");
/// let keep_token_clear_cipher = Shop::new().clear_shop_cipher();
/// # let _ = (replace_both, keep_token_clear_cipher);
/// ```
#[derive(Clone, Default)]
pub struct Shop {
    access_token: Change,
    shop_cipher: Change,
}

impl Shop {
    /// Changes nothing.
    pub fn new() -> Self {
        Self::default()
    }

    /// Use this access token. An empty one clears it.
    pub fn access_token(mut self, token: impl Into<String>) -> Self {
        self.access_token = Change::Set(token.into());
        self
    }

    /// Use this shop cipher. An empty one clears it.
    pub fn shop_cipher(mut self, cipher: impl Into<String>) -> Self {
        self.shop_cipher = Change::Set(cipher.into());
        self
    }

    /// Send no access token.
    pub fn clear_access_token(mut self) -> Self {
        self.access_token = Change::Clear;
        self
    }

    /// Send no shop cipher.
    pub fn clear_shop_cipher(mut self) -> Self {
        self.shop_cipher = Change::Clear;
        self
    }
}

impl fmt::Debug for Shop {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let show = |c: &Change| match c {
            Change::Keep => "Keep",
            Change::Set(_) => "Set([redacted])",
            Change::Clear => "Clear",
        };
        f.debug_struct("Shop")
            .field("access_token", &format_args!("{}", show(&self.access_token)))
            .field("shop_cipher", &format_args!("{}", show(&self.shop_cipher)))
            .finish()
    }
}

/// A client for the TikTok Shop API: one field per API group, e.g.
/// `client.orders.get_order_list(20, None, None, None, None).await`.
pub struct TikTokShop {
    pub affiliate_creator: AffiliateCreatorApi,
    pub affiliate_partner: AffiliatePartnerApi,
    pub affiliate_seller: AffiliateSellerApi,
    pub analytics: AnalyticsApi,
    pub authorization: AuthorizationApi,
    pub customer_engagement: CustomerEngagementApi,
    pub customer_service: CustomerServiceApi,
    pub event: EventApi,
    pub finance: FinanceApi,
    pub fulfilled_by_tiktok: FulfilledByTikTokApi,
    pub fulfillment: FulfillmentApi,
    pub logistics: LogisticsApi,
    pub orders: OrdersApi,
    pub products: ProductsApi,
    pub promotion: PromotionApi,
    pub return_and_refund: ReturnAndRefundApi,
    pub seller: SellerApi,
    pub supply_chain: SupplyChainApi,
    pub tools: ToolsApi,
    options: Options,
    http: reqwest::Client,
}

impl TikTokShop {
    /// Builds a client. Fails only if the HTTP client cannot be built (e.g. the TLS backend cannot start).
    pub fn new(mut options: Options) -> Result<Self, Error> {
        let http = match options.http_client.take() {
            Some(c) => c,
            None => {
                // No redirects: the access-token header must never follow one to another host.
                let mut b = reqwest::Client::builder().redirect(reqwest::redirect::Policy::none());
                if let Some(t) = options.timeout.filter(|t| !t.is_zero()) {
                    b = b.timeout(t);
                }
                b.build().map_err(Error::from_reqwest)?
            }
        };
        Ok(Self::with_http(options, http))
    }

    fn with_http(options: Options, http: reqwest::Client) -> Self {
        let middleware = SigningMiddleware::new(
            options.app_key.clone(),
            options.app_secret.clone(),
            options.access_token.clone(),
            options.shop_cipher.clone(),
        );
        let client = ClientBuilder::new(http.clone()).with(middleware).build();
        let base = options.base_url.as_deref().unwrap_or(DEFAULT_BASE_URL).trim_end_matches('/').to_owned();
        let mut config = Configuration::new();
        config.base_path = base;
        config.user_agent = Some(USER_AGENT.to_owned());
        config.client = client;
        let c = Arc::new(config);
        Self {
            affiliate_creator: AffiliateCreatorApi::new(c.clone()),
            affiliate_partner: AffiliatePartnerApi::new(c.clone()),
            affiliate_seller: AffiliateSellerApi::new(c.clone()),
            analytics: AnalyticsApi::new(c.clone()),
            authorization: AuthorizationApi::new(c.clone()),
            customer_engagement: CustomerEngagementApi::new(c.clone()),
            customer_service: CustomerServiceApi::new(c.clone()),
            event: EventApi::new(c.clone()),
            finance: FinanceApi::new(c.clone()),
            fulfilled_by_tiktok: FulfilledByTikTokApi::new(c.clone()),
            fulfillment: FulfillmentApi::new(c.clone()),
            logistics: LogisticsApi::new(c.clone()),
            orders: OrdersApi::new(c.clone()),
            products: ProductsApi::new(c.clone()),
            promotion: PromotionApi::new(c.clone()),
            return_and_refund: ReturnAndRefundApi::new(c.clone()),
            seller: SellerApi::new(c.clone()),
            supply_chain: SupplyChainApi::new(c.clone()),
            tools: ToolsApi::new(c),
            options: Options { http_client: None, ..options },
            http,
        }
    }

    /// A client for another shop or token that shares this client's HTTP client, base URL and timeout.
    /// What `shop` does not name keeps this client's value; naming it empty (or `clear_*`) removes it. The
    /// original client is not changed.
    pub fn with_shop(&self, shop: Shop) -> TikTokShop {
        let mut o = self.options.clone();
        o.access_token = shop.access_token.apply(&self.options.access_token);
        o.shop_cipher = shop.shop_cipher.apply(&self.options.shop_cipher);
        Self::with_http(o, self.http.clone())
    }
}

impl fmt::Debug for TikTokShop {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("TikTokShop").field("options", &self.options).finish_non_exhaustive()
    }
}
