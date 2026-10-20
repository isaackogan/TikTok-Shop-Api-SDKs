---
title: Authorization
description: The TikTok Shop OAuth flow for sellers, partners and creators, regions, token lifetimes and refresh.
sidebar:
  order: 2
---

Every SDK has an OAuth helper (`TikTokShopAuth`, or `NewAuth` in Go) with three operations:

| Operation | What it does |
| --- | --- |
| Authorization URL | Builds the page a seller, partner or creator opens to approve your app. |
| Exchange code | Trades the `code` TikTok sends to your redirect URL for a token set. |
| Refresh | Trades a refresh token for a new token set. |

## The flow

1. **Send the user to the authorization URL.** Your server builds it and redirects the user's browser there. Include a `state` value tied to their session.
2. **TikTok redirects back with a code.** The user lands on the redirect URL registered on your app, with `?code=...&state=...`. Check that `state` matches before going on.
3. **Exchange the code.** Your server trades it for an access token and a refresh token.
4. **Store and refresh the tokens.** Keep both tokens server-side, encrypted at rest. Refresh before the access token expires: each token's expiry field is a Unix timestamp in seconds.

The [Getting Started](/#authorize-a-shop) page shows the flow in each language.

## Authorization kinds and regions

| Kind | Who authorizes | URL needs |
| --- | --- | --- |
| Seller | A shop owner | Your service ID |
| Partner | A partner account | Your service ID |
| Creator | A TikTok creator, for affiliate APIs | Your app key |

Seller and partner authorization have separate pages for the United States (`us`) and the rest of the world (`row`). Creator authorization has one page for both regions.

An empty `state` is left out of the URL, the same as no `state`.

## Token sets

The exchange and refresh calls return the same fields in every SDK, named in each language's style:

| Field | Meaning |
| --- | --- |
| Access token | Sent with API calls. |
| Access token expiry | Unix timestamp, in seconds. |
| Refresh token | Trades for a new token set. |
| Refresh token expiry | Unix timestamp, in seconds. |
| Open ID, seller name, seller base region, user type | Who authorized. Creator and partner tokens may lack the seller fields. |
| Granted scopes | The scopes granted. Absent when TikTok sends none, rather than an empty list. |

Token-call errors never contain the app secret, the authorization code or the refresh token. The HTTP clients the SDKs build never follow a redirect from the token endpoint, so those values are never forwarded to another host. Every token-set type except TypeScript's, which is a plain object, also hides the tokens when printed.

## Errors

A token call that fails raises the same error type as an API call, with TikTok's `code`, `message` and request ID. That includes a reply whose `code` is 0 but which has no `data`, which gets code -1. See [errors](/getting-started/errors/).

## By language

| SDK | Page |
| --- | --- |
| TypeScript | [Authorization](/sdks/typescript/authorization/) |
| Python | [Authorization](/sdks/python/authorization/) |
| Go | [Authorization](/sdks/go/authorization/) |
| Java | [Authorization](/sdks/java/authorization/) |
| Kotlin | [Authorization](/sdks/kotlin/authorization/) |
| PHP | [Authorization](/sdks/php/authorization/) |
| Rust | [Authorization](/sdks/rust/authorization/) |
| C# | [Authorization](/sdks/csharp/authorization/) |
