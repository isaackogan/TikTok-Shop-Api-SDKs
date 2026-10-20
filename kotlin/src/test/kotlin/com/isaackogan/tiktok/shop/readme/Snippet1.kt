package com.isaackogan.tiktok.shop.readme

import com.isaackogan.tiktok.shop.TikTokShopAuth
import com.isaackogan.tiktok.shop.TikTokShopAuthOptions

class OAuthExample {
    fun run() {
        val auth = TikTokShopAuth(
            TikTokShopAuthOptions(appKey = "YOUR_APP_KEY", appSecret = "YOUR_APP_SECRET", serviceId = "YOUR_SERVICE_ID"),
        )

        // 1. Send the seller to this page.
        val url = auth.authorizationUrl(TikTokShopAuth.AuthType.SELLER, TikTokShopAuth.Region.US, state = "my-state")

        // 2. TikTok redirects back with ?code=...; trade it for tokens.
        val tokens = auth.exchangeCode("CODE_FROM_THE_REDIRECT")

        // 3. Later, trade the refresh token for new tokens.
        val fresh = auth.refresh(tokens.refreshToken)
    }
}
