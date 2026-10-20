"""Keeps the token-call secrets out of httpx's request log.

httpx logs every request at INFO as ``HTTP Request: GET <full URL> ...``. Token calls carry ``app_secret``,
``auth_code`` and ``refresh_token`` in the URL query, so a service running at INFO would log them. A filter on the
``httpx`` logger replaces those values with ``***`` before any handler sees the record.
"""

from __future__ import annotations

import logging
import re

_SECRET_PARAMS = re.compile(r"(?<=[?&])(app_secret|auth_code|refresh_token)=[^&\s\"']*")


class _RedactTokenSecrets(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        try:
            message = record.getMessage()
        except Exception:  # a malformed record is the logging module's problem, not ours
            return True
        redacted = _SECRET_PARAMS.sub(r"\1=***", message)
        if redacted != message:
            record.msg = redacted
            record.args = None
        return True


def install() -> None:
    """Adds the filter to the ``httpx`` logger once (idempotent)."""
    logger = logging.getLogger("httpx")
    if not any(isinstance(f, _RedactTokenSecrets) for f in logger.filters):
        logger.addFilter(_RedactTokenSecrets())
