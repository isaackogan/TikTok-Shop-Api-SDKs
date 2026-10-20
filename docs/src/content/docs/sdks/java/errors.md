---
title: Errors
description: TikTokShopException, ApiException, and how each kind of failure is reported by the Java SDK, for sync and async calls.
sidebar:
  order: 5
---

Every failed call raises the unchecked `TikTokShopException`, with `getCode()`, `getMessage()`, `getRequestId()`, `getHttpStatus()` and the original exception as `getCause()`. The same rules apply in all eight SDKs; see [errors](/getting-started/errors/).

| What happened | `getCode()` | `getHttpStatus()` |
|---|---|---|
| TikTok's reply has a non-zero `code`, even on HTTP 200 | TikTok's code | the status |
| A non-2xx reply | TikTok's non-zero code if the body has one, else the HTTP status | the status |
| A 2xx reply that can't be read: not a JSON object, a `code` that isn't an integer, a body that doesn't fit its model, or a token reply without `data` | -1 | the status |
| No HTTP response at all: connection refused, DNS, TLS, or a timeout | -1 | `null` |

`getHttpStatus()` returns an `Integer`, so it is `null` when no reply arrived. `getRequestId()` is an empty string when the reply had none.

## TikTokShopException and ApiException

Two exception types are involved, because the API classes are generated and the SDK's error type is not.

- **`TikTokShopException`** is the SDK's. A synchronous call such as `client.orders().getOrderList(...)` throws it for every failure in the table above.
- **`ApiException`** is the generated code's checked exception, so every generated method declares it. It can still surface for client-side problems such as a missing required parameter. Catch or declare both.

The `*Async` methods never throw these to the caller. They report every failure to `ApiCallback.onFailure` as an `ApiException`. When the cause is a `TikTokShopException`, it is that `ApiException`'s `getCause()`, and the `ApiException`'s `getCode()` is the HTTP status, 0 when no response arrived. Read the SDK's code, request ID and status from the cause.

## Notes

- **Look up TikTok's code.** Each operation's error codes are listed in the [API reference](/openapi/reference/) (`x-tts-error-codes` in the spec).
- **Keep the `requestId`.** TikTok's support asks for it.
- **Redirects are errors.** With the default HTTP client, a 3xx reply is a `TikTokShopException` carrying the status, and the client does not follow it. Token calls never follow redirects, even on an `httpClient` you supply.
- **Secrets stay out of errors.** The message never contains the request URL or its query, and token calls never put the app secret, the authorization code or the refresh token in it.
