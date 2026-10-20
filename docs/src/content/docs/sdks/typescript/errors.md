---
title: Errors
description: TikTokShopError, its code and httpStatus, and how each kind of failure is reported in the TypeScript SDK.
sidebar:
  order: 5
---

Every failed call throws `TikTokShopError`, with `code`, `message`, `requestId`, `httpStatus` and the original error as `cause`. The same rules apply in all eight SDKs; see [errors](/getting-started/errors/).

| What happened | `code` | `httpStatus` |
|---|---|---|
| TikTok's reply has a non-zero `code`, even on HTTP 200 | TikTok's code | the status |
| A non-2xx reply | TikTok's non-zero code if the body has one, else the HTTP status | the status |
| A 2xx reply that can't be read: not a JSON object, a `code` that isn't an integer, a body that doesn't fit its model, or a token reply without `data` | -1 | the status |
| No HTTP response at all: connection refused, DNS, TLS, or a timeout | -1 | unset |

- **Look up TikTok's code.** Each operation's error codes are listed in the [API reference](/openapi/reference/) (`x-tts-error-codes` in the spec).
- **Keep the `requestId`.** TikTok's support asks for it.
- **Redirects are errors.** With the default `fetch`, a 3xx reply is an error whose `code` and `httpStatus` are the status, and the client does not follow it.
- **Secrets stay out of errors.** Token calls never put the app secret, the authorization code or the refresh token in the error message.
