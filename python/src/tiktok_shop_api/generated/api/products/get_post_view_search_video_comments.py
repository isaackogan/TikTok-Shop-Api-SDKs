from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_post_view_search_video_comments_response import GetPostViewSearchVideoCommentsResponse
from typing import cast



def _get_kwargs(
    video_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/product/202611/search_videos/{video_id}/comments".format(video_id=quote(str(video_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetPostViewSearchVideoCommentsResponse | None:
    if response.status_code == 200:
        response_200 = GetPostViewSearchVideoCommentsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetPostViewSearchVideoCommentsResponse]:
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

) -> Response[GetPostViewSearchVideoCommentsResponse]:
    """ Get Post-view Search Video Comments

     Only US shops are supported. The video must be present in the authorized shop's warehouse data for
    the
    latest 90 calendar days ending on the latest available data date, including both endpoints. Only
    self-
    posted shop videos are supported. Business policy permits access only to the latest 50 comments
    published through post-view search
    by the video author for one video. This is the accessible query window, not a limit on the total
    number of published comments. Results are ordered by creation time descending. Missing or invalid
    times sort last; equal times preserve source order. Earlier comments are outside the API access
    scope; pagination is not supported. Other user comments are excluded. An empty array
    means no matching comments were returned; it does not prove an earlier timed-out submission failed.
    If
    any underlying read fails or the 10-second budget expires, the request fails.

    Args:
        video_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPostViewSearchVideoCommentsResponse]
     """


    kwargs = _get_kwargs(
        video_id=video_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    video_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> GetPostViewSearchVideoCommentsResponse | None:
    """ Get Post-view Search Video Comments

     Only US shops are supported. The video must be present in the authorized shop's warehouse data for
    the
    latest 90 calendar days ending on the latest available data date, including both endpoints. Only
    self-
    posted shop videos are supported. Business policy permits access only to the latest 50 comments
    published through post-view search
    by the video author for one video. This is the accessible query window, not a limit on the total
    number of published comments. Results are ordered by creation time descending. Missing or invalid
    times sort last; equal times preserve source order. Earlier comments are outside the API access
    scope; pagination is not supported. Other user comments are excluded. An empty array
    means no matching comments were returned; it does not prove an earlier timed-out submission failed.
    If
    any underlying read fails or the 10-second budget expires, the request fails.

    Args:
        video_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPostViewSearchVideoCommentsResponse
     """


    return sync_detailed(
        video_id=video_id,
client=client,

    ).parsed

async def asyncio_detailed(
    video_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetPostViewSearchVideoCommentsResponse]:
    """ Get Post-view Search Video Comments

     Only US shops are supported. The video must be present in the authorized shop's warehouse data for
    the
    latest 90 calendar days ending on the latest available data date, including both endpoints. Only
    self-
    posted shop videos are supported. Business policy permits access only to the latest 50 comments
    published through post-view search
    by the video author for one video. This is the accessible query window, not a limit on the total
    number of published comments. Results are ordered by creation time descending. Missing or invalid
    times sort last; equal times preserve source order. Earlier comments are outside the API access
    scope; pagination is not supported. Other user comments are excluded. An empty array
    means no matching comments were returned; it does not prove an earlier timed-out submission failed.
    If
    any underlying read fails or the 10-second budget expires, the request fails.

    Args:
        video_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPostViewSearchVideoCommentsResponse]
     """


    kwargs = _get_kwargs(
        video_id=video_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    video_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> GetPostViewSearchVideoCommentsResponse | None:
    """ Get Post-view Search Video Comments

     Only US shops are supported. The video must be present in the authorized shop's warehouse data for
    the
    latest 90 calendar days ending on the latest available data date, including both endpoints. Only
    self-
    posted shop videos are supported. Business policy permits access only to the latest 50 comments
    published through post-view search
    by the video author for one video. This is the accessible query window, not a limit on the total
    number of published comments. Results are ordered by creation time descending. Missing or invalid
    times sort last; equal times preserve source order. Earlier comments are outside the API access
    scope; pagination is not supported. Other user comments are excluded. An empty array
    means no matching comments were returned; it does not prove an earlier timed-out submission failed.
    If
    any underlying read fails or the 10-second budget expires, the request fails.

    Args:
        video_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPostViewSearchVideoCommentsResponse
     """


    return (await asyncio_detailed(
        video_id=video_id,
client=client,

    )).parsed
