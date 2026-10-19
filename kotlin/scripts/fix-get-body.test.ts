import assert from 'node:assert/strict';
import { test } from 'node:test';
import { GET_FIXUP, GET_LINE, fixGetBody } from './fix-get-body.ts';

const sample = (get: string) => `when (m) {\n    RequestMethod.DELETE -> x\n    ${get}\n    RequestMethod.HEAD -> y\n}\n`;

test('replaces the stock line, keeping indentation and the rest', () => {
  const out = fixGetBody(sample(GET_LINE));
  assert.equal(out, sample(GET_FIXUP));
  assert.ok(!out.includes(`${GET_LINE}\n`));
});

test('throws on zero matches', () => {
  assert.throws(() => fixGetBody('nothing here'), /expected exactly one/);
});

test('throws on two matches', () => {
  assert.throws(() => fixGetBody(sample(GET_LINE) + sample(GET_LINE)), /expected exactly one/);
});

test('a stock line with trailing code is not silently commented out', () => {
  assert.throws(() => fixGetBody(sample(`${GET_LINE}.get()`)), /expected exactly one/);
});
