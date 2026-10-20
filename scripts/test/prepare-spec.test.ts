import { execFileSync } from 'node:child_process';
import { existsSync, readFileSync, rmSync } from 'node:fs';
import { resolve } from 'node:path';
import { describe, expect, it } from 'vitest';
import { parseSpec, prepareSpec } from '../lib/meta.ts';

const root = resolve(import.meta.dirname, '../..');
const fixtureText = readFileSync(resolve(import.meta.dirname, 'fixtures/mini.openapi.json'), 'utf8');
const fixture = () => parseSpec(fixtureText);
const groups = { Orders: 'orders', Authorization: 'authorization' };

describe('prepareSpec', () => {
  it('removes webhooks and every ShopCipher ref, without mutating the input', () => {
    const input = fixture();
    const before = JSON.stringify(input);
    const { spec } = prepareSpec(input, 'go', groups);
    expect(JSON.stringify(input)).toBe(before);
    expect(spec).not.toHaveProperty('webhooks');
    expect(JSON.stringify(spec.paths)).not.toContain('ShopCipher');
    expect(spec.paths['/order/202309/orders/search'].post.parameters).toHaveLength(2);
  });

  it('describes operations', () => {
    const { meta } = prepareSpec(fixture(), 'go', groups);
    expect(meta.operations).toEqual([
      { operationId: 'getOrderList', tag: 'Orders', group: 'orders', method: 'post', path: '/order/202309/orders/search', requiresShopCipher: true },
      { operationId: 'getAuthorizedShops', tag: 'Authorization', group: 'authorization', method: 'get', path: '/authorization/202309/shops', requiresShopCipher: false },
      { operationId: 'getConversationList', tag: 'Mystery tools (beta)', group: 'mysteryTools', method: 'get', path: '/chat/202309/conversations', requiresShopCipher: true },
    ]);
  });

  it('describes webhooks, omitting eventType when absent', () => {
    const { meta } = prepareSpec(fixture(), 'go', groups);
    expect(meta.webhooks).toEqual([
      { type: 1, schema: 'OrderStatusChangeWebhook', eventType: 'ORDER_STATUS_CHANGE' },
      { type: 4, schema: 'PackageUpdateWebhook' },
    ]);
    expect(meta.webhooks[1]).not.toHaveProperty('eventType');
  });

  it('typescript: turns ID fields into strings and lists them', () => {
    const { spec, meta } = prepareSpec(fixture(), 'typescript', groups);
    const props = spec.components.schemas.OrderRequest.properties;
    expect(props.product_id).toEqual({ type: 'string', description: 'Product', deprecated: true });
    expect(props.sku_ids.items).toEqual({ type: 'string' });
    expect(props.big).toEqual({ type: ['string', 'null'], description: 'Large' });
    expect(props.count).toEqual({ type: 'integer', format: 'int32' });
    expect(props.serial).toEqual({ type: 'integer', format: 'int64' }); // only a string example has 16+ digits
    const params = spec.paths['/order/202309/orders/search'].post.parameters;
    expect(params[0].schema.type).toBe('integer');
    expect(params[1].schema).toEqual({ type: 'string' });
    expect(spec.paths['/chat/202309/conversations'].get.requestBody.content['application/json'].schema.properties.count.type).toBe('integer');
    expect(meta.idFields).toEqual(['big', 'file_id', 'product_id', 'shop_id', 'sku_id', 'sku_ids', 'user_id']);
  });

  it('typescript: records the request-body locations of converted IDs per operation', () => {
    const { meta } = prepareSpec(fixture(), 'typescript', groups);
    // getConversationList: its JSON body has no ID (file_id is only in the multipart body), so it is omitted.
    // OrderLine.note_id is ID-named but a string, so it is not a location. Note.replies recurses without IDs.
    expect(meta.idBodyPaths).toEqual({ getOrderList: ['big', 'buyer.user_id', 'lines[].sku_id', 'product_id', 'sku_ids[]'] });
  });

  it('typescript: records root-array and nested-array locations', () => {
    const spec = {
      paths: {
        '/a': { post: { operationId: 'a', tags: ['T'], requestBody: { content: { 'application/json': { schema: {
          type: 'array', items: { type: 'object', properties: { shop_id: { type: 'integer' }, video_ids: { type: 'array', items: { type: 'array', items: { type: 'integer' } } } } },
        } } } } } },
      },
    };
    expect(prepareSpec(spec, 'typescript', {}).meta.idBodyPaths).toEqual({ a: ['[].shop_id', '[].video_ids[][]'] });
  });

  it('typescript: throws when a converted ID sits where a body path cannot reach', () => {
    const body = (schema: object, schemas: object = {}) => ({
      paths: { '/a': { post: { operationId: 'a', tags: ['T'], requestBody: { content: { 'application/json': { schema } } } } } },
      components: { schemas },
    });
    const viaMap = body({ type: 'object', additionalProperties: { type: 'object', properties: { shop_id: { type: 'integer' } } } });
    expect(() => prepareSpec(viaMap, 'typescript', {})).toThrow(/a: .*additionalProperties/);
    const node = { type: 'object', properties: { sku_id: { type: 'integer' }, children: { type: 'array', items: { $ref: '#/components/schemas/Node' } } } };
    expect(() => prepareSpec(body({ $ref: '#/components/schemas/Node' }, { Node: node }), 'typescript', {})).toThrow(/a: .*children\[\]/);
  });

  it('typescript: leaves example values untouched', () => {
    const { spec } = prepareSpec(fixture(), 'typescript', groups);
    const ex = spec.paths['/order/202309/orders/search'].post.requestBody.content['application/json'].example;
    expect(JSON.stringify(ex)).toContain('7494049642642441621');
  });

  it('other languages change no field type and have no idFields', () => {
    const { spec, meta } = prepareSpec(fixture(), 'go', groups);
    expect(spec.components.schemas.OrderRequest.properties.product_id.type).toBe('integer');
    expect(meta).not.toHaveProperty('idFields');
    expect(meta).not.toHaveProperty('idBodyPaths');
  });
});

