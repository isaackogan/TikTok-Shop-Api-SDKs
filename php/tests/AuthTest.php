<?php

declare(strict_types=1);

namespace TikTokShop\Api\Tests;

use GuzzleHttp\Exception\ConnectException;
use GuzzleHttp\Psr7\Request;
use GuzzleHttp\Psr7\Response;
use PHPUnit\Framework\Attributes\DataProvider;
use PHPUnit\Framework\TestCase;
use TikTokShop\Api\Tests\Support\Stub;
use TikTokShop\Api\TikTokShopAuth;
use TikTokShop\Api\TikTokShopException;
use TikTokShop\Api\TokenSet;

final class AuthTest extends TestCase
{
    private const SECRET = 'APP-SECRET-VALUE-0123456789';
    private const CODE = 'AUTH-CODE-SECRET-0123456789';
    private const REFRESH = 'REFRESH-TOKEN-SECRET-0123456789';

    /** @return array<string, mixed> */
    private static function vectors(): array
    {
        return json_decode((string) file_get_contents(__DIR__ . '/../../shared/test-vectors/auth.json'), true, 512, JSON_THROW_ON_ERROR);
    }

    /** @return array<string, array{array<string, mixed>}> */
    public static function urlCases(): array
    {
        $out = [];
        foreach (self::vectors()['authorizationUrls'] as $i => $case) {
            $out["$i {$case['type']} {$case['region']}"] = [$case];
        }

        return $out;
    }

    /** @return array<string, array{array<string, mixed>}> */
    public static function requestCases(): array
    {
        $out = [];
        foreach (self::vectors()['tokenRequests'] as $case) {
            $out[$case['kind']] = [$case];
        }

        return $out;
    }

    /** @return array<string, array{array<string, mixed>}> */
    public static function responseCases(): array
    {
        $out = [];
        foreach (self::vectors()['tokenResponses'] as $case) {
            $out[$case['name']] = [$case];
        }

        return $out;
    }

    /** @param array<string, mixed> $case */
    #[DataProvider('urlCases')]
    public function testAuthorizationUrlReproducesTheVector(array $case): void
    {
        $auth = new TikTokShopAuth(appKey: $case['appKey'] ?? 'unused-key', appSecret: 's', serviceId: $case['serviceId']);
        $this->assertSame($case['url'], $auth->authorizationUrl($case['type'], $case['region'], $case['state']));
    }

    public function testAnEmptyStateAddsNoStateParameter(): void
    {
        $auth = new TikTokShopAuth('k', 's', serviceId: '7123456789');
        $this->assertSame('https://services.tiktokshop.com/open/authorize?service_id=7123456789', $auth->authorizationUrl('seller', 'row', ''));
    }

    public function testASellerUrlNeedsAServiceId(): void
    {
        $this->expectException(\InvalidArgumentException::class);
        (new TikTokShopAuth('k', 's'))->authorizationUrl('seller', 'us');
    }

    public function testAnUnknownTypeOrRegionIsRejected(): void
    {
        $auth = new TikTokShopAuth('k', 's', serviceId: '1');
        foreach ([['shopper', 'us'], ['seller', 'eu']] as [$type, $region]) {
            try {
                $auth->authorizationUrl($type, $region);
                $this->fail("$type/$region should be rejected");
            } catch (\InvalidArgumentException $e) {
                $this->assertStringContainsString('unknown', $e->getMessage());
            }
        }
    }

    private function auth(Stub $stub, bool $httpErrors = true): TikTokShopAuth
    {
        return new TikTokShopAuth(appKey: '123abc', appSecret: 's3cret', httpClient: $stub->client($httpErrors));
    }

    /** @param array<string, mixed> $case */
    #[DataProvider('requestCases')]
    public function testTokenRequestsAreGetsWithThePinnedQuery(array $case): void
    {
        $stub = (new Stub())->push(Stub::ok(self::tokenData()));
        $auth = $this->auth($stub);
        $case['kind'] === 'exchange' ? $auth->exchangeCode($case['value']) : $auth->refresh($case['value']);

        $this->assertSame('GET', $stub->last()->getMethod());
        $this->assertSame($case['url'], (string) $stub->last()->getUri());
    }

