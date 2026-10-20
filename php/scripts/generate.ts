import { execFileSync } from 'node:child_process';
import { cpSync, mkdirSync, rmSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { renderMeta } from './render-meta.ts';

const pkg = resolve(import.meta.dirname, '..');
const root = resolve(pkg, '..');
const run = (cmd: string, args: string[]) => execFileSync(cmd, args, { cwd: root, stdio: 'inherit' });

run('pnpm', ['exec', 'tsx', 'scripts/prepare-spec.ts', '--lang', 'php']);

const out = resolve(pkg, 'build/out');
rmSync(out, { recursive: true, force: true });

// R20: the generator's CLI wrapper strips backslashes from command-line properties, so the namespace goes in a config file.
// R12: disallowAdditionalPropertiesIfNotPresent=false keeps unknown response fields from failing a decode.
const config = resolve(pkg, 'build/config.json');
writeFileSync(
  config,
  JSON.stringify({ invokerPackage: 'TikTokShop\\Api\\Generated', disallowAdditionalPropertiesIfNotPresent: false }),
);
run('pnpm', [
  'exec', 'openapi-generator-cli', 'generate',
  '-g', 'php',
  '-c', 'php/build/config.json',
  '-i', 'php/build/openapi.json',
  '-o', 'php/build/out',
  '--global-property', 'apiDocs=false,modelDocs=false,apiTests=false,modelTests=false',
]);

// Only lib/: the generator's composer.json, phpunit.xml.dist, README and git_push.sh are discarded.
const dest = resolve(pkg, 'src/Generated');
rmSync(dest, { recursive: true, force: true });
mkdirSync(dest, { recursive: true });
cpSync(resolve(out, 'lib'), dest, { recursive: true });

renderMeta(resolve(pkg, 'build/meta.json'), dest);
