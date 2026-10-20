<?php

declare(strict_types=1);

namespace TikTokShop\Api\Tests;

use PHPUnit\Framework\TestCase;
use TikTokShop\Api\Generated\Model\GetConversationListRequest;
use TikTokShop\Api\Signer;
use TikTokShop\Api\Tests\Support\Stub;
use TikTokShop\Api\TikTokShop;
use TikTokShop\Api\TikTokShopAuth;
use TikTokShop\Api\TikTokShopException;

/**
 * Real sockets: PHP's built-in web server (tests/Support/router.php) and Guzzle's cURL handler. This proves what the
 * mock tests cannot: that a GET body goes over the wire, that redirects are not followed, and how transport
 * failures look.
 */
final class ServerTest extends TestCase
{
    private const SECRET = 's3cret-app-secret';

    /** @var resource|null */
    private static $process = null;
    private static int $port = 0;
    private static string $log = '';

    public static function setUpBeforeClass(): void
    {
        self::$port = self::freePort();
        self::$log = tempnam(sys_get_temp_dir(), 'stublog') ?: self::fail('no temp file');
        $cmd = [PHP_BINARY, '-S', '127.0.0.1:' . self::$port, __DIR__ . '/Support/router.php'];
        $process = proc_open(
            $cmd,
            [0 => ['pipe', 'r'], 1 => ['file', '/dev/null', 'w'], 2 => ['file', '/dev/null', 'w']],
            $pipes,
            __DIR__ . '/Support',
            ['STUB_LOG' => self::$log],
        );
        if (!is_resource($process)) {
            self::fail('could not start the PHP built-in web server');
        }
        self::$process = $process;
        for ($i = 0; $i < 100; $i++) {
            $conn = @fsockopen('127.0.0.1', self::$port, $errno, $errstr, 0.2);
            if ($conn !== false) {
                fclose($conn);

                return;
            }
            usleep(50_000);
        }
        self::fail('the PHP built-in web server did not start');
    }

    public static function tearDownAfterClass(): void
    {
        if (self::$process !== null) {
            proc_terminate(self::$process);
            proc_close(self::$process);
        }
        if (self::$log !== '') {
            @unlink(self::$log);
        }
    }

    protected function setUp(): void
    {
        file_put_contents(self::$log, '');
    }

    private static function freePort(): int
    {
        $server = stream_socket_server('tcp://127.0.0.1:0', $errno, $errstr);
        if ($server === false) {
            self::fail("no free port: $errstr");
        }
        $name = stream_socket_get_name($server, false);
        fclose($server);

        return (int) substr((string) $name, (int) strrpos((string) $name, ':') + 1);
    }

    /** @return list<array<string, mixed>> */
    private static function logged(): array
    {
        $out = [];
        foreach (file(self::$log, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES) ?: [] as $line) {
            $out[] = json_decode($line, true, 512, JSON_THROW_ON_ERROR);
        }

        return $out;
    }

    private function shop(string $prefix, ?float $timeout = null, int $port = 0): TikTokShop
    {
        return new TikTokShop(
            appKey: 'k1',
            appSecret: self::SECRET,
            accessToken: 'tok-1',
            baseUrl: 'http://127.0.0.1:' . ($port ?: self::$port) . $prefix,
            timeout: $timeout,
        );
    }

    public function testAGetBodyGoesOverTheWireAndIsSigned(): void
    {
        $this->shop('/echo')->affiliateSeller->getConversationList(
            10,
            'b2Zmc2V0PTEw+/x==',
            null,
            null,
            new GetConversationListRequest(['only_need_conversation_id' => true]),
        );

        $seen = self::logged();
        $this->assertCount(1, $seen);
        $this->assertSame('GET', $seen[0]['method']);
        $this->assertSame('{"only_need_conversation_id":true}', $seen[0]['body']);

        $query = Stub::parseQuery((string) parse_url($seen[0]['uri'], PHP_URL_QUERY));
        $this->assertContains(['page_token', 'b2Zmc2V0PTEw+/x=='], $query);
        $sign = '';
        $rest = [];
        foreach ($query as $pair) {
            if ($pair[0] === 'sign') {
                $sign = $pair[1];
            } else {
                $rest[] = $pair;
            }
        }
        $headers = array_change_key_case($seen[0]['headers'], CASE_LOWER);
        $this->assertSame('tok-1', $headers['x-tts-access-token']);
        $this->assertSame(
            Signer::sign($seen[0]['path'], $rest, $headers['content-type'], $seen[0]['body'], self::SECRET),
            $sign,
        );
    }

