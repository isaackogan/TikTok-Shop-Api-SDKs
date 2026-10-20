from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_shop_group_and_related_shops_response import GetShopGroupAndRelatedShopsResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/seller/202601/shop_groups",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetShopGroupAndRelatedShopsResponse | None:
    if response.status_code == 200:
        response_200 = GetShopGroupAndRelatedShopsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetShopGroupAndRelatedShopsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetShopGroupAndRelatedShopsResponse]:
    """Get Shop Group and Related Shops

     Retrieves the product interoperability group and related shops for the authenticated shop. For
    example, a group can include a U.S. shop and a Mexico shop.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopGroupAndRelatedShopsResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> GetShopGroupAndRelatedShopsResponse | None:
    """Get Shop Group and Related Shops

     Retrieves the product interoperability group and related shops for the authenticated shop. For
    example, a group can include a U.S. shop and a Mexico shop.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopGroupAndRelatedShopsResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetShopGroupAndRelatedShopsResponse]:
    """Get Shop Group and Related Shops

     Retrieves the product interoperability group and related shops for the authenticated shop. For
    example, a group can include a U.S. shop and a Mexico shop.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopGroupAndRelatedShopsResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> GetShopGroupAndRelatedShopsResponse | None:
    """Get Shop Group and Related Shops

     Retrieves the product interoperability group and related shops for the authenticated shop. For
    example, a group can include a U.S. shop and a Mexico shop.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopGroupAndRelatedShopsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
