package com.isaackogan.tiktok.shop;

import com.google.gson.JsonObject;
import com.isaackogan.tiktok.shop.generated.event.WebhookEventVisitor;

/** A webhook whose integer {@code type} this SDK has no model for. {@link #getRaw()} has the whole body. */
public final class UnknownWebhookEvent extends WebhookEvent {
    public UnknownWebhookEvent(int type, JsonObject raw) {
        super(type, raw);
    }

    @Override
    public <R> R accept(WebhookEventVisitor<R> visitor) {
        return visitor.visitUnknown(this);
    }
}
