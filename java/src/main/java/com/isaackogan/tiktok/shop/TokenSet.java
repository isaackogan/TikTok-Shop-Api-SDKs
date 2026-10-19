package com.isaackogan.tiktok.shop;

import java.util.Collections;
import java.util.List;

/** The result of exchanging an auth code or refreshing a token. */
public final class TokenSet {
    private final String accessToken;
    private final long accessTokenExpireIn;
    private final String refreshToken;
    private final long refreshTokenExpireIn;
    private final String openId;
    private final String sellerName;
    private final String sellerBaseRegion;
    private final Integer userType;
    private final List<String> grantedScopes;

    TokenSet(String accessToken, long accessTokenExpireIn, String refreshToken, long refreshTokenExpireIn, String openId,
            String sellerName, String sellerBaseRegion, Integer userType, List<String> grantedScopes) {
        this.accessToken = accessToken;
        this.accessTokenExpireIn = accessTokenExpireIn;
        this.refreshToken = refreshToken;
        this.refreshTokenExpireIn = refreshTokenExpireIn;
        this.openId = openId;
        this.sellerName = sellerName;
        this.sellerBaseRegion = sellerBaseRegion;
        this.userType = userType;
        this.grantedScopes = Collections.unmodifiableList(grantedScopes);
    }

    public String getAccessToken() {
        return accessToken;
    }

    /** The Unix time (seconds) at which the access token expires. */
    public long getAccessTokenExpireIn() {
        return accessTokenExpireIn;
    }

    public String getRefreshToken() {
        return refreshToken;
    }

    /** The Unix time (seconds) at which the refresh token expires. */
    public long getRefreshTokenExpireIn() {
        return refreshTokenExpireIn;
    }

    /** Null when TikTok sent none. Exact digits, even if TikTok sent a JSON number. */
    public String getOpenId() {
        return openId;
    }

    /** Null when TikTok sent none (creator and partner tokens may lack the seller fields). */
    public String getSellerName() {
        return sellerName;
    }

    /** Null when TikTok sent none. */
    public String getSellerBaseRegion() {
        return sellerBaseRegion;
    }

    /** Null when TikTok sent none. */
    public Integer getUserType() {
        return userType;
    }

    /** Empty when TikTok sent none. */
    public List<String> getGrantedScopes() {
        return grantedScopes;
    }

    // Tokens are secrets: keep them out of logs.
    @Override
    public String toString() {
        return "TokenSet{openId=" + openId + ", sellerName=" + sellerName + ", grantedScopes=" + grantedScopes + ", tokens redacted}";
    }
}
