from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_shop_videos_performance_details_currency import GetShopVideosPerformanceDetailsCurrency
from ...models.get_shop_videos_performance_details_granularity import GetShopVideosPerformanceDetailsGranularity
from ...models.get_shop_videos_performance_details_response import GetShopVideosPerformanceDetailsResponse
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    *,
    video_ids: list[int],
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    granularity: GetShopVideosPerformanceDetailsGranularity | Unset = UNSET,
    currency: GetShopVideosPerformanceDetailsCurrency | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_video_ids = video_ids


    params["video_ids"] = json_video_ids

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
        "url": "/analytics/202609/shop_videos/batch_performance",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetShopVideosPerformanceDetailsResponse | None:
    if response.status_code == 200:
        response_200 = GetShopVideosPerformanceDetailsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetShopVideosPerformanceDetailsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    video_ids: list[int],
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    granularity: GetShopVideosPerformanceDetailsGranularity | Unset = UNSET,
    currency: GetShopVideosPerformanceDetailsCurrency | Unset = UNSET,

) -> Response[GetShopVideosPerformanceDetailsResponse]:
    """ Get Shop Videos Performance Details

     Returns detailed performance metrics for the requested videos.

    Args:
        video_ids (list[int]):
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        granularity (GetShopVideosPerformanceDetailsGranularity | Unset):
        currency (GetShopVideosPerformanceDetailsCurrency | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopVideosPerformanceDetailsResponse]
     """


    kwargs = _get_kwargs(
        video_ids=video_ids,
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
    video_ids: list[int],
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    granularity: GetShopVideosPerformanceDetailsGranularity | Unset = UNSET,
    currency: GetShopVideosPerformanceDetailsCurrency | Unset = UNSET,

) -> GetShopVideosPerformanceDetailsResponse | None:
    """ Get Shop Videos Performance Details

     Returns detailed performance metrics for the requested videos.

    Args:
        video_ids (list[int]):
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        granularity (GetShopVideosPerformanceDetailsGranularity | Unset):
        currency (GetShopVideosPerformanceDetailsCurrency | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopVideosPerformanceDetailsResponse
     """


    return sync_detailed(
        client=client,
video_ids=video_ids,
start_date_ge=start_date_ge,
end_date_lt=end_date_lt,
granularity=granularity,
currency=currency,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    video_ids: list[int],
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    granularity: GetShopVideosPerformanceDetailsGranularity | Unset = UNSET,
    currency: GetShopVideosPerformanceDetailsCurrency | Unset = UNSET,

) -> Response[GetShopVideosPerformanceDetailsResponse]:
    """ Get Shop Videos Performance Details

     Returns detailed performance metrics for the requested videos.

    Args:
        video_ids (list[int]):
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        granularity (GetShopVideosPerformanceDetailsGranularity | Unset):
        currency (GetShopVideosPerformanceDetailsCurrency | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopVideosPerformanceDetailsResponse]
     """


    kwargs = _get_kwargs(
        video_ids=video_ids,
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
    video_ids: list[int],
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    granularity: GetShopVideosPerformanceDetailsGranularity | Unset = UNSET,
    currency: GetShopVideosPerformanceDetailsCurrency | Unset = UNSET,

) -> GetShopVideosPerformanceDetailsResponse | None:
    """ Get Shop Videos Performance Details

     Returns detailed performance metrics for the requested videos.

    Args:
        video_ids (list[int]):
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        granularity (GetShopVideosPerformanceDetailsGranularity | Unset):
        currency (GetShopVideosPerformanceDetailsCurrency | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopVideosPerformanceDetailsResponse
     """


    return (await asyncio_detailed(
        client=client,
video_ids=video_ids,
start_date_ge=start_date_ge,
end_date_lt=end_date_lt,
granularity=granularity,
currency=currency,

    )).parsed
