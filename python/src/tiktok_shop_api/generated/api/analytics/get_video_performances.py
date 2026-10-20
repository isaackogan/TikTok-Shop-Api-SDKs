from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_video_performances_response import GetVideoPerformancesResponse
from typing import cast



def _get_kwargs(
    *,
    video_ids: str,
    start_time_ge: int,
    end_time_le: int,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["video_ids"] = video_ids

    params["start_time_ge"] = start_time_ge

    params["end_time_le"] = end_time_le


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202403/videos/performances",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetVideoPerformancesResponse | None:
    if response.status_code == 200:
        response_200 = GetVideoPerformancesResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetVideoPerformancesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    video_ids: str,
    start_time_ge: int,
    end_time_le: int,

) -> Response[GetVideoPerformancesResponse]:
    """ Get Video Performances

     Use this US-creator-only API to retrieve TikTok e-commerce video metrics, including
    anchor_display_rate, click_through_rate, orders, items_sold, and GMV, for the requested videos.

    Args:
        video_ids (str):
        start_time_ge (int):
        end_time_le (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVideoPerformancesResponse]
     """


    kwargs = _get_kwargs(
        video_ids=video_ids,
start_time_ge=start_time_ge,
end_time_le=end_time_le,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    video_ids: str,
    start_time_ge: int,
    end_time_le: int,

) -> GetVideoPerformancesResponse | None:
    """ Get Video Performances

     Use this US-creator-only API to retrieve TikTok e-commerce video metrics, including
    anchor_display_rate, click_through_rate, orders, items_sold, and GMV, for the requested videos.

    Args:
        video_ids (str):
        start_time_ge (int):
        end_time_le (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVideoPerformancesResponse
     """


    return sync_detailed(
        client=client,
video_ids=video_ids,
start_time_ge=start_time_ge,
end_time_le=end_time_le,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    video_ids: str,
    start_time_ge: int,
    end_time_le: int,

) -> Response[GetVideoPerformancesResponse]:
    """ Get Video Performances

     Use this US-creator-only API to retrieve TikTok e-commerce video metrics, including
    anchor_display_rate, click_through_rate, orders, items_sold, and GMV, for the requested videos.

    Args:
        video_ids (str):
        start_time_ge (int):
        end_time_le (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVideoPerformancesResponse]
     """


    kwargs = _get_kwargs(
        video_ids=video_ids,
start_time_ge=start_time_ge,
end_time_le=end_time_le,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    video_ids: str,
    start_time_ge: int,
    end_time_le: int,

) -> GetVideoPerformancesResponse | None:
    """ Get Video Performances

     Use this US-creator-only API to retrieve TikTok e-commerce video metrics, including
    anchor_display_rate, click_through_rate, orders, items_sold, and GMV, for the requested videos.

    Args:
        video_ids (str):
        start_time_ge (int):
        end_time_le (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVideoPerformancesResponse
     """


    return (await asyncio_detailed(
        client=client,
video_ids=video_ids,
start_time_ge=start_time_ge,
end_time_le=end_time_le,

    )).parsed
