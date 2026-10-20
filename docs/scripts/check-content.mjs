// Checks the authored pages against the SDKs and the spec. Code examples are never written for the docs:
// every block in a language's code comes from that SDK's README, whose examples its own tests compile.
import assert from 'node:assert/strict';
import { readFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { SDKS, SDK_PAGES } from '../sdks.mjs';
import { stampVersions } from '../versions.mjs';

const docsRoot = fileURLToPath(new URL('../', import.meta.url));
const root = path.resolve(docsRoot, '..');
const contentRoot = path.join(docsRoot, 'src/content/docs');

async function filesIn(directory) {
  const entries = await readdir(directory, { withFileTypes: true });
  const files = await Promise.all(entries.map(async (entry) => {
    const file = path.join(directory, entry.name);
    if (entry.isDirectory()) return filesIn(file);
    return /\.mdx?$/.test(entry.name) ? [file] : [];
  }));
  return files.flat().sort();
}

const pages = await Promise.all((await filesIn(contentRoot)).map(async (file) => ({
  file, rel: path.relative(contentRoot, file).split(path.sep).join('/'), text: await readFile(file, 'utf8'),
})));
const page = (rel) => pages.find((p) => p.rel === rel || p.rel === `${rel}x`)?.text ?? assert.fail(`Missing page: ${rel}`);

// The private generator repository is never linked from public pages.
for (const file of [...pages.map((p) => p.file), path.join(docsRoot, 'astro.config.mjs'), path.join(docsRoot, 'README.md')]) {
  const text = await readFile(file, 'utf8');
  assert(!/TikTok-Shop-Api-Generator/i.test(text), `${path.relative(docsRoot, file)} references the private generator repository.`);
}

const disclaimer = 'not affiliated with or endorsed by TikTok or ByteDance';
assert(page('index.md').includes(disclaimer), 'Getting Started must carry the disclaimer.');
assert((await readFile(path.join(docsRoot, 'astro.config.mjs'), 'utf8')).includes(disclaimer), 'The footer must carry the disclaimer.');

// The counts quoted in prose are the spec's.
const spec = JSON.parse(await readFile(path.join(root, '.openapi/tiktok-shop.openapi.json'), 'utf8'));
const methods = new Set(['get', 'put', 'post', 'delete', 'patch', 'head', 'options', 'trace']);
const operations = Object.values(spec.paths).flatMap((item) => Object.keys(item).filter((k) => methods.has(k))).length;
const webhooks = Object.keys(spec.webhooks ?? {}).length;
for (const { rel, text } of pages) {
  for (const [, n] of text.matchAll(/\b(\d+) operations\b/g)) assert.equal(Number(n), operations, `${rel}: the spec has ${operations} operations.`);
  for (const [, n] of text.matchAll(/\b(\d+) webhooks\b/g)) assert.equal(Number(n), webhooks, `${rel}: the spec has ${webhooks} webhooks.`);
}

// The OpenAPI page names every tag and documents every vendor extension the spec uses.
const openapiPage = page('openapi/index.md');
for (const { name } of spec.tags) assert(openapiPage.includes(name), `openapi/index.md does not list the tag ${name}.`);
const extensions = new Set();
(function collect(node) {
  if (Array.isArray(node)) return node.forEach(collect);
  if (!node || typeof node !== 'object') return;
  for (const [key, value] of Object.entries(node)) {
    if (key.startsWith('x-')) extensions.add(key);
    collect(value);
  }
})(spec);
for (const ext of extensions) assert(openapiPage.includes(`| \`${ext}\` |`), `openapi/index.md does not document ${ext}.`);

/** Fenced code blocks, dedented, with the TabItem label that encloses each (if any). */
function codeBlocks(text) {
  const blocks = [];
  let label = null;
  const lines = text.split('\n');
  for (let i = 0; i < lines.length; i++) {
    const tab = lines[i].match(/<TabItem label="([^"]+)"/);
    if (tab) label = tab[1];
    if (/<\/TabItem>/.test(lines[i])) label = null;
    const open = lines[i].match(/^(\s*)(`{3,})(\S*)/);
    if (!open) continue;
    const [, indent, fence, lang] = open;
    const body = [];
    for (i++; i < lines.length && !lines[i].startsWith(`${indent}${fence}`); i++) body.push(lines[i].slice(indent.length));
    blocks.push({ lang, label, code: normalize(body.join('\n')) });
  }
  return blocks;
}
const normalize = (code) => code.split('\n').map((l) => l.trimEnd()).join('\n').replace(/^\n+|\n+$/g, '');

const byName = new Map(SDKS.map((sdk) => [sdk.name, sdk]));
const byFence = new Map(SDKS.map((sdk) => [sdk.fence, sdk]));
const readmes = new Map(await Promise.all(SDKS.map(async (sdk) => {
  const text = await readFile(path.join(root, sdk.readme), 'utf8');
  return [sdk.dir, { text, blocks: codeBlocks(text).map((b) => b.code) }];
})));

// Every SDK section has the same pages, and its overview carries the README's install snippet.
// `--only python,go` limits this to some sections, for checking one section while writing it.
const only = process.argv.includes('--only') ? process.argv[process.argv.indexOf('--only') + 1].split(',') : null;
for (const sdk of SDKS.filter((s) => !only || only.includes(s.dir))) {
  const present = pages.filter((p) => p.rel.startsWith(`sdks/${sdk.dir}/`)).map((p) => p.rel.replace(/^.*\/|\.mdx?$/g, ''));
  assert.deepEqual(present.sort(), [...SDK_PAGES].sort(), `sdks/${sdk.dir}/ must have exactly: ${SDK_PAGES.join(', ')}`);
  const install = readmes.get(sdk.dir).text.split(/^## Install\b/m)[1];
  const installBlock = install && codeBlocks(install)[0]?.code;
  assert(installBlock, `${sdk.readme} has no install snippet.`);
  assert(codeBlocks(page(`sdks/${sdk.dir}/index.md`)).some((b) => stampVersions(b.code) === installBlock),
    `sdks/${sdk.dir}/index must show the install snippet from ${sdk.readme}.`);
}

// Code in an SDK's language, under an SDK's tab, or on an SDK's pages is copied from that SDK's README.
let checked = 0;
for (const { rel, text } of pages) {
  const sectionSdk = SDKS.find((sdk) => rel.startsWith(`sdks/${sdk.dir}/`));
  for (const block of codeBlocks(text)) {
    const sdk = (block.label && byName.get(block.label)) || sectionSdk || byFence.get(block.lang);
    if (!sdk) continue;
    const code = stampVersions(block.code);
    const found = readmes.get(sdk.dir).blocks.some((b) => `\n${b}\n`.includes(`\n${code}\n`));
    assert(found, `${rel}: a ${block.lang || 'plain'} block is not in ${sdk.readme}:\n${code.split('\n').slice(0, 4).join('\n')}`);
    checked++;
  }
}

console.log(`Content check passed: ${pages.length} pages, ${checked} code blocks matched to READMEs, ${operations} operations, ${webhooks} webhooks.`);
