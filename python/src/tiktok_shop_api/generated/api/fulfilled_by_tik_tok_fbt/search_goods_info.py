from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.search_goods_info_request import SearchGoodsInfoRequest
from ...models.search_goods_info_response import SearchGoodsInfoResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: SearchGoodsInfoRequest | Unset = UNSET,
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
        "url": "/fbt/202607/goods/search",
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchGoodsInfoResponse | None:
    if response.status_code == 200:
        response_200 = SearchGoodsInfoResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SearchGoodsInfoResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchGoodsInfoRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,

) -> Response[SearchGoodsInfoResponse]:
    """ Search Goods Info

     Retrieves goods belonging to the merchant that match the specified filters and returns their IDs,
    names, goods-SKU relationships, merchant-declared measurements, warehouse-confirmed measurements,
    and other attributes. When more than one of `goods_ids`, `product_ids`, `reference_codes`, and
    `sku_ids` is provided, the API returns only goods that match all provided filter fields. If all four
    filters are empty or omitted, the API returns the merchant's goods in descending creation-time
    order, limited by `page_size`.

    Args:
        page_size (int):
        page_token (str | Unset):
        body (SearchGoodsInfoRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchGoodsInfoResponse]
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
    body: SearchGoodsInfoRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,

) -> SearchGoodsInfoResponse | None:
    """ Search Goods Info

     Retrieves goods belonging to the merchant that match the specified filters and returns their IDs,
    names, goods-SKU relationships, merchant-declared measurements, warehouse-confirmed measurements,
    and other attributes. When more than one of `goods_ids`, `product_ids`, `reference_codes`, and
    `sku_ids` is provided, the API returns only goods that match all provided filter fields. If all four
    filters are empty or omitted, the API returns the merchant's goods in descending creation-time
    order, limited by `page_size`.

    Args:
        page_size (int):
        page_token (str | Unset):
        body (SearchGoodsInfoRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchGoodsInfoResponse
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
    body: SearchGoodsInfoRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,

) -> Response[SearchGoodsInfoResponse]:
    """ Search Goods Info

     Retrieves goods belonging to the merchant that match the specified filters and returns their IDs,
    names, goods-SKU relationships, merchant-declared measurements, warehouse-confirmed measurements,
    and other attributes. When more than one of `goods_ids`, `product_ids`, `reference_codes`, and
    `sku_ids` is provided, the API returns only goods that match all provided filter fields. If all four
    filters are empty or omitted, the API returns the merchant's goods in descending creation-time
    order, limited by `page_size`.

    Args:
        page_size (int):
        page_token (str | Unset):
        body (SearchGoodsInfoRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchGoodsInfoResponse]
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
    body: SearchGoodsInfoRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,

) -> SearchGoodsInfoResponse | None:
    """ Search Goods Info

     Retrieves goods belonging to the merchant that match the specified filters and returns their IDs,
    names, goods-SKU relationships, merchant-declared measurements, warehouse-confirmed measurements,
    and other attributes. When more than one of `goods_ids`, `product_ids`, `reference_codes`, and
    `sku_ids` is provided, the API returns only goods that match all provided filter fields. If all four
    filters are empty or omitted, the API returns the merchant's goods in descending creation-time
    order, limited by `page_size`.

    Args:
        page_size (int):
        page_token (str | Unset):
        body (SearchGoodsInfoRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchGoodsInfoResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
page_size=page_size,
page_token=page_token,

    )).parsed
