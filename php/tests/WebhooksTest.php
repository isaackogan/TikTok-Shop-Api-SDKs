<?php

declare(strict_types=1);

namespace TikTokShop\Api\Tests;

use PHPUnit\Framework\Attributes\DataProvider;
use PHPUnit\Framework\TestCase;
use TikTokShop\Api\Generated\Event\AppealCompletedEvent;
use TikTokShop\Api\Generated\Event\OrderStatusChangeEvent;
use TikTokShop\Api\Generated\Meta;
use TikTokShop\Api\Generated\Model\AppealCompletedWebhook;
use TikTokShop\Api\Generated\Model\OrderStatusChangeWebhook;
use TikTokShop\Api\Generated\WebhookEvents;
use TikTokShop\Api\UnknownWebhookEvent;
use TikTokShop\Api\WebhookEvent;
use TikTokShop\Api\WebhookSignatureException;
use TikTokShop\Api\Webhooks;

final class WebhooksTest extends TestCase
{
    /** @return array<string, mixed> */
    private static function vectors(): array
    {
        return json_decode((string) file_get_contents(__DIR__ . '/../../shared/test-vectors/webhooks.json'), true, 512, JSON_THROW_ON_ERROR);
    }

    /** @return array<string, array{array<string, mixed>}> */
    public static function verifyCases(): array
    {
        $out = [];
        foreach (self::vectors()['verify'] as $case) {
            $out[$case['name']] = [$case];
        }

        return $out;
    }

    /** @return array<string, array{array<string, mixed>}> */
    public static function parseCases(): array
    {
        $out = [];
        foreach (self::vectors()['parse'] as $case) {
            $out[$case['name']] = [$case];
        }

        return $out;
    }

    /** @param array<string, mixed> $case */
    #[DataProvider('verifyCases')]
    public function testVerifyVector(array $case): void
    {
        $this->assertSame($case['valid'], Webhooks::verify($case['appKey'], $case['appSecret'], $case['rawBody'], $case['signature']));
    }

    /** @param array<string, mixed> $case */
    #[DataProvider('verifyCases')]
    public function testVerifyAndParseVector(array $case): void
    {
        if ($case['valid']) {
            $event = Webhooks::verifyAndParse($case['appKey'], $case['appSecret'], $case['rawBody'], $case['signature']);
            $this->assertInstanceOf(OrderStatusChangeEvent::class, $event);

            return;
        }
        $this->expectException(WebhookSignatureException::class);
        Webhooks::verifyAndParse($case['appKey'], $case['appSecret'], $case['rawBody'], $case['signature']);
    }

    public function testANullSignatureIsFalse(): void
    {
        $this->assertFalse(Webhooks::verify('k', 's', '{}', null));
    }

    /** @param array<string, mixed> $case */
    #[DataProvider('parseCases')]
    public function testParseVector(array $case): void
    {
        $event = Webhooks::parse($case['rawBody']);
        $this->assertSame($case['type'], $event->getType());
        $this->assertSame($case['type'], $event->getRaw()['type']);
        if (!$case['known']) {
            $this->assertInstanceOf(UnknownWebhookEvent::class, $event);

            return;
        }
        [$eventClass, $modelClass, $schema] = WebhookEvents::TYPES[$case['type']];
        $this->assertSame($case['schema'], $schema);
        $this->assertInstanceOf($eventClass, $event);
        $this->assertInstanceOf($modelClass, $event->getPayload());
    }

    public function testTheTypedEventNarrowsToItsPayload(): void
    {
        $case = self::vectors()['parse'][0];

        $event = Webhooks::parse($case['rawBody']);
        $this->assertInstanceOf(OrderStatusChangeEvent::class, $event);
        $this->assertInstanceOf(OrderStatusChangeWebhook::class, $event->getPayload());
        $this->assertSame('576653688135258178', $event->getPayload()->getData()->getOrderId());
        $this->assertSame('UNPAID', $event->getPayload()->getData()->getOrderStatus());
        $this->assertSame('7495540735365777507', $event->getPayload()->getShopId());
        $this->assertSame(OrderStatusChangeEvent::TYPE, $event->getType());
    }

