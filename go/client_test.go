package tiktokshop

import (
	"bytes"
	"context"
	"errors"
	"io"
	"mime"
	"mime/multipart"
	"net"
	"net/http"
	"net/http/httptest"
	"net/url"
	"os"
	"path/filepath"
	"strconv"
	"strings"
	"sync"
	"testing"
	"time"

	"github.com/isaackogan/TikTok-Shop-Api-SDKs/go/generated"
)

const okBody = `{"code":0,"message":"Success","request_id":"r0","data":{}}`

type seen struct {
	Method      string
	Path        string
	RawQuery    string
	Header      http.Header
	Body        []byte
	ContentType string
}

// stub is an httptest.Server that records requests and replies as told.
type stub struct {
	*httptest.Server
	mu     sync.Mutex
	reqs   []seen
	status int
	body   string
}

func newStub(t *testing.T) *stub {
	t.Helper()
	s := &stub{status: 200, body: okBody}
	s.Server = httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		b, _ := io.ReadAll(r.Body)
		s.mu.Lock()
		s.reqs = append(s.reqs, seen{r.Method, r.URL.Path, r.URL.RawQuery, r.Header.Clone(), b, r.Header.Get("Content-Type")})
		status, body := s.status, s.body
		s.mu.Unlock()
		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(status)
		_, _ = w.Write([]byte(body))
	}))
	t.Cleanup(s.Close)
	return s
}

func (s *stub) last(t *testing.T) seen {
	t.Helper()
	s.mu.Lock()
	defer s.mu.Unlock()
	if len(s.reqs) == 0 {
		t.Fatal("stub saw no request")
	}
	return s.reqs[len(s.reqs)-1]
}

func (s *stub) client(opts ...func(*Options)) *TikTokShop {
	o := Options{AppKey: "k1", AppSecret: "s1", AccessToken: "tok", ShopCipher: "cipher1", BaseURL: s.URL}
	for _, f := range opts {
		f(&o)
	}
	return New(o)
}

// decodedQuery percent-decodes a wire query exactly as a server would (a "+" is a space).
func decodedQuery(t *testing.T, raw string) []QueryParam {
	t.Helper()
	var out []QueryParam
	for _, p := range strings.Split(raw, "&") {
		k, v, _ := strings.Cut(p, "=")
		dk, err1 := url.QueryUnescape(k)
		dv, err2 := url.QueryUnescape(v)
		if err1 != nil || err2 != nil {
			t.Fatalf("bad query %q", raw)
		}
		out = append(out, QueryParam{dk, dv})
	}
	return out
}

func qv(q []QueryParam, key string) (string, int) {
	val, n := "", 0
	for _, p := range q {
		if p.Key == key {
			val = p.Value
			n++
		}
	}
	return val, n
}

// checkSigned recomputes the signature from what the server received.
func checkSigned(t *testing.T, r seen, secret string) {
	t.Helper()
	q := decodedQuery(t, r.RawQuery)
	sent, _ := qv(q, "sign")
	var rest []QueryParam
	for _, p := range q {
		if p.Key != "sign" {
			rest = append(rest, p)
		}
	}
	var body []byte
	if len(r.Body) > 0 {
		body = r.Body
	}
	want := Signer{}.Sign(SignRequest{Path: r.Path, Query: rest, ContentType: r.ContentType, Body: body, AppSecret: secret})
	if sent != want {
		t.Errorf("sign = %q, want %q (query %q)", sent, want, r.RawQuery)
	}
}

func TestAuthorizedShopsIsSignedWithTokenAndNoCipher(t *testing.T) {
	s := newStub(t)
	if _, _, err := s.client().Authorization.GetAuthorizedShops(context.Background()).Execute(); err != nil {
		t.Fatal(err)
	}
	r := s.last(t)
	q := decodedQuery(t, r.RawQuery)
	if r.Path != "/authorization/202309/shops" || r.Method != "GET" {
		t.Errorf("got %s %s", r.Method, r.Path)
	}
	if v, _ := qv(q, "app_key"); v != "k1" {
		t.Errorf("app_key = %q", v)
	}
	ts, _ := qv(q, "timestamp")
	if n, err := strconv.ParseInt(ts, 10, 64); err != nil || time.Since(time.Unix(n, 0)) > time.Minute {
		t.Errorf("timestamp = %q", ts)
	}
	if _, n := qv(q, "shop_cipher"); n != 0 {
		t.Error("shop_cipher must not be sent to the authorization endpoint")
	}
	if got := r.Header.Get("x-tts-access-token"); got != "tok" {
		t.Errorf("token header = %q", got)
	}
	checkSigned(t, r, "s1")
}

