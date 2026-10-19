package com.isaackogan.tiktok.shop;

/**
 * The per-shop values {@link TikTokShop#withShop(ShopCredentials)} changes. A value you do not set keeps the client's
 * current value; one you set to {@code null} or an empty string clears it:
 *
 * <pre>{@code
 * client.withShop(ShopCredentials.builder().accessToken("t2").build());   // new token, same cipher
 * client.withShop(ShopCredentials.builder().accessToken("t2").shopCipher("c2").build());
 * client.withShop(ShopCredentials.builder().shopCipher(null).build());    // same token, no cipher
 * }</pre>
 */
public final class ShopCredentials {
    private final boolean accessTokenSet;
    private final String accessToken;
    private final boolean shopCipherSet;
    private final String shopCipher;

    private ShopCredentials(Builder b) {
        this.accessTokenSet = b.accessTokenSet;
        this.accessToken = b.accessToken;
        this.shopCipherSet = b.shopCipherSet;
        this.shopCipher = b.shopCipher;
    }

    public static Builder builder() {
        return new Builder();
    }

    boolean isAccessTokenSet() {
        return accessTokenSet;
    }

    String accessToken() {
        return accessToken;
    }

    boolean isShopCipherSet() {
        return shopCipherSet;
    }

    String shopCipher() {
        return shopCipher;
    }

    /** Builds a {@link ShopCredentials}. */
    public static final class Builder {
        private boolean accessTokenSet;
        private String accessToken;
        private boolean shopCipherSet;
        private String shopCipher;

        private Builder() {}

        /** Sets the access token. {@code null} or an empty string clears it; not calling this keeps the current one. */
        public Builder accessToken(String accessToken) {
            this.accessTokenSet = true;
            this.accessToken = accessToken;
            return this;
        }

        /** Sets the shop cipher. {@code null} or an empty string clears it; not calling this keeps the current one. */
        public Builder shopCipher(String shopCipher) {
            this.shopCipherSet = true;
            this.shopCipher = shopCipher;
            return this;
        }

        public ShopCredentials build() {
            return new ShopCredentials(this);
        }
    }
}
