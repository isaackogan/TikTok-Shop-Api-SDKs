package com.isaackogan.tiktok.shop

/** Thrown by [Webhooks.verifyAndParse] when the signature does not match the body. */
class WebhookSignatureException : RuntimeException("webhook signature does not match")
