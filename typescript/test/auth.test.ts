import { readFileSync } from 'node:fs';
import { createServer, type Server } from 'node:http';
import type { AddressInfo } from 'node:net';
import { afterAll, beforeAll, describe, expect, it } from 'vitest';
import { TikTokShopAuth, TikTokShopError } from '../src/index.ts';

const vectors = JSON.parse(readFileSync(new URL('../../shared/test-vectors/auth.json', import.meta.url), 'utf8'));

let server: Server;
let baseUrl: string;
let seenUrls: string[] = [];
let seenMethods: string[] = [];
let replyBody = '';

beforeAll(async () => {
  server = createServer((req, res) => {
    seenUrls.push(req.url ?? '');
    seenMethods.push(req.method ?? '');
    res.writeHead(200, { 'content-type': 'application/json' });
    res.end(replyBody);
  });
  await new Promise<void>((r) => server.listen(0, '127.0.0.1', r));
  baseUrl = `http://127.0.0.1:${(server.address() as AddressInfo).port}`;
});
afterAll(() => new Promise<void>((r) => server.close(() => r())));

describe('authorizationUrl', () => {
  for (const c of vectors.authorizationUrls) {
    it(`${c.type}/${c.region}/${c.state}`, () => {
      const auth = new TikTokShopAuth({
        appKey: c.appKey ?? 'unused',
        appSecret: 's',
        serviceId: c.serviceId ?? undefined,
      });
      expect(auth.authorizationUrl({ type: c.type, region: c.region, state: c.state ?? undefined })).toBe(c.url);
    });
  }
  it('requires a serviceId for seller', () => {
    expect(() => new TikTokShopAuth({ appKey: 'a', appSecret: 's' }).authorizationUrl({ type: 'seller', region: 'us' })).toThrow();
  });
});

describe('token calls', () => {
  for (const req of vectors.tokenRequests) {
    for (const resp of vectors.tokenResponses) {
      it(`${req.kind} / ${resp.name}`, async () => {
        seenUrls = [];
        seenMethods = [];
        replyBody = resp.body;
        const auth = new TikTokShopAuth({ appKey: req.appKey, appSecret: req.appSecret, baseUrl });
        const call = req.kind === 'exchange' ? auth.exchangeCode(req.value) : auth.refresh(req.value);
        expect(seenUrls).toEqual([]);
        if (resp.errorCode !== null) {
          const err = await call.catch((e) => e);
          expect(err).toBeInstanceOf(TikTokShopError);
          expect(err.code).toBe(resp.errorCode);
          expect(err.requestId).toBe('r2');
        } else {
          expect(await call).toEqual(resp.expected);
        }
        expect(seenMethods).toEqual(['GET']);
        expect(baseUrl + seenUrls[0]).toBe(req.url.replace('https://auth.tiktok-shops.com', baseUrl));
      });
    }
  }
});

describe('token response without data', () => {
  for (const body of ['{"code":0,"message":"ok","request_id":"r9"}', '{"code":0,"message":"ok","request_id":"r9","data":null}', '{"code":0,"message":"ok","request_id":"r9","data":"x"}']) {
    it(body, async () => {
      replyBody = body;
      const auth = new TikTokShopAuth({ appKey: 'a', appSecret: 's', baseUrl });
      const err = await auth.exchangeCode('c').catch((e) => e);
      expect(err).toBeInstanceOf(TikTokShopError);
      expect(err.requestId).toBe('r9');
    });
  }
});

describe('optional token fields', () => {
  it('accepts a response with only the four required fields', async () => {
    replyBody = '{"code":0,"request_id":"r","data":{"access_token":"a","access_token_expire_in":1,"refresh_token":"r","refresh_token_expire_in":2}}';
    const t = await new TikTokShopAuth({ appKey: 'a', appSecret: 's', baseUrl }).exchangeCode('c');
    expect([t.accessToken, t.accessTokenExpireIn, t.refreshToken, t.refreshTokenExpireIn]).toEqual(['a', 1, 'r', 2]);
    for (const k of ['openId', 'sellerName', 'sellerBaseRegion', 'userType', 'grantedScopes'] as const) expect(t[k]).toBeUndefined();
  });
});

