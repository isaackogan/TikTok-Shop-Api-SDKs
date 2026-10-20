// Package tiktokshop is an unofficial Go client for the TikTok Shop API (TikTok Shop Partner API).
//
// Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.
//
// The API methods are generated from the OpenAPI spec into the generated package and exposed as one
// field per API group of [TikTokShop]. This package adds request signing, the shop cipher, the access
// token header and error handling around them.
//
// # OAuth
//
// [NewAuth] builds authorization URLs ([Auth.AuthorizationURL]) and trades codes and refresh tokens for a
// [TokenSet] ([Auth.ExchangeCode], [Auth.Refresh]).
//
// # Webhooks
//
// [Webhooks].VerifyAndParse checks a delivery's signature and returns a [WebhookEvent]: a pointer to the
// generated model for its type (type-switch on it) or an [UnknownWebhookEvent]. [ErrWebhookSignature] means
// the signature does not match.
//
// Parsing is strict: a body that is not a JSON object, has no integer `type`, or is a known type with a
// required field missing or null is an error. A known type missing a required field is a parse error.
//
// Signing follows TikTok's documentation and has not been verified against the live API. If TikTok rejects a
// signature, please open an issue at https://github.com/isaackogan/TikTok-Shop-Api-SDKs/issues.
//
// # Errors
//
// Every failure of a call that was sent is a [*Error], whatever its class, and is returned by the generated
// call's Execute method wrapped by net/http in a [*url.Error] (a decode failure is returned directly). Use
// errors.As:
//
//	var e *tiktokshop.Error
//	if errors.As(err, &e) { fmt.Println(e.Code, e.Message, e.RequestID, e.HTTPStatus) }
//
// The classes are:
//   - an envelope with code != 0, even on HTTP 200: TikTok's code, HTTPStatus set;
//   - a non-2xx response: TikTok's non-zero code if the body has one, else the HTTP status; HTTPStatus set;
//   - a 2xx response that cannot be understood (not a JSON object, a code that is not an integer, or a body that
//     does not decode into its model): Code -1, HTTPStatus set;
//   - a transport failure with no response at all (connection refused, DNS, TLS, timeout): Code -1, HTTPStatus 0.
//
// Cause holds the original error. The generated Execute returns a nil *http.Response for every class except a
// decode failure; HTTPStatus on the Error replaces it.
package tiktokshop
