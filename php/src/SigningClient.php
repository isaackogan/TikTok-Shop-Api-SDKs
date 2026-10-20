<?php

declare(strict_types=1);

namespace TikTokShop\Api;

use GuzzleHttp\ClientInterface;
use GuzzleHttp\Exception\BadResponseException;
use GuzzleHttp\Exception\GuzzleException;
use GuzzleHttp\Promise\Create;
use GuzzleHttp\Promise\PromiseInterface;
use GuzzleHttp\Psr7\MultipartStream;
use GuzzleHttp\Psr7\Request;
use GuzzleHttp\Psr7\Utils;
use Psr\Http\Message\RequestInterface;
use Psr\Http\Message\ResponseInterface;

/**
 * A Guzzle client that signs every request and turns every failure into a {@see TikTokShopException}.
 *
 * It wraps another client and is what each generated `*Api` class is given. Each {@see TikTokShop} has its own
 * (it carries that shop's credentials), while {@see TikTokShop::withShop()} shares the wrapped client.
 *
 * Request hook, in order:
 *  1. drop any `app_key`, `timestamp`, `sign` and `shop_cipher` from the query;
 *  2. add `shop_cipher` when the operation takes one and the client has one;
 *  3. add `app_key` and `timestamp`;
 *  4. set `x-tts-access-token` when the client has a token;
 *  5. sign the final path, decoded query, content type and exact body bytes (a multipart body is never read);
 *  6. add `sign`. The query is built by hand with RFC 3986 percent-encoding, so `+` and `/` survive.
 *
 * Response hook: R13b, see {@see TikTokShopException}.
 *
 * @internal
 */
final class SigningClient implements ClientInterface
{
    private const RESERVED = ['app_key', 'timestamp', 'sign', 'shop_cipher'];

    public function __construct(
        private readonly ClientInterface $inner,
        private readonly Credentials $credentials,
    ) {
    }

    public function send(RequestInterface $request, array $options = []): ResponseInterface
    {
        $signed = $this->prepare($request);
        try {
            $response = $this->inner->send($signed, $options);
        } catch (\Throwable $e) {
            throw $this->failure($e, $signed);
        }

        return $this->check($response);
    }

    public function sendAsync(RequestInterface $request, array $options = []): PromiseInterface
    {
        try {
            $signed = $this->prepare($request);
        } catch (\Throwable $e) {
            return Create::rejectionFor($e);
        }

        return $this->inner->sendAsync($signed, $options)->then(
            fn (ResponseInterface $response): ResponseInterface => $this->check($response),
            function (mixed $reason) use ($signed): never {
                throw $this->failure($reason, $signed);
            },
        );
    }

    /** Only `headers` and `body` are supported in `$options`; build anything else into a PSR-7 request. */
    public function request(string $method, $uri = '', array $options = []): ResponseInterface
    {
        [$request, $rest] = $this->psr7($method, $uri, $options);

        return $this->send($request, $rest);
    }

    /** See {@see self::request()}. */
    public function requestAsync(string $method, $uri = '', array $options = []): PromiseInterface
    {
        [$request, $rest] = $this->psr7($method, $uri, $options);

        return $this->sendAsync($request, $rest);
    }

    public function getConfig(?string $option = null)
    {
        return $this->inner->getConfig($option);
    }

    /** @return array{RequestInterface, array<string, mixed>} */
    private function psr7(string $method, mixed $uri, array $options): array
    {
        foreach (['json', 'form_params', 'multipart', 'query'] as $unsupported) {
            if (array_key_exists($unsupported, $options)) {
                throw new \InvalidArgumentException(
                    "The `$unsupported` request option is not supported; pass a PSR-7 request to send() instead.",
                );
            }
        }
        $headers = $options['headers'] ?? [];
        $body = $options['body'] ?? null;
        unset($options['headers'], $options['body']);

        return [new Request($method, $uri, $headers, $body), $options];
    }

    private function prepare(RequestInterface $request): RequestInterface
    {
        $uri = $request->getUri();
        $path = $uri->getPath();
        $c = $this->credentials;

        // 1. drop reserved parameters
        $query = [];
        foreach (self::parseQuery($uri->getQuery()) as $pair) {
            if (!in_array($pair[0], self::RESERVED, true)) {
                $query[] = $pair;
            }
        }
        // 2. shop_cipher
        if ($c->shopCipher() !== null && Operations::requiresShopCipher($request->getMethod(), $path)) {
            $query[] = ['shop_cipher', $c->shopCipher()];
        }
        // 3. app_key, timestamp
        $query[] = ['app_key', $c->appKey];
        $query[] = ['timestamp', (string) time()];
        // 4. access token
        if ($c->accessToken() !== null) {
            $request = $request->withHeader('x-tts-access-token', $c->accessToken());
        }
        // 5. sign over the final path, decoded query and body bytes
        $body = $request->getBody();
        if ($body instanceof MultipartStream && !$request->hasHeader('Content-Type')) {
            $request = $request->withHeader('Content-Type', 'multipart/form-data; boundary=' . $body->getBoundary());
        }
        $contentType = $request->hasHeader('Content-Type') ? $request->getHeaderLine('Content-Type') : null;
        $bytes = null;
        if (!Signer::isMultipart($contentType)) {
            // Read the exact bytes and hand back a fresh stream, so the position is right for the transport.
            $bytes = (string) $body;
            $request = $request->withBody(Utils::streamFor($bytes));
        }
        // 6. sign
        $query[] = ['sign', Signer::sign($path, $query, $contentType, $bytes, $c->appSecret())];

        $parts = [];
        foreach ($query as [$k, $v]) {
            $parts[] = rawurlencode($k) . '=' . rawurlencode($v);
        }

        return $request->withUri($uri->withQuery(implode('&', $parts)));
    }