describe('token errors never contain secrets', () => {
  const SECRETS = ['SECRET-app-secret-9f3', 'SECRET-auth-code-7c1', 'SECRET-refresh-tok-2b8'];
  const chainText = (err: unknown): string => {
    const parts: string[] = [];
    const seen = new Set<unknown>();
    for (let e = err; e !== undefined && e !== null && !seen.has(e); e = (e as any).cause) {
      seen.add(e);
      parts.push(String(e), JSON.stringify(e, Object.getOwnPropertyNames(Object(e))) ?? '', String((e as any).stack ?? ''));
    }
    return parts.join('\n');
  };
  const calls = (auth: TikTokShopAuth) => [() => auth.exchangeCode(SECRETS[1]!), () => auth.refresh(SECRETS[2]!)];
  const expectClean = async (call: () => Promise<unknown>) => {
    const err = await call().then(() => undefined, (e) => e);
    expect(err).toBeDefined();
    const text = chainText(err);
    for (const s of SECRETS) expect(text).not.toContain(s);
  };

  it('closed port', async () => {
    const closed = createServer();
    await new Promise<void>((r) => closed.listen(0, '127.0.0.1', r));
    const port = (closed.address() as AddressInfo).port;
    await new Promise<void>((r) => closed.close(() => r()));
    const auth = new TikTokShopAuth({ appKey: 'k', appSecret: SECRETS[0]!, baseUrl: `http://127.0.0.1:${port}` });
    for (const call of calls(auth)) await expectClean(call);
  });

  it('timeout', async () => {
    const auth = new TikTokShopAuth({
      appKey: 'k',
      appSecret: SECRETS[0]!,
      baseUrl,
      fetch: (_url, init) => new Promise((_, reject) => {
        const signal = AbortSignal.timeout(20);
        signal.addEventListener('abort', () => reject(signal.reason));
        void init;
      }),
    });
    for (const call of calls(auth)) await expectClean(call);
  });

  // node-fetch, for one, puts the full request URL in its error messages ("request to <url> failed, reason: ...").
  it('a custom fetch whose error embeds the request URL', async () => {
    const auth = new TikTokShopAuth({
      appKey: 'k',
      appSecret: SECRETS[0]!,
      baseUrl,
      fetch: async (url) => {
        throw new Error(`request to ${String(url)} failed, reason: connect ECONNREFUSED`);
      },
    });
    for (const call of calls(auth)) {
      await expectClean(call);
      const err = await call().catch((e) => e);
      expect(err.message).toMatch(/^Token request failed: request to http:\/\/127\.0\.0\.1:\d+\/api\/v2\/token\/\w+ failed, reason: connect ECONNREFUSED$/);
    }
  });

  it('a custom fetch whose error embeds the URL, with secrets that need percent-encoding', async () => {
    const secrets = ['app+sec/ret=1 &x', 'auth+co/de=2 &y', 'refresh+to/ken=3 &z'];
    const auth = new TikTokShopAuth({
      appKey: 'k',
      appSecret: secrets[0]!,
      baseUrl,
      fetch: async (url) => {
        throw new Error(`request to ${String(url)} failed`);
      },
    });
    for (const call of [() => auth.exchangeCode(secrets[1]!), () => auth.refresh(secrets[2]!)]) {
      const text = chainText(await call().catch((e) => e));
      for (const s of secrets) {
        expect(encodeURIComponent(s)).not.toBe(s);
        expect(text).not.toContain(s);
        expect(text).not.toContain(encodeURIComponent(s));
      }
    }
  });

  it('a body read error that embeds the request URL', async () => {
    const auth = new TikTokShopAuth({
      appKey: 'k',
      appSecret: SECRETS[0]!,
      baseUrl,
      fetch: async (url) =>
        new Response(new ReadableStream({ start: (c) => c.error(new Error(`invalid response body at: ${String(url)}`)) }), { status: 200 }),
    });
    for (const call of calls(auth)) await expectClean(call);
  });
});

describe('required token fields', () => {
  const full: Record<string, unknown> = { access_token: 'a', access_token_expire_in: 1, refresh_token: 'r', refresh_token_expire_in: 2 };
  for (const missing of Object.keys(full)) {
    it(`rejects a response missing ${missing}`, async () => {
      const data = { ...full };
      delete data[missing];
      replyBody = JSON.stringify({ code: 0, request_id: 'q7', data });
      const err = await new TikTokShopAuth({ appKey: 'a', appSecret: 's', baseUrl }).exchangeCode('c').catch((e) => e);
      expect(err).toBeInstanceOf(TikTokShopError);
      expect(err.code).toBe(-1);
      expect(err.requestId).toBe('q7');
      expect(err.message).toContain(missing);
    });
  }
  it('rejects wrong types on refresh', async () => {
    replyBody = JSON.stringify({ code: 0, request_id: 'q8', data: { ...full, access_token: '' } });
    const err = await new TikTokShopAuth({ appKey: 'a', appSecret: 's', baseUrl }).refresh('c').catch((e) => e);
    expect(err).toBeInstanceOf(TikTokShopError);
    expect(err.requestId).toBe('q8');
  });
});

describe('wrong-typed token fields', () => {
  const full: Record<string, unknown> = { access_token: 'a', access_token_expire_in: 1, refresh_token: 'r', refresh_token_expire_in: 2 };
  const cases: [string, unknown][] = [
    ['access_token_expire_in', '1'],
    ['refresh_token_expire_in', '2'],
    ['refresh_token', 5],
    ['access_token', null],
  ];
  for (const [k, v] of cases) {
    it(`${k} = ${JSON.stringify(v)}`, async () => {
      replyBody = JSON.stringify({ code: 0, request_id: 'q5', data: { ...full, [k]: v } });
      const err = await new TikTokShopAuth({ appKey: 'a', appSecret: 's', baseUrl }).exchangeCode('c').catch((e) => e);
      expect(err).toBeInstanceOf(TikTokShopError);
      expect(err.code).toBe(-1);
      expect(err.requestId).toBe('q5');
    });
  }
  it('normalises null optional fields to undefined', async () => {
    replyBody = JSON.stringify({ code: 0, request_id: 'q', data: { ...full, open_id: null, seller_name: null, seller_base_region: null, user_type: null, granted_scopes: null } });
    const t = await new TikTokShopAuth({ appKey: 'a', appSecret: 's', baseUrl }).exchangeCode('c');
    for (const k of ['openId', 'sellerName', 'sellerBaseRegion', 'userType', 'grantedScopes'] as const) expect(t[k]).toBeUndefined();
  });
});
