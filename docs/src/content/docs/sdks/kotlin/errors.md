---
title: Errors
description: TikTokShopException, its code and httpStatus, and how each kind of failure is reported in the Kotlin SDK.
sidebar:
  order: 5
---

Every failed call throws `TikTokShopException`, with `code`, `message`, `requestId`, `httpStatus` and the original exception as `cause`. The same rules apply in all eight SDKs; see [errors](/getting-started/errors/).

| What happened | `code` | `httpStatus` |
|---|---|---|
| TikTok's reply has a non-zero `code`, even on HTTP 200 | TikTok's code | the status |
| A non-2xx reply | TikTok's non-zero code if the body has one, else the HTTP status | the status |
| A 2xx reply that can't be read: not a JSON object, a `code` that isn't an integer, a body gson can't decode into its model, or a token reply without `data` | -1 | the status |
| No HTTP response at all: connection refused, DNS, TLS, or a timeout | -1 | `null` |

`httpStatus` is an `Int?`, so it is `null` when no reply arrived. `requestId` is an empty string when the reply had none.

- **Look up TikTok's code.** Each operation's error codes are listed in the [API reference](/openapi/reference/) (`x-tts-error-codes` in the spec).
- **Keep the `requestId`.** TikTok's support asks for it.
- **Redirects are errors.** With the default HTTP client, a 3xx reply is a `TikTokShopException` carrying the status, and the client does not follow it. Token requests never follow redirects, even on an `httpClient` you supply.
- **Secrets stay out of errors.** The message never contains the request URL or its query, and token calls never put the app secret, the authorization code or the refresh token in it.
- **Missing response fields.** gson does not check required properties of a response model: one TikTok leaves out arrives as `null` even where the Kotlin type is non-null.
