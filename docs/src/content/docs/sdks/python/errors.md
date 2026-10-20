---
title: Errors
description: TikTokShopError, its code and http_status, and how each kind of failure is reported in the Python SDK.
sidebar:
  order: 5
---

Every failed call raises `TikTokShopError`, with `code`, `message`, `request_id`, `http_status` and the original exception as `__cause__`. The same rules apply in all eight SDKs; see [errors](/getting-started/errors/). The sync and async clients and auth helpers raise the same error.

| What happened | `code` | `http_status` |
|---|---|---|
| TikTok's reply has a non-zero `code`, even on HTTP 200 | TikTok's code | the status |
| A non-2xx reply | TikTok's non-zero code if the body has one, else the HTTP status | the status |
| A 2xx reply that can't be read: not a JSON object, a `code` that isn't an integer, a body that doesn't fit its model, or a token reply without `data` | -1 | the status |
| No HTTP response at all: connection refused, DNS, TLS, or a timeout | -1 | `None` |

- **Look up TikTok's code.** Each operation's error codes are listed in the [API reference](/openapi/reference/) (`x-tts-error-codes` in the spec).
- **Keep the `request_id`.** TikTok's support asks for it. It is an empty string when the reply had none.
- **Redirects are errors.** The token helpers never follow a redirect, so a 3xx reply is an error whose `code` and `http_status` are the status.
- **Secrets stay out of errors and logs.** Token calls never put the app secret, the authorization code or the refresh token in the error message, and a filter on the `httpx` logger replaces them with `***` in INFO request logs.
