import { execFileSync } from 'node:child_process';
import { cpSync, mkdirSync, rmSync } from 'node:fs';
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

renderMeta(resolve(pkg, 'build/meta.json'), dest);
