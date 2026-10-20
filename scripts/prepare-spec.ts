import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { parseArgs } from 'node:util';
import { LANGS, parseSpec, prepareSpec, type Lang } from './lib/meta.ts';

const root = resolve(import.meta.dirname, '..');

const { values } = parseArgs({ options: { lang: { type: 'string' }, out: { type: 'string' } } });
const lang = values.lang as Lang | undefined;
if (!lang || !LANGS.includes(lang)) {
  console.error(`usage: prepare-spec.ts --lang <${LANGS.join('|')}> [--out <dir>]`);
  process.exit(2);
}

const spec = parseSpec(readFileSync(resolve(root, '.openapi/tiktok-shop.openapi.json'), 'utf8'));
const groups = JSON.parse(readFileSync(resolve(root, 'shared/api-groups.json'), 'utf8'));
const { spec: prepared, meta } = prepareSpec(spec, lang, groups);

const outDir = values.out ? resolve(values.out) : resolve(root, lang, 'build');
mkdirSync(outDir, { recursive: true });
writeFileSync(resolve(outDir, 'openapi.json'), JSON.stringify(prepared));
writeFileSync(resolve(outDir, 'meta.json'), JSON.stringify(meta, null, 2) + '\n');
