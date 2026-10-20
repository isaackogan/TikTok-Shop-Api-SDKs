from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_global_inventory_request import UpdateGlobalInventoryRequest
from ...models.update_global_inventory_response import UpdateGlobalInventoryResponse
from ...types import Response


def _get_kwargs(
    global_product_id: str,
    *,
    body: UpdateGlobalInventoryRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202309/global_products/{global_product_id}/inventory/update".format(
            global_product_id=quote(str(global_product_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UpdateGlobalInventoryResponse | None:
    if response.status_code == 200:
        response_200 = UpdateGlobalInventoryResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdateGlobalInventoryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    global_product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateGlobalInventoryRequest,
) -> Response[UpdateGlobalInventoryResponse]:
    """Update Global Inventory

     Update the inventory of a global product in `DRAFT`, `UNPUBLISHED`, or `PUBLISHED` status. You must
    have access to the Multi-Warehouse feature.

    Args:
        global_product_id (str):
        body (UpdateGlobalInventoryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateGlobalInventoryResponse]
    """

    kwargs = _get_kwargs(
        global_product_id=global_product_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    global_product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateGlobalInventoryRequest,
) -> UpdateGlobalInventoryResponse | None:
    """Update Global Inventory

     Update the inventory of a global product in `DRAFT`, `UNPUBLISHED`, or `PUBLISHED` status. You must
    have access to the Multi-Warehouse feature.

    Args:
        global_product_id (str):
        body (UpdateGlobalInventoryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateGlobalInventoryResponse
    """

    return sync_detailed(
        global_product_id=global_product_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    global_product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateGlobalInventoryRequest,
) -> Response[UpdateGlobalInventoryResponse]:
    """Update Global Inventory

     Update the inventory of a global product in `DRAFT`, `UNPUBLISHED`, or `PUBLISHED` status. You must
    have access to the Multi-Warehouse feature.

    Args:
        global_product_id (str):
        body (UpdateGlobalInventoryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateGlobalInventoryResponse]
    """

    kwargs = _get_kwargs(
        global_product_id=global_product_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    global_product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateGlobalInventoryRequest,
) -> UpdateGlobalInventoryResponse | None:
    """Update Global Inventory

     Update the inventory of a global product in `DRAFT`, `UNPUBLISHED`, or `PUBLISHED` status. You must
    have access to the Multi-Warehouse feature.

    Args:
        global_product_id (str):
        body (UpdateGlobalInventoryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateGlobalInventoryResponse
    """

    return (
        await asyncio_detailed(
            global_product_id=global_product_id,
            client=client,
            body=body,
        )
    ).parsed
