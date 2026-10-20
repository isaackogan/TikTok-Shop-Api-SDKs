---
title: Errors
description: The Go *tiktokshop.Error, its Code and HTTPStatus, and how each kind of failure is reported.
sidebar:
  order: 5
---

Every failure of a call that was sent is a `*tiktokshop.Error`, with `Code`, `Message`, `RequestID`, `HTTPStatus` and the original error as `Cause`. Use `errors.As`. The same rules apply in all eight SDKs; see [errors](/getting-started/errors/).

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

`HTTPStatus` is 0, not unset, when no response arrived. `Cause` holds the original error (the decoder's error, or the network error), so `errors.Is(err, context.DeadlineExceeded)` works.

- **Look up TikTok's code.** Each operation's error codes are listed in the [API reference](/openapi/reference/) (`x-tts-error-codes` in the spec).
- **Keep the `RequestID`.** TikTok's support asks for it. It is empty when the reply had none.
- **Redirects are errors.** With the default transport, a 3xx reply is an error whose `Code` and `HTTPStatus` are the status, and the client does not follow it.
- **Secrets stay out of errors.** Token calls never put the app secret, the authorization code or the refresh token in the error; the request URL is stripped from their network errors, because its query holds them.
