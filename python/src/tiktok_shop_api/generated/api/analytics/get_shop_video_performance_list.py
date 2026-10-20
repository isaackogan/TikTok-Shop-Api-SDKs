import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_shop_video_performance_list_account_type import GetShopVideoPerformanceListAccountType
from ...models.get_shop_video_performance_list_currency import GetShopVideoPerformanceListCurrency
from ...models.get_shop_video_performance_list_response import GetShopVideoPerformanceListResponse
from ...models.get_shop_video_performance_list_sort_field import GetShopVideoPerformanceListSortField
from ...models.get_shop_video_performance_list_sort_order import GetShopVideoPerformanceListSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    page_size: int | Unset = UNSET,
    sort_field: GetShopVideoPerformanceListSortField | Unset = UNSET,
    sort_order: GetShopVideoPerformanceListSortOrder | Unset = UNSET,
    currency: GetShopVideoPerformanceListCurrency | Unset = UNSET,
    page_token: str | Unset = UNSET,
    account_type: GetShopVideoPerformanceListAccountType | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_start_date_ge = start_date_ge.isoformat()
    params["start_date_ge"] = json_start_date_ge

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

    json_account_type: str | Unset = UNSET
    if not isinstance(account_type, Unset):
        json_account_type = account_type.value

    params["account_type"] = json_account_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202605/shop_videos/performance",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetShopVideoPerformanceListResponse | None:
    if response.status_code == 200:
        response_200 = GetShopVideoPerformanceListResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetShopVideoPerformanceListResponse]:
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
    sort_field: GetShopVideoPerformanceListSortField | Unset = UNSET,
    sort_order: GetShopVideoPerformanceListSortOrder | Unset = UNSET,
    currency: GetShopVideoPerformanceListCurrency | Unset = UNSET,
    page_token: str | Unset = UNSET,
    account_type: GetShopVideoPerformanceListAccountType | Unset = UNSET,
) -> Response[GetShopVideoPerformanceListResponse]:
    """Get Shop Video Performance List

     Returns a list of videos and associated metrics for a shop.

    Args:
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        page_size (int | Unset):
        sort_field (GetShopVideoPerformanceListSortField | Unset):
        sort_order (GetShopVideoPerformanceListSortOrder | Unset):
        currency (GetShopVideoPerformanceListCurrency | Unset):
        page_token (str | Unset):
        account_type (GetShopVideoPerformanceListAccountType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopVideoPerformanceListResponse]
    """

    kwargs = _get_kwargs(
        start_date_ge=start_date_ge,
        end_date_lt=end_date_lt,
        page_size=page_size,
        sort_field=sort_field,
        sort_order=sort_order,
        currency=currency,
        page_token=page_token,
        account_type=account_type,
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
    sort_field: GetShopVideoPerformanceListSortField | Unset = UNSET,
    sort_order: GetShopVideoPerformanceListSortOrder | Unset = UNSET,
    currency: GetShopVideoPerformanceListCurrency | Unset = UNSET,
    page_token: str | Unset = UNSET,
    account_type: GetShopVideoPerformanceListAccountType | Unset = UNSET,
) -> GetShopVideoPerformanceListResponse | None:
    """Get Shop Video Performance List

     Returns a list of videos and associated metrics for a shop.

    Args:
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        page_size (int | Unset):
        sort_field (GetShopVideoPerformanceListSortField | Unset):
        sort_order (GetShopVideoPerformanceListSortOrder | Unset):
        currency (GetShopVideoPerformanceListCurrency | Unset):
        page_token (str | Unset):
        account_type (GetShopVideoPerformanceListAccountType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopVideoPerformanceListResponse
    """

    return sync_detailed(
        client=client,
        start_date_ge=start_date_ge,
        end_date_lt=end_date_lt,
        page_size=page_size,
        sort_field=sort_field,
        sort_order=sort_order,
        currency=currency,
        page_token=page_token,
        account_type=account_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    page_size: int | Unset = UNSET,
    sort_field: GetShopVideoPerformanceListSortField | Unset = UNSET,
    sort_order: GetShopVideoPerformanceListSortOrder | Unset = UNSET,
    currency: GetShopVideoPerformanceListCurrency | Unset = UNSET,
    page_token: str | Unset = UNSET,
    account_type: GetShopVideoPerformanceListAccountType | Unset = UNSET,
) -> Response[GetShopVideoPerformanceListResponse]:
    """Get Shop Video Performance List

     Returns a list of videos and associated metrics for a shop.

    Args:
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        page_size (int | Unset):
        sort_field (GetShopVideoPerformanceListSortField | Unset):
        sort_order (GetShopVideoPerformanceListSortOrder | Unset):
        currency (GetShopVideoPerformanceListCurrency | Unset):
        page_token (str | Unset):
        account_type (GetShopVideoPerformanceListAccountType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopVideoPerformanceListResponse]
    """

    kwargs = _get_kwargs(
        start_date_ge=start_date_ge,
        end_date_lt=end_date_lt,
        page_size=page_size,
        sort_field=sort_field,
        sort_order=sort_order,
        currency=currency,
        page_token=page_token,
        account_type=account_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    page_size: int | Unset = UNSET,
    sort_field: GetShopVideoPerformanceListSortField | Unset = UNSET,
    sort_order: GetShopVideoPerformanceListSortOrder | Unset = UNSET,
    currency: GetShopVideoPerformanceListCurrency | Unset = UNSET,
    page_token: str | Unset = UNSET,
    account_type: GetShopVideoPerformanceListAccountType | Unset = UNSET,
) -> GetShopVideoPerformanceListResponse | None:
    """Get Shop Video Performance List

     Returns a list of videos and associated metrics for a shop.

    Args:
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        page_size (int | Unset):
        sort_field (GetShopVideoPerformanceListSortField | Unset):
        sort_order (GetShopVideoPerformanceListSortOrder | Unset):
        currency (GetShopVideoPerformanceListCurrency | Unset):
        page_token (str | Unset):
        account_type (GetShopVideoPerformanceListAccountType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopVideoPerformanceListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            start_date_ge=start_date_ge,
            end_date_lt=end_date_lt,
            page_size=page_size,
            sort_field=sort_field,
            sort_order=sort_order,
            currency=currency,
            page_token=page_token,
            account_type=account_type,
        )
    ).parsed