describe('prepareSpec: R21 relaxes response and webhook string enums', () => {
  const ok = (schema: object) => ({ '200': { description: 'ok', content: { 'application/json': { schema } } } });
  const S = '#/components/schemas/';
  const make = (o: { schemas?: object; response?: object; request?: object; params?: object[]; webhooks?: object }) => ({
    paths: {
      '/a': {
        post: {
          operationId: 'a',
          tags: ['T'],
          ...(o.params ? { parameters: o.params } : {}),
          ...(o.request ? { requestBody: { content: { 'application/json': { schema: o.request } } } } : {}),
          responses: ok(o.response ?? { type: 'object' }),
        },
      },
    },
    ...(o.webhooks ? { webhooks: o.webhooks } : {}),
    components: { schemas: o.schemas ?? {} },
  });
  const prep = (spec: object) => prepareSpec(spec, 'go', {}).spec;

  it('strips an enum on a response property', () => {
    const spec = prep(make({ response: { $ref: S + 'R' }, schemas: { R: { type: 'object', properties: { st: { type: 'string', enum: ['A', 'B'], description: 'A or B' } } } } }));
    expect(spec.components.schemas.R.properties.st).toEqual({ type: 'string', description: 'A or B' });
  });

  it('strips enums in webhook payloads, including via $ref and a component that is itself an enum', () => {
    const spec = prep(make({
      webhooks: { w: { post: { 'x-tts-webhook-type': 1, requestBody: { content: { 'application/json': { schema: { $ref: S + 'W' } } } } } } },
      schemas: {
        W: { type: 'object', properties: { data: { type: 'object', properties: { s: { $ref: S + 'Kind' } } } } },
        Kind: { type: 'string', enum: ['X', 'Y'] },
      },
    }));
    expect(spec.components.schemas.Kind.enum).toBeUndefined();
    expect(spec.components.schemas.Kind.type).toBe('string');
    expect(spec).not.toHaveProperty('webhooks');
  });

  it('keeps an enum that only a request body reaches', () => {
    const spec = prep(make({ request: { $ref: S + 'Q' }, schemas: { Q: { type: 'object', properties: { s: { type: 'string', enum: ['A'] } } } } }));
    expect(spec.components.schemas.Q.properties.s.enum).toEqual(['A']);
    const inline = prep(make({ request: { type: 'object', properties: { s: { type: 'string', enum: ['A'] } } } }));
    expect(inline.paths['/a'].post.requestBody.content['application/json'].schema.properties.s.enum).toEqual(['A']);
  });

  it('keeps query, path and header parameter enums', () => {
    const params = ['query', 'path', 'header'].map((i) => ({ name: 'p_' + i, in: i, schema: { type: 'string', enum: ['A', 'B'] } }));
    const spec = prep(make({ params, response: { type: 'object', properties: { s: { type: 'string', enum: ['A'] } } } }));
    for (const p of spec.paths['/a'].post.parameters) expect(p.schema.enum).toEqual(['A', 'B']);
    expect(spec.paths['/a'].post.responses['200'].content['application/json'].schema.properties.s.enum).toBeUndefined();
  });

  it('strips a schema shared by a request and a response', () => {
    const spec = prep(make({
      request: { $ref: S + 'Shared' },
      response: { $ref: S + 'Shared' },
      schemas: { Shared: { type: 'object', properties: { s: { type: 'string', enum: ['A'] } } } },
    }));
    expect(spec.components.schemas.Shared.properties.s.enum).toBeUndefined();
  });

  it('strips array items enums and nested inline object enums', () => {
    const spec = prep(make({
      response: { type: 'object', properties: {
        list: { type: 'array', items: { type: 'string', enum: ['A', 'B'] } },
        outer: { type: 'object', properties: { inner: { type: 'object', properties: { s: { type: 'string', enum: ['C'] } } } } },
        map: { type: 'object', additionalProperties: { type: 'string', enum: ['D'] } },
        either: { oneOf: [{ type: 'string', enum: ['E'] }, { type: 'integer' }] },
      } },
    }));
    const p = spec.paths['/a'].post.responses['200'].content['application/json'].schema.properties;
    expect(p.list.items.enum).toBeUndefined();
    expect(p.outer.properties.inner.properties.s.enum).toBeUndefined();
    expect(p.map.additionalProperties.enum).toBeUndefined();
    expect(p.either.oneOf[0].enum).toBeUndefined();
  });

  it('keeps integer enums, even on webhook payloads', () => {
    const spec = prep(make({
      response: { type: 'object', properties: { n: { type: 'integer', enum: [1, 2] } } },
      schemas: { W: { type: 'object', properties: { type: { type: 'integer', enum: [1] }, kind: { type: 'string', enum: ['A'] } } } },
      webhooks: { w: { post: { 'x-tts-webhook-type': 1, requestBody: { content: { 'application/json': { schema: { $ref: S + 'W' } } } } } } },
    }));
    expect(spec.components.schemas.W.properties.type.enum).toEqual([1]);
    expect(spec.components.schemas.W.properties.kind.enum).toBeUndefined();
    expect(spec.paths['/a'].post.responses['200'].content['application/json'].schema.properties.n.enum).toEqual([1, 2]);
  });

  it('keeps a property named "enum" or "example" and walks past it', () => {
    const spec = prep(make({ response: { type: 'object', properties: { enum: { type: 'string', enum: ['A'] } } } }));
    const props = spec.paths['/a'].post.responses['200'].content['application/json'].schema.properties;
    expect(props.enum).toEqual({ type: 'string', description: 'Possible values: `A`' });
  });

  it('strips a ["string","null"] enum, dropping x-enum-* extensions', () => {
    const spec = prep(make({ response: { type: 'object', properties: {
      s: { type: ['string', 'null'], enum: ['A', null], 'x-enum-varnames': ['A'], 'x-enum-descriptions': ['a'], description: 'A.' },
    } } }));
    const s = spec.paths['/a'].post.responses['200'].content['application/json'].schema.properties.s;
    expect(s).toEqual({ type: ['string', 'null'], description: 'A.' });
  });

  it('keeps allowed values in the description', () => {
    const schemas = {
      Listed: { type: 'string', enum: ['PAID', 'SHIPPED'], description: 'One of PAID or SHIPPED.' },
      Partial: { type: 'string', enum: ['PAID', 'SHIPPED', 'DONE'], description: 'Status, e.g. PAID.' },
      None: { type: 'string', enum: ['PAID', 'SHIPPED'] },
    };
    const spec = prep(make({
      response: { type: 'object', properties: { a: { $ref: S + 'Listed' }, b: { $ref: S + 'Partial' }, c: { $ref: S + 'None' } } },
      schemas,
    }));
    const c = spec.components.schemas;
    expect(c.Listed.description).toBe('One of PAID or SHIPPED.');
    expect(c.Partial.description).toBe('Status, e.g. PAID.\n\nPossible values: `PAID`, `SHIPPED`, `DONE`');
    expect(c.None.description).toBe('Possible values: `PAID`, `SHIPPED`');
  });

  it('follows allOf and a recursive schema once', () => {
    const spec = prep(make({
      response: { allOf: [{ $ref: S + 'Node' }] },
      schemas: { Node: { type: 'object', properties: { s: { type: 'string', enum: ['A'] }, kids: { type: 'array', items: { $ref: S + 'Node' } } } } },
    }));
    expect(spec.components.schemas.Node.properties.s.enum).toBeUndefined();
  });

  it('ignores non-2xx responses', () => {
    const input = make({ schemas: { E: { type: 'object', properties: { s: { type: 'string', enum: ['A'] } } } } });
    (input.paths['/a'].post.responses as any)['400'] = { content: { 'application/json': { schema: { $ref: S + 'E' } } } };
    expect(prep(input).components.schemas.E.properties.s.enum).toEqual(['A']);
  });

  it('does not mutate the input', () => {
    const input = make({
      response: { $ref: S + 'R' },
      schemas: { R: { type: 'object', properties: { s: { type: 'string', enum: ['A'] } } } },
      webhooks: { w: { post: { 'x-tts-webhook-type': 1, requestBody: { content: { 'application/json': { schema: { $ref: S + 'R' } } } } } } },
    });
    const before = JSON.stringify(input);
    prepareSpec(input, 'kotlin', {});
    expect(JSON.stringify(input)).toBe(before);
  });
});

describe('prepare-spec CLI', () => {
  it('writes openapi.json and meta.json under <lang>/build from any directory', () => {
    const out = resolve(root, 'go/build');
    rmSync(out, { recursive: true, force: true });
    execFileSync(resolve(root, 'scripts/node_modules/.bin/tsx'), [resolve(root, 'scripts/prepare-spec.ts'), '--lang', 'go'], { cwd: import.meta.dirname });
    expect(existsSync(resolve(out, 'openapi.json'))).toBe(true);
    const meta = JSON.parse(readFileSync(resolve(out, 'meta.json'), 'utf8'));
    expect(meta.operations).toHaveLength(320);
    rmSync(out, { recursive: true, force: true });
  });

  it('rejects an unknown language', () => {
    expect(() =>
      execFileSync(resolve(root, 'scripts/node_modules/.bin/tsx'), [resolve(root, 'scripts/prepare-spec.ts'), '--lang', 'cobol'], { stdio: 'pipe' }),
    ).toThrow();
  });
});
