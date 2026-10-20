<?php

declare(strict_types=1);

namespace TikTokShop\Api;

use TikTokShop\Api\Generated\Meta;

/** Looks up API operations by HTTP method and path. */
final class Operations
{
    /** @var list<array{method: string, regex: string, literals: int, needsShopCipher: bool}>|null */
    private static ?array $matchers = null;

    private function __construct()
    {
    }

    /**
     * Whether the operation matching `$method` and `$path` takes a `shop_cipher` query parameter. `{x}` in a path
     * template matches exactly one segment, the method compare is case-insensitive, and the template with the
     * most literal segments wins.
     */
    public static function requiresShopCipher(string $method, string $path): bool
    {
        $m = strtoupper($method);
        $best = null;
        foreach (self::matchers() as $x) {
            if ($x['method'] === $m && preg_match($x['regex'], $path) === 1
                && ($best === null || $x['literals'] > $best['literals'])) {
                $best = $x;
            }
        }

        return $best !== null && $best['needsShopCipher'];
    }

    /** @return list<array{method: string, regex: string, literals: int, needsShopCipher: bool}> */
    private static function matchers(): array
    {
        if (self::$matchers !== null) {
            return self::$matchers;
        }
        $out = [];
        foreach (Meta::OPERATIONS as [, , $method, $path, $needs]) {
            $parts = [];
            $literals = 0;
            foreach (explode('/', $path) as $segment) {
                if (preg_match('/^\{[^}]+\}$/', $segment) === 1) {
                    $parts[] = '[^/]+';
                } else {
                    $parts[] = preg_quote($segment, '~');
                    $literals++;
                }
            }
            $out[] = [
                'method' => $method,
                'regex' => '~^' . implode('/', $parts) . '$~',
                'literals' => $literals,
                'needsShopCipher' => $needs,
            ];
        }

        return self::$matchers = $out;
    }
}
