package com.isaackogan.tiktok.shop

/** The result of exchanging an auth code or refreshing a token. */
class TokenSet(
    val accessToken: String,
    /** The Unix time (seconds) at which the access token expires. */
    val accessTokenExpireIn: Long,
    val refreshToken: String,
    /** The Unix time (seconds) at which the refresh token expires. */
    val refreshTokenExpireIn: Long,
    /** Null when TikTok sent none. Exact digits, even if TikTok sent a JSON number. */
    val openId: String? = null,
    /** Null when TikTok sent none (creator and partner tokens may lack the seller fields). */
    val sellerName: String? = null,
    /** Null when TikTok sent none. */
    val sellerBaseRegion: String? = null,
    /** Null when TikTok sent none. */
    val userType: Int? = null,
    /** Null when TikTok sent none (or something other than a list of strings). */
    val grantedScopes: List<String>? = null,
) {
    // Tokens are secrets: keep them out of logs.
    override fun toString(): String = "TokenSet(openId=$openId, sellerName=$sellerName, grantedScopes=$grantedScopes, tokens redacted)"
}
