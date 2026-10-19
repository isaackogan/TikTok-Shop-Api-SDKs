package tiktokshop

import (
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"net"
	"net/http"
	"net/http/httptest"
	"os"
	"path/filepath"
	"strings"
	"sync"
	"testing"
	"time"
)

type authVectors struct {
	AuthorizationURLs []struct {
		Type      string  `json:"type"`
		Region    string  `json:"region"`
		ServiceID *string `json:"serviceId"`
		AppKey    *string `json:"appKey"`
		State     *string `json:"state"`
		URL       string  `json:"url"`
	} `json:"authorizationUrls"`
	TokenRequests []struct {
		Kind      string `json:"kind"`
		AppKey    string `json:"appKey"`
		AppSecret string `json:"appSecret"`
		Value     string `json:"value"`
		URL       string `json:"url"`
	} `json:"tokenRequests"`
	TokenResponses []struct {
		Name      string          `json:"name"`
		Body      string          `json:"body"`
		Expected  *TokenSet       `json:"-"`
		RawExp    json.RawMessage `json:"expected"`
		ErrorCode *int            `json:"errorCode"`
	} `json:"tokenResponses"`
}

func loadAuthVectors(t *testing.T) authVectors {
	t.Helper()
	b, err := os.ReadFile(filepath.Join("..", "shared", "test-vectors", "auth.json"))
	if err != nil {
		t.Fatal(err)
	}
	var v authVectors
	if err := json.Unmarshal(b, &v); err != nil {
		t.Fatal(err)
	}
	return v
}

func str(p *string) string {
	if p == nil {
		return ""
	}
	return *p
}

func TestAuthorizationURLVectors(t *testing.T) {
	for _, c := range loadAuthVectors(t).AuthorizationURLs {
		a := NewAuth(AuthOptions{AppKey: str(c.AppKey), AppSecret: "x", ServiceID: str(c.ServiceID)})
		got, err := a.AuthorizationURL(AuthorizationURLOptions{Type: AuthType(c.Type), Region: Region(c.Region), State: str(c.State)})
		if err != nil || got != c.URL {
			t.Errorf("%s/%s: got %q, %v; want %q", c.Type, c.Region, got, err, c.URL)
		}
	}
}

func TestAuthorizationURLRejectsBadInput(t *testing.T) {
	a := NewAuth(AuthOptions{AppKey: "k", AppSecret: "s"})
	if _, err := a.AuthorizationURL(AuthorizationURLOptions{Type: AuthSeller, Region: RegionUS}); err == nil {
		t.Error("seller URL without ServiceID must fail")
	}
	if _, err := a.AuthorizationURL(AuthorizationURLOptions{Type: "nope", Region: RegionUS}); err == nil {
		t.Error("unknown type must fail")
	}
	if _, err := a.AuthorizationURL(AuthorizationURLOptions{Type: AuthCreator, Region: "mars"}); err == nil {
		t.Error("unknown region must fail")
	}
}

func authStub(t *testing.T, status int, body string) (*httptest.Server, func() []*http.Request) {
	t.Helper()
	var mu sync.Mutex
	var got []*http.Request
	srv := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		mu.Lock()
		got = append(got, r)
		mu.Unlock()
		w.WriteHeader(status)
		_, _ = w.Write([]byte(body))
	}))
	t.Cleanup(srv.Close)
	return srv, func() []*http.Request {
		mu.Lock()
		defer mu.Unlock()
		return append([]*http.Request(nil), got...)
	}
}

func TestTokenRequestsMatchVectorsAndResponsesMap(t *testing.T) {
	v := loadAuthVectors(t)
	for _, req := range v.TokenRequests {
		srv, got := authStub(t, 200, v.TokenResponses[0].Body)
		a := NewAuth(AuthOptions{AppKey: req.AppKey, AppSecret: req.AppSecret, BaseURL: srv.URL})
		var ts *TokenSet
		var err error
		if req.Kind == "exchange" {
			ts, err = a.ExchangeCode(context.Background(), req.Value)
		} else {
			ts, err = a.Refresh(context.Background(), req.Value)
		}
		if err != nil {
			t.Fatal(err)
		}
		r := got()[0]
		if r.Method != "GET" {
			t.Errorf("%s: method %s", req.Kind, r.Method)
		}
		const prefix = "https://auth.tiktok-shops.com"
		if want := req.URL[len(prefix):]; r.URL.RequestURI() != want {
			t.Errorf("%s: got %s want %s", req.Kind, r.URL.RequestURI(), want)
		}
		if ts.AccessToken == "" {
			t.Error("empty token")
		}
	}
}

