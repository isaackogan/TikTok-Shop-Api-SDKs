// Fix-up (R13d): the generated ApiClient.responseBody decodes a 2xx body with gson, which throws its own exceptions
// (JsonSyntaxException, IllegalStateException, ...) for a body that does not fit the model. Wrap that one call so the failure
// is a TikTokShopException with code -1, the HTTP status, the request ID and the gson exception as cause.
export const DECODE_LINE = 'Serializer.gson.fromJson(bodyContent, (object: TypeToken<T>(){}).getType())';

/** Replace the stock decode line, which must occur exactly once and be the whole line. */
export function fixDecode(src: string): string {
  const mentions = src.split(DECODE_LINE).length - 1;
  const whole = /^([ \t]*)Serializer\.gson\.fromJson\(bodyContent, \(object: TypeToken<T>\(\)\{\}\)\.getType\(\)\)[ \t]*$/gm;
  const lines = [...src.matchAll(whole)];
  if (mentions !== 1 || lines.length !== 1) {
    throw new Error(`generate: expected exactly one whole-line "${DECODE_LINE}" in ApiClient.kt, found ${mentions} occurrence(s), ${lines.length} whole-line`);
  }
  return src.replace(whole, (_m, indent: string) =>
    [
      `${indent}try { // fix-up: scripts/fix-decode.ts (R13d)`,
      `${indent}    ${DECODE_LINE}`,
      `${indent}} catch (e: RuntimeException) {`,
      `${indent}    throw com.isaackogan.tiktok.shop.decodeFailure(response.code, bodyContent, e)`,
      `${indent}}`,
    ].join('\n'),
  );
}
