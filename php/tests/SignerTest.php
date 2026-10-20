<?php

declare(strict_types=1);

namespace TikTokShop\Api\Tests;

use PHPUnit\Framework\Attributes\DataProvider;
use PHPUnit\Framework\TestCase;
use TikTokShop\Api\Operations;
use TikTokShop\Api\Signer;

final class SignerTest extends TestCase
{
    /** @return array<string, array{array<string, mixed>}> */
    public static function vectors(): array
    {
        $json = json_decode((string) file_get_contents(__DIR__ . '/../../shared/test-vectors/signing.json'), true, 512, JSON_THROW_ON_ERROR);
        $out = [];
        foreach ($json['cases'] as $case) {
            $out[$case['name']] = [$case];
        }

        return $out;
    }

    /** @param array<string, mixed> $case */
    #[DataProvider('vectors')]
    public function testStringToSignMatchesTheVector(array $case): void
    {
        $this->assertSame(
            $case['stringToSign'],
            Signer::stringToSign($case['path'], $case['query'], $case['contentType'], $case['body'], $case['secret']),
        );
    }

    /** @param array<string, mixed> $case */
    #[DataProvider('vectors')]
    public function testSignMatchesTheVector(array $case): void
    {
        $this->assertSame(
            $case['sign'],
            Signer::sign($case['path'], $case['query'], $case['contentType'], $case['body'], $case['secret']),
        );
    }

    public function testMultipartIgnoresTheBoundaryAndCase(): void
    {
        $this->assertTrue(Signer::isMultipart('multipart/form-data; boundary=xyz'));
        $this->assertTrue(Signer::isMultipart('Multipart/Form-Data'));
        $this->assertFalse(Signer::isMultipart('application/json'));
        $this->assertFalse(Signer::isMultipart(null));
    }

    /** @return array<string, array{string, string, bool}> */
    public static function cipherCases(): array
    {
        return [
            'order search needs the cipher' => ['POST', '/order/202309/orders/search', true],
            'authorized shops does not' => ['GET', '/authorization/202309/shops', false],
            'a templated product path does' => ['GET', '/product/202309/products/1729507467923261408', true],
            'method is case-insensitive' => ['post', '/order/202309/orders/search', true],
            'an unknown path does not' => ['GET', '/nope/202309/unknown', false],
            'a template matches one segment only' => ['GET', '/product/202309/products/1/2/3', false],
        ];
    }

    #[DataProvider('cipherCases')]
    public function testRequiresShopCipher(string $method, string $path, bool $expected): void
    {
        $this->assertSame($expected, Operations::requiresShopCipher($method, $path));
    }
}
