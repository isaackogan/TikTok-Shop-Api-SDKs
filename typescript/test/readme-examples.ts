// Type-checked copy of the README's code (the statements are verbatim; imports point at ../src).
// `test/readme.test.ts` fails if the README and this file drift apart.
import { createServer } from 'node:http';
import { isUnknownWebhookEvent, TikTokShop, TikTokShopAuth, Webhooks, WebhookSignatureError } from '../src/index.ts';
import type { OrderStatusChangeWebhook, UnknownWebhookEvent, WebhookEvent } from '../src/index.ts';

export async function oauthAndCalls(callbackUrl: string, tokenA: string, tokenB: string, cipherA: string, cipherB: string) {

  const auth = new TikTokShopAuth({
    appKey: process.env.TTS_APP_KEY!,
    appSecret: process.env.TTS_APP_SECRET!,
    serviceId: process.env.TTS_SERVICE_ID!, // seller and partner flows
  });

  // 1. Send the seller here. `type` is 'seller' | 'partner' | 'creator'; `region` is 'us' | 'row'.
  const url = auth.authorizationUrl({ type: 'seller', region: 'us', state: 'csrf-token' });

  // 2. TikTok redirects back with ?code=...; exchange it.
  const code = new URL(callbackUrl).searchParams.get('code')!;
  const tokens = await auth.exchangeCode(code);
  // tokens.accessToken, tokens.refreshToken, tokens.openId, tokens.grantedScopes, ...

  // 3. Before the access token expires (accessTokenExpireIn is a Unix timestamp):
  const renewed = await auth.refresh(tokens.refreshToken);

  const client = new TikTokShop({
    appKey: process.env.TTS_APP_KEY!,
    appSecret: process.env.TTS_APP_SECRET!,
    accessToken: tokens.accessToken,
  });

  // Find the shop cipher
  const shops = await client.authorization.getAuthorizedShops();
  const shopCipher = shops.data?.shops?.[0]?.cipher;

  const seller = client.withShop({ accessToken: tokens.accessToken, shopCipher });
  const orders = await seller.orders.getOrderList({ pageSize: 20 });
  const shopA = client.withShop({ accessToken: tokenA, shopCipher: cipherA });
  const shopB = client.withShop({ accessToken: tokenB, shopCipher: cipherB });
}

export function webhookServer() {

  createServer(async (req, res) => {
    const chunks: Buffer[] = [];
    for await (const chunk of req) chunks.push(chunk as Buffer);
    const rawBody = Buffer.concat(chunks); // exactly as received

    try {
      const event = Webhooks.verifyAndParse({
        appKey: process.env.TTS_APP_KEY!,
        appSecret: process.env.TTS_APP_SECRET!,
        rawBody,
        signature: String(req.headers.authorization ?? ''),
      });
      if ('raw' in event) {
        console.log('unknown webhook type', event.type, event.raw);
      } else if (event.type === 1) {
        console.log(event.shopId, event.data?.orderStatus); // OrderStatusChangeWebhook
      }
      res.writeHead(200).end();
    } catch (e) {
      res.writeHead(e instanceof WebhookSignatureError ? 401 : 500).end();
    }
  }).listen(3000);
}

// Type-level checks of the union design: a simple check separates unknown events, then `type` narrows.
export function narrowing(event: WebhookEvent | UnknownWebhookEvent): string | undefined {
  if (isUnknownWebhookEvent(event)) {
    const t: number = event.type;
    const raw: unknown = event.raw;
    void t; void raw;
    return undefined;
  }
  if (event.type === 1) {
    const order: OrderStatusChangeWebhook = event;
    return order.data?.orderStatus;
  }
  return undefined;
}
