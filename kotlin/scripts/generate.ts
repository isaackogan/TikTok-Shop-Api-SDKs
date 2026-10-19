import { execFileSync } from 'node:child_process';
import { cpSync, mkdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { fixGetBody } from './fix-get-body.ts';
import { renderEvents } from './render-events.ts';
import { renderMeta } from './render-meta.ts';

const pkg = resolve(import.meta.dirname, '..');
const root = resolve(pkg, '..');
const run = (cmd: string, args: string[], cwd = root) => execFileSync(cmd, args, { cwd, stdio: 'inherit' });

run('pnpm', ['exec', 'tsx', 'scripts/prepare-spec.ts', '--lang', 'kotlin']);

const out = resolve(pkg, 'build/out');
rmSync(out, { recursive: true, force: true });
run('pnpm', [
  'exec', 'openapi-generator-cli', 'generate',
  '-g', 'kotlin',
  '--library', 'jvm-okhttp4',
  '-i', 'kotlin/build/openapi.json',
  '-o', 'kotlin/build/out',
  '--global-property', 'apiDocs=false,modelDocs=false,apiTests=false,modelTests=false',
  // File=FileInfo: the spec's `File` schema (a certification file) otherwise becomes java.io.File and the model file does not compile.
  '--model-name-mappings', 'File=FileInfo',
  // gson ignores unknown fields by default; disallowAdditionalPropertiesIfNotPresent=false is harmless here (R12).
  '--additional-properties=packageName=com.isaackogan.tiktok.shop.generated,serializationLibrary=gson,hideGenerationTimestamp=true,disallowAdditionalPropertiesIfNotPresent=false',
]);

// Only the Kotlin sources: the generator's gradle files, README and docs are discarded.
const pkgPath = 'src/main/kotlin/com/isaackogan/tiktok/shop/generated';
const dest = resolve(pkg, pkgPath);
rmSync(dest, { recursive: true, force: true });
mkdirSync(dest, { recursive: true });
cpSync(resolve(out, pkgPath), dest, { recursive: true });

// Fix-up (R18): see fix-get-body.ts.
const apiClient = resolve(dest, 'infrastructure/ApiClient.kt');
writeFileSync(apiClient, fixGetBody(readFileSync(apiClient, 'utf8')));

renderMeta(resolve(pkg, 'build/meta.json'), dest);
renderEvents(resolve(pkg, 'build/meta.json'), dest);