    /**
     * Parse a raw query string into decoded pairs. A literal `+` stays a `+`.
     *
     * @return list<array{string, string}>
     */
    private static function parseQuery(string $raw): array
    {
        $out = [];
        foreach (explode('&', $raw) as $part) {
            if ($part === '') {
                continue;
            }
            $i = strpos($part, '=');
            $out[] = $i === false
                ? [rawurldecode($part), '']
                : [rawurldecode(substr($part, 0, $i)), rawurldecode(substr($part, $i + 1))];
        }

        return $out;
    }

    /** Pass a 2xx reply with `code` 0 through; throw for anything else. */
    private function check(ResponseInterface $response): ResponseInterface
    {
        $text = (string) $response->getBody();
        $error = $this->interpret($response, $text);
        if ($error !== null) {
            throw $error;
        }

        // The body was consumed: hand the caller a fresh stream.
        return $response->withBody(Utils::streamFor($text));
    }

    /** R13b. */
    private function interpret(ResponseInterface $response, string $text): ?TikTokShopException
    {
        $status = $response->getStatusCode();
        $ok = $status >= 200 && $status < 300;

        $envelope = null;
        $parseError = null;
        try {
            $envelope = json_decode($text, false, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $e) {
            $parseError = $e;
        }
        $isObject = $envelope instanceof \stdClass;

        if ($ok && !$isObject) {
            return new TikTokShopException("Response is not valid JSON (HTTP $status)", -1, '', $status, $parseError);
        }
        $hasCode = $isObject && property_exists($envelope, 'code');
        $code = $hasCode && is_int($envelope->code) ? $envelope->code : null;
        $message = $isObject && isset($envelope->message) && is_string($envelope->message) ? $envelope->message : null;
        $requestId = $isObject && isset($envelope->request_id) && is_string($envelope->request_id) ? $envelope->request_id : '';

        if (!$ok) {
            $reason = $response->getReasonPhrase();

            return new TikTokShopException(
                $message ?? ($reason !== '' ? $reason : "HTTP $status"),
                $code !== null && $code !== 0 ? $code : $status,
                $requestId,
                $status,
            );
        }
        if ($hasCode && $code === null) {
            // Lesson 34: a code that is present but not an integer makes the reply unreadable.
            return new TikTokShopException("Response has a non-integer code (HTTP $status)", -1, $requestId, $status);
        }
        if ($code !== null && $code !== 0) {
            return new TikTokShopException($message ?? '', $code, $requestId, $status);
        }

        return null;
    }

    /** The exception to throw for a failed send. */
    private function failure(mixed $reason, RequestInterface $request): \Throwable
    {
        if ($reason instanceof BadResponseException) {
            // A 4xx/5xx from a client with http_errors on: interpret the reply, never the exception (it holds the URL).
            $response = $reason->getResponse();

            return $this->interpret($response, (string) $response->getBody())
                ?? new TikTokShopException('HTTP ' . $response->getStatusCode(), $response->getStatusCode(), '', $response->getStatusCode());
        }
        if ($reason instanceof \Throwable && !$reason instanceof GuzzleException) {
            return $reason; // already a TikTokShopException, or a programming error
        }

        $raw = $reason instanceof \Throwable ? $reason->getMessage() : (is_scalar($reason) ? (string) $reason : 'unknown error');
        $clean = $this->scrub($raw, $request);
        $timedOut = stripos($raw, 'timed out') !== false || stripos($raw, 'timeout') !== false;
        $kind = $reason instanceof \Throwable ? $reason::class : 'error';

        // A fresh previous exception: Guzzle's own holds the request, and with it the URL.
        return new TikTokShopException(
            ($timedOut ? 'Request timed out' : 'Request failed') . " ($kind): $clean",
            -1,
            '',
            null,
            new \RuntimeException($clean),
        );
    }

    /** Strip the request URL's query, and every secret, out of a transport error message. */
    private function scrub(string $message, RequestInterface $request): string
    {
        $uri = $request->getUri();
        $message = str_replace((string) $uri, (string) $uri->withQuery('')->withFragment(''), $message);
        $message = preg_replace('~(\bhttps?://[^\s?#]*)\?[^\s)]*~i', '$1', $message) ?? $message;
        $message = preg_replace('~[?&](?:app_key|timestamp|sign|shop_cipher)=[^\s&)]*~', '', $message) ?? $message;
        $c = $this->credentials;
        foreach ([$c->appSecret(), $c->accessToken(), $c->shopCipher()] as $secret) {
            if ($secret !== null && $secret !== '') {
                $message = str_replace([$secret, rawurlencode($secret)], '***', $message);
            }
        }

        return $message;
    }
}
