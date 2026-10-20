package tiktokshop

// Cross-language rules from the final review: R13c, R13d, R28, lesson 34 and the minors that align Go with the
// other seven SDKs.

import (
	"context"
	"encoding/json"
	"errors"
	"net"
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
	"time"

	"github.com/isaackogan/TikTok-Shop-Api-SDKs/go/generated"
)

func closedURL(t *testing.T) string {
	t.Helper()
	l, err := net.Listen("tcp", "127.0.0.1:0")
	if err != nil {
		t.Fatal(err)
	}
	addr := l.Addr().String()
	_ = l.Close()
	return "http://" + addr
}

func hangingURL(t *testing.T) string {
	t.Helper()
	srv := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) { <-r.Context().Done() }))
	t.Cleanup(srv.Close)
	return srv.URL
}

func wantTransportError(t *testing.T, what string, err error) {
	t.Helper()
	var e *Error
	if !errors.As(err, &e) {
		t.Fatalf("%s: errors.As failed: %T %v", what, err, err)
	}
	if e.Code != -1 || e.HTTPStatus != 0 || e.Cause == nil {
		t.Errorf("%s: code %d, http %d, cause %v; want -1, 0, non-nil", what, e.Code, e.HTTPStatus, e.Cause)
	}
}

// R13c: a transport failure with no HTTP response is code -1 with no HTTPStatus, on API and token calls.
func TestTransportFailuresAreMinusOneWithoutStatus(t *testing.T) {
	ctx := context.Background()
	_, _, err := New(Options{AppKey: "k", AppSecret: "s", BaseURL: closedURL(t)}).Authorization.GetAuthorizedShops(ctx).Execute()
	wantTransportError(t, "API closed port", err)
	_, _, err = New(Options{AppKey: "k", AppSecret: "s", BaseURL: hangingURL(t), Timeout: 100 * time.Millisecond}).Authorization.GetAuthorizedShops(ctx).Execute()
	wantTransportError(t, "API timeout", err)

	_, err = NewAuth(AuthOptions{AppKey: "k", AppSecret: "s", BaseURL: closedURL(t)}).ExchangeCode(ctx, "c")
	wantTransportError(t, "token closed port", err)
	_, err = NewAuth(AuthOptions{AppKey: "k", AppSecret: "s", BaseURL: hangingURL(t), Timeout: 100 * time.Millisecond}).Refresh(ctx, "r")
	wantTransportError(t, "token timeout", err)
}

// R13d: a 2xx envelope that does not decode into its model is an *Error with code -1, the status and the request ID.
func TestDecodeFailureIsAnErrorWithMinusOne(t *testing.T) {
	s := newStub(t)
	s.body = `{"code":0,"message":"Success","request_id":"q9","data":{"shops":"not a list"}}`
	out, res, err := s.client().Authorization.GetAuthorizedShops(context.Background()).Execute()
	var e *Error
	if !errors.As(err, &e) {
		t.Fatalf("errors.As failed: %T %v", err, err)
	}
	if e.Code != -1 || e.HTTPStatus != 200 || e.RequestID != "q9" || e.Cause == nil {
		t.Errorf("got %+v", e)
	}
	var ge *generated.GenericOpenAPIError
	if errors.As(err, &ge) {
		t.Error("still a GenericOpenAPIError")
	}
	_, _ = out, res
}

