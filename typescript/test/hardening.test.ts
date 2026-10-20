import { createServer, type Server } from 'node:http';
import type { AddressInfo } from 'node:net';
import { inspect } from 'node:util';
import { afterAll, beforeAll, describe, expect, it } from 'vitest';
import { TikTokShop, TikTokShopAuth, TikTokShopError } from '../src/index.ts';

const SECRET = 'super-secret-value';
const TOKEN = 'tok-value-xyz';
const CIPHER = 'cipher-value-xyz';
const REFRESH = 'refresh-value-xyz';

const forms = (o: object): string[] => [
  inspect(o, { depth: null, showHidden: true }),
  inspect(o, { depth: null, getters: true }),
  String(o),
  JSON.stringify(o) ?? '',
  `${JSON.stringify({ wrapped: o })}`,
];

function expectNoSecrets(o: object) {
  for (const text of forms(o)) for (const s of [SECRET, TOKEN, CIPHER, REFRESH]) expect(text).not.toContain(s);
}

describe('secrets never appear in debug or string forms', () => {
  it('TikTokShop shows none under util.inspect, String() or JSON.stringify', () => {
    const client = new TikTokShop({ appKey: 'appkey1', appSecret: SECRET, accessToken: TOKEN, shopCipher: CIPHER });
    expectNoSecrets(client);
    expectNoSecrets(client.withShop({ accessToken: TOKEN, shopCipher: CIPHER }));
    expectNoSecrets(client.orders);
  });
  it('TikTokShopAuth shows none', () => {
    expectNoSecrets(new TikTokShopAuth({ appKey: 'appkey1', appSecret: SECRET, serviceId: 'svc' }));
  });
  it('the client still works after hiding its options (withShop keeps unspecified values)', async () => {
    const seen: string[] = [];
    const fetchSpy: typeof fetch = async (input, init) => {
      seen.push(`${String(input)}|${new Headers(init?.headers).get('x-tts-access-token')}`);
      return new Response('{"code":0,"message":"Success","request_id":"r","data":{}}', { headers: { 'content-type': 'application/json' } });
    };
    const c = new TikTokShop({ appKey: 'k', appSecret: SECRET, accessToken: TOKEN, shopCipher: CIPHER, fetch: fetchSpy });
    await c.withShop({ shopCipher: 'other' }).orders.getOrderList({ pageSize: 1 });
    expect(seen[0]).toContain('shop_cipher=other');
    expect(seen[0]).toContain(`|${TOKEN}`);
  });
  it('TokenSet stays a plain, serialisable data object', async () => {
    const server = createServer((_req, res) => {
      res.writeHead(200, { 'content-type': 'application/json' });
      res.end(JSON.stringify({ code: 0, request_id: 'r', data: { access_token: TOKEN, access_token_expire_in: 1, refresh_token: REFRESH, refresh_token_expire_in: 2 } }));
    });
    await new Promise<void>((r) => server.listen(0, '127.0.0.1', r));
    try {
      const baseUrl = `http://127.0.0.1:${(server.address() as AddressInfo).port}`;
      const ts = await new TikTokShopAuth({ appKey: 'k', appSecret: SECRET, baseUrl }).exchangeCode('c');
      expect(JSON.parse(JSON.stringify(ts))).toMatchObject({ accessToken: TOKEN, refreshToken: REFRESH });
    } finally {
      server.close();
    }
  });
});

