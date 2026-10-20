---
title: Webhooks
description: Verify TikTok Shop webhook signatures and parse typed webhook events in TypeScript.
sidebar:
  order: 4
---

`Webhooks.verifyAndParse` checks TikTok's signature against the raw request body, then parses the body into a typed event. See [webhooks](/getting-started/webhooks/) for how TikTok signs and delivers them.

```ts
import { createServer } from 'node:http';
import { WebhookParseError, Webhooks, WebhookSignatureError } from 'tiktok-shop-api';

createServer(async (req, res) => {
  const chunks: Buffer[] = [];
  for await (const chunk of req) chunks.push(chunk as Buffer);
  const rawBody = Buffer.concat(chunks); // exactly as received

  try {
    const event = Webhooks.verifyAndParse({
      appKey: process.env.TTS_APP_KEY!,
      appSecret: process.env.TTS_APP_SECRET!,
      rawBody,
      signature: String(req.headers.authorization ?? ''),
    });
    if ('raw' in event) {
      console.log('unknown webhook type', event.type, event.raw);
    } else if (event.type === 1) {
      console.log(event.shopId, event.data?.orderStatus); // OrderStatusChangeWebhook
    }
    res.writeHead(200).end();
  } catch (e) {
    res.writeHead(e instanceof WebhookSignatureError ? 401 : e instanceof WebhookParseError ? 400 : 500).end();
  }
}).listen(3000);
```

## Rules

- **Verify the raw body.** Never re-serialize the body before verifying: changed whitespace or key order makes the signature fail.
- **Parsing is strict.** `verifyAndParse` throws `WebhookParseError` when:
  - the body is not a JSON object;
  - `type` is missing or is not an integer;
  - a known type is missing a required field, or the field is null. A known type missing a required field is always a parse error.
- **Unknown types are kept.** A webhook type this SDK does not know comes back as `{ type, raw }`. Known events never have a `raw` property, so `'raw' in event` (or `isUnknownWebhookEvent(event)`) separates the two. After that check, `event.type` narrows to the specific webhook model.
- **Type names.** `EVENT_TYPES` maps a type number to its name; `1` is `ORDER_STATUS_CHANGE`.
- **IDs are strings.** 64-bit IDs in webhook payloads are strings, as in API responses.

A bad signature throws `WebhookSignatureError`. Answer it with 401 and a parse failure with 400, so neither is mistaken for success.
