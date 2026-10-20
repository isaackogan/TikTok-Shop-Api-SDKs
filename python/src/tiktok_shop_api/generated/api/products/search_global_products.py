from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.search_global_products_request import SearchGlobalProductsRequest
from ...models.search_global_products_response import SearchGlobalProductsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: SearchGlobalProductsRequest | Unset = UNSET,
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
        "url": "/product/202312/global_products/search",
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchGlobalProductsResponse | None:
    if response.status_code == 200:
        response_200 = SearchGlobalProductsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SearchGlobalProductsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchGlobalProductsRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,

) -> Response[SearchGlobalProductsResponse]:
    """ Search Global Products

     Retrieve a list of global products that meet the specified conditions. Results are sorted by
    creation time in descending order. This API returns only key product properties. To obtain more
    details, pass a returned global product ID to the [Get Global Product
    API](https://partner.tiktokshop.com/docv2/page/6509e2b0bace3e02b7490c96).

    Args:
        page_size (int):
        page_token (str | Unset):
        body (SearchGlobalProductsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchGlobalProductsResponse]
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
    body: SearchGlobalProductsRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,

) -> SearchGlobalProductsResponse | None:
    """ Search Global Products

     Retrieve a list of global products that meet the specified conditions. Results are sorted by
    creation time in descending order. This API returns only key product properties. To obtain more
    details, pass a returned global product ID to the [Get Global Product
    API](https://partner.tiktokshop.com/docv2/page/6509e2b0bace3e02b7490c96).

    Args:
        page_size (int):
        page_token (str | Unset):
        body (SearchGlobalProductsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchGlobalProductsResponse
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
    body: SearchGlobalProductsRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,

) -> Response[SearchGlobalProductsResponse]:
    """ Search Global Products

     Retrieve a list of global products that meet the specified conditions. Results are sorted by
    creation time in descending order. This API returns only key product properties. To obtain more
    details, pass a returned global product ID to the [Get Global Product
    API](https://partner.tiktokshop.com/docv2/page/6509e2b0bace3e02b7490c96).

    Args:
        page_size (int):
        page_token (str | Unset):
        body (SearchGlobalProductsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchGlobalProductsResponse]
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
    body: SearchGlobalProductsRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,

) -> SearchGlobalProductsResponse | None:
    """ Search Global Products

     Retrieve a list of global products that meet the specified conditions. Results are sorted by
    creation time in descending order. This API returns only key product properties. To obtain more
    details, pass a returned global product ID to the [Get Global Product
    API](https://partner.tiktokshop.com/docv2/page/6509e2b0bace3e02b7490c96).

    Args:
        page_size (int):
        page_token (str | Unset):
        body (SearchGlobalProductsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchGlobalProductsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
page_size=page_size,
page_token=page_token,

    )).parsed
