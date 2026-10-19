package tiktokshop

import (
	"encoding/json"
	"errors"
	"os"
	"path/filepath"
	"reflect"
	"strings"
	"testing"

	"github.com/isaackogan/TikTok-Shop-Api-SDKs/go/generated"
)

type webhookVectors struct {
	Verify []struct {
		Name      string `json:"name"`
		AppKey    string `json:"appKey"`
		AppSecret string `json:"appSecret"`
		RawBody   string `json:"rawBody"`
		Signature string `json:"signature"`
		Valid     bool   `json:"valid"`
	} `json:"verify"`
	Parse []struct {
		Name    string  `json:"name"`
		RawBody string  `json:"rawBody"`
		Type    int64   `json:"type"`
		Schema  *string `json:"schema"`
		Known   bool    `json:"known"`
	} `json:"parse"`
}

func loadWebhookVectors(t *testing.T) webhookVectors {
	t.Helper()
	b, err := os.ReadFile(filepath.Join("..", "shared", "test-vectors", "webhooks.json"))
	if err != nil {
		t.Fatal(err)
	}
	var v webhookVectors
	if err := json.Unmarshal(b, &v); err != nil {
		t.Fatal(err)
	}
	return v
}

func TestWebhookVerifyVectors(t *testing.T) {
	for _, c := range loadWebhookVectors(t).Verify {
		got := Webhooks.Verify(WebhookVerifyOptions{AppKey: c.AppKey, AppSecret: c.AppSecret, RawBody: []byte(c.RawBody), Signature: c.Signature})
		if got != c.Valid {
			t.Errorf("%s: got %v", c.Name, got)
		}
	}
}

func TestWebhookParseVectors(t *testing.T) {
	for _, c := range loadWebhookVectors(t).Parse {
		ev, err := Webhooks.Parse([]byte(c.RawBody))
		if err != nil {
			t.Fatalf("%s: %v", c.Name, err)
		}
		if ev.WebhookType() != int(c.Type) {
			t.Errorf("%s: type %d", c.Name, ev.WebhookType())
		}
		if !c.Known {
			u, ok := ev.(UnknownWebhookEvent)
			if !ok || u.Type != c.Type || u.Raw["type"] == nil {
				t.Errorf("%s: %#v", c.Name, ev)
			}
			continue
		}
		if name := reflect.TypeOf(ev).Elem().Name(); name != *c.Schema {
			t.Errorf("%s: %s want %s", c.Name, name, *c.Schema)
		}
	}
}

func TestParseReturnsTypedModelForTypeSwitch(t *testing.T) {
	ev, err := Webhooks.Parse([]byte(`{"type":1,"tts_notification_id":"n","shop_id":"7495540735365777507","timestamp":5,"data":{"order_id":"576653688135258178","order_status":"UNPAID"}}`))
	if err != nil {
		t.Fatal(err)
	}
	switch e := ev.(type) {
	case *generated.OrderStatusChangeWebhook:
		if e.GetShopId() != "7495540735365777507" || e.Data.GetOrderId() != "576653688135258178" {
			t.Errorf("%+v", e)
		}
	default:
		t.Fatalf("%T", ev)
	}
}

func TestNineteenDigitShopIDKeepsEveryDigit(t *testing.T) {
	ev, err := Webhooks.Parse([]byte(`{"type":1,"shop_id":7494049642642441621,"data":{"order_id":576653688135258178}}`))
	if err != nil {
		t.Fatal(err)
	}
	e := ev.(*generated.OrderStatusChangeWebhook)
	if e.GetShopId() != "7494049642642441621" || e.Data.GetOrderId() != "576653688135258178" {
		t.Errorf("%s %s", e.GetShopId(), e.Data.GetOrderId())
	}
	unk, err := Webhooks.Parse([]byte(`{"type":424242,"shop_id":7494049642642441621,"n":1.50}`))
	if err != nil {
		t.Fatal(err)
	}
	u := unk.(UnknownWebhookEvent)
	if u.Raw["shop_id"].(json.Number).String() != "7494049642642441621" {
		t.Errorf("%#v", u.Raw["shop_id"])
	}
	if u.Raw["n"].(json.Number).String() != "1.50" {
		t.Errorf("%#v", u.Raw["n"])
	}
}

