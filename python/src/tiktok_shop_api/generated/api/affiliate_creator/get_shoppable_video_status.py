from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_shoppable_video_status_response import GetShoppableVideoStatusResponse
from ...types import Response


def _get_kwargs(
    video_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/affiliate_creator/202509/videos/{video_id}/status".format(
            video_id=quote(str(video_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetShoppableVideoStatusResponse | None:
    if response.status_code == 200:
        response_200 = GetShoppableVideoStatusResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetShoppableVideoStatusResponse]:
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
) -> Response[GetShoppableVideoStatusResponse]:
    """Get Shoppable Video Status

     Use this API to get shoppable video posting results.

    Args:
        video_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShoppableVideoStatusResponse]
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
) -> GetShoppableVideoStatusResponse | None:
    """Get Shoppable Video Status

     Use this API to get shoppable video posting results.

    Args:
        video_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShoppableVideoStatusResponse
    """

    return sync_detailed(
        video_id=video_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    video_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetShoppableVideoStatusResponse]:
    """Get Shoppable Video Status

     Use this API to get shoppable video posting results.

    Args:
        video_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShoppableVideoStatusResponse]
    """

    kwargs = _get_kwargs(
        video_id=video_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    video_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetShoppableVideoStatusResponse | None:
    """Get Shoppable Video Status

     Use this API to get shoppable video posting results.

    Args:
        video_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShoppableVideoStatusResponse
    """

    return (
        await asyncio_detailed(
            video_id=video_id,
            client=client,
        )
    ).parsed
