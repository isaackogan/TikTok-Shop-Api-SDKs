using System;

namespace TikTokShop.Api;

/// <summary>
/// The app key, app secret, access token and shop cipher a client signs with. Immutable.
/// <see cref="ToString"/> never prints a secret.
/// </summary>
public sealed class ShopCredentials
{
    /// <summary>Creates credentials. An empty access token or shop cipher means none.</summary>
    public ShopCredentials(string appKey, string appSecret, string? accessToken = null, string? shopCipher = null)
    {
        AppKey = appKey ?? throw new ArgumentNullException(nameof(appKey));
        AppSecret = appSecret ?? throw new ArgumentNullException(nameof(appSecret));
        AccessToken = string.IsNullOrEmpty(accessToken) ? null : accessToken;
        ShopCipher = string.IsNullOrEmpty(shopCipher) ? null : shopCipher;
    }

    /// <summary>The app key, sent as <c>app_key</c>.</summary>
    public string AppKey { get; }

    /// <summary>The app secret, which signs requests. Never sent.</summary>
    public string AppSecret { get; }

    /// <summary>Sent as <c>x-tts-access-token</c>; <c>null</c> for none.</summary>
    public string? AccessToken { get; }

    /// <summary>Sent as <c>shop_cipher</c> to the operations that take one; <c>null</c> for none.</summary>
    public string? ShopCipher { get; }

    /// <summary>
    /// Credentials for another shop. A value that was not given keeps this one; <c>null</c> or <c>""</c> clears it.
    /// This instance is not changed.
    /// </summary>
    public ShopCredentials With(Optional<string?> accessToken = default, Optional<string?> shopCipher = default) =>
        new(AppKey, AppSecret, accessToken.GetValueOrDefault(AccessToken), shopCipher.GetValueOrDefault(ShopCipher));

    /// <inheritdoc/>
    public override string ToString() =>
        $"ShopCredentials {{ AppKey = {AppKey}, AppSecret = ***, AccessToken = {(AccessToken is null ? "null" : "***")}, ShopCipher = {(ShopCipher is null ? "null" : "***")} }}";
}
