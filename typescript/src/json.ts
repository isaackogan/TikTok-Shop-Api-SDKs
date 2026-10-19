/**
 * Lossless JSON for 64-bit IDs (design §6.6). Needs `JSON.parse` source text access and
 * `JSON.rawJSON`, both in Node 22+.
 */

interface ParseContext {
  source?: string;
}
interface JsonWithSource {
  parse(text: string, reviver: (this: unknown, key: string, value: unknown, context?: ParseContext) => unknown): unknown;
  rawJSON(text: string): object;
  isRawJSON(value: unknown): boolean;
}
const J = JSON as unknown as JsonWithSource;

const INTEGER = /^-?\d+$/;
/** An ID that can be written as a JSON number: digits only, no leading zero. */
const ID_NUMBER = /^(?:0|[1-9]\d*)$/;

const isObject = (v: unknown): v is Record<string, unknown> =>
  typeof v === 'object' && v !== null && !Array.isArray(v) && !J.isRawJSON(v);

const idStrings = (v: unknown): unknown =>
  Array.isArray(v) ? v.map(idStrings) : typeof v === 'number' ? String(v) : v;

/**
 * `JSON.parse`, except that any integer beyond 2^53 becomes an exact string, and any number under
 * an `idFields` key (or in an array under one) becomes a string, so values match their string types.
 */
export function parseJsonExact(text: string, idFields: readonly string[]): unknown {
  const ids = new Set(idFields);
  return J.parse(text, function (key, value, context) {
    const isId = ids.has(key) && !Array.isArray(this);
    if (typeof value === 'number') {
      const src = context?.source;
      if (src !== undefined && (isId || (INTEGER.test(src) && !Number.isSafeInteger(value)))) return src;
      return value;
    }
    // Array elements were revived first: big ones are exact strings already, the rest are safe numbers.
    return isId && Array.isArray(value) ? idStrings(value) : value;
  });
}

type Step = string | typeof EACH;
const EACH = Symbol('each');

/** `products[].product_id` → ['products', EACH, 'product_id']; `[].shop_id` → [EACH, 'shop_id']. */
function steps(path: string): Step[] {
  const out: Step[] = [];
  for (const segment of path.split('.')) {
    const m = /^(.*?)((?:\[\])*)$/.exec(segment)!;
    if (m[1] !== '') out.push(m[1]);
    for (let i = 0; i < m[2].length / 2; i++) out.push(EACH);
  }
  return out;
}

/** Copy-on-write: returns `node` itself when nothing under it changed. */
function apply(node: unknown, path: Step[], i: number): unknown {
  if (i === path.length) return typeof node === 'string' && ID_NUMBER.test(node) ? J.rawJSON(node) : node;
  const step = path[i];
  if (step === EACH) {
    if (!Array.isArray(node)) return node;
    let out: unknown[] = node;
    node.forEach((x, j) => {
      const y = apply(x, path, i + 1);
      if (y === x) return;
      if (out === node) out = node.slice();
      out[j] = y;
    });
    return out;
  }
  if (!isObject(node) || !Object.hasOwn(node, step)) return node;
  const x = node[step];
  const y = apply(x, path, i + 1);
  return y === x ? node : { ...node, [step]: y };
}

function withIdNumbers(value: unknown, paths: readonly string[]): unknown {
  return paths.reduce((v, p) => apply(v, steps(p), 0), value);
}

/**
 * `JSON.stringify`, writing each all-digit string found at one of `paths` as a bare JSON number.
 * Paths are dot-separated property names with `[]` after a name whose array items are walked,
 * e.g. `product_id`, `products[].product_id`, `ids[]`. Nothing else changes, whatever its name.
 */
export function stringifyWithIdNumbers(value: unknown, paths: readonly string[]): string {
  return JSON.stringify(withIdNumbers(value, paths));
}

/**
 * Rewrites the JSON text `text` as {@link stringifyWithIdNumbers} does. Other numbers keep their
 * exact source text. Returns `text` itself when nothing is rewritten or it is not valid JSON.
 */
export function rewriteIdNumbers(text: string, paths: readonly string[]): string {
  let value: unknown;
  try {
    value = J.parse(text, (_key, v, context) =>
      typeof v === 'number' && context?.source !== undefined ? J.rawJSON(context.source) : v,
    );
  } catch {
    return text;
  }
  const out = withIdNumbers(value, paths);
  return out === value ? text : JSON.stringify(out);
}
