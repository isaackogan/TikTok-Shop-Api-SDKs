<?php

declare(strict_types=1);

namespace TikTokShop\Api\Tests;

use GuzzleHttp\Exception\ConnectException;
use GuzzleHttp\Psr7\Request;
use GuzzleHttp\Psr7\Response;
use PHPUnit\Framework\Attributes\DataProvider;
use PHPUnit\Framework\TestCase;
use TikTokShop\Api\Tests\Support\Stub;
use TikTokShop\Api\TikTokShop;
use TikTokShop\Api\TikTokShopAuth;
use TikTokShop\Api\TikTokShopException;

/** Cross-language rules from the final review: R13c, R13d, R21b and lesson 34. */
final class ConsistencyTest extends TestCase
{
    private const TOKEN_DATA = '"access_token":"a","access_token_expire_in":1,"refresh_token":"r","refresh_token_expire_in":2';

    private function shop(Stub $stub): TikTokShop
    {
        return new TikTokShop(appKey: 'k1', appSecret: 's', accessToken: 't', httpClient: $stub->client());
    }

    private function auth(Stub $stub): TikTokShopAuth
    {
        return new TikTokShopAuth('k1', 's', httpClient: $stub->client());
    }

    private static function raw(string $body, int $status = 200): Response
    {
        return new Response($status, ['Content-Type' => 'application/json'], $body);
    }

    // --- R13c ------------------------------------------------------------------------------------------------------

    public function testAnApiTimeoutIsMinusOneWithNoStatus(): void
    {
        $stub = (new Stub())->push(new ConnectException('cURL error 28: Operation timed out after 500 milliseconds', new Request('GET', 'http://127.0.0.1:1/')));
        try {
            $this->shop($stub)->authorization->getAuthorizedShops();
            $this->fail('expected a TikTokShopException');
        } catch (TikTokShopException $e) {
            $this->assertSame(-1, $e->getTikTokCode());
            $this->assertNull($e->getHttpStatus());
            $this->assertNotNull($e->getPrevious());
            $this->assertStringContainsString('timed out', $e->getMessage());
        }
    }

    // --- R13d ------------------------------------------------------------------------------------------------------

    public function testAWrongTypedListIsMinusOneWithStatusRequestIdAndPrevious(): void
    {
        $stub = (new Stub())->push(self::raw('{"code":0,"message":"Success","request_id":"q9","data":{"shops":"not a list"}}'));
        try {
            $this->shop($stub)->authorization->getAuthorizedShops();
            $this->fail('expected a TikTokShopException');
        } catch (TikTokShopException $e) {
            $this->assertSame(-1, $e->getTikTokCode());
            $this->assertSame(200, $e->getHttpStatus());
            $this->assertSame('q9', $e->getRequestId());
            $this->assertInstanceOf(\InvalidArgumentException::class, $e->getPrevious());
        }
    }

    public function testAnAsyncWrongTypedListRejectsWithMinusOne(): void
    {
        $stub = (new Stub())->push(self::raw('{"code":0,"message":"Success","request_id":"q10","data":{"shops":"not a list"}}'));
        try {
            $this->shop($stub)->authorization->getAuthorizedShopsAsync()->wait();
            $this->fail('expected a TikTokShopException');
        } catch (TikTokShopException $e) {
            $this->assertSame(-1, $e->getTikTokCode());
            $this->assertSame(200, $e->getHttpStatus());
            $this->assertSame('q10', $e->getRequestId());
        }
    }

    // --- lesson 34: a 2xx whose code is present but not an integer is -1 ---------------------------------------------

    /** @return array<string, array{string}> */
    public static function nonIntegerCodes(): array
    {
        return ['string' => ['"0"'], 'float' => ['1.5'], 'bool' => ['true'], 'null' => ['null'], 'object' => ['{}']];
    }

