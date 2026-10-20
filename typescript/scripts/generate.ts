import { execFileSync } from 'node:child_process';
import { cpSync, mkdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { renderMeta } from './render-meta.ts';

const pkg = resolve(import.meta.dirname, '..');
const root = resolve(pkg, '..');
const run = (cmd: string, args: string[]) => execFileSync(cmd, args, { cwd: root, stdio: 'inherit' });

run('pnpm', ['exec', 'tsx', 'scripts/prepare-spec.ts', '--lang', 'typescript']);

const out = resolve(pkg, 'build/out');
rmSync(out, { recursive: true, force: true });
run('pnpm', [
  'exec', 'openapi-generator-cli', 'generate',
  '-g', 'typescript-fetch',
  '-i', 'typescript/build/openapi.json',
  '-o', 'typescript/build/out',
  '--global-property', 'apiDocs=false,modelDocs=false,apiTests=false,modelTests=false',
  '--additional-properties=supportsES6=true',
]);

const dest = resolve(pkg, 'src/generated');
rmSync(dest, { recursive: true, force: true });
mkdirSync(dest, { recursive: true });
for (const item of ['apis', 'models', 'runtime.ts', 'index.ts']) {
  cpSync(resolve(out, item), resolve(dest, item), { recursive: true });
}

// R13d: a 2xx body that FromJSON cannot read (a list or object of the wrong shape) becomes a TikTokShopError with
// code -1, not a raw TypeError. The one place a model transformer runs is JSONApiResponse.value().
const runtimePath = resolve(dest, 'runtime.ts');
const runtime = readFileSync(runtimePath, 'utf8');
const VALUE = '    async value(): Promise<T> {\n        return this.transformer(await this.raw.json());\n    }\n';
const IMPORT_AFTER = '/* eslint-disable */\n';
for (const [what, needle] of [['JSONApiResponse.value', VALUE], ['the eslint header', IMPORT_AFTER]] as const) {
  const count = runtime.split(needle).length - 1;
  if (count !== 1) throw new Error(`runtime.ts fix-up: expected ${what} exactly once, found ${count}`);
}
writeFileSync(
  runtimePath,
  runtime
    .replace(IMPORT_AFTER, `${IMPORT_AFTER}import { decodeFailure } from '../errors.ts';\n`)
    .replace(
      VALUE,
      '    async value(): Promise<T> {\n        const json = await this.raw.json();\n        try {\n            return this.transformer(json);\n' +
        '        } catch (e) {\n            throw decodeFailure(this.raw, json, e);\n        }\n    }\n',
    ),
);

renderMeta(resolve(pkg, 'build/meta.json'), dest, resolve(pkg, 'build/openapi.json'));
