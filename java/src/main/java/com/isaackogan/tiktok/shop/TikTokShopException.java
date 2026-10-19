package com.isaackogan.tiktok.shop;

/**
 * Thrown for every failed call:
 *
 * <ul>
 *   <li>an envelope with {@code code != 0}, even on HTTP 200;
 *   <li>a non-2xx response ({@link #getHttpStatus()} is set; {@link #getCode()} is TikTok's code from the body, or the HTTP
 *       status when the body has none);
 *   <li>a 2xx response whose body is not a JSON object ({@link #getCode()} is 0);
 *   <li>a network error or timeout ({@link #getCause()} is the {@link java.io.IOException}, {@link #getHttpStatus()} is
 *       null).
 * </ul>
 *
 * <p>The message never contains the request URL or its query.
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
