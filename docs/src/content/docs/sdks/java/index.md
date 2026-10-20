---
title: Java SDK
description: Install tiktok-shop-api, the typed TikTok Shop API client for Java, from Maven Central and make your first call.
sidebar:
  label: Overview
  order: 1
---

`tiktok-shop-api` is a typed Java client for the TikTok Shop Partner API. It signs requests, handles OAuth, works with many shops at once, and verifies and types webhooks. It is published to [Maven Central](https://central.sonatype.com/artifact/com.isaackogan/tiktok-shop-api), and its source is in [`java/`](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/java).

## Install

Maven:

```xml
<dependency>
  <groupId>com.isaackogan</groupId>
  <artifactId>tiktok-shop-api</artifactId>
  <version>{{version:java}}</version>
</dependency>
```

Gradle:

```groovy
implementation 'com.isaackogan:tiktok-shop-api:{{version:java}}'
```

Requires Java 11 or newer. The HTTP layer is OkHttp and the JSON layer is gson.

## First call

With an access token from the [OAuth helper](/sdks/java/authorization/), build a client and call an operation:

```java
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
```

Each API group is a getter on the client (`orders()`, `products()`, `fulfillment()`, `finance()`, ...) returning the generated API class. Signing, `app_key`, `timestamp`, the `x-tts-access-token` header and `shop_cipher` are added for you.

## In this section

- [Authorization](/sdks/java/authorization/): `TikTokShopAuth`, authorization URLs, token exchange and refresh.
- [Calling the API](/sdks/java/calling-the-api/): the client, API groups, many shops and options.
- [Webhooks](/sdks/java/webhooks/): `Webhooks.verifyAndParse` and typed events.
- [Errors](/sdks/java/errors/): `TikTokShopException`, `ApiException` and their codes.
