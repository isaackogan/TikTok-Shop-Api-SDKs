<?php

declare(strict_types=1);

namespace TikTokShop\Api;

use GuzzleHttp\Client;
use GuzzleHttp\ClientInterface;
use GuzzleHttp\Psr7\Request;
use Psr\Http\Message\ResponseInterface;

/**
 * The OAuth helper: authorization URLs, code exchange and token refresh.
 *
 * ```php
 * $auth = new TikTokShopAuth(appKey: '...', appSecret: '...', serviceId: '...');
 * $url = $auth->authorizationUrl(TikTokShopAuth::SELLER, TikTokShopAuth::US, state: 'csrf-token');
 * $tokens = $auth->exchangeCode($codeFromTheRedirect);
 * ```
 *
 * Every failure is a {@see TikTokShopException}. Its message and previous exceptions never contain the request URL
 * or the app secret, the code or the refresh token (the token requests carry them in the URL's query). On PHP 8.2+ they
 * are also hidden from stack traces (`#[\SensitiveParameter]`).
 *
 * HTTP client: by default the SDK builds a Guzzle client with the given timeout and Guzzle's default proxy behaviour.
 * A client you pass as `$httpClient` is used as is (its timeout, proxy and TLS settings apply, `$timeout` is ignored),
 * except that the token calls never follow redirects, even on that client, because the URL holds the app secret and
 * the code: a 3xx reply is thrown with code 302 (the status) and the redirect target receives nothing.
 *
 * Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.
 */
final class TikTokShopAuth
{
    public const DEFAULT_BASE_URL = 'https://auth.tiktok-shops.com';

    /** Seconds, used when no `$timeout` is given. */
    public const DEFAULT_TIMEOUT = 30.0;

    /** Authorizes your app for a seller. Needs a service ID. */
    public const SELLER = 'seller';
    /** Authorizes your app for a partner. Needs a service ID. */
    public const PARTNER = 'partner';
    /** Authorizes your app for an affiliate creator. */
    public const CREATOR = 'creator';

    /** The United States host. */
    public const US = 'us';
    /** The rest-of-world host. */
    public const ROW = 'row';

    /** type => [US host, rest-of-world host, path]. */
    private const PAGES = [
        self::SELLER => ['https://services.us.tiktokshop.com', 'https://services.tiktokshop.com', '/open/authorize'],
        self::PARTNER => ['https://partner.us.tiktokshop.com', 'https://partner.tiktokshop.com', '/open/authorize'],
        self::CREATOR => ['https://shop.tiktok.com', 'https://shop.tiktok.com', '/alliance/creator/auth'],
    ];

    private readonly Credentials $credentials;
    private readonly ?string $serviceId;
    private readonly string $baseUrl;
    private readonly ClientInterface $httpClient;

    /**
     * @param string|null $serviceId Your Partner Center service ID. Needed for {@see self::SELLER} and {@see self::PARTNER} URLs.
     * @param string|null $baseUrl Overrides {@see self::DEFAULT_BASE_URL}, e.g. for a test server.
     * @param float|null $timeout Seconds for one request, for the client the SDK builds. 0 means no limit.
     * @param ClientInterface|null $httpClient A Guzzle client to use as is, see the class comment.
     */
    public function __construct(
        string $appKey,
        #[\SensitiveParameter] string $appSecret,
        ?string $serviceId = null,
        ?string $baseUrl = null,
        ?float $timeout = null,
        ?ClientInterface $httpClient = null,
    ) {
        if ($timeout !== null && $timeout < 0) {
            throw new \InvalidArgumentException('timeout must not be negative (0 means no limit)');
        }
        $this->credentials = new Credentials($appKey, $appSecret);
        $this->serviceId = $serviceId === '' ? null : $serviceId;
        $this->baseUrl = rtrim($baseUrl === null || $baseUrl === '' ? self::DEFAULT_BASE_URL : $baseUrl, '/');
        $this->httpClient = $httpClient ?? new Client([
            'allow_redirects' => false,
            'http_errors' => false,
            'timeout' => $timeout ?? self::DEFAULT_TIMEOUT,
            'connect_timeout' => $timeout ?? self::DEFAULT_TIMEOUT,
        ]);
    }

