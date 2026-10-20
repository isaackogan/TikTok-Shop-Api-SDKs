<?php

declare(strict_types=1);

namespace TikTokShop\Api\Tests;

use GuzzleHttp\Exception\ConnectException;
use GuzzleHttp\Psr7\Request;
use GuzzleHttp\Psr7\Response;
use PHPUnit\Framework\Attributes\DataProvider;
use PHPUnit\Framework\TestCase;
use TikTokShop\Api\Credentials;
use TikTokShop\Api\Generated\Model\GetConversationListRequest;
use TikTokShop\Api\Generated\Model\PredictProductPackageDimensionsAndWeightRequest;
use TikTokShop\Api\SigningClient;
use TikTokShop\Api\Tests\Support\Stub;
use TikTokShop\Api\TikTokShop;
use TikTokShop\Api\TikTokShopException;

final class ClientTest extends TestCase
{
    private const SECRET = 's3cret-app-secret';

    private function shop(Stub $stub, bool $httpErrors = true): TikTokShop
    {
        return new TikTokShop(
            appKey: 'k1',
            appSecret: self::SECRET,
            accessToken: 'tok-1',
            shopCipher: 'cipher-1',
            httpClient: $stub->client($httpErrors),
        );
    }

    public function testAuthorizedShopsIsSignedAndHasNoShopCipher(): void
    {
        $stub = (new Stub())->push(Stub::ok(['shops' => []]));
        $this->shop($stub)->authorization->getAuthorizedShops();

        $req = $stub->last();
        $this->assertSame('GET', $req->getMethod());
        $this->assertSame('/authorization/202309/shops', $req->getUri()->getPath());
        $this->assertSame(['k1'], Stub::values($req, 'app_key'));
        $this->assertEqualsWithDelta(time(), (int) Stub::values($req, 'timestamp')[0], 5);
        $this->assertSame([], Stub::values($req, 'shop_cipher'));
        $this->assertSame('tok-1', $req->getHeaderLine('x-tts-access-token'));
        [$given, $expected] = Stub::signs($req, self::SECRET);
        $this->assertMatchesRegularExpression('/^[0-9a-f]{64}$/', $given);
        $this->assertSame($expected, $given);
    }

    public function testOrderListSendsTheShopCipher(): void
    {
        $stub = (new Stub())->push(Stub::ok(['orders' => []]));
        $this->shop($stub)->orders->getOrderList(10);

        $req = $stub->last();
        $this->assertSame('/order/202309/orders/search', $req->getUri()->getPath());
        $this->assertSame(['cipher-1'], Stub::values($req, 'shop_cipher'));
        $this->assertSame(['10'], Stub::values($req, 'page_size'));
        [$given, $expected] = Stub::signs($req, self::SECRET);
        $this->assertSame($expected, $given);
    }

    public function testAGetWithABodySendsTheBodySigned(): void
    {
        $stub = (new Stub())->push(Stub::ok(['conversations' => []]));
        $this->shop($stub)->affiliateSeller->getConversationList(
            10,
            null,
            null,
            null,
            new GetConversationListRequest(['only_need_conversation_id' => true]),
        );

        $req = $stub->last();
        $this->assertSame('GET', $req->getMethod());
        $this->assertSame('{"only_need_conversation_id":true}', (string) $req->getBody());
        $this->assertStringContainsString('application/json', $req->getHeaderLine('Content-Type'));
        [$given, $expected] = Stub::signs($req, self::SECRET); // signs() reads the body it received
        $this->assertSame($expected, $given);
        // and the body is part of the signature
        $without = \TikTokShop\Api\Signer::sign(
            $req->getUri()->getPath(),
            array_values(array_filter(Stub::query($req), static fn (array $p): bool => $p[0] !== 'sign')),
            $req->getHeaderLine('Content-Type'),
            '',
            self::SECRET,
        );
        $this->assertNotSame($without, $given);
    }

