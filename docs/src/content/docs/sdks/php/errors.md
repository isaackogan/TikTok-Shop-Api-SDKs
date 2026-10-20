---
title: Errors
description: TikTokShopException, getTikTokCode and getHttpStatus, and how each kind of failure is reported in the PHP SDK.
sidebar:
  order: 5
---

Every failed call throws `TikTokShopException`, with `getTikTokCode()`, `getMessage()`, `getRequestId()`, `getHttpStatus()` and the original exception as `getPrevious()`. The same rules apply in all eight SDKs; see [errors](/getting-started/errors/).

```php
use TikTokShop\Api\TikTokShop;
use TikTokShop\Api\TikTokShopException;

$shop = new TikTokShop(appKey: 'YOUR_APP_KEY', appSecret: 'YOUR_APP_SECRET', accessToken: 'THE_SELLER_ACCESS_TOKEN');

try {
    $shop->authorization->getAuthorizedShops();
} catch (TikTokShopException $e) {
    // TikTok's code (or the HTTP status), its request ID for support, and the HTTP status (null if the request never got a reply).
    error_log($e->getTikTokCode() . ' ' . $e->getMessage() . ' ' . $e->getRequestId() . ' ' . $e->getHttpStatus());
}
```

| What happened | `getTikTokCode()` | `getHttpStatus()` |
|---|---|---|
| TikTok's reply has a non-zero `code`, even on HTTP 200 | TikTok's code | the status |
| A non-2xx reply | TikTok's non-zero code if the body has one, else the HTTP status | the status |
| A 2xx reply that can't be read: not a JSON object, a `code` that isn't an integer, a body that doesn't fit its model, or a token reply without `data` | -1 | the status |
| No HTTP response at all: connection refused, DNS, TLS, or a timeout | -1 | `null` |

`getCode()` returns the same value as `getTikTokCode()`. `getRequestId()` is an empty string when the reply had none.

- **Look up TikTok's code.** Each operation's error codes are listed in the [API reference](/openapi/reference/) (`x-tts-error-codes` in the spec).
- **Keep the `requestId`.** TikTok's support asks for it.
- **Redirects are errors.** With the default Guzzle client, a 3xx reply is a `TikTokShopException` carrying the status, and the client does not follow it. Token calls never follow redirects, even on an `httpClient` you supply.
- **Secrets stay out of errors.** Messages and previous exceptions never contain the request URL, so a logged exception does not leak the signature. Token calls never put the app secret, the authorization code or the refresh token in them.
