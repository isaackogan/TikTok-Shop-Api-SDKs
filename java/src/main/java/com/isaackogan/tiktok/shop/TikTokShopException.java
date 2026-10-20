package com.isaackogan.tiktok.shop;

/**
 * Thrown for every failed call:
 *
 * <ul>
 *   <li>an envelope with {@code code != 0}, even on HTTP 200: TikTok's code, with {@link #getHttpStatus()} set;
 *   <li>a non-2xx response ({@link #getHttpStatus()} is always set; {@link #getCode()} is TikTok's non-zero code from the
 *       body, or the HTTP status when the body has none, whatever the body is);
 *   <li>a 2xx response that cannot be understood ({@link #getCode()} is -1, {@link #getHttpStatus()} is set): a body that
 *       is not a JSON object, a {@code code} that is not an integer, a body that does not fit its model (the decoder's
 *       exception is the cause), or a token reply with {@code code} 0 but no {@code data};
 *   <li>a transport failure with no response at all: connection refused, DNS, TLS, timeout ({@link #getCode()} is -1,
 *       {@link #getCause()} is the {@link java.io.IOException}, {@link #getHttpStatus()} is null).
 * </ul>
 *
 * <p>The message never contains the request URL or its query. The {@code *Async} methods deliver it to
 * {@code ApiCallback.onFailure} as the cause of the {@code ApiException}.
 */
public class TikTokShopException extends RuntimeException {
    private static final long serialVersionUID = 1L;

    private final int code;
    private final String requestId;
    private final Integer httpStatus;

    public TikTokShopException(int code, String message, String requestId, Integer httpStatus, Throwable cause) {
        super(message, cause);
        this.code = code;
        this.requestId = requestId;
        this.httpStatus = httpStatus;
    }

    /** TikTok's error code. */
    public int getCode() {
        return code;
    }

    /** TikTok's request_id, or an empty string when the response had none. */
    public String getRequestId() {
        return requestId;
    }

    /** The HTTP status, or null when no response arrived. */
    public Integer getHttpStatus() {
        return httpStatus;
    }

    @Override
    public String toString() {
        StringBuilder s = new StringBuilder(getClass().getName()).append(": ").append(getMessage()).append(" (code ").append(code);
        if (requestId != null && !requestId.isEmpty()) {
            s.append(", request_id ").append(requestId);
        }
        return s.append(')').toString();
    }
}
