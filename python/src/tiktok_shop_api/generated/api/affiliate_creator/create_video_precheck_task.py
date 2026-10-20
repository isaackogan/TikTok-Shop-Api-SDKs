from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_video_precheck_task_request import CreateVideoPrecheckTaskRequest
from ...models.create_video_precheck_task_response import CreateVideoPrecheckTaskResponse
from typing import cast



def _get_kwargs(
    *,
    body: CreateVideoPrecheckTaskRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_creator/202511/videos/precheck_task",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateVideoPrecheckTaskResponse | None:
    if response.status_code == 200:
        response_200 = CreateVideoPrecheckTaskResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateVideoPrecheckTaskResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateVideoPrecheckTaskRequest,

) -> Response[CreateVideoPrecheckTaskResponse]:
    """ Create Video Precheck Task

     Use this API to create a task that checks a video and its shoppable content anchor for violations.
    If the task is created successfully, the response returns a task ID.

    Args:
        body (CreateVideoPrecheckTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateVideoPrecheckTaskResponse]
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
    body: CreateVideoPrecheckTaskRequest,

) -> CreateVideoPrecheckTaskResponse | None:
    """ Create Video Precheck Task

     Use this API to create a task that checks a video and its shoppable content anchor for violations.
    If the task is created successfully, the response returns a task ID.

    Args:
        body (CreateVideoPrecheckTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateVideoPrecheckTaskResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateVideoPrecheckTaskRequest,

) -> Response[CreateVideoPrecheckTaskResponse]:
    """ Create Video Precheck Task

     Use this API to create a task that checks a video and its shoppable content anchor for violations.
    If the task is created successfully, the response returns a task ID.

    Args:
        body (CreateVideoPrecheckTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateVideoPrecheckTaskResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateVideoPrecheckTaskRequest,

) -> CreateVideoPrecheckTaskResponse | None:
    """ Create Video Precheck Task

     Use this API to create a task that checks a video and its shoppable content anchor for violations.
    If the task is created successfully, the response returns a task ID.

    Args:
        body (CreateVideoPrecheckTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateVideoPrecheckTaskResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
