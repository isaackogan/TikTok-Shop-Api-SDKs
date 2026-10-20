<?php
use TikTokShop\Api\TikTokShop;
use TikTokShop\Api\TikTokShopException;

$shop = new TikTokShop(appKey: 'YOUR_APP_KEY', appSecret: 'YOUR_APP_SECRET', accessToken: 'THE_SELLER_ACCESS_TOKEN');

try {
    $shop->authorization->getAuthorizedShops();
} catch (TikTokShopException $e) {
    // TikTok's code (or the HTTP status), its request ID for support, and the HTTP status (null if the request never got a reply).
    error_log($e->getTikTokCode() . ' ' . $e->getMessage() . ' ' . $e->getRequestId() . ' ' . $e->getHttpStatus());
}
