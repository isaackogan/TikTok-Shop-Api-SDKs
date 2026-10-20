package tiktokshop

import (
	"fmt"
	"net/http"
	"strings"
	"time"

	"github.com/isaackogan/TikTok-Shop-Api-SDKs/go/generated"
)

const (
	// DefaultBaseURL is the TikTok Shop API's address.
	DefaultBaseURL = "https://open-api.tiktokglobalshop.com"
	// DefaultTimeout bounds one request, response body included.
	DefaultTimeout = 30 * time.Second
)

// Options configure [New].
type Options struct {
	AppKey    string
	AppSecret string
	// AccessToken is sent as the x-tts-access-token header. Empty sends none.
	AccessToken string
	// ShopCipher is added to the operations that take one. Empty adds none.
	ShopCipher string
	// BaseURL overrides DefaultBaseURL, e.g. for a test server.
	BaseURL string
	// Timeout bounds one request, response body included. 0 means DefaultTimeout; negative means none.
	Timeout time.Duration
	// Transport carries the signed requests. nil means http.DefaultTransport, which honours the proxy
	// environment variables. [TikTokShop.WithShop] shares it. The client the SDK builds around it never
	// follows a redirect: a 3xx reply is returned as an [*Error] carrying the status, so the access token
	// is never forwarded to another host. A Transport you supply is used as it is.
	Transport http.RoundTripper
}

// String describes the options without the app secret, the access token or the shop cipher.
func (o Options) String() string {
	return fmt.Sprintf("Options{AppKey:%s AppSecret:%s AccessToken:%s ShopCipher:%s BaseURL:%s Timeout:%s Transport:%t}",
		o.AppKey, redact(o.AppSecret), redact(o.AccessToken), redact(o.ShopCipher), o.BaseURL, o.Timeout, o.Transport != nil)
}

// GoString is String, so %#v does not print the secrets either.
func (o Options) GoString() string { return o.String() }

// redact masks a secret, keeping only whether it is set.
func redact(secret string) string {
	if secret == "" {
		return "<empty>"
	}
	return "***"
}

// ShopOption selects what [TikTokShop.WithShop] changes. See [ShopAccessToken] and [ShopCipher].
type ShopOption func(*Options)

// ShopAccessToken sets the access token of the client WithShop returns. An empty token clears it.
func ShopAccessToken(token string) ShopOption { return func(o *Options) { o.AccessToken = token } }

// ShopCipher sets the shop cipher of the client WithShop returns. An empty cipher clears it.
func ShopCipher(cipher string) ShopOption { return func(o *Options) { o.ShopCipher = cipher } }

// TikTokShop is a client for the TikTok Shop API: one field per API group, each the concrete generated
// service, e.g. client.Orders.GetOrderList(ctx).PageSize(20).Execute().
type TikTokShop struct {
	AffiliateCreator   *generated.AffiliateCreatorAPIService
	AffiliatePartner   *generated.AffiliatePartnerAPIService
	AffiliateSeller    *generated.AffiliateSellerAPIService
	Analytics          *generated.AnalyticsAPIService
	Authorization      *generated.AuthorizationAPIService
	CustomerEngagement *generated.CustomerEngagementAPIService
	CustomerService    *generated.CustomerServiceAPIService
	Event              *generated.EventAPIService
	Finance            *generated.FinanceAPIService
	FulfilledByTikTok  *generated.FulfilledByTikTokFBTAPIService
	Fulfillment        *generated.FulfillmentAPIService
	Logistics          *generated.LogisticsAPIService
	Orders             *generated.OrdersAPIService
	Products           *generated.ProductsAPIService
	Promotion          *generated.PromotionAPIService
	ReturnAndRefund    *generated.ReturnAndRefundAPIService
	Seller             *generated.SellerAPIService
	SupplyChain        *generated.SupplyChainAPIService
	Tools              *generated.ToolsAPIService

	opts Options
}

// String describes the client without its secrets.
func (c TikTokShop) String() string { return "TikTokShop{" + c.opts.String() + "}" }

// GoString is String, so %#v does not print the secrets either.
func (c TikTokShop) GoString() string { return c.String() }

// New returns a client. It never fails and does no I/O.
func New(o Options) *TikTokShop {
	if o.BaseURL == "" {
		o.BaseURL = DefaultBaseURL
	}
	o.BaseURL = strings.TrimRight(o.BaseURL, "/")
	if o.Timeout == 0 {
		o.Timeout = DefaultTimeout
	} else if o.Timeout < 0 {
		o.Timeout = 0
	}
	t := &signingTransport{
		creds:   credentials{o.AppKey, o.AppSecret, o.AccessToken, o.ShopCipher},
		inner:   o.Transport,
		timeout: o.Timeout,
	}
	cfg := generated.NewConfiguration()
	cfg.Servers = generated.ServerConfigurations{{URL: o.BaseURL}}
	cfg.UserAgent = "tiktok-shop-api-go/0.1.0"
	// No http.Client.Timeout: net/http would replace our *Error with its own string error. The
	// transport applies the timeout itself.
	cfg.HTTPClient = &http.Client{Transport: t, CheckRedirect: noRedirect}
	api := generated.NewAPIClient(cfg)
	return &TikTokShop{
		AffiliateCreator:   api.AffiliateCreatorAPI,
		AffiliatePartner:   api.AffiliatePartnerAPI,
		AffiliateSeller:    api.AffiliateSellerAPI,
		Analytics:          api.AnalyticsAPI,
		Authorization:      api.AuthorizationAPI,
		CustomerEngagement: api.CustomerEngagementAPI,
		CustomerService:    api.CustomerServiceAPI,
		Event:              api.EventAPI,
		Finance:            api.FinanceAPI,
		FulfilledByTikTok:  api.FulfilledByTikTokFBTAPI,
		Fulfillment:        api.FulfillmentAPI,
		Logistics:          api.LogisticsAPI,
		Orders:             api.OrdersAPI,
		Products:           api.ProductsAPI,
		Promotion:          api.PromotionAPI,
		ReturnAndRefund:    api.ReturnAndRefundAPI,
		Seller:             api.SellerAPI,
		SupplyChain:        api.SupplyChainAPI,
		Tools:              api.ToolsAPI,
		opts:               o,
	}
}

// WithShop returns a client for another shop or token that shares this client's transport, base URL
// and timeout. A value you do not pass keeps this client's value; passing it empty clears it:
//
//	other := c.WithShop(tiktokshop.ShopAccessToken("t2"), tiktokshop.ShopCipher("c2"))
//	keepsCipher := c.WithShop(tiktokshop.ShopAccessToken("t2"))
//	noCipher := c.WithShop(tiktokshop.ShopCipher(""))
//
// The receiver is not changed.
func (c *TikTokShop) WithShop(opts ...ShopOption) *TikTokShop {
	o := c.opts
	for _, f := range opts {
		f(&o)
	}
	if o.Timeout == 0 {
		o.Timeout = -1 // already resolved: 0 here means none
	}
	return New(o)
}

// noRedirect makes an http.Client hand back a 3xx reply instead of following it.
func noRedirect(*http.Request, []*http.Request) error { return http.ErrUseLastResponse }