func TestOrderListSendsCipherAndPageTokenIntact(t *testing.T) {
	s := newStub(t)
	_, _, err := s.client().Orders.GetOrderList(context.Background()).PageSize(20).PageToken("b2Zmc2V0PTEw+/x==").Execute()
	if err != nil {
		t.Fatal(err)
	}
	r := s.last(t)
	q := decodedQuery(t, r.RawQuery)
	if r.Method != "POST" {
		t.Errorf("method %s", r.Method)
	}
	if v, _ := qv(q, "shop_cipher"); v != "cipher1" {
		t.Errorf("shop_cipher = %q", v)
	}
	if v, _ := qv(q, "page_token"); v != "b2Zmc2V0PTEw+/x==" {
		t.Errorf("page_token = %q", v)
	}
	if !strings.Contains(r.RawQuery, "page_token=b2Zmc2V0PTEw%2B%2Fx%3D%3D") {
		t.Errorf("wire query not RFC 3986 encoded: %s", r.RawQuery)
	}
	checkSigned(t, r, "s1")
}

func TestSpaceIsPercent20AndSignedDecoded(t *testing.T) {
	s := newStub(t)
	_, _, err := s.client().Orders.GetOrderList(context.Background()).PageSize(1).PageToken("a b+c").Execute()
	if err != nil {
		t.Fatal(err)
	}
	r := s.last(t)
	if !strings.Contains(r.RawQuery, "page_token=a%20b%2Bc") {
		t.Errorf("wire query: %s", r.RawQuery)
	}
	if v, _ := qv(decodedQuery(t, r.RawQuery), "page_token"); v != "a b+c" {
		t.Errorf("decoded = %q", v)
	}
	checkSigned(t, r, "s1")
}

func TestJSONBodyIsSigned(t *testing.T) {
	s := newStub(t)
	st := "UNPAID"
	req := generated.GetOrderListRequest{OrderStatus: &st}
	if _, _, err := s.client().Orders.GetOrderList(context.Background()).PageSize(5).GetOrderListRequest(req).Execute(); err != nil {
		t.Fatal(err)
	}
	r := s.last(t)
	if !bytes.Contains(r.Body, []byte("UNPAID")) {
		t.Errorf("body = %s", r.Body)
	}
	checkSigned(t, r, "s1")
}

func TestGetWithBodySendsAndSignsTheBody(t *testing.T) {
	s := newStub(t)
	yes := true
	_, _, err := s.client().AffiliateSeller.GetConversationList(context.Background()).PageSize(10).
		GetConversationListRequest(generated.GetConversationListRequest{OnlyNeedConversationId: &yes}).Execute()
	if err != nil {
		t.Fatal(err)
	}
	r := s.last(t)
	if r.Method != "GET" || r.Path != "/affiliate_seller/202412/conversations" {
		t.Errorf("got %s %s", r.Method, r.Path)
	}
	if strings.TrimSpace(string(r.Body)) != `{"only_need_conversation_id":true}` {
		t.Errorf("GET body did not arrive: %q", r.Body)
	}
	if v, _ := qv(decodedQuery(t, r.RawQuery), "shop_cipher"); v != "cipher1" {
		t.Errorf("shop_cipher = %q", v)
	}
	checkSigned(t, r, "s1")
}

func TestNoTokenHeaderWithoutAccessToken(t *testing.T) {
	s := newStub(t)
	c := s.client(func(o *Options) { o.AccessToken = "" })
	if _, _, err := c.Authorization.GetAuthorizedShops(context.Background()).Execute(); err != nil {
		t.Fatal(err)
	}
	if _, ok := s.last(t).Header["X-Tts-Access-Token"]; ok {
		t.Error("token header sent without a token")
	}
}

// recorder is an inner RoundTripper that records what the signing layer hands it.
type recorder struct{ got *http.Request }

func (r *recorder) RoundTrip(req *http.Request) (*http.Response, error) {
	r.got = req
	return &http.Response{StatusCode: 200, Header: http.Header{"Content-Type": {"application/json"}}, Body: io.NopCloser(strings.NewReader(okBody)), Request: req}, nil
}

