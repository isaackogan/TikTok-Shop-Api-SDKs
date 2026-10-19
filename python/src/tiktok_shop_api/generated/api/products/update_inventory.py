from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_inventory_request import UpdateInventoryRequest
from ...models.update_inventory_response import UpdateInventoryResponse
from ...types import Response


def _get_kwargs(
    product_id: str,
    *,
    body: UpdateInventoryRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202309/products/{product_id}/inventory/update".format(
            product_id=quote(str(product_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UpdateInventoryResponse | None:
    if response.status_code == 200:
        response_200 = UpdateInventoryResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdateInventoryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateInventoryRequest,
) -> Response[UpdateInventoryResponse]:
    """Update Inventory

     Update the inventory quantity of SKUs belonging to a product. The product must be in `DRAFT`,
    `PENDING`, `FAILED`, `ACTIVATE`, or `SELLER_DEACTIVATED` status.

    Args:
        product_id (str):
        body (UpdateInventoryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateInventoryResponse]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateInventoryRequest,
) -> UpdateInventoryResponse | None:
    """Update Inventory

     Update the inventory quantity of SKUs belonging to a product. The product must be in `DRAFT`,
    `PENDING`, `FAILED`, `ACTIVATE`, or `SELLER_DEACTIVATED` status.

    Args:
        product_id (str):
        body (UpdateInventoryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateInventoryResponse
    """

    return sync_detailed(
        product_id=product_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateInventoryRequest,
) -> Response[UpdateInventoryResponse]:
    """Update Inventory

     Update the inventory quantity of SKUs belonging to a product. The product must be in `DRAFT`,
    `PENDING`, `FAILED`, `ACTIVATE`, or `SELLER_DEACTIVATED` status.

    Args:
        product_id (str):
        body (UpdateInventoryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateInventoryResponse]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateInventoryRequest,
) -> UpdateInventoryResponse | None:
    """Update Inventory

     Update the inventory quantity of SKUs belonging to a product. The product must be in `DRAFT`,
    `PENDING`, `FAILED`, `ACTIVATE`, or `SELLER_DEACTIVATED` status.

    Args:
        product_id (str):
        body (UpdateInventoryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateInventoryResponse
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            client=client,
            body=body,
        )
    ).parsed
