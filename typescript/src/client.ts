import * as g from './generated/index.ts';
import { TikTokShopError } from './errors.ts';
import { ID_BODY_PATHS } from './generated/meta.ts';
import { rewriteIdNumbers } from './json.ts';
import { operationFor, requiresShopCipher, sign } from './signing.ts';
import { createFetchApi } from './transport.ts';
import { USER_AGENT } from './version.ts';

export const DEFAULT_BASE_URL = 'https://open-api.tiktokglobalshop.com';

export interface TikTokShopOptions {
  appKey: string;
  appSecret: string;
  accessToken?: string;
  shopCipher?: string;
  /**
   * API host, an origin only (`https://host[:port]`): any path prefix breaks signing and shop-cipher matching, which use
   * the request path. Defaults to {@link DEFAULT_BASE_URL}.
   */
  baseUrl?: string;
  /** Per-request timeout in milliseconds. Defaults to 30 000 ({@link DEFAULT_TIMEOUT_MS}); 0 means no limit. */
  timeoutMs?: number;
  /**
   * HTTP client override (defaults to the global `fetch`). A GET with a body, which `fetch`
   * refuses, is sent with `node:http`/`node:https` instead.
   *
   * The default client never follows a redirect: a 3xx reply is thrown as a {@link TikTokShopError}
   * whose `code` and `httpStatus` are the status, so the access token is never forwarded to another
   * host. A `fetch` you supply is used as is, so its own redirect policy applies.
   */
  fetch?: typeof fetch;
}

const JSON_MIME = /^application\/(?:[^;/\s]+\+)?json\s*(?:;|$)/i;

/** Parse a raw query string into decoded pairs. A literal `+` stays a `+`. */
function parseQuery(raw: string): [string, string][] {
  if (raw === '') return [];
  return raw.split('&').filter(Boolean).map((p) => {
    const i = p.indexOf('=');
    return i < 0
      ? ([decodeURIComponent(p), ''] as [string, string])
      : ([decodeURIComponent(p.slice(0, i)), decodeURIComponent(p.slice(i + 1))] as [string, string]);
  });
}

export class TikTokShop {
  readonly affiliateCreator: g.AffiliateCreatorApi;
  readonly affiliatePartner: g.AffiliatePartnerApi;
  readonly affiliateSeller: g.AffiliateSellerApi;
  readonly analytics: g.AnalyticsApi;
  readonly authorization: g.AuthorizationApi;
  readonly customerEngagement: g.CustomerEngagementApi;
  readonly customerService: g.CustomerServiceApi;
  readonly event: g.EventApi;
  readonly finance: g.FinanceApi;
  readonly fulfilledByTikTok: g.FulfilledByTikTokFBTApi;
  readonly fulfillment: g.FulfillmentApi;
  readonly logistics: g.LogisticsApi;
  readonly orders: g.OrdersApi;
  readonly products: g.ProductsApi;
  readonly promotion: g.PromotionApi;
  readonly returnAndRefund: g.ReturnAndRefundApi;
  readonly seller: g.SellerApi;
  readonly supplyChain: g.SupplyChainApi;
  readonly tools: g.ToolsApi;

  // A #private field: it never shows in util.inspect, console.log, JSON.stringify or Object.keys, so the app
  // secret, access token and shop cipher stay out of logs.
  readonly #options: TikTokShopOptions;

  constructor(options: TikTokShopOptions) {
    this.#options = options;
    const cfg = new g.Configuration({
      basePath: (options.baseUrl ?? DEFAULT_BASE_URL).replace(/\/+$/, ''),
      middleware: [{ pre: (ctx) => this.requestHook(ctx), post: (ctx) => this.responseHook(ctx),
        onError: (ctx) => this.errorHook(ctx),
      }],
      fetchApi: createFetchApi({ fetch: options.fetch, timeoutMs: options.timeoutMs }),
    });
    this.affiliateCreator = new g.AffiliateCreatorApi(cfg);
    this.affiliatePartner = new g.AffiliatePartnerApi(cfg);
    this.affiliateSeller = new g.AffiliateSellerApi(cfg);
    this.analytics = new g.AnalyticsApi(cfg);
    this.authorization = new g.AuthorizationApi(cfg);
    this.customerEngagement = new g.CustomerEngagementApi(cfg);
    this.customerService = new g.CustomerServiceApi(cfg);
    this.event = new g.EventApi(cfg);
    this.finance = new g.FinanceApi(cfg);
    this.fulfilledByTikTok = new g.FulfilledByTikTokFBTApi(cfg);
    this.fulfillment = new g.FulfillmentApi(cfg);
    this.logistics = new g.LogisticsApi(cfg);
    this.orders = new g.OrdersApi(cfg);
    this.products = new g.ProductsApi(cfg);
    this.promotion = new g.PromotionApi(cfg);
    this.returnAndRefund = new g.ReturnAndRefundApi(cfg);
    this.seller = new g.SellerApi(cfg);
    this.supplyChain = new g.SupplyChainApi(cfg);
    this.tools = new g.ToolsApi(cfg);
  }

