package tiktokshop

import (
	"encoding/json"
	"os"
	"testing"
)

type signingCase struct {
	Name         string     `json:"name"`
	Secret       string     `json:"secret"`
	Method       string     `json:"method"`
	Path         string     `json:"path"`
	Query        [][]string `json:"query"`
	ContentType  *string    `json:"contentType"`
	Body         *string    `json:"body"`
	StringToSign string     `json:"stringToSign"`
	Sign         string     `json:"sign"`
}

func TestSigningVectors(t *testing.T) {
	raw, err := os.ReadFile("../shared/test-vectors/signing.json")
	if err != nil {
		t.Fatal(err)
	}
	var file struct {
		Cases []signingCase `json:"cases"`
	}
	if err := json.Unmarshal(raw, &file); err != nil {
		t.Fatal(err)
	}
	if len(file.Cases) == 0 {
		t.Fatal("no cases")
	}
	for _, c := range file.Cases {
		t.Run(c.Name, func(t *testing.T) {
			req := SignRequest{Path: c.Path, AppSecret: c.Secret}
			for _, p := range c.Query {
				req.Query = append(req.Query, QueryParam{Key: p[0], Value: p[1]})
			}
			if c.ContentType != nil {
				req.ContentType = *c.ContentType
			}
			if c.Body != nil {
				req.Body = []byte(*c.Body)
			}
			if got := (Signer{}).StringToSign(req); got != c.StringToSign {
				t.Errorf("StringToSign\n got %q\nwant %q", got, c.StringToSign)
			}
			if got := (Signer{}).Sign(req); got != c.Sign {
				t.Errorf("Sign got %q want %q", got, c.Sign)
			}
		})
	}
}

func TestRequiresShopCipher(t *testing.T) {
	cases := []struct {
		method, path string
		want         bool
	}{
		{"POST", "/order/202309/orders/search", true},
		{"post", "/order/202309/orders/search", true},
		{"GET", "/authorization/202309/shops", false},
		{"GET", "/product/202309/products/1729507467923261408", true},
		{"GET", "/no/such/path", false},
		{"DELETE", "/order/202309/orders/search", false},
	}
	for _, c := range cases {
		if got := RequiresShopCipher(c.method, c.path); got != c.want {
			t.Errorf("RequiresShopCipher(%s, %s) = %v, want %v", c.method, c.path, got, c.want)
		}
	}
}
