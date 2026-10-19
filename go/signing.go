package tiktokshop

import (
	"crypto/hmac"
	"crypto/sha256"
	"encoding/hex"
	"regexp"
	"sort"
	"strings"

	"github.com/isaackogan/TikTok-Shop-Api-SDKs/go/generated"
)

// QueryParam is one query parameter with its decoded value.
type QueryParam struct{ Key, Value string }

// SignRequest is what the signature covers.
type SignRequest struct {
	// Path is the request path, e.g. "/order/202309/orders/search".
	Path string
	// Query holds the decoded values, as the server receives them.
	Query []QueryParam
	// ContentType is the Content-Type header, "" when there is none. A multipart/form-data body is not signed.
	ContentType string
	// Body is the exact request body, nil when there is none.
	Body      []byte
	AppSecret string
}

// Signer holds the pure signing functions.
type Signer struct{}

func isMultipart(contentType string) bool {
	return strings.HasPrefix(strings.ToLower(contentType), "multipart/form-data")
}

// StringToSign is secret + path + the sorted key+value pairs (without sign and access_token) + the
// body (unless multipart) + secret.
func (Signer) StringToSign(r SignRequest) string {
	pairs := make([]QueryParam, 0, len(r.Query))
	for _, p := range r.Query {
		if p.Key != "sign" && p.Key != "access_token" {
			pairs = append(pairs, p)
		}
	}
	sort.SliceStable(pairs, func(i, j int) bool { return pairs[i].Key < pairs[j].Key })
	var b strings.Builder
	b.WriteString(r.AppSecret)
	b.WriteString(r.Path)
	for _, p := range pairs {
		b.WriteString(p.Key)
		b.WriteString(p.Value)
	}
	if !isMultipart(r.ContentType) {
		b.Write(r.Body)
	}
	b.WriteString(r.AppSecret)
	return b.String()
}

// Sign is the lowercase hex HMAC-SHA256 of StringToSign, keyed with the app secret.
func (s Signer) Sign(r SignRequest) string {
	mac := hmac.New(sha256.New, []byte(r.AppSecret))
	mac.Write([]byte(s.StringToSign(r)))
	return hex.EncodeToString(mac.Sum(nil))
}

type matcher struct {
	op       *generated.OperationMeta
	method   string
	literals int
	re       *regexp.Regexp
}

var matchers = func() []matcher {
	var out []matcher
	for i := range generated.Operations {
		op := &generated.Operations[i]
		segs := strings.Split(op.Path, "/")
		lit := 0
		parts := make([]string, len(segs))
		for j, s := range segs {
			if strings.HasPrefix(s, "{") && strings.HasSuffix(s, "}") {
				parts[j] = "[^/]+"
			} else {
				parts[j] = regexp.QuoteMeta(s)
				lit++
			}
		}
		out = append(out, matcher{op, strings.ToUpper(op.HTTPMethod), lit, regexp.MustCompile("^" + strings.Join(parts, "/") + "$")})
	}
	return out
}()

// RequiresShopCipher reports whether the operation matching method and path takes a shop_cipher query
// parameter. A "{x}" in a path template matches exactly one segment; the template with the most
// literal segments wins.
func RequiresShopCipher(method, path string) bool {
	m := strings.ToUpper(method)
	var best *matcher
	for i := range matchers {
		x := &matchers[i]
		if x.method == m && x.re.MatchString(path) && (best == nil || x.literals > best.literals) {
			best = x
		}
	}
	return best != nil && best.op.RequiresShopCipher
}