    public function testEventTypesComeFromTheSpec(): void
    {
        $this->assertSame(Meta::EVENT_TYPES, Webhooks::EVENT_TYPES);
        $this->assertSame('ORDER_STATUS_CHANGE', Webhooks::EVENT_TYPES[1]);
        $this->assertNotEmpty(Webhooks::EVENT_TYPES);
    }

    public function testA19DigitShopIdSentAsAJsonNumberKeepsItsExactValue(): void
    {
        $event = Webhooks::parse('{"type":1,"tts_notification_id":"n1","shop_id":7494049642642441621,"timestamp":1718305585,"data":{"order_id":"1","order_status":"PAID"}}');
        $this->assertInstanceOf(OrderStatusChangeEvent::class, $event);
        $this->assertSame('7494049642642441621', $event->getPayload()->getShopId());
        $this->assertSame('7494049642642441621', (string) $event->getRaw()['shop_id']);
    }

    public function testAnIdBeyond64BitsKeepsItsExactDigits(): void
    {
        $event = Webhooks::parse('{"type":1,"shop_id":92233720368547758079,"data":{}}');
        $this->assertInstanceOf(OrderStatusChangeEvent::class, $event);
        $this->assertSame('92233720368547758079', $event->getPayload()->getShopId());
        $this->assertSame('92233720368547758079', $event->getRaw()['shop_id']);
    }

    /** @return array<string, array{string}> */
    public static function badTypes(): array
    {
        return [
            'missing' => ['{"shop_id":"1"}'],
            'string' => ['{"type":"1"}'],
            'bool' => ['{"type":true}'],
            'null' => ['{"type":null}'],
            'float' => ['{"type":1.5}'],
            'float with a zero fraction' => ['{"type":1.0}'],
            'array' => ['{"type":[1]}'],
            'object' => ['{"type":{"a":1}}'],
            'beyond 64 bits' => ['{"type":92233720368547758079}'],
        ];
    }

    #[DataProvider('badTypes')]
    public function testAMissingOrNonIntegerTypeIsRejected(string $body): void
    {
        $this->expectException(\InvalidArgumentException::class);
        $this->expectExceptionMessageMatches('/"type"/');
        Webhooks::parse($body);
    }

    /** @return array<string, array{string}> */
    public static function notObjects(): array
    {
        return ['not json' => ['not json'], 'empty' => [''], 'a list' => ['[1]'], 'a string' => ['"x"'], 'a number' => ['1'], 'null' => ['null']];
    }

    #[DataProvider('notObjects')]
    public function testABodyThatIsNotAJsonObjectIsRejected(string $body): void
    {
        $this->expectException(\InvalidArgumentException::class);
        Webhooks::parse($body);
    }

    public function testAWebhookWithUnknownFieldsStillParses(): void
    {
        $event = Webhooks::parse('{"type":1,"brand_new":{"x":[1,2]},"shop_id":"7","data":{"order_id":"9","also_new":true}}');
        $this->assertInstanceOf(OrderStatusChangeEvent::class, $event);
        $this->assertSame('9', $event->getPayload()->getData()->getOrderId());
        $this->assertSame(['x' => [1, 2]], $event->getRaw()['brand_new']);
        $this->assertTrue($event->getRaw()['data']['also_new']);

        $unknown = Webhooks::parse('{"type":424242,"anything":"goes"}');
        $this->assertInstanceOf(UnknownWebhookEvent::class, $unknown);
        $this->assertSame('goes', $unknown->getRaw()['anything']);
    }

    private const APPEAL = '{"type":66,"shop_id":"7494049642642441621","tts_notification_id":"n","timestamp":1,'
        . '"data":{"product_id":1729507467923261408,"appeal_task":{"size_chart_id":5,"appeal_audit_result":['
        . '{"indicator_type":"A","status":"PASS"},{"indicator_type":"B","status":"FAIL","reject_reason":"r"}]}}}';

