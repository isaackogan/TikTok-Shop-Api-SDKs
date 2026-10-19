from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_shop_live_products_performance_list_response import GetShopLIVEProductsPerformanceListResponse
from ...models.get_shop_live_products_performance_list_sort_field import GetShopLiveProductsPerformanceListSortField
from ...models.get_shop_live_products_performance_list_sort_order import GetShopLiveProductsPerformanceListSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    live_id: str,
    *,
    sort_order: GetShopLiveProductsPerformanceListSortOrder | Unset = UNSET,
    sort_field: GetShopLiveProductsPerformanceListSortField | Unset = UNSET,
    currency: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sort_order"] = json_sort_order

    json_sort_field: str | Unset = UNSET
    if not isinstance(sort_field, Unset):
        json_sort_field = sort_field.value

    params["sort_field"] = json_sort_field

    params["currency"] = currency

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202512/shop/{live_id}/products_performance".format(
            live_id=quote(str(live_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetShopLIVEProductsPerformanceListResponse | None:
    if response.status_code == 200:
        response_200 = GetShopLIVEProductsPerformanceListResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetShopLIVEProductsPerformanceListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    live_id: str,
    *,
    client: AuthenticatedClient | Client,
    sort_order: GetShopLiveProductsPerformanceListSortOrder | Unset = UNSET,
    sort_field: GetShopLiveProductsPerformanceListSortField | Unset = UNSET,
    currency: str | Unset = UNSET,
) -> Response[GetShopLIVEProductsPerformanceListResponse]:
    """Get Shop LIVE Products Performance List

     Returns sale performance for each product in a shop-related LIVE session from the official account
    or marketing accounts.

    Args:
        live_id (str):
        sort_order (GetShopLiveProductsPerformanceListSortOrder | Unset):
        sort_field (GetShopLiveProductsPerformanceListSortField | Unset):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopLIVEProductsPerformanceListResponse]
    """

    kwargs = _get_kwargs(
        live_id=live_id,
        sort_order=sort_order,
        sort_field=sort_field,
        currency=currency,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    live_id: str,
    *,
    client: AuthenticatedClient | Client,
    sort_order: GetShopLiveProductsPerformanceListSortOrder | Unset = UNSET,
    sort_field: GetShopLiveProductsPerformanceListSortField | Unset = UNSET,
    currency: str | Unset = UNSET,
) -> GetShopLIVEProductsPerformanceListResponse | None:
    """Get Shop LIVE Products Performance List

     Returns sale performance for each product in a shop-related LIVE session from the official account
    or marketing accounts.

    Args:
        live_id (str):
        sort_order (GetShopLiveProductsPerformanceListSortOrder | Unset):
        sort_field (GetShopLiveProductsPerformanceListSortField | Unset):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopLIVEProductsPerformanceListResponse
    """

    return sync_detailed(
        live_id=live_id,
        client=client,
        sort_order=sort_order,
        sort_field=sort_field,
        currency=currency,
    ).parsed


async def asyncio_detailed(
    live_id: str,
    *,
    client: AuthenticatedClient | Client,
    sort_order: GetShopLiveProductsPerformanceListSortOrder | Unset = UNSET,
    sort_field: GetShopLiveProductsPerformanceListSortField | Unset = UNSET,
    currency: str | Unset = UNSET,
) -> Response[GetShopLIVEProductsPerformanceListResponse]:
    """Get Shop LIVE Products Performance List

     Returns sale performance for each product in a shop-related LIVE session from the official account
    or marketing accounts.

    Args:
        live_id (str):
        sort_order (GetShopLiveProductsPerformanceListSortOrder | Unset):
        sort_field (GetShopLiveProductsPerformanceListSortField | Unset):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopLIVEProductsPerformanceListResponse]
    """

    kwargs = _get_kwargs(
        live_id=live_id,
        sort_order=sort_order,
        sort_field=sort_field,
        currency=currency,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    live_id: str,
    *,
    client: AuthenticatedClient | Client,
    sort_order: GetShopLiveProductsPerformanceListSortOrder | Unset = UNSET,
    sort_field: GetShopLiveProductsPerformanceListSortField | Unset = UNSET,
    currency: str | Unset = UNSET,
) -> GetShopLIVEProductsPerformanceListResponse | None:
    """Get Shop LIVE Products Performance List

     Returns sale performance for each product in a shop-related LIVE session from the official account
    or marketing accounts.

    Args:
        live_id (str):
        sort_order (GetShopLiveProductsPerformanceListSortOrder | Unset):
        sort_field (GetShopLiveProductsPerformanceListSortField | Unset):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopLIVEProductsPerformanceListResponse
    """

    return (
        await asyncio_detailed(
            live_id=live_id,
            client=client,
            sort_order=sort_order,
            sort_field=sort_field,
            currency=currency,
        )
    ).parsed