    public function testTheBaseUrlIsOverridable(): void
    {
        $stub = (new Stub())->push(Stub::ok(self::tokenData()));
        $auth = new TikTokShopAuth('k', 's', baseUrl: 'http://127.0.0.1:9/some/', httpClient: $stub->client());
        $auth->exchangeCode('c');
        $this->assertSame('http://127.0.0.1:9/some/api/v2/token/get?app_key=k&app_secret=s&auth_code=c&grant_type=authorized_code', (string) $stub->last()->getUri());
    }

    public function testQueryValuesArePercentEncodedAsRfc3986(): void
    {
        $stub = (new Stub())->push(Stub::ok(self::tokenData()));
        $this->auth($stub)->exchangeCode('a b+c/d=e&f');
        $this->assertStringContainsString('auth_code=a%20b%2Bc%2Fd%3De%26f&', (string) $stub->last()->getUri());
    }

    /** @param array<string, mixed> $case */
    #[DataProvider('responseCases')]
    public function testTokenResponseVector(array $case): void
    {
        foreach ([true, false] as $httpErrors) {
            $stub = (new Stub())->push(new Response(200, [], $case['body']));
            $auth = $this->auth($stub, $httpErrors);
            if ($case['errorCode'] !== null) {
                try {
                    $auth->exchangeCode('c');
                    $this->fail('expected a TikTokShopException');
                } catch (TikTokShopException $e) {
                    $this->assertSame($case['errorCode'], $e->getTikTokCode());
                    $this->assertSame($case['errorCode'], $e->getCode());
                    $this->assertSame('r2', $e->getRequestId());
                    $this->assertSame(200, $e->getHttpStatus());
                }
                continue;
            }
            $this->assertSame($case['expected'], $auth->exchangeCode('c')->toArray());
        }
    }

    /** @return array<string, mixed> */
    private static function tokenData(): array
    {
        return ['access_token' => 'AT-1', 'access_token_expire_in' => 1000, 'refresh_token' => 'RT-1', 'refresh_token_expire_in' => 2000];
    }

    /** R14: only the four token fields are required. */
    public function testAMinimalFourFieldResponseSucceeds(): void
    {
        $stub = (new Stub())->push(Stub::ok(self::tokenData()));
        $tokens = $this->auth($stub)->exchangeCode('c');

        $this->assertSame('AT-1', $tokens->getAccessToken());
        $this->assertSame(1000, $tokens->accessTokenExpireIn);
        $this->assertSame('RT-1', $tokens->getRefreshToken());
        $this->assertSame(2000, $tokens->refreshTokenExpireIn);
        $this->assertNull($tokens->openId);
        $this->assertNull($tokens->sellerName);
        $this->assertNull($tokens->sellerBaseRegion);
        $this->assertNull($tokens->userType);
        $this->assertSame([], $tokens->grantedScopes);
    }

    public function testNullOptionalFieldsBecomeNull(): void
    {
        $stub = (new Stub())->push(Stub::ok(self::tokenData() + [
            'open_id' => null, 'seller_name' => null, 'seller_base_region' => null, 'user_type' => null, 'granted_scopes' => null,
        ]));
        $tokens = $this->auth($stub)->exchangeCode('c');

        $this->assertNull($tokens->openId);
        $this->assertNull($tokens->sellerName);
        $this->assertNull($tokens->sellerBaseRegion);
        $this->assertNull($tokens->userType);
        $this->assertSame([], $tokens->grantedScopes);
    }

    public function testWrongTypedOptionalFieldsAreTreatedAsAbsent(): void
    {
        $stub = (new Stub())->push(Stub::ok(self::tokenData() + [
            'open_id' => true, 'seller_name' => 5, 'seller_base_region' => ['US'], 'user_type' => 'x', 'granted_scopes' => ['a', 1, null, 'b'],
        ]));
        $tokens = $this->auth($stub)->exchangeCode('c');

        $this->assertNull($tokens->openId);
        $this->assertNull($tokens->sellerName);
        $this->assertNull($tokens->sellerBaseRegion);
        $this->assertNull($tokens->userType);
        $this->assertSame(['a', 'b'], $tokens->grantedScopes);
    }

