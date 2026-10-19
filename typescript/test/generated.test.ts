import { readFileSync } from 'node:fs';
import { describe, expect, it } from 'vitest';
import * as generated from '../src/generated/index.ts';
import { EVENT_TYPES, GROUPS, OPERATIONS } from '../src/generated/meta.ts';

const groups = Object.values(
  JSON.parse(readFileSync(new URL('../../shared/api-groups.json', import.meta.url), 'utf8')),
) as string[];

describe('generated client', () => {
  it('maps all 19 groups to exported API classes', () => {
    expect(groups).toHaveLength(19);
    for (const g of groups) {
      expect(GROUPS[g], g).toBeDefined();
      expect((generated as Record<string, unknown>)[GROUPS[g].className], g).toBeTypeOf('function');
    }
  });
  it('has 320 operations', () => {
    expect(OPERATIONS.length).toBe(320);
  });
  it('names webhook event types', () => {
    expect(EVENT_TYPES[1]).toBe('ORDER_STATUS_CHANGE');
  });
});
