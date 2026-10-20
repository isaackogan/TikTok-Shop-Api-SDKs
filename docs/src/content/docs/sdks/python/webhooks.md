---
title: Webhooks
description: Verify TikTok Shop webhook signatures and parse typed webhook events in Python.
sidebar:
  order: 4
---

`Webhooks.verify_and_parse` checks TikTok's signature against the raw request body, then parses the body into a typed event. See [webhooks](/getting-started/webhooks/) for how TikTok signs and delivers them.

This example uses Flask; any framework that gives you the unmodified bytes works:

```python
import os

from flask import Flask, request

from tiktok_shop_api import UnknownWebhookEvent, WebhookSignatureError, Webhooks
from tiktok_shop_api.generated.models import OrderStatusChangeWebhook

app = Flask(__name__)


@app.post("/webhooks/tiktok-shop")
def tiktok_shop_webhook():
    try:
        event = Webhooks.verify_and_parse(
            app_key=os.environ["TTS_APP_KEY"],
            app_secret=os.environ["TTS_APP_SECRET"],
            raw_body=request.get_data(),  # exactly as received
            signature=request.headers.get("Authorization", ""),
        )
    except WebhookSignatureError:
        return "", 401
    except ValueError:  # not a webhook this SDK can read
        return "", 400
    if isinstance(event, UnknownWebhookEvent):
        print("unknown webhook type", event.type, event.raw)
    elif isinstance(event, OrderStatusChangeWebhook):
        print(event.shop_id, event.data)
    return "", 200
```

## Rules

- **Verify the raw body.** Never re-serialize the body before verifying: changed whitespace or key order makes the signature fail.
- **Parsing is strict.** `Webhooks.parse` raises `ValueError` for a body that is not a JSON object, a `type` that is missing or not an integer, or a known type with a required field missing or null. A known type missing a required field is a parse error.
- **Unknown types are kept.** A webhook type this SDK does not know comes back as `UnknownWebhookEvent(type, raw)`. Known events are the generated model for that webhook, so `isinstance` narrows them.
- **Type names.** `EVENT_TYPES` maps a type number to its name; `1` is `ORDER_STATUS_CHANGE`.

A bad signature raises `WebhookSignatureError`. Answer it with 401 and a parse failure (`ValueError`) with 400, so neither is mistaken for success. `Webhooks.verify` returns a plain `bool` if you want to check the signature without parsing.