    public function testAnOpenIdSentAsANumberKeepsItsExactDigits(): void
    {
        foreach (['7494049642642441621', '92233720368547758079'] as $digits) {
            $body = '{"code":0,"message":"success","request_id":"r","data":{"access_token":"AT","access_token_expire_in":1,'
                . '"refresh_token":"RT","refresh_token_expire_in":2,"open_id":' . $digits . '}}';
            $stub = (new Stub())->push(new Response(200, [], $body));
            $this->assertSame($digits, $this->auth($stub)->exchangeCode('c')->openId);
        }
    }

    /** @return array<string, array{string}> a `data` object that must be rejected */
    public static function illTypedData(): array
    {
        // The four required fields with one of them replaced by raw JSON, or removed when `$raw` is null.
        $build = static function (string $field, ?string $raw): string {
            $pairs = [];
            foreach (['access_token' => '"AT"', 'access_token_expire_in' => '1', 'refresh_token' => '"RT"', 'refresh_token_expire_in' => '2'] as $key => $value) {
                if ($key === $field) {
                    if ($raw === null) {
                        continue;
                    }
                    $value = $raw;
                }
                $pairs[] = "\"$key\":$value";
            }

            return '{' . implode(',', $pairs) . '}';
        };
        $out = ['all missing' => ['{}']];
        $tokenKinds = ['missing' => null, 'null' => 'null', 'empty' => '""', 'number' => '5', 'bool' => 'true', 'array' => '["x"]'];
        foreach (['access_token', 'refresh_token'] as $field) {
            foreach ($tokenKinds as $kind => $raw) {
                $out["$field $kind"] = [$build($field, $raw)];
            }
        }
        $expiryKinds = ['missing' => null, 'null' => 'null', 'string' => '"123"', 'float' => '1.5', 'float zero' => '1.0', 'exponent' => '1e3', 'bool' => 'true', 'array' => '[1]'];
        foreach (['access_token_expire_in', 'refresh_token_expire_in'] as $field) {
            foreach ($expiryKinds as $kind => $raw) {
                $out["$field $kind"] = [$build($field, $raw)];
            }
        }

        return $out;
    }

    #[DataProvider('illTypedData')]
    public function testAMissingOrIllTypedRequiredFieldIsMinusOneKeepingTheRequestId(string $data): void
    {
        foreach ([true, false] as $httpErrors) {
            $stub = (new Stub())->push(new Response(200, [], '{"code":0,"message":"success","request_id":"rq-1","data":' . $data . '}'));
            try {
                $this->auth($stub, $httpErrors)->refresh('r');
                $this->fail('expected a TikTokShopException');
            } catch (TikTokShopException $e) {
                $this->assertSame(-1, $e->getTikTokCode());
                $this->assertSame('rq-1', $e->getRequestId());
                $this->assertSame(200, $e->getHttpStatus());
            }
        }
    }

    /** @return array<string, array{int, string, int, ?string, string}> status, body, expected code, expected message, request id */
    public static function failures(): array
    {
        return [
            '503 with only a message' => [503, '{"message":"x"}', 503, 'x', ''],
            '503 with code 0' => [503, '{"code":0}', 503, null, ''],
            '503 not json' => [503, 'upstream down', 503, null, ''],
            '503 empty' => [503, '', 503, null, ''],
            '503 with a TikTok code' => [503, '{"code":12345,"message":"m","request_id":"r9"}', 12345, 'm', 'r9'],
            '400 with a TikTok code' => [400, '{"code":36004004,"message":"bad","request_id":"r8"}', 36004004, 'bad', 'r8'],
            '200 not json' => [200, 'not json', -1, null, ''],
            '200 json list' => [200, '[]', -1, null, ''],
            '200 code 0 without data' => [200, '{"code":0,"message":"ok","request_id":"r7"}', -1, null, 'r7'],
            '200 code 0 with data as a list' => [200, '{"code":0,"data":[]}', -1, null, ''],
            '200 with a TikTok code' => [200, '{"code":36004004,"message":"invalid","request_id":"r6","data":{}}', 36004004, 'invalid', 'r6'],
        ];
    }

