package tiktokshop

import (
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"net/http"
	"net/http/httptest"
	"strings"
	"sync/atomic"
	"testing"
)

// redirectTarget counts the requests a redirect would have forwarded the access token to.
func redirectTarget(t *testing.T) (*httptest.Server, *atomic.Int32) {
	t.Helper()
	var n atomic.Int32
	srv := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		n.Add(1)
		w.Header().Set("Content-Type", "application/json")
		_, _ = w.Write([]byte(okBody))
	}))
	t.Cleanup(srv.Close)
	return srv, &n
}

func redirector(t *testing.T, to string) *httptest.Server {
	t.Helper()
	srv := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		http.Redirect(w, r, to+"/stolen", http.StatusFound)
	}))
	t.Cleanup(srv.Close)
	return srv
}

func TestAPIRedirectIsNotFollowedAndSurfacesAsTheStatus(t *testing.T) {
	target, hits := redirectTarget(t)
	src := redirector(t, target.URL)
	c := New(Options{AppKey: "k", AppSecret: "s", AccessToken: "tok", BaseURL: src.URL})
	_, _, err := c.Authorization.GetAuthorizedShops(context.Background()).Execute()
	var e *Error
	if !errors.As(err, &e) {
		t.Fatalf("errors.As failed: %T %v", err, err)
	}
	if e.Code != 302 || e.HTTPStatus != 302 {
		t.Errorf("code %d status %d, want 302/302", e.Code, e.HTTPStatus)
	}
	if hits.Load() != 0 {
		t.Errorf("the redirect target got %d request(s)", hits.Load())
	}
}

func TestTokenRedirectIsNotFollowedAndSurfacesAsTheStatus(t *testing.T) {
	target, hits := redirectTarget(t)
	src := redirector(t, target.URL)
	_, err := NewAuth(AuthOptions{AppKey: "k", AppSecret: "s", BaseURL: src.URL}).ExchangeCode(context.Background(), "c")
	var e *Error
	if !errors.As(err, &e) {
		t.Fatalf("errors.As failed: %T %v", err, err)
	}
	if e.Code != 302 || e.HTTPStatus != 302 {
		t.Errorf("code %d status %d, want 302/302", e.Code, e.HTTPStatus)
	}
	if hits.Load() != 0 {
		t.Errorf("the redirect target got %d request(s)", hits.Load())
	}
}

func TestNon2xxWithNoCodeOrCodeZeroUsesTheHTTPStatus(t *testing.T) {
	for _, body := range []string{`{"message":"x"}`, `{"code":0}`} {
		s := newStub(t)
		s.status, s.body = 503, body
		_, _, err := s.client().Authorization.GetAuthorizedShops(context.Background()).Execute()
		var e *Error
		if !errors.As(err, &e) || e.Code != 503 || e.HTTPStatus != 503 {
			t.Errorf("api %s: %+v", body, e)
		}
		srv, _ := authStub(t, 503, body)
		_, err = NewAuth(AuthOptions{AppKey: "k", AppSecret: "s", BaseURL: srv.URL}).Refresh(context.Background(), "r")
		if !errors.As(err, &e) || e.Code != 503 || e.HTTPStatus != 503 {
			t.Errorf("token %s: %+v", body, e)
		}
	}
}

const (
	secretValue  = "super-secret-value"
	tokenValue   = "tok-value-xyz"
	cipherValue  = "cipher-value-xyz"
	refreshValue = "refresh-value-xyz"
)

func assertNoSecrets(t *testing.T, what string, v any, visible ...string) {
	t.Helper()
	for _, verb := range []string{"%v", "%+v", "%s", "%#v"} {
		out := fmt.Sprintf(verb, v)
		for _, s := range []string{secretValue, tokenValue, cipherValue, refreshValue} {
			if strings.Contains(out, s) {
				t.Errorf("%s %s leaked %q: %s", what, verb, s, out)
			}
		}
		for _, w := range visible {
			if verb != "%#v" && !strings.Contains(out, w) {
				t.Errorf("%s %s should show %q: %s", what, verb, w, out)
			}
		}
	}
}

func TestStringFormsNeverPrintSecrets(t *testing.T) {
	opts := Options{AppKey: "appkey1", AppSecret: secretValue, AccessToken: tokenValue, ShopCipher: cipherValue}
	assertNoSecrets(t, "Options", opts, "appkey1")
	assertNoSecrets(t, "*Options", &opts, "appkey1")
	c := New(opts)
	assertNoSecrets(t, "*TikTokShop", c, "appkey1")
	assertNoSecrets(t, "TikTokShop", *c, "appkey1")
	assertNoSecrets(t, "WithShop", c.WithShop(ShopAccessToken(tokenValue)), "appkey1")

	ao := AuthOptions{AppKey: "appkey1", AppSecret: secretValue}
	assertNoSecrets(t, "AuthOptions", ao, "appkey1")
	assertNoSecrets(t, "*Auth", NewAuth(ao), "appkey1")

	ts := TokenSet{AccessToken: tokenValue, RefreshToken: refreshValue, OpenID: "open1", SellerName: "shop"}
	assertNoSecrets(t, "TokenSet", ts, "open1")
	assertNoSecrets(t, "*TokenSet", &ts, "open1")
}

