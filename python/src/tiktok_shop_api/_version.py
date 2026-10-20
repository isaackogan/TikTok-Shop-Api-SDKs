"""The package version, kept in step with pyproject.toml by scripts/bump-version.ts."""

__version__ = "0.1.0"

#: Sent as the ``User-Agent`` of every API and token call.
USER_AGENT = "tiktok-shop-api-python/" + __version__
