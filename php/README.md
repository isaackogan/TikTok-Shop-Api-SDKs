# TikTok Shop API for PHP

A PHP client for the **TikTok Shop API** (the TikTok Shop Partner API / Open API). It covers every endpoint in the published spec, signs every request, ships an OAuth helper, and parses webhooks into typed event classes you narrow with `instanceof`.

Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.

- **Every TikTok Shop API endpoint**, grouped like TikTok's own docs: `$shop->orders`, `$shop->products`, `$shop->fulfillment`, `$shop->finance`, and 15 more.
- **Typed models.** Generated from the [OpenAPI spec](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/.openapi/tiktok-shop.openapi.yaml), so requests and responses are PHP classes with getters and setters. 64-bit IDs are never rounded.
- **Request signing** (HMAC-SHA256), `app_key`, `timestamp`, `shop_cipher` and the `x-tts-access-token` header added for you.
- **OAuth helper** for the authorization URL, code exchange and token refresh.
- **Webhooks**: verify the signature, then get a typed event class for any of the webhook types.
- **PHP 8.2+** with `ext-curl`, `ext-json` and `ext-mbstring`, on Guzzle 7.

> Request signing follows TikTok's documentation and has not been verified against the live API. If TikTok rejects a signature, please open an issue at https://github.com/isaackogan/TikTok-Shop-Api-SDKs/issues.

## Install

```bash
composer require isaackogan/tiktok-shop-api
```

Needs PHP 8.2 or newer, with `ext-curl`, `ext-json` and `ext-mbstring`.

The package is developed in the [TikTok-Shop-Api-SDKs](https://github.com/isaackogan/TikTok-Shop-Api-SDKs) monorepo and mirrored to [isaackogan/TikTok-Shop-Api-PHP](https://github.com/isaackogan/TikTok-Shop-Api-PHP), which is the repository Packagist reads. Please open issues in the main repository.

## Authorize a shop (OAuth)

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

`TokenSet` holds secrets. The access and refresh tokens are not properties: `var_dump` and `print_r` show `***`, `var_export` and `(array)` show neither token, and `serialize()` refuses. Read them with `getAccessToken()` and `getRefreshToken()`; `toArray()` and `json_encode()` give the real values for storage.

## Make your first call

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

The generated methods take their parameters positionally, in the order of the generated signature. The `shop_cipher` parameter is not among them: the client adds it.

## Several shops (`withShop`)

```php
use TikTokShop\Api\TikTokShop;

$shop = new TikTokShop(appKey: 'YOUR_APP_KEY', appSecret: 'YOUR_APP_SECRET', accessToken: 'TOKEN_A', shopCipher: 'CIPHER_A');

// Another shop, sharing the HTTP client. $shop is not changed.
$other = $shop->withShop(accessToken: 'TOKEN_B', shopCipher: 'CIPHER_B');

// An argument you leave out keeps this client's value; null (or '') clears it.
$sameShopNewToken = $shop->withShop(accessToken: 'TOKEN_A2');
$noShop = $shop->withShop(shopCipher: null);
```

## Errors

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

Every failure is a `TikTokShopException`, with `getTikTokCode()`, `getMessage()`, `getRequestId()`, `getHttpStatus()` and the original exception as `getPrevious()`:

| What happened | `getTikTokCode()` | `getHttpStatus()` |
|---|---|---|
| TikTok's reply has a non-zero `code`, even on HTTP 200 | TikTok's code | the status |
| A non-2xx reply | TikTok's non-zero code if the body has one, else the HTTP status | the status |
| A 2xx reply that can't be read: not a JSON object, a `code` that isn't an integer, a body that doesn't fit its model, or a token reply without `data` | -1 | the status |
| No HTTP response at all: connection refused, DNS, TLS, or a timeout | -1 | `null` |

Messages and previous exceptions never contain the request URL, so a logged exception does not leak the signature.

## Webhooks

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

- `Webhooks::parse()` returns one event class per webhook type (they live in `TikTokShop\Api\Generated\Event`, rendered from the spec), each with a typed `getPayload()`, or an `UnknownWebhookEvent`. Narrow with `instanceof`. All of them extend `TikTokShop\Api\WebhookEvent`, which has `getType()` and `getRaw()` (the decoded body, unknown fields included).
- Verify against the **raw body** as received: re-encoding the JSON changes the signature.
- Parsing is strict. A body that is not a JSON object, a `type` that is missing or not an integer, or a known type with a required property missing or null throws `InvalidArgumentException`: a known type missing a required field is a parse error. An integer `type` this SDK does not know becomes `UnknownWebhookEvent`. Unknown fields are ignored.
- 64-bit IDs keep their exact digits (a `shop_id` sent as a JSON number arrives as the string `"7494049642642441621"`).
- `Webhooks::EVENT_TYPES` maps a type to its name, for example `1` to `ORDER_STATUS_CHANGE`.

## API surface

The client's properties are the API groups: `affiliateCreator`, `affiliatePartner`, `affiliateSeller`, `analytics`, `authorization`, `customerEngagement`, `customerService`, `event`, `finance`, `fulfilledByTikTok`, `fulfillment`, `logistics`, `orders`, `products`, `promotion`, `returnAndRefund`, `seller`, `supplyChain`, `tools`. Each is the concrete generated API class, so your IDE completes the operations and models.

## HTTP client

By default the SDK builds a Guzzle client that never follows redirects, with a 30 second timeout (`timeout:`, 0 for none) and Guzzle's default proxy behaviour. `baseUrl:` (on the client and the OAuth helper) must be an origin such as `https://host:8443`, with no path prefix: signing and shop-cipher matching use the request path. Requests carry the User-Agent `tiktok-shop-api-php/<version>`. Pass your own with `httpClient:`; it is used as is, except that the OAuth token calls never follow redirects even on your client, because their URL holds your app secret.

## Notes

- Generated from [the spec](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/blob/main/.openapi/tiktok-shop.openapi.yaml) in the [TikTok-Shop-Api-SDKs](https://github.com/isaackogan/TikTok-Shop-Api-SDKs) repository, which also has SDKs for TypeScript, Python, Go, Java, Kotlin, Rust and C#.
- Three operations are GETs with a body (`getConversationList`, `mapTokopediaToTikTokShopProductIDs`, `getShippingTemplateAvailability`). The SDK sends the body and signs it.
- The secrets passed to the OAuth helper are also hidden from stack traces (`#[\SensitiveParameter]`).

## License

MIT
