import { createHmac } from 'node:crypto';

export interface VerifyInput {
  appKey: string;
  appSecret: string;
  rawBody: string;
  signature: string;
}

export function webhookSignature(appKey: string, appSecret: string, rawBody: string): string {
  return createHmac('sha256', appSecret).update(appKey + rawBody, 'utf8').digest('hex');
}

/** Exact comparison: an uppercased signature is invalid. */
export function verifyWebhook(v: VerifyInput): boolean {
  return v.signature === webhookSignature(v.appKey, v.appSecret, v.rawBody);
}
