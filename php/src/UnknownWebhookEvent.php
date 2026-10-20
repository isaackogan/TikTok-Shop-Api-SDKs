<?php

declare(strict_types=1);

namespace TikTokShop\Api;

/** A webhook whose integer `type` this SDK does not know. Its body is in {@see WebhookEvent::getRaw()}. */
final class UnknownWebhookEvent extends WebhookEvent
{
}
