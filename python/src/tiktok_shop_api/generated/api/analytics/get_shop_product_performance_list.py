from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_shop_product_performance_list_currency import GetShopProductPerformanceListCurrency
from ...models.get_shop_product_performance_list_product_status_filter import GetShopProductPerformanceListProductStatusFilter
from ...models.get_shop_product_performance_list_response import GetShopProductPerformanceListResponse
from ...models.get_shop_product_performance_list_sort_field import GetShopProductPerformanceListSortField
from ...models.get_shop_product_performance_list_sort_order import GetShopProductPerformanceListSortOrder
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    *,
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    sort_field: GetShopProductPerformanceListSortField | Unset = UNSET,
    sort_order: GetShopProductPerformanceListSortOrder | Unset = UNSET,
    currency: GetShopProductPerformanceListCurrency | Unset = UNSET,
    category_filter: list[str] | Unset = UNSET,
    product_status_filter: GetShopProductPerformanceListProductStatusFilter | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_start_date_ge = start_date_ge.isoformat()
    params["start_date_ge"] = json_start_date_ge

    json_end_date_lt = end_date_lt.isoformat()
    params["end_date_lt"] = json_end_date_lt

    params["page_size"] = page_size

    params["page_token"] = page_token

    json_sort_field: str | Unset = UNSET
    if not isinstance(sort_field, Unset):
        json_sort_field = sort_field.value

    params["sort_field"] = json_sort_field

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sort_order"] = json_sort_order

    json_currency: str | Unset = UNSET
    if not isinstance(currency, Unset):
        json_currency = currency.value

    params["currency"] = json_currency

    json_category_filter: list[str] | Unset = UNSET
    if not isinstance(category_filter, Unset):
        json_category_filter = category_filter


    params["category_filter"] = json_category_filter

    json_product_status_filter: str | Unset = UNSET
    if not isinstance(product_status_filter, Unset):
        json_product_status_filter = product_status_filter.value

    params["product_status_filter"] = json_product_status_filter


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202605/shop_products/performance",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetShopProductPerformanceListResponse | None:
    if response.status_code == 200:
        response_200 = GetShopProductPerformanceListResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetShopProductPerformanceListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    sort_field: GetShopProductPerformanceListSortField | Unset = UNSET,
    sort_order: GetShopProductPerformanceListSortOrder | Unset = UNSET,
    currency: GetShopProductPerformanceListCurrency | Unset = UNSET,
    category_filter: list[str] | Unset = UNSET,
    product_status_filter: GetShopProductPerformanceListProductStatusFilter | Unset = UNSET,

) -> Response[GetShopProductPerformanceListResponse]:
    """ Get Shop Product Performance List

     Returns a paginated list of shop products and their total, seller-channel, affiliate-channel, and
    Shop Tab performance metrics for the specified date range.

    Args:
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        page_size (int | Unset):
        page_token (str | Unset):
        sort_field (GetShopProductPerformanceListSortField | Unset):
        sort_order (GetShopProductPerformanceListSortOrder | Unset):
        currency (GetShopProductPerformanceListCurrency | Unset):
        category_filter (list[str] | Unset):
        product_status_filter (GetShopProductPerformanceListProductStatusFilter | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopProductPerformanceListResponse]
     """


    kwargs = _get_kwargs(
        start_date_ge=start_date_ge,
end_date_lt=end_date_lt,
page_size=page_size,
page_token=page_token,
sort_field=sort_field,
sort_order=sort_order,
currency=currency,
category_filter=category_filter,
product_status_filter=product_status_filter,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    sort_field: GetShopProductPerformanceListSortField | Unset = UNSET,
    sort_order: GetShopProductPerformanceListSortOrder | Unset = UNSET,
    currency: GetShopProductPerformanceListCurrency | Unset = UNSET,
    category_filter: list[str] | Unset = UNSET,
    product_status_filter: GetShopProductPerformanceListProductStatusFilter | Unset = UNSET,

) -> GetShopProductPerformanceListResponse | None:
    """ Get Shop Product Performance List

     Returns a paginated list of shop products and their total, seller-channel, affiliate-channel, and
    Shop Tab performance metrics for the specified date range.

    Args:
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        page_size (int | Unset):
        page_token (str | Unset):
        sort_field (GetShopProductPerformanceListSortField | Unset):
        sort_order (GetShopProductPerformanceListSortOrder | Unset):
        currency (GetShopProductPerformanceListCurrency | Unset):
        category_filter (list[str] | Unset):
        product_status_filter (GetShopProductPerformanceListProductStatusFilter | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopProductPerformanceListResponse
     """


    return sync_detailed(
        client=client,
start_date_ge=start_date_ge,
end_date_lt=end_date_lt,
page_size=page_size,
page_token=page_token,
sort_field=sort_field,
sort_order=sort_order,
currency=currency,
category_filter=category_filter,
product_status_filter=product_status_filter,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    sort_field: GetShopProductPerformanceListSortField | Unset = UNSET,
    sort_order: GetShopProductPerformanceListSortOrder | Unset = UNSET,
    currency: GetShopProductPerformanceListCurrency | Unset = UNSET,
    category_filter: list[str] | Unset = UNSET,
    product_status_filter: GetShopProductPerformanceListProductStatusFilter | Unset = UNSET,

) -> Response[GetShopProductPerformanceListResponse]:
    """ Get Shop Product Performance List

     Returns a paginated list of shop products and their total, seller-channel, affiliate-channel, and
    Shop Tab performance metrics for the specified date range.

    Args:
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        page_size (int | Unset):
        page_token (str | Unset):
        sort_field (GetShopProductPerformanceListSortField | Unset):
        sort_order (GetShopProductPerformanceListSortOrder | Unset):
        currency (GetShopProductPerformanceListCurrency | Unset):
        category_filter (list[str] | Unset):
        product_status_filter (GetShopProductPerformanceListProductStatusFilter | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopProductPerformanceListResponse]
     """


    kwargs = _get_kwargs(
        start_date_ge=start_date_ge,
end_date_lt=end_date_lt,
page_size=page_size,
page_token=page_token,
sort_field=sort_field,
sort_order=sort_order,
currency=currency,
category_filter=category_filter,
product_status_filter=product_status_filter,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    sort_field: GetShopProductPerformanceListSortField | Unset = UNSET,
    sort_order: GetShopProductPerformanceListSortOrder | Unset = UNSET,
    currency: GetShopProductPerformanceListCurrency | Unset = UNSET,
    category_filter: list[str] | Unset = UNSET,
    product_status_filter: GetShopProductPerformanceListProductStatusFilter | Unset = UNSET,

) -> GetShopProductPerformanceListResponse | None:
    """ Get Shop Product Performance List

     Returns a paginated list of shop products and their total, seller-channel, affiliate-channel, and
    Shop Tab performance metrics for the specified date range.

    Args:
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        page_size (int | Unset):
        page_token (str | Unset):
        sort_field (GetShopProductPerformanceListSortField | Unset):
        sort_order (GetShopProductPerformanceListSortOrder | Unset):
        currency (GetShopProductPerformanceListCurrency | Unset):
        category_filter (list[str] | Unset):
        product_status_filter (GetShopProductPerformanceListProductStatusFilter | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopProductPerformanceListResponse
     """


    return (await asyncio_detailed(
        client=client,
start_date_ge=start_date_ge,
end_date_lt=end_date_lt,
page_size=page_size,
page_token=page_token,
sort_field=sort_field,
sort_order=sort_order,
currency=currency,
category_filter=category_filter,
product_status_filter=product_status_filter,

    )).parsed
