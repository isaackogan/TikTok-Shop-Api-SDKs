import { describe, expect, it } from 'vitest';
import { webhookModels } from '../lib/webhook-models.ts';

describe('webhookModels (the required-field table behind strict webhook parsing, R28)', () => {
  const hook = [{ type: 1, schema: 'W' }];
  const S = '#/components/schemas/';
  it('follows objects, nullable objects, lists and maps, keeping required names', () => {
    const out = webhookModels(
      {
        W: { required: ['type', 'data'], properties: { type: { type: 'integer' }, data: { $ref: S + 'D' } } },
        D: {
          required: ['id'],
          properties: {
            id: { type: 'string' },
            maybe: { anyOf: [{ $ref: S + 'M' }, { type: 'null' }] },
            list: { type: 'array', items: { $ref: S + 'L' } },
            map: { type: 'object', additionalProperties: { $ref: S + 'V' } },
            tags: { type: 'array', items: { type: 'string' } },
          },
        },
        M: { required: ['m'] },
        L: { required: ['l'] },
        V: {},
      },
      hook,
    );
    expect(out.W).toEqual({ required: ['type', 'data'], children: { data: ['object', 'D'] } });
    expect(out.D!.children).toEqual({ maybe: ['object', 'M'], list: ['list', 'L'], map: ['map', 'V'] });
    expect(out.L!.required).toEqual(['l']);
  });
  const unhandled: [string, object][] = [
    ['a list of lists', { type: 'array', items: { type: 'array', items: { $ref: S + 'D' } } }],
    ['an inline object', { type: 'object', properties: { a: { type: 'string' } } }],
    ['a combinator', { oneOf: [{ $ref: S + 'D' }, { type: 'string' }] }],
    ['a list of inline objects', { type: 'array', items: { type: 'object', properties: { a: { type: 'string' } } } }],
  ];
  for (const [name, prop] of unhandled) {
    it(`throws at generation on ${name}`, () => {
      expect(() => webhookModels({ W: { properties: { p: prop as never } }, D: {} }, hook)).toThrow(/W\.p/);
    });
  }
  it('throws when a webhook model has a "raw" property', () => {
    expect(() => webhookModels({ W: { properties: { raw: { type: 'string' } } } }, hook)).toThrow(/raw/);
  });
});
