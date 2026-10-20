from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_shop_products_response import GetShopProductsResponse
from ...models.get_shop_products_sort_field import GetShopProductsSortField
from ...models.get_shop_products_sort_order import GetShopProductsSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    title_keyword: str | Unset = UNSET,
    sort_field: GetShopProductsSortField | Unset = UNSET,
    sort_order: GetShopProductsSortOrder | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["title_keyword"] = title_keyword

    json_sort_field: str | Unset = UNSET
    if not isinstance(sort_field, Unset):
        json_sort_field = sort_field.value

    params["sort_field"] = json_sort_field

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sort_order"] = json_sort_order

    params["page_size"] = page_size

    params["page_token"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/affiliate_creator/202509/shop_products",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetShopProductsResponse | None:
    if response.status_code == 200:
        response_200 = GetShopProductsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetShopProductsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    title_keyword: str | Unset = UNSET,
    sort_field: GetShopProductsSortField | Unset = UNSET,
    sort_order: GetShopProductsSortOrder | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,
) -> Response[GetShopProductsResponse]:
    """Get Shop Products

     Searches for products in the shop bound to the authenticated creator. Optionally use `title_keyword`
    to filter products by title. The creator must have a bound shop before calling this API.

    Args:
        title_keyword (str | Unset):
        sort_field (GetShopProductsSortField | Unset):
        sort_order (GetShopProductsSortOrder | Unset):
        page_size (int):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopProductsResponse]
    """

    kwargs = _get_kwargs(
        title_keyword=title_keyword,
        sort_field=sort_field,
        sort_order=sort_order,
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
    title_keyword: str | Unset = UNSET,
    sort_field: GetShopProductsSortField | Unset = UNSET,
    sort_order: GetShopProductsSortOrder | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,
) -> GetShopProductsResponse | None:
    """Get Shop Products

     Searches for products in the shop bound to the authenticated creator. Optionally use `title_keyword`
    to filter products by title. The creator must have a bound shop before calling this API.

    Args:
        title_keyword (str | Unset):
        sort_field (GetShopProductsSortField | Unset):
        sort_order (GetShopProductsSortOrder | Unset):
        page_size (int):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopProductsResponse
    """

    return sync_detailed(
        client=client,
        title_keyword=title_keyword,
        sort_field=sort_field,
        sort_order=sort_order,
        page_size=page_size,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    title_keyword: str | Unset = UNSET,
    sort_field: GetShopProductsSortField | Unset = UNSET,
    sort_order: GetShopProductsSortOrder | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,
) -> Response[GetShopProductsResponse]:
    """Get Shop Products

     Searches for products in the shop bound to the authenticated creator. Optionally use `title_keyword`
    to filter products by title. The creator must have a bound shop before calling this API.

    Args:
        title_keyword (str | Unset):
        sort_field (GetShopProductsSortField | Unset):
        sort_order (GetShopProductsSortOrder | Unset):
        page_size (int):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopProductsResponse]
    """

    kwargs = _get_kwargs(
        title_keyword=title_keyword,
        sort_field=sort_field,
        sort_order=sort_order,
        page_size=page_size,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    title_keyword: str | Unset = UNSET,
    sort_field: GetShopProductsSortField | Unset = UNSET,
    sort_order: GetShopProductsSortOrder | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,
) -> GetShopProductsResponse | None:
    """Get Shop Products

     Searches for products in the shop bound to the authenticated creator. Optionally use `title_keyword`
    to filter products by title. The creator must have a bound shop before calling this API.

    Args:
        title_keyword (str | Unset):
        sort_field (GetShopProductsSortField | Unset):
        sort_order (GetShopProductsSortOrder | Unset):
        page_size (int):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopProductsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            title_keyword=title_keyword,
            sort_field=sort_field,
            sort_order=sort_order,
            page_size=page_size,
            page_token=page_token,
        )
    ).parsed
