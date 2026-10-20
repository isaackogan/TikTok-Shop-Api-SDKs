from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.update_fbt_goods_info_request import UpdateFBTGoodsInfoRequest
from ...models.update_fbt_goods_info_response import UpdateFBTGoodsInfoResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: UpdateFBTGoodsInfoRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fbt/202607/goods/update_goods_info",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UpdateFBTGoodsInfoResponse | None:
    if response.status_code == 200:
        response_200 = UpdateFBTGoodsInfoResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UpdateFBTGoodsInfoResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateFBTGoodsInfoRequest | Unset = UNSET,

) -> Response[UpdateFBTGoodsInfoResponse]:
    """ Update FBT Goods Info

     Update FBT goods information, including goods name, image URL, dimensions, hazmat details, shelf-
    life attributes, and return address information.

    Args:
        body (UpdateFBTGoodsInfoRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateFBTGoodsInfoResponse]
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
    body: UpdateFBTGoodsInfoRequest | Unset = UNSET,

) -> UpdateFBTGoodsInfoResponse | None:
    """ Update FBT Goods Info

     Update FBT goods information, including goods name, image URL, dimensions, hazmat details, shelf-
    life attributes, and return address information.

    Args:
        body (UpdateFBTGoodsInfoRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateFBTGoodsInfoResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateFBTGoodsInfoRequest | Unset = UNSET,

) -> Response[UpdateFBTGoodsInfoResponse]:
    """ Update FBT Goods Info

     Update FBT goods information, including goods name, image URL, dimensions, hazmat details, shelf-
    life attributes, and return address information.

    Args:
        body (UpdateFBTGoodsInfoRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateFBTGoodsInfoResponse]
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
    body: UpdateFBTGoodsInfoRequest | Unset = UNSET,

) -> UpdateFBTGoodsInfoResponse | None:
    """ Update FBT Goods Info

     Update FBT goods information, including goods name, image URL, dimensions, hazmat details, shelf-
    life attributes, and return address information.

    Args:
        body (UpdateFBTGoodsInfoRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateFBTGoodsInfoResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
