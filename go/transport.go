package tiktokshop

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"strconv"
	"strings"
	"time"
)

type credentials struct {
	appKey, appSecret, accessToken, shopCipher string
}

var reserved = map[string]bool{"app_key": true, "timestamp": true, "sign": true, "shop_cipher": true}

// signingTransport is the request and response hook: it signs every request and turns every failure
// into an *Error. It never modifies the request it is given.
type signingTransport struct {
	creds   credentials
	inner   http.RoundTripper
	timeout time.Duration // 0: none
}

const unreserved = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~"

// encode is RFC 3986 percent-encoding: everything but the unreserved characters.
func encode(s string) string {
	var b strings.Builder
	for i := 0; i < len(s); i++ {
		if strings.IndexByte(unreserved, s[i]) >= 0 {
			b.WriteByte(s[i])
		} else {
			fmt.Fprintf(&b, "%%%02X", s[i])
		}
	}
	return b.String()
}

// decodeQuery recovers the decoded pairs. The generated client writes the query with url.Values.Encode,
// so a space is "+" and a literal plus is "%2B": QueryUnescape inverts it exactly.
func decodeQuery(raw string) []QueryParam {
	var out []QueryParam
	for _, p := range strings.Split(raw, "&") {
		if p == "" {
			continue
		}
		k, v, _ := strings.Cut(p, "=")
		if dk, err := url.QueryUnescape(k); err == nil {
			k = dk
		}
		if dv, err := url.QueryUnescape(v); err == nil {
			v = dv
		}
		out = append(out, QueryParam{k, v})
	}
	return out
}

func (t *signingTransport) RoundTrip(req *http.Request) (*http.Response, error) {
	var body []byte
	if req.Body != nil && req.Body != http.NoBody {
		b, err := io.ReadAll(req.Body)
		_ = req.Body.Close()
		if err != nil {
			return nil, &Error{Message: "reading the request body: " + err.Error(), Cause: err}
		}
		body = b
	}

	out := req.Clone(req.Context())
	c := t.creds
	var query []QueryParam
	for _, p := range decodeQuery(req.URL.RawQuery) {
		if !reserved[p.Key] {
			query = append(query, p)
		}
	}
	if c.shopCipher != "" && RequiresShopCipher(req.Method, req.URL.Path) {
		query = append(query, QueryParam{"shop_cipher", c.shopCipher})
	}
	query = append(query, QueryParam{"app_key", c.appKey}, QueryParam{"timestamp", strconv.FormatInt(time.Now().Unix(), 10)})
	if c.accessToken != "" {
		out.Header.Set("x-tts-access-token", c.accessToken)
	}
	sign := Signer{}.Sign(SignRequest{
		Path:        req.URL.EscapedPath(),
		Query:       query,
		ContentType: req.Header.Get("Content-Type"),
		Body:        body,
		AppSecret:   c.appSecret,
	})
	query = append(query, QueryParam{"sign", sign})
	parts := make([]string, len(query))
	for i, p := range query {
		parts[i] = encode(p.Key) + "=" + encode(p.Value)
	}
	out.URL.RawQuery = strings.Join(parts, "&")

	// A body on any method, GET included, is sent as is.
	if len(body) > 0 {
		out.Body = io.NopCloser(bytes.NewReader(body))
		out.GetBody = func() (io.ReadCloser, error) { return io.NopCloser(bytes.NewReader(body)), nil }
		out.ContentLength = int64(len(body))
	} else {
		out.Body, out.GetBody, out.ContentLength = http.NoBody, nil, 0
	}

	if t.timeout > 0 {
		ctx, cancel := context.WithTimeout(out.Context(), t.timeout)
		defer cancel() // the body is read before returning, so the deadline covers it
		out = out.WithContext(ctx)
	}
	inner := t.inner
	if inner == nil {
		inner = http.DefaultTransport
	}
	resp, err := inner.RoundTrip(out)
	if err != nil {
		return nil, &Error{Message: "request failed: " + err.Error(), Cause: err}
	}
	data, err := io.ReadAll(resp.Body)
	_ = resp.Body.Close()
	if err != nil {
		return nil, &Error{Message: "reading the response: " + err.Error(), HTTPStatus: resp.StatusCode, Cause: err}
	}
	if err := checkResponse(resp.StatusCode, resp.Status, data); err != nil {
		return nil, err
	}
	resp.Body = io.NopCloser(bytes.NewReader(data))
	return resp, nil
}

// checkResponse is the response hook: nil for a successful envelope, otherwise the *Error.
func checkResponse(status int, statusText string, data []byte) error {
	ok := status >= 200 && status < 300
	var env map[string]json.RawMessage
	parseErr := json.Unmarshal(data, &env)
	if ok && parseErr != nil && !json.Valid(data) {
		return &Error{Message: fmt.Sprintf("Response is not valid JSON (HTTP %d)", status), HTTPStatus: status, Cause: parseErr}
	}
	var code *int
	var message *string
	requestID := ""
	if raw, found := env["code"]; found {
		var n json.Number
		if json.Unmarshal(raw, &n) == nil {
			if v, err := strconv.Atoi(n.String()); err == nil {
				code = &v
			}
		}
	}
	if raw, found := env["message"]; found {
		var s string
		if json.Unmarshal(raw, &s) == nil {
			message = &s
		}
	}
	if raw, found := env["request_id"]; found {
		_ = json.Unmarshal(raw, &requestID)
	}
	if !ok {
		e := &Error{Code: status, RequestID: requestID, HTTPStatus: status}
		if code != nil {
			e.Code = *code
		}
		switch {
		case message != nil:
			e.Message = *message
		case http.StatusText(status) != "":
			e.Message = http.StatusText(status)
		default:
			e.Message = fmt.Sprintf("HTTP %d", status)
		}
		return e
	}
	if code != nil && *code != 0 {
		m := ""
		if message != nil {
			m = *message
		}
		return &Error{Code: *code, Message: m, RequestID: requestID, HTTPStatus: status}
	}
	return nil
}
