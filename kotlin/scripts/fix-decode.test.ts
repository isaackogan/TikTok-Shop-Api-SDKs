import assert from 'node:assert/strict';
import { test } from 'node:test';
import { DECODE_LINE, fixDecode } from './fix-decode.ts';

const sample = (line: string) => `when {\n    json -> {\n        val bodyContent = body.string()\n        ${line}\n    }\n}\n`;

test('wraps the stock decode line, keeping its indentation', () => {
  const out = fixDecode(sample(DECODE_LINE));
  assert.ok(out.includes(`        try { // fix-up: scripts/fix-decode.ts (R13d)\n            ${DECODE_LINE}\n        } catch (e: RuntimeException) {`));
  assert.ok(out.includes('decodeFailure(response.code, bodyContent, e)'));
});

test('throws on zero matches', () => {
  assert.throws(() => fixDecode('nothing here'), /expected exactly one/);
});

test('throws on two matches', () => {
  assert.throws(() => fixDecode(sample(DECODE_LINE) + sample(DECODE_LINE)), /expected exactly one/);
});

test('throws when something follows the call on its line', () => {
  assert.throws(() => fixDecode(sample(`${DECODE_LINE} as T`)), /whole-line/);
});
