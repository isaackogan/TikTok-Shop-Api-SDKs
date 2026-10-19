package tiktokshop

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"strings"
	"time"
)

// DefaultAuthBaseURL is the host of the token endpoints.
const DefaultAuthBaseURL = "https://auth.tiktok-shops.com"

// AuthType selects whose authorization page [Auth.AuthorizationURL] points at.
type AuthType string

// Region selects the US or the rest-of-world TikTok Shop host.
type Region string

const (
	// AuthSeller authorizes your app for a seller. Needs a service ID.
	AuthSeller AuthType = "seller"
	// AuthPartner authorizes your app for a partner. Needs a service ID.
	AuthPartner AuthType = "partner"
	// AuthCreator authorizes your app for an affiliate creator.
	AuthCreator AuthType = "creator"

	// RegionUS is the United States host.
	RegionUS Region = "us"
	// RegionROW is the rest-of-world host.
	RegionROW Region = "row"
)

var authHosts = map[AuthType]struct {
	us, row, path string
}{
	AuthSeller:  {"https://services.us.tiktokshop.com", "https://services.tiktokshop.com", "/open/authorize"},
	AuthPartner: {"https://partner.us.tiktokshop.com", "https://partner.tiktokshop.com", "/open/authorize"},
	AuthCreator: {"https://shop.tiktok.com", "https://shop.tiktok.com", "/alliance/creator/auth"},
}

// AuthOptions configure [NewAuth].
type AuthOptions struct {
	AppKey    string
	AppSecret string
	// ServiceID is your Partner Center service ID. Needed for AuthSeller and AuthPartner URLs.
	ServiceID string
	// BaseURL overrides DefaultAuthBaseURL, e.g. for a test server.
	BaseURL string
	// Timeout bounds one token request. 0 means DefaultTimeout; negative means none.
	Timeout time.Duration
	// Transport carries the requests. nil means http.DefaultTransport.
	Transport http.RoundTripper
}

// AuthorizationURLOptions select the page [Auth.AuthorizationURL] builds.
type AuthorizationURLOptions struct {
	Type   AuthType
	Region Region
	// State is echoed back to your redirect URL. Empty adds no state parameter.
	State string
}

// TokenSet is the result of exchanging a code or refreshing a token.
type TokenSet struct {
	AccessToken string
	// AccessTokenExpireIn is the Unix time (seconds) at which the access token expires.
	AccessTokenExpireIn int64
	RefreshToken        string
	// RefreshTokenExpireIn is the Unix time (seconds) at which the refresh token expires.
	RefreshTokenExpireIn int64
	OpenID               string
	SellerName           string
	SellerBaseRegion     string
	UserType             int
	GrantedScopes        []string
}

// Auth is the OAuth helper: authorization URLs, code exchange and token refresh.
type Auth struct {
	opts   AuthOptions
	client *http.Client
}

// NewAuth returns an OAuth helper. It never fails and does no I/O.
func NewAuth(o AuthOptions) *Auth {
	if o.BaseURL == "" {
		o.BaseURL = DefaultAuthBaseURL
	}
	o.BaseURL = strings.TrimRight(o.BaseURL, "/")
	timeout := o.Timeout
	if timeout == 0 {
		timeout = DefaultTimeout
	} else if timeout < 0 {
		timeout = 0
	}
	return &Auth{opts: o, client: &http.Client{Transport: o.Transport, Timeout: timeout}}
}

// enc is RFC 3986 percent-encoding: only unreserved characters stay, a space becomes %20.
func enc(s string) string { return strings.ReplaceAll(url.QueryEscape(s), "+", "%20") }

// AuthorizationURL returns the page to send the seller (or partner, or creator) to.
func (a *Auth) AuthorizationURL(o AuthorizationURLOptions) (string, error) {
	h, ok := authHosts[o.Type]
	if !ok {
		return "", fmt.Errorf("tiktokshop: unknown authorization type %q", o.Type)
	}
	var host string
	switch o.Region {
	case RegionUS:
		host = h.us
	case RegionROW:
		host = h.row
	default:
		return "", fmt.Errorf("tiktokshop: unknown region %q", o.Region)
	}
	var first string
	if o.Type == AuthCreator {
		first = "app_key=" + enc(a.opts.AppKey)
	} else {
		if a.opts.ServiceID == "" {
			return "", fmt.Errorf("tiktokshop: ServiceID is required for %s authorization URLs", o.Type)
		}
		first = "service_id=" + enc(a.opts.ServiceID)
	}
	u := host + h.path + "?" + first
	if o.State != "" {
		u += "&state=" + enc(o.State)
	}
	return u, nil
}

