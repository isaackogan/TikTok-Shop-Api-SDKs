import { createHmac, timingSafeEqual } from 'node:crypto';
import { parseJsonExact } from './json.ts';
import * as models from './generated/models/index.ts';
import { EVENT_TYPES as GENERATED_EVENT_TYPES, ID_FIELDS, WEBHOOK_MODELS, WEBHOOKS } from './generated/meta.ts';
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

/**
 * The body is not a webhook this SDK can read: not JSON, not a JSON object, no integer `type`, or a known `type` whose
 * required fields are missing or null, or whose model fields aren't JSON objects (R28). Only an integer `type` the SDK
 * does not know gives an {@link UnknownWebhookEvent}.
 */
export class WebhookParseError extends Error {
  override name = 'WebhookParseError';
  constructor(message: string, options?: { cause?: unknown }) {
    super(message, options);
  }
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

interface Hook {
  schema: string;
  fromJson: (json: any) => unknown;
  instanceOf: (value: object) => boolean;
}
const generated = models as unknown as Record<string, (j: any) => any>;
const hooks = new Map<number, Hook>(
  WEBHOOKS.map((w) => [
    w.type,
    { schema: w.schema, fromJson: generated[`${w.schema}FromJSON`]!, instanceOf: generated[`instanceOf${w.schema}`]! },
  ]),
);

const isPlainObject = (v: unknown): v is Record<string, unknown> => typeof v === 'object' && v !== null && !Array.isArray(v);

/** The first required property (dotted path) that is missing or null, checking nested models, lists and maps. */
function firstMissing(model: string, json: Record<string, unknown>, path: string): string | undefined {
  const entry = WEBHOOK_MODELS[model];
  if (!entry) return undefined;
  for (const name of entry.required) {
    if (json[name] === undefined || json[name] === null) return path + name;
  }
  for (const [name, [kind, child]] of Object.entries(entry.children)) {
    const value = json[name];
    if (kind === 'object') {
      const found = isPlainObject(value) ? firstMissing(child, value, `${path}${name}.`) : undefined;
      if (found) return found;
    } else if (kind === 'list' && Array.isArray(value)) {
      for (const [i, item] of value.entries()) {
        const found = isPlainObject(item) ? firstMissing(child, item, `${path}${name}[${i}].`) : undefined;
        if (found) return found;
      }
    } else if (kind === 'map' && isPlainObject(value)) {
      for (const [k, item] of Object.entries(value)) {
        const found = isPlainObject(item) ? firstMissing(child, item, `${path}${name}.${k}.`) : undefined;
        if (found) return found;
      }
    }
  }
  return undefined;
}

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

  /**
   * Parses a body to its typed model; an integer `type` this SDK does not know comes back as `{type, raw}`. 64-bit IDs
   * stay exact.
   *
   * Parsing is strict (R28): it throws {@link WebhookParseError} when the body is not a JSON object, its `type` is
   * missing or not an integer (a string, bool, null or float), or a known type lacks a required field, has it null, or
   * has a model field that isn't a JSON object, at any depth.
   */
  parse(rawBody: RawBody): WebhookEvent | UnknownWebhookEvent {
    let json: unknown;
    try {
      const text = typeof rawBody === 'string' ? rawBody : new TextDecoder('utf-8', { fatal: true }).decode(rawBody);
      json = parseJsonExact(text, ID_FIELDS);
    } catch (e) {
      throw new WebhookParseError(`Webhook body is not valid JSON: ${e instanceof Error ? e.message : String(e)}`, { cause: e });
    }
    if (!isPlainObject(json)) throw new WebhookParseError('Webhook body is not a JSON object');
    const type = json.type;
    if (typeof type !== 'number' || !Number.isSafeInteger(type)) throw new WebhookParseError('Webhook body has no integer "type"');
    const hook = hooks.get(type);
    if (!hook) return { type, raw: json };
    const missing = firstMissing(hook.schema, json, '');
    if (missing !== undefined) {
      throw new WebhookParseError(`Webhook type ${type} does not match ${hook.schema}: required field "${missing}" is missing or null`);
    }
    let event: unknown;
    try {
      event = hook.fromJson(json);
    } catch (e) {
      throw new WebhookParseError(`Webhook type ${type} does not match ${hook.schema}: ${e instanceof Error ? e.message : String(e)}`, { cause: e });
    }
    if (!isPlainObject(event) || !hook.instanceOf(event)) throw new WebhookParseError(`Webhook type ${type} does not match ${hook.schema}`);
    return event as unknown as WebhookEvent;
  },

  /** Verifies, then parses. Throws {@link WebhookSignatureError} on a mismatch. */
  verifyAndParse(opts: VerifyOptions): WebhookEvent | UnknownWebhookEvent {
    if (!Webhooks.verify(opts)) throw new WebhookSignatureError();
    return Webhooks.parse(opts.rawBody);
  },
  EVENT_TYPES,
};
