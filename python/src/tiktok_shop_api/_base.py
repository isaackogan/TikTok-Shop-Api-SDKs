"""Base classes of the generated per-tag API groups, and the error translation they share."""

from __future__ import annotations

from collections.abc import Awaitable, Callable
from typing import Any

import httpx

from .errors import TikTokShopError

# What a parse failure of an otherwise successful response looks like from the generated models.
_PARSE_ERRORS = (KeyError, TypeError, ValueError, AttributeError)


def _transport_error(e: httpx.HTTPError | httpx.InvalidURL) -> TikTokShopError:
    kind = "Request timed out" if isinstance(e, httpx.TimeoutException) else "Request failed"
    return TikTokShopError(f"{kind}: {e}")


class SyncGroup:
    def __init__(self, client: Any) -> None:
        self._client = client

    def _run(self, fn: Callable[..., Any], **kwargs: Any) -> Any:
        try:
            return fn(client=self._client, **kwargs).parsed
        except TikTokShopError:
            raise
        except (httpx.HTTPError, httpx.InvalidURL) as e:
            raise _transport_error(e) from e
        except _PARSE_ERRORS as e:
            raise TikTokShopError(f"Unexpected response shape: {e!r}") from e


class AsyncGroup:
    def __init__(self, client: Any) -> None:
        self._client = client

    async def _run(self, fn: Callable[..., Awaitable[Any]], **kwargs: Any) -> Any:
        try:
            return (await fn(client=self._client, **kwargs)).parsed
        except TikTokShopError:
            raise
        except (httpx.HTTPError, httpx.InvalidURL) as e:
            raise _transport_error(e) from e
        except _PARSE_ERRORS as e:
            raise TikTokShopError(f"Unexpected response shape: {e!r}") from e
