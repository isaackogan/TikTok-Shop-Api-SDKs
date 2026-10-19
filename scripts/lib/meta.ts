export type Lang = 'typescript' | 'python' | 'go' | 'java' | 'kotlin' | 'php' | 'rust' | 'csharp';
export const LANGS: readonly Lang[] = ['typescript', 'python', 'go', 'java', 'kotlin', 'php', 'rust', 'csharp'];

export interface OperationMeta {
  operationId: string;
  tag: string;
  group: string;
  method: string;
  path: string;
  requiresShopCipher: boolean;
}
export interface WebhookMeta {
  type: number;
  schema: string;
  eventType?: string;
}
export interface Meta {
  operations: OperationMeta[];
  webhooks: WebhookMeta[];
  idFields?: string[];
}

const METHODS = ['get', 'put', 'post', 'delete', 'options', 'head', 'patch', 'trace'];
const SHOP_CIPHER_REF = '#/components/parameters/ShopCipher';
const ID_DIGITS = 16;
// Values under these keys are data, never schema: do not rewrite them.
const DATA_KEYS = new Set(['example', 'examples', 'default', 'enum', 'const']);

type Json = any;
const isObj = (v: unknown): v is Record<string, Json> => typeof v === 'object' && v !== null && !Array.isArray(v);
const isRaw = (v: unknown): boolean => (JSON as any).isRawJSON(v);

/** Parse the spec keeping integers of 16+ digits exact (as JSON.rawJSON values). */
export function parseSpec(text: string): Json {
  return JSON.parse(text, function (_key: string, value: Json, context?: { source?: string }) {
    const src = context?.source;
    if (typeof value === 'number' && src && /^-?\d{16,}$/.test(src)) return (JSON as any).rawJSON(src);
    return value;
  });
}

/** Deep copy that preserves rawJSON values. */
function clone<T>(v: T): T {
  if (Array.isArray(v)) return v.map(clone) as T;
  if (isObj(v) && !isRaw(v)) return Object.fromEntries(Object.entries(v).map(([k, x]) => [k, clone(x)])) as T;
  return v;
}

export function groupName(tag: string, groups: Record<string, string>): string {
  if (groups[tag]) return groups[tag];
  const words = tag.replace(/\([^)]*\)/g, ' ').split(/[^A-Za-z0-9]+/).filter(Boolean);
  return words.map((w, i) => (i === 0 ? w[0].toLowerCase() : w[0].toUpperCase()) + w.slice(1)).join('');
}

function digitsOf(v: unknown): number {
  if (isRaw(v)) return String((v as any).rawJSON).replace('-', '').length;
  if (typeof v === 'number' && Number.isInteger(v)) return BigInt(Math.abs(v)).toString().length;
  return 0;
}

/** Names that have at least one example value of 16+ digits anywhere in the spec. */
function longExampleNames(spec: Json): Set<string> {
  const names = new Set<string>();
  const scan = (value: Json, name?: string): void => {
    if (Array.isArray(value)) return void value.forEach((x) => scan(x, name));
    if (isObj(value) && !isRaw(value)) return void Object.entries(value).forEach(([k, x]) => scan(x, k));
    if (name && digitsOf(value) >= ID_DIGITS) names.add(name);
  };
  const walk = (node: Json, name?: string): void => {
    if (Array.isArray(node)) return void node.forEach((x) => walk(x));
    if (!isObj(node) || isRaw(node)) return;
    for (const [k, v] of Object.entries(node)) {
      if (k === 'example') scan(v, typeof node.name === 'string' ? node.name : name);
      else if (k === 'properties' && isObj(v)) Object.entries(v).forEach(([p, s]) => walk(s, p));
      else if (k === 'items' || k === 'schema') walk(v, name);
      else if (!DATA_KEYS.has(k)) walk(v);
    }
  };
  walk(spec);
  return names;
}

const isIntegerType = (t: unknown): boolean => t === 'integer' || (Array.isArray(t) && t.includes('integer'));

/** Rewrites integer ID schemas to strings in place (on an already-cloned spec). */
function stringifyIds(spec: Json, isIdName: (n: string) => boolean): string[] {
  const converted = new Set<string>();
  const convert = (schema: Json, name: string): void => {
    const out: Json = { type: Array.isArray(schema.type) ? schema.type.map((t: string) => (t === 'integer' ? 'string' : t)) : 'string' };
    if (schema.description !== undefined) out.description = schema.description;
    if (schema.deprecated !== undefined) out.deprecated = schema.deprecated;
    for (const k of Object.keys(schema)) delete schema[k];
    Object.assign(schema, out);
    converted.add(name);
  };
  const walk = (node: Json, name?: string): void => {
    if (Array.isArray(node)) return void node.forEach((x) => walk(x, name));
    if (!isObj(node) || isRaw(node)) return;
    if (name && isIntegerType(node.type) && isIdName(name)) return convert(node, name);
    for (const [k, v] of Object.entries(node)) {
      if (DATA_KEYS.has(k)) continue;
      if (k === 'properties' && isObj(v)) Object.entries(v).forEach(([p, s]) => walk(s, p));
      else if (k === 'items' || k === 'allOf' || k === 'anyOf' || k === 'oneOf') walk(v, name);
      else if (k === 'parameters' && Array.isArray(v)) v.forEach((p) => isObj(p) && walk(p.schema, p.name));
      else walk(v);
    }
  };
  walk(spec);
  return [...converted].sort();
}

function removeShopCipher(spec: Json): void {
  const strip = (node: Json): void => {
    if (!Array.isArray(node.parameters)) return;
    node.parameters = node.parameters.filter((p: Json) => !(isObj(p) && p.$ref === SHOP_CIPHER_REF));
  };
  for (const item of Object.values<Json>(spec.paths ?? {})) {
    strip(item);
    for (const m of METHODS) if (isObj(item[m])) strip(item[m]);
  }
}

function operationsMeta(spec: Json, groups: Record<string, string>): OperationMeta[] {
  const ops: OperationMeta[] = [];
  for (const [path, item] of Object.entries<Json>(spec.paths ?? {})) {
    for (const method of METHODS) {
      const op = item[method];
      if (!isObj(op)) continue;
      const tag: string = op.tags[0];
      ops.push({
        operationId: op.operationId,
        tag,
        group: groupName(tag, groups),
        method,
        path,
        requiresShopCipher: op['x-tts-requires-shop-cipher'] === true,
      });
    }
  }
  return ops;
}

function webhooksMeta(spec: Json): WebhookMeta[] {
  return Object.values<Json>(spec.webhooks ?? {}).map((item) => {
    const post = item.post;
    const ref: string = post.requestBody.content['application/json'].schema.$ref;
    const hook: WebhookMeta = { type: post['x-tts-webhook-type'], schema: ref.split('/').pop()! };
    if (post['x-tts-event-type'] !== undefined) hook.eventType = post['x-tts-event-type'];
    return hook;
  });
}

export function prepareSpec(spec: object, lang: Lang, groups: Record<string, string>): { spec: Json; meta: Meta } {
  const out: Json = clone(spec);
  const meta: Meta = { operations: operationsMeta(out, groups), webhooks: webhooksMeta(out) };
  delete out.webhooks;
  removeShopCipher(out);
  if (lang === 'typescript') {
    const long = longExampleNames(out);
    meta.idFields = stringifyIds(out, (n) => n === 'id' || n.endsWith('_id') || n.endsWith('_ids') || long.has(n));
  }
  return { spec: out, meta };
}
