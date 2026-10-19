from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_live_room_user_portraits_response import GetLiveRoomUserPortraitsResponse
from ...types import Response


def _get_kwargs(
    live_room_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202502/live_rooms/{live_room_id}/user_portraits".format(
            live_room_id=quote(str(live_room_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetLiveRoomUserPortraitsResponse | None:
    if response.status_code == 200:
        response_200 = GetLiveRoomUserPortraitsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetLiveRoomUserPortraitsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    live_room_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetLiveRoomUserPortraitsResponse]:
    """Get Live Room User Portraits

     Returns user portrait indicators for the specified live room, including age, gender, fan,
    advertisement, and region distributions.

    Args:
        live_room_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLiveRoomUserPortraitsResponse]
    """

    kwargs = _get_kwargs(
        live_room_id=live_room_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    live_room_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetLiveRoomUserPortraitsResponse | None:
    """Get Live Room User Portraits

     Returns user portrait indicators for the specified live room, including age, gender, fan,
    advertisement, and region distributions.

    Args:
        live_room_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetLiveRoomUserPortraitsResponse
    """

    return sync_detailed(
        live_room_id=live_room_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    live_room_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetLiveRoomUserPortraitsResponse]:
    """Get Live Room User Portraits

     Returns user portrait indicators for the specified live room, including age, gender, fan,
    advertisement, and region distributions.

    Args:
        live_room_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLiveRoomUserPortraitsResponse]
    """

    kwargs = _get_kwargs(
        live_room_id=live_room_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    live_room_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetLiveRoomUserPortraitsResponse | None:
    """Get Live Room User Portraits

     Returns user portrait indicators for the specified live room, including age, gender, fan,
    advertisement, and region distributions.

    Args:
        live_room_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetLiveRoomUserPortraitsResponse
    """

    return (
        await asyncio_detailed(
            live_room_id=live_room_id,
            client=client,
        )
    ).parsed
