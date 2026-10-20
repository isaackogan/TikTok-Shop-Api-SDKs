// Cross-language rules from the final review: R13c, R13d, lesson 34 and the minors that align TypeScript with the
// other seven SDKs.
import { readFileSync } from 'node:fs';
import { createServer, type IncomingMessage, type Server } from 'node:http';
import type { AddressInfo } from 'node:net';
import { afterAll, afterEach, beforeAll, beforeEach, describe, expect, it, vi } from 'vitest';
import { DEFAULT_TIMEOUT_MS, TikTokShop, TikTokShopAuth, TikTokShopError, USER_AGENT } from '../src/index.ts';

const PKG = JSON.parse(readFileSync(new URL('../package.json', import.meta.url), 'utf8')) as { version: string };

let server: Server;
let baseUrl: string;
let reply: { status: number; body: string; reason?: string } = { status: 200, body: '' };
let seen: IncomingMessage[] = [];

beforeAll(async () => {
  server = createServer((req, res) => {
    req.resume();
    req.on('end', () => {
      seen.push(req);
      if (reply.reason !== undefined) res.writeHead(reply.status, reply.reason, { 'content-type': 'application/json' });
      else res.writeHead(reply.status, { 'content-type': 'application/json' });
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
afterEach(() => vi.restoreAllMocks());

const client = (extra = {}) => new TikTokShop({ appKey: 'k', appSecret: 's', accessToken: 't', baseUrl, ...extra });
const auth = (extra = {}) => new TikTokShopAuth({ appKey: 'k', appSecret: 's', baseUrl, ...extra });
const tokenData = { access_token: 'a', access_token_expire_in: 1, refresh_token: 'r', refresh_token_expire_in: 2 };

async function closedPort(): Promise<string> {
  const tmp = createServer();
  await new Promise<void>((r) => tmp.listen(0, '127.0.0.1', r));
  const port = (tmp.address() as AddressInfo).port;
  await new Promise<void>((r) => tmp.close(() => r()));
  return `http://127.0.0.1:${port}`;
}

async function withHangingServer(fn: (url: string) => Promise<void>): Promise<void> {
  const hang = createServer(() => {});
  await new Promise<void>((r) => hang.listen(0, '127.0.0.1', r));
  try {
    await fn(`http://127.0.0.1:${(hang.address() as AddressInfo).port}`);
  } finally {
    hang.closeAllConnections();
    await new Promise<void>((r) => hang.close(() => r()));
  }
}

function expectTransportError(err: unknown) {
  expect(err).toBeInstanceOf(TikTokShopError);
  const e = err as TikTokShopError;
  expect(e.code).toBe(-1);
  expect(e.httpStatus).toBeUndefined();
  expect(e.cause).toBeDefined();
}

describe('R13c: a transport failure is code -1 with no httpStatus', () => {
  it('API call, closed port', async () => {
    expectTransportError(await client({ baseUrl: await closedPort() }).authorization.getAuthorizedShops().catch((e) => e));
  });
  it('API call, timeout', async () => {
    await withHangingServer(async (url) => {
      const err = await client({ baseUrl: url, timeoutMs: 100 }).authorization.getAuthorizedShops().catch((e) => e);
      expectTransportError(err);
      expect(err.message).toMatch(/timed out/);
    });
  });
  it('API call with a GET body (node:http path), closed port', async () => {
    const err = await client({ baseUrl: await closedPort() })
      .affiliateSeller.getConversationList({ pageSize: 1, getConversationListRequest: { onlyNeedConversationId: true } })
      .catch((e) => e);
    expectTransportError(err);
  });
  it('token calls, closed port', async () => {
    const a = auth({ baseUrl: await closedPort() });
    for (const call of [() => a.exchangeCode('c'), () => a.refresh('r')]) expectTransportError(await call().catch((e) => e));
  });
  it('token calls, timeout', async () => {
    await withHangingServer(async (url) => {
      const a = auth({ baseUrl: url, timeoutMs: 100 });
      for (const call of [() => a.exchangeCode('c'), () => a.refresh('r')]) {
        const err = await call().catch((e) => e);
        expectTransportError(err);
        expect(err.message).toMatch(/timed out/);
      }
    });
  });
});

describe('M1: timeouts', () => {
  it('API calls default to 30 s; 0 means no limit', async () => {
    expect(DEFAULT_TIMEOUT_MS).toBe(30_000);
    const spy = vi.spyOn(AbortSignal, 'timeout');
    await client().authorization.getAuthorizedShops();
    expect(spy).toHaveBeenCalledWith(30_000);
    spy.mockClear();
    await client({ timeoutMs: 0 }).authorization.getAuthorizedShops();
    expect(spy).not.toHaveBeenCalled();
  });
  it('token calls default to 30 s, take timeoutMs, and 0 means no limit', async () => {
    reply.body = JSON.stringify({ code: 0, request_id: 'r', data: tokenData });
    const spy = vi.spyOn(AbortSignal, 'timeout');
    await auth().exchangeCode('c');
    expect(spy).toHaveBeenLastCalledWith(30_000);
    await auth({ timeoutMs: 1234 }).refresh('r');
    expect(spy).toHaveBeenLastCalledWith(1234);
    spy.mockClear();
    await auth({ timeoutMs: 0 }).refresh('r');
    expect(spy).not.toHaveBeenCalled();
  });
});

describe('M2: a 2xx envelope error carries httpStatus 200', () => {
  it('API call', async () => {
    reply.body = '{"code":36009003,"message":"bad","request_id":"q1","data":{}}';
    const err = await client().authorization.getAuthorizedShops().catch((e) => e);
    expect([err.code, err.httpStatus, err.requestId]).toEqual([36009003, 200, 'q1']);
  });
  it('token call', async () => {
    reply.body = '{"code":36004004,"message":"bad","request_id":"q2"}';
    const err = await auth().exchangeCode('c').catch((e) => e);
    expect([err.code, err.httpStatus, err.requestId]).toEqual([36004004, 200, 'q2']);
  });
  it('token call: code 0 without data, and a missing required field', async () => {
    reply.body = '{"code":0,"request_id":"q3"}';
    expect((await auth().exchangeCode('c').catch((e) => e)).httpStatus).toBe(200);
    reply.body = JSON.stringify({ code: 0, request_id: 'q4', data: { ...tokenData, access_token: '' } });
    expect((await auth().exchangeCode('c').catch((e) => e)).httpStatus).toBe(200);
  });
});

describe('M20 (lesson 34): a 2xx whose code is present but not an integer is unreadable: -1', () => {
  for (const code of ['"0"', '1.5', 'true', 'null', '{}']) {
    it(`API call, code ${code}`, async () => {
      reply.body = `{"code":${code},"message":"m","request_id":"q5","data":{}}`;
      const err = await client().authorization.getAuthorizedShops().catch((e) => e);
      expect(err).toBeInstanceOf(TikTokShopError);
      expect([err.code, err.httpStatus, err.requestId]).toEqual([-1, 200, 'q5']);
    });
    it(`token call, code ${code}`, async () => {
      reply.body = JSON.stringify({ code: JSON.parse(code), request_id: 'q6', data: tokenData });
      const err = await auth().exchangeCode('c').catch((e) => e);
      expect(err).toBeInstanceOf(TikTokShopError);
      expect([err.code, err.httpStatus]).toEqual([-1, 200]);
    });
  }
  it('a 2xx with no code at all is still a success (API)', async () => {
    reply.body = '{"request_id":"q","data":{}}';
    await expect(client().authorization.getAuthorizedShops()).resolves.toBeDefined();
  });
  it('a non-2xx with a non-integer code uses the HTTP status', async () => {
    reply = { status: 503, body: '{"code":1.5,"message":"m"}' };
    const err = await client().authorization.getAuthorizedShops().catch((e) => e);
    expect([err.code, err.httpStatus]).toEqual([503, 503]);
  });
});

describe('M17: an empty reason phrase falls through to "HTTP <status>"', () => {
  it('API call', async () => {
    reply = { status: 503, body: '{}', reason: '' };
    const err = await client().authorization.getAuthorizedShops().catch((e) => e);
    expect(err.message).toBe('HTTP 503');
  });
});

describe('M18 (lesson 34): User-Agent is tiktok-shop-api-typescript/<version>', () => {
  it('matches package.json', () => {
    expect(USER_AGENT).toBe(`tiktok-shop-api-typescript/${PKG.version}`);
  });
  it('is sent on API calls, including a GET with a body', async () => {
    await client().authorization.getAuthorizedShops();
    await client().affiliateSeller.getConversationList({ pageSize: 1, getConversationListRequest: { onlyNeedConversationId: true } });
    expect(seen.map((r) => r.headers['user-agent'])).toEqual([USER_AGENT, USER_AGENT]);
  });
  it('is sent on token calls', async () => {
    reply.body = JSON.stringify({ code: 0, request_id: 'r', data: tokenData });
    await auth().exchangeCode('c');
    await auth().refresh('r');
    expect(seen.map((r) => r.headers['user-agent'])).toEqual([USER_AGENT, USER_AGENT]);
  });
});

describe('M19 (lesson 34): an empty state is omitted from the authorization URL', () => {
  it('seller and creator', () => {
    const a = new TikTokShopAuth({ appKey: 'ak', appSecret: 's', serviceId: 'svc' });
    expect(a.authorizationUrl({ type: 'seller', region: 'us', state: '' })).toBe('https://services.us.tiktokshop.com/open/authorize?service_id=svc');
    expect(a.authorizationUrl({ type: 'creator', region: 'row', state: '' })).toBe('https://shop.tiktok.com/alliance/creator/auth?app_key=ak');
  });
});

describe('M3: token validation', () => {
  for (const [k, v] of [['access_token_expire_in', 1.5], ['refresh_token_expire_in', 2 ** 53], ['access_token_expire_in', true]] as const) {
    it(`rejects a non-integer ${k} = ${String(v)}`, async () => {
      reply.body = JSON.stringify({ code: 0, request_id: 'q7', data: { ...tokenData, [k]: v } });
      const err = await auth().exchangeCode('c').catch((e) => e);
      expect(err).toBeInstanceOf(TikTokShopError);
      expect([err.code, err.requestId]).toEqual([-1, 'q7']);
    });
  }
  it('treats wrong-typed optional fields as absent', async () => {
    reply.body = JSON.stringify({
      code: 0,
      request_id: 'q',
      data: { ...tokenData, open_id: true, seller_name: 5, seller_base_region: ['US'], user_type: 'x', granted_scopes: 'scope' },
    });
    const t = await auth().exchangeCode('c');
    for (const k of ['openId', 'sellerName', 'sellerBaseRegion', 'userType', 'grantedScopes'] as const) expect(t[k], k).toBeUndefined();
  });
  it('a granted_scopes list with a non-string item is absent; a non-integer user_type is absent', async () => {
    reply.body = JSON.stringify({ code: 0, request_id: 'q', data: { ...tokenData, granted_scopes: ['a', 1], user_type: 1.5 } });
    const t = await auth().exchangeCode('c');
    expect([t.grantedScopes, t.userType]).toEqual([undefined, undefined]);
  });
  it('keeps well-typed optional fields, and a numeric open_id as its exact digits', async () => {
    reply.body = `{"code":0,"request_id":"q","data":{"access_token":"a","access_token_expire_in":1,"refresh_token":"r","refresh_token_expire_in":2,"open_id":7010736057180325637,"seller_name":"S","seller_base_region":"US","user_type":0,"granted_scopes":["x"]}}`;
    const t = await auth().exchangeCode('c');
    expect([t.openId, t.sellerName, t.sellerBaseRegion, t.userType, t.grantedScopes]).toEqual(['7010736057180325637', 'S', 'US', 0, ['x']]);
  });
});

describe('R12: unknown response fields decode', () => {
  it('at data level and inside a nested model', async () => {
    reply.body =
      '{"code":0,"message":"Success","request_id":"r","data":{"brand_new":1,"id":"1729507467923261408","skus":[{"id":"2","seller_sku":"s","future":{"a":[1]}}]}}';
    const res = await client().products.getProduct({ productId: '1729507467923261408' });
    expect(res.data?.id).toBe('1729507467923261408');
    expect(res.data?.skus?.[0]?.sellerSku).toBe('s');
  });
});

describe('R13d: a 2xx envelope that does not fit its model', () => {
  // typescript-fetch's FromJSON copies scalars without checking their types (they arrive as sent), but it throws on a
  // list or object of the wrong shape. That throw becomes a TikTokShopError with code -1.
  it('a wrong-typed list is a TikTokShopError with code -1, httpStatus, requestId and the decoder error as cause', async () => {
    reply.body = '{"code":0,"message":"Success","request_id":"q9","data":{"skus":"not a list"}}';
    const err = await client().products.getProduct({ productId: '1' }).catch((e) => e);
    expect(err).toBeInstanceOf(TikTokShopError);
    expect([err.code, err.httpStatus, err.requestId]).toEqual([-1, 200, 'q9']);
    expect(err.cause).toBeInstanceOf(TypeError);
  });
  it('a wrong-typed nested object is a TikTokShopError too', async () => {
    reply.body = '{"code":0,"message":"Success","request_id":"q10","data":{"skus":[{"id":"1","sales_attributes":"not a list"}]}}';
    const err = await client().products.getProduct({ productId: '1' }).catch((e) => e);
    expect(err).toBeInstanceOf(TikTokShopError);
    expect([err.code, err.requestId]).toEqual([-1, 'q10']);
  });
  it('a wrong-typed scalar is returned as sent (documented leniency)', async () => {
    reply.body = '{"code":0,"message":"Success","request_id":"r","data":{"id":{"not":"a string"}}}';
    const res = await client().products.getProduct({ productId: '1' });
    expect(res.data?.id as unknown).toEqual({ not: 'a string' });
  });
});

describe('R21b: an integer enum value the spec does not list still decodes', () => {
  it('user_type_tag', async () => {
    reply.body = '{"code":0,"request_id":"r","data":{"creators":[{"creator_profile":{"user_type_tag":[1,3]}}]}}';
    const res = await client().affiliateSeller.searchCreatorsInCreatorMarketplace({ pageSize: 1 });
    const tags: number[] | undefined = res.data?.creators?.[0]?.creatorProfile?.userTypeTag;
    expect(tags).toEqual([1, 3]);
  });
});
