from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_shop_video_product_performance_list_currency import GetShopVideoProductPerformanceListCurrency
from ...models.get_shop_video_product_performance_list_response import GetShopVideoProductPerformanceListResponse
from ...models.get_shop_video_product_performance_list_sort_field import GetShopVideoProductPerformanceListSortField
from ...models.get_shop_video_product_performance_list_sort_order import GetShopVideoProductPerformanceListSortOrder
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    video_id: str,
    *,
    end_date_lt: datetime.date,
    page_size: int | Unset = UNSET,
    sort_field: GetShopVideoProductPerformanceListSortField | Unset = UNSET,
    sort_order: GetShopVideoProductPerformanceListSortOrder | Unset = UNSET,
    currency: GetShopVideoProductPerformanceListCurrency | Unset = UNSET,
    page_token: str | Unset = UNSET,
    start_date_ge: datetime.date,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_end_date_lt = end_date_lt.isoformat()
    params["end_date_lt"] = json_end_date_lt

    params["page_size"] = page_size

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

    params["page_token"] = page_token

    json_start_date_ge = start_date_ge.isoformat()
    params["start_date_ge"] = json_start_date_ge


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202509/shop_videos/{video_id}/products/performance".format(video_id=quote(str(video_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetShopVideoProductPerformanceListResponse | None:
    if response.status_code == 200:
        response_200 = GetShopVideoProductPerformanceListResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetShopVideoProductPerformanceListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    video_id: str,
    *,
    client: AuthenticatedClient | Client,
    end_date_lt: datetime.date,
    page_size: int | Unset = UNSET,
    sort_field: GetShopVideoProductPerformanceListSortField | Unset = UNSET,
    sort_order: GetShopVideoProductPerformanceListSortOrder | Unset = UNSET,
    currency: GetShopVideoProductPerformanceListCurrency | Unset = UNSET,
    page_token: str | Unset = UNSET,
    start_date_ge: datetime.date,

) -> Response[GetShopVideoProductPerformanceListResponse]:
    """ Get Shop Video Product Performance List

     Returns performance metrics for a list of products promoted in a given video.

    Args:
        video_id (str):
        end_date_lt (datetime.date):
        page_size (int | Unset):
        sort_field (GetShopVideoProductPerformanceListSortField | Unset):
        sort_order (GetShopVideoProductPerformanceListSortOrder | Unset):
        currency (GetShopVideoProductPerformanceListCurrency | Unset):
        page_token (str | Unset):
        start_date_ge (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopVideoProductPerformanceListResponse]
     """


    kwargs = _get_kwargs(
        video_id=video_id,
end_date_lt=end_date_lt,
page_size=page_size,
sort_field=sort_field,
sort_order=sort_order,
currency=currency,
page_token=page_token,
start_date_ge=start_date_ge,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    video_id: str,
    *,
    client: AuthenticatedClient | Client,
    end_date_lt: datetime.date,
    page_size: int | Unset = UNSET,
    sort_field: GetShopVideoProductPerformanceListSortField | Unset = UNSET,
    sort_order: GetShopVideoProductPerformanceListSortOrder | Unset = UNSET,
    currency: GetShopVideoProductPerformanceListCurrency | Unset = UNSET,
    page_token: str | Unset = UNSET,
    start_date_ge: datetime.date,

) -> GetShopVideoProductPerformanceListResponse | None:
    """ Get Shop Video Product Performance List

     Returns performance metrics for a list of products promoted in a given video.

    Args:
        video_id (str):
        end_date_lt (datetime.date):
        page_size (int | Unset):
        sort_field (GetShopVideoProductPerformanceListSortField | Unset):
        sort_order (GetShopVideoProductPerformanceListSortOrder | Unset):
        currency (GetShopVideoProductPerformanceListCurrency | Unset):
        page_token (str | Unset):
        start_date_ge (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopVideoProductPerformanceListResponse
     """


    return sync_detailed(
        video_id=video_id,
client=client,
end_date_lt=end_date_lt,
page_size=page_size,
sort_field=sort_field,
sort_order=sort_order,
currency=currency,
page_token=page_token,
start_date_ge=start_date_ge,

    ).parsed

async def asyncio_detailed(
    video_id: str,
    *,
    client: AuthenticatedClient | Client,
    end_date_lt: datetime.date,
    page_size: int | Unset = UNSET,
    sort_field: GetShopVideoProductPerformanceListSortField | Unset = UNSET,
    sort_order: GetShopVideoProductPerformanceListSortOrder | Unset = UNSET,
    currency: GetShopVideoProductPerformanceListCurrency | Unset = UNSET,
    page_token: str | Unset = UNSET,
    start_date_ge: datetime.date,

) -> Response[GetShopVideoProductPerformanceListResponse]:
    """ Get Shop Video Product Performance List

     Returns performance metrics for a list of products promoted in a given video.

    Args:
        video_id (str):
        end_date_lt (datetime.date):
        page_size (int | Unset):
        sort_field (GetShopVideoProductPerformanceListSortField | Unset):
        sort_order (GetShopVideoProductPerformanceListSortOrder | Unset):
        currency (GetShopVideoProductPerformanceListCurrency | Unset):
        page_token (str | Unset):
        start_date_ge (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopVideoProductPerformanceListResponse]
     """


    kwargs = _get_kwargs(
        video_id=video_id,
end_date_lt=end_date_lt,
page_size=page_size,
sort_field=sort_field,
sort_order=sort_order,
currency=currency,
page_token=page_token,
start_date_ge=start_date_ge,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    video_id: str,
    *,
    client: AuthenticatedClient | Client,
    end_date_lt: datetime.date,
    page_size: int | Unset = UNSET,
    sort_field: GetShopVideoProductPerformanceListSortField | Unset = UNSET,
    sort_order: GetShopVideoProductPerformanceListSortOrder | Unset = UNSET,
    currency: GetShopVideoProductPerformanceListCurrency | Unset = UNSET,
    page_token: str | Unset = UNSET,
    start_date_ge: datetime.date,

) -> GetShopVideoProductPerformanceListResponse | None:
    """ Get Shop Video Product Performance List

     Returns performance metrics for a list of products promoted in a given video.

    Args:
        video_id (str):
        end_date_lt (datetime.date):
        page_size (int | Unset):
        sort_field (GetShopVideoProductPerformanceListSortField | Unset):
        sort_order (GetShopVideoProductPerformanceListSortOrder | Unset):
        currency (GetShopVideoProductPerformanceListCurrency | Unset):
        page_token (str | Unset):
        start_date_ge (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopVideoProductPerformanceListResponse
     """


    return (await asyncio_detailed(
        video_id=video_id,
client=client,
end_date_lt=end_date_lt,
page_size=page_size,
sort_field=sort_field,
sort_order=sort_order,
currency=currency,
page_token=page_token,
start_date_ge=start_date_ge,

    )).parsed