func TestTokenSetJSONIsUnchanged(t *testing.T) {
	ts := TokenSet{AccessToken: tokenValue, AccessTokenExpireIn: 1, RefreshToken: refreshValue, RefreshTokenExpireIn: 2, OpenID: "o"}
	b, err := json.Marshal(ts)
	if err != nil {
		t.Fatal(err)
	}
	if !strings.Contains(string(b), tokenValue) || !strings.Contains(string(b), refreshValue) {
		t.Errorf("json.Marshal must keep the tokens so users can store them: %s", b)
	}
	var back TokenSet
	if err := json.Unmarshal(b, &back); err != nil || back.AccessToken != tokenValue || back.RefreshToken != refreshValue {
		t.Errorf("round trip: %v %+v", err, back)
	}
}

// R13b: a non-2xx has TikTok's non-zero code if the body has one, else the HTTP status; -1 only for an unreadable 2xx.
var r13b = []struct {
	status int
	body   string
	want   int
}{
	{503, `{"message":"x"}`, 503},
	{503, `{"code":0}`, 503},
	{503, `down`, 503},
	{503, ``, 503},
	{503, `[1]`, 503},
	{302, ``, 302},
	{503, `{"code":12345,"message":"m"}`, 12345},
	{200, `<html>`, -1},
	{200, `[1]`, -1},
}

func TestR13bAPIAndTokenCodes(t *testing.T) {
	for _, c := range r13b {
		s := newStub(t)
		s.status, s.body = c.status, c.body
		// A 302 from the stub carries no Location, so nothing follows either way.
		_, _, err := s.client().Authorization.GetAuthorizedShops(context.Background()).Execute()
		var e *Error
		if !errors.As(err, &e) || e.Code != c.want || e.HTTPStatus != c.status {
			t.Errorf("api %d %q: %+v", c.status, c.body, e)
		}
		srv, _ := authStub(t, c.status, c.body)
		for _, refresh := range []bool{false, true} {
			a := NewAuth(AuthOptions{AppKey: "k", AppSecret: "s", BaseURL: srv.URL})
			if refresh {
				_, err = a.Refresh(context.Background(), "r")
			} else {
				_, err = a.ExchangeCode(context.Background(), "c")
			}
			e = nil
			if !errors.As(err, &e) || e.Code != c.want || e.HTTPStatus != c.status {
				t.Errorf("token %d %q: %+v", c.status, c.body, e)
			}
		}
	}
	srv, _ := authStub(t, 200, `{"code":0,"request_id":"r"}`)
	_, err := NewAuth(AuthOptions{AppKey: "k", AppSecret: "s", BaseURL: srv.URL}).Refresh(context.Background(), "r")
	var e *Error
	if !errors.As(err, &e) || e.Code != -1 {
		t.Errorf("code 0 without data: %+v", e)
	}
}

// The SDK-built http.Client itself refuses to follow a redirect. The signing transport would error on a 3xx first, so
// this drives the clients through a transport that passes the 302 straight back, which only CheckRedirect can stop.
func TestSDKBuiltClientsRefuseRedirectsThemselves(t *testing.T) {
	target, hits := redirectTarget(t)
	passthrough := roundTripFunc(func(r *http.Request) (*http.Response, error) {
		if strings.HasPrefix(target.URL, "http://"+r.URL.Host) {
			hits.Add(1)
			return &http.Response{StatusCode: 200, Header: http.Header{}, Body: http.NoBody, Request: r}, nil
		}
		h := http.Header{}
		h.Set("Location", target.URL+"/stolen")
		return &http.Response{StatusCode: 302, Header: h, Body: http.NoBody, Request: r}, nil
	})
	for name, client := range map[string]*http.Client{
		"API client":  newHTTPClient(passthrough),
		"auth client": NewAuth(AuthOptions{Transport: passthrough}).client,
	} {
		req, _ := http.NewRequest(http.MethodGet, "http://origin.example/x", nil)
		res, err := client.Do(req)
		if err != nil || res.StatusCode != http.StatusFound {
			t.Errorf("%s: status %v err %v, want the 302 handed back", name, res, err)
		}
	}
	if hits.Load() != 0 {
		t.Errorf("the redirect target got %d request(s)", hits.Load())
	}
}

type roundTripFunc func(*http.Request) (*http.Response, error)

func (f roundTripFunc) RoundTrip(r *http.Request) (*http.Response, error) { return f(r) }
