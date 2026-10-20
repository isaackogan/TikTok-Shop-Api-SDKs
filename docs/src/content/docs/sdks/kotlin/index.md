---
title: Kotlin SDK
description: Install tiktok-shop-api-kotlin, the typed TikTok Shop API client for Kotlin on the JVM, and make your first call.
sidebar:
  label: Overview
  order: 1
---

`tiktok-shop-api-kotlin` is a typed Kotlin client for the TikTok Shop Partner API. It signs requests, handles OAuth, works with many shops at once, and verifies and types webhooks as a sealed class. It is published to [Maven Central](https://central.sonatype.com/artifact/com.isaackogan/tiktok-shop-api-kotlin), and its source is in [`kotlin/`](https://github.com/isaackogan/TikTok-Shop-Api-SDKs/tree/main/kotlin).

## Install

Gradle (Kotlin DSL):

```kts
dependencies {
    implementation("com.isaackogan:tiktok-shop-api-kotlin:{{version:kotlin}}")
}
```

Maven:

```xml
<dependency>
  <groupId>com.isaackogan</groupId>
  <artifactId>tiktok-shop-api-kotlin</artifactId>
  <version>{{version:kotlin}}</version>
</dependency>
```

Needs JVM 11 or newer. The runtime dependencies are OkHttp and gson.

## First call

With an access token from the [OAuth helper](/sdks/kotlin/authorization/), create a client and call an operation:

```kotlin
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
```

Pass `shopCipher = "..."` in the options and every operation that needs one gets it. Every call is signed, timestamped and sent with your access token.

## In this section

- [Authorization](/sdks/kotlin/authorization/): `TikTokShopAuth`, authorization URLs, token exchange and refresh.
- [Calling the API](/sdks/kotlin/calling-the-api/): the client, API areas, many shops and options.
- [Webhooks](/sdks/kotlin/webhooks/): `Webhooks.verifyAndParse` and the `WebhookEvent` sealed class.
- [Errors](/sdks/kotlin/errors/): `TikTokShopException` and its codes.
