<?php

declare(strict_types=1);

namespace TikTokShop\Api;

/**
 * The tokens TikTok returns for an authorization code or a refresh token.
 *
 * **It holds secrets.** The access and refresh tokens are not properties (read them with {@see self::getAccessToken()}
 * and {@see self::getRefreshToken()}), so `var_dump`, `print_r`, `var_export` and `(array)` show neither, and
 * `serialize()` refuses. To store it, use {@see self::toArray()} (or `json_encode($tokenSet)`, which uses
 * {@see self::jsonSerialize()}) and restore it with {@see self::fromArray()}. Those hold the real token values:
 * encrypt them at rest and keep them out of logs.
 *
 * The two `*ExpireIn` values are the Unix timestamps TikTok returns, not durations.
 */
final class TokenSet implements \JsonSerializable
{
    /** @var \WeakMap<TokenSet, array{string, string}>|null */
    private static ?\WeakMap $secrets = null;

    /**
     * @param list<string> $grantedScopes
     */
    public function __construct(
        string $accessToken,
        public readonly int $accessTokenExpireIn,
        string $refreshToken,
        public readonly int $refreshTokenExpireIn,
        public readonly ?string $openId = null,
        public readonly ?string $sellerName = null,
        public readonly ?string $sellerBaseRegion = null,
        public readonly ?int $userType = null,
        public readonly array $grantedScopes = [],
    ) {
        if ($accessToken === '' || $refreshToken === '') {
            throw new \InvalidArgumentException('accessToken and refreshToken must not be empty');
        }
        self::$secrets ??= new \WeakMap();
        self::$secrets[$this] = [$accessToken, $refreshToken];
    }

    public function getAccessToken(): string
    {
        return self::$secrets[$this][0];
    }

    public function getRefreshToken(): string
    {
        return self::$secrets[$this][1];
    }

    /**
     * Every field with its real values, tokens included, under the camelCase names of the constructor.
     *
     * @return array{accessToken: string, accessTokenExpireIn: int, refreshToken: string, refreshTokenExpireIn: int, openId: ?string, sellerName: ?string, sellerBaseRegion: ?string, userType: ?int, grantedScopes: list<string>}
     */
    public function toArray(): array
    {
        return [
            'accessToken' => $this->getAccessToken(),
            'accessTokenExpireIn' => $this->accessTokenExpireIn,
            'refreshToken' => $this->getRefreshToken(),
            'refreshTokenExpireIn' => $this->refreshTokenExpireIn,
            'openId' => $this->openId,
            'sellerName' => $this->sellerName,
            'sellerBaseRegion' => $this->sellerBaseRegion,
            'userType' => $this->userType,
            'grantedScopes' => $this->grantedScopes,
        ];
    }

    /**
     * The inverse of {@see self::toArray()}.
     *
     * @param array<string, mixed> $data
     * @throws \InvalidArgumentException if a token or an expiry is missing or of the wrong type
     */
    public static function fromArray(array $data): self
    {
        $access = $data['accessToken'] ?? null;
        $refresh = $data['refreshToken'] ?? null;
        $accessExp = $data['accessTokenExpireIn'] ?? null;
        $refreshExp = $data['refreshTokenExpireIn'] ?? null;
        if (!is_string($access) || !is_string($refresh) || !is_int($accessExp) || !is_int($refreshExp)) {
            throw new \InvalidArgumentException('accessToken and refreshToken must be strings, and both expiries integers');
        }
        $scopes = $data['grantedScopes'] ?? [];

        return new self(
            $access,
            $accessExp,
            $refresh,
            $refreshExp,
            is_string($data['openId'] ?? null) ? $data['openId'] : null,
            is_string($data['sellerName'] ?? null) ? $data['sellerName'] : null,
            is_string($data['sellerBaseRegion'] ?? null) ? $data['sellerBaseRegion'] : null,
            is_int($data['userType'] ?? null) ? $data['userType'] : null,
            is_array($scopes) ? array_values(array_filter($scopes, 'is_string')) : [],
        );
    }

    /** The same as {@see self::toArray()}: real token values, see the class comment. */
    public function jsonSerialize(): array
    {
        return $this->toArray();
    }

    /** @return array<string, mixed> */
    public function __debugInfo(): array
    {
        return [
            'accessToken' => '***',
            'accessTokenExpireIn' => $this->accessTokenExpireIn,
            'refreshToken' => '***',
            'refreshTokenExpireIn' => $this->refreshTokenExpireIn,
            'openId' => $this->openId,
            'sellerName' => $this->sellerName,
            'sellerBaseRegion' => $this->sellerBaseRegion,
            'userType' => $this->userType,
            'grantedScopes' => $this->grantedScopes,
        ];
    }

    /** The tokens are keyed by object identity, so a clone would have none. A TokenSet is immutable: share it, or use {@see self::fromArray()}. */
    public function __clone(): void
    {
        throw new \LogicException('TokenSet cannot be cloned; it is immutable, so share it or rebuild it with fromArray(toArray()).');
    }

    public function __serialize(): array
    {
        throw new \LogicException('TokenSet cannot be serialized; store toArray() instead.');
    }
}