// I3: an operation whose optional body is omitted sends no body at all (not a JSON null), signed in the empty-body form.
func TestOmittedOptionalBodyIsSentEmpty(t *testing.T) {
	s := newStub(t)
	if _, _, err := s.client().Orders.GetOrderList(context.Background()).PageSize(20).Execute(); err != nil {
		t.Fatal(err)
	}
	r := s.last(t)
	if len(r.Body) != 0 || r.ContentType != "" {
		t.Errorf("body %q, content type %q; want both empty", r.Body, r.ContentType)
	}
	checkSigned(t, r, "s1")

	// The three GET-with-body operations too, with no body set.
	if _, _, err := s.client().AffiliateSeller.GetConversationList(context.Background()).PageSize(1).Execute(); err != nil {
		t.Fatal(err)
	}
	if r := s.last(t); len(r.Body) != 0 || r.ContentType != "" {
		t.Errorf("GET: body %q, content type %q", r.Body, r.ContentType)
	}
	// A body that is set is still sent and signed.
	if _, _, err := s.client().Orders.GetOrderList(context.Background()).PageSize(1).GetOrderListRequest(generated.GetOrderListRequest{}).Execute(); err != nil {
		t.Fatal(err)
	}
	if r := s.last(t); strings.TrimSpace(string(r.Body)) != "{}" {
		t.Errorf("set body = %q", r.Body)
	}
}

// M1: a zero Timeout means DefaultTimeout; a negative one means no limit.
func TestTimeoutZeroIsTheDefaultAndNegativeIsNone(t *testing.T) {
	timeoutOf := func(c *TikTokShop) time.Duration { return c.opts.Timeout } // as resolved by New: 0 is none
	if got := timeoutOf(New(Options{})); got != DefaultTimeout {
		t.Errorf("0 -> %v, want %v", got, DefaultTimeout)
	}
	if got := timeoutOf(New(Options{Timeout: -1})); got != 0 {
		t.Errorf("-1 -> %v, want none", got)
	}
	if got := timeoutOf(New(Options{Timeout: -1}).WithShop()); got != 0 {
		t.Errorf("WithShop of -1 -> %v, want none", got)
	}
	if got := NewAuth(AuthOptions{}).client.Timeout; got != DefaultTimeout {
		t.Errorf("auth 0 -> %v", got)
	}
	if got := NewAuth(AuthOptions{Timeout: -1}).client.Timeout; got != 0 {
		t.Errorf("auth -1 -> %v", got)
	}
}

// M3: an empty access_token or refresh_token is rejected like a missing one.
func TestEmptyTokenStringsAreRejected(t *testing.T) {
	for _, k := range []string{"access_token", "refresh_token"} {
		d := map[string]any{"access_token": "a", "access_token_expire_in": 1, "refresh_token": "r", "refresh_token_expire_in": 2}
		d[k] = ""
		b, _ := json.Marshal(map[string]any{"code": 0, "request_id": "q7", "data": d})
		srv, _ := authStub(t, 200, string(b))
		_, err := NewAuth(AuthOptions{AppKey: "k", AppSecret: "s", BaseURL: srv.URL}).ExchangeCode(context.Background(), "c")
		var e *Error
		if !errors.As(err, &e) || e.Code != -1 || e.RequestID != "q7" || e.HTTPStatus != 200 {
			t.Errorf("%s empty: %v", k, err)
		}
	}
}

// M20 (lesson 34): a 2xx whose code is present but not an integer is -1.
func TestNonIntegerCodeOn2xxIsMinusOne(t *testing.T) {
	for _, code := range []string{`"0"`, `1.5`, `true`, `null`, `{}`, `1e2`} {
		s := newStub(t)
		s.body = `{"code":` + code + `,"message":"m","request_id":"q5","data":{}}`
		_, _, err := s.client().Authorization.GetAuthorizedShops(context.Background()).Execute()
		var e *Error
		if !errors.As(err, &e) || e.Code != -1 || e.HTTPStatus != 200 || e.RequestID != "q5" {
			t.Errorf("API code %s: %v", code, err)
		}
		srv, _ := authStub(t, 200, `{"code":`+code+`,"request_id":"q6","data":{"access_token":"a","access_token_expire_in":1,"refresh_token":"r","refresh_token_expire_in":2}}`)
		_, err = NewAuth(AuthOptions{AppKey: "k", AppSecret: "s", BaseURL: srv.URL}).ExchangeCode(context.Background(), "c")
		if !errors.As(err, &e) || e.Code != -1 || e.HTTPStatus != 200 {
			t.Errorf("token code %s: %v", code, err)
		}
	}
	s := newStub(t)
	s.body = `{"request_id":"q","data":{}}`
	if _, _, err := s.client().Authorization.GetAuthorizedShops(context.Background()).Execute(); err != nil {
		t.Errorf("no code at all is a success: %v", err)
	}
}