describe('redirects are never followed by SDK-built clients', () => {
  let origin: Server;
  let target: Server;
  let originUrl: string;
  let targetHits = 0;

  beforeAll(async () => {
    target = createServer((_req, res) => {
      targetHits++;
      res.writeHead(200, { 'content-type': 'application/json' });
      res.end('{"code":0,"message":"Success","request_id":"r","data":{}}');
    });
    await new Promise<void>((r) => target.listen(0, '127.0.0.1', r));
    const targetUrl = `http://127.0.0.1:${(target.address() as AddressInfo).port}`;
    origin = createServer((_req, res) => {
      res.writeHead(302, { location: `${targetUrl}/stolen` });
      res.end();
    });
    await new Promise<void>((r) => origin.listen(0, '127.0.0.1', r));
    originUrl = `http://127.0.0.1:${(origin.address() as AddressInfo).port}`;
  });
  afterAll(async () => {
    await Promise.all([origin, target].map((s) => new Promise<void>((r) => s.close(() => r()))));
  });

  it('an API call gets the 302 as an error with code and httpStatus 302, and the target sees nothing', async () => {
    targetHits = 0;
    const err = await new TikTokShop({ appKey: 'k', appSecret: 's', accessToken: TOKEN, baseUrl: originUrl }).authorization
      .getAuthorizedShops().catch((e) => e);
    expect(err).toBeInstanceOf(TikTokShopError);
    expect(err.code).toBe(302);
    expect(err.httpStatus).toBe(302);
    expect(targetHits).toBe(0);
  });

  it('a GET with a body (node:http path) does not follow either', async () => {
    targetHits = 0;
    const err = await new TikTokShop({ appKey: 'k', appSecret: 's', accessToken: TOKEN, baseUrl: originUrl }).affiliateSeller
      .getConversationList({ pageSize: 10, getConversationListRequest: { onlyNeedConversationId: true } } as never).catch((e) => e);
    expect(err).toBeInstanceOf(TikTokShopError);
    expect(err.code).toBe(302);
    expect(targetHits).toBe(0);
  });

  it('a token call gets the 302 as an error with code and httpStatus 302', async () => {
    targetHits = 0;
    const err = await new TikTokShopAuth({ appKey: 'k', appSecret: 's', baseUrl: originUrl }).exchangeCode('c').catch((e) => e);
    expect(err).toBeInstanceOf(TikTokShopError);
    expect(err.code).toBe(302);
    expect(err.httpStatus).toBe(302);
    expect(targetHits).toBe(0);
  });

  it('a supplied fetch is used as is: it receives no redirect option from the SDK', async () => {
    const inits: (RequestInit | undefined)[] = [];
    const custom: typeof fetch = async (_input, init) => {
      inits.push(init);
      return new Response('{"code":0,"message":"Success","request_id":"r","data":{}}', { headers: { 'content-type': 'application/json' } });
    };
    await new TikTokShop({ appKey: 'k', appSecret: 's', fetch: custom }).authorization.getAuthorizedShops();
    expect(inits).toHaveLength(1);
    expect(inits[0]?.redirect).toBeUndefined();
  });
});

describe('R13a: a failure without a TikTok code uses the HTTP status as its code', () => {
  let server: Server;
  let baseUrl: string;
  let reply = { status: 503, body: '' };
  beforeAll(async () => {
    server = createServer((_req, res) => {
      res.writeHead(reply.status, { 'content-type': 'application/json' });
      res.end(reply.body);
    });
    await new Promise<void>((r) => server.listen(0, '127.0.0.1', r));
    baseUrl = `http://127.0.0.1:${(server.address() as AddressInfo).port}`;
  });
  afterAll(() => new Promise<void>((r) => server.close(() => r())));

  for (const body of ['{"message":"x"}', '{"code":0}']) {
    it(`API call, 503 ${body}`, async () => {
      reply = { status: 503, body };
      const err = await new TikTokShop({ appKey: 'k', appSecret: 's', baseUrl }).authorization.getAuthorizedShops().catch((e) => e);
      expect(err).toBeInstanceOf(TikTokShopError);
      expect([err.code, err.httpStatus]).toEqual([503, 503]);
    });
    it(`token call, 503 ${body}`, async () => {
      reply = { status: 503, body };
      const auth = new TikTokShopAuth({ appKey: 'k', appSecret: 's', baseUrl });
      for (const call of [() => auth.exchangeCode('c'), () => auth.refresh('r')]) {
        const err = await call().catch((e) => e);
        expect(err).toBeInstanceOf(TikTokShopError);
        expect([err.code, err.httpStatus]).toEqual([503, 503]);
      }
    });
  }

  it('token: -1 only when there is no TikTok code at all', async () => {
    const auth = new TikTokShopAuth({ appKey: 'k', appSecret: 's', baseUrl });
    for (const [status, body] of [[503, 'down'], [200, '<html>'], [503, '[1]'], [200, '{"code":0,"request_id":"r"}']] as const) {
      reply = { status, body };
      const err = await auth.refresh('r').catch((e) => e);
      expect(err, `${status} ${body}`).toBeInstanceOf(TikTokShopError);
      expect(err.code, `${status} ${body}`).toBe(-1);
    }
  });
});
