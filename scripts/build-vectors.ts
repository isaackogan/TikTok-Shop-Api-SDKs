import { writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { sign, stringToSign } from './reference/signer.ts';
import { webhookSignature } from './reference/webhook.ts';

type Query = [string, string][];
interface SignInput {
  name: string;
  secret: string;
  method: string;
  path: string;
  query: Query;
  contentType: string | null;
  body: string | null;
}

const SIGNING_INPUTS: SignInput[] = [
  {
    name: 'docs-worked-example',
    secret: 'abc000def111',
    method: 'GET',
    path: '/authorization/202309/shops',
    query: [['app_key', '123456'], ['timestamp', '1234567890']],
    contentType: null,
    body: null,
  },
  {
    name: 'json-body',
    secret: 'abc000def111',
    method: 'POST',
    path: '/product/202309/products',
    query: [
      ['app_key', '123456'],
      ['timestamp', '1234567890'],
      ['shop_cipher', 'GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3'],
    ],
    contentType: 'application/json',
    body: '{"title":"Café","price":"9.99"}',
  },
  {
    name: 'excluded-params',
    secret: 'abc000def111',
    method: 'GET',
    path: '/order/202309/orders',
    query: [
      ['timestamp', '1234567890'],
      ['sign', 'ffff'],
      ['access_token', 'TTP_x'],
      ['app_key', '123456'],
      ['page_size', '20'],
    ],
    contentType: null,
    body: null,
  },
  {
    name: 'multipart-body-excluded',
    secret: 'abc000def111',
    method: 'POST',
    path: '/product/202309/images/upload',
    query: [['app_key', '123456'], ['timestamp', '1234567890']],
    contentType: 'multipart/form-data; boundary=xyz',
    body: '--xyz\r\nContent-Disposition: form-data; name="data"; filename="a.png"\r\n\r\nPNGDATA\r\n--xyz--\r\n',
  },
  {
    name: 'decoded-page-token-and-array',
    secret: 'abc000def111',
    method: 'GET',
    path: '/product/202502/products/search',
    query: [
      ['page_token', 'b2Zmc2V0PTEw+/x=='],
      ['ids', '1,2,3'],
      ['app_key', '123456'],
      ['timestamp', '1234567890'],
    ],
    contentType: null,
    body: null,
  },
  {
    name: 'empty-json-body',
    secret: 'abc000def111',
    method: 'POST',
    path: '/seller/202309/shops',
    query: [['app_key', '123456'], ['timestamp', '1234567890']],
    contentType: 'application/json',
    body: '',
  },
];

function signingVectors() {
  return {
    cases: SIGNING_INPUTS.map((c) => {
      const req = {
        path: c.path,
        query: c.query,
        contentType: c.contentType,
        body: c.body === null ? null : Buffer.from(c.body, 'utf8'),
        appSecret: c.secret,
      };
      return { ...c, stringToSign: stringToSign(req), sign: sign(req) };
    }),
  };
}

const DOCS_BODY =
  '{"type":1,"tts_notification_id":"7380066284010030890","shop_id":"7495540735365777507","timestamp":1718305585,"data":{"is_on_hold_order":true,"order_id":"576653688135258178","order_status":"UNPAID","update_time":1718305585}}';

function webhookVectors() {
  const appKey = 'abcdef';
  const appSecret = '123';
  const good = webhookSignature(appKey, appSecret, DOCS_BODY);
  const v = (name: string, rawBody: string, signature: string, valid: boolean) => ({
    name, appKey, appSecret, rawBody, signature, valid,
  });
  return {
    verify: [
      v('docs-reproducible-example', DOCS_BODY, good, true),
      v('tampered-body', DOCS_BODY.replace('UNPAID', 'PAID'), good, false),
      v('reserialized-body', JSON.stringify(JSON.parse(DOCS_BODY), null, 2), good, false),
      v('uppercase-signature', DOCS_BODY, good.toUpperCase(), false),
      v('empty-signature', DOCS_BODY, '', false),
    ],
    parse: [
      { name: 'docs-order-status-change', rawBody: DOCS_BODY, type: 1, schema: 'OrderStatusChangeWebhook', known: true },
      { name: 'unknown-type', rawBody: '{"type":9999,"shop_id":"1","data":{}}', type: 9999, schema: null, known: false },
    ],
  };
}

// Copied verbatim from TikTok's authorization overview (token/get response example).
const DOCS_TOKEN_BODY = `{
  "code": 0,
  "message": "success",
  "request_id": "2024080809462301024509910319695C45",
  "data": {
    "access_token": "TTP_Fw8rBwAAAAAkW03FYd09DG-9INtpw361hWthei8S3fHX8iPJ5AUv99fLSCYD9-UucaqxTgNRzKZxi5",
    "access_token_expire_in": 1660556783,
    "refresh_token": "TTP_NTUxZTNhYTQ2ZDk2YmRmZWNmYWY2YWY2YzkxNGYwNjQ3YjkzYTllYjA0YmNlMw",
    "refresh_token_expire_in": 1691487031,
    "open_id": "7010736057180325637",
    "seller_name": "Test Seller",
    "seller_base_region": "US",
    "user_type": 0,
    "granted_scopes": [
      "seller.affiliate_collaboration.read",
      "seller.affiliate_collaboration.write"
    ]
  }
}`;

function authVectors() {
  const serviceId = '7123456789';
  const url = (type: string, region: string, sid: string | null, appKey: string | null, state: string | null, u: string) => ({
    type, region, serviceId: sid, appKey, state, url: u,
  });
  const d = JSON.parse(DOCS_TOKEN_BODY).data;
  return {
    authorizationUrls: [
      url('seller', 'us', serviceId, null, 'abc', 'https://services.us.tiktokshop.com/open/authorize?service_id=7123456789&state=abc'),
      url('seller', 'row', serviceId, null, null, 'https://services.tiktokshop.com/open/authorize?service_id=7123456789'),
      url('partner', 'us', serviceId, null, 'abc', 'https://partner.us.tiktokshop.com/open/authorize?service_id=7123456789&state=abc'),
      url('partner', 'row', serviceId, null, 'abc', 'https://partner.tiktokshop.com/open/authorize?service_id=7123456789&state=abc'),
      url('creator', 'row', null, '123abc', 'a b&c', 'https://shop.tiktok.com/alliance/creator/auth?app_key=123abc&state=a%20b%26c'),
    ],
    tokenRequests: [
      {
        kind: 'exchange', appKey: '123abc', appSecret: 's3cret', value: 'CODE123',
        url: 'https://auth.tiktok-shops.com/api/v2/token/get?app_key=123abc&app_secret=s3cret&auth_code=CODE123&grant_type=authorized_code',
      },
      {
        kind: 'refresh', appKey: '123abc', appSecret: 's3cret', value: 'TTP_C2XWDN63ON-FOHJSMR0WSG',
        url: 'https://auth.tiktok-shops.com/api/v2/token/refresh?app_key=123abc&app_secret=s3cret&refresh_token=TTP_C2XWDN63ON-FOHJSMR0WSG&grant_type=refresh_token',
      },
    ],
    tokenResponses: [
      {
        name: 'docs-example',
        body: DOCS_TOKEN_BODY,
        expected: {
          accessToken: d.access_token,
          accessTokenExpireIn: d.access_token_expire_in,
          refreshToken: d.refresh_token,
          refreshTokenExpireIn: d.refresh_token_expire_in,
          openId: d.open_id,
          sellerName: d.seller_name,
          sellerBaseRegion: d.seller_base_region,
          userType: d.user_type,
          grantedScopes: d.granted_scopes,
        },
        errorCode: null,
      },
      {
        name: 'error',
        body: '{"code":36004004,"message":"invalid auth code","request_id":"r2","data":{}}',
        expected: null,
        errorCode: 36004004,
      },
    ],
  };
}

export function buildVectors(): Record<string, string> {
  const json = (o: unknown) => JSON.stringify(o, null, 2) + '\n';
  return {
    'signing.json': json(signingVectors()),
    'webhooks.json': json(webhookVectors()),
    'auth.json': json(authVectors()),
  };
}

if (process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1]) {
  const out = fileURLToPath(new URL('../shared/test-vectors/', import.meta.url));
  for (const [name, text] of Object.entries(buildVectors())) writeFileSync(out + name, text);
}
