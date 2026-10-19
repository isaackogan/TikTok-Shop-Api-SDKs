"""Webhook verification and typed parsing."""

from __future__ import annotations

import hashlib
import hmac
import importlib
import json
from dataclasses import dataclass
from typing import Any

from .generated._meta import EVENT_TYPES as _EVENT_TYPES
from .generated._meta import WEBHOOKS

#: Webhook type ID -> event name, e.g. ``1`` -> ``"ORDER_STATUS_CHANGE"``.
EVENT_TYPES: dict[int, str] = dict(_EVENT_TYPES)

_SCHEMAS: dict[int, str] = {w["type"]: w["schema"] for w in WEBHOOKS}


class WebhookSignatureError(Exception):
    """The webhook's signature does not match its body."""

    def __init__(self, message: str = "Webhook signature does not match") -> None:
        super().__init__(message)


@dataclass(frozen=True)
class UnknownWebhookEvent:
    """A webhook whose ``type`` this SDK does not know. ``raw`` is the parsed JSON body."""

    type: int
    raw: dict[str, Any]


def _model(schema: str) -> Any:
    # generated/models/<snake_case>.py defines <schema>; the package re-exports it.
    return getattr(importlib.import_module("tiktok_shop_api.generated.models"), schema)


def _to_bytes(raw_body: bytes | bytearray | memoryview | str) -> bytes:
    return raw_body.encode("utf-8") if isinstance(raw_body, str) else bytes(raw_body)


class Webhooks:
    EVENT_TYPES = EVENT_TYPES

    @staticmethod
    def verify(*, app_key: str, app_secret: str, raw_body: bytes | str, signature: str) -> bool:
        """HMAC-SHA256 (key ``app_secret``) over ``app_key + raw_body``, lowercase hex, compared in constant time.

        Pass the body exactly as received; never re-serialize it.
        """
        if not signature:
            return False
        mac = hmac.new(app_secret.encode("utf-8"), digestmod=hashlib.sha256)
        mac.update(app_key.encode("utf-8"))
        mac.update(_to_bytes(raw_body))
        return hmac.compare_digest(mac.hexdigest().encode("ascii"), signature.encode("utf-8"))

    @staticmethod
    def parse(raw_body: bytes | str) -> Any:
        """Parse a body to its generated model; an unknown ``type`` gives an :class:`UnknownWebhookEvent`.

        Raises ``ValueError`` when the body is not JSON, not an object, or lacks the fields its type requires.
        """
        body = json.loads(_to_bytes(raw_body))
        if not isinstance(body, dict):
            raise ValueError("Webhook body is not a JSON object")
        t = body.get("type")
        schema = _SCHEMAS.get(t) if isinstance(t, int) and not isinstance(t, bool) else None
        if schema is None:
            return UnknownWebhookEvent(type=t, raw=body)  # type: ignore[arg-type]
        try:
            return _model(schema).from_dict(body)
        except (KeyError, TypeError, AttributeError) as e:
            raise ValueError(f"Webhook type {t} does not match {schema}: {e!r}") from e

    @staticmethod
    def verify_and_parse(*, app_key: str, app_secret: str, raw_body: bytes | str, signature: str) -> Any:
        """Verify, then parse. Raises :class:`WebhookSignatureError` on a mismatch."""
        if not Webhooks.verify(app_key=app_key, app_secret=app_secret, raw_body=raw_body, signature=signature):
            raise WebhookSignatureError()
        return Webhooks.parse(raw_body)
