package com.isaackogan.tiktok.shop.readme;

import com.isaackogan.tiktok.shop.TikTokShop;

class ManyShops {
    void run(TikTokShop client) {
        // Same HTTP client and connection pool, different shop. The original is not changed.
        TikTokShop shop = client.withShop("OTHER_ACCESS_TOKEN", "OTHER_SHOP_CIPHER");
    }
}
