import { TikTokShopError } from './errors.ts';
import { parseJsonExact } from './json.ts';

export const DEFAULT_AUTH_BASE_URL = 'https://auth.tiktok-shops.com';

export interface TikTokShopAuthOptions {
  appKey: string;
  appSecret: string;
  /** Your Partner Center service ID. Needed for `seller` and `partner` authorization URLs. */
  serviceId?: string;
  /** Token endpoint host. Defaults to `https://auth.tiktok-shops.com`. */
  baseUrl?: string;
  /** HTTP client override (defaults to the global `fetch`). */
  fetch?: typeof fetch;
}

export interface AuthorizationUrlOptions {
  type: 'seller' | 'partner' | 'creator';
  region: 'us' | 'row';
  state?: string;
}

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
    return `${host}${h.path}?${first}${state === undefined ? '' : `&state=${enc(state)}`}`;
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
    const res = await (this.#opts.fetch ?? fetch)(url, { method: 'GET' });
    const text = await res.text();
    let env: any;
    try {
      env = parseJsonExact(text, ['open_id']);
    } catch (cause) {
      throw new TikTokShopError({ code: -1, message: `Unparseable token response (HTTP ${res.status})`, requestId: '', httpStatus: res.status, cause });
    }
    const code = typeof env?.code === 'number' ? env.code : res.ok ? -1 : res.status;
    if (code !== 0 || !res.ok) {
      throw new TikTokShopError({
        code,
        message: env?.message ?? `HTTP ${res.status}`,
        requestId: env?.request_id ?? '',
        httpStatus: res.ok ? undefined : res.status,
      });
    }
    const d = env.data;
    if (typeof d !== 'object' || d === null || Array.isArray(d)) {
      throw new TikTokShopError({ code: -1, message: 'Token response has no data', requestId: env.request_id ?? '' });
    }
    for (const k of ['access_token', 'refresh_token']) {
      if (typeof d[k] !== 'string' || d[k] === '') {
        throw new TikTokShopError({ code: -1, message: `Token response is missing ${k}`, requestId: env.request_id ?? '' });
      }
    }
    for (const k of ['access_token_expire_in', 'refresh_token_expire_in']) {
      if (typeof d[k] !== 'number') {
        throw new TikTokShopError({ code: -1, message: `Token response is missing ${k}`, requestId: env.request_id ?? '' });
      }
    }
    return {
      accessToken: d.access_token,
      accessTokenExpireIn: d.access_token_expire_in,
      refreshToken: d.refresh_token,
      refreshTokenExpireIn: d.refresh_token_expire_in,
      openId: d.open_id,
      sellerName: d.seller_name,
      sellerBaseRegion: d.seller_base_region,
      userType: d.user_type,
      grantedScopes: d.granted_scopes ?? undefined,
    };
  }
}
