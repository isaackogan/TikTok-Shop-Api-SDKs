import { execFileSync } from 'node:child_process';
import { cpSync, mkdirSync, readdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { renderEvents } from './render-events.ts';
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

// Fix-up: the generated async rejection handlers call $exception->getResponse() / getRequest(), which a
// TikTokShopException (rightly) does not have, so they would die with a fatal Error. Let ours through untouched.
// There is one such handler per operation; any other count means the generator's template changed.
const HANDLER = /(function \(\$exception\) \{\n)(\s*)(\$response = \$exception->getResponse\(\);)/g;
let patched = 0;
for (const f of readdirSync(resolve(dest, 'Api')).filter((n) => n.endsWith('Api.php'))) {
  const p = resolve(dest, 'Api', f);
  const src = readFileSync(p, 'utf8');
  const fixed = src.replace(HANDLER, (_m, head: string, ind: string, rest: string) => {
    patched++;
    return `${head}${ind}if ($exception instanceof \\TikTokShop\\Api\\TikTokShopException) {\n${ind}    throw $exception;\n${ind}}\n${ind}${rest}`;
  });
  if (fixed !== src) writeFileSync(p, fixed);
}
const ops = (JSON.parse(readFileSync(resolve(pkg, 'build/meta.json'), 'utf8')) as { operations: unknown[] }).operations.length;
if (patched !== ops) throw new Error(`async rejection fix-up: patched ${patched} handlers, expected ${ops} (one per operation)`);

renderMeta(resolve(pkg, 'build/meta.json'), dest);
renderEvents(resolve(pkg, 'build/meta.json'), resolve(pkg, 'build/openapi.json'), dest);
