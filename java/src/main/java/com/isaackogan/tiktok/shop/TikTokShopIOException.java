package com.isaackogan.tiktok.shop;

import com.isaackogan.tiktok.shop.generated.ApiException;
import java.io.IOException;

/**
 * Carries a {@link TikTokShopException} out of {@link SigningInterceptor}. An interceptor may only throw an
 * {@link IOException}: OkHttp hands one to an async call's {@code onFailure}, but rethrows anything else on its
 * dispatcher thread. {@link TikTokApiClient} unwraps it again, so callers never see this type.
 */
final class TikTokShopIOException extends IOException {
    private static final long serialVersionUID = 1L;

    TikTokShopIOException(TikTokShopException cause) {
        super(cause.getMessage(), cause);
    }

    @Override
    public synchronized TikTokShopException getCause() {
        return (TikTokShopException) super.getCause();
    }

    /**
     * The {@link TikTokShopException} behind {@code e}, or null. It may be tunnelled (OkHttp wraps the tunnel in an
     * {@code InterruptedIOException} once the call timeout has passed) or direct (a decode failure on an async call).
     */
    static TikTokShopException unwrap(ApiException e) {
        for (Throwable c = e.getCause(); c != null; c = c.getCause()) {
            if (c instanceof TikTokShopIOException) {
                return ((TikTokShopIOException) c).getCause();
            }
            if (c instanceof TikTokShopException) {
                return (TikTokShopException) c;
            }
        }
        return null;
    }
}
