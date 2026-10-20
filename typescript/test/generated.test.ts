import { readdirSync, readFileSync } from 'node:fs';
import { describe, expect, it } from 'vitest';
import * as generated from '../src/generated/index.ts';
import { EVENT_TYPES, GROUPS, ID_BODY_PATHS, ID_FIELDS, OPERATIONS, WEBHOOK_MODELS, WEBHOOKS } from '../src/generated/meta.ts';
import { findGroupClasses } from '../scripts/render-meta.ts';

const groups = Object.values(
  JSON.parse(readFileSync(new URL('../../shared/api-groups.json', import.meta.url), 'utf8')),
) as string[];
// Everything here reads committed files: the rendered src/generated/meta.ts and the generated API sources.
// Nothing under build/ (gitignored), and no hard-coded spec counts.
const apiSources = (cls: string): string => {
  const dir = new URL('../src/generated/apis/', import.meta.url);
  for (const f of readdirSync(dir)) {
    const src = readFileSync(new URL(f, dir), 'utf8');
    if (new RegExp(`export class ${cls}\\b`).test(src)) return src;
  }
  throw new Error(`no source for ${cls}`);
};

describe('generated client', () => {
  it('maps every group to an exported API class', () => {
    expect(groups.length).toBeGreaterThan(0);
    expect(Object.keys(GROUPS).sort()).toEqual([...groups].sort());
    for (const g of groups) {
      expect(GROUPS[g], g).toBeDefined();
      expect((generated as Record<string, unknown>)[GROUPS[g].className], g).toBeTypeOf('function');
    }
  });
  it('has every operation as a method on its group class, with unique ids', () => {
    expect(OPERATIONS.length).toBeGreaterThan(0);
    expect(new Set(OPERATIONS.map((o) => o.operationId)).size).toBe(OPERATIONS.length);
    expect(new Set(OPERATIONS.map((o) => o.group))).toEqual(new Set(groups));
    const sources = new Map<string, string>();
    for (const op of OPERATIONS) {
      const cls = GROUPS[op.group].className;
      if (!sources.has(cls)) sources.set(cls, apiSources(cls));
      expect(sources.get(cls), `${op.operationId} on ${cls}`).toMatch(new RegExp(`async ${op.operationId}\\(`));
    }
    expect(OPERATIONS.some((o) => o.requiresShopCipher)).toBe(true);
    expect(OPERATIONS.some((o) => !o.requiresShopCipher)).toBe(true);
  });
  it('carries the webhooks, each with a generated model, and their event types', () => {
    expect(WEBHOOKS.length).toBeGreaterThan(0);
    const models = new Set(readdirSync(new URL('../src/generated/models/', import.meta.url)).map((f) => f.replace(/\.ts$/, '')));
    for (const w of WEBHOOKS) expect(models.has(w.schema), w.schema).toBe(true);
    expect(EVENT_TYPES).toEqual(Object.fromEntries(WEBHOOKS.filter((w) => w.eventType).map((w) => [w.type, w.eventType])));
    expect(EVENT_TYPES[1]).toBe('ORDER_STATUS_CHANGE');
  });
  it('carries the ID fields', () => {
    for (const f of ['product_id', 'shop_id', 'sku_id', 'material_id', 'tts_pid']) {
      expect(ID_FIELDS).toContain(f);
    }
  });
  it('carries request-body ID paths only for operations that exist', () => {
    expect(ID_BODY_PATHS).toBeTypeOf('object');
    const ids = new Set(OPERATIONS.map((o) => o.operationId));
    for (const id of Object.keys(ID_BODY_PATHS)) expect(ids.has(id), id).toBe(true);
  });
});

describe('findGroupClasses', () => {
  const op = (operationId: string, group = 'g') =>
    ({ operationId, tag: 'T', group, method: 'get', path: '/x', requiresShopCipher: false });
  const api = (file: string, cls: string, ids: string[]) => ({
    file,
    src: `export class ${cls} {\n${ids.map((i) => `    async ${i}(a) {}\n`).join('')}}\n`,
  });
  const idx = "export * from './AApi';\nexport * from './BApi';\n";
  const root = "export * from './apis/index';\n";

  it('finds the class', () => {
    expect(findGroupClasses([api('AApi.ts', 'AApi', ['foo'])], [op('foo')], idx, root)).toEqual({ g: { className: 'AApi' } });
  });
  it('throws when a group operation is in no API file', () => {
    expect(() => findGroupClasses([api('AApi.ts', 'AApi', ['bar'])], [op('foo')], idx, root)).toThrow(/no generated API class/);
  });
  it('throws when the method is in several API files', () => {
    const apis = [api('AApi.ts', 'AApi', ['foo']), api('BApi.ts', 'BApi', ['foo'])];
    expect(() => findGroupClasses(apis, [op('foo')], idx, root)).toThrow(/several API files/);
  });
  it('throws when the class is not exported from apis/index', () => {
    expect(() => findGroupClasses([api('CApi.ts', 'CApi', ['foo'])], [op('foo')], idx, root)).toThrow(/not exported/);
  });
  it('throws when the generated index does not re-export apis', () => {
    expect(() => findGroupClasses([api('AApi.ts', 'AApi', ['foo'])], [op('foo')], idx, '')).toThrow(/re-export/);
  });
});

describe('the rendered webhook required-field table', () => {
  it('the committed table covers every webhook schema', () => {
    for (const w of WEBHOOKS) expect(WEBHOOK_MODELS[w.schema], w.schema).toBeDefined();
    expect(Object.values(WEBHOOK_MODELS).some((m) => m.required.length > 1)).toBe(true);
  });
});