    #[DataProvider('failures')]
    public function testFailuresFollowR13b(int $status, string $body, int $code, ?string $message, string $requestId): void
    {
        foreach ([true, false] as $httpErrors) {
            $stub = (new Stub())->push(new Response($status, [], $body));
            try {
                $this->auth($stub, $httpErrors)->exchangeCode('c');
                $this->fail('expected a TikTokShopException');
            } catch (TikTokShopException $e) {
                $this->assertSame($code, $e->getTikTokCode());
                $this->assertSame($status, $e->getHttpStatus());
                $this->assertSame($requestId, $e->getRequestId());
                if ($message !== null) {
                    $this->assertSame($message, $e->getMessage());
                }
            }
        }
    }

    public function testARedirectIsAFailureWithTheStatusAsItsCode(): void
    {
        $stub = (new Stub())->push(new Response(302, ['Location' => 'http://evil.example/steal']));
        try {
            $this->auth($stub)->exchangeCode('c');
            $this->fail('expected a TikTokShopException');
        } catch (TikTokShopException $e) {
            $this->assertSame(302, $e->getTikTokCode());
            $this->assertSame(302, $e->getHttpStatus());
        }
    }

    public function testTokenCallsAskNotToFollowRedirectsEvenOnASuppliedClient(): void
    {
        // A supplied client that would follow redirects and throw on 4xx/5xx.
        $stub = (new Stub())->push(Stub::ok(self::tokenData()), Stub::ok(self::tokenData()));
        $auth = new TikTokShopAuth('k', 's', httpClient: new \GuzzleHttp\Client([
            'handler' => $stub->client()->getConfig('handler'),
            'allow_redirects' => true,
            'http_errors' => true,
        ]));
        $auth->exchangeCode('c');
        $auth->refresh('r');

        $this->assertCount(2, $stub->history);
        foreach ($stub->history as $entry) {
            $this->assertFalse($entry['options']['allow_redirects']);
            $this->assertFalse($entry['options']['http_errors']);
        }
    }

    /** @return array<string, array{\Throwable}> */
    public static function transportErrors(): array
    {
        $url = 'http://127.0.0.1:1/api/v2/token/%s?app_key=123abc&app_secret=' . self::SECRET . '&%s=%s&grant_type=%s';
        $make = static fn (string $message): \Throwable => new ConnectException($message, new Request('GET', 'http://127.0.0.1:1/'));

        return [
            'refused' => [$make('cURL error 7: Failed to connect to 127.0.0.1 port 1 after 0 ms: Connection refused (see https://curl.haxx.se/libcurl/c/libcurl-errors.html) for ' . $url)],
            'timeout' => [$make('cURL error 28: Operation timed out after 500 milliseconds with 0 bytes received (see https://curl.haxx.se/libcurl/c/libcurl-errors.html) for ' . $url)],
        ];
    }

    #[DataProvider('transportErrors')]
    public function testATransportErrorLeaksNoSecretsOnExchangeOrRefresh(\Throwable $failure): void
    {
        foreach (['exchange', 'refresh'] as $kind) {
            // The message holds the URL with all three secrets, as Guzzle's does.
            $message = sprintf($failure->getMessage(), $kind === 'exchange' ? 'get' : 'refresh', $kind === 'exchange' ? 'auth_code' : 'refresh_token', $kind === 'exchange' ? self::CODE : self::REFRESH, $kind === 'exchange' ? 'authorized_code' : 'refresh_token');
            $this->assertStringContainsString(self::SECRET, $message, 'the fixture must contain the secret');
            $stub = (new Stub())->push(new ConnectException($message, new Request('GET', 'http://127.0.0.1:1/')));
            $auth = new TikTokShopAuth('123abc', self::SECRET, httpClient: $stub->client());
            try {
                $kind === 'exchange' ? $auth->exchangeCode(self::CODE) : $auth->refresh(self::REFRESH);
                $this->fail('expected a TikTokShopException');
            } catch (TikTokShopException $e) {
                $this->assertSame(0, $e->getTikTokCode());
                $this->assertNull($e->getHttpStatus());
                $this->assertNotNull($e->getPrevious());
                self::assertNoSecrets($this, $e, [self::SECRET, self::CODE, self::REFRESH]);
            }
        }
    }

