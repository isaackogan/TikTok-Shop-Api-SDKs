# TikTok Shop API client for Go

A typed Go client for the **TikTok Shop API** (the TikTok Shop Partner API): over 300 operations across 19 API groups, request signing, OAuth token helpers and typed webhooks. The API methods are generated from a machine-readable OpenAPI v3 spec built from TikTok's partner documentation, so they track the docs.

Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.

> Request signing follows TikTok's documentation and has not been verified against the live API. If TikTok rejects a signature, please open an issue at https://github.com/isaackogan/TikTok-Shop-Api-SDKs/issues. The OpenAPI spec this client is generated from is published at <https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/.openapi/tiktok-shop.openapi.yaml>.

## Install

Requires Go 1.22 or newer.

```sh
go get github.com/isaackogan/TikTok-Shop-Api-SDKs/go
```

The package name is `tiktokshop`. It has no dependencies beyond the standard library and the generated code's validator.

## Authorize a shop (OAuth)

Send the seller to the authorization URL. TikTok redirects back to your app with a `code`, which you trade for an access token. Refresh before the access token expires.

```go
import (
	"context"
	"fmt"

	tiktokshop "github.com/isaackogan/TikTok-Shop-Api-SDKs/go"
)

func authorize(ctx context.Context) error {
	auth := tiktokshop.NewAuth(tiktokshop.AuthOptions{
		AppKey:    "APP_KEY",
		AppSecret: "APP_SECRET",
		ServiceID: "SERVICE_ID",
	})

	url, err := auth.AuthorizationURL(tiktokshop.AuthorizationURLOptions{
		Type:   tiktokshop.AuthSeller,
		Region: tiktokshop.RegionUS,
		State:  "my-csrf-token",
	})
	if err != nil {
		return err
	}
	fmt.Println("send the seller to", url)

	tokens, err := auth.ExchangeCode(ctx, "CODE_FROM_THE_REDIRECT")
	if err != nil {
		return err
	}
	fmt.Println(tokens.AccessToken, tokens.OpenID, tokens.GrantedScopes)

	tokens, err = auth.Refresh(ctx, tokens.RefreshToken)
	if err != nil {
		return err
	}
	fmt.Println("expires at", tokens.AccessTokenExpireIn)
	return nil
}
```

## Make a call

Every API group is a field of the client (`Orders`, `Products`, `Fulfillment`, `Finance`, ...) holding the generated service. Signing, `app_key`, `timestamp`, the `x-tts-access-token` header and `shop_cipher` are added for you.

```go
import (
	"context"
	"fmt"

	tiktokshop "github.com/isaackogan/TikTok-Shop-Api-SDKs/go"
)

func listOrders(ctx context.Context) error {
	client := tiktokshop.New(tiktokshop.Options{
		AppKey:      "APP_KEY",
		AppSecret:   "APP_SECRET",
		AccessToken: "ACCESS_TOKEN",
		ShopCipher:  "SHOP_CIPHER",
	})

	orders, _, err := client.Orders.GetOrderList(ctx).PageSize(20).Execute()
	if err != nil {
		return err
	}
	data := orders.GetData()
	fmt.Println(data.GetTotalCount(), "orders; request", orders.GetRequestId())
	return nil
}
```

Every failure of a call that was sent is a `*tiktokshop.Error`. Use `errors.As`:

```go
import (
	"context"
	"errors"
	"fmt"

	tiktokshop "github.com/isaackogan/TikTok-Shop-Api-SDKs/go"
)

func handleErrors(ctx context.Context, client *tiktokshop.TikTokShop) {
	_, _, err := client.Orders.GetOrderList(ctx).Execute()

	var apiErr *tiktokshop.Error
	if errors.As(err, &apiErr) {
		fmt.Println(apiErr.Code, apiErr.Message, apiErr.RequestID, apiErr.HTTPStatus)
	}
}
```

| What happened | `Code` | `HTTPStatus` |
|---|---|---|
| TikTok's reply has a non-zero `code`, even on HTTP 200 | TikTok's code | the status |
| A non-2xx reply | TikTok's non-zero code if the body has one, else the HTTP status | the status |
| A 2xx reply that can't be read: not a JSON object, a `code` that isn't an integer, a body that doesn't decode into its model, or a token reply without `data` | -1 | the status |
| No HTTP response at all: connection refused, DNS, TLS, or a timeout | -1 | 0 |

`Cause` holds the original error (the decoder's error, or the network error), so `errors.Is(err, context.DeadlineExceeded)` works.

## Several shops: `WithShop`

`WithShop` returns a client for another shop that shares the HTTP transport. A value you leave out keeps this client's value; passing it empty clears it. The original is never changed.

```go
import (
	tiktokshop "github.com/isaackogan/TikTok-Shop-Api-SDKs/go"
)

func otherShop(client *tiktokshop.TikTokShop) *tiktokshop.TikTokShop {
	return client.WithShop(
		tiktokshop.ShopAccessToken("OTHER_ACCESS_TOKEN"),
		tiktokshop.ShopCipher("OTHER_SHOP_CIPHER"),
	)
}
```

## Webhooks

`Webhooks.VerifyAndParse` checks the signature (HMAC-SHA256 over the app key plus the raw body) and returns a typed event. Pass the body exactly as received: never re-serialize it. Type-switch on the result; each case is a generated model. A type this SDK does not know comes back as `tiktokshop.UnknownWebhookEvent`.

Parsing is strict: a body that is not a JSON object, a `type` that is missing or not an integer, or a known type with a required field missing or null is an error. In short, a known type missing a required field is a parse error.

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

IDs such as `shop_id` keep every digit whether TikTok sends them as strings or as JSON numbers. `tiktokshop.EventTypes` maps a webhook type to its event name (`1` is `ORDER_STATUS_CHANGE`).

## Notes

- Query values are signed decoded, exactly as the server receives them.
- Honours `HTTP_PROXY`/`HTTPS_PROXY` through `http.DefaultTransport` unless you pass your own `Transport`.
- `Options.BaseURL` and `AuthOptions.BaseURL` can point at a test server. Either must be an origin such as `https://host:8443`, with no path prefix: signing and shop-cipher matching use the request path.
- `Options.Timeout` and `AuthOptions.Timeout` bound one request, response body included. 0 means `DefaultTimeout` (30 seconds); a negative value means no limit.
- Requests carry the User-Agent `tiktok-shop-api-go/<version>`.
- An operation whose optional request body you leave unset sends no body at all.

## License

MIT. See [LICENSE](LICENSE).
