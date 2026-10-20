from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_global_seller_warehouses_response import GetGlobalSellerWarehousesResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/logistics/202309/global_warehouses",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetGlobalSellerWarehousesResponse | None:
    if response.status_code == 200:
        response_200 = GetGlobalSellerWarehousesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetGlobalSellerWarehousesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetGlobalSellerWarehousesResponse]:
    """Get Global Seller Warehouses

     This API retrieves global warehouses associated with the seller, including each warehouse's global
    warehouse ID, name, and ownership.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGlobalSellerWarehousesResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> GetGlobalSellerWarehousesResponse | None:
    """Get Global Seller Warehouses

     This API retrieves global warehouses associated with the seller, including each warehouse's global
    warehouse ID, name, and ownership.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGlobalSellerWarehousesResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetGlobalSellerWarehousesResponse]:
    """Get Global Seller Warehouses

     This API retrieves global warehouses associated with the seller, including each warehouse's global
    warehouse ID, name, and ownership.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGlobalSellerWarehousesResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> GetGlobalSellerWarehousesResponse | None:
    """Get Global Seller Warehouses

     This API retrieves global warehouses associated with the seller, including each warehouse's global
    warehouse ID, name, and ownership.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGlobalSellerWarehousesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
