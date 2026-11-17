from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_post_view_search_video_response import GetPostViewSearchVideoResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    video_id: str,
    *,
    start_date_ge: str | Unset = UNSET,
    end_date_le: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["start_date_ge"] = start_date_ge

    params["end_date_le"] = end_date_le


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/product/202611/search_videos/{video_id}".format(video_id=quote(str(video_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetPostViewSearchVideoResponse | None:
    if response.status_code == 200:
        response_200 = GetPostViewSearchVideoResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetPostViewSearchVideoResponse]:
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
    start_date_ge: str | Unset = UNSET,
    end_date_le: str | Unset = UNSET,

) -> Response[GetPostViewSearchVideoResponse]:
    """ Get Post-view Search Video

     Only US shops are supported. Returns video metadata, period metrics and current configuration for a
    video found in the authorized shop's data. Missing video data or a failed access check fails the
    request. Self-posted video detail also requires the author to be resolved for comment retrieval.

    Args:
        video_id (str):
        start_date_ge (str | Unset):
        end_date_le (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPostViewSearchVideoResponse]
     """


    kwargs = _get_kwargs(
        video_id=video_id,
start_date_ge=start_date_ge,
end_date_le=end_date_le,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    video_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_date_ge: str | Unset = UNSET,
    end_date_le: str | Unset = UNSET,

) -> GetPostViewSearchVideoResponse | None:
    """ Get Post-view Search Video

     Only US shops are supported. Returns video metadata, period metrics and current configuration for a
    video found in the authorized shop's data. Missing video data or a failed access check fails the
    request. Self-posted video detail also requires the author to be resolved for comment retrieval.

    Args:
        video_id (str):
        start_date_ge (str | Unset):
        end_date_le (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPostViewSearchVideoResponse
     """


    return sync_detailed(
        video_id=video_id,
client=client,
start_date_ge=start_date_ge,
end_date_le=end_date_le,

    ).parsed

async def asyncio_detailed(
    video_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_date_ge: str | Unset = UNSET,
    end_date_le: str | Unset = UNSET,

) -> Response[GetPostViewSearchVideoResponse]:
    """ Get Post-view Search Video

     Only US shops are supported. Returns video metadata, period metrics and current configuration for a
    video found in the authorized shop's data. Missing video data or a failed access check fails the
    request. Self-posted video detail also requires the author to be resolved for comment retrieval.

    Args:
        video_id (str):
        start_date_ge (str | Unset):
        end_date_le (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPostViewSearchVideoResponse]
     """


    kwargs = _get_kwargs(
        video_id=video_id,
start_date_ge=start_date_ge,
end_date_le=end_date_le,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    video_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_date_ge: str | Unset = UNSET,
    end_date_le: str | Unset = UNSET,

) -> GetPostViewSearchVideoResponse | None:
    """ Get Post-view Search Video

     Only US shops are supported. Returns video metadata, period metrics and current configuration for a
    video found in the authorized shop's data. Missing video data or a failed access check fails the
    request. Self-posted video detail also requires the author to be resolved for comment retrieval.

    Args:
        video_id (str):
        start_date_ge (str | Unset):
        end_date_le (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPostViewSearchVideoResponse
     """


    return (await asyncio_detailed(
        video_id=video_id,
client=client,
start_date_ge=start_date_ge,
end_date_le=end_date_le,

    )).parsed
