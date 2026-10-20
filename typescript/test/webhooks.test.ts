import { createHmac } from 'node:crypto';
import { readFileSync } from 'node:fs';
import { describe, expect, it } from 'vitest';
import { EVENT_TYPES, isUnknownWebhookEvent, WebhookParseError, Webhooks, WebhookSignatureError } from '../src/index.ts';

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
  it('keeps an order_status the spec does not list (R21)', () => {
    const ev = Webhooks.parse('{"type":1,"shop_id":"1","data":{"order_status":"SOME_NEW_STATUS"}}') as any;
    expect(ev.raw).toBeUndefined();
    const status: string | undefined = ev.data.orderStatus;
    expect(status).toBe('SOME_NEW_STATUS');
  });
  it('accepts bytes', () => {
    expect((Webhooks.parse(Buffer.from('{"type":1,"shop_id":"1"}')) as any).shopId).toBe('1');
  });
});

// Lesson 16 + R28: parsing is strict. Only an integer `type` the SDK doesn't know becomes an UnknownWebhookEvent.
describe('strict parsing (lesson 16, R28)', () => {
  // Type 66 (AppealCompletedWebhook) has required fields at every level, including inside a list.
  const appeal = () => ({
    type: 66,
    shop_id: '1',
    tts_notification_id: 'n1',
    timestamp: 1,
    data: { product_id: 'p1', appeal_task: { appeal_audit_result: [{ indicator_type: 'A', status: 'S' }] } },
  });
  it('parses a complete known event', () => {
    const ev = Webhooks.parse(JSON.stringify(appeal())) as any;
    expect(isUnknownWebhookEvent(ev)).toBe(false);
    expect(ev.data.appealTask.appealAuditResult[0].status).toBe('S');
  });
  const bad: [string, string][] = [
    ['not JSON', 'nope'],
    ['an array', '[{"type":1}]'],
    ['a number', '1'],
    ['a string', '"x"'],
    ['null', 'null'],
    ['no type', '{"shop_id":"1"}'],
    ['a string type', '{"type":"1"}'],
    ['a bool type', '{"type":true}'],
    ['a null type', '{"type":null}'],
    ['a float type', '{"type":1.5}'],
    ['an unsafe integer type', '{"type":9007199254740993}'],
  ];
  for (const [name, body] of bad) {
    it(`rejects ${name}`, () => {
      expect(() => Webhooks.parse(body)).toThrow(WebhookParseError);
    });
  }
  const broken: [string, (j: any) => void, string][] = [
    ['a missing top-level required field', (j) => delete j.shop_id, 'shop_id'],
    ['a null top-level required field', (j) => (j.timestamp = null), 'timestamp'],
    ['a missing nested required field', (j) => delete j.data.product_id, 'data.product_id'],
    ['a null required field inside a list', (j) => (j.data.appeal_task.appeal_audit_result[0].status = null), 'data.appeal_task.appeal_audit_result[0].status'],
  ];
  for (const [name, edit, path] of broken) {
    it(`rejects a known type with ${name}`, () => {
      const j = appeal();
      edit(j);
      expect(() => Webhooks.parse(JSON.stringify(j))).toThrow(WebhookParseError);
      expect(() => Webhooks.parse(JSON.stringify(j))).toThrow(path);
    });
  }
  it('rejects a known type whose list field is not a list (FromJSON would throw a TypeError)', () => {
    const j = appeal() as any;
    j.data.appeal_task.appeal_audit_result = 'x';
    expect(() => Webhooks.parse(JSON.stringify(j))).toThrow(WebhookParseError);
  });
  const wrongKind: [string, (j: any) => void][] = [
    ['data is a string', (j) => (j.data = 'not an object')],
    ['a nested object is a number', (j) => (j.data.appeal_task = 5)],
    ['a nested object is a list', (j) => (j.data.appeal_task = [{ appeal_audit_result: [] }])],
    ['a list item is a string', (j) => (j.data.appeal_task.appeal_audit_result = ['x'])],
  ];
  for (const [name, edit] of wrongKind) {
    it(`rejects a known type where a model should be an object: ${name}`, () => {
      const j = appeal();
      edit(j);
      expect(() => Webhooks.parse(JSON.stringify(j))).toThrow(WebhookParseError);
    });
  }
  it("rejects the reviewer's probe: type 66 with data a string", () => {
    const body = '{"type":66,"shop_id":"1","tts_notification_id":"n","timestamp":1,"data":"not an object"}';
    expect(() => Webhooks.parse(body)).toThrow(WebhookParseError);
    const signature = createHmac('sha256', 's').update('k' + body).digest('hex');
    expect(() => Webhooks.verifyAndParse({ appKey: 'k', appSecret: 's', rawBody: body, signature })).toThrow(WebhookParseError);
  });
  it('rejects bytes that are not UTF-8', () => {
    expect(() => Webhooks.parse(new Uint8Array([0x7b, 0xff, 0x7d]))).toThrow(WebhookParseError);
  });
  it('an integer type it does not know is an UnknownWebhookEvent, not an error', () => {
    const ev = Webhooks.parse('{"type":9999,"anything":[1]}');
    expect(isUnknownWebhookEvent(ev)).toBe(true);
    expect(ev.type).toBe(9999);
  });
  it('verifyAndParse is strict too: a correctly signed body that is not an object is a parse error', () => {
    const signature = createHmac('sha256', 's').update('k[]').digest('hex');
    expect(Webhooks.verify({ appKey: 'k', appSecret: 's', rawBody: '[]', signature })).toBe(true);
    expect(() => Webhooks.verifyAndParse({ appKey: 'k', appSecret: 's', rawBody: '[]', signature })).toThrow(WebhookParseError);
  });
});

describe('R12: unknown fields are kept out of the way, never an error', () => {
  it('parses a known event with extra fields at the top level and inside data', () => {
    const j = { type: 1, shop_id: '1', brand_new: { x: 1 }, data: { order_id: '5', order_status: 'UNPAID', future_field: [1, 2] } };
    const ev = Webhooks.parse(JSON.stringify(j)) as any;
    expect(isUnknownWebhookEvent(ev)).toBe(false);
    expect(ev.data.orderStatus).toBe('UNPAID');
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
