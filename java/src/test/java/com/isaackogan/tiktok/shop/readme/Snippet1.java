package com.isaackogan.tiktok.shop.readme;

import com.isaackogan.tiktok.shop.TikTokShopAuth;
import com.isaackogan.tiktok.shop.TokenSet;

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
