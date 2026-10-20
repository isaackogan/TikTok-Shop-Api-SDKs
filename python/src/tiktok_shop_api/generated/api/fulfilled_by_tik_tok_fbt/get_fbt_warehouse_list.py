from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_fbt_warehouse_list_response import GetFBTWarehouseListResponse
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fbt/202408/warehouses",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetFBTWarehouseListResponse | None:
    if response.status_code == 200:
        response_200 = GetFBTWarehouseListResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetFBTWarehouseListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetFBTWarehouseListResponse]:
    """ Get FBT Warehouse List

     This API is used to retrieve all Fulfilled by TikTok warehouse information including the warehouse
    name, warehouse address information, etc. The IDs of subscribed warehouses can be used to query
    inventory-related information.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFBTWarehouseListResponse]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> GetFBTWarehouseListResponse | None:
    """ Get FBT Warehouse List

     This API is used to retrieve all Fulfilled by TikTok warehouse information including the warehouse
    name, warehouse address information, etc. The IDs of subscribed warehouses can be used to query
    inventory-related information.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFBTWarehouseListResponse
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetFBTWarehouseListResponse]:
    """ Get FBT Warehouse List

     This API is used to retrieve all Fulfilled by TikTok warehouse information including the warehouse
    name, warehouse address information, etc. The IDs of subscribed warehouses can be used to query
    inventory-related information.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFBTWarehouseListResponse]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> GetFBTWarehouseListResponse | None:
    """ Get FBT Warehouse List

     This API is used to retrieve all Fulfilled by TikTok warehouse information including the warehouse
    name, warehouse address information, etc. The IDs of subscribed warehouses can be used to query
    inventory-related information.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFBTWarehouseListResponse
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
