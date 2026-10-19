package com.isaackogan.tiktok.shop;

// The README's Java snippets, verbatim. ReadmeTest fails if the README and this file drift apart.
// Compile-only: nothing here runs.
import com.isaackogan.tiktok.shop.TikTokShopAuth;
import com.isaackogan.tiktok.shop.TokenSet;
import com.isaackogan.tiktok.shop.TikTokShop;
import com.isaackogan.tiktok.shop.generated.ApiException;
import com.isaackogan.tiktok.shop.generated.model.GetAuthorizedShopsResponse;
import com.isaackogan.tiktok.shop.WebhookEvent;
import com.isaackogan.tiktok.shop.WebhookSignatureException;
import com.isaackogan.tiktok.shop.Webhooks;
import com.isaackogan.tiktok.shop.generated.event.OrderStatusChangeEvent;
import com.isaackogan.tiktok.shop.generated.model.OrderStatusChangeWebhook;

class OAuthExample {
    void run() {
        TikTokShopAuth auth = TikTokShopAuth.builder()
                .appKey("YOUR_APP_KEY")
                .appSecret("YOUR_APP_SECRET")
                .serviceId("YOUR_SERVICE_ID")
                .build();

        // 1. Send the seller to this page.
        String url = auth.authorizationUrl(TikTokShopAuth.AuthType.SELLER, TikTokShopAuth.Region.US, "my-state");

        // 2. TikTok redirects back with ?code=...; trade it for tokens.
        TokenSet tokens = auth.exchangeCode("CODE_FROM_THE_REDIRECT");

        // 3. Later, trade the refresh token for new tokens.
        TokenSet fresh = auth.refresh(tokens.getRefreshToken());
    }
}

class FirstCall {
    void run() throws ApiException {
        TikTokShop client = TikTokShop.builder()
                .appKey("YOUR_APP_KEY")
                .appSecret("YOUR_APP_SECRET")
                .accessToken("ACCESS_TOKEN")
                .build();

        GetAuthorizedShopsResponse shops = client.authorization().getAuthorizedShops();
        System.out.println(shops.getData().getShops().get(0).getCipher());
    }
}

class ManyShops {
    void run(TikTokShop client) {
        // Same HTTP client and connection pool, different shop. The original is not changed.
        TikTokShop shop = client.withShop("OTHER_ACCESS_TOKEN", "OTHER_SHOP_CIPHER");
    }
}

class WebhookExample {
    /** Call with the body bytes exactly as received, and the Authorization header. */
    void handle(byte[] rawBody, String authorizationHeader) {
        WebhookEvent event;
        try {
            event = Webhooks.verifyAndParse("YOUR_APP_KEY", "YOUR_APP_SECRET", rawBody, authorizationHeader);
        } catch (WebhookSignatureException e) {
            return; // respond 401
        }

        if (event instanceof OrderStatusChangeEvent) {
            OrderStatusChangeWebhook order = ((OrderStatusChangeEvent) event).getPayload();
            System.out.println(order.getData().getOrderId());
        }
    }
}
