"""Base classes of the generated per-tag API groups, and the error translation they share."""

from __future__ import annotations

from collections.abc import Awaitable, Callable
from contextvars import ContextVar
from typing import Any

import httpx

from .errors import TikTokShopError

# What a parse failure of an otherwise successful response looks like from the generated models.
_PARSE_ERRORS = (KeyError, TypeError, ValueError, AttributeError)

#: The HTTP status and request ID of the last reply the response hook accepted in this context, so a decode failure
#: after it can carry them (R13d).
_ACCEPTED: ContextVar[tuple[int, str] | None] = ContextVar("tiktok_shop_api_accepted", default=None)


def _transport_error(e: httpx.HTTPError | httpx.InvalidURL) -> TikTokShopError:
    """R13c: no HTTP response at all (connect, DNS, TLS, timeout) is code -1 with no http_status."""
    kind = "Request timed out" if isinstance(e, httpx.TimeoutException) else "Request failed"
    return TikTokShopError(f"{kind}: {e}", code=-1)


def _decode_error(e: Exception) -> TikTokShopError:
    """R13d: a 2xx envelope that does not fit its model is code -1, with the status and request ID."""
    status, request_id = _ACCEPTED.get() or (None, "")
    return TikTokShopError(f"Response does not match its model: {e!r}", code=-1, request_id=request_id, http_status=status)


class SyncGroup:
    def __init__(self, client: Any) -> None:
        self._client = client

    def _run(self, fn: Callable[..., Any], **kwargs: Any) -> Any:
        token = _ACCEPTED.set(None)
        try:
            return fn(client=self._client, **kwargs).parsed
        except TikTokShopError:
            raise
        except (httpx.HTTPError, httpx.InvalidURL) as e:
            raise _transport_error(e) from e
        except _PARSE_ERRORS as e:
            raise _decode_error(e) from e
        finally:
            _ACCEPTED.reset(token)


class AsyncGroup:
    def __init__(self, client: Any) -> None:
        self._client = client

    async def _run(self, fn: Callable[..., Awaitable[Any]], **kwargs: Any) -> Any:
        token = _ACCEPTED.set(None)
        try:
            return (await fn(client=self._client, **kwargs)).parsed
        except TikTokShopError:
            raise
        except (httpx.HTTPError, httpx.InvalidURL) as e:
            raise _transport_error(e) from e
        except _PARSE_ERRORS as e:
            raise _decode_error(e) from e
        finally:
            _ACCEPTED.reset(token)
