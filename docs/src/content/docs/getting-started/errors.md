---
title: Errors
description: How every TikTok Shop API SDK reports API errors, unreadable replies, decode failures and network failures.
sidebar:
  order: 4
---

Each SDK raises one error type for every failed API call and token call. Webhook verification has its own errors; see [webhooks](/getting-started/webhooks/). The error type carries TikTok's `code`, its `message`, its `request_id` and the HTTP status. The code follows the same rules in every language.

| What happened | Code | HTTP status |
|---|---|---|
| TikTok's reply has a non-zero `code`, even on HTTP 200 | TikTok's code | the status |
| A non-2xx reply | TikTok's non-zero code if the body has one, else the HTTP status | the status |
| A 2xx reply that can't be read: not a JSON object, a `code` that isn't an integer, a body that doesn't fit its model, or a token reply without `data` | -1 | the status |
| No HTTP response at all: connection refused, DNS, TLS, or a timeout | -1 | none |

TikTok returns HTTP 200 for many errors, with a non-zero `code` in the body. A 200 reply is therefore not proof of success; the SDKs check `code` for you.

## By language

| SDK | Error type | Fields |
| --- | --- | --- |
| TypeScript | `TikTokShopError` | `code`, `message`, `requestId`, `httpStatus` (unset with no response), `cause` |
| Python | `TikTokShopError` | `code`, `message`, `request_id`, `http_status` (`None` with no response) |
| Go | `*tiktokshop.Error`, matched with `errors.As` | `Code`, `Message`, `RequestID`, `HTTPStatus` (0 with no response), `Cause` |
| Java | `TikTokShopException` (unchecked) | `getCode()`, `getMessage()`, `getRequestId()`, `getHttpStatus()` (`null` with no response), `getCause()` |
| Kotlin | `TikTokShopException` | `code`, `message`, `requestId`, `httpStatus` (`null` with no response) |
| PHP | `TikTokShopException` | `getTikTokCode()` (also `getCode()`), `getMessage()`, `getRequestId()`, `getHttpStatus()` (`null` with no response) |
| Rust | `tiktok_shop_api::Error` | `Error::Api { code, message, request_id, http_status }`, with `Error::Decode`, `Error::Timeout` and `Error::Http` for the last two rows |
| C# | `TikTokShopException` | `Code`, `Message`, `RequestId`, `HttpStatus` (`null` with no response) |

Each SDK's errors page has the details, including errors the generated code raises before a request is sent, such as a missing required parameter.

## Working with errors

- **Look up the code.** Each operation's documented error codes are in the [API reference](/openapi/reference/) (`x-tts-error-codes` in the spec).
- **Keep the request ID.** TikTok's support asks for it.
- **Retry with care.** A code of -1 with no HTTP status means the request may or may not have reached TikTok. Retry only operations that are safe to repeat.
- **Secrets stay out of errors.** Token-call errors never contain the app secret, the authorization code or the refresh token.
