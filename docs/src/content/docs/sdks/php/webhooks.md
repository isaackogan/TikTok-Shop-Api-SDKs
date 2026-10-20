---
title: Webhooks
description: Verify TikTok Shop webhook signatures and parse typed webhook events in PHP.
sidebar:
  order: 4
---

`Webhooks::verifyAndParse` checks TikTok's signature against the raw request body, then parses the body into a typed event. See [webhooks](/getting-started/webhooks/) for how TikTok signs and delivers them.

```php
use TikTokShop\Api\Generated\Event\OrderStatusChangeEvent;
use TikTokShop\Api\Generated\Event\SellerDeauthorizationEvent;
use TikTokShop\Api\UnknownWebhookEvent;
use TikTokShop\Api\WebhookSignatureException;
use TikTokShop\Api\Webhooks;

// The body exactly as received (never re-encode it), and the Authorization header.
$rawBody = file_get_contents('php://input');
$signature = $_SERVER['HTTP_AUTHORIZATION'] ?? '';

try {
    $event = Webhooks::verifyAndParse('YOUR_APP_KEY', 'YOUR_APP_SECRET', $rawBody, $signature);
} catch (WebhookSignatureException) {
    http_response_code(401);
    exit;
} catch (InvalidArgumentException) {
    http_response_code(400); // not a webhook this SDK can read
    exit;
}

if ($event instanceof OrderStatusChangeEvent) {
    $data = $event->getPayload()->getData();
    echo $data->getOrderId(), ' is now ', $data->getOrderStatus(), PHP_EOL;
} elseif ($event instanceof SellerDeauthorizationEvent) {
    echo 'shop ', $event->getPayload()->getShopId(), ' revoked access', PHP_EOL;
} elseif ($event instanceof UnknownWebhookEvent) {
    error_log('unhandled webhook type ' . $event->getType());
}
http_response_code(200);
```

## Rules

- **Verify the raw body.** Never re-encode the body before verifying: changed bytes make the signature fail.
- **Parsing is strict.** `Webhooks::parse` throws `InvalidArgumentException` when:
  - the body is not a JSON object;
  - `type` is missing or is not an integer;
  - a known type is missing a required property, or the property is null. A known type missing a required field is always a parse error.
- **Unknown types are kept.** An integer `type` this SDK does not know becomes an `UnknownWebhookEvent`. Unknown fields are ignored.
- **Narrow the event.** `Webhooks::parse()` returns one event class per webhook type (they live in `TikTokShop\Api\Generated\Event`, rendered from the spec), each with a typed `getPayload()`, or an `UnknownWebhookEvent`. Narrow with `instanceof`. All of them extend `TikTokShop\Api\WebhookEvent`, which has `getType()` and `getRaw()` (the decoded body, unknown fields included).
- **Type names.** `Webhooks::EVENT_TYPES` maps a type number to its name; `1` is `ORDER_STATUS_CHANGE`.
- **IDs keep their digits.** 64-bit IDs keep their exact digits: a `shop_id` sent as a JSON number arrives as the string `"7494049642642441621"`.

## Exceptions

A bad signature throws `WebhookSignatureException`. A body that cannot be read as a webhook throws `InvalidArgumentException`. Answer the first with 401 and the second with 400, so neither is mistaken for success.
