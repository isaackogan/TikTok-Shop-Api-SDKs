from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_live_room_core_stats_response import GetLiveRoomCoreStatsResponse
from typing import cast



def _get_kwargs(
    live_room_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202502/live_rooms/{live_room_id}/core_stats".format(live_room_id=quote(str(live_room_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetLiveRoomCoreStatsResponse | None:
    if response.status_code == 200:
        response_200 = GetLiveRoomCoreStatsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetLiveRoomCoreStatsResponse]:
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

) -> Response[GetLiveRoomCoreStatsResponse]:
    """ Get Live Room Core Stats

     Returns core stats for the specified live room, including GMV, order counts, buyer counts, product
    click counts, and view counts.

    Args:
        live_room_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLiveRoomCoreStatsResponse]
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

) -> GetLiveRoomCoreStatsResponse | None:
    """ Get Live Room Core Stats

     Returns core stats for the specified live room, including GMV, order counts, buyer counts, product
    click counts, and view counts.

    Args:
        live_room_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetLiveRoomCoreStatsResponse
     """


    return sync_detailed(
        live_room_id=live_room_id,
client=client,

    ).parsed

async def asyncio_detailed(
    live_room_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetLiveRoomCoreStatsResponse]:
    """ Get Live Room Core Stats

     Returns core stats for the specified live room, including GMV, order counts, buyer counts, product
    click counts, and view counts.

    Args:
        live_room_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLiveRoomCoreStatsResponse]
     """


    kwargs = _get_kwargs(
        live_room_id=live_room_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    live_room_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> GetLiveRoomCoreStatsResponse | None:
    """ Get Live Room Core Stats

     Returns core stats for the specified live room, including GMV, order counts, buyer counts, product
    click counts, and view counts.

    Args:
        live_room_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetLiveRoomCoreStatsResponse
     """


    return (await asyncio_detailed(
        live_room_id=live_room_id,
client=client,

    )).parsed
