import { createServer, type IncomingMessage, type Server } from 'node:http';
import type { AddressInfo } from 'node:net';
import { afterAll, beforeAll, beforeEach, describe, expect, it } from 'vitest';
import { createFetchApi } from '../src/transport.ts';

interface Seen {
  method: string;
  url: string;
  headers: IncomingMessage['headers'];
  body: string;
}

let server: Server;
let base: string;
let seen: Seen[] = [];
let reply: { status: number; body: string | null; hang?: boolean } = { status: 200, body: '{}' };

beforeAll(async () => {
  server = createServer((req, res) => {
    const chunks: Buffer[] = [];
    req.on('data', (c) => chunks.push(c));
    req.on('end', () => {
      seen.push({ method: req.method ?? '', url: req.url ?? '', headers: req.headers, body: Buffer.concat(chunks).toString('utf8') });
      if (reply.hang) return;
      res.writeHead(reply.status, reply.body === null ? {} : { 'content-type': 'application/json', 'x-tts-logid': 'log1' });
      res.end(reply.body ?? undefined);
    });
  });
  await new Promise<void>((r) => server.listen(0, '127.0.0.1', r));
  base = `http://127.0.0.1:${(server.address() as AddressInfo).port}`;
});
afterAll(() => {
  server.closeAllConnections();
  return new Promise<void>((r) => server.close(() => r()));
});
beforeEach(() => {
  seen = [];
  reply = { status: 200, body: '{}' };
});

/** A fetch override that records its calls and never touches the network. */
function fakeFetch(body = '{}') {
  const calls: { url: string; method: string; body: unknown }[] = [];
  const f = (async (input: RequestInfo | URL, init?: RequestInit) => {
    calls.push({ url: String(input), method: init?.method ?? 'GET', body: init?.body });
    return new Response(body, { status: 200, headers: { 'content-type': 'application/json' } });
  }) as typeof fetch;
  return { f, calls };
}

const BIG = '{"code":0,"data":{"product_id":7494049642642441621,"count":3,"total":9007199254740993,"video_ids":[1,2]}}';
const EXACT = { code: 0, data: { product_id: '7494049642642441621', count: 3, total: '9007199254740993', video_ids: ['1', '2'] } };

describe('createFetchApi', () => {
  it('sends a GET with a body over node:http, with the body and headers intact', async () => {
    const { f, calls } = fakeFetch();
    const res = await createFetchApi({ fetch: f })(`${base}/chat/x?a=1&b=%2B`, {
      method: 'GET',
      headers: { 'Content-Type': 'application/json', 'x-tts-access-token': 'tok' },
      body: '{"page_size":"10"}',
    });
    expect(calls).toHaveLength(0);
    expect(seen).toHaveLength(1);
    expect(seen[0]).toMatchObject({ method: 'GET', url: '/chat/x?a=1&b=%2B', body: '{"page_size":"10"}' });
    expect(seen[0].headers['content-type']).toBe('application/json');
    expect(seen[0].headers['x-tts-access-token']).toBe('tok');
    expect(seen[0].headers['content-length']).toBe('18');
    expect(res).toBeInstanceOf(Response);
    expect(res.status).toBe(200);
    expect(res.ok).toBe(true);
    expect(res.headers.get('x-tts-logid')).toBe('log1');
    expect(await res.text()).toBe('{}');
  });

  it('uses fetch for every other request', async () => {
    const { f, calls } = fakeFetch();
    const api = createFetchApi({ fetch: f });
    await api(`${base}/a`, { method: 'POST', body: '{"x":1}' });
    await api(`${base}/b`, { method: 'GET' });
    expect(calls.map((c) => [c.method, c.url, c.body])).toEqual([
      ['POST', `${base}/a`, '{"x":1}'],
      ['GET', `${base}/b`, undefined],
    ]);
    expect(seen).toHaveLength(0);
  });

  it('reads JSON exactly from fetch responses, also through clone()', async () => {
    const res = await createFetchApi({ fetch: fakeFetch(BIG).f })(`${base}/a`, { method: 'POST' });
    expect(await res.clone().json()).toEqual(EXACT);
    expect(await res.json()).toEqual(EXACT);
  });

  it('reads JSON exactly from GET-with-body responses', async () => {
    reply = { status: 200, body: BIG };
    const res = await createFetchApi()(`${base}/a`, { method: 'GET', body: '{}' });
    expect(await res.clone().json()).toEqual(EXACT);
    expect(await res.json()).toEqual(EXACT);
  });

  it('returns error statuses and empty bodies as responses', async () => {
    const api = createFetchApi();
    reply = { status: 500, body: '{"code":1}' };
    const err = await api(`${base}/a`, { method: 'GET', body: '{}' });
    expect([err.status, err.ok, await err.text()]).toEqual([500, false, '{"code":1}']);
    reply = { status: 204, body: null };
    const empty = await api(`${base}/a`, { method: 'GET', body: '{}' });
    expect([empty.status, await empty.text()]).toEqual([204, '']);
  });

  it('times out a GET with a body after timeoutMs', async () => {
    reply = { status: 200, body: '{}', hang: true };
    const err = await createFetchApi({ timeoutMs: 100 })(`${base}/a`, { method: 'GET', body: '{}' }).catch((e) => e);
    expect(err).toBeInstanceOf(Error);
    expect(err.name).toBe('TimeoutError');
  });

  it("aborts a GET with a body on the caller's signal", async () => {
    reply = { status: 200, body: '{}', hang: true };
    const ctl = new AbortController();
    const p = createFetchApi()(`${base}/a`, { method: 'GET', body: '{}', signal: ctl.signal });
    setTimeout(() => ctl.abort(), 50);
    const err = await p.catch((e) => e);
    expect(err.name).toBe('AbortError');
  });

  it('rejects a GET with a body when the connection fails', async () => {
    const tmp = createServer();
    await new Promise<void>((r) => tmp.listen(0, '127.0.0.1', r));
    const port = (tmp.address() as AddressInfo).port;
    await new Promise<void>((r) => tmp.close(() => r()));
    const err = await createFetchApi()(`http://127.0.0.1:${port}/a`, { method: 'GET', body: '{}' }).catch((e) => e);
    expect(err).toBeInstanceOf(Error);
    expect(err.code).toBe('ECONNREFUSED');
  });

  it('speaks TLS to an https URL', async () => {
    // The stub only speaks plain HTTP, so a TLS handshake fails before any request reaches it.
    const err = await createFetchApi()(`${base.replace('http:', 'https:')}/a`, { method: 'GET', body: '{}' }).catch((e) => e);
    expect(err).toBeInstanceOf(Error);
    expect(seen).toHaveLength(0);
  });
});
