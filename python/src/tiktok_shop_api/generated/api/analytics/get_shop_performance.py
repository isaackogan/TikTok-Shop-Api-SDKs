from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_shop_performance_currency import GetShopPerformanceCurrency
from ...models.get_shop_performance_granularity import GetShopPerformanceGranularity
from ...models.get_shop_performance_response import GetShopPerformanceResponse
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    *,
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    granularity: GetShopPerformanceGranularity | Unset = UNSET,
    currency: GetShopPerformanceCurrency | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_start_date_ge = start_date_ge.isoformat()
    params["start_date_ge"] = json_start_date_ge

    json_end_date_lt = end_date_lt.isoformat()
    params["end_date_lt"] = json_end_date_lt

    json_granularity: str | Unset = UNSET
    if not isinstance(granularity, Unset):
        json_granularity = granularity.value

    params["granularity"] = json_granularity

    json_currency: str | Unset = UNSET
    if not isinstance(currency, Unset):
        json_currency = currency.value

    params["currency"] = json_currency


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202609/shop/performance",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetShopPerformanceResponse | None:
    if response.status_code == 200:
        response_200 = GetShopPerformanceResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetShopPerformanceResponse]:
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
    granularity: GetShopPerformanceGranularity | Unset = UNSET,
    currency: GetShopPerformanceCurrency | Unset = UNSET,

) -> Response[GetShopPerformanceResponse]:
    """ Get Shop Performance

     Returns performance metrics at shop/seller level.

    Args:
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        granularity (GetShopPerformanceGranularity | Unset):
        currency (GetShopPerformanceCurrency | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopPerformanceResponse]
     """


    kwargs = _get_kwargs(
        start_date_ge=start_date_ge,
end_date_lt=end_date_lt,
granularity=granularity,
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
    granularity: GetShopPerformanceGranularity | Unset = UNSET,
    currency: GetShopPerformanceCurrency | Unset = UNSET,

) -> GetShopPerformanceResponse | None:
    """ Get Shop Performance

     Returns performance metrics at shop/seller level.

    Args:
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        granularity (GetShopPerformanceGranularity | Unset):
        currency (GetShopPerformanceCurrency | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopPerformanceResponse
     """


    return sync_detailed(
        client=client,
start_date_ge=start_date_ge,
end_date_lt=end_date_lt,
granularity=granularity,
currency=currency,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    granularity: GetShopPerformanceGranularity | Unset = UNSET,
    currency: GetShopPerformanceCurrency | Unset = UNSET,

) -> Response[GetShopPerformanceResponse]:
    """ Get Shop Performance

     Returns performance metrics at shop/seller level.

    Args:
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        granularity (GetShopPerformanceGranularity | Unset):
        currency (GetShopPerformanceCurrency | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopPerformanceResponse]
     """


    kwargs = _get_kwargs(
        start_date_ge=start_date_ge,
end_date_lt=end_date_lt,
granularity=granularity,
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
    granularity: GetShopPerformanceGranularity | Unset = UNSET,
    currency: GetShopPerformanceCurrency | Unset = UNSET,

) -> GetShopPerformanceResponse | None:
    """ Get Shop Performance

     Returns performance metrics at shop/seller level.

    Args:
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        granularity (GetShopPerformanceGranularity | Unset):
        currency (GetShopPerformanceCurrency | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopPerformanceResponse
     """


    return (await asyncio_detailed(
        client=client,
start_date_ge=start_date_ge,
end_date_lt=end_date_lt,
granularity=granularity,
currency=currency,

    )).parsed
