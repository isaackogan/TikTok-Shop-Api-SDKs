<?php

declare(strict_types=1);

namespace TikTokShop\Api\Tests;

use PHPUnit\Framework\Attributes\DataProvider;
use PHPUnit\Framework\TestCase;
use TikTokShop\Api\Generated\Meta;
use TikTokShop\Api\TikTokShop;
use TikTokShop\Api\TikTokShopAuth;
use TikTokShop\Api\TikTokShopException;
use TikTokShop\Api\TokenSet;
use TikTokShop\Api\WebhookEvent;

/**
 * Each ```php block of the README is its own file, tests/Readme/SnippetN.php. This test checks that the files match the
 * README block by block (in order, `use` lines included), that each parses, and that every class, method, constant,
 * function and named argument a snippet uses exists.
 */
final class ReadmeTest extends TestCase
{
    private const README = __DIR__ . '/../README.md';

    /** @return list<string> */
    private static function blocks(): array
    {
        preg_match_all('/^```php\n(.*?)^```$/ms', (string) file_get_contents(self::README), $m);

        return $m[1];
    }

    /** @return list<string> */
    private static function files(): array
    {
        $files = glob(__DIR__ . '/Readme/Snippet*.php') ?: [];
        natsort($files);

        return array_values($files);
    }

    /** @return array<string, array{int}> */
    public static function snippets(): array
    {
        $out = [];
        foreach (array_keys(self::blocks()) as $i) {
            $out['Snippet' . ($i + 1)] = [$i + 1];
        }

        return $out;
    }

    public function testEveryReadmePhpBlockHasItsOwnFileInOrder(): void
    {
        $blocks = self::blocks();
        $this->assertNotEmpty($blocks);
        $expected = [];
        foreach (array_keys($blocks) as $i) {
            $expected[] = __DIR__ . '/Readme/Snippet' . ($i + 1) . '.php';
        }
        $this->assertSame($expected, self::files(), 'one SnippetN.php per README php block, numbered from 1');
    }

    public function testTheComposerDescriptionCarriesTheDisclaimer(): void
    {
        // Packagist search results show the composer.json description, not the README.
        $composer = json_decode((string) file_get_contents(__DIR__ . '/../composer.json'), true, 512, JSON_THROW_ON_ERROR);
        $this->assertIsArray($composer);
        $this->assertIsString($composer['description'] ?? null, 'the package has a description');
        $this->assertStringEndsWith('Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.', $composer['description']);
    }

    #[DataProvider('snippets')]
    public function testASnippetFileIsItsReadmeBlock(int $n): void
    {
        $this->assertSame(
            "<?php\n" . self::blocks()[$n - 1],
            (string) file_get_contents(__DIR__ . "/Readme/Snippet$n.php"),
            "Snippet$n.php differs from README php block $n",
        );
    }

    #[DataProvider('snippets')]
    public function testASnippetLints(int $n): void
    {
        $output = [];
        exec(escapeshellarg(PHP_BINARY) . ' -l ' . escapeshellarg(__DIR__ . "/Readme/Snippet$n.php") . ' 2>&1', $output, $code);
        $this->assertSame(0, $code, implode("\n", $output));
    }

