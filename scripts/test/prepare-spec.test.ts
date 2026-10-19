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
    expect(meta.idFields).toEqual(['big', 'product_id', 'shop_id', 'sku_ids']);
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
