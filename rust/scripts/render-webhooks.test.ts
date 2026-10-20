import assert from 'node:assert/strict';
import { test } from 'node:test';
import { stringPaths, variantName } from './render-webhooks.ts';

const ref = (n: string) => ({ $ref: `#/components/schemas/${n}` });

test('top-level, nested object and nullable strings; non-strings are skipped', () => {
  const schemas = {
    Root: {
      type: 'object',
      properties: {
        shop_id: { type: 'string' },
        timestamp: { type: 'integer' },
        note: { type: ['string', 'null'] },
        data: { type: 'object', properties: { order_id: { type: 'string' }, n: { type: 'number' } } },
      },
    },
  };
  assert.deepEqual(stringPaths(schemas, 'Root'), [['shop_id'], ['note'], ['data', 'order_id']]);
});

test('arrays of strings and arrays of objects', () => {
  const schemas = {
    Root: {
      type: 'object',
      properties: {
        ids: { type: 'array', items: { type: 'string' } },
        rows: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' } } } },
      },
    },
  };
  assert.deepEqual(stringPaths(schemas, 'Root'), [['ids', '[]'], ['rows', '[]', 'id']]);
});

test('$ref and allOf are followed', () => {
  const schemas = {
    Root: { type: 'object', properties: { inner: ref('Inner'), merged: { allOf: [ref('Inner'), { type: 'object', properties: { extra: { type: 'string' } } }] } } },
    Inner: { type: 'object', properties: { id: { type: 'string' } } },
  };
  assert.deepEqual(stringPaths(schemas, 'Root'), [['inner', 'id'], ['merged', 'id'], ['merged', 'extra']]);
});

test('a $ref cycle terminates', () => {
  const schemas = {
    Node: { type: 'object', properties: { id: { type: 'string' }, next: ref('Node'), kids: { type: 'array', items: ref('Node') } } },
  };
  assert.deepEqual(stringPaths(schemas, 'Node'), [['id']]);
});

test('an additionalProperties map of strings gets a wildcard segment', () => {
  const schemas = {
    Root: { type: 'object', properties: { labels: { type: 'object', additionalProperties: { type: 'string' } }, flags: { type: 'object', additionalProperties: true } } },
  };
  assert.deepEqual(stringPaths(schemas, 'Root'), [['labels', '*']]);
});

test('an unresolved $ref is an error', () => {
  assert.throws(() => stringPaths({ Root: { properties: { a: ref('Missing') } } }, 'Root'), /unresolved/);
});

test('variant names come from the generated model name', () => {
  assert.equal(variantName('FbtMerchantOnboardingWebhook'), 'FbtMerchantOnboarding');
  assert.equal(variantName('OrderStatusChangeWebhook'), 'OrderStatusChange');
});
