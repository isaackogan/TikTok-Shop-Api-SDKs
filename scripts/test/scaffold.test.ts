import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { describe, expect, it } from 'vitest';

const root = resolve(import.meta.dirname, '../..');
const read = (p: string): string => readFileSync(resolve(root, p), 'utf8');

const FOLDERS = ['typescript', 'python', 'go', 'java', 'kotlin', 'php', 'rust', 'csharp'];

describe('monorepo scaffold', () => {
  const groups: Record<string, string> = JSON.parse(read('shared/api-groups.json'));

  it('api-groups.json maps every tag used by an operation', () => {
    const spec = JSON.parse(read('.openapi/tiktok-shop.openapi.json'));
    const tags = new Set<string>();
    for (const item of Object.values<any>(spec.paths)) {
      for (const op of Object.values<any>(item)) {
        for (const tag of op?.tags ?? []) tags.add(tag);
      }
    }
    expect(tags.size).toBe(19);
    expect(Object.keys(groups).sort()).toEqual([...tags].sort());
  });

  it('group names are unique camelCase strings', () => {
    const values = Object.values(groups);
    expect(new Set(values).size).toBe(values.length);
    for (const v of values) expect(v).toMatch(/^[a-z][a-zA-Z0-9]*$/);
  });

  it('.gitattributes marks all 8 generated folders', () => {
    const attrs = read('.gitattributes');
    for (const f of FOLDERS) expect(attrs).toContain(`${f}/`);
    expect(attrs).toContain('linguist-generated=true');
  });
});
