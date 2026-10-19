import { createServer, type IncomingMessage, type Server } from 'node:http';
import type { AddressInfo } from 'node:net';
import { afterAll, beforeAll, beforeEach, describe, expect, it } from 'vitest';
import { OPERATIONS } from '../src/generated/meta.ts';
import { sign, TikTokShop, TikTokShopError } from '../src/index.ts';

interface Seen {
  method: string;
  path: string;
  rawQuery: string;
  query: [string, string][];
  headers: IncomingMessage['headers'];
  body: string;
}

let server: Server;
let baseUrl: string;
let seen: Seen[] = [];
let reply: { status: number; body: string } = { status: 200, body: '{"code":0,"message":"Success","request_id":"r0","data":{}}' };

const decode = (s: string) => decodeURIComponent(s);
function parseQuery(raw: string): [string, string][] {
  return raw === ''
    ? []
    : raw.split('&').map((p) => {
        const i = p.indexOf('=');
        return [decode(p.slice(0, i)), decode(p.slice(i + 1))] as [string, string];
      });
}

beforeAll(async () => {
  server = createServer((req, res) => {
    const chunks: Buffer[] = [];
    req.on('data', (c) => chunks.push(c));
    req.on('end', () => {
      const u = req.url ?? '';
      const qi = u.indexOf('?');
      const rawQuery = qi < 0 ? '' : u.slice(qi + 1);
      seen.push({
        method: req.method ?? '',
        path: qi < 0 ? u : u.slice(0, qi),
        rawQuery,
        query: parseQuery(rawQuery),
        headers: req.headers,
        body: Buffer.concat(chunks).toString('utf8'),
      });
      res.writeHead(reply.status, { 'content-type': 'application/json' });
      res.end(reply.body);
    });
  });
  await new Promise<void>((r) => server.listen(0, '127.0.0.1', r));
  baseUrl = `http://127.0.0.1:${(server.address() as AddressInfo).port}`;
});
afterAll(() => new Promise<void>((r) => server.close(() => r())));
beforeEach(() => {
  seen = [];
  reply = { status: 200, body: '{"code":0,"message":"Success","request_id":"r0","data":{}}' };
});

const make = (extra = {}) =>
  new TikTokShop({ appKey: 'k1', appSecret: 's1', accessToken: 'tok', shopCipher: 'cipher1', baseUrl, ...extra });

function checkSigned(s: Seen, secret = 's1') {
  const sent = s.query.find(([k]) => k === 'sign')![1];
  const rest = s.query.filter(([k]) => k !== 'sign');
  const ct = (s.headers['content-type'] as string | undefined) ?? null;
  const expected = sign({
    path: s.path,
    query: rest,
    contentType: ct,
    body: s.body === '' ? null : new TextEncoder().encode(s.body),
    appSecret: secret,
  });
  expect(sent).toBe(expected);
}
const q = (s: Seen, k: string) => s.query.find(([n]) => n === k)?.[1];

describe('stub transport', () => {
  it('getAuthorizedShops: app_key, timestamp, sign, token, no shop_cipher', async () => {
    await make().authorization.getAuthorizedShops();
    const s = seen[0];
    expect(s.path).toBe('/authorization/202309/shops');
    expect(q(s, 'app_key')).toBe('k1');
    expect(Number(q(s, 'timestamp'))).toBeGreaterThan(1_700_000_000);
    expect(s.headers['x-tts-access-token']).toBe('tok');
    expect(q(s, 'shop_cipher')).toBeUndefined();
    checkSigned(s);
  });

  it('getOrderList sends shop_cipher and a page_token with + / = intact', async () => {
    await make().orders.getOrderList({ pageSize: 20, pageToken: 'b2Zmc2V0PTEw+/x==' });
    const s = seen[0];
    expect(s.method).toBe('POST');
    expect(q(s, 'shop_cipher')).toBe('cipher1');
    expect(q(s, 'page_token')).toBe('b2Zmc2V0PTEw+/x==');
    checkSigned(s);
  });

  it('signs a JSON body', async () => {
    await make().orders.getOrderList({ pageSize: 5, getOrderListRequest: { orderStatus: 'UNPAID' } as never });
    const s = seen[0];
    expect(s.body).toContain('UNPAID');
    checkSigned(s);
  });

  it('rewrites ID fields in the JSON body to bare numbers', async () => {
    await make().affiliateSeller.createOpenCollaboration({
      createOpenCollaborationRequest: { productId: '7494049642642441621' } as never,
    });
    const s = seen[0];
    expect(s.body).toContain('"product_id":7494049642642441621');
    expect(s.body).not.toContain('"7494049642642441621"');
    checkSigned(s);
  });

  it('omits the token header when there is no access token', async () => {
    await make({ accessToken: undefined }).authorization.getAuthorizedShops();
    expect(seen[0].headers['x-tts-access-token']).toBeUndefined();
  });

  it('raises TikTokShopError for code != 0 with HTTP 200', async () => {
    reply = { status: 200, body: '{"code":36009003,"message":"invalid","request_id":"r1","data":{}}' };
    const err = await make().authorization.getAuthorizedShops().catch((e) => e);
    expect(err).toBeInstanceOf(TikTokShopError);
    expect(err.code).toBe(36009003);
    expect(err.message).toBe('invalid');
    expect(err.requestId).toBe('r1');
  });

  it('raises TikTokShopError with httpStatus for non-2xx', async () => {
    reply = { status: 500, body: '{"code":1,"message":"boom","request_id":"r2"}' };
    const err = await make().authorization.getAuthorizedShops().catch((e) => e);
    expect(err).toBeInstanceOf(TikTokShopError);
    expect(err.httpStatus).toBe(500);
    expect(err.requestId).toBe('r2');
  });

  it('withShop changes token and cipher without touching the original', async () => {
    const a = make();
    const b = a.withShop({ accessToken: 'tok2', shopCipher: 'cipher2' });
    await b.orders.getOrderList({ pageSize: 1 });
    await a.orders.getOrderList({ pageSize: 1 });
    expect(seen[0].headers['x-tts-access-token']).toBe('tok2');
    expect(q(seen[0], 'shop_cipher')).toBe('cipher2');
    expect(seen[1].headers['x-tts-access-token']).toBe('tok');
    expect(q(seen[1], 'shop_cipher')).toBe('cipher1');
  });
});

describe('wiring', () => {
  it('every operation is reachable as client.<group>.<operationId>', () => {
    const c = make() as unknown as Record<string, Record<string, unknown>>;
    for (const op of OPERATIONS) {
      expect(typeof c[op.group]?.[op.operationId], `${op.group}.${op.operationId}`).toBe('function');
    }
  });
});
