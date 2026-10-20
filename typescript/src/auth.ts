import { TikTokShopError } from './errors.ts';
import { parseJsonExact } from './json.ts';
import { timeoutSignal } from './transport.ts';
import { USER_AGENT } from './version.ts';

export const DEFAULT_AUTH_BASE_URL = 'https://auth.tiktok-shops.com';

export interface TikTokShopAuthOptions {
  appKey: string;
  appSecret: string;
  /** Your Partner Center service ID. Needed for `seller` and `partner` authorization URLs. */
  serviceId?: string;
  /** Token endpoint host, an origin only (no path prefix). Defaults to `https://auth.tiktok-shops.com`. */
  baseUrl?: string;
  /** Per-request timeout in milliseconds. Defaults to 30 000 (`DEFAULT_TIMEOUT_MS`); 0 means no limit. */
  timeoutMs?: number;
  /**
   * HTTP client override (defaults to the global `fetch`). The default never follows a redirect: a 3xx reply is thrown
   * as a {@link TikTokShopError} whose `code` and `httpStatus` are the status, so the app secret and the code are never
   * forwarded to another host. A `fetch` you supply is used as is, so its own redirect policy applies.
   */
  fetch?: typeof fetch;
}

export interface AuthorizationUrlOptions {
  type: 'seller' | 'partner' | 'creator';
  region: 'us' | 'row';
  state?: string;
}

/**
 * The result of exchanging an auth code or refreshing a token. It is a plain data object, so you can serialise it to
 * store it, but it holds secrets (`accessToken`, `refreshToken`): never log it, and protect wherever you store it.
 */
export interface TokenSet {
  accessToken: string;
  /** Unix timestamp (seconds) at which the access token expires. */
  accessTokenExpireIn: number;
  refreshToken: string;
  /** Unix timestamp (seconds) at which the refresh token expires. */
  refreshTokenExpireIn: number;
  /** The fields below are optional: creator and partner tokens may lack the seller fields. */
  openId?: string;
  sellerName?: string;
  sellerBaseRegion?: string;
  userType?: number;
  grantedScopes?: string[];
}

const HOSTS = {
  seller: { us: 'https://services.us.tiktokshop.com', row: 'https://services.tiktokshop.com', path: '/open/authorize' },
  partner: { us: 'https://partner.us.tiktokshop.com', row: 'https://partner.tiktokshop.com', path: '/open/authorize' },
  creator: { us: 'https://shop.tiktok.com', row: 'https://shop.tiktok.com', path: '/alliance/creator/auth' },
} as const;

