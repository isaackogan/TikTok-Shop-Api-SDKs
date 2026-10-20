package com.isaackogan.tiktok.shop;

import okhttp3.MediaType;

/**
 * A request body that rides on a GET request as a tag: OkHttp refuses {@code method("GET", body)}, so {@link TikTokApiClient}
 * parks the body here and {@link SigningInterceptor} sends it.
 */
final class GetBody {
    final byte[] bytes;
    final MediaType mediaType;

    GetBody(byte[] bytes, MediaType mediaType) {
        this.bytes = bytes;
        this.mediaType = mediaType;
    }
}