    /**
     * The page to send the seller (or partner, or creator) to.
     *
     * @param string $type {@see self::SELLER}, {@see self::PARTNER} or {@see self::CREATOR}
     * @param string $region {@see self::US} or {@see self::ROW}
     * @param string|null $state Echoed back to your redirect URL. Null or empty adds no `state` parameter.
     * @throws \InvalidArgumentException for an unknown type or region, or a seller or partner URL without a service ID
     */
    public function authorizationUrl(string $type, string $region, ?string $state = null): string
    {
        $page = self::PAGES[$type] ?? throw new \InvalidArgumentException("unknown authorization type \"$type\" (seller, partner or creator)");
        if ($region !== self::US && $region !== self::ROW) {
            throw new \InvalidArgumentException("unknown region \"$region\" (us or row)");
        }
        $url = $page[$region === self::US ? 0 : 1] . $page[2] . '?';
        if ($type === self::CREATOR) {
            $url .= 'app_key=' . rawurlencode($this->credentials->appKey);
        } else {
            if ($this->serviceId === null) {
                throw new \InvalidArgumentException("serviceId is required for $type authorization URLs");
            }
            $url .= 'service_id=' . rawurlencode($this->serviceId);
        }
        if ($state !== null && $state !== '') {
            $url .= '&state=' . rawurlencode($state);
        }

        return $url;
    }