    public function testAPageTokenWithPlusSlashAndEqualsArrivesIntactAndSigned(): void
    {
        $stub = (new Stub())->push(Stub::ok(['conversations' => []]));
        $this->shop($stub)->affiliateSeller->getConversationList(10, 'b2Zmc2V0PTEw+/x==');

        $req = $stub->last();
        $this->assertSame(['b2Zmc2V0PTEw+/x=='], Stub::values($req, 'page_token'));
        $this->assertStringContainsString('page_token=b2Zmc2V0PTEw%2B%2Fx%3D%3D', $req->getUri()->getQuery());
        $this->assertStringNotContainsString('page_token=b2Zmc2V0PTEw+', $req->getUri()->getQuery());
        [$given, $expected] = Stub::signs($req, self::SECRET);
        $this->assertSame($expected, $given);
    }

    public function testAnEnvelopeWithACodeRaisesTheException(): void
    {
        $stub = (new Stub())->push(Stub::json(['code' => 36009003, 'message' => 'invalid', 'request_id' => 'r1', 'data' => new \stdClass()]));
        try {
            $this->shop($stub)->orders->getOrderList(10);
            $this->fail('expected a TikTokShopException');
        } catch (TikTokShopException $e) {
            $this->assertSame(36009003, $e->getTikTokCode());
            $this->assertSame(36009003, $e->getCode());
            $this->assertSame('invalid', $e->getMessage());
            $this->assertSame('r1', $e->getRequestId());
            $this->assertSame(200, $e->getHttpStatus());
        }
    }

    /** @return array<string, array{int, string, int, string, string}> */
    public static function replies(): array
    {
        return [
            '503 json without a code' => [503, '{"message":"x"}', 503, 'x', ''],
            '503 with code 0' => [503, '{"code":0}', 503, 'Service Unavailable', ''],
            '503 not json' => [503, 'upstream down', 503, 'Service Unavailable', ''],
            '503 empty body' => [503, '', 503, 'Service Unavailable', ''],
            '503 with a TikTok code' => [503, '{"code":12345,"message":"m","request_id":"r9"}', 12345, 'm', 'r9'],
            '302 redirect' => [302, '', 302, 'Found', ''],
            '200 not json' => [200, 'not json', -1, 'Response is not valid JSON (HTTP 200)', ''],
            '200 empty body' => [200, '', -1, 'Response is not valid JSON (HTTP 200)', ''],
            '200 json array' => [200, '[]', -1, 'Response is not valid JSON (HTTP 200)', ''],
            '200 with a TikTok code' => [200, '{"code":98765,"message":"bad","request_id":"r2"}', 98765, 'bad', 'r2'],
        ];
    }

    /** R13b, on a client that throws for 4xx/5xx (Guzzle's default) and on one that does not. */
    #[DataProvider('replies')]
    public function testEveryFailedReplyIsATikTokShopException(int $status, string $body, int $code, string $message, string $requestId): void
    {
        foreach ([true, false] as $httpErrors) {
            $stub = (new Stub())->push(new Response($status, $status === 302 ? ['Location' => 'https://elsewhere.test/'] : [], $body));
            try {
                $this->shop($stub, $httpErrors)->authorization->getAuthorizedShops();
                $this->fail('expected a TikTokShopException');
            } catch (TikTokShopException $e) {
                $this->assertSame($code, $e->getTikTokCode(), "code (http_errors=$httpErrors)");
                $this->assertSame($message, $e->getMessage());
                $this->assertSame($requestId, $e->getRequestId());
                $this->assertSame($status, $e->getHttpStatus());
            }
        }
    }

    public function testANonJsonReplyKeepsTheParseErrorAsPrevious(): void
    {
        $stub = (new Stub())->push(new Response(200, [], 'not json'));
        try {
            $this->shop($stub)->authorization->getAuthorizedShops();
            $this->fail('expected a TikTokShopException');
        } catch (TikTokShopException $e) {
            $this->assertInstanceOf(\JsonException::class, $e->getPrevious());
        }
    }

