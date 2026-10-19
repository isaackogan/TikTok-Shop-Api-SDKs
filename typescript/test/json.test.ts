import { describe, expect, it } from 'vitest';
import { parseJsonExact, rewriteIdNumbers, stringifyWithIdNumbers } from '../src/json.ts';

describe('parseJsonExact', () => {
  it('turns an ID field into an exact string and leaves other numbers alone', () => {
    expect(parseJsonExact('{"shop_id":7494049642642441621,"count":3}', ['shop_id'])).toEqual({
      shop_id: '7494049642642441621',
      count: 3,
    });
  });

  it('turns every element of an ID array into a string', () => {
    expect(parseJsonExact('{"product_ids":[1,7494049642642441621]}', ['product_ids'])).toEqual({
      product_ids: ['1', '7494049642642441621'],
    });
  });

  it('turns a small ID into a string, so values match their string types', () => {
    expect(parseJsonExact('{"id":42}', ['id'])).toEqual({ id: '42' });
  });

  it('keeps any integer beyond 2^53 exact as a string, ID field or not', () => {
    expect(parseJsonExact('{"total":9007199254740993}', [])).toEqual({ total: '9007199254740993' });
    expect(parseJsonExact('{"neg":-9007199254740993}', [])).toEqual({ neg: '-9007199254740993' });
    expect(parseJsonExact('[9007199254740993]', [])).toEqual(['9007199254740993']);
  });

  it('applies at any depth and leaves strings, nulls, floats and safe integers as they are', () => {
    const text = '{"data":{"products":[{"product_id":1729507467923261408,"price":1.5,"stock":9007199254740991,"sku_id":null,"shop_id":"7"}]}}';
    expect(parseJsonExact(text, ['product_id', 'sku_id', 'shop_id'])).toEqual({
      data: { products: [{ product_id: '1729507467923261408', price: 1.5, stock: 9007199254740991, sku_id: null, shop_id: '7' }] },
    });
  });

  it('throws on invalid JSON like JSON.parse', () => {
    expect(() => parseJsonExact('{', [])).toThrow(SyntaxError);
  });
});

describe('stringifyWithIdNumbers', () => {
  it('writes an all-digit string at a path as a bare JSON number', () => {
    expect(stringifyWithIdNumbers({ shop_id: '7494049642642441621', name: '1' }, ['shop_id'])).toBe(
      '{"shop_id":7494049642642441621,"name":"1"}',
    );
  });

  it('is location-precise: the same or an ID-like name elsewhere stays a string', () => {
    const value = { product_id: '7494049642642441621', id: '1729507467923261408', other: { product_id: '2' } };
    expect(stringifyWithIdNumbers(value, ['product_id'])).toBe(
      '{"product_id":7494049642642441621,"id":"1729507467923261408","other":{"product_id":"2"}}',
    );
  });

  it('walks arrays marked with []', () => {
    const value = { products: [{ product_id: '11', n: '1' }, { product_id: '12' }], ids: ['1', '2'], grid: [['3'], ['4']] };
    expect(stringifyWithIdNumbers(value, ['products[].product_id', 'ids[]', 'grid[][]'])).toBe(
      '{"products":[{"product_id":11,"n":"1"},{"product_id":12}],"ids":[1,2],"grid":[[3],[4]]}',
    );
    expect(stringifyWithIdNumbers([{ shop_id: '5' }, { shop_id: '6' }], ['[].shop_id'])).toBe('[{"shop_id":5},{"shop_id":6}]');
  });

  it('leaves values that are not plain all-digit strings, and missing or mismatched paths, alone', () => {
    const value = { a: 'x1', b: '0123', c: '', d: '-1', e: 5, f: null, g: '0', h: { x: '1' }, i: '1' };
    expect(stringifyWithIdNumbers(value, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i[]', 'missing', 'h.x.y', 'a[]'])).toBe(
      '{"a":"x1","b":"0123","c":"","d":"-1","e":5,"f":null,"g":0,"h":{"x":"1"},"i":"1"}',
    );
  });

  it('does not change the input value', () => {
    const value = { products: [{ product_id: '11' }] };
    stringifyWithIdNumbers(value, ['products[].product_id']);
    expect(value).toEqual({ products: [{ product_id: '11' }] });
  });
});

describe('rewriteIdNumbers', () => {
  it('rewrites the paths of a JSON text', () => {
    expect(rewriteIdNumbers('{"product_id":"7494049642642441621","size_chart_id":"7"}', ['product_id'])).toBe(
      '{"product_id":7494049642642441621,"size_chart_id":"7"}',
    );
  });

  it('keeps other numbers byte-exact, including ones beyond 2^53', () => {
    expect(rewriteIdNumbers('{"product_id":"1","big":9007199254740993,"f":1.50}', ['product_id'])).toBe(
      '{"product_id":1,"big":9007199254740993,"f":1.50}',
    );
  });

  it('returns the text unchanged when nothing is rewritten or it is not JSON', () => {
    const text = '{ "product_id" : "abc" }';
    expect(rewriteIdNumbers(text, ['product_id'])).toBe(text);
    expect(rewriteIdNumbers('not json', ['product_id'])).toBe('not json');
  });
});
