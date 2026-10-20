---
title: Troubleshooting
description: Fix signature rejections, missing shop ciphers, expired tokens, webhook verification failures and other common TikTok Shop API problems.
---

## TikTok rejects the signature

Signing follows TikTok's documentation but has not yet been verified against the live API. Before reporting a problem, check these:

- **App credentials.** The app key and app secret are from the same app, with no surrounding whitespace.
- **Base URL.** It is an origin, such as `https://open-api.tiktokglobalshop.com`, with no path prefix. Signing uses the request path, so a prefix such as a proxy's `/tiktok` changes what is signed.
- **The request.** Nothing between the SDK and TikTok rewrites it: a proxy that reorders query parameters or re-encodes the body breaks the signature.
- **The clock.** The machine's clock is correct. The `timestamp` parameter is the current Unix time.

If all of that holds and TikTok still rejects the signature, please open an issue at https://github.com/isaackogan/TikTok-Shop-Api-SDKs/issues with:
- the operation;
- the SDK and its version;
- TikTok's `code`, `message` and `request_id`.

Never include your app secret or tokens.

## An operation says the shop cipher is missing or invalid

Most operations act on one shop and need its cipher. Get it from the authorized-shops operation (`getAuthorizedShops` or the language's equivalent), then create the client with it or derive a client for that shop. The SDK adds `shop_cipher` only to the operations the spec flags with `x-tts-requires-shop-cipher`; see [shop cipher](/getting-started/concepts/#shop-cipher).

A cipher belongs to the shop the access token was granted for. Use the token and cipher of the same shop.

## The access token has expired

The access token expiry is a Unix timestamp, not a duration. Refresh before that moment with the OAuth helper's refresh call, and store the whole token set it returns, including its refresh token. See [authorization](/getting-started/authorization/).

## A call fails with code -1

Code -1 means the SDK couldn't use the reply, or there was no reply at all:

- **No HTTP status:** there was no response, from a connection failure, DNS, TLS or a timeout. Check network access to the API host, and the client's timeout.
- **An HTTP status:** the reply wasn't a JSON object, its `code` wasn't an integer, or its `data` didn't fit the operation's model. The original error is the cause. If TikTok's reply doesn't match the spec, please open an issue with the operation and the request ID.

See [errors](/getting-started/errors/) for every case.

## Webhook signatures never match

The usual cause is verifying a body that isn't byte-for-byte what TikTok sent:

- **JSON middleware.** A framework's JSON middleware parsed and re-serialized the body. Read the raw bytes for the webhook route instead.
- **Character decoding.** The body was decoded with the wrong character set, or had whitespace trimmed.
- **The wrong secret.** The app key and app secret are from a different app than the webhook's.

The signature is the `Authorization` header's whole value. See [webhooks](/getting-started/webhooks/).

## A webhook fails to parse

Parsing is strict: a known webhook type missing a required field is a parse error. If TikTok sends a payload that is valid but fails to parse, the spec is wrong about that webhook. Please open an issue with the webhook type and the payload, with the IDs and personal data removed.

An unknown webhook type is not an error. It comes back as an unknown event holding the raw JSON.

## A method or field is missing

The SDKs are generated from TikTok's documentation. If an operation or field is missing, check whether TikTok documents it at the version you need; the [API reference](/openapi/reference/) links each operation's page. If TikTok documents it and the spec doesn't have it, please open an issue with a link to TikTok's page.
