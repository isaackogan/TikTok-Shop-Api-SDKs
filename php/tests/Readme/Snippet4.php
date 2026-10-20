<?php
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
