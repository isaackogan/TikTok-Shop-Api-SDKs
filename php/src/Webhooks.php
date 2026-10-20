<?php

declare(strict_types=1);

namespace TikTokShop\Api;

use TikTokShop\Api\Generated\Meta;
use TikTokShop\Api\Generated\WebhookEvents;

/**
 * Verifies and parses TikTok Shop webhooks.
 *
 * ```php
 * $event = Webhooks::verifyAndParse($appKey, $appSecret, $rawBody, $authorizationHeader);
 * if ($event instanceof OrderStatusChangeEvent) {
 *     $orderId = $event->getPayload()->getData()->getOrderId();
 * }
 * ```
 *
 * @phpstan-import-type WebhookEventUnion from WebhookEvents
 * @psalm-import-type WebhookEventUnion from WebhookEvents
 */
final class Webhooks
{
    /** Webhook type => event name, e.g. `1 => 'ORDER_STATUS_CHANGE'`. */
    public const EVENT_TYPES = Meta::EVENT_TYPES;

    /**
     * Checks the `Authorization` header: lowercase hex HMAC-SHA256 (key: the app secret) over `$appKey . $rawBody`,
     * compared in constant time. A null or empty signature is false.
     *
     * @param string $rawBody The body exactly as received. Never re-serialize it.
     */
    public static function verify(string $appKey, string $appSecret, string $rawBody, ?string $signature): bool
    {
        if ($signature === null || $signature === '') {
            return false;
        }

        return hash_equals(hash_hmac('sha256', $appKey . $rawBody, $appSecret), $signature);
    }

    /**
     * Parses a body to its event, picked by the integer `type`. A `type` this SDK does not know gives an
     * {@see UnknownWebhookEvent}. 64-bit IDs keep their exact digits, and unknown fields are accepted. Narrow the
     * result with `instanceof`, e.g. `$event instanceof OrderStatusChangeEvent`, then call `getPayload()`.
     *
     * @return WebhookEvent
     * @phpstan-return WebhookEventUnion
     * @psalm-return WebhookEventUnion
     *
     * @throws \InvalidArgumentException if the body is not a JSON object, its `type` is missing or not an integer (a
     *     string, boolean, null, fraction or array), or the body does not fit its model (a required property is missing
     *     or null)
     */
    public static function parse(string $rawBody): WebhookEvent
    {
        $flags = JSON_BIGINT_AS_STRING | JSON_THROW_ON_ERROR;
        try {
            $json = json_decode($rawBody, false, 512, $flags);
            $raw = json_decode($rawBody, true, 512, $flags);
        } catch (\JsonException $e) {
            throw new \InvalidArgumentException('webhook body is not valid JSON: ' . $e->getMessage(), 0, $e);
        }
        if (!$json instanceof \stdClass || !is_array($raw)) {
            throw new \InvalidArgumentException('webhook body is not a JSON object');
        }
        if (!property_exists($json, 'type') || !is_int($json->type)) {
            throw new \InvalidArgumentException('webhook "type" is missing or not an integer');
        }
        $type = $json->type;

        $known = WebhookEvents::TYPES[$type] ?? null;
        if ($known === null) {
            return new UnknownWebhookEvent($type, $raw);
        }
        [$eventClass, $modelClass, $schema] = $known;

        $missing = self::firstMissing($schema, $json, '');
        if ($missing !== null) {
            throw new \InvalidArgumentException("webhook of type $type does not match its model: required property \"$missing\" is missing");
        }
        try {
            // ObjectSerializer reads only the properties a model knows, so unknown fields are ignored, and it turns a
            // 64-bit ID that arrived as a JSON number into its string property with settype(), digit for digit.
            $payload = Generated\ObjectSerializer::deserialize($json, $modelClass);
        } catch (\Throwable $e) {
            throw new \InvalidArgumentException("webhook of type $type does not match its model: " . $e->getMessage(), 0, $e);
        }

        return new $eventClass($raw, $payload);
    }

    /**
     * Verifies, then parses.
     *
     * @return WebhookEvent
     * @phpstan-return WebhookEventUnion
     * @psalm-return WebhookEventUnion
     *
     * @throws WebhookSignatureException if the signature does not match
     * @throws \InvalidArgumentException as {@see self::parse()}
     */
    public static function verifyAndParse(string $appKey, string $appSecret, string $rawBody, ?string $signature): WebhookEvent
    {
        if (!self::verify($appKey, $appSecret, $rawBody, $signature)) {
            throw new WebhookSignatureException();
        }

        return self::parse($rawBody);
    }

    /**
     * The first required property the JSON lacks (a missing key and a JSON null both count), as a dotted path, or null.
     * Recurses into nested objects, lists and maps; a value of an unexpected shape is left to the decoder.
     */
    private static function firstMissing(string $model, \stdClass $json, string $path): ?string
    {
        $entry = WebhookEvents::REQUIRED[$model] ?? null;
        if ($entry === null) {
            return null;
        }
        [$required, $children] = $entry;
        foreach ($required as $name) {
            if (!property_exists($json, $name) || $json->{$name} === null) {
                return $path . $name;
            }
        }
        foreach ($children as $name => [$kind, $childModel]) {
            if (!property_exists($json, $name)) {
                continue;
            }
            $value = $json->{$name};
            $found = null;
            if ($kind === 'object') {
                $found = $value instanceof \stdClass ? self::firstMissing($childModel, $value, "$path$name.") : null;
            } else {
                $items = $kind === 'map' && $value instanceof \stdClass ? get_object_vars($value) : ($kind === 'list' && is_array($value) ? $value : []);
                foreach ($items as $item) {
                    if ($item instanceof \stdClass && ($found = self::firstMissing($childModel, $item, "$path$name.")) !== null) {
                        break;
                    }
                }
            }
            if ($found !== null) {
                return $found;
            }
        }

        return null;
    }
}
