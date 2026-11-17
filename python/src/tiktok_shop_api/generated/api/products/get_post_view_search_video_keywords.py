from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_post_view_search_video_keywords_response import GetPostViewSearchVideoKeywordsResponse
from typing import cast



def _get_kwargs(
    video_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/product/202611/search_videos/{video_id}/keywords".format(video_id=quote(str(video_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetPostViewSearchVideoKeywordsResponse | None:
    if response.status_code == 200:
        response_200 = GetPostViewSearchVideoKeywordsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetPostViewSearchVideoKeywordsResponse]:
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

) -> Response[GetPostViewSearchVideoKeywordsResponse]:
    """ Get Post-view Search Video Keywords

     Only US shops are supported. The video must be present in the authorized shop's warehouse data for
    the
    latest 90 calendar days ending on the latest available data date, including both endpoints. Returns
    the current configured keyword set; an empty array means none are configured. Popular search
    keywords
    are separate observation data.

    Args:
        video_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPostViewSearchVideoKeywordsResponse]
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

) -> GetPostViewSearchVideoKeywordsResponse | None:
    """ Get Post-view Search Video Keywords

     Only US shops are supported. The video must be present in the authorized shop's warehouse data for
    the
    latest 90 calendar days ending on the latest available data date, including both endpoints. Returns
    the current configured keyword set; an empty array means none are configured. Popular search
    keywords
    are separate observation data.

    Args:
        video_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPostViewSearchVideoKeywordsResponse
     """


    return sync_detailed(
        video_id=video_id,
client=client,

    ).parsed

async def asyncio_detailed(
    video_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetPostViewSearchVideoKeywordsResponse]:
    """ Get Post-view Search Video Keywords

     Only US shops are supported. The video must be present in the authorized shop's warehouse data for
    the
    latest 90 calendar days ending on the latest available data date, including both endpoints. Returns
    the current configured keyword set; an empty array means none are configured. Popular search
    keywords
    are separate observation data.

    Args:
        video_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPostViewSearchVideoKeywordsResponse]
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

) -> GetPostViewSearchVideoKeywordsResponse | None:
    """ Get Post-view Search Video Keywords

     Only US shops are supported. The video must be present in the authorized shop's warehouse data for
    the
    latest 90 calendar days ending on the latest available data date, including both endpoints. Returns
    the current configured keyword set; an empty array means none are configured. Popular search
    keywords
    are separate observation data.

    Args:
        video_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPostViewSearchVideoKeywordsResponse
     """


    return (await asyncio_detailed(
        video_id=video_id,
client=client,

    )).parsed
