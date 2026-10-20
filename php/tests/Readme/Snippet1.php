<?php
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
