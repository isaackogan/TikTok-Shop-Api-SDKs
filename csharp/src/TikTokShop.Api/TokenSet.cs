using System;
using System.Collections.Generic;
using System.Text;

namespace TikTokShop.Api;

/// <summary>
/// The tokens TikTok returns for an authorization code or a refresh token.
/// </summary>
/// <remarks>
/// <see cref="ToString"/> never prints a token. The type stays serializable for storage with System.Text.Json or Newtonsoft.Json,
/// and those serializers write the real values: protect what you store.
/// </remarks>
public sealed record TokenSet
{
    /// <summary>Creates a token set.</summary>
    /// <param name="accessToken">Sent as <c>x-tts-access-token</c>.</param>
    /// <param name="accessTokenExpireIn">When the access token expires, as TikTok sends it (a Unix timestamp in seconds).</param>
    /// <param name="refreshToken">Trade it for new tokens with <see cref="TikTokShopAuth.RefreshAsync"/>.</param>
    /// <param name="refreshTokenExpireIn">When the refresh token expires, as TikTok sends it (a Unix timestamp in seconds).</param>
    /// <param name="openId">The seller's open ID, with its exact digits; <c>null</c> when TikTok sent none.</param>
    /// <param name="sellerName">The seller's name; <c>null</c> when TikTok sent none.</param>
    /// <param name="sellerBaseRegion">The seller's base region; <c>null</c> when TikTok sent none.</param>
    /// <param name="userType">TikTok's user type; <c>null</c> when TikTok sent none.</param>
    /// <param name="grantedScopes">The scopes the seller granted; null when TikTok sent none.</param>
    public TokenSet(
        string accessToken,
        long accessTokenExpireIn,
        string refreshToken,
        long refreshTokenExpireIn,
        string? openId = null,
        string? sellerName = null,
        string? sellerBaseRegion = null,
        int? userType = null,
        IReadOnlyList<string>? grantedScopes = null)
    {
        AccessToken = accessToken ?? throw new ArgumentNullException(nameof(accessToken));
        AccessTokenExpireIn = accessTokenExpireIn;
        RefreshToken = refreshToken ?? throw new ArgumentNullException(nameof(refreshToken));
        RefreshTokenExpireIn = refreshTokenExpireIn;
        OpenId = openId;
        SellerName = sellerName;
        SellerBaseRegion = sellerBaseRegion;
        UserType = userType;
        GrantedScopes = grantedScopes;
    }

    /// <summary>Sent as <c>x-tts-access-token</c>.</summary>
    public string AccessToken { get; init; }

    /// <summary>When the access token expires, as TikTok sends it (a Unix timestamp in seconds).</summary>
    public long AccessTokenExpireIn { get; init; }

    /// <summary>Trade it for new tokens with <see cref="TikTokShopAuth.RefreshAsync"/>.</summary>
    public string RefreshToken { get; init; }

    /// <summary>When the refresh token expires, as TikTok sends it (a Unix timestamp in seconds).</summary>
    public long RefreshTokenExpireIn { get; init; }

    /// <summary>The seller's open ID, with its exact digits; <c>null</c> when TikTok sent none.</summary>
    public string? OpenId { get; init; }

    /// <summary>The seller's name; <c>null</c> when TikTok sent none.</summary>
    public string? SellerName { get; init; }

    /// <summary>The seller's base region; <c>null</c> when TikTok sent none.</summary>
    public string? SellerBaseRegion { get; init; }

    /// <summary>TikTok's user type; <c>null</c> when TikTok sent none.</summary>
    public int? UserType { get; init; }

    /// <summary>The scopes the seller granted; <c>null</c> when TikTok sent none (or something other than a list of strings).</summary>
    public IReadOnlyList<string>? GrantedScopes { get; init; }

    /// <summary>The members that are safe to print: no token.</summary>
    private bool PrintMembers(StringBuilder builder)
    {
        builder.Append("AccessToken = ***, AccessTokenExpireIn = ").Append(AccessTokenExpireIn)
            .Append(", RefreshToken = ***, RefreshTokenExpireIn = ").Append(RefreshTokenExpireIn)
            .Append(", OpenId = ").Append(OpenId ?? "null")
            .Append(", SellerName = ").Append(SellerName ?? "null")
            .Append(", SellerBaseRegion = ").Append(SellerBaseRegion ?? "null")
            .Append(", UserType = ").Append(UserType?.ToString() ?? "null")
            .Append(", GrantedScopes = ").Append(GrantedScopes is null ? "null" : "[" + string.Join(", ", GrantedScopes) + "]");
        return true;
    }

    /// <summary>Prints the record without its tokens.</summary>
    public override string ToString()
    {
        var builder = new StringBuilder("TokenSet { ");
        PrintMembers(builder);
        return builder.Append(" }").ToString();
    }
}
