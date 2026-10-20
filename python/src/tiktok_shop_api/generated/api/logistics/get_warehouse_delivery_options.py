from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_warehouse_delivery_options_response import GetWarehouseDeliveryOptionsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    warehouse_id: str,
    *,
    scope: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["scope"] = scope

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/logistics/202309/warehouses/{warehouse_id}/delivery_options".format(
            warehouse_id=quote(str(warehouse_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetWarehouseDeliveryOptionsResponse | None:
    if response.status_code == 200:
        response_200 = GetWarehouseDeliveryOptionsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetWarehouseDeliveryOptionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    warehouse_id: str,
    *,
    client: AuthenticatedClient | Client,
    scope: str | Unset = UNSET,
) -> Response[GetWarehouseDeliveryOptionsResponse]:
    """Get Warehouse Delivery Options

     This API is used to obtain a list of delivery options available through the seller's designated
    warehouse.

    Args:
        warehouse_id (str):
        scope (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWarehouseDeliveryOptionsResponse]
    """

    kwargs = _get_kwargs(
        warehouse_id=warehouse_id,
        scope=scope,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    warehouse_id: str,
    *,
    client: AuthenticatedClient | Client,
    scope: str | Unset = UNSET,
) -> GetWarehouseDeliveryOptionsResponse | None:
    """Get Warehouse Delivery Options

     This API is used to obtain a list of delivery options available through the seller's designated
    warehouse.

    Args:
        warehouse_id (str):
        scope (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWarehouseDeliveryOptionsResponse
    """

    return sync_detailed(
        warehouse_id=warehouse_id,
        client=client,
        scope=scope,
    ).parsed


async def asyncio_detailed(
    warehouse_id: str,
    *,
    client: AuthenticatedClient | Client,
    scope: str | Unset = UNSET,
) -> Response[GetWarehouseDeliveryOptionsResponse]:
    """Get Warehouse Delivery Options

     This API is used to obtain a list of delivery options available through the seller's designated
    warehouse.

    Args:
        warehouse_id (str):
        scope (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWarehouseDeliveryOptionsResponse]
    """

    kwargs = _get_kwargs(
        warehouse_id=warehouse_id,
        scope=scope,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    warehouse_id: str,
    *,
    client: AuthenticatedClient | Client,
    scope: str | Unset = UNSET,
) -> GetWarehouseDeliveryOptionsResponse | None:
    """Get Warehouse Delivery Options

     This API is used to obtain a list of delivery options available through the seller's designated
    warehouse.

    Args:
        warehouse_id (str):
        scope (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWarehouseDeliveryOptionsResponse
    """

    return (
        await asyncio_detailed(
            warehouse_id=warehouse_id,
            client=client,
            scope=scope,
        )
    ).parsed
