import { createHmac, timingSafeEqual } from 'node:crypto';
import { parseJsonExact } from './json.ts';
import * as models from './generated/models/index.ts';
import { EVENT_TYPES as GENERATED_EVENT_TYPES, ID_FIELDS, WEBHOOKS } from './generated/meta.ts';
import type { WebhookEvent as GeneratedWebhookEvent } from './generated/models/WebhookEvent.ts';

/** A typed webhook: one of the generated webhook models, discriminated by `type`. */
export type WebhookEvent = GeneratedWebhookEvent;

/**
 * A webhook whose `type` this SDK does not know. `raw` is the parsed body.
 * Known events never have a `raw` property, so `'raw' in event` (or {@link isUnknownWebhookEvent})
 * separates the two; after that, `event.type` narrows to a specific webhook model.
 */
export interface UnknownWebhookEvent {
  type: number;
  raw: unknown;
}

export function isUnknownWebhookEvent(event: WebhookEvent | UnknownWebhookEvent): event is UnknownWebhookEvent {
  return 'raw' in event;
}

export class WebhookSignatureError extends Error {
  override name = 'WebhookSignatureError';
  constructor(message = 'Webhook signature does not match') {
    super(message);
  }
}

/** Webhook type ID → event name, e.g. `1` → `ORDER_STATUS_CHANGE`. */
export const EVENT_TYPES: Record<number, string> = GENERATED_EVENT_TYPES;

export type RawBody = string | Uint8Array;

export interface VerifyOptions {
  appKey: string;
  appSecret: string;
  /** The body exactly as received. Never re-serialize it. */
  rawBody: RawBody;
  /** The `Authorization` header value. */
  signature: string;
}

const converters = new Map<number, (json: any) => unknown>(
  WEBHOOKS.map((w) => [w.type, (models as unknown as Record<string, (j: any) => unknown>)[`${w.schema}FromJSON`]!]),
);

const toBuffer = (b: RawBody) => (typeof b === 'string' ? Buffer.from(b, 'utf8') : Buffer.from(b.buffer, b.byteOffset, b.byteLength));

export const Webhooks = {
  /** HMAC-SHA256 (key `appSecret`) over `appKey + rawBody`, lowercase hex, compared in constant time. */
  verify({ appKey, appSecret, rawBody, signature }: VerifyOptions): boolean {
    if (!signature) return false;
    const expected = createHmac('sha256', appSecret).update(appKey, 'utf8').update(toBuffer(rawBody)).digest('hex');
    const a = Buffer.from(expected, 'utf8');
    const b = Buffer.from(signature, 'utf8');
    return a.length === b.length && timingSafeEqual(a, b);
  },

  /** Parses a body to its typed model; unknown types come back as `{type, raw}`. 64-bit IDs stay exact. */
  parse(rawBody: RawBody): WebhookEvent | UnknownWebhookEvent {
    const text = typeof rawBody === 'string' ? rawBody : new TextDecoder().decode(rawBody);
    const json = parseJsonExact(text, ID_FIELDS) as any;
    const convert = typeof json?.type === 'number' ? converters.get(json.type) : undefined;
    if (!convert) return { type: json?.type, raw: json };
    return convert(json) as WebhookEvent;
  },

  /** Verifies, then parses. Throws {@link WebhookSignatureError} on a mismatch. */
  verifyAndParse(opts: VerifyOptions): WebhookEvent | UnknownWebhookEvent {
    if (!Webhooks.verify(opts)) throw new WebhookSignatureError();
    return Webhooks.parse(opts.rawBody);
  },
  EVENT_TYPES,
};
