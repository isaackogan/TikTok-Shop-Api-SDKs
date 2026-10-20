<?php

declare(strict_types=1);

namespace TikTokShop\Api;

/**
 * Every failed call: an envelope with `code != 0` (even on HTTP 200), a non-2xx status, a 2xx reply that is not
 * JSON, and transport failures (connection refused, timeout).
 *
 * The code follows ruling R13b. A non-2xx reply's code is TikTok's non-zero `code` from the body, else the HTTP
 * status. A 2xx reply's code is TikTok's code, or -1 when the reply cannot be understood. A transport failure has
 * code -1 and no HTTP status (ruling R13c). {@see self::getCode()} returns the same value as {@see self::getTikTokCode()}.
 *
 * Transport failures never carry the request URL (it holds the signature and other request parameters): the
 * message and the {@see self::getPrevious()} chain are scrubbed.
 */
class TikTokShopException extends \RuntimeException
{
    public function __construct(
        string $message,
        private readonly int $tikTokCode,
        private readonly string $requestId = '',
        private readonly ?int $httpStatus = null,
        ?\Throwable $previous = null,
    ) {
        parent::__construct($message, $tikTokCode, $previous);
    }

    /** TikTok's error code, see the class comment. */
    public function getTikTokCode(): int
    {
        return $this->tikTokCode;
    }

    /** TikTok's `request_id`, or an empty string when the reply had none. */
    public function getRequestId(): string
    {
        return $this->requestId;
    }

    /** The HTTP status, or null for a transport failure. */
    public function getHttpStatus(): ?int
    {
        return $this->httpStatus;
    }
}
