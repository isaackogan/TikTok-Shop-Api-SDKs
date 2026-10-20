<?php
use TikTokShop\Api\TikTokShop;

$shop = new TikTokShop(appKey: 'YOUR_APP_KEY', appSecret: 'YOUR_APP_SECRET', accessToken: 'THE_SELLER_ACCESS_TOKEN');

// The shop cipher comes from the authorized-shops call.
$response = $shop->authorization->getAuthorizedShops();
foreach ($response->getData()->getShops() as $authorized) {
    echo $authorized->getName(), ' ', $authorized->getRegion(), ' ', $authorized->getCipher(), PHP_EOL;
}
