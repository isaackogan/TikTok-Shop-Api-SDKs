"""Webhook verification and typed parsing."""

from __future__ import annotations

import hashlib
import hmac
import importlib
import json
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, TypeAlias

import attrs

from .generated._meta import EVENT_TYPES as _EVENT_TYPES
from .generated._meta import WEBHOOKS

#: Webhook type ID -> event name, e.g. ``1`` -> ``"ORDER_STATUS_CHANGE"``.
EVENT_TYPES: dict[int, str] = dict(_EVENT_TYPES)

if TYPE_CHECKING:
    from .generated._webhook_event import GeneratedWebhookEvent


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


#: A parsed webhook: one generated model per known type, or :class:`UnknownWebhookEvent`.
WebhookEvent: TypeAlias = "GeneratedWebhookEvent | UnknownWebhookEvent"


def _model(schema: str) -> Any:
    # generated/models/<snake_case>.py defines <schema>; the package re-exports it.
    return getattr(importlib.import_module("tiktok_shop_api.generated.models"), schema)


def _first_null_required(value: Any, path: str) -> str | None:
    """R28: the first required attribute (dotted path) that is None, in a generated model and the models it holds."""
    if isinstance(value, list):
        for i, item in enumerate(value):
            found = _first_null_required(item, f"{path}[{i}]")
            if found is not None:
                return found
        return None
    if not attrs.has(type(value)):
        return None
    for f in attrs.fields(type(value)):
        if not f.init:  # additional_properties
            continue
        v = getattr(value, f.name)
        where = f"{path}.{f.name}" if path else f.name
        if v is None and f.default is attrs.NOTHING:
            return where
        found = _first_null_required(v, where)
        if found is not None:
            return found
    return None


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
    def parse(raw_body: bytes | str) -> WebhookEvent:
        """Parse a body to its generated model; an unknown ``type`` gives an :class:`UnknownWebhookEvent`.

        Parsing is strict (R28): raises ``ValueError`` when the body is not JSON, not an object, has no integer ``type``,
        or (for a known type) lacks a required field or has it null, at any depth.
        """
        body = json.loads(_to_bytes(raw_body))
        if not isinstance(body, dict):
            raise ValueError("Webhook body is not a JSON object")
        t = body.get("type")
        if not isinstance(t, int) or isinstance(t, bool):
            raise ValueError("Webhook body has no integer 'type'")
        schema = _SCHEMAS.get(t)
        if schema is None:
            return UnknownWebhookEvent(type=t, raw=body)
        try:
            event = _model(schema).from_dict(body)
        except (KeyError, TypeError, AttributeError, ValueError) as e:
            raise ValueError(f"Webhook type {t} does not match {schema}: {e!r}") from e
        missing = _first_null_required(event, "")
        if missing is not None:
            raise ValueError(f"Webhook type {t} does not match {schema}: required field {missing!r} is null")
        return event

    @staticmethod
    def verify_and_parse(*, app_key: str, app_secret: str, raw_body: bytes | str, signature: str) -> WebhookEvent:
        """Verify, then parse. Raises :class:`WebhookSignatureError` on a mismatch."""
        if not Webhooks.verify(app_key=app_key, app_secret=app_secret, raw_body=raw_body, signature=signature):
            raise WebhookSignatureError()
        return Webhooks.parse(raw_body)