    /** No secret anywhere in the message, `(string)$e` or any `getPrevious()`, not even its first characters (a stack trace cuts long arguments). */
    /** @param list<string> $secrets */
    public static function assertNoSecrets(TestCase $test, \Throwable $e, array $secrets): void
    {
        $all = (string) $e;
        for ($t = $e; $t !== null; $t = $t->getPrevious()) {
            $all .= "\n" . $t->getMessage() . "\n" . (string) $t;
        }
        foreach ($secrets as $secret) {
            $test->assertStringNotContainsString($secret, $all);
            $test->assertStringNotContainsString(substr($secret, 0, 10), $all);
        }
        $test->assertStringNotContainsString('app_secret=', $all);
        $test->assertStringNotContainsString('auth_code=', $all);
        $test->assertStringNotContainsString('refresh_token=', $all);
    }

    public function testTheTokenSetHoldsItsFieldsAndCanBeStored(): void
    {
        $original = new TokenSet('AT', 11, 'RT', 22, '7494049642642441621', 'Shop', 'US', 1, ['a.read']);
        $array = $original->toArray();
        $this->assertSame('AT', $array['accessToken']);
        $this->assertSame('RT', $array['refreshToken']);

        $again = TokenSet::fromArray(json_decode(json_encode($original, JSON_THROW_ON_ERROR), true, 512, JSON_THROW_ON_ERROR));
        $this->assertSame($array, $again->toArray());
        $this->assertSame('AT', $again->getAccessToken());
    }

    public function testFromArrayRejectsAnIllTypedStore(): void
    {
        $this->expectException(\InvalidArgumentException::class);
        TokenSet::fromArray(['accessToken' => 'AT', 'accessTokenExpireIn' => '1', 'refreshToken' => 'RT', 'refreshTokenExpireIn' => 2]);
    }

    public function testTheTokenSetAndTheAuthNeverPrintTheirSecrets(): void
    {
        $tokens = new TokenSet('ACCESS-TOKEN-SECRET-VALUE', 11, 'REFRESH-TOKEN-SECRET-VALUE', 22);
        $auth = new TikTokShopAuth('public-key', self::SECRET, serviceId: '1');
        $secrets = ['ACCESS-TOKEN-SECRET-VALUE', 'REFRESH-TOKEN-SECRET-VALUE', self::SECRET];

        foreach ([$tokens, $auth] as $object) {
            ob_start();
            var_dump($object);
            $text = (string) ob_get_clean();
            ob_start();
            print_r($object);
            $text .= (string) ob_get_clean();
            set_error_handler(static fn (): bool => true);
            try {
                ob_start();
                var_export($object);
                $text .= (string) ob_get_clean();
            } finally {
                restore_error_handler();
            }
            $text .= json_encode((array) $object, JSON_PARTIAL_OUTPUT_ON_ERROR) ?: '';
            foreach ($secrets as $secret) {
                $this->assertStringNotContainsString($secret, $text);
            }
            $this->assertStringContainsString('***', $text);
        }
        $this->expectException(\LogicException::class);
        serialize($tokens);
    }

    public function testATokenSetCannotBeCloned(): void
    {
        $this->expectException(\LogicException::class);
        $tokens = new TokenSet('AT', 1, 'RT', 2);
        $copy = clone $tokens;
        $this->assertNotNull($copy);
    }
}
