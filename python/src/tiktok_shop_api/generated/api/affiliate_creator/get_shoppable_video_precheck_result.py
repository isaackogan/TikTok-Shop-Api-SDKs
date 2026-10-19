from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_shoppable_video_precheck_result_response import GetShoppableVideoPrecheckResultResponse
from ...types import Response


def _get_kwargs(
    task_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/affiliate_creator/202601/videos/precheck_tasks/{task_id}".format(
            task_id=quote(str(task_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetShoppableVideoPrecheckResultResponse | None:
    if response.status_code == 200:
        response_200 = GetShoppableVideoPrecheckResultResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetShoppableVideoPrecheckResultResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    task_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetShoppableVideoPrecheckResultResponse]:
    """Get Shoppable Video Precheck Result

     Retrieve the violation and, when enabled, good-quality check results for a video precheck task. If a
    returned check status is `PROCESSING`, call this API again later. If a check status is `FAIL`,
    review its `issues` field for the detected issues and suggested improvements.

    Args:
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShoppableVideoPrecheckResultResponse]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    task_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetShoppableVideoPrecheckResultResponse | None:
    """Get Shoppable Video Precheck Result

     Retrieve the violation and, when enabled, good-quality check results for a video precheck task. If a
    returned check status is `PROCESSING`, call this API again later. If a check status is `FAIL`,
    review its `issues` field for the detected issues and suggested improvements.

    Args:
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShoppableVideoPrecheckResultResponse
    """

    return sync_detailed(
        task_id=task_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    task_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetShoppableVideoPrecheckResultResponse]:
    """Get Shoppable Video Precheck Result

     Retrieve the violation and, when enabled, good-quality check results for a video precheck task. If a
    returned check status is `PROCESSING`, call this API again later. If a check status is `FAIL`,
    review its `issues` field for the detected issues and suggested improvements.

    Args:
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShoppableVideoPrecheckResultResponse]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    task_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetShoppableVideoPrecheckResultResponse | None:
    """Get Shoppable Video Precheck Result

     Retrieve the violation and, when enabled, good-quality check results for a video precheck task. If a
    returned check status is `PROCESSING`, call this API again later. If a check status is `FAIL`,
    review its `issues` field for the detected issues and suggested improvements.

    Args:
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShoppableVideoPrecheckResultResponse
    """

    return (
        await asyncio_detailed(
            task_id=task_id,
            client=client,
        )
    ).parsed
