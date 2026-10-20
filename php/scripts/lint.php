<?php
// Syntax-checks every PHP file under src/ (a parse error fails the build). Usage: php scripts/lint.php
declare(strict_types=1);

$root = dirname(__DIR__) . '/src';
$failed = 0;
$count = 0;
foreach (new RecursiveIteratorIterator(new RecursiveDirectoryIterator($root, FilesystemIterator::SKIP_DOTS)) as $file) {
    if ($file->getExtension() !== 'php') {
        continue;
    }
    $count++;
    try {
        token_get_all((string) file_get_contents($file->getPathname()), TOKEN_PARSE);
    } catch (ParseError $e) {
        fwrite(STDERR, "{$file->getPathname()}:{$e->getLine()}: {$e->getMessage()}\n");
        $failed++;
    }
}
echo "checked $count files, $failed with syntax errors\n";
exit($failed === 0 ? 0 : 1);
