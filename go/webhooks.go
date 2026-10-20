package tiktokshop

import (
	"bytes"
	"crypto/hmac"
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"io"
	"reflect"
	"sort"
	"strings"

	"github.com/isaackogan/TikTok-Shop-Api-SDKs/go/generated"
)

// WebhookEvent is a parsed webhook: a pointer to one of the generated webhook models (for example
// *generated.OrderStatusChangeWebhook) or an [UnknownWebhookEvent]. Type-switch on it.
type WebhookEvent interface {
	// WebhookType is the integer `type` of the webhook.
	WebhookType() int
}

// UnknownWebhookEvent is a webhook whose type this SDK does not know. Raw is the decoded body; its
// numbers are json.Number, so 64-bit IDs keep every digit.
type UnknownWebhookEvent struct {
	Type int64
	Raw  map[string]any
}

// WebhookType returns Type.
func (u UnknownWebhookEvent) WebhookType() int { return int(u.Type) }

// WebhookSignatureError means a webhook's signature does not match its body.
type WebhookSignatureError struct{}

func (*WebhookSignatureError) Error() string { return "tiktokshop: webhook signature does not match" }

// ErrWebhookSignature is what [Webhooks.VerifyAndParse] returns on a mismatch; errors.Is and errors.As
// (with *WebhookSignatureError) both match it.
var ErrWebhookSignature error = &WebhookSignatureError{}

// EventTypes maps a webhook type to its event name, e.g. 1 -> "ORDER_STATUS_CHANGE".
var EventTypes = func() map[int]string {
	m := make(map[int]string, len(generated.EventTypes))
	for k, v := range generated.EventTypes {
		m[k] = v
	}
	return m
}()

// WebhookVerifyOptions are the inputs of [Webhooks.Verify] and [Webhooks.VerifyAndParse].
type WebhookVerifyOptions struct {
	AppKey    string
	AppSecret string
	// RawBody is the body exactly as received. Never re-serialize it.
	RawBody []byte
	// Signature is the Authorization header value.
	Signature string
}

type webhooks struct{}

// Webhooks verifies and parses TikTok Shop webhook deliveries.
var Webhooks webhooks

// Verify reports whether Signature is the lowercase hex HMAC-SHA256 (key AppSecret) of AppKey + RawBody.
func (webhooks) Verify(o WebhookVerifyOptions) bool {
	if o.Signature == "" {
		return false
	}
	mac := hmac.New(sha256.New, []byte(o.AppSecret))
	mac.Write([]byte(o.AppKey))
	mac.Write(o.RawBody)
	expected := []byte(hex.EncodeToString(mac.Sum(nil)))
	// hmac.Equal is constant time and false for different lengths.
	return hmac.Equal(expected, []byte(o.Signature))
}

// Parse decodes a body into the generated model for its integer `type`. An unknown type returns an
// [UnknownWebhookEvent]. Parsing is strict: a body that is not a JSON object, has no integer `type`, or does not
// fit its model is an error, and so is a known type with a required field missing or null at any depth. 64-bit IDs keep every digit even when TikTok sends them as JSON numbers; fields a
// model does not know are kept in its AdditionalProperties.
func (webhooks) Parse(rawBody []byte) (WebhookEvent, error) {
	dec := json.NewDecoder(bytes.NewReader(rawBody))
	dec.UseNumber()
	var v any
	if err := dec.Decode(&v); err != nil {
		return nil, fmt.Errorf("tiktokshop: webhook body is not JSON: %w", err)
	}
	if _, err := dec.Token(); err != io.EOF {
		return nil, fmt.Errorf("tiktokshop: webhook body has trailing data")
	}
	body, ok := v.(map[string]any)
	if !ok {
		return nil, fmt.Errorf("tiktokshop: webhook body is not a JSON object")
	}
	n, ok := body["type"].(json.Number)
	if !ok {
		return nil, fmt.Errorf("tiktokshop: webhook body has no integer \"type\"")
	}
	t, err := n.Int64()
	if err != nil {
		return nil, fmt.Errorf("tiktokshop: webhook body has no integer \"type\": %q", n.String())
	}
	var model generated.WebhookModel
	if int64(int(t)) == t {
		model = generated.NewWebhookModel(int(t))
	}
	if model == nil {
		return UnknownWebhookEvent{Type: t, Raw: body}, nil
	}
	// R28: the generated models decode a JSON null in a required field to its zero value, so check first.
	if missing := firstMissing(webhookSchemas[int(t)], body, ""); missing != "" {
		return nil, fmt.Errorf("tiktokshop: webhook type %d does not match %T: required field %q is missing or null", t, model, missing)
	}
	fixed, err := json.Marshal(fit(body, reflect.TypeOf(model).Elem()))
	if err == nil {
		err = json.Unmarshal(fixed, model)
	}
	if err != nil {
		return nil, fmt.Errorf("tiktokshop: webhook type %d does not match %T: %w", t, model, err)
	}
	return model, nil
}

