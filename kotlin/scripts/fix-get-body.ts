// Fix-up (R18): the generated ApiClient builds a GET without its body (`RequestMethod.GET -> Request.Builder().url(url)`), and
// OkHttp cannot send one anyway. Carry the serialized body as a tag; the hand-written SigningInterceptor sends it.
export const GET_LINE = 'RequestMethod.GET -> Request.Builder().url(url)';
export const GET_FIXUP =
  'RequestMethod.GET -> Request.Builder().url(url).apply { if (requestConfig.body != null) tag(RequestBody::class.java, requestBody(requestConfig.body, contentType)) } // fix-up: scripts/generate.ts (GET with a body)';

/** Replace the stock GET line, which must occur exactly once and be the whole line (nothing may follow it). */
export function fixGetBody(src: string): string {
  const mentions = src.split(GET_LINE).length - 1;
  const whole = [...src.matchAll(/^([ \t]*)RequestMethod\.GET -> Request\.Builder\(\)\.url\(url\)[ \t]*$/gm)];
  if (mentions !== 1 || whole.length !== 1) {
    throw new Error(
      `generate: expected exactly one whole-line "${GET_LINE}" in ApiClient.kt, found ${mentions} occurrence(s), ${whole.length} whole-line`,
    );
  }
  return src.replace(/^([ \t]*)RequestMethod\.GET -> Request\.Builder\(\)\.url\(url\)[ \t]*$/m, (_m, indent) => indent + GET_FIXUP);
}