func TestHookReplacesCallerSuppliedReservedParams(t *testing.T) {
	rec := &recorder{}
	tr := &signingTransport{creds: credentials{appKey: "k1", appSecret: "s1", accessToken: "tok", shopCipher: "cipher1"}, inner: rec}
	req, _ := http.NewRequest("POST", "https://open-api.tiktokglobalshop.com/order/202309/orders/search?app_key=evil&sign=x&timestamp=1&shop_cipher=bad&page_size=3", strings.NewReader("{}"))
	req.Header.Set("Content-Type", "application/json")
	resp, err := tr.RoundTrip(req)
	if err != nil {
		t.Fatal(err)
	}
	_ = resp.Body.Close()
	if req.URL.RawQuery != "app_key=evil&sign=x&timestamp=1&shop_cipher=bad&page_size=3" {
		t.Error("the caller's request must not be modified")
	}
	q := decodedQuery(t, rec.got.URL.RawQuery)
	for _, k := range []string{"app_key", "sign", "timestamp", "shop_cipher"} {
		if _, n := qv(q, k); n != 1 {
			t.Errorf("%s appears %d times", k, n)
		}
	}
	if v, _ := qv(q, "app_key"); v != "k1" {
		t.Errorf("app_key = %q", v)
	}
	if v, _ := qv(q, "shop_cipher"); v != "cipher1" {
		t.Errorf("shop_cipher = %q", v)
	}
	if v, _ := qv(q, "timestamp"); v == "1" {
		t.Error("timestamp not replaced")
	}
	if v, _ := qv(q, "sign"); v == "x" {
		t.Error("sign not replaced")
	}
	if v, _ := qv(q, "page_size"); v != "3" {
		t.Errorf("page_size = %q", v)
	}
	body, _ := io.ReadAll(rec.got.Body)
	checkSigned(t, seen{Path: rec.got.URL.Path, RawQuery: rec.got.URL.RawQuery, Body: body, ContentType: "application/json"}, "s1")
}

func TestMultipartUploadIsSentIntactAndSignedWithoutTheBody(t *testing.T) {
	s := newStub(t)
	f := filepath.Join(t.TempDir(), "a.png")
	if err := os.WriteFile(f, []byte("PNGDATA"), 0o600); err != nil {
		t.Fatal(err)
	}
	file, err := os.Open(f)
	if err != nil {
		t.Fatal(err)
	}
	defer file.Close()
	if _, _, err := s.client().Products.UploadProductImage(context.Background()).Data(file).Execute(); err != nil {
		t.Fatal(err)
	}
	r := s.last(t)
	mt, params, err := mime.ParseMediaType(r.ContentType)
	if err != nil || mt != "multipart/form-data" || params["boundary"] == "" {
		t.Fatalf("content type %q", r.ContentType)
	}
	part, err := multipart.NewReader(bytes.NewReader(r.Body), params["boundary"]).NextPart()
	if err != nil {
		t.Fatalf("multipart body did not arrive intact: %v", err)
	}
	data, _ := io.ReadAll(part)
	if string(data) != "PNGDATA" || part.FileName() != "a.png" {
		t.Errorf("part = %q %q", part.FileName(), data)
	}
	q := decodedQuery(t, r.RawQuery)
	sent, _ := qv(q, "sign")
	var rest []QueryParam
	for _, p := range q {
		if p.Key != "sign" {
			rest = append(rest, p)
		}
	}
	if want := (Signer{}).Sign(SignRequest{Path: r.Path, Query: rest, ContentType: r.ContentType, AppSecret: "s1"}); sent != want {
		t.Errorf("sign = %q, want the body-less %q", sent, want)
	}
	// A signature over the body must differ, so the check above is not vacuous.
	if with := (Signer{}).Sign(SignRequest{Path: r.Path, Query: rest, ContentType: "application/octet-stream", Body: r.Body, AppSecret: "s1"}); sent == with {
		t.Error("signature equals the one that includes the body")
	}
}

func TestCodeNotZeroIsAnErrorEvenOnHTTP200(t *testing.T) {
	s := newStub(t)
	s.body = `{"code":36009003,"message":"invalid","request_id":"r1","data":{}}`
	_, _, err := s.client().Authorization.GetAuthorizedShops(context.Background()).Execute()
	var e *Error
	if !errors.As(err, &e) {
		t.Fatalf("errors.As failed: %T %v", err, err)
	}
	if e.Code != 36009003 || e.Message != "invalid" || e.RequestID != "r1" || e.HTTPStatus != 200 {
		t.Errorf("%+v", e)
	}
}