    #[DataProvider('nonIntegerCodes')]
    public function testANonIntegerCodeOnA2xxIsMinusOne(string $code): void
    {
        $stub = (new Stub())->push(self::raw('{"code":' . $code . ',"message":"m","request_id":"q5","data":{}}'));
        try {
            $this->shop($stub)->authorization->getAuthorizedShops();
            $this->fail('expected a TikTokShopException');
        } catch (TikTokShopException $e) {
            $this->assertSame([-1, 200, 'q5'], [$e->getTikTokCode(), $e->getHttpStatus(), $e->getRequestId()]);
        }
        $stub = (new Stub())->push(self::raw('{"code":' . $code . ',"request_id":"q6","data":{' . self::TOKEN_DATA . '}}'));
        try {
            $this->auth($stub)->exchangeCode('c');
            $this->fail('expected a TikTokShopException');
        } catch (TikTokShopException $e) {
            $this->assertSame([-1, 200], [$e->getTikTokCode(), $e->getHttpStatus()]);
        }
    }

    public function testA2xxWithNoCodeAtAllIsStillASuccess(): void
    {
        $stub = (new Stub())->push(self::raw('{"request_id":"q","data":{}}'));
        $this->assertNotNull($this->shop($stub)->authorization->getAuthorizedShops());
    }

    // --- lesson 34: User-Agent and granted_scopes ------------------------------------------------------------------

    public function testTheUserAgentIsSentOnApiAndTokenCalls(): void
    {
        // In this checkout Composer reports no release version, so the stamped one is used.
        $this->assertMatchesRegularExpression('~^tiktok-shop-api-php/\d+\.\d+\.\d+$~', TikTokShop::userAgent());
        $stub = (new Stub())->push(Stub::ok());
        $this->shop($stub)->authorization->getAuthorizedShops();
        $this->assertSame(TikTokShop::userAgent(), $stub->last()->getHeaderLine('User-Agent'));
        $stub = (new Stub())->push(self::raw('{"code":0,"request_id":"r","data":{' . self::TOKEN_DATA . '}}'));
        $this->auth($stub)->refresh('r');
        $this->assertSame(TikTokShop::userAgent(), $stub->last()->getHeaderLine('User-Agent'));
    }

    /** @return array<string, array{string}> */
    public static function absentScopes(): array
    {
        return ['absent' => [''], 'null' => [',"granted_scopes":null'], 'a string' => [',"granted_scopes":"x"'], 'a non-string item' => [',"granted_scopes":["a",1]']];
    }

    #[DataProvider('absentScopes')]
    public function testGrantedScopesAbsentNullOrIllTypedIsNull(string $extra): void
    {
        $stub = (new Stub())->push(self::raw('{"code":0,"request_id":"r","data":{' . self::TOKEN_DATA . $extra . '}}'));
        $tokens = $this->auth($stub)->exchangeCode('c');
        $this->assertNull($tokens->grantedScopes);
        $this->assertNull(\TikTokShop\Api\TokenSet::fromArray($tokens->toArray())->grantedScopes);
    }

    public function testWellTypedGrantedScopesAreKept(): void
    {
        $stub = (new Stub())->push(self::raw('{"code":0,"request_id":"r","data":{' . self::TOKEN_DATA . ',"granted_scopes":["a","b"]}}'));
        $this->assertSame(['a', 'b'], $this->auth($stub)->exchangeCode('c')->grantedScopes);
    }

    // --- R21b ------------------------------------------------------------------------------------------------------

    public function testAnIntegerEnumValueTheSpecDoesNotListStillDecodes(): void
    {
        $stub = (new Stub())->push(self::raw('{"code":0,"request_id":"r","data":{"creators":[{"creator_profile":{"user_type_tag":[1,3]}}]}}'));
        $res = $this->shop($stub)->affiliateSeller->searchCreatorsInCreatorMarketplace(1);
        $this->assertSame([1, 3], $res->getData()->getCreators()[0]->getCreatorProfile()->getUserTypeTag());
    }
}