    public function testANestedModelWithRequiredPropertiesParses(): void
    {
        $event = Webhooks::parse(self::APPEAL);
        $this->assertInstanceOf(AppealCompletedEvent::class, $event);
        $this->assertInstanceOf(AppealCompletedWebhook::class, $event->getPayload());
        $results = $event->getPayload()->getData()->getAppealTask()->getAppealAuditResult();
        $this->assertCount(2, $results);
        $this->assertSame('FAIL', $results[1]->getStatus());
        $this->assertSame(1729507467923261408, $event->getPayload()->getData()->getProductId());
    }

    /** @return array<string, array{string, string}> body => the property the error must name */
    public static function missingRequired(): array
    {
        $decode = static fn (): array => json_decode(self::APPEAL, true, 512, JSON_THROW_ON_ERROR);
        $cases = [];
        $without = static function (string $name, callable $edit) use ($decode, &$cases): void {
            $body = $decode();
            $edit($body);
            $cases[$name] = [json_encode($body, JSON_THROW_ON_ERROR), $name];
        };
        $without('shop_id', static function (array &$b): void { unset($b['shop_id']); });
        $without('data', static function (array &$b): void { $b['data'] = null; });
        $without('data.product_id', static function (array &$b): void { unset($b['data']['product_id']); });
        $without('data.appeal_task', static function (array &$b): void { $b['data']['appeal_task'] = null; });
        $without('data.appeal_task.appeal_audit_result.status', static function (array &$b): void {
            unset($b['data']['appeal_task']['appeal_audit_result'][1]['status']);
        });
        $without('data.appeal_task.appeal_audit_result.indicator_type', static function (array &$b): void {
            $b['data']['appeal_task']['appeal_audit_result'][0]['indicator_type'] = null;
        });

        return $cases;
    }

    #[DataProvider('missingRequired')]
    public function testAMissingOrNullRequiredPropertyIsRejectedByName(string $body, string $property): void
    {
        $this->expectException(\InvalidArgumentException::class);
        $this->expectExceptionMessage("required property \"$property\" is missing");
        Webhooks::parse($body);
    }

    public function testEveryWebhookTypeDispatchesToItsEventAndPayload(): void
    {
        $this->assertNotEmpty(Meta::WEBHOOKS);
        $this->assertCount(count(Meta::WEBHOOKS), WebhookEvents::TYPES);
        foreach (Meta::WEBHOOKS as [$type, $schema]) {
            [$eventClass, $modelClass, $name] = WebhookEvents::TYPES[$type];
            $this->assertSame($schema, $name);
            $this->assertTrue(class_exists($eventClass), $eventClass);
            $this->assertTrue(class_exists($modelClass), $modelClass);
            $this->assertTrue(is_subclass_of($eventClass, WebhookEvent::class), $eventClass);
            $this->assertSame($modelClass, (string) (new \ReflectionMethod($eventClass, 'getPayload'))->getReturnType());

            $required = WebhookEvents::REQUIRED[$schema][0];
            if (array_diff($required, ["type"]) === []) {
                $event = Webhooks::parse('{"type":' . $type . '}');
                $this->assertInstanceOf($eventClass, $event);
                $this->assertSame($type, $event->getType());
                $this->assertInstanceOf($modelClass, $event->getPayload());
            } else {
                try {
                    Webhooks::parse('{"type":' . $type . '}');
                    $this->fail("type $type has required properties, yet parsed without them");
                } catch (\InvalidArgumentException $e) {
                    $this->assertStringContainsString('required property', $e->getMessage());
                }
            }
        }
    }

    public function testTheRequiredTableMatchesTheGeneratedModels(): void
    {
        $this->assertNotEmpty(WebhookEvents::REQUIRED);
        foreach (WebhookEvents::REQUIRED as $schema => [$required, $children]) {
            $class = 'TikTokShop\\Api\\Generated\\Model\\' . $schema;
            $this->assertTrue(class_exists($class), $class);
            $json = array_values($class::attributeMap());
            foreach ($required as $name) {
                $this->assertContains($name, $json, "$schema: required $name");
            }
            foreach ($children as $name => [$kind, $child]) {
                $this->assertContains($name, $json, "$schema: child $name");
                $this->assertContains($kind, ['object', 'list', 'map']);
                $this->assertArrayHasKey($child, WebhookEvents::REQUIRED, "$schema.$name");
            }
        }
    }
}
