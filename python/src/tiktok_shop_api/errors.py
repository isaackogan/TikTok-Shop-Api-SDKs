from __future__ import annotations


class TikTokShopError(Exception):
    """Raised for every failed call. The original exception, if any, is ``__cause__``.

    - An envelope with a non-zero ``code``, even on HTTP 200: TikTok's ``code``, with ``http_status`` set.
    - A non-2xx reply: TikTok's non-zero ``code`` if the body has one, else the HTTP status; ``http_status`` is set.
    - A 2xx reply that cannot be understood: -1 with ``http_status`` set. That covers a body that is not a JSON object,
      a ``code`` that is not an integer, ``code`` 0 without ``data`` on a token call, and a body that does not fit its
      model.
    - A transport failure with no HTTP response at all (connection refused, DNS, TLS, timeout): -1 with ``http_status``
      ``None``.
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
