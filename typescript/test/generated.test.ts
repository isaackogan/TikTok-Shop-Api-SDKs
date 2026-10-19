import { readFileSync } from 'node:fs';
import { describe, expect, it } from 'vitest';
import * as generated from '../src/generated/index.ts';
import { EVENT_TYPES, GROUPS, ID_BODY_PATHS, ID_FIELDS, OPERATIONS, WEBHOOKS } from '../src/generated/meta.ts';
import { findGroupClasses } from '../scripts/render-meta.ts';

const groups = Object.values(
  JSON.parse(readFileSync(new URL('../../shared/api-groups.json', import.meta.url), 'utf8')),
) as string[];
const meta = JSON.parse(readFileSync(new URL('../build/meta.json', import.meta.url), 'utf8'));

describe('generated client', () => {
  it('maps all 19 groups to exported API classes', () => {
    expect(groups).toHaveLength(19);
    for (const g of groups) {
      expect(GROUPS[g], g).toBeDefined();
      expect((generated as Record<string, unknown>)[GROUPS[g].className], g).toBeTypeOf('function');
    }
  });
  it('has 320 operations matching meta.json', () => {
    expect(OPERATIONS.length).toBe(320);
    expect(OPERATIONS).toEqual(meta.operations);
  });
  it('carries the webhooks and event types from meta.json', () => {
    expect(WEBHOOKS).toHaveLength(44);
    expect(WEBHOOKS).toEqual(meta.webhooks);
    expect(EVENT_TYPES[1]).toBe('ORDER_STATUS_CHANGE');
    expect(Object.keys(EVENT_TYPES)).toHaveLength(16);
  });
  it('carries the ID fields from meta.json', () => {
    expect(ID_FIELDS).toEqual(meta.idFields);
    for (const f of ['product_id', 'shop_id', 'sku_id', 'material_id', 'tts_pid']) {
      expect(ID_FIELDS).toContain(f);
    }
  });
  it('carries the request-body ID paths from meta.json', () => {
    expect(meta.idBodyPaths).toBeTypeOf('object');
    expect(ID_BODY_PATHS).toEqual(meta.idBodyPaths);
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
