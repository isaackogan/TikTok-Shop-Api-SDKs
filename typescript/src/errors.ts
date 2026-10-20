export interface TikTokShopErrorInit {
  code: number;
  message: string;
  requestId: string;
  httpStatus?: number;
  cause?: unknown;
}

/**
 * Raised for every failed call:
 * - an envelope with a non-zero `code`, even on HTTP 200: TikTok's `code`, with `httpStatus` set;
 * - a non-2xx reply: TikTok's non-zero `code` if the body has one, else the HTTP status; `httpStatus` is always set;
 * - a 2xx reply that cannot be understood: -1 with `httpStatus` set. That covers a body that is not a JSON object, a
 *   `code` that is not an integer, `code` 0 without `data` on a token call, and a body that does not fit its model;
 * - a transport failure with no HTTP response at all (connection refused, DNS, TLS, timeout): -1 with no `httpStatus`.
 *
 * The original error, if any, is the `cause`.
 */
export class TikTokShopError extends Error {
  override name = 'TikTokShopError';
  readonly code: number;
  readonly requestId: string;
  readonly httpStatus?: number;

  constructor(init: TikTokShopErrorInit) {
    super(init.message, init.cause === undefined ? undefined : { cause: init.cause });
    this.code = init.code;
    this.requestId = init.requestId;
    this.httpStatus = init.httpStatus;
  }
}

/**
 * R13d: a 2xx body that does not fit its generated model. Called by the generated `JSONApiResponse.value()` (an
 * asserted fix-up in scripts/generate.ts). Not exported from the package.
 */
export function decodeFailure(res: Response, json: unknown, cause: unknown): TikTokShopError {
  const env = json !== null && typeof json === 'object' && !Array.isArray(json) ? (json as Record<string, unknown>) : {};
  return new TikTokShopError({
    code: -1,
    message: `Response does not match its model (HTTP ${res.status}): ${cause instanceof Error ? cause.message : String(cause)}`,
    requestId: typeof env.request_id === 'string' ? env.request_id : '',
    httpStatus: res.status,
    cause,
  });
}
