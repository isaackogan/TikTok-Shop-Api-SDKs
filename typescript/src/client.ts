import * as g from './generated/index.ts';
import { TikTokShopError } from './errors.ts';
import { requiresShopCipher, sign } from './signing.ts';

export const DEFAULT_BASE_URL = 'https://open-api.tiktokglobalshop.com';

export interface TikTokShopOptions {
  appKey: string;
  appSecret: string;
  accessToken?: string;
  shopCipher?: string;
  baseUrl?: string;
  /** Per-request timeout in milliseconds. */
  timeoutMs?: number;
  /** HTTP client override (defaults to the global `fetch`). */
  fetch?: typeof fetch;
}

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

  private readonly options: TikTokShopOptions;

  constructor(options: TikTokShopOptions) {
    this.options = options;
    const cfg = new g.Configuration({
      basePath: (options.baseUrl ?? DEFAULT_BASE_URL).replace(/\/+$/, ''),
      middleware: [{ pre: (ctx) => this.requestHook(ctx), post: (ctx) => this.responseHook(ctx) }],
      fetchApi: this.buildFetch(),
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
    return new TikTokShop({ ...this.options, ...shop });
  }

  private buildFetch(): typeof fetch {
    const base = this.options.fetch ?? ((...a: Parameters<typeof fetch>) => fetch(...a));
    const ms = this.options.timeoutMs;
    if (!ms) return base;
    return (input, init) => base(input, { ...init, signal: init?.signal ?? AbortSignal.timeout(ms) });
  }

  private async requestHook(ctx: g.RequestContext): Promise<g.FetchParams> {
    const o = this.options;
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
    // 3. TODO(Task 7): location-precise rewrite of integer ID fields in the JSON body goes here.
    // 4. access token
    if (o.accessToken) headers.set('x-tts-access-token', o.accessToken);
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
    let envelope: { code?: unknown; message?: unknown; request_id?: unknown } | undefined;
    try {
      envelope = JSON.parse(await res.clone().text());
    } catch {
      envelope = undefined;
    }
    const isObj = envelope !== null && typeof envelope === 'object';
    const code = isObj && typeof envelope!.code === 'number' ? envelope!.code : undefined;
    const message = isObj && typeof envelope!.message === 'string' ? envelope!.message : undefined;
    const requestId = isObj && typeof envelope!.request_id === 'string' ? envelope!.request_id : '';
    if (!res.ok) {
      throw new TikTokShopError({
        code: code ?? res.status,
        message: message ?? res.statusText ?? `HTTP ${res.status}`,
        requestId,
        httpStatus: res.status,
      });
    }
    if (code !== undefined && code !== 0) {
      throw new TikTokShopError({ code, message: message ?? '', requestId });
    }
  }
}
