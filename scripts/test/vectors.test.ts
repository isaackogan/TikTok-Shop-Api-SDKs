import { describe, expect, it } from 'vitest';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { stringToSign, sign } from '../reference/signer.ts';
import { verifyWebhook } from '../reference/webhook.ts';
import { buildVectors } from '../build-vectors.ts';

const dir = fileURLToPath(new URL('../../shared/test-vectors/', import.meta.url));
const read = (n: string) => readFileSync(dir + n, 'utf8');
const signing = () => JSON.parse(read('signing.json')).cases as any[];
const req = (c: any) => ({
  path: c.path,
  query: c.query as [string, string][],
  contentType: c.contentType as string | null,
  body: c.body === null ? null : Buffer.from(c.body, 'utf8'),
  appSecret: c.secret as string,
});

describe('reference signer', () => {
  it('reproduces the docs worked example', () => {
    const c = signing().find((x) => x.name === 'docs-worked-example');
    const r = {
      path: '/authorization/202309/shops',
      query: [['app_key', '123456'], ['timestamp', '1234567890']] as [string, string][],
      contentType: null,
      body: null,
      appSecret: 'abc000def111',
    };
    expect(stringToSign(r)).toBe(
      'abc000def111/authorization/202309/shopsapp_key123456timestamp1234567890abc000def111',
    );
    expect(sign(r)).toBe('c8767e4fd7a1b48a0ce3fd23197f058159ce11b53f1ae1ad6d1ec931a1da5540');
    expect(c.sign).toBe(sign(r));
  });
  it('excludes sign and access_token', () => {
    const s = stringToSign(req(signing().find((x) => x.name === 'excluded-params')));
    expect(s).not.toContain('sign');
    expect(s).not.toContain('access_token');
    expect(s).not.toContain('TTP_x');
  });
  it('excludes a multipart body', () => {
    const c = signing().find((x) => x.name === 'multipart-body-excluded');
    expect(c.body).not.toBeNull();
    expect(stringToSign(req(c))).not.toContain(c.body);
  });
  it('every committed case matches the reference', () => {
    for (const c of signing()) {
      expect(stringToSign(req(c)), c.name).toBe(c.stringToSign);
      expect(sign(req(c)), c.name).toBe(c.sign);
    }
  });
});

describe('reference webhook verifier', () => {
  it('gives the docs published signature', () => {
    const v = JSON.parse(read('webhooks.json')).verify.find((x: any) => x.name === 'docs-reproducible-example');
    expect(v.signature).toBe('5dec0f11ec2f6783b8deee53c9ffbf8d024302f7c7e7fa55a35d17629031ac05');
    expect(verifyWebhook(v)).toBe(true);
  });
  it('every committed verify case matches', () => {
    for (const v of JSON.parse(read('webhooks.json')).verify) expect(verifyWebhook(v), v.name).toBe(v.valid);
  });
});

describe('committed vectors', () => {
  it('equal what build-vectors produces now', () => {
    const built = buildVectors();
    for (const name of ['signing.json', 'webhooks.json', 'auth.json']) {
      expect(read(name), name).toBe(built[name]);
    }
  });
});
