<?php

declare(strict_types=1);

namespace TikTokShop\Api\Tests;

use PHPUnit\Framework\TestCase;
use TikTokShop\Api\Credentials;
use TikTokShop\Api\TikTokShop;

final class RedactionTest extends TestCase
{
    private const SECRETS = ['APP-SECRET-VALUE', 'ACCESS-TOKEN-VALUE', 'SHOP-CIPHER-VALUE'];

    private function shop(): TikTokShop
    {
        return new TikTokShop(appKey: 'public-app-key', appSecret: 'APP-SECRET-VALUE', accessToken: 'ACCESS-TOKEN-VALUE', shopCipher: 'SHOP-CIPHER-VALUE');
    }

    private function assertNoSecrets(string $text): void
    {
        foreach (self::SECRETS as $secret) {
            $this->assertStringNotContainsString($secret, $text);
        }
    }

    public function testVarDumpAndPrintRMaskTheSecrets(): void
    {
        foreach ([$this->shop(), new Credentials('public-app-key', 'APP-SECRET-VALUE', 'ACCESS-TOKEN-VALUE', 'SHOP-CIPHER-VALUE')] as $object) {
            ob_start();
            var_dump($object);
            $dump = (string) ob_get_clean();
            ob_start();
            print_r($object);
            $printed = (string) ob_get_clean();

            foreach ([$dump, $printed] as $text) {
                $this->assertNoSecrets($text);
                $this->assertStringContainsString('public-app-key', $text);
                $this->assertStringContainsString('***', $text);
            }
        }
    }

    public function testVarExportSerializeAndJsonShowNoSecrets(): void
    {
        $shop = $this->shop();
        // var_export of the whole object graph may warn about references; the text is what matters.
        set_error_handler(static fn (): bool => true);
        try {
            ob_start();
            var_export($shop);
            $exported = (string) ob_get_clean();
            ob_start();
            var_export(new Credentials('k', 'APP-SECRET-VALUE', 'ACCESS-TOKEN-VALUE', 'SHOP-CIPHER-VALUE'));
            $exported .= (string) ob_get_clean();
        } finally {
            restore_error_handler();
        }
        $this->assertNoSecrets($exported);
        $this->assertNoSecrets((string) json_encode($shop));
        $this->assertNoSecrets(print_r((array) $shop, true));
    }

    public function testCredentialsCannotBeCloned(): void
    {
        $this->expectException(\LogicException::class);
        $this->expectExceptionMessage('use with()');
        clone new Credentials('k', 'APP-SECRET-VALUE');
    }

    public function testCredentialsCannotBeSerialized(): void
    {
        $this->expectException(\LogicException::class);
        serialize(new Credentials('k', 'APP-SECRET-VALUE'));
    }

    public function testCredentialsKeepTheirValuesForTheClient(): void
    {
        $c = new Credentials('k', 'APP-SECRET-VALUE', 'ACCESS-TOKEN-VALUE', '');
        $this->assertSame('APP-SECRET-VALUE', $c->appSecret());
        $this->assertSame('ACCESS-TOKEN-VALUE', $c->accessToken());
        $this->assertNull($c->shopCipher(), "'' means none");
    }
}
