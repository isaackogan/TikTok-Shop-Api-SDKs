<?php

declare(strict_types=1);

namespace TikTokShop\Api;

/**
 * The app key, app secret, access token and shop cipher of a client.
 *
 * The secrets are not properties: var_dump, print_r, var_export, serialize, json_encode and (array) casts show
 * none of them. {@see self::__debugInfo()} masks them for debug output.
 */
final class Credentials
{
    /** @var \WeakMap<Credentials, array{string, ?string, ?string}>|null */
    private static ?\WeakMap $secrets = null;

    public function __construct(
        public readonly string $appKey,
        string $appSecret,
        ?string $accessToken = null,
        ?string $shopCipher = null,
    ) {
        self::$secrets ??= new \WeakMap();
        self::$secrets[$this] = [
            $appSecret,
            $accessToken === '' ? null : $accessToken,
            $shopCipher === '' ? null : $shopCipher,
        ];
    }

    public function appSecret(): string
    {
        return self::$secrets[$this][0];
    }

    public function accessToken(): ?string
    {
        return self::$secrets[$this][1];
    }

    public function shopCipher(): ?string
    {
        return self::$secrets[$this][2];
    }

    /** A copy with another access token and/or shop cipher. {@see Keep::Current} keeps the current value; `null` or `''` clears it. */
    public function with(string|null|Keep $accessToken = Keep::Current, string|null|Keep $shopCipher = Keep::Current): self
    {
        return new self(
            $this->appKey,
            $this->appSecret(),
            $accessToken instanceof Keep ? $this->accessToken() : $accessToken,
            $shopCipher instanceof Keep ? $this->shopCipher() : $shopCipher,
        );
    }

    /** @return array<string, mixed> */
    public function __debugInfo(): array
    {
        return [
            'appKey' => $this->appKey,
            'appSecret' => '***',
            'accessToken' => $this->accessToken() === null ? null : '***',
            'shopCipher' => $this->shopCipher() === null ? null : '***',
        ];
    }

    public function __serialize(): array
    {
        throw new \LogicException('Credentials cannot be serialized.');
    }
}
