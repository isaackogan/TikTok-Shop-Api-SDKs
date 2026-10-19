package com.isaackogan.tiktok.shop.readme;

import com.isaackogan.tiktok.shop.TikTokShop;
import com.isaackogan.tiktok.shop.generated.ApiException;
import com.isaackogan.tiktok.shop.generated.model.GetAuthorizedShopsResponse;

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