    public function testARedirectIsNotFollowed(): void
    {
        try {
            $this->shop('/redirect')->authorization->getAuthorizedShops();
            $this->fail('expected a TikTokShopException');
        } catch (TikTokShopException $e) {
            $this->assertSame(302, $e->getTikTokCode());
            $this->assertSame(302, $e->getHttpStatus());
        }

        $paths = array_column(self::logged(), 'path');
        $this->assertCount(1, $paths, 'only the original request reached the server');
        $this->assertStringStartsWith('/redirect', $paths[0]);
        $this->assertNotContains('/target/secret', $paths);
    }

    public function testAClosedPortIsATikTokShopExceptionWithoutTheQuery(): void
    {
        $closed = self::freePort();
        try {
            $this->shop('/x', 5.0, $closed)->orders->getOrderList(10);
            $this->fail('expected a TikTokShopException');
        } catch (TikTokShopException $e) {
            $this->assertSame(0, $e->getTikTokCode());
            $this->assertNull($e->getHttpStatus());
            $this->assertNotNull($e->getPrevious());
            $this->assertScrubbedOfRequest($e);
        }
    }

    public function testATimeoutIsATikTokShopExceptionWithoutTheQuery(): void
    {
        $started = microtime(true);
        try {
            $this->shop('/sleep-800', 0.5)->orders->getOrderList(10);
            $this->fail('expected a TikTokShopException');
        } catch (TikTokShopException $e) {
            $this->assertLessThan(2.0, microtime(true) - $started);
            $this->assertSame(0, $e->getTikTokCode());
            $this->assertStringContainsString('timed out', $e->getMessage());
            $this->assertScrubbedOfRequest($e);
        }
    }

    public function testAZeroTimeoutMeansNoLimit(): void
    {
        // The stub answers after 0.7 s; a timeout of 0 must wait for it, not give up at once.
        $result = $this->shop('/sleep-700', 0.0)->authorization->getAuthorizedShops();
        $this->assertSame('req-live', $result->getRequestId());
    }

    public function testAnAsyncClosedPortRejectsWithATikTokShopException(): void
    {
        $closed = self::freePort();
        try {
            $this->shop('/x', 5.0, $closed)->authorization->getAuthorizedShopsAsync()->wait();
            $this->fail('expected a TikTokShopException');
        } catch (TikTokShopException $e) {
            $this->assertSame(0, $e->getTikTokCode());
            $this->assertScrubbedOfRequest($e);
        }
    }

    private const CODE = 'AUTH-CODE-SECRET-0123456789';
    private const REFRESH = 'REFRESH-TOKEN-SECRET-0123456789';

    private function auth(string $prefix, ?float $timeout = null, int $port = 0): TikTokShopAuth
    {
        return new TikTokShopAuth(
            appKey: 'k1',
            appSecret: self::SECRET,
            baseUrl: 'http://127.0.0.1:' . ($port ?: self::$port) . $prefix,
            timeout: $timeout,
        );
    }

    public function testATokenCallDoesNotFollowARedirect(): void
    {
        foreach (['exchange', 'refresh'] as $kind) {
            file_put_contents(self::$log, '');
            try {
                $auth = $this->auth('/redirect');
                $kind === 'exchange' ? $auth->exchangeCode(self::CODE) : $auth->refresh(self::REFRESH);
                $this->fail('expected a TikTokShopException');
            } catch (TikTokShopException $e) {
                $this->assertSame(302, $e->getTikTokCode());
                $this->assertSame(302, $e->getHttpStatus());
            }

            $paths = array_column(self::logged(), 'path');
            $this->assertCount(1, $paths, 'only the original request reached the server');
            $this->assertNotContains('/target/secret', $paths);
        }
    }

