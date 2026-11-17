from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.list_post_view_search_videos_response import ListPostViewSearchVideosResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    author_type: str | Unset = UNSET,
    optimization_inputs: str | Unset = UNSET,
    video_id: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    start_date_ge: str | Unset = UNSET,
    end_date_le: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["author_type"] = author_type

    params["optimization_inputs"] = optimization_inputs

    params["video_id"] = video_id

    params["page_size"] = page_size

    params["page_token"] = page_token

    params["start_date_ge"] = start_date_ge

    params["end_date_le"] = end_date_le


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/product/202611/search_videos",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ListPostViewSearchVideosResponse | None:
    if response.status_code == 200:
        response_200 = ListPostViewSearchVideosResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ListPostViewSearchVideosResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    author_type: str | Unset = UNSET,
    optimization_inputs: str | Unset = UNSET,
    video_id: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    start_date_ge: str | Unset = UNSET,
    end_date_le: str | Unset = UNSET,

) -> Response[ListPostViewSearchVideosResponse]:
    """ List Post-view Search Videos

     Only US shops are supported. Returns videos in the authorized shop's available data. ALL sorts by
    video views descending, then video ID descending. INPUTS_ADDED follows most-recent operation order;
    videos absent from the selected data period are omitted. Both modes support only the first 10,000
    source records. Collections can change between requests; pagination is not a snapshot. Use the
    returned start_date and end_date on subsequent pages to keep the period fixed.

    Args:
        author_type (str | Unset):
        optimization_inputs (str | Unset):
        video_id (str | Unset):
        page_size (int | Unset):
        page_token (str | Unset):
        start_date_ge (str | Unset):
        end_date_le (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListPostViewSearchVideosResponse]
     """


    kwargs = _get_kwargs(
        author_type=author_type,
optimization_inputs=optimization_inputs,
video_id=video_id,
page_size=page_size,
page_token=page_token,
start_date_ge=start_date_ge,
end_date_le=end_date_le,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    author_type: str | Unset = UNSET,
    optimization_inputs: str | Unset = UNSET,
    video_id: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    start_date_ge: str | Unset = UNSET,
    end_date_le: str | Unset = UNSET,

) -> ListPostViewSearchVideosResponse | None:
    """ List Post-view Search Videos

     Only US shops are supported. Returns videos in the authorized shop's available data. ALL sorts by
    video views descending, then video ID descending. INPUTS_ADDED follows most-recent operation order;
    videos absent from the selected data period are omitted. Both modes support only the first 10,000
    source records. Collections can change between requests; pagination is not a snapshot. Use the
    returned start_date and end_date on subsequent pages to keep the period fixed.

    Args:
        author_type (str | Unset):
        optimization_inputs (str | Unset):
        video_id (str | Unset):
        page_size (int | Unset):
        page_token (str | Unset):
        start_date_ge (str | Unset):
        end_date_le (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListPostViewSearchVideosResponse
     """


    return sync_detailed(
        client=client,
author_type=author_type,
optimization_inputs=optimization_inputs,
video_id=video_id,
page_size=page_size,
page_token=page_token,
start_date_ge=start_date_ge,
end_date_le=end_date_le,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    author_type: str | Unset = UNSET,
    optimization_inputs: str | Unset = UNSET,
    video_id: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    start_date_ge: str | Unset = UNSET,
    end_date_le: str | Unset = UNSET,

) -> Response[ListPostViewSearchVideosResponse]:
    """ List Post-view Search Videos

     Only US shops are supported. Returns videos in the authorized shop's available data. ALL sorts by
    video views descending, then video ID descending. INPUTS_ADDED follows most-recent operation order;
    videos absent from the selected data period are omitted. Both modes support only the first 10,000
    source records. Collections can change between requests; pagination is not a snapshot. Use the
    returned start_date and end_date on subsequent pages to keep the period fixed.

    Args:
        author_type (str | Unset):
        optimization_inputs (str | Unset):
        video_id (str | Unset):
        page_size (int | Unset):
        page_token (str | Unset):
        start_date_ge (str | Unset):
        end_date_le (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListPostViewSearchVideosResponse]
     """


    kwargs = _get_kwargs(
        author_type=author_type,
optimization_inputs=optimization_inputs,
video_id=video_id,
page_size=page_size,
page_token=page_token,
start_date_ge=start_date_ge,
end_date_le=end_date_le,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    author_type: str | Unset = UNSET,
    optimization_inputs: str | Unset = UNSET,
    video_id: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    start_date_ge: str | Unset = UNSET,
    end_date_le: str | Unset = UNSET,

) -> ListPostViewSearchVideosResponse | None:
    """ List Post-view Search Videos

     Only US shops are supported. Returns videos in the authorized shop's available data. ALL sorts by
    video views descending, then video ID descending. INPUTS_ADDED follows most-recent operation order;
    videos absent from the selected data period are omitted. Both modes support only the first 10,000
    source records. Collections can change between requests; pagination is not a snapshot. Use the
    returned start_date and end_date on subsequent pages to keep the period fixed.

    Args:
        author_type (str | Unset):
        optimization_inputs (str | Unset):
        video_id (str | Unset):
        page_size (int | Unset):
        page_token (str | Unset):
        start_date_ge (str | Unset):
        end_date_le (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListPostViewSearchVideosResponse
     """


    return (await asyncio_detailed(
        client=client,
author_type=author_type,
optimization_inputs=optimization_inputs,
video_id=video_id,
page_size=page_size,
page_token=page_token,
start_date_ge=start_date_ge,
end_date_le=end_date_le,

    )).parsed