    public function testReservedParametersAreReplacedByTheClientsOwn(): void
    {
        $stub = (new Stub())->push(Stub::ok());
        $client = new SigningClient($stub->client(), new Credentials('k1', self::SECRET, 'tok-1', 'cipher-1'));
        $client->send(new Request(
            'POST',
            'https://open-api.tiktokglobalshop.com/order/202309/orders/search?app_key=evil&sign=x&timestamp=1&shop_cipher=bad&page_size=5',
        ));

        $req = $stub->last();
        $this->assertSame(['k1'], Stub::values($req, 'app_key'));
        $this->assertSame(['cipher-1'], Stub::values($req, 'shop_cipher'));
        $this->assertCount(1, Stub::values($req, 'timestamp'));
        $this->assertNotSame('1', Stub::values($req, 'timestamp')[0]);
        $this->assertCount(1, Stub::values($req, 'sign'));
        $this->assertNotSame('x', Stub::values($req, 'sign')[0]);
        $this->assertSame(['5'], Stub::values($req, 'page_size'));
        [$given, $expected] = Stub::signs($req, self::SECRET);
        $this->assertSame($expected, $given);
    }

    public function testMultipartUploadIsSignedWithoutItsBody(): void
    {
        $file = tempnam(sys_get_temp_dir(), 'img');
        file_put_contents($file, "PNGDATA\r\n\x00\x01binary");
        try {
            $stub = (new Stub())->push(Stub::ok());
            $this->shop($stub)->products->uploadProductImage(new \SplFileObject($file), 'MAIN_IMAGE');
        } finally {
            unlink($file);
        }

        $req = $stub->last();
        $contentType = $req->getHeaderLine('Content-Type');
        $this->assertMatchesRegularExpression('~^multipart/form-data; boundary=\S+$~', $contentType);
        $boundary = substr($contentType, strlen('multipart/form-data; boundary='));
        $body = (string) $req->getBody();
        $this->assertStringContainsString("--$boundary\r\n", $body);
        $this->assertStringContainsString("PNGDATA\r\n\x00\x01binary", $body);
        $this->assertStringEndsWith("--$boundary--\r\n", $body);

        $query = array_values(array_filter(Stub::query($req), static fn (array $p): bool => $p[0] !== 'sign'));
        $given = Stub::values($req, 'sign')[0];
        $this->assertSame(
            \TikTokShop\Api\Signer::sign($req->getUri()->getPath(), $query, $contentType, null, self::SECRET),
            $given,
        );
        // The body is not part of the string to sign, so it does not matter what it is.
        $this->assertStringNotContainsString('PNGDATA', \TikTokShop\Api\Signer::stringToSign($req->getUri()->getPath(), $query, $contentType, $body, self::SECRET));
    }

    public function testUnknownFieldsInAResponseStillDecode(): void
    {
        $stub = (new Stub())->push(Stub::json([
            'code' => 0,
            'message' => 'Success',
            'request_id' => 'r',
            'brand_new_top_level' => 1,
            'data' => [
                'shops' => [['id' => '1', 'name' => 'n', 'cipher' => 'c', 'brand_new_in_shop' => ['a' => 1]]],
                'brand_new_in_data' => true,
            ],
        ]));
        $result = $this->shop($stub)->authorization->getAuthorizedShops();

        $shop = $result->getData()->getShops()[0];
        $this->assertSame('1', $shop->getId());
        $this->assertSame('c', $shop->getCipher());
    }

    public function testUnknownFieldsInsideANestedModelWithRequiredPropertiesStillDecode(): void
    {
        $stub = (new Stub())->push(Stub::json([
            'code' => 0,
            'message' => 'Success',
            'request_id' => 'r',
            'data' => [
                'package_dimensions' => ['length' => 3, 'width' => 2, 'height' => 1, 'unit' => 'CM', 'brand_new' => 'x'],
                'package_weight' => ['unit' => 'KILOGRAM', 'value' => '0.5', 'brand_new' => ['y' => 1]],
                'brand_new_in_data' => 1,
            ],
        ]));
        $request = new PredictProductPackageDimensionsAndWeightRequest(['category_id' => '1']);
        $result = $this->shop($stub)->products->predictProductPackageDimensionsAndWeight($request);

        $data = $result->getData();
        $this->assertSame(3, $data->getPackageDimensions()->getLength());
        $this->assertSame('CM', $data->getPackageDimensions()->getUnit());
        $this->assertSame('0.5', $data->getPackageWeight()->getValue());
    }