func TestNon2xxIsAnError(t *testing.T) {
	s := newStub(t)
	s.status = 503
	s.body = `{"code":98765,"message":"busy","request_id":"r2"}`
	_, _, err := s.client().Authorization.GetAuthorizedShops(context.Background()).Execute()
	var e *Error
	if !errors.As(err, &e) {
		t.Fatalf("errors.As failed: %T %v", err, err)
	}
	if e.HTTPStatus != 503 || e.Code != 98765 || e.Message != "busy" || e.RequestID != "r2" {
		t.Errorf("%+v", e)
	}
}

func TestNon2xxWithoutEnvelope(t *testing.T) {
	s := newStub(t)
	s.status = 502
	s.body = "<html>bad gateway</html>"
	_, _, err := s.client().Authorization.GetAuthorizedShops(context.Background()).Execute()
	var e *Error
	if !errors.As(err, &e) {
		t.Fatalf("errors.As failed: %T %v", err, err)
	}
	if e.HTTPStatus != 502 || e.Code != 502 || e.Message == "" {
		t.Errorf("%+v", e)
	}
}

func TestNonJSON2xxIsAnErrorWithCause(t *testing.T) {
	s := newStub(t)
	s.body = "not json"
	_, _, err := s.client().Authorization.GetAuthorizedShops(context.Background()).Execute()
	var e *Error
	if !errors.As(err, &e) {
		t.Fatalf("errors.As failed: %T %v", err, err)
	}
	if e.HTTPStatus != 200 || e.Cause == nil {
		t.Errorf("%+v", e)
	}
}

func TestSuccessReturnsTheParsedModel(t *testing.T) {
	s := newStub(t)
	s.body = `{"code":0,"message":"Success","request_id":"r9","data":{"shops":[{"id":"7494049642642441621","name":"Shop"}]}}`
	out, _, err := s.client().Authorization.GetAuthorizedShops(context.Background()).Execute()
	if err != nil {
		t.Fatal(err)
	}
	if out.GetRequestId() != "r9" || len(out.Data.GetShops()) != 1 || out.Data.GetShops()[0].GetId() != "7494049642642441621" {
		t.Errorf("%+v", out)
	}
}

func TestClosedPortIsAnErrorWithCause(t *testing.T) {
	l, err := net.Listen("tcp", "127.0.0.1:0")
	if err != nil {
		t.Fatal(err)
	}
	addr := l.Addr().String()
	_ = l.Close()
	c := New(Options{AppKey: "k", AppSecret: "s", BaseURL: "http://" + addr})
	_, _, err = c.Authorization.GetAuthorizedShops(context.Background()).Execute()
	var e *Error
	if !errors.As(err, &e) {
		t.Fatalf("errors.As failed: %T %v", err, err)
	}
	var op *net.OpError
	if e.Cause == nil || !errors.As(err, &op) {
		t.Errorf("cause = %v", e.Cause)
	}
	if e.HTTPStatus != 0 {
		t.Errorf("HTTPStatus = %d", e.HTTPStatus)
	}
}

func TestTimeoutIsAnErrorWithCause(t *testing.T) {
	release := make(chan struct{})
	srv := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		select {
		case <-release:
		case <-r.Context().Done():
		}
	}))
	t.Cleanup(func() { close(release); srv.Close() })
	c := New(Options{AppKey: "k", AppSecret: "s", BaseURL: srv.URL, Timeout: 150 * time.Millisecond})
	start := time.Now()
	_, _, err := c.Authorization.GetAuthorizedShops(context.Background()).Execute()
	var e *Error
	if !errors.As(err, &e) {
		t.Fatalf("errors.As failed: %T %v", err, err)
	}
	if !errors.Is(err, context.DeadlineExceeded) {
		t.Errorf("cause = %v", e.Cause)
	}
	if time.Since(start) > 5*time.Second {
		t.Error("took too long")
	}
}

func TestCallerContextCancellationIsReported(t *testing.T) {
	s := newStub(t)
	ctx, cancel := context.WithCancel(context.Background())
	cancel()
	_, _, err := s.client().Authorization.GetAuthorizedShops(ctx).Execute()
	if !errors.Is(err, context.Canceled) {
		t.Errorf("err = %v", err)
	}
}