/** RFC 3986 unreserved characters stay; everything else is percent-encoded. */
const enc = (s: string) => encodeURIComponent(s).replace(/[!'()*]/g, (c) => '%' + c.charCodeAt(0).toString(16).toUpperCase());

export class TikTokShopAuth {
  readonly #opts: TikTokShopAuthOptions;

  constructor(options: TikTokShopAuthOptions) {
    this.#opts = options;
  }

  authorizationUrl({ type, region, state }: AuthorizationUrlOptions): string {
    const h = HOSTS[type];
    if (!h) throw new Error(`Unknown authorization type: ${String(type)}`);
    const host = h[region];
    if (!host) throw new Error(`Unknown region: ${String(region)}`);
    let first: string;
    if (type === 'creator') {
      first = `app_key=${enc(this.#opts.appKey)}`;
    } else {
      if (!this.#opts.serviceId) throw new Error(`serviceId is required for ${type} authorization URLs`);
      first = `service_id=${enc(this.#opts.serviceId)}`;
    }
    // Lesson 34: an empty state is omitted, like an absent one.
    return `${host}${h.path}?${first}${state === undefined || state === '' ? '' : `&state=${enc(state)}`}`;
  }

  exchangeCode(code: string): Promise<TokenSet> {
    return this.#token('get', [['auth_code', code], ['grant_type', 'authorized_code']]);
  }

  refresh(refreshToken: string): Promise<TokenSet> {
    return this.#token('refresh', [['refresh_token', refreshToken], ['grant_type', 'refresh_token']]);
  }

  async #token(endpoint: 'get' | 'refresh', extra: [string, string][]): Promise<TokenSet> {
    const params: [string, string][] = [['app_key', this.#opts.appKey], ['app_secret', this.#opts.appSecret], ...extra];
    const base = (this.#opts.baseUrl ?? DEFAULT_AUTH_BASE_URL).replace(/\/+$/, '');
    const url = `${base}/api/v2/token/${endpoint}?${params.map(([k, v]) => `${k}=${enc(v)}`).join('&')}`;
    const signal = timeoutSignal(this.#opts.timeoutMs);
    const init: RequestInit = { method: 'GET', headers: { 'user-agent': USER_AGENT }, ...(signal ? { signal } : {}) };
    // 'manual' targets Node, where a 3xx comes back as a normal response; in a browser it would be an opaque status-0 response.
    if (!this.#opts.fetch) init.redirect = 'manual';
    // R15: the query carries the app secret and the code or refresh token (extra's first value), and a fetch you
    // supply may quote the URL in its errors.
    const secrets = [this.#opts.appSecret, extra[0]![1]];
    let res: Response;
    try {
      res = await (this.#opts.fetch ?? fetch)(url, init);
    } catch (e) {
      // R13c: no HTTP response at all.
      throw transportError(e, secrets);
    }
    let text: string;
    try {
      text = await res.text();
    } catch (e) {
      throw new TikTokShopError({
        code: -1,
        message: `Token response could not be read (HTTP ${res.status})`,
        requestId: '',
        httpStatus: res.status,
        cause: safeCause(e, secrets),
      });
    }
    // R13b: a reply with no usable TikTok code has the HTTP status as its code if it is non-2xx (a redirect included,
    // since it is never followed); -1 only when a 2xx reply cannot be understood.
    const noCode = res.ok ? -1 : res.status;
    let env: any;
    try {
      env = parseJsonExact(text, ['open_id']);
    } catch (cause) {
      throw new TikTokShopError({ code: noCode, message: `Unparseable token response (HTTP ${res.status})`, requestId: '', httpStatus: res.status, cause });
    }
    if (typeof env !== 'object' || env === null || Array.isArray(env)) {
      throw new TikTokShopError({ code: noCode, message: `Unexpected token response (HTTP ${res.status})`, requestId: '', httpStatus: res.status });
    }
    const requestId = typeof env.request_id === 'string' ? env.request_id : '';
    // Lesson 34: a code that is missing or not an integer makes a 2xx unreadable (-1); on a non-2xx the status is the code.
    let code = Number.isSafeInteger(env.code) ? (env.code as number) : res.ok ? -1 : res.status;
    if (code !== 0 || !res.ok) {
      if (code === 0) code = res.status; // R13a: a failure that carries no TikTok code uses the HTTP status
      throw new TikTokShopError({
        code,
        message: (typeof env.message === 'string' && env.message) || `HTTP ${res.status}`,
        requestId,
        httpStatus: res.status,
      });
    }
    const fail = (message: string) => new TikTokShopError({ code: -1, message, requestId, httpStatus: res.status });
    const d = env.data;
    if (typeof d !== 'object' || d === null || Array.isArray(d)) throw fail('Token response has no data');
    for (const k of ['access_token', 'refresh_token']) {
      if (typeof d[k] !== 'string' || d[k] === '') throw fail(`Token response is missing ${k}`);
    }
    for (const k of ['access_token_expire_in', 'refresh_token_expire_in']) {
      if (!Number.isSafeInteger(d[k])) throw fail(`Token response is missing ${k}`);
    }
    // Lesson 21: an optional field of the wrong type is treated as absent.
    const str = (v: unknown) => (typeof v === 'string' ? v : undefined);
    return {
      accessToken: d.access_token,
      accessTokenExpireIn: d.access_token_expire_in,
      refreshToken: d.refresh_token,
      refreshTokenExpireIn: d.refresh_token_expire_in,
      openId: str(d.open_id),
      sellerName: str(d.seller_name),
      sellerBaseRegion: str(d.seller_base_region),
      userType: Number.isSafeInteger(d.user_type) ? d.user_type : undefined,
      grantedScopes: Array.isArray(d.granted_scopes) && d.granted_scopes.every((x: unknown) => typeof x === 'string') ? d.granted_scopes : undefined,
    };
  }
}

function transportError(e: unknown, secrets: string[]): TikTokShopError {
  const timedOut = e instanceof Error && (e.name === 'TimeoutError' || e.name === 'AbortError');
  return new TikTokShopError({
    code: -1,
    message: `${timedOut ? 'Token request timed out or was aborted' : 'Token request failed'}: ${scrub(e instanceof Error ? e.message : String(e), secrets)}`,
    requestId: '',
    cause: safeCause(e, secrets),
  });
}

/** Each secret as sent and as it appears in the URL. */
const forms = (secrets: string[]) => secrets.filter((s) => s !== '').flatMap((s) => [s, enc(s)]);

/** R15: `text` without URL queries, token parameters or secrets. */
function scrub(text: string, secrets: string[]): string {
  let out = text
    .replace(/(\bhttps?:\/\/[^\s?#]*)\?[^\s)]*/gi, '$1')
    .replace(/[?&](?:app_key|app_secret|auth_code|refresh_token|grant_type)=[^\s&)]*/g, '');
  for (const s of forms(secrets)) out = out.replaceAll(s, '***');
  return out;
}

/**
 * R15: `e` itself when no text along its cause chain holds a secret (fetch's own errors don't), else a fresh error with
 * the same name and the scrubbed message.
 */
function safeCause(e: unknown, secrets: string[]): unknown {
  const leaks = (t: unknown) => typeof t === 'string' && forms(secrets).some((s) => t.includes(s));
  const seen = new Set<unknown>();
  for (let c: any = e; c != null && !seen.has(c); c = typeof c === 'object' ? c.cause : undefined) {
    seen.add(c);
    if (typeof c !== 'object' ? leaks(String(c)) : Object.getOwnPropertyNames(c).some((k) => leaks(c[k]))) {
      const fresh = new Error(scrub(e instanceof Error ? e.message : String(e), secrets));
      if (e instanceof Error) fresh.name = e.name;
      return fresh;
    }
  }
  return e;
}
