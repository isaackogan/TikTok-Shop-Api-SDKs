import { readFileSync } from 'node:fs';
import { describe, expect, it } from 'vitest';
import { operationFor, requiresShopCipher, sign, stringToSign } from '../src/signing.ts';

const vectors = JSON.parse(
  readFileSync(new URL('../../shared/test-vectors/signing.json', import.meta.url), 'utf8'),
).cases as Array<{
  name: string;
  secret: string;
  method: string;
  path: string;
  query: [string, string][];
  contentType: string | null;
  body: string | null;
  stringToSign: string;
  sign: string;
}>;

describe('signer', () => {
  it('has the 6 shared cases', () => expect(vectors).toHaveLength(6));
  for (const c of vectors) {
    const req = {
      path: c.path,
      query: c.query,
      contentType: c.contentType,
      body: c.body === null ? null : new TextEncoder().encode(c.body),
      appSecret: c.secret,
    };
    it(`${c.name}: stringToSign`, () => expect(stringToSign(req)).toBe(c.stringToSign));
    it(`${c.name}: sign`, () => expect(sign(req)).toBe(c.sign));
  }
});

describe('requiresShopCipher', () => {
  it('POST search needs it', () => expect(requiresShopCipher('POST', '/order/202309/orders/search')).toBe(true));
  it('method is case-insensitive', () => expect(requiresShopCipher('post', '/order/202309/orders/search')).toBe(true));
  it('authorized shops does not', () => expect(requiresShopCipher('GET', '/authorization/202309/shops')).toBe(false));
  it('{x} matches one segment', () =>
    expect(requiresShopCipher('GET', '/product/202309/products/1729507467923261408')).toBe(true));
  it('{x} does not match several segments', () =>
    expect(requiresShopCipher('GET', '/product/202309/products/1/2')).toBe(false));
  it('unknown path is false', () => expect(requiresShopCipher('GET', '/nope')).toBe(false));
});

describe('operationFor', () => {
  const id = (method: string, path: string) => operationFor(method, path)?.operationId;
  it('matches method and path template', () => {
    expect(id('POST', '/product/202604/appeals/submit')).toBe('submitSizeChartAppeal');
    expect(id('get', '/product/202604/opportunities/o-1')).toBe('getOpportunityDetail');
    expect(id('DELETE', '/product/202604/appeals/submit')).toBeUndefined();
    expect(id('GET', '/nope')).toBeUndefined();
  });
  it('prefers a literal segment over a {param} when both match', () => {
    expect(id('GET', '/product/202604/opportunities/submissions')).toBe('getSubmissionRecords');
    expect(id('GET', '/product/202606/skpps/sum')).toBe('getShopSKPPSummary');
  });
});
