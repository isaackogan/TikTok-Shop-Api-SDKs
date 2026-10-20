---
title: PHP SDK
description: Install isaackogan/tiktok-shop-api, the typed TikTok Shop API client for PHP, with Composer and make your first call.
sidebar:
  label: Overview
  order: 1
---

`isaackogan/tiktok-shop-api` is a typed PHP client for the TikTok Shop Partner API. It signs requests, handles OAuth, works with many shops at once, and verifies and types webhooks. It is published to [Packagist](https://packagist.org/packages/isaackogan/tiktok-shop-api), and its source is in [`php/`](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/php).

## Install

```bash
composer require isaackogan/tiktok-shop-api
```

Needs PHP 8.2 or newer, with `ext-curl`, `ext-json` and `ext-mbstring`. The HTTP client is Guzzle 7.

The package is developed in the [TikTok-Shop-Api-SDKs](https://github.com/isaackogan/TikTok-Shop-Api-SDKs) monorepo and mirrored to [isaackogan/TikTok-Shop-Api-PHP](https://github.com/isaackogan/TikTok-Shop-Api-PHP), which is the repository Packagist reads. Please open issues in the main repository.

## First call

With an access token from the [OAuth helper](/sdks/php/authorization/), create a client and call an operation:

```php
use TikTokShop\Api\TikTokShop;

$shop = new TikTokShop(appKey: 'YOUR_APP_KEY', appSecret: 'YOUR_APP_SECRET', accessToken: 'THE_SELLER_ACCESS_TOKEN');

// The shop cipher comes from the authorized-shops call.
$response = $shop->authorization->getAuthorizedShops();
foreach ($response->getData()->getShops() as $authorized) {
    echo $authorized->getName(), ' ', $authorized->getRegion(), ' ', $authorized->getCipher(), PHP_EOL;
}
```

Every request is signed, timestamped and sent with your access token. With a shop cipher, the operations that need one work too; see [calling the API](/sdks/php/calling-the-api/).

## In this section

- [Authorization](/sdks/php/authorization/): `TikTokShopAuth`, authorization URLs, token exchange, refresh and storing a `TokenSet`.
- [Calling the API](/sdks/php/calling-the-api/): the client, API areas, many shops and the HTTP client.
- [Webhooks](/sdks/php/webhooks/): `Webhooks::verifyAndParse` and typed events.
- [Errors](/sdks/php/errors/): `TikTokShopException` and its codes.