func TestTokenResponseVectors(t *testing.T) {
	for _, c := range loadAuthVectors(t).TokenResponses {
		srv, _ := authStub(t, 200, c.Body)
		a := NewAuth(AuthOptions{AppKey: "k", AppSecret: "s", BaseURL: srv.URL})
		ts, err := a.ExchangeCode(context.Background(), "c")
		if c.ErrorCode != nil {
			var e *Error
			if !errors.As(err, &e) || e.Code != *c.ErrorCode || e.RequestID != "r2" {
				t.Errorf("%s: err %v", c.Name, err)
			}
			continue
		}
		if err != nil {
			t.Fatalf("%s: %v", c.Name, err)
		}
		var want struct {
			AccessToken          string   `json:"accessToken"`
			AccessTokenExpireIn  int64    `json:"accessTokenExpireIn"`
			RefreshToken         string   `json:"refreshToken"`
			RefreshTokenExpireIn int64    `json:"refreshTokenExpireIn"`
			OpenID               string   `json:"openId"`
			SellerName           string   `json:"sellerName"`
			SellerBaseRegion     string   `json:"sellerBaseRegion"`
			UserType             int      `json:"userType"`
			GrantedScopes        []string `json:"grantedScopes"`
		}
		if err := json.Unmarshal(c.RawExp, &want); err != nil {
			t.Fatal(err)
		}
		got := *ts
		if got.AccessToken != want.AccessToken || got.AccessTokenExpireIn != want.AccessTokenExpireIn ||
			got.RefreshToken != want.RefreshToken || got.RefreshTokenExpireIn != want.RefreshTokenExpireIn ||
			got.OpenID != want.OpenID || got.SellerName != want.SellerName || got.SellerBaseRegion != want.SellerBaseRegion ||
			got.UserType != want.UserType || len(got.GrantedScopes) != len(want.GrantedScopes) || got.GrantedScopes[0] != want.GrantedScopes[0] {
			t.Errorf("got %+v want %+v", got, want)
		}
	}
}

func TestOpenIDNumberKeepsEveryDigit(t *testing.T) {
	body := `{"code":0,"request_id":"r","data":{"access_token":"a","access_token_expire_in":1,"refresh_token":"r","refresh_token_expire_in":2,"open_id":7494049642642441621,"seller_name":"n","seller_base_region":"US","user_type":0}}`
	srv, _ := authStub(t, 200, body)
	ts, err := NewAuth(AuthOptions{AppKey: "k", AppSecret: "s", BaseURL: srv.URL}).Refresh(context.Background(), "r")
	if err != nil || ts.OpenID != "7494049642642441621" || ts.GrantedScopes == nil && false {
		t.Fatalf("%+v %v", ts, err)
	}
}

func TestTokenResponseFailuresAreErrors(t *testing.T) {
	cases := map[string]struct {
		status int
		body   string
		code   int
	}{
		"code 0 without data":    {200, `{"code":0,"request_id":"r1"}`, -1},
		"code 0 data not object": {200, `{"code":0,"request_id":"r1","data":[]}`, -1},
		"code 0 data null":       {200, `{"code":0,"request_id":"r1","data":null}`, -1},
		"code 0 missing fields":  {200, `{"code":0,"request_id":"r1","data":{"access_token":"a","open_id":"1","seller_name":"n"}}`, -1},
		"not json":               {200, `<html>`, -1},
		"json not an object":     {200, `[1]`, -1},
		"500 with envelope":      {500, `{"code":1234,"message":"boom","request_id":"r9"}`, 1234},
		"500 with code 0":        {500, `{"code":0,"message":"weird","request_id":"r9","data":{}}`, 500},
		"503 without json":       {503, `down`, -1},
		"code != 0 on 200":       {200, `{"code":36004004,"message":"bad","request_id":"r2","data":{}}`, 36004004},
	}
	for name, c := range cases {
		srv, _ := authStub(t, c.status, c.body)
		ts, err := NewAuth(AuthOptions{AppKey: "k", AppSecret: "s", BaseURL: srv.URL}).ExchangeCode(context.Background(), "c")
		var e *Error
		if ts != nil || !errors.As(err, &e) {
			t.Errorf("%s: ts=%v err=%v", name, ts, err)
			continue
		}
		if e.HTTPStatus != c.status || e.Code != c.code {
			t.Errorf("%s: code %d http %d, want %d %d", name, e.Code, e.HTTPStatus, c.code, c.status)
		}
	}
}

