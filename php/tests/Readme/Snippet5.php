<?php
use TikTokShop\Api\TikTokShop;

$shop = new TikTokShop(appKey: 'YOUR_APP_KEY', appSecret: 'YOUR_APP_SECRET', accessToken: 'TOKEN_A', shopCipher: 'CIPHER_A');

// Another shop, sharing the HTTP client. $shop is not changed.
$other = $shop->withShop(accessToken: 'TOKEN_B', shopCipher: 'CIPHER_B');

// An argument you leave out keeps this client's value; null (or '') clears it.
$sameShopNewToken = $shop->withShop(accessToken: 'TOKEN_A2');
$noShop = $shop->withShop(shopCipher: null);
