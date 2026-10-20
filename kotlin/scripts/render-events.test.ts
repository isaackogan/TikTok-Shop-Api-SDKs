import assert from 'node:assert/strict';
import { mkdirSync, mkdtempSync, readFileSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { test } from 'node:test';
import { readModels, renderEvents } from './render-events.ts';

const model = `data class FooWebhook (

    /* a */
    @SerializedName("type")
    val type: FooWebhook.Type,

    /* b */
    @SerializedName("old")
    @Deprecated(message = "This property is deprecated.")
    val old: kotlin.String? = null,

    @SerializedName("data")
    val \`data\`: FooWebhookData

) {
    enum class Type(val value: kotlin.Int) {
        @SerializedName(value = "7") _7(7);
    }
}
`;
const data = `data class FooWebhookData (

    @SerializedName("items")
    val items: kotlin.collections.List<FooWebhookData>? = null,

    @SerializedName("count")
    val count: kotlin.Long = 0

)
`;

function fixture() {
  const dir = mkdtempSync(join(tmpdir(), 'render-events-'));
  mkdirSync(join(dir, 'models'));
  writeFileSync(join(dir, 'models/FooWebhook.kt'), model);
  writeFileSync(join(dir, 'models/FooWebhookData.kt'), data);
  const meta = join(dir, 'meta.json');
  writeFileSync(meta, JSON.stringify({ webhooks: [{ type: 7, schema: 'FooWebhook', eventType: 'FOO' }] }));
  return { dir, meta };
}

test('readModels finds required properties, skipping defaults, nullables and extra annotations', () => {
  const { dir } = fixture();
  const m = readModels(join(dir, 'models'));
  assert.deepEqual(m.get('FooWebhook')!.filter((p) => p.required).map((p) => [p.kotlin, p.json]), [['type', 'type'], ['data', 'data']]);
  assert.deepEqual(m.get('FooWebhookData')!.filter((p) => p.required), []);
});

test('renderEvents writes a sealed subclass per webhook and the required-property table', () => {
  const { dir, meta } = fixture();
  renderEvents(meta, dir);
  const ev = readFileSync(join(dir, 'WebhookEvent.kt'), 'utf8');
  assert.match(ev, /^package com\.isaackogan\.tiktok\.shop$/m);
  assert.match(ev, /sealed class WebhookEvent/);
  assert.match(ev, /class Foo\(\s*[^)]*override val payload: FooWebhook,/);
  assert.match(ev, /const val TYPE: Int = 7/);
  assert.match(ev, /7 -> WebhookEvent\.Foo\(gson\.fromJson\(raw, FooWebhook::class\.java\), raw\)/);
  const req = readFileSync(join(dir, 'WebhookRequired.kt'), 'utf8');
  assert.match(req, /"FooWebhook" to Model\(listOf\("type", "data"\), mapOf\("data" to Child\("FooWebhookData", Kind\.OBJECT\)\)\)/);
  assert.match(req, /"FooWebhookData" to Model\(listOf\(\), mapOf\("items" to Child\("FooWebhookData", Kind\.LIST\)\)\)/);
});

test('a webhook schema without a model is an error', () => {
  const { dir, meta } = fixture();
  writeFileSync(meta, JSON.stringify({ webhooks: [{ type: 8, schema: 'BarWebhook' }] }));
  assert.throws(() => renderEvents(meta, dir), /no generated model/);
});
