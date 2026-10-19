from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_shoppable_video_request import PostShoppableVideoRequest
from ...models.post_shoppable_video_response import PostShoppableVideoResponse
from ...types import Response


def _get_kwargs(
    *,
    body: PostShoppableVideoRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_creator/202603/videos",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PostShoppableVideoResponse | None:
    if response.status_code == 200:
        response_200 = PostShoppableVideoResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PostShoppableVideoResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostShoppableVideoRequest,
) -> Response[PostShoppableVideoResponse]:
    """Post Shoppable Video

     Use this API to submit a shoppable video for publishing. When the submission succeeds, pass the
    returned video ID as the `video_id` path parameter to Get Shoppable Video Status (`GET
    /affiliate_creator/202509/videos/{video_id}/status`) to retrieve the posting status: `PROCESSING`,
    `SUCCESS`, or `FAIL`. If the status is `PROCESSING`, call the status API again later to check for a
    terminal status.

    Args:
        body (PostShoppableVideoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostShoppableVideoResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: PostShoppableVideoRequest,
) -> PostShoppableVideoResponse | None:
    """Post Shoppable Video

     Use this API to submit a shoppable video for publishing. When the submission succeeds, pass the
    returned video ID as the `video_id` path parameter to Get Shoppable Video Status (`GET
    /affiliate_creator/202509/videos/{video_id}/status`) to retrieve the posting status: `PROCESSING`,
    `SUCCESS`, or `FAIL`. If the status is `PROCESSING`, call the status API again later to check for a
    terminal status.

    Args:
        body (PostShoppableVideoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostShoppableVideoResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostShoppableVideoRequest,
) -> Response[PostShoppableVideoResponse]:
    """Post Shoppable Video

     Use this API to submit a shoppable video for publishing. When the submission succeeds, pass the
    returned video ID as the `video_id` path parameter to Get Shoppable Video Status (`GET
    /affiliate_creator/202509/videos/{video_id}/status`) to retrieve the posting status: `PROCESSING`,
    `SUCCESS`, or `FAIL`. If the status is `PROCESSING`, call the status API again later to check for a
    terminal status.

    Args:
        body (PostShoppableVideoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostShoppableVideoResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostShoppableVideoRequest,
) -> PostShoppableVideoResponse | None:
    """Post Shoppable Video

     Use this API to submit a shoppable video for publishing. When the submission succeeds, pass the
    returned video ID as the `video_id` path parameter to Get Shoppable Video Status (`GET
    /affiliate_creator/202509/videos/{video_id}/status`) to retrieve the posting status: `PROCESSING`,
    `SUCCESS`, or `FAIL`. If the status is `PROCESSING`, call the status API again later to check for a
    terminal status.

    Args:
        body (PostShoppableVideoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostShoppableVideoResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
