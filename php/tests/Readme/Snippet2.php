<?php
use TikTokShop\Api\TikTokShopAuth;
use TikTokShop\Api\TokenSet;

$auth = new TikTokShopAuth(appKey: 'YOUR_APP_KEY', appSecret: 'YOUR_APP_SECRET');

// Store the tokens: toArray() holds the real values, so encrypt it at rest.
$stored = json_encode($tokens->toArray());

// Later: refresh before the access token expires.
$tokens = TokenSet::fromArray(json_decode($stored, true));
$tokens = $auth->refresh($tokens->getRefreshToken());
