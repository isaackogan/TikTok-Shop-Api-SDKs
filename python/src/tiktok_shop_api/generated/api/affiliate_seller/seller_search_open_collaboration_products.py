from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.seller_search_open_collaboration_products_request import SellerSearchOpenCollaborationProductsRequest
from ...models.seller_search_open_collaboration_products_response import SellerSearchOpenCollaborationProductsResponse
from ...models.seller_search_open_collaboration_products_sort_field import SellerSearchOpenCollaborationProductsSortField
from ...models.seller_search_open_collaboration_products_sort_order import SellerSearchOpenCollaborationProductsSortOrder
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: SellerSearchOpenCollaborationProductsRequest | Unset = UNSET,
    sort_order: SellerSearchOpenCollaborationProductsSortOrder | Unset = UNSET,
    sort_field: SellerSearchOpenCollaborationProductsSortField | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sort_order"] = json_sort_order

    json_sort_field: str | Unset = UNSET
    if not isinstance(sort_field, Unset):
        json_sort_field = sort_field.value

    params["sort_field"] = json_sort_field

    params["page_token"] = page_token

    params["page_size"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_seller/202405/open_collaborations/products/search",
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SellerSearchOpenCollaborationProductsResponse | None:
    if response.status_code == 200:
        response_200 = SellerSearchOpenCollaborationProductsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SellerSearchOpenCollaborationProductsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SellerSearchOpenCollaborationProductsRequest | Unset = UNSET,
    sort_order: SellerSearchOpenCollaborationProductsSortOrder | Unset = UNSET,
    sort_field: SellerSearchOpenCollaborationProductsSortField | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int,

) -> Response[SellerSearchOpenCollaborationProductsResponse]:
    """ Seller Search Open Collaboration Products

     Searches for open-collaboration products on the TikTok Shop Affiliate Product Marketplace within the
    regions where the seller is registered to sell. Category, commission rate, sales price, and title
    keyword filters are optional. When multiple filter groups are supplied, a product must match every
    supplied group. When none of these filter groups is supplied, no filter from these groups is
    applied; results remain scoped to eligible open-collaboration products in the seller's registered
    regions and are returned through pagination.

    Args:
        sort_order (SellerSearchOpenCollaborationProductsSortOrder | Unset):
        sort_field (SellerSearchOpenCollaborationProductsSortField | Unset):
        page_token (str | Unset):
        page_size (int):
        body (SellerSearchOpenCollaborationProductsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SellerSearchOpenCollaborationProductsResponse]
     """


    kwargs = _get_kwargs(
        body=body,
sort_order=sort_order,
sort_field=sort_field,
page_token=page_token,
page_size=page_size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SellerSearchOpenCollaborationProductsRequest | Unset = UNSET,
    sort_order: SellerSearchOpenCollaborationProductsSortOrder | Unset = UNSET,
    sort_field: SellerSearchOpenCollaborationProductsSortField | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int,

) -> SellerSearchOpenCollaborationProductsResponse | None:
    """ Seller Search Open Collaboration Products

     Searches for open-collaboration products on the TikTok Shop Affiliate Product Marketplace within the
    regions where the seller is registered to sell. Category, commission rate, sales price, and title
    keyword filters are optional. When multiple filter groups are supplied, a product must match every
    supplied group. When none of these filter groups is supplied, no filter from these groups is
    applied; results remain scoped to eligible open-collaboration products in the seller's registered
    regions and are returned through pagination.

    Args:
        sort_order (SellerSearchOpenCollaborationProductsSortOrder | Unset):
        sort_field (SellerSearchOpenCollaborationProductsSortField | Unset):
        page_token (str | Unset):
        page_size (int):
        body (SellerSearchOpenCollaborationProductsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SellerSearchOpenCollaborationProductsResponse
     """


    return sync_detailed(
        client=client,
body=body,
sort_order=sort_order,
sort_field=sort_field,
page_token=page_token,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SellerSearchOpenCollaborationProductsRequest | Unset = UNSET,
    sort_order: SellerSearchOpenCollaborationProductsSortOrder | Unset = UNSET,
    sort_field: SellerSearchOpenCollaborationProductsSortField | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int,

) -> Response[SellerSearchOpenCollaborationProductsResponse]:
    """ Seller Search Open Collaboration Products

     Searches for open-collaboration products on the TikTok Shop Affiliate Product Marketplace within the
    regions where the seller is registered to sell. Category, commission rate, sales price, and title
    keyword filters are optional. When multiple filter groups are supplied, a product must match every
    supplied group. When none of these filter groups is supplied, no filter from these groups is
    applied; results remain scoped to eligible open-collaboration products in the seller's registered
    regions and are returned through pagination.

    Args:
        sort_order (SellerSearchOpenCollaborationProductsSortOrder | Unset):
        sort_field (SellerSearchOpenCollaborationProductsSortField | Unset):
        page_token (str | Unset):
        page_size (int):
        body (SellerSearchOpenCollaborationProductsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SellerSearchOpenCollaborationProductsResponse]
     """


    kwargs = _get_kwargs(
        body=body,
sort_order=sort_order,
sort_field=sort_field,
page_token=page_token,
page_size=page_size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SellerSearchOpenCollaborationProductsRequest | Unset = UNSET,
    sort_order: SellerSearchOpenCollaborationProductsSortOrder | Unset = UNSET,
    sort_field: SellerSearchOpenCollaborationProductsSortField | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int,

) -> SellerSearchOpenCollaborationProductsResponse | None:
    """ Seller Search Open Collaboration Products

     Searches for open-collaboration products on the TikTok Shop Affiliate Product Marketplace within the
    regions where the seller is registered to sell. Category, commission rate, sales price, and title
    keyword filters are optional. When multiple filter groups are supplied, a product must match every
    supplied group. When none of these filter groups is supplied, no filter from these groups is
    applied; results remain scoped to eligible open-collaboration products in the seller's registered
    regions and are returned through pagination.

    Args:
        sort_order (SellerSearchOpenCollaborationProductsSortOrder | Unset):
        sort_field (SellerSearchOpenCollaborationProductsSortField | Unset):
        page_token (str | Unset):
        page_size (int):
        body (SellerSearchOpenCollaborationProductsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SellerSearchOpenCollaborationProductsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
sort_order=sort_order,
sort_field=sort_field,
page_token=page_token,
page_size=page_size,

    )).parsed
