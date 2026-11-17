from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.add_post_view_search_video_comment_request import AddPostViewSearchVideoCommentRequest
from ...models.add_post_view_search_video_comment_response import AddPostViewSearchVideoCommentResponse
from typing import cast



def _get_kwargs(
    video_id: str,
    *,
    body: AddPostViewSearchVideoCommentRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202611/search_videos/{video_id}/comments".format(video_id=quote(str(video_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AddPostViewSearchVideoCommentResponse | None:
    if response.status_code == 200:
        response_200 = AddPostViewSearchVideoCommentResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AddPostViewSearchVideoCommentResponse]:
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
    body: AddPostViewSearchVideoCommentRequest,

) -> Response[AddPostViewSearchVideoCommentResponse]:
    """ Add Post-view Search Video Comment

     Only US shops are supported. The video must be present in the authorized shop's warehouse data for
    the
    latest 90 calendar days ending on the latest available data date, including both endpoints. The
    request changes one video. Inspect the business result even when the response code is zero. The
    request timeout is 10 seconds; a timeout or request-level error does not prove that nothing changed.
    Do not automatically retry writes. Each invocation has a new server-generated submission ID and
    cannot
    resume an earlier request. Only self-posted shop videos are supported. Adds one nonblank comment of
    at
    most 500 Unicode characters; existing comments are preserved. Repeating a request may publish a
    duplicate comment. Existing downstream publication and frequency rules apply. After an unknown
    outcome, inspect recent comments, but absence from that limited view or matching text cannot
    identify
    this request conclusively. If the result remains uncertain, contact support with the request log ID
    instead of resubmitting. Concurrent changes to the same video may overwrite keyword updates. Avoid
    simultaneous writes for one video.

    Args:
        video_id (str):
        body (AddPostViewSearchVideoCommentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddPostViewSearchVideoCommentResponse]
     """


    kwargs = _get_kwargs(
        video_id=video_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    video_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AddPostViewSearchVideoCommentRequest,

) -> AddPostViewSearchVideoCommentResponse | None:
    """ Add Post-view Search Video Comment

     Only US shops are supported. The video must be present in the authorized shop's warehouse data for
    the
    latest 90 calendar days ending on the latest available data date, including both endpoints. The
    request changes one video. Inspect the business result even when the response code is zero. The
    request timeout is 10 seconds; a timeout or request-level error does not prove that nothing changed.
    Do not automatically retry writes. Each invocation has a new server-generated submission ID and
    cannot
    resume an earlier request. Only self-posted shop videos are supported. Adds one nonblank comment of
    at
    most 500 Unicode characters; existing comments are preserved. Repeating a request may publish a
    duplicate comment. Existing downstream publication and frequency rules apply. After an unknown
    outcome, inspect recent comments, but absence from that limited view or matching text cannot
    identify
    this request conclusively. If the result remains uncertain, contact support with the request log ID
    instead of resubmitting. Concurrent changes to the same video may overwrite keyword updates. Avoid
    simultaneous writes for one video.

    Args:
        video_id (str):
        body (AddPostViewSearchVideoCommentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddPostViewSearchVideoCommentResponse
     """


    return sync_detailed(
        video_id=video_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    video_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AddPostViewSearchVideoCommentRequest,

) -> Response[AddPostViewSearchVideoCommentResponse]:
    """ Add Post-view Search Video Comment

     Only US shops are supported. The video must be present in the authorized shop's warehouse data for
    the
    latest 90 calendar days ending on the latest available data date, including both endpoints. The
    request changes one video. Inspect the business result even when the response code is zero. The
    request timeout is 10 seconds; a timeout or request-level error does not prove that nothing changed.
    Do not automatically retry writes. Each invocation has a new server-generated submission ID and
    cannot
    resume an earlier request. Only self-posted shop videos are supported. Adds one nonblank comment of
    at
    most 500 Unicode characters; existing comments are preserved. Repeating a request may publish a
    duplicate comment. Existing downstream publication and frequency rules apply. After an unknown
    outcome, inspect recent comments, but absence from that limited view or matching text cannot
    identify
    this request conclusively. If the result remains uncertain, contact support with the request log ID
    instead of resubmitting. Concurrent changes to the same video may overwrite keyword updates. Avoid
    simultaneous writes for one video.

    Args:
        video_id (str):
        body (AddPostViewSearchVideoCommentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddPostViewSearchVideoCommentResponse]
     """


    kwargs = _get_kwargs(
        video_id=video_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    video_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AddPostViewSearchVideoCommentRequest,

) -> AddPostViewSearchVideoCommentResponse | None:
    """ Add Post-view Search Video Comment

     Only US shops are supported. The video must be present in the authorized shop's warehouse data for
    the
    latest 90 calendar days ending on the latest available data date, including both endpoints. The
    request changes one video. Inspect the business result even when the response code is zero. The
    request timeout is 10 seconds; a timeout or request-level error does not prove that nothing changed.
    Do not automatically retry writes. Each invocation has a new server-generated submission ID and
    cannot
    resume an earlier request. Only self-posted shop videos are supported. Adds one nonblank comment of
    at
    most 500 Unicode characters; existing comments are preserved. Repeating a request may publish a
    duplicate comment. Existing downstream publication and frequency rules apply. After an unknown
    outcome, inspect recent comments, but absence from that limited view or matching text cannot
    identify
    this request conclusively. If the result remains uncertain, contact support with the request log ID
    instead of resubmitting. Concurrent changes to the same video may overwrite keyword updates. Avoid
    simultaneous writes for one video.

    Args:
        video_id (str):
        body (AddPostViewSearchVideoCommentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddPostViewSearchVideoCommentResponse
     """


    return (await asyncio_detailed(
        video_id=video_id,
client=client,
body=body,

    )).parsed