  /** A client for another shop or token that shares this client's HTTP client. */
  withShop(shop: { accessToken?: string; shopCipher?: string }): TikTokShop {
    return new TikTokShop({ ...this.#options, ...shop });
  }

  private async requestHook(ctx: g.RequestContext): Promise<g.FetchParams> {
    const o = this.#options;
    const url = new URL(ctx.url);
    const method = (ctx.init.method ?? 'GET').toUpperCase();
    const query = parseQuery(url.search.slice(1)).filter(
      ([k]) => k !== 'app_key' && k !== 'timestamp' && k !== 'sign' && k !== 'shop_cipher',
    );
    // 1. shop_cipher
    if (o.shopCipher && requiresShopCipher(method, url.pathname)) query.push(['shop_cipher', o.shopCipher]);
    // 2. app_key, timestamp
    query.push(['app_key', o.appKey], ['timestamp', String(Math.floor(Date.now() / 1000))]);

    const headers = new Headers(ctx.init.headers as HeadersInit | undefined);
    const contentType = headers.get('content-type');
    let body = ctx.init.body;
    // 3. the operation's integer ID locations in a JSON body go out as bare JSON numbers (§6.6);
    //    every other body is sent byte-for-byte as is
    if (typeof body === 'string' && JSON_MIME.test(contentType ?? '')) {
      const op = operationFor(method, url.pathname);
      const paths = op && ID_BODY_PATHS[op.operationId];
      if (paths && paths.length > 0) body = rewriteIdNumbers(body, paths);
    }
    // 4. access token
    if (o.accessToken) headers.set('x-tts-access-token', o.accessToken);
    headers.set('user-agent', USER_AGENT);
    // 5. sign over the final path, decoded query and body
    const bodyBytes = body == null ? null : typeof body === 'string' ? body : null;
    query.push([
      'sign',
      sign({ path: url.pathname, query, contentType, body: bodyBytes, appSecret: o.appSecret }),
    ]);

    const qs = query.map(([k, v]) => `${encodeURIComponent(k)}=${encodeURIComponent(v)}`).join('&');
    return { url: `${url.origin}${url.pathname}?${qs}`, init: { ...ctx.init, headers, body } };
  }

  private async responseHook(ctx: g.ResponseContext): Promise<Response | void> {
    const res = ctx.response;
    let envelope: { code?: unknown; message?: unknown; request_id?: unknown } | null | undefined;
    let parseError: unknown;
    try {
      envelope = JSON.parse(await res.clone().text());
    } catch (e) {
      envelope = undefined;
      parseError = e;
    }
    const isObj = envelope !== null && typeof envelope === 'object' && !Array.isArray(envelope);
    // R13b: -1 only for a 2xx reply that cannot be understood (not a JSON object).
    if (res.ok && !isObj) {
      throw new TikTokShopError({
        code: -1,
        message: `Response is not valid JSON (HTTP ${res.status})`,
        requestId: '',
        httpStatus: res.status,
        cause: parseError,
      });
    }
    const rawCode = isObj ? envelope!.code : undefined;
    const code = Number.isSafeInteger(rawCode) ? (rawCode as number) : undefined;
    const message = isObj && typeof envelope!.message === 'string' ? envelope!.message : undefined;
    const requestId = isObj && typeof envelope!.request_id === 'string' ? envelope!.request_id : '';
    if (!res.ok) {
      throw new TikTokShopError({
        // R13a: a body with no integer code, or code 0, still failed, so the HTTP status is the code.
        code: code || res.status,
        message: message || res.statusText || `HTTP ${res.status}`,
        requestId,
        httpStatus: res.status,
      });
    }
    // Lesson 34: a `code` that is present but not an integer makes the reply unreadable.
    if (rawCode !== undefined && code === undefined) {
      throw new TikTokShopError({
        code: -1,
        message: `Response has a non-integer code (HTTP ${res.status})`,
        requestId,
        httpStatus: res.status,
      });
    }
    if (code !== undefined && code !== 0) {
      throw new TikTokShopError({ code, message: message ?? '', requestId, httpStatus: res.status });
    }
  }

  private async errorHook(ctx: g.ErrorContext): Promise<Response | void> {
    // R13c: no HTTP response at all (connection refused, DNS, TLS, timeout): -1, no httpStatus.
    const e = ctx.error;
    const timedOut = e instanceof Error && (e.name === 'TimeoutError' || e.name === 'AbortError');
    throw new TikTokShopError({
      code: -1,
      message: `${timedOut ? 'Request timed out or was aborted' : 'Request failed'}: ${e instanceof Error ? e.message : String(e)}`,
      requestId: '',
      cause: e,
    });
  }
}
