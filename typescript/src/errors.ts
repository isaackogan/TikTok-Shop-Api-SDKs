export interface TikTokShopErrorInit {
  code: number;
  message: string;
  requestId: string;
  httpStatus?: number;
  cause?: unknown;
}

/** Raised for an envelope with `code != 0`, and for non-2xx statuses (with `httpStatus`). */
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
