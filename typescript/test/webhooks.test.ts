import { readFileSync } from 'node:fs';
import { describe, expect, it } from 'vitest';
import { EVENT_TYPES, Webhooks, WebhookSignatureError } from '../src/index.ts';

const vectors = JSON.parse(readFileSync(new URL('../../shared/test-vectors/webhooks.json', import.meta.url), 'utf8'));

describe('verify', () => {
  for (const c of vectors.verify) {
    it(c.name, () => {
      const args = { appKey: c.appKey, appSecret: c.appSecret, signature: c.signature };
      expect(Webhooks.verify({ ...args, rawBody: c.rawBody })).toBe(c.valid);
      expect(Webhooks.verify({ ...args, rawBody: Buffer.from(c.rawBody) })).toBe(c.valid);
      expect(Webhooks.verify({ ...args, rawBody: new TextEncoder().encode(c.rawBody) })).toBe(c.valid);
    });
  }
  it('rejects a signature of a different length', () => {
    expect(Webhooks.verify({ appKey: 'a', appSecret: 'b', rawBody: '{}', signature: 'abc' })).toBe(false);
  });
});

describe('parse', () => {
  for (const c of vectors.parse) {
    it(c.name, () => {
      const ev = Webhooks.parse(c.rawBody) as any;
      expect(ev.type).toBe(c.type);
      if (c.known) {
        expect(ev.raw).toBeUndefined();
        expect(ev.shopId).toBe('7495540735365777507');
        expect(ev.data.orderStatus).toBe('UNPAID');
      } else {
        expect(ev.raw).toEqual(JSON.parse(c.rawBody));
      }
    });
  }
  it('keeps a 19-digit shop_id sent as a JSON number exact', () => {
    const ev = Webhooks.parse('{"type":1,"shop_id":7494049642642441621,"data":{"order_id":576653688135258178}}') as any;
    expect(ev.shopId).toBe('7494049642642441621');
    expect(ev.data.orderId).toBe('576653688135258178');
  });
  it('accepts bytes', () => {
    expect((Webhooks.parse(Buffer.from('{"type":1,"shop_id":"1"}')) as any).shopId).toBe('1');
  });
});

describe('verifyAndParse', () => {
  const ok = vectors.verify[0];
  const base = { appKey: ok.appKey, appSecret: ok.appSecret, rawBody: ok.rawBody };
  it('returns the event', () => {
    expect((Webhooks.verifyAndParse({ ...base, signature: ok.signature }) as any).type).toBe(1);
  });
  it('throws on mismatch', () => {
    expect(() => Webhooks.verifyAndParse({ ...base, signature: 'bad' })).toThrow(WebhookSignatureError);
  });
});

it('EVENT_TYPES', () => {
  expect(EVENT_TYPES[1]).toBe('ORDER_STATUS_CHANGE');
});
