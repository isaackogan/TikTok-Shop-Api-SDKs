from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_order_price_details_response import GetOrderPriceDetailsResponse
from typing import cast



def _get_kwargs(
    order_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/order/202407/orders/{order_id}/price_detail".format(order_id=quote(str(order_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetOrderPriceDetailsResponse | None:
    if response.status_code == 200:
        response_200 = GetOrderPriceDetailsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetOrderPriceDetailsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetOrderPriceDetailsResponse]:
    """ Get Order Price Details

     Get the detailed pricing calculation information of an order or a line item, including vouchers,
    tax, etc.

    Args:
        order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrderPriceDetailsResponse]
     """


    kwargs = _get_kwargs(
        order_id=order_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> GetOrderPriceDetailsResponse | None:
    """ Get Order Price Details

     Get the detailed pricing calculation information of an order or a line item, including vouchers,
    tax, etc.

    Args:
        order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOrderPriceDetailsResponse
     """


    return sync_detailed(
        order_id=order_id,
client=client,

    ).parsed

async def asyncio_detailed(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetOrderPriceDetailsResponse]:
    """ Get Order Price Details

     Get the detailed pricing calculation information of an order or a line item, including vouchers,
    tax, etc.

    Args:
        order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrderPriceDetailsResponse]
     """


    kwargs = _get_kwargs(
        order_id=order_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> GetOrderPriceDetailsResponse | None:
    """ Get Order Price Details

     Get the detailed pricing calculation information of an order or a line item, including vouchers,
    tax, etc.

    Args:
        order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOrderPriceDetailsResponse
     """


    return (await asyncio_detailed(
        order_id=order_id,
client=client,

    )).parsed