// webhookSchemas maps a webhook type to its schema name.
var webhookSchemas = func() map[int]string {
	m := make(map[int]string, len(generated.Webhooks))
	for _, w := range generated.Webhooks {
		m[w.Type] = w.Schema
	}
	return m
}()

// firstMissing returns the first required property (a dotted path) that is missing or null in a model's JSON,
// checking the models it holds directly, in lists and in maps. Values of an unexpected shape are left to the decoder.
func firstMissing(schema string, obj map[string]any, path string) string {
	m, ok := generated.WebhookRequiredFields[schema]
	if !ok {
		return ""
	}
	for _, name := range m.Required {
		if v, found := obj[name]; !found || v == nil {
			return path + name
		}
	}
	names := make([]string, 0, len(m.Children))
	for name := range m.Children {
		names = append(names, name)
	}
	sort.Strings(names)
	for _, name := range names {
		child := m.Children[name]
		switch v := obj[name].(type) {
		case map[string]any:
			if child.Kind == "object" {
				if found := firstMissing(child.Model, v, path+name+"."); found != "" {
					return found
				}
			} else if child.Kind == "map" {
				keys := make([]string, 0, len(v))
				for k := range v {
					keys = append(keys, k)
				}
				sort.Strings(keys)
				for _, k := range keys {
					if item, ok := v[k].(map[string]any); ok {
						if found := firstMissing(child.Model, item, path+name+"."+k+"."); found != "" {
							return found
						}
					}
				}
			}
		case []any:
			if child.Kind == "list" {
				for i, it := range v {
					if item, ok := it.(map[string]any); ok {
						if found := firstMissing(child.Model, item, fmt.Sprintf("%s%s[%d].", path, name, i)); found != "" {
							return found
						}
					}
				}
			}
		}
	}
	return ""
}

// VerifyAndParse verifies, then parses. It returns [ErrWebhookSignature] on a mismatch.
func (w webhooks) VerifyAndParse(o WebhookVerifyOptions) (WebhookEvent, error) {
	if !w.Verify(o) {
		return nil, ErrWebhookSignature
	}
	return w.Parse(o.RawBody)
}

// fit shapes a decoded body for the generated models: a JSON number where the model has a string
// (TikTok sometimes sends IDs as numbers) becomes that number's exact text. Keys a model does not know
// pass through to its AdditionalProperties.
func fit(v any, t reflect.Type) any {
	for t.Kind() == reflect.Pointer {
		t = t.Elem()
	}
	switch x := v.(type) {
	case json.Number:
		if t.Kind() == reflect.String {
			return x.String()
		}
	case []any:
		if t.Kind() == reflect.Slice || t.Kind() == reflect.Array {
			out := make([]any, len(x))
			for i, e := range x {
				out[i] = fit(e, t.Elem())
			}
			return out
		}
	case map[string]any:
		switch t.Kind() {
		case reflect.Map:
			out := make(map[string]any, len(x))
			for k, e := range x {
				out[k] = fit(e, t.Elem())
			}
			return out
		case reflect.Struct:
			fields := jsonFields(t)
			if len(fields) == 0 {
				return v // not a plain model (e.g. a oneOf wrapper): leave it to its own unmarshaller
			}
			out := make(map[string]any, len(x))
			for k, e := range x {
				if ft, ok := fields[k]; ok {
					out[k] = fit(e, ft)
				} else {
					out[k] = e // unknown to the model: its AdditionalProperties keeps it
				}
			}
			return out
		}
	}
	return v
}

func jsonFields(t reflect.Type) map[string]reflect.Type {
	fields := map[string]reflect.Type{}
	for i := 0; i < t.NumField(); i++ {
		f := t.Field(i)
		name, _, _ := strings.Cut(f.Tag.Get("json"), ",")
		if !f.IsExported() || name == "" || name == "-" {
			continue
		}
		fields[name] = f.Type
	}
	return fields
}