    #[DataProvider('snippets')]
    public function testASnippetOnlyUsesNamesThatExist(int $n): void
    {
        $source = (string) file_get_contents(__DIR__ . "/Readme/Snippet$n.php");

        // use lines: each imported name must exist
        $alias = [];
        preg_match_all('/^use ([\w\\\\]+);$/m', $source, $uses);
        foreach ($uses[1] as $fqcn) {
            $this->assertTrue(class_exists($fqcn) || interface_exists($fqcn), "use $fqcn: no such class");
            $alias[substr($fqcn, (int) strrpos($fqcn, '\\') + 1)] = $fqcn;
        }
        $resolve = function (string $name) use ($alias): string {
            $class = $alias[$name] ?? $name;
            $this->assertTrue(class_exists($class) || interface_exists($class), "class $name is not imported or does not exist");

            return $class;
        };

        $tokens = array_values(array_filter(
            token_get_all($source),
            static fn ($t): bool => !is_array($t) || !in_array($t[0], [T_WHITESPACE, T_COMMENT, T_DOC_COMMENT], true),
        ));
        $methodNames = [];
        $paramNames = [];
        $seen = [];
        foreach ($tokens as $i => $t) {
            $id = is_array($t) ? $t[0] : $t;
            $text = is_array($t) ? $t[1] : $t;
            $next = $tokens[$i + 1] ?? null;
            $nextId = is_array($next) ? $next[0] : $next;
            $prev = $tokens[$i - 1] ?? null;
            $prevId = is_array($prev) ? $prev[0] : $prev;

            if ($id === T_STRING && $nextId === T_DOUBLE_COLON) {
                // Class::member
                $class = $resolve($text);
                $member = $tokens[$i + 2][1] ?? '';
                $isCall = ($tokens[$i + 3] ?? null) === '(';
                $this->assertTrue(
                    $isCall ? method_exists($class, $member) : defined("$class::$member"),
                    "$class::$member does not exist",
                );
                $seen[] = $class;
            } elseif ($id === T_STRING && in_array($prevId, [T_NEW, T_INSTANCEOF], true)) {
                $seen[] = $resolve($text);
            } elseif ($id === T_STRING && $prevId === '(' && ($tokens[$i - 2][0] ?? null) === T_CATCH) {
                $seen[] = $resolve($text);
            } elseif ($id === T_STRING && $prevId === T_OBJECT_OPERATOR && $next === '(') {
                $methodNames[] = $text;
            } elseif ($id === T_STRING && $next === '(' && !in_array($prevId, [T_OBJECT_OPERATOR, T_DOUBLE_COLON, T_NEW, T_FUNCTION], true)) {
                $this->assertTrue(function_exists($text), "function $text() does not exist");
            } elseif ($id === T_STRING && $next === ':' && in_array($prevId, ['(', ','], true)) {
                $paramNames[] = $text; // a named argument
            }
        }

        // ->method() calls: it must exist on one of the classes the snippet imports or on a generated API, event or model class.
        $known = self::knownMethods($seen);
        foreach ($methodNames as $method) {
            $this->assertContains($method, $known, "->$method() is not a method of any class the snippet uses or of a generated class");
        }
        // named arguments: a parameter of some method of an imported class
        $params = [];
        foreach ($seen as $class) {
            foreach ((new \ReflectionClass($class))->getMethods(\ReflectionMethod::IS_PUBLIC) as $method) {
                foreach ($method->getParameters() as $p) {
                    $params[] = $p->getName();
                }
            }
        }
        foreach ($paramNames as $name) {
            $this->assertContains($name, $params, "named argument $name: is not a parameter of any class the snippet uses");
        }
    }

    /**
     * @param list<class-string> $classes
     * @return list<string>
     */
    private static function knownMethods(array $classes): array
    {
        static $generated = null;
        if ($generated === null) {
            $generated = [];
            $dir = __DIR__ . '/../src/Generated';
            foreach (Meta::GROUPS as [, $api]) {
                $generated[] = $api;
            }
            foreach (['Model', 'Event'] as $folder) {
                foreach (glob("$dir/$folder/*.php") ?: [] as $file) {
                    $generated[] = "TikTokShop\\Api\\Generated\\$folder\\" . basename($file, '.php');
                }
            }
        }
        $methods = [];
        foreach ([...$classes, ...$generated, TikTokShop::class, TikTokShopAuth::class, TokenSet::class, TikTokShopException::class, WebhookEvent::class] as $class) {
            foreach (get_class_methods($class) as $m) {
                $methods[$m] = true;
            }
        }

        return array_keys($methods);
    }
}
