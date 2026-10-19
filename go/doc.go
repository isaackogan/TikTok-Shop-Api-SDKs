// Package tiktokshop is an unofficial Go client for the TikTok Shop API (TikTok Shop Partner API).
//
// Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.
//
// The API methods are generated from the OpenAPI spec into the generated package and exposed as one
// field per API group of [TikTokShop]. This package adds request signing, the shop cipher, the access
// token header and error handling around them.
//
// # Errors
//
// Every failure is a [*Error], whatever its class, and is returned by the generated call's Execute
// method wrapped by net/http in a [*url.Error]. Use errors.As:
//
//	var e *tiktokshop.Error
//	if errors.As(err, &e) { fmt.Println(e.Code, e.Message, e.RequestID, e.HTTPStatus) }
//
// The classes are: an envelope with code != 0 (even on HTTP 200), a non-2xx response (Code and Message
// come from the body when it has them, otherwise Code is the HTTP status), a 2xx response whose body is
// not JSON, and network errors and timeouts (Cause holds the original error). The generated
// Execute returns a nil *http.Response for all of them; HTTPStatus on the Error replaces it.
package tiktokshop
