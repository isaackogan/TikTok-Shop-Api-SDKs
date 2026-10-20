from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.update_stock_operation_settings_request import UpdateStockOperationSettingsRequest
from ...models.update_stock_operation_settings_response import UpdateStockOperationSettingsResponse
from typing import cast



def _get_kwargs(
    *,
    body: UpdateStockOperationSettingsRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202608/inventory/operation/settings",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UpdateStockOperationSettingsResponse | None:
    if response.status_code == 200:
        response_200 = UpdateStockOperationSettingsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UpdateStockOperationSettingsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateStockOperationSettingsRequest,

) -> Response[UpdateStockOperationSettingsResponse]:
    """ Update Stock Operation Settings

     Configure auto-restock behavior for 1 to 500 SKUs in one request. For seller-fulfilled orders, this
    setting controls whether inventory reserved for a canceled order is returned to the SKU's available
    inventory.

    Args:
        body (UpdateStockOperationSettingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateStockOperationSettingsResponse]
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
    body: UpdateStockOperationSettingsRequest,

) -> UpdateStockOperationSettingsResponse | None:
    """ Update Stock Operation Settings

     Configure auto-restock behavior for 1 to 500 SKUs in one request. For seller-fulfilled orders, this
    setting controls whether inventory reserved for a canceled order is returned to the SKU's available
    inventory.

    Args:
        body (UpdateStockOperationSettingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateStockOperationSettingsResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateStockOperationSettingsRequest,

) -> Response[UpdateStockOperationSettingsResponse]:
    """ Update Stock Operation Settings

     Configure auto-restock behavior for 1 to 500 SKUs in one request. For seller-fulfilled orders, this
    setting controls whether inventory reserved for a canceled order is returned to the SKU's available
    inventory.

    Args:
        body (UpdateStockOperationSettingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateStockOperationSettingsResponse]
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
    body: UpdateStockOperationSettingsRequest,

) -> UpdateStockOperationSettingsResponse | None:
    """ Update Stock Operation Settings

     Configure auto-restock behavior for 1 to 500 SKUs in one request. For seller-fulfilled orders, this
    setting controls whether inventory reserved for a canceled order is returned to the SKU's available
    inventory.

    Args:
        body (UpdateStockOperationSettingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateStockOperationSettingsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