func TestTokenNetworkErrorsAreErrors(t *testing.T) {
	l, _ := net.Listen("tcp", "127.0.0.1:0")
	addr := l.Addr().String()
	l.Close() // closed port
	_, err := NewAuth(AuthOptions{AppKey: "k", AppSecret: "s", BaseURL: "http://" + addr}).Refresh(context.Background(), "r")
	var e *Error
	if !errors.As(err, &e) || e.Cause == nil {
		t.Errorf("closed port: %v", err)
	}

	hang := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) { <-r.Context().Done() }))
	defer hang.Close()
	start := time.Now()
	_, err = NewAuth(AuthOptions{AppKey: "k", AppSecret: "s", BaseURL: hang.URL, Timeout: 100 * time.Millisecond}).Refresh(context.Background(), "r")
	if !errors.As(err, &e) || e.Cause == nil || time.Since(start) > 5*time.Second {
		t.Errorf("timeout: %v", err)
	}

	ctx, cancel := context.WithCancel(context.Background())
	cancel()
	_, err = NewAuth(AuthOptions{AppKey: "k", AppSecret: "s", BaseURL: hang.URL}).Refresh(ctx, "r")
	if !errors.As(err, &e) || !errors.Is(err, context.Canceled) {
		t.Errorf("canceled: %v", err)
	}
}

func TestMinimalTokenResponseSucceeds(t *testing.T) {
	body := `{"code":0,"request_id":"r","data":{"access_token":"a","access_token_expire_in":1,"refresh_token":"r","refresh_token_expire_in":2}}`
	srv, _ := authStub(t, 200, body)
	ts, err := NewAuth(AuthOptions{AppKey: "k", AppSecret: "s", BaseURL: srv.URL}).ExchangeCode(context.Background(), "c")
	if err != nil || ts.AccessToken != "a" || ts.RefreshTokenExpireIn != 2 || ts.OpenID != "" || ts.SellerName != "" || ts.UserType != 0 || len(ts.GrantedScopes) != 0 {
		t.Fatalf("%+v %v", ts, err)
	}
}

func TestTokenErrorsNeverContainCredentials(t *testing.T) {
	const secret, code, refresh = "SECRET-VALUE-9", "AUTHCODE-VALUE-7", "REFRESHTOKEN-VALUE-5"
	l, _ := net.Listen("tcp", "127.0.0.1:0")
	closed := "http://" + l.Addr().String()
	l.Close()
	hang := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) { <-r.Context().Done() }))
	defer hang.Close()
	bad, _ := authStub(t, 500, `{"code":1,"message":"boom","request_id":"r"}`)
	html, _ := authStub(t, 200, `<html>`)
	ctx, cancel := context.WithCancel(context.Background())
	cancel()

	cases := map[string]func() error{
		"closed port": func() error {
			_, err := NewAuth(AuthOptions{AppKey: "k", AppSecret: secret, BaseURL: closed}).ExchangeCode(context.Background(), code)
			return err
		},
		"timeout": func() error {
			_, err := NewAuth(AuthOptions{AppKey: "k", AppSecret: secret, BaseURL: hang.URL, Timeout: 100 * time.Millisecond}).Refresh(context.Background(), refresh)
			return err
		},
		"canceled": func() error {
			_, err := NewAuth(AuthOptions{AppKey: "k", AppSecret: secret, BaseURL: hang.URL}).ExchangeCode(ctx, code)
			return err
		},
		"500": func() error {
			_, err := NewAuth(AuthOptions{AppKey: "k", AppSecret: secret, BaseURL: bad.URL}).Refresh(context.Background(), refresh)
			return err
		},
		"not json": func() error {
			_, err := NewAuth(AuthOptions{AppKey: "k", AppSecret: secret, BaseURL: html.URL}).ExchangeCode(context.Background(), code)
			return err
		},
		"bad base url": func() error {
			_, err := NewAuth(AuthOptions{AppKey: "k", AppSecret: secret, BaseURL: "http://bad host"}).ExchangeCode(context.Background(), code)
			return err
		},
	}
	for name, run := range cases {
		err := run()
		if err == nil {
			t.Errorf("%s: no error", name)
			continue
		}
		var e *Error
		if !errors.As(err, &e) {
			t.Errorf("%s: %T", name, err)
			continue
		}
		texts := []string{e.Error(), fmt.Sprintf("%+v", e), fmt.Sprintf("%v", err), fmt.Sprintf("%#v", e.Cause)}
		for c := error(e); c != nil; c = errors.Unwrap(c) {
			texts = append(texts, c.Error())
		}
		for _, text := range texts {
			for _, v := range []string{secret, code, refresh} {
				if strings.Contains(text, v) {
					t.Errorf("%s: %q leaks %q", name, text, v)
				}
			}
		}
	}
}
