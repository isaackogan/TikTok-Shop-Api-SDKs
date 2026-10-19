package com.isaackogan.tiktok.shop.readme

import com.isaackogan.tiktok.shop.WebhookEvent
import com.isaackogan.tiktok.shop.WebhookSignatureException
import com.isaackogan.tiktok.shop.Webhooks

class WebhookExample {
    /** Call with the body bytes exactly as received, and the Authorization header. */
    fun handle(rawBody: ByteArray, authorizationHeader: String?) {
        val event = try {
            Webhooks.verifyAndParse("YOUR_APP_KEY", "YOUR_APP_SECRET", rawBody, authorizationHeader)
        } catch (e: WebhookSignatureException) {
            return // respond 401
        }

        when (event) {
            is WebhookEvent.OrderStatusChange -> println(event.payload.data?.orderId)
            is WebhookEvent.Unknown -> println("a webhook type this SDK does not know: ${event.type}")
            else -> {}
        }
    }
}
