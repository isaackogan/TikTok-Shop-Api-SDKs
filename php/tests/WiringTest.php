<?php

declare(strict_types=1);

namespace TikTokShop\Api\Tests;

use PHPUnit\Framework\TestCase;
use TikTokShop\Api\Generated\Meta;
use TikTokShop\Api\TikTokShop;

final class WiringTest extends TestCase
{
    private function shop(): TikTokShop
    {
        return new TikTokShop(appKey: 'k', appSecret: 's');
    }

    public function testEveryOperationIsReachableAsGroupMethod(): void
    {
        $shop = $this->shop();
        $this->assertNotEmpty(Meta::OPERATIONS);
        foreach (Meta::OPERATIONS as [$operationId, $group]) {
            $this->assertTrue(property_exists($shop, $group), "no group property $group for $operationId");
            $this->assertTrue(is_callable([$shop->$group, $operationId]), "$group->$operationId is not callable");
        }
    }

    public function testGroupNamesAreTheCanonicalCamelCaseList(): void
    {
        $expected = [
            'affiliateCreator', 'affiliatePartner', 'affiliateSeller', 'analytics', 'authorization',
            'customerEngagement', 'customerService', 'event', 'finance', 'fulfilledByTikTok', 'fulfillment',
            'logistics', 'orders', 'products', 'promotion', 'returnAndRefund', 'seller', 'supplyChain', 'tools',
        ];
        $groups = array_keys(Meta::GROUPS);
        sort($groups);
        $sorted = $expected;
        sort($sorted);
        $this->assertSame($sorted, $groups);

        $json = json_decode((string) file_get_contents(__DIR__ . '/../../shared/api-groups.json'), true, 512, JSON_THROW_ON_ERROR);
        $fromShared = array_values($json);
        sort($fromShared);
        $this->assertSame($fromShared, $groups);
    }

    public function testEveryGroupIsAPublicReadonlyPropertyTypedWithItsGeneratedApiClass(): void
    {
        $class = new \ReflectionClass(TikTokShop::class);
        foreach (Meta::GROUPS as $name => [, $apiClass]) {
            $property = $class->getProperty($name);
            $this->assertTrue($property->isPublic(), $name);
            $this->assertTrue($property->isReadOnly(), $name);
            $type = $property->getType();
            $this->assertInstanceOf(\ReflectionNamedType::class, $type, $name);
            $this->assertSame($apiClass, $type->getName(), $name);
            $this->assertInstanceOf($apiClass, $this->shop()->$name);
        }
    }

    public function testEveryOperationsGroupIsInTheGroupTable(): void
    {
        foreach (Meta::OPERATIONS as [$operationId, $group]) {
            $this->assertArrayHasKey($group, Meta::GROUPS, $operationId);
        }
    }
}
