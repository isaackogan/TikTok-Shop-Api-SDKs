from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_shop_live_performance_list_account_type import GetShopLivePerformanceListAccountType
from ...models.get_shop_live_performance_list_currency import GetShopLivePerformanceListCurrency
from ...models.get_shop_live_performance_list_response import GetShopLIVEPerformanceListResponse
from ...models.get_shop_live_performance_list_sort_field import GetShopLivePerformanceListSortField
from ...models.get_shop_live_performance_list_sort_order import GetShopLivePerformanceListSortOrder
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    *,
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    account_type: GetShopLivePerformanceListAccountType,
    page_size: int | Unset = UNSET,
    sort_field: GetShopLivePerformanceListSortField | Unset = UNSET,
    sort_order: GetShopLivePerformanceListSortOrder | Unset = UNSET,
    currency: GetShopLivePerformanceListCurrency | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_start_date_ge = start_date_ge.isoformat()
    params["start_date_ge"] = json_start_date_ge

    json_end_date_lt = end_date_lt.isoformat()
    params["end_date_lt"] = json_end_date_lt

    json_account_type = account_type.value
    params["account_type"] = json_account_type

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


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202609/shop_lives/performance",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetShopLIVEPerformanceListResponse | None:
    if response.status_code == 200:
        response_200 = GetShopLIVEPerformanceListResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetShopLIVEPerformanceListResponse]:
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
    account_type: GetShopLivePerformanceListAccountType,
    page_size: int | Unset = UNSET,
    sort_field: GetShopLivePerformanceListSortField | Unset = UNSET,
    sort_order: GetShopLivePerformanceListSortOrder | Unset = UNSET,
    currency: GetShopLivePerformanceListCurrency | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> Response[GetShopLIVEPerformanceListResponse]:
    """ Get Shop LIVE Performance List

     Returns a list of LIVE stream sessions and associated metrics for a shop. Sellers can only query
    room ID data for their own official creator accounts.

    Args:
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        account_type (GetShopLivePerformanceListAccountType):
        page_size (int | Unset):
        sort_field (GetShopLivePerformanceListSortField | Unset):
        sort_order (GetShopLivePerformanceListSortOrder | Unset):
        currency (GetShopLivePerformanceListCurrency | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopLIVEPerformanceListResponse]
     """


    kwargs = _get_kwargs(
        start_date_ge=start_date_ge,
end_date_lt=end_date_lt,
account_type=account_type,
page_size=page_size,
sort_field=sort_field,
sort_order=sort_order,
currency=currency,
page_token=page_token,

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
    account_type: GetShopLivePerformanceListAccountType,
    page_size: int | Unset = UNSET,
    sort_field: GetShopLivePerformanceListSortField | Unset = UNSET,
    sort_order: GetShopLivePerformanceListSortOrder | Unset = UNSET,
    currency: GetShopLivePerformanceListCurrency | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> GetShopLIVEPerformanceListResponse | None:
    """ Get Shop LIVE Performance List

     Returns a list of LIVE stream sessions and associated metrics for a shop. Sellers can only query
    room ID data for their own official creator accounts.

    Args:
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        account_type (GetShopLivePerformanceListAccountType):
        page_size (int | Unset):
        sort_field (GetShopLivePerformanceListSortField | Unset):
        sort_order (GetShopLivePerformanceListSortOrder | Unset):
        currency (GetShopLivePerformanceListCurrency | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopLIVEPerformanceListResponse
     """


    return sync_detailed(
        client=client,
start_date_ge=start_date_ge,
end_date_lt=end_date_lt,
account_type=account_type,
page_size=page_size,
sort_field=sort_field,
sort_order=sort_order,
currency=currency,
page_token=page_token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    account_type: GetShopLivePerformanceListAccountType,
    page_size: int | Unset = UNSET,
    sort_field: GetShopLivePerformanceListSortField | Unset = UNSET,
    sort_order: GetShopLivePerformanceListSortOrder | Unset = UNSET,
    currency: GetShopLivePerformanceListCurrency | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> Response[GetShopLIVEPerformanceListResponse]:
    """ Get Shop LIVE Performance List

     Returns a list of LIVE stream sessions and associated metrics for a shop. Sellers can only query
    room ID data for their own official creator accounts.

    Args:
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        account_type (GetShopLivePerformanceListAccountType):
        page_size (int | Unset):
        sort_field (GetShopLivePerformanceListSortField | Unset):
        sort_order (GetShopLivePerformanceListSortOrder | Unset):
        currency (GetShopLivePerformanceListCurrency | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopLIVEPerformanceListResponse]
     """


    kwargs = _get_kwargs(
        start_date_ge=start_date_ge,
end_date_lt=end_date_lt,
account_type=account_type,
page_size=page_size,
sort_field=sort_field,
sort_order=sort_order,
currency=currency,
page_token=page_token,

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
    account_type: GetShopLivePerformanceListAccountType,
    page_size: int | Unset = UNSET,
    sort_field: GetShopLivePerformanceListSortField | Unset = UNSET,
    sort_order: GetShopLivePerformanceListSortOrder | Unset = UNSET,
    currency: GetShopLivePerformanceListCurrency | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> GetShopLIVEPerformanceListResponse | None:
    """ Get Shop LIVE Performance List

     Returns a list of LIVE stream sessions and associated metrics for a shop. Sellers can only query
    room ID data for their own official creator accounts.

    Args:
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        account_type (GetShopLivePerformanceListAccountType):
        page_size (int | Unset):
        sort_field (GetShopLivePerformanceListSortField | Unset):
        sort_order (GetShopLivePerformanceListSortOrder | Unset):
        currency (GetShopLivePerformanceListCurrency | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopLIVEPerformanceListResponse
     """


    return (await asyncio_detailed(
        client=client,
start_date_ge=start_date_ge,
end_date_lt=end_date_lt,
account_type=account_type,
page_size=page_size,
sort_field=sort_field,
sort_order=sort_order,
currency=currency,
page_token=page_token,

    )).parsed
