import { createHmac } from 'node:crypto';
import { OPERATIONS, type OperationMeta } from './generated/meta.ts';

export interface SignRequest {
  path: string;
  /** Decoded `[key, value]` pairs. */
  query: [string, string][];
  contentType: string | null;
  body: Uint8Array | string | null;
  appSecret: string;
}

const EXCLUDED = new Set(['sign', 'access_token']);

const bodyText = (b: Uint8Array | string | null): string =>
  b === null ? '' : typeof b === 'string' ? b : new TextDecoder().decode(b);

/** secret + path + sorted `key+value` pairs + body (not multipart) + secret. */
export function stringToSign(req: SignRequest): string {
  const pairs = req.query
    .filter(([k]) => !EXCLUDED.has(k))
    .sort(([a], [b]) => (a < b ? -1 : a > b ? 1 : 0));
  let s = req.appSecret + req.path;
  for (const [k, v] of pairs) s += k + v;
  const multipart = (req.contentType ?? '').toLowerCase().startsWith('multipart/form-data');
  if (!multipart) s += bodyText(req.body);
  return s + req.appSecret;
}

/** Lowercase hex HMAC-SHA256 of {@link stringToSign}, keyed with the app secret. */
export function sign(req: SignRequest): string {
  return createHmac('sha256', req.appSecret).update(stringToSign(req), 'utf8').digest('hex');
}

const escapeRe = (s: string) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
const matchers: { op: OperationMeta; literals: number; method: string; re: RegExp; needs: boolean }[] = OPERATIONS.map((op) => ({
  op,
  literals: op.path.split('/').filter((seg) => !/^\{[^}]+\}$/.test(seg)).length,
  method: op.method.toUpperCase(),
  re: new RegExp(
    '^' +
      op.path
        .split('/')
        .map((seg) => (/^\{[^}]+\}$/.test(seg) ? '[^/]+' : escapeRe(seg)))
        .join('/') +
      '$',
  ),
  needs: op.requiresShopCipher,
}));

/** Whether the operation matching `method` and `path` takes a `shop_cipher` query parameter. */
export function requiresShopCipher(method: string, path: string): boolean {
  const m = method.toUpperCase();
  return matchers.some((x) => x.method === m && x.re.test(path) && x.needs);
}

/** The operation for `method` and `path`, preferring the template with the most literal segments. */
export function operationFor(method: string, path: string): OperationMeta | undefined {
  const m = method.toUpperCase();
  let best: (typeof matchers)[number] | undefined;
  for (const x of matchers) if (x.method === m && x.re.test(path) && (!best || x.literals > best.literals)) best = x;
  return best?.op;
}
