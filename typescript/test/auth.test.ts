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
