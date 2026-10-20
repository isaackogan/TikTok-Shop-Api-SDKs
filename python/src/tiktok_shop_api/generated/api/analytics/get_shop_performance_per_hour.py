from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_shop_performance_per_hour_currency import GetShopPerformancePerHourCurrency
from ...models.get_shop_performance_per_hour_response import GetShopPerformancePerHourResponse
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    date: datetime.date,
    *,
    currency: GetShopPerformancePerHourCurrency | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_currency: str | Unset = UNSET
    if not isinstance(currency, Unset):
        json_currency = currency.value

    params["currency"] = json_currency


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202510/shop/performance/{date}/performance_per_hour".format(date=quote(str(date), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetShopPerformancePerHourResponse | None:
    if response.status_code == 200:
        response_200 = GetShopPerformancePerHourResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetShopPerformancePerHourResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    date: datetime.date,
    *,
    client: AuthenticatedClient | Client,
    currency: GetShopPerformancePerHourCurrency | Unset = UNSET,

) -> Response[GetShopPerformancePerHourResponse]:
    """ Get Shop Performance Per Hour

     Returns hourly shop performance details for the requested date. The date can be within the last 30
    days, including today.

    Args:
        date (datetime.date):
        currency (GetShopPerformancePerHourCurrency | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopPerformancePerHourResponse]
     """


    kwargs = _get_kwargs(
        date=date,
currency=currency,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    date: datetime.date,
    *,
    client: AuthenticatedClient | Client,
    currency: GetShopPerformancePerHourCurrency | Unset = UNSET,

) -> GetShopPerformancePerHourResponse | None:
    """ Get Shop Performance Per Hour

     Returns hourly shop performance details for the requested date. The date can be within the last 30
    days, including today.

    Args:
        date (datetime.date):
        currency (GetShopPerformancePerHourCurrency | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopPerformancePerHourResponse
     """


    return sync_detailed(
        date=date,
client=client,
currency=currency,

    ).parsed

async def asyncio_detailed(
    date: datetime.date,
    *,
    client: AuthenticatedClient | Client,
    currency: GetShopPerformancePerHourCurrency | Unset = UNSET,

) -> Response[GetShopPerformancePerHourResponse]:
    """ Get Shop Performance Per Hour

     Returns hourly shop performance details for the requested date. The date can be within the last 30
    days, including today.

    Args:
        date (datetime.date):
        currency (GetShopPerformancePerHourCurrency | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopPerformancePerHourResponse]
     """


    kwargs = _get_kwargs(
        date=date,
currency=currency,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    date: datetime.date,
    *,
    client: AuthenticatedClient | Client,
    currency: GetShopPerformancePerHourCurrency | Unset = UNSET,

) -> GetShopPerformancePerHourResponse | None:
    """ Get Shop Performance Per Hour

     Returns hourly shop performance details for the requested date. The date can be within the last 30
    days, including today.

    Args:
        date (datetime.date):
        currency (GetShopPerformancePerHourCurrency | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopPerformancePerHourResponse
     """


    return (await asyncio_detailed(
        date=date,
client=client,
currency=currency,

    )).parsed
