<?php
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