    public function testATransportErrorNeverCarriesTheQuery(): void
    {
        $url = 'https://open-api.tiktokglobalshop.com/order/202309/orders/search?app_key=k1&sign=abc123&shop_cipher=cipher-1&timestamp=1';
        $stub = (new Stub())->push(new ConnectException(
            "cURL error 7: Failed to connect (see https://curl.haxx.se/libcurl/c/libcurl-errors.html) for $url",
            new Request('GET', $url),
        ));
        try {
            $this->shop($stub)->orders->getOrderList(10);
            $this->fail('expected a TikTokShopException');
        } catch (TikTokShopException $e) {
            $this->assertSame(0, $e->getTikTokCode());
            $this->assertNull($e->getHttpStatus());
            self::assertScrubbed($e);
            $this->assertStringContainsString('cURL error 7', $e->getMessage());
        }
    }

    public function testWithShopKeepsReplacesAndClears(): void
    {
        $stub = (new Stub())->push(Stub::ok(), Stub::ok(), Stub::ok(), Stub::ok(), Stub::ok(), Stub::ok());
        $a = $this->shop($stub);

        // keep: leaving an argument out keeps this client's value
        $keepAll = $a->withShop();
        $keepAll->orders->getOrderList(1);
        $this->assertSame('tok-1', $stub->last()->getHeaderLine('x-tts-access-token'));
        $this->assertSame(['cipher-1'], Stub::values($stub->last(), 'shop_cipher'));

        // replace one, keep the other
        $b = $a->withShop(accessToken: 'tok-2');
        $b->orders->getOrderList(1);
        $this->assertSame('tok-2', $stub->last()->getHeaderLine('x-tts-access-token'));
        $this->assertSame(['cipher-1'], Stub::values($stub->last(), 'shop_cipher'));
        $c = $a->withShop(shopCipher: 'cipher-2');
        $c->orders->getOrderList(1);
        $this->assertSame('tok-1', $stub->last()->getHeaderLine('x-tts-access-token'));
        $this->assertSame(['cipher-2'], Stub::values($stub->last(), 'shop_cipher'));

        // clear: an explicit null (or '') removes the value
        $d = $a->withShop(shopCipher: null);
        $d->orders->getOrderList(1);
        $this->assertSame([], Stub::values($stub->last(), 'shop_cipher'));
        $this->assertSame('tok-1', $stub->last()->getHeaderLine('x-tts-access-token'));
        $e = $a->withShop(accessToken: '');
        $e->orders->getOrderList(1);
        $this->assertFalse($stub->last()->hasHeader('x-tts-access-token'));
        $this->assertSame(['cipher-1'], Stub::values($stub->last(), 'shop_cipher'));

        // the original is untouched, and every call went through the one shared client
        $a->orders->getOrderList(1);
        $this->assertSame('tok-1', $stub->last()->getHeaderLine('x-tts-access-token'));
        $this->assertSame(['cipher-1'], Stub::values($stub->last(), 'shop_cipher'));
        $this->assertCount(6, $stub->history);
        $this->assertNotSame($a, $b);
    }

    public function testANegativeTimeoutIsRejected(): void
    {
        $this->expectException(\InvalidArgumentException::class);
        new TikTokShop(appKey: 'k', appSecret: 's', timeout: -1.0);
    }

    /** Asserts that neither the message nor the previous chain nor the string form holds a query or a secret. */
    public static function assertScrubbed(\Throwable $e): void
    {
        $all = (string) $e;
        for ($t = $e; $t !== null; $t = $t->getPrevious()) {
            self::assertStringNotContainsString('?', $t->getMessage());
            self::assertStringNotContainsString('sign=', $t->getMessage());
            self::assertStringNotContainsString('app_key', $t->getMessage());
            self::assertStringNotContainsString('cipher-1', $t->getMessage());
            self::assertStringNotContainsString('abc123', $t->getMessage());
        }
        self::assertStringNotContainsString('?', $all);
        self::assertStringNotContainsString('sign=', $all);
        self::assertStringNotContainsString('app_key=', $all);
        self::assertStringNotContainsString('cipher-1', $all);
        self::assertStringNotContainsString(self::SECRET, $all);
    }
}
