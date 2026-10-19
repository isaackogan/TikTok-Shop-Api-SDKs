import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_shop_video_performance_overview_account_type import GetShopVideoPerformanceOverviewAccountType
from ...models.get_shop_video_performance_overview_currency import GetShopVideoPerformanceOverviewCurrency
from ...models.get_shop_video_performance_overview_granularity import GetShopVideoPerformanceOverviewGranularity
from ...models.get_shop_video_performance_overview_response import GetShopVideoPerformanceOverviewResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    today: bool | Unset = UNSET,
    granularity: GetShopVideoPerformanceOverviewGranularity | Unset = UNSET,
    currency: GetShopVideoPerformanceOverviewCurrency | Unset = UNSET,
    account_type: GetShopVideoPerformanceOverviewAccountType | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_start_date_ge = start_date_ge.isoformat()
    params["start_date_ge"] = json_start_date_ge

    json_end_date_lt = end_date_lt.isoformat()
    params["end_date_lt"] = json_end_date_lt

    params["today"] = today

    json_granularity: str | Unset = UNSET
    if not isinstance(granularity, Unset):
        json_granularity = granularity.value

    params["granularity"] = json_granularity

    json_currency: str | Unset = UNSET
    if not isinstance(currency, Unset):
        json_currency = currency.value

    params["currency"] = json_currency

    json_account_type: str | Unset = UNSET
    if not isinstance(account_type, Unset):
        json_account_type = account_type.value

    params["account_type"] = json_account_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202609/shop_videos/overview_performance",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetShopVideoPerformanceOverviewResponse | None:
    if response.status_code == 200:
        response_200 = GetShopVideoPerformanceOverviewResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetShopVideoPerformanceOverviewResponse]:
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
    today: bool | Unset = UNSET,
    granularity: GetShopVideoPerformanceOverviewGranularity | Unset = UNSET,
    currency: GetShopVideoPerformanceOverviewCurrency | Unset = UNSET,
    account_type: GetShopVideoPerformanceOverviewAccountType | Unset = UNSET,
) -> Response[GetShopVideoPerformanceOverviewResponse]:
    """Get Shop Video Performance Overview

     Returns overall performance metrics for all videos under a shop.

    Args:
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        today (bool | Unset):
        granularity (GetShopVideoPerformanceOverviewGranularity | Unset):
        currency (GetShopVideoPerformanceOverviewCurrency | Unset):
        account_type (GetShopVideoPerformanceOverviewAccountType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopVideoPerformanceOverviewResponse]
    """

    kwargs = _get_kwargs(
        start_date_ge=start_date_ge,
        end_date_lt=end_date_lt,
        today=today,
        granularity=granularity,
        currency=currency,
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
    today: bool | Unset = UNSET,
    granularity: GetShopVideoPerformanceOverviewGranularity | Unset = UNSET,
    currency: GetShopVideoPerformanceOverviewCurrency | Unset = UNSET,
    account_type: GetShopVideoPerformanceOverviewAccountType | Unset = UNSET,
) -> GetShopVideoPerformanceOverviewResponse | None:
    """Get Shop Video Performance Overview

     Returns overall performance metrics for all videos under a shop.

    Args:
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        today (bool | Unset):
        granularity (GetShopVideoPerformanceOverviewGranularity | Unset):
        currency (GetShopVideoPerformanceOverviewCurrency | Unset):
        account_type (GetShopVideoPerformanceOverviewAccountType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopVideoPerformanceOverviewResponse
    """

    return sync_detailed(
        client=client,
        start_date_ge=start_date_ge,
        end_date_lt=end_date_lt,
        today=today,
        granularity=granularity,
        currency=currency,
        account_type=account_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    today: bool | Unset = UNSET,
    granularity: GetShopVideoPerformanceOverviewGranularity | Unset = UNSET,
    currency: GetShopVideoPerformanceOverviewCurrency | Unset = UNSET,
    account_type: GetShopVideoPerformanceOverviewAccountType | Unset = UNSET,
) -> Response[GetShopVideoPerformanceOverviewResponse]:
    """Get Shop Video Performance Overview

     Returns overall performance metrics for all videos under a shop.

    Args:
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        today (bool | Unset):
        granularity (GetShopVideoPerformanceOverviewGranularity | Unset):
        currency (GetShopVideoPerformanceOverviewCurrency | Unset):
        account_type (GetShopVideoPerformanceOverviewAccountType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopVideoPerformanceOverviewResponse]
    """

    kwargs = _get_kwargs(
        start_date_ge=start_date_ge,
        end_date_lt=end_date_lt,
        today=today,
        granularity=granularity,
        currency=currency,
        account_type=account_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    today: bool | Unset = UNSET,
    granularity: GetShopVideoPerformanceOverviewGranularity | Unset = UNSET,
    currency: GetShopVideoPerformanceOverviewCurrency | Unset = UNSET,
    account_type: GetShopVideoPerformanceOverviewAccountType | Unset = UNSET,
) -> GetShopVideoPerformanceOverviewResponse | None:
    """Get Shop Video Performance Overview

     Returns overall performance metrics for all videos under a shop.

    Args:
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        today (bool | Unset):
        granularity (GetShopVideoPerformanceOverviewGranularity | Unset):
        currency (GetShopVideoPerformanceOverviewCurrency | Unset):
        account_type (GetShopVideoPerformanceOverviewAccountType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopVideoPerformanceOverviewResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            start_date_ge=start_date_ge,
            end_date_lt=end_date_lt,
            today=today,
            granularity=granularity,
            currency=currency,
            account_type=account_type,
        )
    ).parsed
