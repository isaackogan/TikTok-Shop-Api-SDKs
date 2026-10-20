<?php

declare(strict_types=1);

namespace TikTokShop\Api\Tests;

use PHPUnit\Framework\TestCase;

/** PSR-4: every class under src/ lives in a file named after it, so Composer can autoload it. */
final class AutoloadTest extends TestCase
{
    public function testEveryClassUnderSrcAutoloadsFromItsPath(): void
    {
        $src = realpath(__DIR__ . '/../src');
        $this->assertNotFalse($src);
        $count = 0;
        foreach (new \RecursiveIteratorIterator(new \RecursiveDirectoryIterator($src, \FilesystemIterator::SKIP_DOTS)) as $file) {
            $path = $file->getPathname();
            // The ~2000 generated models and APIs are covered by the wiring and webhook tests.
            if ($file->getExtension() !== 'php' || str_contains($path, '/Generated/Model/') || str_contains($path, '/Generated/Api/')) {
                continue;
            }
            $relative = substr($path, strlen($src) + 1, -4);
            $class = 'TikTokShop\\Api\\' . str_replace('/', '\\', $relative);
            $count++;
            $this->assertTrue(
                class_exists($class) || interface_exists($class) || enum_exists($class),
                "$path should declare $class (PSR-4: one class per file, named after the file)",
            );
        }
        $this->assertGreaterThan(10, $count);
    }
}
