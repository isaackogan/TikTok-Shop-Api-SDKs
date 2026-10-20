import { request as httpRequest, type IncomingMessage } from 'node:http';
import { request as httpsRequest } from 'node:https';
import { ID_FIELDS } from './generated/meta.ts';
import { parseJsonExact } from './json.ts';

export interface TransportOptions {
  /** Sends every request except a GET with a body. Defaults to the global `fetch`. */
  fetch?: typeof fetch;
  /** Per-request timeout in milliseconds, used when the request carries no signal of its own. */
  timeoutMs?: number;
}

/**
 * The `fetchApi` for the generated client. Its responses' `.json()` keeps 64-bit IDs exact
 * (`parseJsonExact` with `ID_FIELDS`). The default `fetch` never follows a redirect (a supplied one is used as is).
 * A GET with a body, which `fetch` refuses, is sent with
 * `node:http`/`node:https` instead and comes back as a standard `Response`.
 */
export function createFetchApi(options: TransportOptions = {}): typeof fetch {
  const base = options.fetch ?? ((...a: Parameters<typeof fetch>) => fetch(...a));
  const ms = options.timeoutMs;
  return async (input, init) => {
    const signal = init?.signal ?? (ms ? AbortSignal.timeout(ms) : undefined);
    const method = (init?.method ?? 'GET').toUpperCase();
    const res =
      method === 'GET' && init?.body != null && !(input instanceof Request)
        ? await sendWithBody(String(input), init, signal)
        : await base(input, { ...init, ...(signal ? { signal } : {}), ...(options.fetch ? {} : { redirect: 'manual' as const }) });
    return exactJson(res);
  };
}

/** Makes `res.json()` (and that of its clones) parse with {@link parseJsonExact}. */
function exactJson(res: Response): Response {
  const clone = res.clone.bind(res);
  return Object.defineProperties(res, {
    json: { value: async () => parseJsonExact(await res.text(), ID_FIELDS), configurable: true, writable: true },
    clone: { value: () => exactJson(clone()), configurable: true, writable: true },
  });
}

async function sendWithBody(url: string, init: RequestInit, signal?: AbortSignal): Promise<Response> {
  signal?.throwIfAborted();
  const u = new URL(url);
  const send = u.protocol === 'https:' ? httpsRequest : u.protocol === 'http:' ? httpRequest : undefined;
  if (!send) throw new TypeError(`Unsupported protocol for a GET with a body: ${u.protocol}`);
  // Encode any BodyInit the way fetch would, including its default content type.
  const encoded = new Response(init.body);
  const body = new Uint8Array(await encoded.arrayBuffer());
  const headers = new Headers(init.headers);
  const defaultType = encoded.headers.get('content-type');
  if (!headers.has('content-type') && defaultType) headers.set('content-type', defaultType);
  headers.set('content-length', String(body.byteLength));
  const plain: Record<string, string> = {};
  headers.forEach((v, k) => (plain[k] = v));

  return new Promise<Response>((resolve, reject) => {
    const req = send(u, { method: 'GET', headers: plain });
    const onAbort = () => {
      reject(signal!.reason);
      req.destroy();
    };
    signal?.addEventListener('abort', onAbort, { once: true });
    const settle = (fn: () => void) => {
      signal?.removeEventListener('abort', onAbort);
      try {
        fn();
      } catch (e) {
        reject(e);
      }
    };
    req.on('error', (e) => settle(() => reject(e)));
    req.on('response', (res) => {
      const chunks: Buffer[] = [];
      res.on('data', (c: Buffer) => chunks.push(c));
      res.on('error', (e) => settle(() => reject(e)));
      res.on('close', () => {
        if (!res.complete) settle(() => reject(new Error('The connection closed before the response ended')));
      });
      res.on('end', () => settle(() => resolve(toResponse(res, Buffer.concat(chunks)))));
    });
    req.end(body);
  });
}

function toResponse(res: IncomingMessage, body: Uint8Array): Response {
  const headers = new Headers();
  for (let i = 0; i < res.rawHeaders.length; i += 2) headers.append(res.rawHeaders[i], res.rawHeaders[i + 1]);
  const status = res.statusCode ?? 0;
  // A Response cannot carry a body with these statuses.
  const nullBody = status === 204 || status === 205 || status === 304;
  return new Response(nullBody ? null : new Uint8Array(body), { status, statusText: res.statusMessage, headers });
}