// ExchangeCode trades the auth_code from your redirect URL for tokens.
func (a *Auth) ExchangeCode(ctx context.Context, code string) (*TokenSet, error) {
	return a.token(ctx, "get", [][2]string{{"auth_code", code}, {"grant_type", "authorized_code"}})
}

// Refresh trades a refresh token for new tokens.
func (a *Auth) Refresh(ctx context.Context, refreshToken string) (*TokenSet, error) {
	return a.token(ctx, "refresh", [][2]string{{"refresh_token", refreshToken}, {"grant_type", "refresh_token"}})
}

func (a *Auth) token(ctx context.Context, endpoint string, extra [][2]string) (*TokenSet, error) {
	params := append([][2]string{{"app_key", a.opts.AppKey}, {"app_secret", a.opts.AppSecret}}, extra...)
	parts := make([]string, len(params))
	for i, p := range params {
		parts[i] = p[0] + "=" + enc(p[1])
	}
	req, err := http.NewRequestWithContext(ctx, http.MethodGet, a.opts.BaseURL+"/api/v2/token/"+endpoint+"?"+strings.Join(parts, "&"), nil)
	if err != nil {
		return nil, &Error{Message: "invalid token request: " + err.Error(), Cause: err}
	}
	res, err := a.client.Do(req)
	var body []byte
	if err == nil {
		body, err = io.ReadAll(res.Body)
		res.Body.Close()
	}
	if err != nil {
		return nil, &Error{Message: "token request failed: " + err.Error(), Cause: err}
	}
	return toTokenSet(res.StatusCode, body)
}

func toTokenSet(status int, body []byte) (*TokenSet, error) {
	ok := status >= 200 && status < 300
	var env map[string]json.RawMessage
	if err := json.Unmarshal(body, &env); err != nil || env == nil {
		if err == nil {
			err = fmt.Errorf("body is not a JSON object")
		}
		return nil, &Error{Code: -1, Message: fmt.Sprintf("unparseable token response (HTTP %d)", status), HTTPStatus: status, Cause: err}
	}
	var requestID, message string
	_ = json.Unmarshal(env["request_id"], &requestID)
	_ = json.Unmarshal(env["message"], &message)
	var code int
	if err := json.Unmarshal(env["code"], &code); err != nil {
		code = -1
		if !ok {
			code = status
		}
	}
	if code != 0 || !ok {
		if code == 0 {
			code = status
		}
		if message == "" {
			message = fmt.Sprintf("HTTP %d", status)
		}
		return nil, &Error{Code: code, Message: message, RequestID: requestID, HTTPStatus: status}
	}
	fail := func(msg string, cause error) (*TokenSet, error) {
		return nil, &Error{Code: -1, Message: msg, RequestID: requestID, HTTPStatus: status, Cause: cause}
	}
	var d struct {
		AccessToken          *string         `json:"access_token"`
		AccessTokenExpireIn  *int64          `json:"access_token_expire_in"`
		RefreshToken         *string         `json:"refresh_token"`
		RefreshTokenExpireIn *int64          `json:"refresh_token_expire_in"`
		OpenID               json.RawMessage `json:"open_id"`
		SellerName           *string         `json:"seller_name"`
		SellerBaseRegion     *string         `json:"seller_base_region"`
		UserType             *int            `json:"user_type"`
		GrantedScopes        []string        `json:"granted_scopes"`
	}
	if raw := bytes.TrimSpace(env["data"]); len(raw) == 0 || raw[0] != '{' {
		return fail("token response has no data", nil)
	}
	if err := json.Unmarshal(env["data"], &d); err != nil {
		return fail("token response data is malformed: "+err.Error(), err)
	}
	// open_id is an ID: keep its digits whether TikTok sends a string or a number.
	var openID string
	if err := json.Unmarshal(d.OpenID, &openID); err != nil {
		var n json.Number
		dec := json.NewDecoder(bytes.NewReader(d.OpenID))
		dec.UseNumber()
		if dec.Decode(&n) != nil || n == "" {
			return fail("token response is missing open_id", nil)
		}
		openID = n.String()
	}
	if d.AccessToken == nil || d.AccessTokenExpireIn == nil || d.RefreshToken == nil || d.RefreshTokenExpireIn == nil ||
		d.SellerName == nil || d.SellerBaseRegion == nil || d.UserType == nil {
		return fail("token response is missing fields", nil)
	}
	return &TokenSet{
		AccessToken:          *d.AccessToken,
		AccessTokenExpireIn:  *d.AccessTokenExpireIn,
		RefreshToken:         *d.RefreshToken,
		RefreshTokenExpireIn: *d.RefreshTokenExpireIn,
		OpenID:               openID,
		SellerName:           *d.SellerName,
		SellerBaseRegion:     *d.SellerBaseRegion,
		UserType:             *d.UserType,
		GrantedScopes:        d.GrantedScopes,
	}, nil
}
