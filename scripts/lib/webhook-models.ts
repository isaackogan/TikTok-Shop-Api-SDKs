// The required-field table behind strict webhook parsing (R28), shared by the languages whose generated models do not
// check required fields themselves (TypeScript, Go, PHP).

export interface SchemaNode {
  $ref?: string;
  type?: unknown;
  properties?: Record<string, SchemaNode>;
  required?: string[];
  items?: SchemaNode;
  additionalProperties?: SchemaNode | boolean;
  allOf?: SchemaNode[];
  anyOf?: SchemaNode[];
  oneOf?: SchemaNode[];
}
interface Webhook {
  type: number;
  schema: string;
}
export type ChildKind = 'object' | 'list' | 'map';
export interface WebhookModel {
  required: string[];
  children: Record<string, [ChildKind, string]>;
}

const refName = (p: SchemaNode | boolean | undefined): string | undefined =>
  typeof p === 'object' && p !== null && typeof p.$ref === 'string' ? p.$ref.split('/').pop() : undefined;
/** `anyOf`/`oneOf` of exactly a `$ref` and `{type: 'null'}`: a nullable model. */
const nullableRef = (p: SchemaNode | undefined): string | undefined => {
  const alts = p?.anyOf ?? p?.oneOf;
  if (!Array.isArray(alts) || alts.length !== 2) return undefined;
  const ref = alts.map(refName).filter(Boolean);
  const isNull = alts.some((a) => a.type === 'null' && Object.keys(a).length === 1);
  return ref.length === 1 && isNull ? ref[0] : undefined;
};
/** True when a schema could hold a model somewhere this table cannot point at. */
const holdsModels = (p: SchemaNode | boolean | undefined): boolean =>
  typeof p === 'object' && p !== null &&
  (p.properties !== undefined || p.$ref !== undefined || p.allOf !== undefined || p.anyOf !== undefined ||
    p.oneOf !== undefined || p.items !== undefined || (typeof p.additionalProperties === 'object'));

/** The model a property holds directly, as a list, or as a string-keyed map. Throws on any other shape that could hold one. */
function childOf(p: SchemaNode, where: string): [ChildKind, string] | undefined {
  const direct = refName(p) ?? nullableRef(p);
  if (direct) return ['object', direct];
  const unhandled = () => new Error(`${where}: a webhook property shape the required-field check does not handle`);
  if (p.items !== undefined) {
    const item = refName(p.items) ?? nullableRef(p.items);
    if (item) return ['list', item];
    if (holdsModels(p.items)) throw unhandled(); // a list of lists, an inline object, a combinator
  }
  if (typeof p.additionalProperties === 'object') {
    const value = refName(p.additionalProperties) ?? nullableRef(p.additionalProperties);
    if (value) return ['map', value];
    if (holdsModels(p.additionalProperties)) throw unhandled();
  }
  if (p.properties !== undefined || p.allOf !== undefined || p.anyOf !== undefined || p.oneOf !== undefined) throw unhandled();
  return undefined;
}

/**
 * Every model reachable from a webhook: its required JSON property names, and which properties hold other such models.
 * Each SDK's webhook parser checks presence (and non-null) with this table. Throws on a property
 * shape it cannot follow, and when a webhook model has a `raw` property (TypeScript tells an unknown event apart by `'raw' in`).
 */
export function webhookModels(schemas: Record<string, SchemaNode>, webhooks: readonly Webhook[]): Record<string, WebhookModel> {
  const out: Record<string, WebhookModel> = {};
  const walk = (name: string): void => {
    if (name in out) return;
    const schema = schemas[name];
    if (!schema) throw new Error(`schema ${name} not found`);
    const model: WebhookModel = { required: [...(schema.required ?? [])], children: {} };
    out[name] = model;
    for (const [prop, p] of Object.entries(schema.properties ?? {})) {
      const child = childOf(p, `${name}.${prop}`);
      if (child) {
        model.children[prop] = child;
        walk(child[1]);
      }
    }
  };
  for (const w of webhooks) {
    const props = Object.keys(schemas[w.schema]?.properties ?? {});
    const raw = props.find((k) => k.replace(/_/g, '').toLowerCase() === 'raw');
    if (raw !== undefined) throw new Error(`webhook ${w.schema} has a "${raw}" property, which isUnknownWebhookEvent relies on being absent`);
    walk(w.schema);
  }
  return Object.fromEntries(Object.entries(out).sort(([a], [b]) => (a < b ? -1 : a > b ? 1 : 0)));
}
