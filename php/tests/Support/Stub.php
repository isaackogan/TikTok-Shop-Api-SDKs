<?php

declare(strict_types=1);

namespace TikTokShop\Api\Tests\Support;

use GuzzleHttp\Client;
use GuzzleHttp\Handler\MockHandler;
use GuzzleHttp\HandlerStack;
use GuzzleHttp\Middleware;
use GuzzleHttp\Psr7\Response;
use Psr\Http\Message\RequestInterface;
use TikTokShop\Api\Signer;

/** An in-process HTTP stub: Guzzle's MockHandler plus a history of the requests it received. */
final class Stub
{
    /** @var list<array{request: RequestInterface, options: array<string, mixed>}> */
    public array $history = [];

    private MockHandler $mock;

    public function __construct()
    {
        $this->mock = new MockHandler();
    }

    public function push(mixed ...$items): self
    {
        $this->mock->append(...$items);

        return $this;
    }

    /**
     * A user-supplied client that records into {@see self::$history}. `$httpErrors` is Guzzle's own default (on)
     * unless a test turns it off, so both paths of the SDK's error handling can be exercised.
     */
    public function client(bool $httpErrors = true): Client
    {
        $stack = HandlerStack::create($this->mock);
        $stack->push(Middleware::history($this->history));

        return new Client(['handler' => $stack, 'http_errors' => $httpErrors, 'allow_redirects' => false]);
    }

    public function last(): RequestInterface
    {
        \PHPUnit\Framework\Assert::assertNotEmpty($this->history, 'the stub received no request');

        return $this->history[array_key_last($this->history)]['request'];
    }

    public static function ok(mixed $data = null): Response
    {
        return self::json(['code' => 0, 'message' => 'Success', 'request_id' => 'req-ok', 'data' => $data ?? new \stdClass()]);
    }

    public static function json(mixed $body, int $status = 200): Response
    {
        return new Response($status, ['Content-Type' => 'application/json'], json_encode($body, JSON_THROW_ON_ERROR));
    }

    /**
     * The decoded query pairs of a request, as the server receives them: percent-decoded, `+` stays `+`.
     *
     * @return list<array{string, string}>
     */
    public static function query(RequestInterface $request): array
    {
        return self::parseQuery($request->getUri()->getQuery());
    }

    /** @return list<array{string, string}> */
    public static function parseQuery(string $raw): array
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

    /** The values of one query parameter, in order. @return list<string> */
    public static function values(RequestInterface $request, string $name): array
    {
        $out = [];
        foreach (self::query($request) as [$k, $v]) {
            if ($k === $name) {
                $out[] = $v;
            }
        }

        return $out;
    }

    /** The `sign` the request carries, and the `sign` recomputed from everything else the request carries. @return array{string, string} */
    public static function signs(RequestInterface $request, string $appSecret): array
    {
        $given = '';
        $rest = [];
        foreach (self::query($request) as $pair) {
            if ($pair[0] === 'sign') {
                $given = $pair[1];
            } else {
                $rest[] = $pair;
            }
        }
        $contentType = $request->hasHeader('Content-Type') ? $request->getHeaderLine('Content-Type') : null;

        return [$given, Signer::sign($request->getUri()->getPath(), $rest, $contentType, (string) $request->getBody(), $appSecret)];
    }
}