    public function testARedirectIsNotFollowedEvenOnASuppliedClientThatFollowsThem(): void
    {
        $auth = new TikTokShopAuth('k1', self::SECRET, baseUrl: 'http://127.0.0.1:' . self::$port . '/redirect', httpClient: new \GuzzleHttp\Client(['allow_redirects' => true]));
        try {
            $auth->exchangeCode(self::CODE);
            $this->fail('expected a TikTokShopException');
        } catch (TikTokShopException $e) {
            $this->assertSame(302, $e->getTikTokCode());
        }
        $this->assertNotContains('/target/secret', array_column(self::logged(), 'path'));
    }

    public function testATokenCallToAClosedPortLeaksNoSecrets(): void
    {
        $closed = self::freePort();
        foreach (['exchange', 'refresh'] as $kind) {
            try {
                $auth = $this->auth('/x', 5.0, $closed);
                $kind === 'exchange' ? $auth->exchangeCode(self::CODE) : $auth->refresh(self::REFRESH);
                $this->fail('expected a TikTokShopException');
            } catch (TikTokShopException $e) {
                $this->assertSame(0, $e->getTikTokCode());
                $this->assertNull($e->getHttpStatus());
                $this->assertNotNull($e->getPrevious());
                AuthTest::assertNoSecrets($this, $e, [self::SECRET, self::CODE, self::REFRESH]);
            }
        }
    }

    public function testATokenCallThatTimesOutLeaksNoSecrets(): void
    {
        $started = microtime(true);
        foreach (['exchange', 'refresh'] as $kind) {
            try {
                $auth = $this->auth('/sleep-800', 0.5);
                $kind === 'exchange' ? $auth->exchangeCode(self::CODE) : $auth->refresh(self::REFRESH);
                $this->fail('expected a TikTokShopException');
            } catch (TikTokShopException $e) {
                $this->assertSame(0, $e->getTikTokCode());
                $this->assertStringContainsString('timed out', $e->getMessage());
                AuthTest::assertNoSecrets($this, $e, [self::SECRET, self::CODE, self::REFRESH]);
            }
        }
        $this->assertLessThan(3.0, microtime(true) - $started);
    }

    public function testATokenCallSendsTheDocumentedQuery(): void
    {
        try {
            $this->auth('/echo')->exchangeCode('c o+d/e=');
        } catch (TikTokShopException) {
            // The stub answers with no tokens; only what it received matters here.
        }
        $seen = self::logged();
        $this->assertCount(1, $seen);
        $this->assertSame('GET', $seen[0]['method']);
        $this->assertSame('/echo/api/v2/token/get', $seen[0]['path']);
        $this->assertSame(
            'app_key=k1&app_secret=' . self::SECRET . '&auth_code=c%20o%2Bd%2Fe%3D&grant_type=authorized_code',
            parse_url($seen[0]['uri'], PHP_URL_QUERY),
        );
    }

    private function assertScrubbedOfRequest(\Throwable $e): void
    {
        for ($t = $e; $t !== null; $t = $t->getPrevious()) {
            $this->assertStringNotContainsString('?', $t->getMessage());
            $this->assertStringNotContainsString('app_key', $t->getMessage());
            $this->assertStringNotContainsString('sign=', $t->getMessage());
            $this->assertStringNotContainsString('tok-1', $t->getMessage());
        }
        $all = (string) $e;
        $this->assertStringNotContainsString('?', $all);
        $this->assertStringNotContainsString('app_key=', $all);
        $this->assertStringNotContainsString('sign=', $all);
        $this->assertStringNotContainsString(self::SECRET, $all);
    }
}
