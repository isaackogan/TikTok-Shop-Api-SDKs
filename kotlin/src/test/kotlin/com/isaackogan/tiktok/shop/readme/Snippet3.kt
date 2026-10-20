package com.isaackogan.tiktok.shop.readme

import com.isaackogan.tiktok.shop.TikTokShop

class ManyShops {
    fun run(client: TikTokShop) {
        // Same HTTP client and connection pool, different shop. The original is not changed.
        val shop = client.withShop(accessToken = "OTHER_ACCESS_TOKEN", shopCipher = "OTHER_SHOP_CIPHER")
    }
}
