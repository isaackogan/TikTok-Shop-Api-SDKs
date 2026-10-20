from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.inventory_search_request import InventorySearchRequest
from ...models.inventory_search_response import InventorySearchResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: InventorySearchRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202309/inventory/search",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InventorySearchResponse | None:
    if response.status_code == 200:
        response_200 = InventorySearchResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InventorySearchResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: InventorySearchRequest | Unset = UNSET,

) -> Response[InventorySearchResponse]:
    """ Inventory Search

     Retrieve inventory information for multiple products or SKUs.
    **Note**:
    - If both `sku_ids` and `product_ids` are passed, `sku_ids` takes precedence and `product_ids` is
    ignored.
    - Passing product IDs returns the inventory information of all SKUs under the specified products.
    - Passing SKU IDs returns the inventory information for the specified SKUs.

    Args:
        body (InventorySearchRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InventorySearchResponse]
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
    body: InventorySearchRequest | Unset = UNSET,

) -> InventorySearchResponse | None:
    """ Inventory Search

     Retrieve inventory information for multiple products or SKUs.
    **Note**:
    - If both `sku_ids` and `product_ids` are passed, `sku_ids` takes precedence and `product_ids` is
    ignored.
    - Passing product IDs returns the inventory information of all SKUs under the specified products.
    - Passing SKU IDs returns the inventory information for the specified SKUs.

    Args:
        body (InventorySearchRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InventorySearchResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: InventorySearchRequest | Unset = UNSET,

) -> Response[InventorySearchResponse]:
    """ Inventory Search

     Retrieve inventory information for multiple products or SKUs.
    **Note**:
    - If both `sku_ids` and `product_ids` are passed, `sku_ids` takes precedence and `product_ids` is
    ignored.
    - Passing product IDs returns the inventory information of all SKUs under the specified products.
    - Passing SKU IDs returns the inventory information for the specified SKUs.

    Args:
        body (InventorySearchRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InventorySearchResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: InventorySearchRequest | Unset = UNSET,

) -> InventorySearchResponse | None:
    """ Inventory Search

     Retrieve inventory information for multiple products or SKUs.
    **Note**:
    - If both `sku_ids` and `product_ids` are passed, `sku_ids` takes precedence and `product_ids` is
    ignored.
    - Passing product IDs returns the inventory information of all SKUs under the specified products.
    - Passing SKU IDs returns the inventory information for the specified SKUs.

    Args:
        body (InventorySearchRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InventorySearchResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
