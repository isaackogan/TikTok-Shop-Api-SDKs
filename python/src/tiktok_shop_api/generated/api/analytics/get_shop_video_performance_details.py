from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_shop_video_performance_details_currency import GetShopVideoPerformanceDetailsCurrency
from ...models.get_shop_video_performance_details_granularity import GetShopVideoPerformanceDetailsGranularity
from ...models.get_shop_video_performance_details_response import GetShopVideoPerformanceDetailsResponse
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    video_id: str,
    *,
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    granularity: GetShopVideoPerformanceDetailsGranularity | Unset = UNSET,
    currency: GetShopVideoPerformanceDetailsCurrency | Unset = UNSET,

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
        "url": "/analytics/202509/shop_videos/{video_id}/performance".format(video_id=quote(str(video_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetShopVideoPerformanceDetailsResponse | None:
    if response.status_code == 200:
        response_200 = GetShopVideoPerformanceDetailsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetShopVideoPerformanceDetailsResponse]:
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
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    granularity: GetShopVideoPerformanceDetailsGranularity | Unset = UNSET,
    currency: GetShopVideoPerformanceDetailsCurrency | Unset = UNSET,

) -> Response[GetShopVideoPerformanceDetailsResponse]:
    """ Get Shop Video Performance Details

     Returns detailed performance metrics for a (requested) video.

    Args:
        video_id (str):
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        granularity (GetShopVideoPerformanceDetailsGranularity | Unset):
        currency (GetShopVideoPerformanceDetailsCurrency | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopVideoPerformanceDetailsResponse]
     """


    kwargs = _get_kwargs(
        video_id=video_id,
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
    video_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    granularity: GetShopVideoPerformanceDetailsGranularity | Unset = UNSET,
    currency: GetShopVideoPerformanceDetailsCurrency | Unset = UNSET,

) -> GetShopVideoPerformanceDetailsResponse | None:
    """ Get Shop Video Performance Details

     Returns detailed performance metrics for a (requested) video.

    Args:
        video_id (str):
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        granularity (GetShopVideoPerformanceDetailsGranularity | Unset):
        currency (GetShopVideoPerformanceDetailsCurrency | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopVideoPerformanceDetailsResponse
     """


    return sync_detailed(
        video_id=video_id,
client=client,
start_date_ge=start_date_ge,
end_date_lt=end_date_lt,
granularity=granularity,
currency=currency,

    ).parsed

async def asyncio_detailed(
    video_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    granularity: GetShopVideoPerformanceDetailsGranularity | Unset = UNSET,
    currency: GetShopVideoPerformanceDetailsCurrency | Unset = UNSET,

) -> Response[GetShopVideoPerformanceDetailsResponse]:
    """ Get Shop Video Performance Details

     Returns detailed performance metrics for a (requested) video.

    Args:
        video_id (str):
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        granularity (GetShopVideoPerformanceDetailsGranularity | Unset):
        currency (GetShopVideoPerformanceDetailsCurrency | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopVideoPerformanceDetailsResponse]
     """


    kwargs = _get_kwargs(
        video_id=video_id,
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
    video_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    granularity: GetShopVideoPerformanceDetailsGranularity | Unset = UNSET,
    currency: GetShopVideoPerformanceDetailsCurrency | Unset = UNSET,

) -> GetShopVideoPerformanceDetailsResponse | None:
    """ Get Shop Video Performance Details

     Returns detailed performance metrics for a (requested) video.

    Args:
        video_id (str):
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        granularity (GetShopVideoPerformanceDetailsGranularity | Unset):
        currency (GetShopVideoPerformanceDetailsCurrency | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopVideoPerformanceDetailsResponse
     """


    return (await asyncio_detailed(
        video_id=video_id,
client=client,
start_date_ge=start_date_ge,
end_date_lt=end_date_lt,
granularity=granularity,
currency=currency,

    )).parsed
