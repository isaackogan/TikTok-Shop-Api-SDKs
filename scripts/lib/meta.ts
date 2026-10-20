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
  /** Per operationId, the JSON request-body locations of converted IDs, e.g. `products[].product_id`. */
  idBodyPaths?: Record<string, string[]>;
}

const METHODS = ['get', 'put', 'post', 'delete', 'options', 'head', 'patch', 'trace'];
const SHOP_CIPHER_REF = '#/components/parameters/ShopCipher';
const SCHEMA_REF = '#/components/schemas/';
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

/**
 * Rewrites integer ID schemas to strings in place (on an already-cloned spec).
 * Returns the converted field names and the converted schema objects themselves.
 */
function stringifyIds(spec: Json, isIdName: (n: string) => boolean): { names: string[]; nodes: Set<Json> } {
  const converted = new Set<string>();
  const nodes = new Set<Json>();
  const convert = (schema: Json, name: string): void => {
    const out: Json = { type: Array.isArray(schema.type) ? schema.type.map((t: string) => (t === 'integer' ? 'string' : t)) : 'string' };
    if (schema.description !== undefined) out.description = schema.description;
    if (schema.deprecated !== undefined) out.deprecated = schema.deprecated;
    for (const k of Object.keys(schema)) delete schema[k];
    Object.assign(schema, out);
    converted.add(name);
    nodes.add(schema);
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
  return { names: [...converted].sort(), nodes };
}

/**
 * For each operation's `application/json` request body, the paths of the fields in `converted`:
 * dot-separated property names, with `[]` after a name whose array items are walked (`[]` alone
 * for a root array). Operations without such fields are omitted. Throws when a converted field is
 * reachable only where a path cannot point (a recursive schema, `additionalProperties`, ...).
 */
function idBodyPaths(spec: Json, converted: Set<Json>): Record<string, string[]> {
  const schemas: Json = spec.components?.schemas ?? {};
  const target = (ref: unknown): Json =>
    typeof ref === 'string' && ref.startsWith(SCHEMA_REF) ? schemas[ref.slice(SCHEMA_REF.length)] : undefined;
  const reaches = (node: Json, seen = new Set<Json>()): boolean => {
    if (Array.isArray(node)) return node.some((x) => reaches(x, seen));
    if (!isObj(node) || isRaw(node) || seen.has(node)) return false;
    seen.add(node);
    if (converted.has(node) || reaches(target(node.$ref), seen)) return true;
    return Object.entries(node).some(([k, v]) =>
      k === 'properties' ? isObj(v) && reaches(Object.values(v), seen) : !DATA_KEYS.has(k) && reaches(v, seen),
    );
  };
  const out: Record<string, string[]> = {};
  for (const item of Object.values<Json>(spec.paths ?? {})) {
    for (const method of METHODS) {
      const op = item[method];
      const root = isObj(op) ? op.requestBody?.content?.['application/json']?.schema : undefined;
      if (!isObj(root)) continue;
      const found = new Set<string>();
      const walk = (node: Json, path: string, stack: readonly Json[]): void => {
        if (!isObj(node) || isRaw(node)) return;
        if (converted.has(node)) return void found.add(path);
        for (const [k, v] of Object.entries(node)) {
          if (DATA_KEYS.has(k)) continue;
          const at = (where: string) => `${op.operationId}: an integer ID under ${where} has no body path`;
          if (k === '$ref') {
            const t = target(v);
            if (!stack.includes(t)) walk(t, path, [...stack, t]);
            else if (reaches(t)) throw new Error(at(`the recursive ${v} at "${path}"`));
          } else if (k === 'properties' && isObj(v)) {
            for (const [p, s] of Object.entries(v)) walk(s, path === '' ? p : `${path}.${p}`, stack);
          } else if (k === 'items' && isObj(v)) {
            walk(v, `${path}[]`, stack);
          } else if ((k === 'allOf' || k === 'anyOf' || k === 'oneOf') && Array.isArray(v)) {
            v.forEach((x) => walk(x, path, stack));
          } else if (reaches(v)) {
            throw new Error(at(`"${path}" ${k}`));
          }
        }
      };
      walk(root, '', []);
      if (found.size) out[op.operationId] = [...found].sort();
    }
  }
  return out;
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

export interface RelaxStats {
  /** String and integer enums turned into plain strings and integers. */
  stripped: number;
  /** Schemas reachable from a response or webhook payload. */
  reachable: number;
}

/** True when `t` is `kind`, or a type array of `kind` plus optionally "null". */
const isScalarType = (t: unknown, kind: string): boolean =>
  t === kind || (Array.isArray(t) && t.length > 0 && t.every((x) => x === kind || x === 'null') && t.includes(kind));

const escapeRegExp = (s: string): string => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

/** True when `value` occurs in `text` as a whole token: not glued to `[A-Za-z0-9_]` on either side. */
const mentionsWhole = (text: string, value: string): boolean =>
  new RegExp(`(?<![A-Za-z0-9_])${escapeRegExp(value)}(?![A-Za-z0-9_])`).test(text);

function appendValues(schema: Json, values: string[]): void {
  const desc: string | undefined = typeof schema.description === 'string' && schema.description !== '' ? schema.description : undefined;
  if (desc !== undefined && values.every((v) => mentionsWhole(desc, v))) return;
  const list = `Possible values: ${values.map((v) => `\`${v}\``).join(', ')}`;
  schema.description = desc === undefined ? list : `${desc}\n\n${list}`;
}

/**
 * R21: TikTok adds values to status-like fields over time, so every string enum a client or
 * webhook receiver can decode becomes a plain string (the values move into the description).
 * R21b: integer enums get the same treatment and become plain integers. The webhook `type` is a
 * `const`, not an enum, so it is untouched.
 * Request-only schemas and parameters keep their enums. Mutates `spec` (an already-cloned spec).
 */
export function relaxResponseEnums(spec: Json): RelaxStats {
  const seen = new Set<Json>();
  const stats: RelaxStats = { stripped: 0, reachable: 0 };
  const resolve = (ref: string): Json => {
    if (!ref.startsWith('#/')) return undefined;
    return ref.slice(2).split('/').reduce<Json>((n, seg) => n?.[seg.replace(/~1/g, '/').replace(/~0/g, '~')], spec);
  };
  const walk = (node: Json): void => {
    if (!isObj(node) || isRaw(node) || seen.has(node)) return;
    seen.add(node);
    stats.reachable++;
    if (Array.isArray(node.enum) && (isScalarType(node.type, 'string') || isScalarType(node.type, 'integer'))) {
      appendValues(node, node.enum.filter((v: unknown) => v !== null).map((v: unknown) => (isRaw(v) ? String((v as any).rawJSON) : String(v))));
      delete node.enum;
      delete node['x-enum-varnames'];
      delete node['x-enum-descriptions'];
      stats.stripped++;
    }
    if (typeof node.$ref === 'string') walk(resolve(node.$ref));
    if (isObj(node.properties)) Object.values(node.properties).forEach(walk);
    for (const k of ['items', 'additionalProperties', 'not']) walk(node[k]);
    for (const k of ['allOf', 'anyOf', 'oneOf', 'prefixItems']) if (Array.isArray(node[k])) node[k].forEach(walk);
  };
  const bodies = (content: Json): void => {
    if (!isObj(content)) return;
    for (const [type, media] of Object.entries<Json>(content)) {
      if (/json/i.test(type) && isObj(media)) walk(media.schema);
    }
  };
  const response = (r: Json): void => {
    const resolved = isObj(r) && typeof r.$ref === 'string' ? resolve(r.$ref) : r;
    if (isObj(resolved)) bodies(resolved.content);
  };
  for (const item of Object.values<Json>(spec.paths ?? {})) {
    for (const m of METHODS) {
      const responses = item[m]?.responses;
      if (!isObj(responses)) continue;
      for (const [code, r] of Object.entries(responses)) if (/^2/.test(code)) response(r);
    }
  }
  for (const item of Object.values<Json>(spec.webhooks ?? {})) {
    for (const m of METHODS) bodies(item[m]?.requestBody?.content);
  }
  return stats;
}

export function prepareSpec(spec: object, lang: Lang, groups: Record<string, string>): { spec: Json; meta: Meta } {
  const out: Json = clone(spec);
  const meta: Meta = { operations: operationsMeta(out, groups), webhooks: webhooksMeta(out) };
  relaxResponseEnums(out); // before the webhooks go: their payloads are decoded too
  delete out.webhooks;
  removeShopCipher(out);
  if (lang === 'typescript') {
    const long = longExampleNames(out);
    const ids = stringifyIds(out, (n) => n === 'id' || n.endsWith('_id') || n.endsWith('_ids') || long.has(n));
    meta.idFields = ids.names;
    meta.idBodyPaths = idBodyPaths(out, ids.nodes);
  }
  return { spec: out, meta };
}
