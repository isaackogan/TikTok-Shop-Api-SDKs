from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.search_products_request import SearchProductsRequest
from ...models.search_products_response import SearchProductsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: SearchProductsRequest | Unset = UNSET,
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
        "url": "/product/202502/products/search",
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchProductsResponse | None:
    if response.status_code == 200:
        response_200 = SearchProductsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SearchProductsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchProductsRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,

) -> Response[SearchProductsResponse]:
    """ Search Products

     Retrieve a list of products that meet the specified conditions.
    This API will only return the key product properties. You can pass a returned product ID to the [Get
    Product API](https://partner.tiktokshop.com/docv2/page/6509d85b4a0bb702c057fdda) to obtain more
    details about the product.

    Args:
        page_size (int):
        page_token (str | Unset):
        body (SearchProductsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchProductsResponse]
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
    body: SearchProductsRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,

) -> SearchProductsResponse | None:
    """ Search Products

     Retrieve a list of products that meet the specified conditions.
    This API will only return the key product properties. You can pass a returned product ID to the [Get
    Product API](https://partner.tiktokshop.com/docv2/page/6509d85b4a0bb702c057fdda) to obtain more
    details about the product.

    Args:
        page_size (int):
        page_token (str | Unset):
        body (SearchProductsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchProductsResponse
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
    body: SearchProductsRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,

) -> Response[SearchProductsResponse]:
    """ Search Products

     Retrieve a list of products that meet the specified conditions.
    This API will only return the key product properties. You can pass a returned product ID to the [Get
    Product API](https://partner.tiktokshop.com/docv2/page/6509d85b4a0bb702c057fdda) to obtain more
    details about the product.

    Args:
        page_size (int):
        page_token (str | Unset):
        body (SearchProductsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchProductsResponse]
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
    body: SearchProductsRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,

) -> SearchProductsResponse | None:
    """ Search Products

     Retrieve a list of products that meet the specified conditions.
    This API will only return the key product properties. You can pass a returned product ID to the [Get
    Product API](https://partner.tiktokshop.com/docv2/page/6509d85b4a0bb702c057fdda) to obtain more
    details about the product.

    Args:
        page_size (int):
        page_token (str | Unset):
        body (SearchProductsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchProductsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
page_size=page_size,
page_token=page_token,

    )).parsed
