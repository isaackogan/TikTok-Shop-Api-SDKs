package com.isaackogan.tiktok.shop;

/** The webhook's signature does not match its body. */
public class WebhookSignatureException extends RuntimeException {
    private static final long serialVersionUID = 1L;

    public WebhookSignatureException() {
        super("Webhook signature does not match");
    }
}
