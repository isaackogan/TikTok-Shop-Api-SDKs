---
title: The OpenAPI spec
description: Download the TikTok Shop Partner API OpenAPI 3.1 spec, with every operation, webhook, scope and error code, and use it with any OpenAPI tool.
---

All eight SDKs are generated from one OpenAPI 3.1 document describing the TikTok Shop Partner API. It covers 318 operations and 44 webhooks, built automatically from TikTok Shop's [partner documentation](https://partner.tiktokshop.com/docv2). When the docs change, the spec and the SDKs are regenerated, so they don't drift the way hand-written clients do.

This site bundles the spec it was built from:

- [`tiktok-shop.openapi.yaml`](/openapi/tiktok-shop.openapi.yaml)
- [`tiktok-shop.openapi.json`](/openapi/tiktok-shop.openapi.json)

The same files are in the repository's [`.openapi/`](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/.openapi) folder. Browse every operation and webhook in the [API reference](/openapi/reference/).

## Coverage

Operations are grouped by tag, and each SDK groups its methods the same way:

| Tags |
| --- |
| Affiliate creator, Affiliate partner, Affiliate seller |
| Analytics, Authorization |
| Customer engagement, Customer service |
| Event, Finance |
| Fulfilled by TikTok (FBT), Fulfillment, Logistics |
| Orders, Products, Promotion |
| Return and refund, Seller, Supply chain, Tools |

For each operation, the spec includes:
- its parameters, request body and response schema, with types and required fields;
- the enums and the length and range limits stated in the docs;
- the scopes it needs, its documented error codes, and a link to its page in TikTok's docs.

## Conventions described once

Three things apply to most operations, so the spec states each one once instead of repeating it everywhere:

- **Signing.** Every request needs the `app_key`, `timestamp` and `sign` query parameters. They are described by the top-level `x-tts-signing` extension; see [request signing](/getting-started/concepts/#request-signing).
- **Access token.** Authenticated operations use the `accessToken` security scheme, which is the `x-tts-access-token` header.
- **Shop cipher.** Shop-scoped operations take the shared `ShopCipher` query parameter and are flagged with `x-tts-requires-shop-cipher`.

The server is `https://open-api.tiktokglobalshop.com`.

## Vendor extensions

| Extension | Where | Meaning |
| --- | --- | --- |
| `x-tts-signing` | Top level | The signed query parameters, the algorithm and a link to TikTok's signing guide. |
| `x-tts-webhook-signing` | Top level | How webhooks are signed: the `Authorization` header, HMAC-SHA256 over `app_key` and the raw body, keyed with the app secret, in lowercase hex. |
| `x-tts-requires-shop-cipher` | Operation | `true` when the operation needs `shop_cipher`. |
| `x-tts-scopes` | Operation | The API scopes the operation needs. |
| `x-tts-error-codes` | Operation | The documented error codes, each with TikTok's message. |
| `x-tts-docs-url` | Operation and webhook | The page in TikTok's documentation. |
| `x-tts-scenario` | Operation | The scenario number TikTok's documentation assigns to the operation, as given. |
| `x-tts-webhook-type` | Webhook | The numeric `type` the webhook is delivered with. |
| `x-tts-event-type` | Webhook | The event name used to subscribe to the webhook, such as `ORDER_STATUS_CHANGE`. |
| `x-enum-descriptions` | Schema | A description for each enum value, in the same order as `enum`. |

## Webhooks

Webhooks are in the OpenAPI 3.1 `webhooks` section, keyed by event name. Each webhook has a request-body schema whose `type` property is a `const` of the webhook's number. The `WebhookEvent` schema is a `oneOf` of every payload. It has no discriminator object, because a discriminator in OpenAPI must be a string and `type` is an integer. See [webhooks](/getting-started/webhooks/) for verification.

## Using it with other tools

The spec is valid OpenAPI 3.1, so code generators, API clients and documentation viewers can read it. To generate your own client:
- **Implement signing yourself.** It can't be expressed in OpenAPI; the SDKs add it by hand.
- **Add `shop_cipher` yourself** on the flagged operations.
- **Strip the `webhooks` section** if your generator doesn't support it.
- **Read IDs as strings in JavaScript**, because 64-bit IDs lose precision as numbers.

The spec is generated, so never edit it by hand. If it is wrong about an operation, please open an issue at https://github.com/isaackogan/TikTok-Shop-Api-SDKs/issues with a link to TikTok's page for that operation.
