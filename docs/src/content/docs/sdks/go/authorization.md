---
title: Authorization
description: Build TikTok Shop authorization URLs and exchange and refresh tokens with the Go Auth helper.
sidebar:
  order: 2
---

`tiktokshop.NewAuth` returns an `Auth` helper. It builds the URL a seller, partner or creator opens to authorize your app, and calls TikTok's token endpoints. See [authorization](/getting-started/authorization/) for the flow itself.

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

`Type` is `AuthSeller`, `AuthPartner` or `AuthCreator`; `Region` is `RegionUS` or `RegionROW`. `NewAuth` never fails and does no I/O. `AuthorizationURL` returns an error for an unknown type or region, or for a seller or partner URL without a `ServiceID`.

## Options

| Option | Meaning |
| --- | --- |
| `AppKey`, `AppSecret` | Your app's credentials from Partner Center. |
| `ServiceID` | Your Partner Center service ID. Required for `AuthSeller` and `AuthPartner` authorization URLs; `AuthCreator` URLs use the app key instead. |
| `BaseURL` | Token endpoint host, an origin with no path prefix. Defaults to `DefaultAuthBaseURL`, `https://auth.tiktok-shops.com`. |
| `Timeout` | Bounds one token request. 0 means `DefaultTimeout` (30 seconds); a negative value means no limit. |
| `Transport` | An `http.RoundTripper` override, defaulting to `http.DefaultTransport`. The client the SDK builds around it never follows a redirect, so the app secret and the code are never forwarded to another host. A `Transport` you supply is used as it is. |

`AuthorizationURL` omits an empty `State`, the same as an absent one.

## Tokens

`ExchangeCode` and `Refresh` take a `context.Context` and return a `*TokenSet`:

| Field | Meaning |
| --- | --- |
| `AccessToken`, `RefreshToken` | The tokens. Send the access token with API calls; trade the refresh token for a new pair. |
| `AccessTokenExpireIn`, `RefreshTokenExpireIn` | Unix times in seconds (`int64`) at which each token expires. They are moments, not durations. |
| `OpenID`, `SellerName`, `SellerBaseRegion`, `UserType`, `GrantedScopes` | Optional. Creator and partner tokens may lack the seller fields. An absent field is the zero value: an empty string, `0` or a nil slice. |

A non-zero `code` in TikTok's response returns a `*tiktokshop.Error` with `Code`, `Message` and `RequestID`, and so does a token reply without `data`. See [errors](/sdks/go/errors/).

## Storing tokens

`TokenSet.String` and `GoString` print the set without its tokens, so `fmt` and `%#v` don't leak them. `json.Marshal` is unchanged, so you can still serialize a set to store it. Protect wherever you store it.

`Options` and `AuthOptions` hide the app secret the same way when formatted directly. Keep them out of structs you log: `fmt` reflects into struct fields without calling their `String` method.
