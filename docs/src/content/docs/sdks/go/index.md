---
title: Go SDK
description: Install the TikTok Shop API client for Go, the tiktokshop package, and make your first call.
sidebar:
  label: Overview
  order: 1
---

The `tiktokshop` package is a typed Go client for the TikTok Shop Partner API. It signs requests, handles OAuth, works with many shops at once, and verifies and types webhooks. It is published as a Go module on [pkg.go.dev](https://pkg.go.dev/github.com/isaackogan/TikTok-Shop-Api-SDKs/go), and its source is in [`go/`](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/go).

## Install

```sh
go get github.com/isaackogan/TikTok-Shop-Api-SDKs/go
```

Requires Go 1.22 or newer. The package name is `tiktokshop`. It has no dependencies beyond the standard library and the generated code's validator.

## First call

With an access token from the [OAuth helper](/sdks/go/authorization/), create a client and call an operation. Each operation is a request builder: set the parameters, then call `Execute`.

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

Every call is signed, timestamped and sent with your access token. The `shop_cipher` query parameter is added for you on the endpoints that need it.

## In this section

- [Authorization](/sdks/go/authorization/): `NewAuth`, authorization URLs, token exchange and refresh.
- [Calling the API](/sdks/go/calling-the-api/): the client, API areas, many shops and options.
- [Webhooks](/sdks/go/webhooks/): `Webhooks.VerifyAndParse` and typed events.
- [Errors](/sdks/go/errors/): `*tiktokshop.Error` and its codes.
