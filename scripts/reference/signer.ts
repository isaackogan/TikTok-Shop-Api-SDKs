import { createHmac } from 'node:crypto';

export interface SignRequest {
  path: string;
  query: [string, string][]; // decoded values
  contentType: string | null;
  body: Uint8Array | null;
  appSecret: string;
}

const EXCLUDED = new Set(['sign', 'access_token']);

function isMultipart(contentType: string | null): boolean {
  if (!contentType) return false;
  return contentType.split(';')[0].trim().toLowerCase() === 'multipart/form-data';
}

export function stringToSign(req: SignRequest): string {
  const params = req.query
    .filter(([k]) => !EXCLUDED.has(k))
    .sort(([a], [b]) => (a < b ? -1 : a > b ? 1 : 0));
  let s = req.path + params.map(([k, v]) => k + v).join('');
  if (req.body && req.body.length > 0 && !isMultipart(req.contentType)) {
    s += Buffer.from(req.body).toString('utf8');
  }
  return req.appSecret + s + req.appSecret;
}

export function sign(req: SignRequest): string {
  return createHmac('sha256', req.appSecret).update(stringToSign(req), 'utf8').digest('hex');
}
