---
title: Calling the API
description: Create the Go TikTokShop client, call operations by API area, and work with many shops using WithShop.
sidebar:
  order: 3
---

`tiktokshop.New` returns the API client, a `*TikTokShop`. It never fails and does no I/O. Each request it sends gets the following automatically:
- the `app_key`, `timestamp` and `sign` query parameters;
- your access token, in the `x-tts-access-token` header;
- `shop_cipher`, on the operations that need one.

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

## API areas

One field per API area hangs off the client, matching the spec's tags. Each holds the generated service for that area:

| Field | Area |
| --- | --- |
| `AffiliateCreator`, `AffiliatePartner`, `AffiliateSeller` | Affiliate creator, partner and seller |
| `Analytics` | Analytics |
| `Authorization` | Authorization, including `GetAuthorizedShops` |
| `CustomerEngagement`, `CustomerService` | Customer engagement and customer service |
| `Event` | Event (webhook subscriptions) |
| `Finance` | Finance |
| `FulfilledByTikTok` | Fulfilled by TikTok (FBT) |
| `Fulfillment`, `Logistics` | Fulfillment and logistics |
| `Orders`, `Products`, `Promotion` | Orders, products and promotion |
| `ReturnAndRefund` | Return and refund |
| `Seller`, `SupplyChain`, `Tools` | Seller, supply chain and tools |

Each operation is a method that takes a `context.Context` and returns a request builder. Set parameters on the builder, such as `PageSize(20)`, then call `Execute()` to send the request. It returns the typed response, the `*http.Response` and an error. Names follow the [API reference](/openapi/reference/), in Pascal case.

An operation whose optional request body you leave unset sends no body at all.

## Many shops

`WithShop` returns a client for another shop that shares the HTTP transport, base URL and timeout. A value you leave out keeps this client's value; passing it empty clears it. The original is never changed.

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

## Options

| Option | Meaning |
| --- | --- |
| `AppKey`, `AppSecret` | Your app's credentials. |
| `AccessToken` | The seller's access token, sent in `x-tts-access-token`. Empty sends none. |
| `ShopCipher` | The shop cipher added to operations that need one. Empty adds none. |
| `BaseURL` | The API host, an origin such as `https://host:8443` with no path prefix: signing and shop-cipher matching use the request path. Defaults to `DefaultBaseURL`, `https://open-api.tiktokglobalshop.com`. |
| `Timeout` | Bounds one request, response body included. 0 means `DefaultTimeout` (30 seconds); a negative value means no limit. |
| `Transport` | An `http.RoundTripper` carrying the signed requests. nil means `http.DefaultTransport`, which honours the proxy environment variables (`HTTP_PROXY`, `HTTPS_PROXY`). |

The client the SDK builds around the transport never follows a redirect. A 3xx reply is returned as a `*tiktokshop.Error` carrying the status, so the access token is never forwarded to another host. A `Transport` you supply is used as it is.

Query values are signed decoded, exactly as the server receives them. A request body is sent as is on any method, GET included.

Requests carry the User-Agent `tiktok-shop-api-go/<version>`. `Options.String` describes the options without the app secret, the access token or the shop cipher.
