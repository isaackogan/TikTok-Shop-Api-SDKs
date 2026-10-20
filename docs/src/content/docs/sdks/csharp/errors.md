---
title: Errors
description: TikTokShopException, its Code and HttpStatus, and how each kind of failure is reported in the C# SDK.
sidebar:
  order: 5
---

Every failed call throws `TikTokShopException`, with `Code`, `TikTokMessage` (the same text as `Message`), `RequestId`, `HttpStatus` and the original exception as `InnerException`. The same rules apply in all eight SDKs; see [errors](/getting-started/errors/).

```csharp
using System;
using TikTokShop.Api;

var client = new TikTokShopClient("YOUR_APP_KEY", "YOUR_APP_SECRET", accessToken: "THE_SELLER_ACCESS_TOKEN");

try
{
    await client.Authorization.GetAuthorizedShopsAsync();
}
catch (TikTokShopException e)
{
    // TikTok's code (or the HTTP status), its message, its request ID for support, and the HTTP status (null if no reply came).
    Console.WriteLine($"{e.Code} {e.TikTokMessage} {e.RequestId} {e.HttpStatus}");
}
```

| What happened | `Code` | `HttpStatus` |
|---|---|---|
| TikTok's reply has a non-zero `code`, even on HTTP 200 | TikTok's code | the status |
| A non-2xx reply | TikTok's non-zero code if the body has one, else the HTTP status | the status |
| A 2xx reply that can't be read: not a JSON object, a `code` that isn't an integer, a body that doesn't decode into its model (the decoder's exception is the `InnerException`), or a token reply without `data` | -1 | the status |
| No HTTP response at all: connection refused, DNS, TLS, or a timeout | -1 | `null` |

`Code` is a `long` and `HttpStatus` is an `int?`. `RequestId` is an empty string when the reply had none.

- **Look up TikTok's code.** Each operation's error codes are listed in the [API reference](/openapi/reference/) (`x-tts-error-codes` in the spec).
- **Keep the `RequestId`.** TikTok's support asks for it.
- **Redirects are errors.** With the default handler, a 3xx reply is a `TikTokShopException` with code 302, and the client does not follow it. The OAuth calls never follow redirects, and refuse a handler that does.
- **Secrets stay out of errors.** Messages and inner exceptions never contain the request URL or any secret, so a logged exception does not leak the signature or the app secret. The OAuth calls follow the same rules.
