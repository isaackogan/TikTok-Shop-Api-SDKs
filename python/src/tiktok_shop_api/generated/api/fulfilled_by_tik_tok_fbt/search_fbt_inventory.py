from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.search_fbt_inventory_request import SearchFBTInventoryRequest
from ...models.search_fbt_inventory_response import SearchFBTInventoryResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: SearchFBTInventoryRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["page_size"] = page_size

    params["page_token"] = page_token


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fbt/202408/inventory/search",
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchFBTInventoryResponse | None:
    if response.status_code == 200:
        response_200 = SearchFBTInventoryResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SearchFBTInventoryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchFBTInventoryRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,

) -> Response[SearchFBTInventoryResponse]:
    """ Search FBT Inventory

     This API is used to retrieve detailed inventory information for goods and matched SKUs, including
    sellable inventory, reserved inventory, unsellable inventory, and in-transit inventory at the
    warehouse level.

    Args:
        page_size (int):
        page_token (str | Unset):
        body (SearchFBTInventoryRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchFBTInventoryResponse]
     """


    kwargs = _get_kwargs(
        body=body,
page_size=page_size,
page_token=page_token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SearchFBTInventoryRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,

) -> SearchFBTInventoryResponse | None:
    """ Search FBT Inventory

     This API is used to retrieve detailed inventory information for goods and matched SKUs, including
    sellable inventory, reserved inventory, unsellable inventory, and in-transit inventory at the
    warehouse level.

    Args:
        page_size (int):
        page_token (str | Unset):
        body (SearchFBTInventoryRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchFBTInventoryResponse
     """


    return sync_detailed(
        client=client,
body=body,
page_size=page_size,
page_token=page_token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchFBTInventoryRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,

) -> Response[SearchFBTInventoryResponse]:
    """ Search FBT Inventory

     This API is used to retrieve detailed inventory information for goods and matched SKUs, including
    sellable inventory, reserved inventory, unsellable inventory, and in-transit inventory at the
    warehouse level.

    Args:
        page_size (int):
        page_token (str | Unset):
        body (SearchFBTInventoryRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchFBTInventoryResponse]
     """


    kwargs = _get_kwargs(
        body=body,
page_size=page_size,
page_token=page_token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchFBTInventoryRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,

) -> SearchFBTInventoryResponse | None:
    """ Search FBT Inventory

     This API is used to retrieve detailed inventory information for goods and matched SKUs, including
    sellable inventory, reserved inventory, unsellable inventory, and in-transit inventory at the
    warehouse level.

    Args:
        page_size (int):
        page_token (str | Unset):
        body (SearchFBTInventoryRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchFBTInventoryResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
page_size=page_size,
page_token=page_token,

    )).parsed
