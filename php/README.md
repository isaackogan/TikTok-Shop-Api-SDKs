# TikTok Shop API for PHP (Unofficial)

[TikTok Shop API](https://partner.tiktokshop.com/) Client for PHP (Unofficial, Unaffiliated with TikTok or ByteDance Ltd.)

A PHP client for the TikTok Shop API, also called the TikTok Shop Partner API or Open API. It covers every endpoint in
the published spec, over 300 operations across orders, products, fulfillment, logistics, returns and refunds, finance,
promotions, affiliate, analytics and customer service, grouped like TikTok's own docs.

Every request is signed with HMAC-SHA256 and sent with your access token, and the shop cipher is added wherever an
endpoint needs it. The OAuth helper builds the authorization URL and exchanges and refreshes tokens. One client can
serve many shops, and TikTok Shop webhooks are verified and parsed into typed event classes you narrow with
`instanceof`. Requests and responses are PHP classes with getters and setters, generated from the OpenAPI spec, and
64-bit IDs are never rounded. It needs PHP 8.2+ and runs on Guzzle 7.

Full guides, API reference and documentation: <https://ttspa.docs.isaackogan.com/sdks/php/>

The guides cover [Authorization](https://ttspa.docs.isaackogan.com/sdks/php/authorization/), [Calling the API](https://ttspa.docs.isaackogan.com/sdks/php/calling-the-api/),
[Webhooks](https://ttspa.docs.isaackogan.com/sdks/php/webhooks/) and [Errors](https://ttspa.docs.isaackogan.com/sdks/php/errors/), and the [API reference](https://ttspa.docs.isaackogan.com/openapi/reference/) lists every operation and webhook.

[![Packagist](https://img.shields.io/packagist/v/isaackogan/tiktok-shop-api?style=flat&color=0274b5)](https://packagist.org/packages/isaackogan/tiktok-shop-api)
![PHP](https://img.shields.io/packagist/dependency-v/isaackogan/tiktok-shop-api/php?style=flat&color=0274b5)
![Stars](https://img.shields.io/github/stars/isaackogan/TikTok-Shop-Api-SDKs?style=flat&color=0274b5)
![Issues](https://img.shields.io/github/issues/isaackogan/TikTok-Shop-Api-SDKs?style=flat&color=0274b5)
![License](https://img.shields.io/github/license/isaackogan/TikTok-Shop-Api-SDKs?style=flat&color=0274b5)

> [!IMPORTANT]
> Request signing follows TikTok's documentation and has not been verified against the live API. If TikTok rejects a signature, please open an issue at https://github.com/isaackogan/TikTok-Shop-Api-SDKs/issues.

> [!NOTE]
> The package is developed in the [TikTok-Shop-Api-SDKs](https://github.com/isaackogan/TikTok-Shop-Api-SDKs) monorepo
> and mirrored to [isaackogan/TikTok-Shop-Api-PHP](https://github.com/isaackogan/TikTok-Shop-Api-PHP), which is the
> repository Packagist reads. Please open issues in the main repository.

> [!TIP]
> The OpenAPI spec this client is generated from is published at
> [tiktok-shop.openapi.yaml](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/.openapi/tiktok-shop.openapi.yaml).
> Point any OpenAPI 3.1 tool at it.

### Do you prefer other programming languages?

- [TikTok Shop API for TypeScript](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/typescript), `tiktok-shop-api` on npm
- [TikTok Shop API for Python](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/python), `tiktok-shop-api` on PyPI
- [TikTok Shop API for Go](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/go), `github.com/isaackogan/TikTok-Shop-Api-SDKs/go`
- [TikTok Shop API for Java](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/java), `com.isaackogan:tiktok-shop-api` on Maven Central
- [TikTok Shop API for Kotlin](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/kotlin), `com.isaackogan:tiktok-shop-api-kotlin` on Maven Central
- [TikTok Shop API for Rust](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/rust), `tiktok-shop-api` on crates.io
- [TikTok Shop API for C# and .NET](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/csharp), `TikTokShop.Api` on NuGet

### Table of Contents

- [Getting Started](#getting-started)
- [Params and Options](#params-and-options)
- [Methods](#methods)
- [Examples](#examples)
- [Frequently Asked Questions](#frequently-asked-questions)
- [Contributors](#contributors)
- [License](#license)

## Getting Started

1. Install the package with Composer

```bash
composer require isaackogan/tiktok-shop-api
```

It needs PHP 8.2 or newer, with `ext-curl`, `ext-json` and `ext-mbstring`.

2. Authorize a shop with OAuth and get an access token

```php
use TikTokShop\Api\TikTokShopAuth;

$auth = new TikTokShopAuth(appKey: 'YOUR_APP_KEY', appSecret: 'YOUR_APP_SECRET', serviceId: 'YOUR_SERVICE_ID');

// 1. Send the seller to this page. Use TikTokShopAuth::PARTNER or CREATOR for the other kinds,
//    and TikTokShopAuth::ROW outside the United States.
$url = $auth->authorizationUrl(TikTokShopAuth::SELLER, TikTokShopAuth::US, state: 'a-random-csrf-token');
header('Location: ' . $url);

// 2. TikTok redirects back to your redirect URL with ?code=...
$tokens = $auth->exchangeCode($_GET['code']);

echo $tokens->getAccessToken(), ' expires at ', $tokens->accessTokenExpireIn, PHP_EOL;
echo $tokens->sellerName, ' (', $tokens->sellerBaseRegion, ')', PHP_EOL;
```

Refresh the tokens, and store them:

```php
use TikTokShop\Api\TikTokShopAuth;
use TikTokShop\Api\TokenSet;

$auth = new TikTokShopAuth(appKey: 'YOUR_APP_KEY', appSecret: 'YOUR_APP_SECRET');

// Store the tokens: toArray() holds the real values, so encrypt it at rest.
$stored = json_encode($tokens->toArray());

// Later: refresh before the access token expires.
$tokens = TokenSet::fromArray(json_decode($stored, true));
$tokens = $auth->refresh($tokens->getRefreshToken());
```

`TokenSet` holds secrets. The access and refresh tokens are not properties: `var_dump` and `print_r` show `***`,
`var_export` and `(array)` show neither token, and `serialize()` refuses. Read them with `getAccessToken()` and
`getRefreshToken()`; `toArray()` and `json_encode()` give the real values for storage.

3. Make your first call

```php
use TikTokShop\Api\TikTokShop;

$shop = new TikTokShop(appKey: 'YOUR_APP_KEY', appSecret: 'YOUR_APP_SECRET', accessToken: 'THE_SELLER_ACCESS_TOKEN');

// The shop cipher comes from the authorized-shops call.
$response = $shop->authorization->getAuthorizedShops();
foreach ($response->getData()->getShops() as $authorized) {
    echo $authorized->getName(), ' ', $authorized->getRegion(), ' ', $authorized->getCipher(), PHP_EOL;
}
```

With a shop cipher, the operations that need one (most of them) work:

```php
use TikTokShop\Api\TikTokShop;

$shop = new TikTokShop(
    appKey: 'YOUR_APP_KEY',
    appSecret: 'YOUR_APP_SECRET',
    accessToken: 'THE_SELLER_ACCESS_TOKEN',
    shopCipher: 'THE_SHOP_CIPHER',
);

// Every request is signed, and shop_cipher is added to the operations that take one.
$orders = $shop->orders->getOrderList(20);
foreach ($orders->getData()->getOrders() as $order) {
    echo $order->getId(), PHP_EOL;
}
```

The generated methods take their parameters positionally, in the order of the generated signature. The `shop_cipher`
parameter is not among them: the client adds it.

## Params and Options

To create a new client, pass these named arguments.

`new TikTokShop(appKey: ..., appSecret: ..., ...)`

| Param Name | Required | Description |
|------------|----------|-------------|
| `appKey` | Yes | Your app key. |
| `appSecret` | Yes | Your app secret. It signs every request. |
| `accessToken` | No | The seller's access token, sent as the `x-tts-access-token` header. |
| `shopCipher` | No | The shop's cipher, added as `shop_cipher` to the operations that take one. `$shop->authorization->getAuthorizedShops()` returns it. |
| `baseUrl` | No | Default `TikTokShop::DEFAULT_BASE_URL` (`https://open-api.tiktokglobalshop.com`). It must be an origin such as `https://host:8443`, with no path prefix: signing and shop-cipher matching use the request path. |
| `timeout` | No | Seconds for the whole request, for the client the SDK builds. Default 30; 0 means no limit. A negative value throws `InvalidArgumentException`. |
| `httpClient` | No | Your own Guzzle client, used as is. By default the SDK builds a Guzzle client that never follows redirects, with Guzzle's default proxy behaviour. |

The OAuth helper takes its own named arguments.

`new TikTokShopAuth(appKey: ..., appSecret: ..., ...)`

| Param Name | Required | Description |
|------------|----------|-------------|
| `appKey` | Yes | Your app key. |
| `appSecret` | Yes | Your app secret. It is hidden from stack traces (`#[\SensitiveParameter]`). |
| `serviceId` | No | Your Partner Center service ID. `TikTokShopAuth::SELLER` and `TikTokShopAuth::PARTNER` URLs need it. |
| `baseUrl` | No | Default `TikTokShopAuth::DEFAULT_BASE_URL` (`https://auth.tiktok-shops.com`). An origin, with no path prefix. |
| `timeout` | No | Seconds for one request, for the client the SDK builds. Default 30; 0 means no limit. |
| `httpClient` | No | Your own Guzzle client. The token calls never follow redirects even on your client, because their URL holds your app secret. |

Requests carry the User-Agent `tiktok-shop-api-php/<version>` (`TikTokShop::userAgent()`).

## Methods

Each API group is a property of the client: `affiliateCreator`, `affiliatePartner`, `affiliateSeller`, `analytics`,
`authorization`, `customerEngagement`, `customerService`, `event`, `finance`, `fulfilledByTikTok`, `fulfillment`,
`logistics`, `orders`, `products`, `promotion`, `returnAndRefund`, `seller`, `supplyChain` and `tools`. Each is the
concrete generated API class, so your IDE completes the operations and models.

| Method Name | Description |
|-------------|-------------|
| `$shop->withShop(accessToken: ..., shopCipher: ...)` | Returns a client for another shop or token that shares the HTTP client. An argument you leave out keeps this client's value; `null` or `''` clears it. See [Several shops](#several-shops). |
| `$auth->authorizationUrl($type, $region, state: ...)` | Builds the URL to send a seller, partner or creator to. `$type` is `TikTokShopAuth::SELLER`, `PARTNER` or `CREATOR`; `$region` is `TikTokShopAuth::US` or `ROW`. |
| `$auth->exchangeCode($code)` | Trades the `code` from the redirect for a `TokenSet`. |
| `$auth->refresh($refreshToken)` | Trades a refresh token for a new `TokenSet`. |
| `TokenSet::fromArray($data)` | Rebuilds a `TokenSet` you stored with `toArray()`. |
| `Webhooks::verify($appKey, $appSecret, $rawBody, $signature)` | Checks a webhook's `Authorization` header against the raw body. Returns `true` or `false`. |
| `Webhooks::parse($rawBody)` | Parses a body into its event class, or an `UnknownWebhookEvent`. Throws `InvalidArgumentException` for a body it cannot read. |
| `Webhooks::verifyAndParse($appKey, $appSecret, $rawBody, $signature)` | Verifies, then parses. Throws `WebhookSignatureException` when the signature does not match. |

A `TokenSet` has `getAccessToken()` and `getRefreshToken()`, and the properties `accessTokenExpireIn`,
`refreshTokenExpireIn`, `openId`, `sellerName`, `sellerBaseRegion`, `userType` and `grantedScopes`.

## Examples

### Several shops

```php
use TikTokShop\Api\TikTokShop;

$shop = new TikTokShop(appKey: 'YOUR_APP_KEY', appSecret: 'YOUR_APP_SECRET', accessToken: 'TOKEN_A', shopCipher: 'CIPHER_A');

// Another shop, sharing the HTTP client. $shop is not changed.
$other = $shop->withShop(accessToken: 'TOKEN_B', shopCipher: 'CIPHER_B');

// An argument you leave out keeps this client's value; null (or '') clears it.
$sameShopNewToken = $shop->withShop(accessToken: 'TOKEN_A2');
$noShop = $shop->withShop(shopCipher: null);
```

### Handle errors

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

Every failure is a `TikTokShopException`, with `getTikTokCode()`, `getMessage()`, `getRequestId()`, `getHttpStatus()`
and the original exception as `getPrevious()`:

| What happened | `getTikTokCode()` | `getHttpStatus()` |
|---|---|---|
| TikTok's reply has a non-zero `code`, even on HTTP 200 | TikTok's code | the status |
| A non-2xx reply | TikTok's non-zero code if the body has one, else the HTTP status | the status |
| A 2xx reply that can't be read: not a JSON object, a `code` that isn't an integer, a body that doesn't fit its model, or a token reply without `data` | -1 | the status |
| No HTTP response at all: connection refused, DNS, TLS, or a timeout | -1 | `null` |

Messages and previous exceptions never contain the request URL, so a logged exception does not leak the signature.

### Webhooks

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

- `Webhooks::parse()` returns one event class per webhook type (they live in `TikTokShop\Api\Generated\Event`, rendered
  from the spec), each with a typed `getPayload()`, or an `UnknownWebhookEvent`. Narrow with `instanceof`. All of them
  extend `TikTokShop\Api\WebhookEvent`, which has `getType()` and `getRaw()` (the decoded body, unknown fields
  included).
- Verify against the raw body as received: re-encoding the JSON changes the signature.
- Parsing is strict. A body that is not a JSON object, a `type` that is missing or not an integer, or a known type with
  a required property missing or null throws `InvalidArgumentException`: a known type missing a required field is a
  parse error. An integer `type` this SDK does not know becomes `UnknownWebhookEvent`. Unknown fields are ignored.
- 64-bit IDs keep their exact digits (a `shop_id` sent as a JSON number arrives as the string `"7494049642642441621"`).
- `Webhooks::EVENT_TYPES` maps a type to its name, for example `1` to `ORDER_STATUS_CHANGE`.

### GET requests with a body

Three operations are GETs with a body (`getConversationList`, `mapTokopediaToTikTokShopProductIDs`,
`getShippingTemplateAvailability`). The SDK sends the body and signs it.

## Frequently Asked Questions

### How do I get a TikTok Shop access token in PHP?

Create a `TikTokShopAuth` with your app key, app secret and service ID, redirect the seller to `authorizationUrl()`,
then trade the `code` TikTok sends back with `exchangeCode()`. Call `refresh()` before the access token expires. See
[Getting Started](#getting-started).

### What is a shop cipher, and where do I find it?

Most TikTok Shop API endpoints act on one shop and need a `shop_cipher` query parameter. Call
`$shop->authorization->getAuthorizedShops()` with the seller's access token: each shop in the reply has a cipher. Pass
it as `shopCipher:` and the client adds it to every endpoint that needs it.

### How do I verify TikTok Shop webhooks in Laravel or plain PHP?

Pass the raw body and the `Authorization` header to `Webhooks::verifyAndParse`. In plain PHP the body is
`file_get_contents('php://input')`. In any framework, use the body as received, because re-encoded JSON no longer
matches the signature. See [Webhooks](#webhooks).

### Can one app manage many TikTok Shop sellers?

Yes. Keep one client per shop with `withShop`. They share one HTTP client. See [Several shops](#several-shops).

### How do I store tokens safely?

`toArray()` and `json_encode()` give the real token values, so encrypt what you store. `var_dump`, `print_r` and
`var_export` never show them, and `serialize()` refuses a `TokenSet`.

### Which TikTok Shop API versions does it cover?

Every endpoint in TikTok's partner documentation, from API version 202309 onwards, and every documented webhook.

### Is this affiliated with TikTok?

No. It is an independent open-source project, built from TikTok's partner documentation.

### Is this available in other languages?

Yes. See [Do you prefer other programming languages?](#do-you-prefer-other-programming-languages) for the TypeScript,
Python, Go, Java, Kotlin, Rust and C# SDKs.

## Contributors

* **Isaac Kogan** - *Creator & Maintainer* - [isaackogan](https://github.com/isaackogan)

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/LICENSE) file for details.

Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.
