"""Request signing and shop-cipher detection."""

from __future__ import annotations

import hashlib
import hmac
import re
from collections.abc import Sequence
from typing import Any

from .generated._meta import OPERATIONS

_EXCLUDED = frozenset({"sign", "access_token"})


class Signer:
    """Pure signing functions. Query values are the decoded values, as the server receives them."""

    @staticmethod
    def string_to_sign(
        *,
        path: str,
        query: Sequence[tuple[str, str]],
        content_type: str | None,
        body: bytes | str | None,
        app_secret: str,
    ) -> str:
        """``secret + path + sorted key+value pairs + body (unless multipart) + secret``."""
        pairs = sorted((p for p in query if p[0] not in _EXCLUDED), key=lambda p: p[0])
        out = [app_secret, path]
        for k, v in pairs:
            out.append(k)
            out.append(v)
        if not (content_type or "").lower().startswith("multipart/form-data"):
            if isinstance(body, (bytes, bytearray)):
                out.append(bytes(body).decode("utf-8"))
            elif body is not None:
                out.append(body)
        out.append(app_secret)
        return "".join(out)

    @staticmethod
    def sign(
        *,
        path: str,
        query: Sequence[tuple[str, str]],
        content_type: str | None,
        body: bytes | str | None,
        app_secret: str,
    ) -> str:
        """Lowercase hex HMAC-SHA256 of :meth:`string_to_sign`, keyed with the app secret."""
        text = Signer.string_to_sign(
            path=path, query=query, content_type=content_type, body=body, app_secret=app_secret
        )
        return hmac.new(app_secret.encode("utf-8"), text.encode("utf-8"), hashlib.sha256).hexdigest()


_PARAM = re.compile(r"^\{[^}]+\}$")


class _Matcher:
    __slots__ = ("op", "method", "literals", "regex")

    def __init__(self, op: dict[str, Any]) -> None:
        self.op = op
        self.method = op["method"].upper()
        segs = op["path"].split("/")
        self.literals = sum(1 for s in segs if not _PARAM.match(s))
        self.regex = re.compile("^" + "/".join("[^/]+" if _PARAM.match(s) else re.escape(s) for s in segs) + "$")


_MATCHERS = [_Matcher(op) for op in OPERATIONS]


def operation_for(method: str, path: str) -> dict[str, Any] | None:
    """The operation for ``method`` and ``path``; the template with the most literal segments wins."""
    m = method.upper()
    best: _Matcher | None = None
    for x in _MATCHERS:
        if x.method == m and x.regex.match(path) and (best is None or x.literals > best.literals):
            best = x
    return best.op if best else None


def requires_shop_cipher(method: str, path: str) -> bool:
    """Whether the operation matching ``method`` and ``path`` takes a ``shop_cipher`` query parameter."""
    op = operation_for(method, path)
    return bool(op and op["requiresShopCipher"])
