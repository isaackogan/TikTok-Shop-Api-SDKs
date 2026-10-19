import { execFileSync } from 'node:child_process';
import { cpSync, mkdirSync, rmSync } from 'node:fs';
import { resolve } from 'node:path';
import { renderMeta } from './render-meta.ts';

const pkg = resolve(import.meta.dirname, '..');
const root = resolve(pkg, '..');
const run = (cmd: string, args: string[], cwd = root) => execFileSync(cmd, args, { cwd, stdio: 'inherit' });

run('pnpm', ['exec', 'tsx', 'scripts/prepare-spec.ts', '--lang', 'java']);

const out = resolve(pkg, 'build/out');
rmSync(out, { recursive: true, force: true });
run('pnpm', [
  'exec', 'openapi-generator-cli', 'generate',
  '-g', 'java',
  '--library', 'okhttp-gson',
  '-i', 'java/build/openapi.json',
  '-o', 'java/build/out',
  '--global-property', 'apiDocs=false,modelDocs=false,apiTests=false,modelTests=false',
  // disallowAdditionalPropertiesIfNotPresent=false: without it validateJsonElement throws on any field the spec lacks.
  '--additional-properties=apiPackage=com.isaackogan.tiktok.shop.generated.api,modelPackage=com.isaackogan.tiktok.shop.generated.model,invokerPackage=com.isaackogan.tiktok.shop.generated,hideGenerationTimestamp=true,openApiNullable=false,disallowAdditionalPropertiesIfNotPresent=false',
]);

// Only the Java sources: the generator's pom, gradle files, README and api/ are discarded.
const pkgPath = 'src/main/java/com/isaackogan/tiktok/shop/generated';
const dest = resolve(pkg, pkgPath);
rmSync(dest, { recursive: true, force: true });
mkdirSync(dest, { recursive: true });
cpSync(resolve(out, pkgPath), dest, { recursive: true });

renderMeta(resolve(pkg, 'build/meta.json'), dest);
