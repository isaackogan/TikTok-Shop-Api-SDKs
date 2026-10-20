from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_order_detail_response import GetOrderDetailResponse
from typing import cast



def _get_kwargs(
    *,
    ids: list[str],

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_ids = ids


    params["ids"] = json_ids


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/order/202507/orders",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetOrderDetailResponse | None:
    if response.status_code == 200:
        response_200 = GetOrderDetailResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetOrderDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    ids: list[str],

) -> Response[GetOrderDetailResponse]:
    """ Get Order Detail

     Get the detailed order information of an order, including important attributes such as order status,
    shipping addresses, payment details, price and tax info, and package information.

    Args:
        ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrderDetailResponse]
     """


    kwargs = _get_kwargs(
        ids=ids,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    ids: list[str],

) -> GetOrderDetailResponse | None:
    """ Get Order Detail

     Get the detailed order information of an order, including important attributes such as order status,
    shipping addresses, payment details, price and tax info, and package information.

    Args:
        ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOrderDetailResponse
     """


    return sync_detailed(
        client=client,
ids=ids,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    ids: list[str],

) -> Response[GetOrderDetailResponse]:
    """ Get Order Detail

     Get the detailed order information of an order, including important attributes such as order status,
    shipping addresses, payment details, price and tax info, and package information.

    Args:
        ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrderDetailResponse]
     """


    kwargs = _get_kwargs(
        ids=ids,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    ids: list[str],

) -> GetOrderDetailResponse | None:
    """ Get Order Detail

     Get the detailed order information of an order, including important attributes such as order status,
    shipping addresses, payment details, price and tax info, and package information.

    Args:
        ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOrderDetailResponse
     """


    return (await asyncio_detailed(
        client=client,
ids=ids,

    )).parsed
