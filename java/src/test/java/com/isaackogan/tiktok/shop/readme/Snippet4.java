package com.isaackogan.tiktok.shop.readme;

import com.isaackogan.tiktok.shop.WebhookEvent;
import com.isaackogan.tiktok.shop.WebhookSignatureException;
import com.isaackogan.tiktok.shop.Webhooks;
import com.isaackogan.tiktok.shop.generated.event.OrderStatusChangeEvent;
import com.isaackogan.tiktok.shop.generated.model.OrderStatusChangeWebhook;

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
