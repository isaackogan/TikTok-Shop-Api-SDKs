package com.isaackogan.tiktok.shop;

import com.google.gson.JsonObject;
import com.isaackogan.tiktok.shop.generated.event.WebhookEventVisitor;

/**
 * A parsed webhook. {@link Webhooks#parse} returns one of the generated event classes in
 * {@code com.isaackogan.tiktok.shop.generated.event} (one per webhook type, e.g. {@code OrderStatusChangeEvent}, each with
 * {@code getPayload()} returning the generated model), or an {@link UnknownWebhookEvent}.
 *
 * <p>Narrow with {@code instanceof}, or call {@link #accept} with a {@link WebhookEventVisitor}.
 */
public abstract class WebhookEvent {
    private final int type;
    private final JsonObject raw;

    protected WebhookEvent(int type, JsonObject raw) {
        this.type = type;
        this.raw = raw;
    }

    /** The webhook's integer {@code type}. */
    public final int getType() {
        return type;
    }

    /**
     * The body as parsed JSON, with every field TikTok sent, including those this SDK's models do not know. Do not modify it.
     */
    public final JsonObject getRaw() {
        return raw;
    }

    /** Calls the visitor method for this event's class. */
    public abstract <R> R accept(WebhookEventVisitor<R> visitor);
}
