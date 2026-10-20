package tiktokshop

import (
	"bytes"
	"context"
	"encoding/json"
	"errors"
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
	// Transport carries the requests. nil means http.DefaultTransport. The client the SDK builds around it never
	// follows a redirect (a 3xx reply is returned as an [*Error] carrying the status), so the app secret and the
	// code are never forwarded to another host. A Transport you supply is used as it is.
	Transport http.RoundTripper
}

// String describes the options without the app secret.
func (o AuthOptions) String() string {
	return fmt.Sprintf("AuthOptions{AppKey:%s AppSecret:%s ServiceID:%s BaseURL:%s Timeout:%s Transport:%t}",
		o.AppKey, redact(o.AppSecret), o.ServiceID, o.BaseURL, o.Timeout, o.Transport != nil)
}

// GoString is String, so %#v does not print the secret either.
func (o AuthOptions) GoString() string { return o.String() }

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

// String describes the set without its tokens. json.Marshal is unchanged, so a set can still be stored.
func (t TokenSet) String() string {
	return fmt.Sprintf("TokenSet{AccessToken:*** RefreshToken:*** OpenID:%s SellerName:%s SellerBaseRegion:%s UserType:%d GrantedScopes:%v}",
		t.OpenID, t.SellerName, t.SellerBaseRegion, t.UserType, t.GrantedScopes)
}

// GoString is String, so %#v does not print the tokens either.
func (t TokenSet) GoString() string { return t.String() }

// Auth is the OAuth helper: authorization URLs, code exchange and token refresh.
type Auth struct {
	opts   AuthOptions
	client *http.Client
}

// String describes the helper without the app secret.
func (a Auth) String() string { return "Auth{" + a.opts.String() + "}" }

// GoString is String, so %#v does not print the secret either.
func (a Auth) GoString() string { return a.String() }

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
	return &Auth{opts: o, client: &http.Client{Transport: o.Transport, Timeout: timeout, CheckRedirect: noRedirect}}
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
		err = withoutURL(err)
		return nil, &Error{Code: -1, Message: "invalid token request: " + err.Error(), Cause: err}
	}
	req.Header.Set("User-Agent", userAgent)
	res, err := a.client.Do(req)
	var body []byte
	status := 0
	if err == nil {
		status = res.StatusCode
		body, err = io.ReadAll(res.Body)
		res.Body.Close()
	}
	if err != nil {
		// R13c: -1, with no HTTPStatus when no response arrived. net/http's *url.Error carries the full URL, whose
		// query holds the app secret and the code or refresh token, so neither the message nor the cause may include it.
		err = withoutURL(err)
		return nil, &Error{Code: -1, Message: "token request to /api/v2/token/" + endpoint + " failed: " + err.Error(), HTTPStatus: status, Cause: err}
	}
	return toTokenSet(res.StatusCode, body)
}

// withoutURL returns the error inside a *url.Error, which has no URL.
func withoutURL(err error) error {
	var ue *url.Error
	if errors.As(err, &ue) && ue.Err != nil {
		return ue.Err
	}
	return err
}

func toTokenSet(status int, body []byte) (*TokenSet, error) {
	ok := status >= 200 && status < 300
	var env map[string]json.RawMessage
	if err := json.Unmarshal(body, &env); err != nil || env == nil {
		if err == nil {
			err = fmt.Errorf("body is not a JSON object")
		}
		// R13b: a non-2xx reply (a redirect included, since it is never followed) has the HTTP status as its code
		// whatever the body; only an unreadable 2xx is -1.
		code := -1
		if !ok {
			code = status
		}
		return nil, &Error{Code: code, Message: fmt.Sprintf("unparseable token response (HTTP %d)", status), HTTPStatus: status, Cause: err}
	}
	var requestID, message string
	_ = json.Unmarshal(env["request_id"], &requestID)
	_ = json.Unmarshal(env["message"], &message)
	// Lesson 34: a code that is missing or not an integer makes a 2xx unreadable (-1); on a non-2xx the status is the code.
	code, isInt := intCode(env["code"])
	if !isInt {
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
		SellerName           string          `json:"seller_name"`
		SellerBaseRegion     string          `json:"seller_base_region"`
		UserType             int             `json:"user_type"`
		GrantedScopes        []string        `json:"granted_scopes"`
	}
	if raw := bytes.TrimSpace(env["data"]); len(raw) == 0 || raw[0] != '{' {
		return fail("token response has no data", nil)
	}
	if err := json.Unmarshal(env["data"], &d); err != nil {
		return fail("token response data is malformed: "+err.Error(), err)
	}
	// open_id is an ID: keep its digits whether TikTok sends a string or a number.
	// It is optional: absent or null gives "".
	var openID string
	if raw := bytes.TrimSpace(d.OpenID); len(raw) > 0 && string(raw) != "null" {
		if err := json.Unmarshal(raw, &openID); err != nil {
			var n json.Number
			dec := json.NewDecoder(bytes.NewReader(raw))
			dec.UseNumber()
			if dec.Decode(&n) != nil || n == "" {
				return fail("token response has a malformed open_id", nil)
			}
			openID = n.String()
		}
	}
	// Creator and partner tokens may lack the seller fields, so only the token fields are required.
	if d.AccessToken == nil || d.AccessTokenExpireIn == nil || d.RefreshToken == nil || d.RefreshTokenExpireIn == nil {
		return fail("token response is missing token fields", nil)
	}
	if *d.AccessToken == "" || *d.RefreshToken == "" {
		return fail("token response has an empty access_token or refresh_token", nil)
	}
	return &TokenSet{
		AccessToken:          *d.AccessToken,
		AccessTokenExpireIn:  *d.AccessTokenExpireIn,
		RefreshToken:         *d.RefreshToken,
		RefreshTokenExpireIn: *d.RefreshTokenExpireIn,
		OpenID:               openID,
		SellerName:           d.SellerName,
		SellerBaseRegion:     d.SellerBaseRegion,
		UserType:             d.UserType,
		GrantedScopes:        d.GrantedScopes,
	}, nil
}
