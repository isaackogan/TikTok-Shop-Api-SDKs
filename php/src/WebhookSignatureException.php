<?php

declare(strict_types=1);

namespace TikTokShop\Api;

/** The webhook signature did not match. Thrown by {@see Webhooks::verifyAndParse()}. */
final class WebhookSignatureException extends \RuntimeException
{
    public function __construct(string $message = 'webhook signature does not match')
    {
        parent::__construct($message);
    }
}
