<?php

declare(strict_types=1);

namespace TikTokShop\Api;

/**
 * A parsed webhook. {@see Webhooks::parse()} returns one of the classes in `Generated\Event` (one per webhook the
 * spec describes, each with a typed `getPayload()`), or an {@see UnknownWebhookEvent}. Narrow with `instanceof`.
 */
abstract class WebhookEvent
{
    /** @param array<string, mixed> $raw */
    public function __construct(
        private readonly int $type,
        private readonly array $raw,
    ) {
    }

    /** The integer `type` of the webhook, e.g. 1 for `ORDER_STATUS_CHANGE`. */
    public function getType(): int
    {
        return $this->type;
    }

    /**
     * The body decoded to an array, exactly as received: unknown fields included. 64-bit IDs that do not fit a PHP
     * integer are strings.
     *
     * @return array<string, mixed>
     */
    public function getRaw(): array
    {
        return $this->raw;
    }
}
