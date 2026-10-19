from __future__ import annotations


class TikTokShopError(Exception):
    """Raised for every failed call.

    Covers an envelope with ``code != 0`` (even on HTTP 200), a non-2xx status (``http_status`` is set,
    ``code`` and ``message`` come from the body when it has them), a 2xx response whose body is not JSON,
    and network errors and timeouts. The original exception, if any, is ``__cause__``.
    """

    def __init__(
        self,
        message: str,
        *,
        code: int = 0,
        request_id: str = "",
        http_status: int | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.code = code
        self.request_id = request_id
        self.http_status = http_status

    def __repr__(self) -> str:
        return (
            f"TikTokShopError(code={self.code!r}, message={self.message!r}, "
            f"request_id={self.request_id!r}, http_status={self.http_status!r})"
        )