func TestWithShopDoesNotTouchTheOriginal(t *testing.T) {
	s := newStub(t)
	a := s.client()
	b := a.WithShop(ShopAccessToken("tok2"), ShopCipher("cipher2"))
	if _, _, err := b.Orders.GetOrderList(context.Background()).PageSize(1).Execute(); err != nil {
		t.Fatal(err)
	}
	rb := s.last(t)
	if v, _ := qv(decodedQuery(t, rb.RawQuery), "shop_cipher"); v != "cipher2" || rb.Header.Get("x-tts-access-token") != "tok2" {
		t.Errorf("child sent cipher %q token %q", v, rb.Header.Get("x-tts-access-token"))
	}
	checkSigned(t, rb, "s1")
	if _, _, err := a.Orders.GetOrderList(context.Background()).PageSize(1).Execute(); err != nil {
		t.Fatal(err)
	}
	ra := s.last(t)
	if v, _ := qv(decodedQuery(t, ra.RawQuery), "shop_cipher"); v != "cipher1" || ra.Header.Get("x-tts-access-token") != "tok" {
		t.Errorf("original now sends cipher %q token %q", v, ra.Header.Get("x-tts-access-token"))
	}
}

func TestWithShopSharesTheTransport(t *testing.T) {
	rec := &recorder{}
	a := New(Options{AppKey: "k", AppSecret: "s", BaseURL: "http://example.invalid", Transport: rec})
	b := a.WithShop(ShopAccessToken("t"), ShopCipher("c"))
	if _, _, err := b.Authorization.GetAuthorizedShops(context.Background()).Execute(); err != nil {
		t.Fatal(err)
	}
	if rec.got == nil || rec.got.Header.Get("x-tts-access-token") != "t" {
		t.Error("the child did not use the shared inner transport")
	}
}

// withShopSends calls GetOrderList on c and returns the shop_cipher (and its count) and the token header.
func withShopSends(t *testing.T, s *stub, c *TikTokShop) (cipher string, n int, token string) {
	t.Helper()
	if _, _, err := c.Orders.GetOrderList(context.Background()).PageSize(1).Execute(); err != nil {
		t.Fatal(err)
	}
	r := s.last(t)
	cipher, n = qv(decodedQuery(t, r.RawQuery), "shop_cipher")
	return cipher, n, r.Header.Get("x-tts-access-token")
}

func TestWithShopKeepsWhatIsOmitted(t *testing.T) {
	s := newStub(t)
	a := s.client()
	if cipher, _, token := withShopSends(t, s, a.WithShop(ShopAccessToken("tok2"))); cipher != "cipher1" || token != "tok2" {
		t.Errorf("token-only: cipher %q token %q", cipher, token)
	}
	if cipher, _, token := withShopSends(t, s, a.WithShop(ShopCipher("cipher2"))); cipher != "cipher2" || token != "tok" {
		t.Errorf("cipher-only: cipher %q token %q", cipher, token)
	}
	if cipher, _, token := withShopSends(t, s, a.WithShop()); cipher != "cipher1" || token != "tok" {
		t.Errorf("none: cipher %q token %q", cipher, token)
	}
	if cipher, _, token := withShopSends(t, s, a); cipher != "cipher1" || token != "tok" {
		t.Errorf("original changed: cipher %q token %q", cipher, token)
	}
}

func TestWithShopReplacesBoth(t *testing.T) {
	s := newStub(t)
	a := s.client()
	if cipher, n, token := withShopSends(t, s, a.WithShop(ShopAccessToken("tok2"), ShopCipher("cipher2"))); cipher != "cipher2" || n != 1 || token != "tok2" {
		t.Errorf("cipher %q (x%d) token %q", cipher, n, token)
	}
	if cipher, _, token := withShopSends(t, s, a); cipher != "cipher1" || token != "tok" {
		t.Errorf("original changed: cipher %q token %q", cipher, token)
	}
}

func TestWithShopEmptyValueClears(t *testing.T) {
	s := newStub(t)
	a := s.client()
	if _, n, token := withShopSends(t, s, a.WithShop(ShopCipher(""))); n != 0 || token != "tok" {
		t.Errorf("cipher cleared: shop_cipher x%d token %q", n, token)
	}
	if _, _, token := withShopSends(t, s, a.WithShop(ShopAccessToken(""))); token != "" {
		t.Errorf("token cleared: token %q", token)
	}
	if cipher, n, token := withShopSends(t, s, a); cipher != "cipher1" || n != 1 || token != "tok" {
		t.Errorf("original changed: cipher %q token %q", cipher, token)
	}
}
