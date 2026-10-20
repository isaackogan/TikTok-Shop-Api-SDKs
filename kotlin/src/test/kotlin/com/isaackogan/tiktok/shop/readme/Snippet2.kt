package com.isaackogan.tiktok.shop.readme

import com.isaackogan.tiktok.shop.TikTokShop
import com.isaackogan.tiktok.shop.TikTokShopException
import com.isaackogan.tiktok.shop.TikTokShopOptions

class FirstCall {
    fun run() {
        val client = TikTokShop(
            TikTokShopOptions(appKey = "YOUR_APP_KEY", appSecret = "YOUR_APP_SECRET", accessToken = "ACCESS_TOKEN"),
        )

        try {
            val shops = client.authorization.getAuthorizedShops()
            println(shops.data?.shops?.firstOrNull()?.cipher)
        } catch (e: TikTokShopException) {
            println("TikTok said ${e.code}: ${e.message} (request ${e.requestId})")
        }
    }
}
