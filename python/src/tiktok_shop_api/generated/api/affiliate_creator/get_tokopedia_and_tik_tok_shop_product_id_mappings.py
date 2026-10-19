from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_tokopedia_and_tik_tok_shop_product_id_mappings_request import (
    GetTokopediaAndTikTokShopProductIDMappingsRequest,
)
from ...models.get_tokopedia_and_tik_tok_shop_product_id_mappings_response import (
    GetTokopediaAndTikTokShopProductIDMappingsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: GetTokopediaAndTikTokShopProductIDMappingsRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_creator/202607/map_toko_product",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetTokopediaAndTikTokShopProductIDMappingsResponse | None:
    if response.status_code == 200:
        response_200 = GetTokopediaAndTikTokShopProductIDMappingsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetTokopediaAndTikTokShopProductIDMappingsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetTokopediaAndTikTokShopProductIDMappingsRequest | Unset = UNSET,
) -> Response[GetTokopediaAndTikTokShopProductIDMappingsResponse]:
    """Get Tokopedia and TikTok Shop Product ID Mappings

     Returns mappings from the specified Tokopedia product IDs to the corresponding TikTok Shop product
    IDs.

    Args:
        body (GetTokopediaAndTikTokShopProductIDMappingsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTokopediaAndTikTokShopProductIDMappingsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: GetTokopediaAndTikTokShopProductIDMappingsRequest | Unset = UNSET,
) -> GetTokopediaAndTikTokShopProductIDMappingsResponse | None:
    """Get Tokopedia and TikTok Shop Product ID Mappings

     Returns mappings from the specified Tokopedia product IDs to the corresponding TikTok Shop product
    IDs.

    Args:
        body (GetTokopediaAndTikTokShopProductIDMappingsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTokopediaAndTikTokShopProductIDMappingsResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetTokopediaAndTikTokShopProductIDMappingsRequest | Unset = UNSET,
) -> Response[GetTokopediaAndTikTokShopProductIDMappingsResponse]:
    """Get Tokopedia and TikTok Shop Product ID Mappings

     Returns mappings from the specified Tokopedia product IDs to the corresponding TikTok Shop product
    IDs.

    Args:
        body (GetTokopediaAndTikTokShopProductIDMappingsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTokopediaAndTikTokShopProductIDMappingsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GetTokopediaAndTikTokShopProductIDMappingsRequest | Unset = UNSET,
) -> GetTokopediaAndTikTokShopProductIDMappingsResponse | None:
    """Get Tokopedia and TikTok Shop Product ID Mappings

     Returns mappings from the specified Tokopedia product IDs to the corresponding TikTok Shop product
    IDs.

    Args:
        body (GetTokopediaAndTikTokShopProductIDMappingsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTokopediaAndTikTokShopProductIDMappingsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
