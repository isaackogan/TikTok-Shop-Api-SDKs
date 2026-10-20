from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.search_open_collaboration_products_request import SearchOpenCollaborationProductsRequest
from ...models.search_open_collaboration_products_response import SearchOpenCollaborationProductsResponse
from ...models.search_open_collaboration_products_sort_field import SearchOpenCollaborationProductsSortField
from ...models.search_open_collaboration_products_sort_order import SearchOpenCollaborationProductsSortOrder
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: SearchOpenCollaborationProductsRequest | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int,
    sort_field: SearchOpenCollaborationProductsSortField | Unset = UNSET,
    sort_order: SearchOpenCollaborationProductsSortOrder | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["page_token"] = page_token

    params["page_size"] = page_size

    json_sort_field: str | Unset = UNSET
    if not isinstance(sort_field, Unset):
        json_sort_field = sort_field.value

    params["sort_field"] = json_sort_field

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sort_order"] = json_sort_order


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_creator/202405/open_collaborations/products/search",
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchOpenCollaborationProductsResponse | None:
    if response.status_code == 200:
        response_200 = SearchOpenCollaborationProductsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SearchOpenCollaborationProductsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchOpenCollaborationProductsRequest | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int,
    sort_field: SearchOpenCollaborationProductsSortField | Unset = UNSET,
    sort_order: SearchOpenCollaborationProductsSortOrder | Unset = UNSET,

) -> Response[SearchOpenCollaborationProductsResponse]:
    """ Search Open Collaboration Products

     This API is used to search the information of products with open collaboration by category,
    commission rate, and keywords. It will return all products on the TikTok Shop Affiliate Product
    Marketplace that are in an open collaboration.
    Creators can only search for open collaboration within the regions they are registered in the
    affiliate.

    Args:
        page_token (str | Unset):
        page_size (int):
        sort_field (SearchOpenCollaborationProductsSortField | Unset):
        sort_order (SearchOpenCollaborationProductsSortOrder | Unset):
        body (SearchOpenCollaborationProductsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchOpenCollaborationProductsResponse]
     """


    kwargs = _get_kwargs(
        body=body,
page_token=page_token,
page_size=page_size,
sort_field=sort_field,
sort_order=sort_order,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SearchOpenCollaborationProductsRequest | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int,
    sort_field: SearchOpenCollaborationProductsSortField | Unset = UNSET,
    sort_order: SearchOpenCollaborationProductsSortOrder | Unset = UNSET,

) -> SearchOpenCollaborationProductsResponse | None:
    """ Search Open Collaboration Products

     This API is used to search the information of products with open collaboration by category,
    commission rate, and keywords. It will return all products on the TikTok Shop Affiliate Product
    Marketplace that are in an open collaboration.
    Creators can only search for open collaboration within the regions they are registered in the
    affiliate.

    Args:
        page_token (str | Unset):
        page_size (int):
        sort_field (SearchOpenCollaborationProductsSortField | Unset):
        sort_order (SearchOpenCollaborationProductsSortOrder | Unset):
        body (SearchOpenCollaborationProductsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchOpenCollaborationProductsResponse
     """


    return sync_detailed(
        client=client,
body=body,
page_token=page_token,
page_size=page_size,
sort_field=sort_field,
sort_order=sort_order,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchOpenCollaborationProductsRequest | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int,
    sort_field: SearchOpenCollaborationProductsSortField | Unset = UNSET,
    sort_order: SearchOpenCollaborationProductsSortOrder | Unset = UNSET,

) -> Response[SearchOpenCollaborationProductsResponse]:
    """ Search Open Collaboration Products

     This API is used to search the information of products with open collaboration by category,
    commission rate, and keywords. It will return all products on the TikTok Shop Affiliate Product
    Marketplace that are in an open collaboration.
    Creators can only search for open collaboration within the regions they are registered in the
    affiliate.

    Args:
        page_token (str | Unset):
        page_size (int):
        sort_field (SearchOpenCollaborationProductsSortField | Unset):
        sort_order (SearchOpenCollaborationProductsSortOrder | Unset):
        body (SearchOpenCollaborationProductsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchOpenCollaborationProductsResponse]
     """


    kwargs = _get_kwargs(
        body=body,
page_token=page_token,
page_size=page_size,
sort_field=sort_field,
sort_order=sort_order,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchOpenCollaborationProductsRequest | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int,
    sort_field: SearchOpenCollaborationProductsSortField | Unset = UNSET,
    sort_order: SearchOpenCollaborationProductsSortOrder | Unset = UNSET,

) -> SearchOpenCollaborationProductsResponse | None:
    """ Search Open Collaboration Products

     This API is used to search the information of products with open collaboration by category,
    commission rate, and keywords. It will return all products on the TikTok Shop Affiliate Product
    Marketplace that are in an open collaboration.
    Creators can only search for open collaboration within the regions they are registered in the
    affiliate.

    Args:
        page_token (str | Unset):
        page_size (int):
        sort_field (SearchOpenCollaborationProductsSortField | Unset):
        sort_order (SearchOpenCollaborationProductsSortOrder | Unset):
        body (SearchOpenCollaborationProductsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchOpenCollaborationProductsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
page_token=page_token,
page_size=page_size,
sort_field=sort_field,
sort_order=sort_order,

    )).parsed
