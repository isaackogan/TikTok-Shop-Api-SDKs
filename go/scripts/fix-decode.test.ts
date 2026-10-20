import assert from 'node:assert/strict';
import { test } from 'node:test';
import { fixDecodeErrors } from './fix-decode.ts';

const CALL = '\terr = a.client.decode(&localVarReturnValue, localVarBody, localVarHTTPResponse.Header.Get("Content-Type"))\n';
const STOCK = CALL + '\tif err != nil {\n\t\tnewErr := &GenericOpenAPIError{\n\t\t\tbody:  localVarBody,\n\t\t\terror: err.Error(),\n\t\t}\n\t\treturn localVarReturnValue, localVarHTTPResponse, newErr\n\t}\n';
const op = (block: string) => `func (a *X) Op() {\n${block}\treturn localVarReturnValue, localVarHTTPResponse, nil\n}\n`;

test('replaces every post-decode error block with the DecodeError hook', () => {
  const out = fixDecodeErrors(op(STOCK) + op(STOCK), 'api_x.go');
  assert.equal(out.split('DecodeError(localVarHTTPResponse, localVarBody, err)').length - 1, 2);
  assert.ok(!out.includes('newErr := &GenericOpenAPIError'));
});

test('throws when a file has no decode call', () => {
  assert.throws(() => fixDecodeErrors('package generated\n', 'api_x.go'), /api_x\.go: decode fix-up/);
});

test('throws when a decode call is not followed by the stock block', () => {
  const drifted = CALL + '\tif err != nil {\n\t\treturn nil, nil, err\n\t}\n';
  assert.throws(() => fixDecodeErrors(op(STOCK) + op(drifted), 'api_x.go'), /every one of 2 decode call\(s\).*found 1/);
});