// Lesson 34: User-Agent tiktok-shop-api-go/<version> on API and token calls.
func TestUserAgentOnAPIAndTokenCalls(t *testing.T) {
	if !strings.HasPrefix(userAgent, "tiktok-shop-api-go/") {
		t.Fatalf("userAgent = %q", userAgent)
	}
	s := newStub(t)
	if _, _, err := s.client().Authorization.GetAuthorizedShops(context.Background()).Execute(); err != nil {
		t.Fatal(err)
	}
	if ua := s.last(t).Header.Get("User-Agent"); ua != userAgent {
		t.Errorf("API UA = %q", ua)
	}
	var got string
	srv := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		got = r.Header.Get("User-Agent")
		_, _ = w.Write([]byte(`{"code":0,"request_id":"r","data":{"access_token":"a","access_token_expire_in":1,"refresh_token":"r","refresh_token_expire_in":2}}`))
	}))
	defer srv.Close()
	if _, err := NewAuth(AuthOptions{AppKey: "k", AppSecret: "s", BaseURL: srv.URL}).Refresh(context.Background(), "r"); err != nil {
		t.Fatal(err)
	}
	if got != userAgent {
		t.Errorf("token UA = %q", got)
	}
}

// R21b: an integer enum value the spec does not list still decodes.
func TestUnknownIntegerEnumValueDecodes(t *testing.T) {
	s := newStub(t)
	s.body = `{"code":0,"request_id":"r","data":{"creators":[{"creator_profile":{"user_type_tag":[1,3]}}]}}`
	out, _, err := s.client().AffiliateSeller.SearchCreatorsInCreatorMarketplace(context.Background()).PageSize(1).Execute()
	if err != nil {
		t.Fatal(err)
	}
	b, _ := json.Marshal(out)
	if !strings.Contains(string(b), `"user_type_tag":[1,3]`) {
		t.Errorf("%s", b)
	}
}

// R28: a known type's required fields must be present and non-null, at any depth.
func TestParseRejectsNullOrMissingRequiredFields(t *testing.T) {
	appeal := func() map[string]any {
		return map[string]any{
			"type": 66, "shop_id": "1", "tts_notification_id": "n1", "timestamp": 1,
			"data": map[string]any{"product_id": 5, "appeal_task": map[string]any{"appeal_audit_result": []any{map[string]any{"indicator_type": "A", "status": "S"}}}},
		}
	}
	b, _ := json.Marshal(appeal())
	if _, err := Webhooks.Parse(b); err != nil {
		t.Fatalf("complete event: %v", err)
	}
	edits := map[string]func(map[string]any){
		"null shop_id":         func(m map[string]any) { m["shop_id"] = nil },
		"null timestamp":       func(m map[string]any) { m["timestamp"] = nil },
		"null data":            func(m map[string]any) { m["data"] = nil },
		"missing product_id":   func(m map[string]any) { delete(m["data"].(map[string]any), "product_id") },
		"null product_id":      func(m map[string]any) { m["data"].(map[string]any)["product_id"] = nil },
		"null status in list":  func(m map[string]any) { listItem(m)["status"] = nil },
		"missing type in list": func(m map[string]any) { delete(listItem(m), "indicator_type") },
	}
	for name, edit := range edits {
		m := appeal()
		edit(m)
		b, _ := json.Marshal(m)
		if ev, err := Webhooks.Parse(b); err == nil {
			t.Errorf("%s: want a parse error, got %#v", name, ev)
		}
	}
}

func listItem(m map[string]any) map[string]any {
	return m["data"].(map[string]any)["appeal_task"].(map[string]any)["appeal_audit_result"].([]any)[0].(map[string]any)
}
