from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_shop_sku_performance_list_product_status_filter import GetShopSkuPerformanceListProductStatusFilter
from ...models.get_shop_sku_performance_list_response import GetShopSKUPerformanceListResponse
from ...models.get_shop_sku_performance_list_sort_field import GetShopSkuPerformanceListSortField
from ...models.get_shop_sku_performance_list_sort_order import GetShopSkuPerformanceListSortOrder
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    *,
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    sort_field: GetShopSkuPerformanceListSortField | Unset = UNSET,
    sort_order: GetShopSkuPerformanceListSortOrder | Unset = UNSET,
    category_filter: list[str] | Unset = UNSET,
    product_status_filter: GetShopSkuPerformanceListProductStatusFilter | Unset = UNSET,
    product_ids: list[str] | Unset = UNSET,
    currency: str | Unset = UNSET,

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

    json_category_filter: list[str] | Unset = UNSET
    if not isinstance(category_filter, Unset):
        json_category_filter = category_filter


    params["category_filter"] = json_category_filter

    json_product_status_filter: str | Unset = UNSET
    if not isinstance(product_status_filter, Unset):
        json_product_status_filter = product_status_filter.value

    params["product_status_filter"] = json_product_status_filter

    json_product_ids: list[str] | Unset = UNSET
    if not isinstance(product_ids, Unset):
        json_product_ids = product_ids


    params["product_ids"] = json_product_ids

    params["currency"] = currency


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202509/shop_skus/performance",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetShopSKUPerformanceListResponse | None:
    if response.status_code == 200:
        response_200 = GetShopSKUPerformanceListResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetShopSKUPerformanceListResponse]:
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
    sort_field: GetShopSkuPerformanceListSortField | Unset = UNSET,
    sort_order: GetShopSkuPerformanceListSortOrder | Unset = UNSET,
    category_filter: list[str] | Unset = UNSET,
    product_status_filter: GetShopSkuPerformanceListProductStatusFilter | Unset = UNSET,
    product_ids: list[str] | Unset = UNSET,
    currency: str | Unset = UNSET,

) -> Response[GetShopSKUPerformanceListResponse]:
    """ Get Shop SKU Performance List

     Returns a paginated list of performance metrics for the shop's SKUs over the requested date range.

    Args:
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        page_size (int | Unset):
        page_token (str | Unset):
        sort_field (GetShopSkuPerformanceListSortField | Unset):
        sort_order (GetShopSkuPerformanceListSortOrder | Unset):
        category_filter (list[str] | Unset):
        product_status_filter (GetShopSkuPerformanceListProductStatusFilter | Unset):
        product_ids (list[str] | Unset):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopSKUPerformanceListResponse]
     """


    kwargs = _get_kwargs(
        start_date_ge=start_date_ge,
end_date_lt=end_date_lt,
page_size=page_size,
page_token=page_token,
sort_field=sort_field,
sort_order=sort_order,
category_filter=category_filter,
product_status_filter=product_status_filter,
product_ids=product_ids,
currency=currency,

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
    sort_field: GetShopSkuPerformanceListSortField | Unset = UNSET,
    sort_order: GetShopSkuPerformanceListSortOrder | Unset = UNSET,
    category_filter: list[str] | Unset = UNSET,
    product_status_filter: GetShopSkuPerformanceListProductStatusFilter | Unset = UNSET,
    product_ids: list[str] | Unset = UNSET,
    currency: str | Unset = UNSET,

) -> GetShopSKUPerformanceListResponse | None:
    """ Get Shop SKU Performance List

     Returns a paginated list of performance metrics for the shop's SKUs over the requested date range.

    Args:
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        page_size (int | Unset):
        page_token (str | Unset):
        sort_field (GetShopSkuPerformanceListSortField | Unset):
        sort_order (GetShopSkuPerformanceListSortOrder | Unset):
        category_filter (list[str] | Unset):
        product_status_filter (GetShopSkuPerformanceListProductStatusFilter | Unset):
        product_ids (list[str] | Unset):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopSKUPerformanceListResponse
     """


    return sync_detailed(
        client=client,
start_date_ge=start_date_ge,
end_date_lt=end_date_lt,
page_size=page_size,
page_token=page_token,
sort_field=sort_field,
sort_order=sort_order,
category_filter=category_filter,
product_status_filter=product_status_filter,
product_ids=product_ids,
currency=currency,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    sort_field: GetShopSkuPerformanceListSortField | Unset = UNSET,
    sort_order: GetShopSkuPerformanceListSortOrder | Unset = UNSET,
    category_filter: list[str] | Unset = UNSET,
    product_status_filter: GetShopSkuPerformanceListProductStatusFilter | Unset = UNSET,
    product_ids: list[str] | Unset = UNSET,
    currency: str | Unset = UNSET,

) -> Response[GetShopSKUPerformanceListResponse]:
    """ Get Shop SKU Performance List

     Returns a paginated list of performance metrics for the shop's SKUs over the requested date range.

    Args:
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        page_size (int | Unset):
        page_token (str | Unset):
        sort_field (GetShopSkuPerformanceListSortField | Unset):
        sort_order (GetShopSkuPerformanceListSortOrder | Unset):
        category_filter (list[str] | Unset):
        product_status_filter (GetShopSkuPerformanceListProductStatusFilter | Unset):
        product_ids (list[str] | Unset):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopSKUPerformanceListResponse]
     """


    kwargs = _get_kwargs(
        start_date_ge=start_date_ge,
end_date_lt=end_date_lt,
page_size=page_size,
page_token=page_token,
sort_field=sort_field,
sort_order=sort_order,
category_filter=category_filter,
product_status_filter=product_status_filter,
product_ids=product_ids,
currency=currency,

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
    sort_field: GetShopSkuPerformanceListSortField | Unset = UNSET,
    sort_order: GetShopSkuPerformanceListSortOrder | Unset = UNSET,
    category_filter: list[str] | Unset = UNSET,
    product_status_filter: GetShopSkuPerformanceListProductStatusFilter | Unset = UNSET,
    product_ids: list[str] | Unset = UNSET,
    currency: str | Unset = UNSET,

) -> GetShopSKUPerformanceListResponse | None:
    """ Get Shop SKU Performance List

     Returns a paginated list of performance metrics for the shop's SKUs over the requested date range.

    Args:
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        page_size (int | Unset):
        page_token (str | Unset):
        sort_field (GetShopSkuPerformanceListSortField | Unset):
        sort_order (GetShopSkuPerformanceListSortOrder | Unset):
        category_filter (list[str] | Unset):
        product_status_filter (GetShopSkuPerformanceListProductStatusFilter | Unset):
        product_ids (list[str] | Unset):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopSKUPerformanceListResponse
     """


    return (await asyncio_detailed(
        client=client,
start_date_ge=start_date_ge,
end_date_lt=end_date_lt,
page_size=page_size,
page_token=page_token,
sort_field=sort_field,
sort_order=sort_order,
category_filter=category_filter,
product_status_filter=product_status_filter,
product_ids=product_ids,
currency=currency,

    )).parsed