    /**
     * Trades the `auth_code` from your redirect URL for tokens.
     *
     * @throws TikTokShopException for every failure
     */
    public function exchangeCode(#[\SensitiveParameter] string $code): TokenSet
    {
        return $this->token('get', 'auth_code', $code, 'authorized_code');
    }

    /**
     * Trades a refresh token for new tokens.
     *
     * @throws TikTokShopException for every failure
     */
    public function refresh(#[\SensitiveParameter] string $refreshToken): TokenSet
    {
        return $this->token('refresh', 'refresh_token', $refreshToken, 'refresh_token');
    }

    private function token(string $endpoint, string $name, #[\SensitiveParameter] string $value, string $grantType): TokenSet
    {
        $where = "token request to /api/v2/token/$endpoint";
        // The query is built by hand (RFC 3986, in the pinned order).
        $query = 'app_key=' . rawurlencode($this->credentials->appKey)
            . '&app_secret=' . rawurlencode($this->credentials->appSecret())
            . '&' . $name . '=' . rawurlencode($value)
            . '&grant_type=' . $grantType;
        $request = new Request('GET', "{$this->baseUrl}/api/v2/token/$endpoint?$query", ['User-Agent' => TikTokShop::userAgent()]);
        try {
            // Per request, so it holds on a client you supplied: a redirect would carry the secret and the code on.
            $response = $this->httpClient->send($request, ['allow_redirects' => false, 'http_errors' => false]);
        } catch (\Throwable $e) {
            throw $this->failure($where, $e, [$this->credentials->appSecret(), $value]);
        }

        return $this->toTokenSet($response);
    }

    /** R13b, and R14 for the fields. */
    private function toTokenSet(ResponseInterface $response): TokenSet
    {
        $status = $response->getStatusCode();
        $ok = $status >= 200 && $status < 300;
        $text = (string) $response->getBody();

        $env = null;
        $parseError = null;
        try {
            $env = json_decode($text, false, 512, JSON_BIGINT_AS_STRING | JSON_THROW_ON_ERROR);
        } catch (\JsonException $e) {
            $parseError = $e;
        }
        if (!$env instanceof \stdClass) {
            // A non-2xx reply (a redirect included, since it is never followed) has the HTTP status as its code whatever
            // the body; only an unreadable 2xx is -1.
            throw new TikTokShopException(
                "unparseable token response (HTTP $status)",
                $ok ? -1 : $status,
                '',
                $status,
                $parseError,
            );
        }
        $requestId = isset($env->request_id) && is_string($env->request_id) ? $env->request_id : '';
        $message = isset($env->message) && is_string($env->message) ? $env->message : '';
        $hasCode = property_exists($env, 'code');
        $code = $hasCode && is_int($env->code) ? $env->code : null;
        if ($ok && $hasCode && $code === null) {
            // Lesson 34: a code that is present but not an integer makes the reply unreadable.
            throw new TikTokShopException("token response has a non-integer code (HTTP $status)", -1, $requestId, $status);
        }

        if (!$ok || ($code !== null && $code !== 0)) {
            throw new TikTokShopException(
                $message !== '' ? $message : "HTTP $status",
                $code !== null && $code !== 0 ? $code : ($ok ? -1 : $status),
                $requestId,
                $status,
            );
        }
        $data = $env->data ?? null;
        if (!$data instanceof \stdClass) {
            throw new TikTokShopException('token response has no data', -1, $requestId, $status);
        }

        $access = $data->access_token ?? null;
        $refresh = $data->refresh_token ?? null;
        $accessExp = $data->access_token_expire_in ?? null;
        $refreshExp = $data->refresh_token_expire_in ?? null;
        if (!is_string($access) || $access === '' || !is_string($refresh) || $refresh === ''
            || !is_int($accessExp) || !is_int($refreshExp)) {
            throw new TikTokShopException(
                'token response is missing a token field, or one has the wrong type',
                -1,
                $requestId,
                $status,
            );
        }

        // Optional fields: anything of the wrong type is treated as absent. open_id is an ID, so a number keeps its digits
        // (json_decode gives a number beyond 64 bits as a string already).
        $openId = $data->open_id ?? null;
        $scopes = $data->granted_scopes ?? null;

        return new TokenSet(
            $access,
            $accessExp,
            $refresh,
            $refreshExp,
            is_string($openId) || is_int($openId) ? (string) $openId : null,
            isset($data->seller_name) && is_string($data->seller_name) ? $data->seller_name : null,
            isset($data->seller_base_region) && is_string($data->seller_base_region) ? $data->seller_base_region : null,
            isset($data->user_type) && is_int($data->user_type) ? $data->user_type : null,
            // Lesson 34: absent, null or ill-typed (not a list of strings) granted_scopes is null, never [].
            is_array($scopes) && array_is_list($scopes) && count(array_filter($scopes, 'is_string')) === count($scopes) ? $scopes : null,
        );
    }

    /**
     * The exception for a failed send: a fresh previous exception with a scrubbed message. Guzzle's own exception holds the
     * request, and with it the URL and its query, so it is dropped.
     *
     * @param list<string> $secrets
     */
    private function failure(string $where, \Throwable $e, #[\SensitiveParameter] array $secrets): TikTokShopException
    {
        $raw = $e->getMessage();
        $clean = preg_replace('~(\bhttps?://[^\s?#]*)\?[^\s)]*~i', '$1', $raw) ?? $raw;
        $clean = preg_replace('~[?&](?:app_key|app_secret|auth_code|refresh_token|grant_type)=[^\s&)]*~', '', $clean) ?? $clean;
        foreach ($secrets as $secret) {
            if (strlen($secret) >= 4) {
                $clean = str_replace([$secret, rawurlencode($secret)], '***', $clean);
            }
        }
        $timedOut = stripos($raw, 'timed out') !== false || stripos($raw, 'timeout') !== false;

        return new TikTokShopException(
            "$where " . ($timedOut ? 'timed out' : 'failed') . ' (' . $e::class . "): $clean",
            -1,
            '',
            null,
            new \RuntimeException($clean),
        );
    }

    /** @return array<string, mixed> */
    public function __debugInfo(): array
    {
        return [
            'credentials' => $this->credentials,
            'serviceId' => $this->serviceId,
            'baseUrl' => $this->baseUrl,
        ];
    }
}