func TestParseRejectsMissingOrNonIntegerType(t *testing.T) {
	for name, body := range map[string]string{
		"missing":      `{"shop_id":"1"}`,
		"string":       `{"type":"1"}`,
		"bool":         `{"type":true}`,
		"null":         `{"type":null}`,
		"float":        `{"type":1.5}`,
		"float whole":  `{"type":1.0}`,
		"exponent":     `{"type":1e0}`,
		"not object":   `[1]`,
		"not json":     `nope`,
		"empty":        ``,
		"trailing":     `{"type":1}{"type":2}`,
		"known no req": `{"type":1,"data":"x"}`,
	} {
		ev, err := Webhooks.Parse([]byte(body))
		if err == nil || ev != nil {
			t.Errorf("%s: want error, got %#v %v", name, ev, err)
		}
	}
}

func TestParseToleratesFieldsTheModelDoesNotKnow(t *testing.T) {
	ev, err := Webhooks.Parse([]byte(`{"type":1,"shop_id":"9","brand_new_field":{"a":1},"data":{"order_id":"1","extra":2}}`))
	if err != nil {
		t.Fatal(err)
	}
	e := ev.(*generated.OrderStatusChangeWebhook)
	if e.Data.GetOrderId() != "1" || e.GetShopId() != "9" || e.AdditionalProperties["brand_new_field"] == nil || e.Data.AdditionalProperties["extra"] == nil {
		t.Errorf("%+v", e)
	}
}

func TestVerifyAndParse(t *testing.T) {
	v := loadWebhookVectors(t).Verify
	good, bad := v[0], v[1]
	ev, err := Webhooks.VerifyAndParse(WebhookVerifyOptions{AppKey: good.AppKey, AppSecret: good.AppSecret, RawBody: []byte(good.RawBody), Signature: good.Signature})
	if err != nil || ev.WebhookType() != 1 {
		t.Fatalf("%v %v", ev, err)
	}
	_, err = Webhooks.VerifyAndParse(WebhookVerifyOptions{AppKey: bad.AppKey, AppSecret: bad.AppSecret, RawBody: []byte(bad.RawBody), Signature: bad.Signature})
	var se *WebhookSignatureError
	if !errors.As(err, &se) || !errors.Is(err, ErrWebhookSignature) {
		t.Errorf("%v", err)
	}
}

func TestEventTypesAndDispatchCoverMeta(t *testing.T) {
	if len(EventTypes) != 16 || EventTypes[1] != "ORDER_STATUS_CHANGE" {
		t.Errorf("%d %q", len(EventTypes), EventTypes[1])
	}
	if len(generated.Webhooks) != 44 {
		t.Fatalf("%d webhooks", len(generated.Webhooks))
	}
	for _, w := range generated.Webhooks {
		m := generated.NewWebhookModel(w.Type)
		if m == nil || reflect.TypeOf(m).Elem().Name() != w.Schema || m.WebhookType() != w.Type {
			t.Errorf("type %d: %T", w.Type, m)
		}
		var _ WebhookEvent = m
		// Every model is reachable through Parse: the only acceptable failure is a missing required field.
		if _, err := Webhooks.Parse([]byte(`{"type":` + itoa(w.Type) + `}`)); err != nil && !strings.Contains(err.Error(), "no value given for required property") {
			t.Errorf("%s: %v", w.Schema, err)
		}
	}
	if generated.NewWebhookModel(9999) != nil {
		t.Error("unknown type must give nil")
	}
}

func itoa(i int) string { b, _ := json.Marshal(i); return string(b) }
