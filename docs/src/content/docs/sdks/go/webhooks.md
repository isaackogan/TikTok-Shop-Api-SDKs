---
title: Webhooks
description: Verify TikTok Shop webhook signatures and parse typed webhook events in Go.
sidebar:
  order: 4
---

`Webhooks.VerifyAndParse` checks the signature (HMAC-SHA256 over the app key plus the raw body) and returns a typed event. See [webhooks](/getting-started/webhooks/) for how TikTok signs and delivers them. Type-switch on the result; each case is a generated model.

```go
import (
	"errors"
	"io"
	"log"
	"net/http"

	tiktokshop "github.com/isaackogan/TikTok-Shop-Api-SDKs/go"
	"github.com/isaackogan/TikTok-Shop-Api-SDKs/go/generated"
)

func webhookHandler(w http.ResponseWriter, r *http.Request) {
	body, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "read failed", http.StatusBadRequest)
		return
	}

	event, err := tiktokshop.Webhooks.VerifyAndParse(tiktokshop.WebhookVerifyOptions{
		AppKey:    "APP_KEY",
		AppSecret: "APP_SECRET",
		RawBody:   body,
		Signature: r.Header.Get("Authorization"),
	})
	if errors.Is(err, tiktokshop.ErrWebhookSignature) {
		http.Error(w, "bad signature", http.StatusUnauthorized)
		return
	}
	if err != nil {
		http.Error(w, "bad webhook", http.StatusBadRequest)
		return
	}

	switch e := event.(type) {
	case *generated.OrderStatusChangeWebhook:
		log.Println("order", e.Data.GetOrderId(), "is now", e.Data.GetOrderStatus(), "in shop", e.GetShopId())
	case *generated.ReturnStatusChangeWebhook:
		log.Println("return", e.Data.GetReturnId())
	case tiktokshop.UnknownWebhookEvent:
		log.Println("unhandled webhook type", e.Type)
	}
	w.WriteHeader(http.StatusOK)
}
```

## Rules

- **Verify the raw body.** Pass the body exactly as received. Never re-serialize it: changed whitespace or key order makes the signature fail.
- **Parsing is strict.** `VerifyAndParse` returns an error when the body is not a JSON object, `type` is missing or is not an integer, or a known type is missing a required field or has it null. A known type missing a required field is a parse error.
- **Unknown types are kept.** A type this SDK does not know comes back as `tiktokshop.UnknownWebhookEvent`, with `Type` and the decoded body in `Raw`. Known events are pointers to the generated models.
- **Type names.** `tiktokshop.EventTypes` maps a type number to its name; `1` is `ORDER_STATUS_CHANGE`.
- **IDs keep every digit.** IDs such as `shop_id` are exact whether TikTok sends them as strings or as JSON numbers.

A bad signature returns `ErrWebhookSignature`; match it with `errors.Is`, or with `errors.As` on `*tiktokshop.WebhookSignatureError`. Answer it with 401 and any other error with 400, so neither is mistaken for success. A parse failure is a plain error, not a `*tiktokshop.Error`. `Webhooks.Verify` returns a plain `bool` if you want to check the signature without parsing.
