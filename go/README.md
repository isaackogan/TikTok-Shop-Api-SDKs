# TikTok Shop API for Go (Unofficial)

[TikTok Shop API](https://partner.tiktokshop.com/) Client for Go (Unofficial, Unaffiliated with TikTok or ByteDance Ltd.)

A typed Go client for the TikTok Shop API, also called the TikTok Shop Partner API or Open API. It covers over 300
operations across 19 API groups: orders, products, fulfillment, logistics, returns and refunds, finance, promotions,
affiliate, analytics, customer service and more, for sellers, partners and creators.

Every request is signed with HMAC-SHA256 and sent with your access token, and the shop cipher is added wherever an
endpoint needs it. The OAuth helper builds the authorization URL and exchanges and refreshes tokens. One client can
serve many shops, and TikTok Shop webhooks are verified and parsed into typed events. The API methods are generated
from a machine-readable OpenAPI v3 spec built from TikTok's partner documentation, so they track the docs.

Full guides, API reference and documentation: <https://ttspa.docs.isaackogan.com/sdks/go/>

The guides cover [Authorization](https://ttspa.docs.isaackogan.com/sdks/go/authorization/), [Calling the API](https://ttspa.docs.isaackogan.com/sdks/go/calling-the-api/),
[Webhooks](https://ttspa.docs.isaackogan.com/sdks/go/webhooks/) and [Errors](https://ttspa.docs.isaackogan.com/sdks/go/errors/), and the [API reference](https://ttspa.docs.isaackogan.com/openapi/reference/) lists every operation and webhook.

[![Go Reference](https://img.shields.io/badge/go-reference-0274b5?style=flat&logo=go&logoColor=white)](https://pkg.go.dev/github.com/isaackogan/TikTok-Shop-Api-SDKs/go)
![Go](https://img.shields.io/github/go-mod/go-version/isaackogan/TikTok-Shop-Api-SDKs?filename=go%2Fgo.mod&style=flat&color=0274b5)
![Stars](https://img.shields.io/github/stars/isaackogan/TikTok-Shop-Api-SDKs?style=flat&color=0274b5)
![Issues](https://img.shields.io/github/issues/isaackogan/TikTok-Shop-Api-SDKs?style=flat&color=0274b5)
![License](https://img.shields.io/github/license/isaackogan/TikTok-Shop-Api-SDKs?style=flat&color=0274b5)

> [!IMPORTANT]
> Request signing follows TikTok's documentation and has not been verified against the live API. If TikTok rejects a signature, please open an issue at https://github.com/isaackogan/TikTok-Shop-Api-SDKs/issues.

> [!TIP]
> The OpenAPI spec this client is generated from is published at
> <https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/.openapi/tiktok-shop.openapi.yaml>.
> Point any OpenAPI 3.1 tool at it.

### Do you prefer other programming languages?

- [TikTok Shop API for TypeScript](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/typescript), `tiktok-shop-api` on npm
- [TikTok Shop API for Python](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/python), `tiktok-shop-api` on PyPI
- [TikTok Shop API for Java](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/java), `com.isaackogan:tiktok-shop-api` on Maven Central
- [TikTok Shop API for Kotlin](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/kotlin), `com.isaackogan:tiktok-shop-api-kotlin` on Maven Central
- [TikTok Shop API for PHP](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/php), `isaackogan/tiktok-shop-api` on Packagist
- [TikTok Shop API for Rust](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/rust), `tiktok-shop-api` on crates.io
- [TikTok Shop API for C# and .NET](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/csharp), `TikTokShop.Api` on NuGet

### Table of Contents

- [Getting Started](#getting-started)
- [Params and Options](#params-and-options)
- [Methods](#methods)
- [Examples](#examples)
- [Frequently Asked Questions](#frequently-asked-questions)
- [Contributors](#contributors)
- [License](#license)

## Getting Started

1. Add the module

```sh
go get github.com/isaackogan/TikTok-Shop-Api-SDKs/go
```

It needs Go 1.22 or newer. The package name is `tiktokshop`. It has no dependencies beyond the standard library and
the generated code's validator.

2. Authorize a shop with OAuth

Send the seller to the authorization URL. TikTok redirects back to your app with a `code`, which you trade for an
access token. Refresh before the access token expires.

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

3. Make your first call

Every API group is a field of the client (`Orders`, `Products`, `Fulfillment`, `Finance`, ...) holding the generated
service. Signing, `app_key`, `timestamp` and the `x-tts-access-token` header are added to every call, and
`shop_cipher` to the operations that take one.

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

## Params and Options

To create a new client, pass a `tiktokshop.Options`.

`tiktokshop.New(tiktokshop.Options{...})`

| Param Name | Required | Description |
|------------|----------|-------------|
| `AppKey` | Yes | Your app key. |
| `AppSecret` | Yes | Your app secret. It signs every request. |
| `AccessToken` | No | The seller's access token, sent as the `x-tts-access-token` header. Empty sends none. |
| `ShopCipher` | No | The shop's cipher, added to the operations that take one. Empty adds none. `Authorization.GetAuthorizedShops` returns it. |
| `BaseURL` | No | Default `tiktokshop.DefaultBaseURL` (`https://open-api.tiktokglobalshop.com`). It can point at a test server, and must be an origin such as `https://host:8443`, with no path prefix: signing and shop-cipher matching use the request path. |
| `Timeout` | No | Bounds one request, response body included. 0 means `DefaultTimeout` (30 seconds); a negative value means no limit. |
| `Transport` | No | The `http.RoundTripper` that carries the signed requests, used as it is. `nil` means `http.DefaultTransport`, which honours `HTTP_PROXY`/`HTTPS_PROXY`. `WithShop` shares it. |

The OAuth helper takes a `tiktokshop.AuthOptions`.

`tiktokshop.NewAuth(tiktokshop.AuthOptions{...})`

| Param Name | Required | Description |
|------------|----------|-------------|
| `AppKey` | Yes | Your app key. |
| `AppSecret` | Yes | Your app secret. |
| `ServiceID` | No | Your Partner Center service ID. `AuthSeller` and `AuthPartner` URLs need it. |
| `BaseURL` | No | Default `tiktokshop.DefaultAuthBaseURL` (`https://auth.tiktok-shops.com`). An origin, with no path prefix. |
| `Timeout` | No | Bounds one token request. 0 means `DefaultTimeout`; a negative value means no limit. |
| `Transport` | No | Carries the token requests. `nil` means `http.DefaultTransport`. |

The HTTP clients the SDK builds around either transport never follow a redirect: a 3xx reply is returned as a
`*tiktokshop.Error` carrying the status, so your credentials are never forwarded to another host. Requests carry the
User-Agent `tiktok-shop-api-go/<version>`. `Options`, `AuthOptions`, `TokenSet` and the clients have `String` and
`GoString` methods that hide their secrets.

## Methods

Each API group is a field of the client: `AffiliateCreator`, `AffiliatePartner`, `AffiliateSeller`, `Analytics`,
`Authorization`, `CustomerEngagement`, `CustomerService`, `Event`, `Finance`, `FulfilledByTikTok`, `Fulfillment`,
`Logistics`, `Orders`, `Products`, `Promotion`, `ReturnAndRefund`, `Seller`, `SupplyChain` and `Tools`. Each holds the
generated service, whose operations build a request you finish with `Execute()`.

| Method Name | Description |
|-------------|-------------|
| `client.WithShop(opts ...ShopOption)` | Returns a client for another shop or token that shares this client's transport, base URL and timeout. Pass `tiktokshop.ShopAccessToken(...)` and `tiktokshop.ShopCipher(...)`. See [Several shops](#several-shops-withshop). |
| `auth.AuthorizationURL(AuthorizationURLOptions)` | Builds the URL to send a seller, partner or creator to. `Type` is `AuthSeller`, `AuthPartner` or `AuthCreator`; `Region` is `RegionUS` or `RegionROW`. |
| `auth.ExchangeCode(ctx, code)` | Trades the `code` from the redirect for a `*TokenSet`. |
| `auth.Refresh(ctx, refreshToken)` | Trades a refresh token for a new `*TokenSet`. |
| `tiktokshop.Webhooks.Verify(WebhookVerifyOptions)` | Reports whether `Signature` is the lowercase hex HMAC-SHA256, keyed with `AppSecret`, of `AppKey` plus `RawBody`. |
| `tiktokshop.Webhooks.Parse(rawBody)` | Parses a body into its generated model, or a `tiktokshop.UnknownWebhookEvent` for a type this SDK does not know. |
| `tiktokshop.Webhooks.VerifyAndParse(WebhookVerifyOptions)` | Verifies, then parses. A bad signature is `tiktokshop.ErrWebhookSignature`. |

A `TokenSet` has `AccessToken`, `AccessTokenExpireIn`, `RefreshToken`, `RefreshTokenExpireIn` (both expiry times are
Unix times in seconds), `OpenID`, `SellerName`, `SellerBaseRegion`, `UserType` and `GrantedScopes`.

## Examples

### Handle errors

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

### Several shops: `WithShop`

`WithShop` returns a client for another shop that shares the HTTP transport. A value you leave out keeps this client's
value; passing it empty clears it. The original is never changed.

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

### Webhooks

`Webhooks.VerifyAndParse` checks the signature (HMAC-SHA256 over the app key plus the raw body) and returns a typed
event. Pass the body exactly as received: never re-serialize it. Type-switch on the result; each case is a generated
model. A type this SDK does not know comes back as `tiktokshop.UnknownWebhookEvent`.

Parsing is strict: a body that is not a JSON object, a `type` that is missing or not an integer, or a known type with a
required field missing or null is an error. In short, a known type missing a required field is a parse error.

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

IDs such as `shop_id` keep every digit whether TikTok sends them as strings or as JSON numbers. `tiktokshop.EventTypes`
maps a webhook type to its event name (`1` is `ORDER_STATUS_CHANGE`).

### Signing and request bodies

- Query values are signed decoded, exactly as the server receives them.
- An operation whose optional request body you leave unset sends no body at all.

## Frequently Asked Questions

### How do I get a TikTok Shop access token in Go?

Create an auth helper with `tiktokshop.NewAuth`, send the seller to `AuthorizationURL`, then trade the `code` TikTok
sends back with `ExchangeCode`. Call `Refresh` before the access token expires. See [Getting Started](#getting-started).

### What is a shop cipher, and where do I find it?

Most TikTok Shop API endpoints act on one shop and need a `shop_cipher` query parameter. Call
`client.Authorization.GetAuthorizedShops` with the seller's access token: each shop in the reply has a cipher. Set it
as `ShopCipher` and the client adds it to every endpoint that needs it.

### How do I verify TikTok Shop webhooks in a Go HTTP handler?

Read the body with `io.ReadAll` and pass it, with the `Authorization` header, to `tiktokshop.Webhooks.VerifyAndParse`.
Don't decode and re-encode the JSON first, because the signature covers the exact bytes. See [Webhooks](#webhooks).

### Can one app manage many TikTok Shop sellers?

Yes. Keep one client per shop with `WithShop`. They share one transport. See
[Several shops](#several-shops-withshop).

### Does it work behind a proxy?

Yes. The default transport is `http.DefaultTransport`, which honours `HTTP_PROXY` and `HTTPS_PROXY`. Pass your own
`Transport` for anything else.

### Which TikTok Shop API versions does it cover?

Every endpoint in TikTok's partner documentation, from API version 202309 onwards, and every documented webhook.

### Is this affiliated with TikTok?

No. It is an independent open-source project, built from TikTok's partner documentation.

### Is this available in other languages?

Yes. See [Do you prefer other programming languages?](#do-you-prefer-other-programming-languages) for the TypeScript,
Python, Java, Kotlin, PHP, Rust and C# SDKs.

## Contributors

* **Isaac Kogan** - *Creator & Maintainer* - [isaackogan](https://github.com/isaackogan)

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/LICENSE) file for details.

Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.
