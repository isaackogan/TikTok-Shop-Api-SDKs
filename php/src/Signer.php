<?php

declare(strict_types=1);

namespace TikTokShop\Api;

/** TikTok Shop request signing. Pure: no state, no I/O. */
final class Signer
{
    /** Parameters that never take part in the signature. */
    private const EXCLUDED = ['sign' => true, 'access_token' => true];

    private function __construct()
    {
    }

    /**
     * secret + path + sorted `key + value` pairs + body (not multipart) + secret.
     *
     * @param list<array{string, string}> $query Decoded `[key, value]` pairs, in any order.
     * @param string|null $body The exact body bytes, or null for none.
     */
    public static function stringToSign(
        string $path,
        array $query,
        ?string $contentType,
        ?string $body,
        string $appSecret,
    ): string {
        $pairs = [];
        foreach ($query as $pair) {
            if (!isset(self::EXCLUDED[(string) $pair[0]])) {
                $pairs[] = [(string) $pair[0], (string) $pair[1]];
            }
        }
        // usort is stable since PHP 8.0, so repeated keys keep their order.
        usort($pairs, static fn (array $a, array $b): int => strcmp($a[0], $b[0]));

        $s = $appSecret . $path;
        foreach ($pairs as [$k, $v]) {
            $s .= $k . $v;
        }
        if (!self::isMultipart($contentType)) {
            $s .= $body ?? '';
        }

        return $s . $appSecret;
    }

    /**
     * Lowercase hex HMAC-SHA256 of {@see self::stringToSign()}, keyed with the app secret.
     *
     * @param list<array{string, string}> $query
     */
    public static function sign(
        string $path,
        array $query,
        ?string $contentType,
        ?string $body,
        string $appSecret,
    ): string {
        return hash_hmac('sha256', self::stringToSign($path, $query, $contentType, $body, $appSecret), $appSecret);
    }

    /** Whether the media type is `multipart/form-data`, ignoring parameters such as the boundary. */
    public static function isMultipart(?string $contentType): bool
    {
        return $contentType !== null && str_starts_with(strtolower(ltrim($contentType)), 'multipart/form-data');
    }
}
