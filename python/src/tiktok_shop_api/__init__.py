"""Unofficial Python client for the TikTok Shop API (TikTok Shop Partner API)."""

from ._version import USER_AGENT, __version__
from .auth import DEFAULT_AUTH_BASE_URL, AsyncTikTokShopAuth, TikTokShopAuth, TokenSet
from .client import DEFAULT_BASE_URL, AsyncTikTokShop, TikTokShop
from .errors import TikTokShopError
from .signing import Signer, operation_for, requires_shop_cipher
from .webhooks import EVENT_TYPES, UnknownWebhookEvent, WebhookEvent, WebhookSignatureError, Webhooks

__all__ = [
    "DEFAULT_AUTH_BASE_URL",
    "DEFAULT_BASE_URL",
    "EVENT_TYPES",
    "AsyncTikTokShop",
    "AsyncTikTokShopAuth",
    "Signer",
    "TikTokShop",
    "TikTokShopAuth",
    "TikTokShopError",
    "TokenSet",
    "USER_AGENT",
    "UnknownWebhookEvent",
    "WebhookEvent",
    "WebhookSignatureError",
    "Webhooks",
    "__version__",
    "operation_for",
    "requires_shop_cipher",
]
