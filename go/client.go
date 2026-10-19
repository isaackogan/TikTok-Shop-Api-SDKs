package tiktokshop

import (
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
	// environment variables. [TikTokShop.WithShop] shares it.
	Transport http.RoundTripper
}

// ShopOptions select another shop for [TikTokShop.WithShop]. An empty value means none.
type ShopOptions struct {
	AccessToken string
	ShopCipher  string
}

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
	cfg.HTTPClient = &http.Client{Transport: t}
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

// WithShop returns a client for another shop and token that shares this client's transport, base URL
// and timeout. The receiver is not changed.
func (c *TikTokShop) WithShop(s ShopOptions) *TikTokShop {
	o := c.opts
	o.AccessToken, o.ShopCipher = s.AccessToken, s.ShopCipher
	if o.Timeout == 0 {
		o.Timeout = -1 // already resolved: 0 here means none
	}
	return New(o)
}
