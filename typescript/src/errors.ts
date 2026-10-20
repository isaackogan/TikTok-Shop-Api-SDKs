export interface TikTokShopErrorInit {
  code: number;
  message: string;
  requestId: string;
  httpStatus?: number;
  cause?: unknown;
}

/**
 * Raised for every failed call. `code` is TikTok's non-zero `code` when the reply has one; for a non-2xx reply without
 * one it is the HTTP status (`httpStatus` is then always set); it is -1 only for a 2xx reply that cannot be understood
 * (not a JSON object, or `code` 0 without `data` on a token call); it is 0 for network errors and timeouts.
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
