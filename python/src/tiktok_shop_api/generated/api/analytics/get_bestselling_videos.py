import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_bestselling_videos_response import GetBestsellingVideosResponse
from ...models.get_bestselling_videos_time_slot import GetBestsellingVideosTimeSlot
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date: datetime.date,
    time_slot: GetBestsellingVideosTimeSlot,
    currency: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_date = date.isoformat()
    params["date"] = json_date

    json_time_slot = time_slot.value
    params["time_slot"] = json_time_slot

    params["currency"] = currency

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202511/videos/bestselling",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetBestsellingVideosResponse | None:
    if response.status_code == 200:
        response_200 = GetBestsellingVideosResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetBestsellingVideosResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    date: datetime.date,
    time_slot: GetBestsellingVideosTimeSlot,
    currency: str | Unset = UNSET,
) -> Response[GetBestsellingVideosResponse]:
    """Get Bestselling Videos

     Returns up to 100 videos ranked by gross merchandise value (GMV) in descending order for the date
    range selected by `date` and `time_slot`.

    Args:
        date (datetime.date):
        time_slot (GetBestsellingVideosTimeSlot):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBestsellingVideosResponse]
    """

    kwargs = _get_kwargs(
        date=date,
        time_slot=time_slot,
        currency=currency,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    date: datetime.date,
    time_slot: GetBestsellingVideosTimeSlot,
    currency: str | Unset = UNSET,
) -> GetBestsellingVideosResponse | None:
    """Get Bestselling Videos

     Returns up to 100 videos ranked by gross merchandise value (GMV) in descending order for the date
    range selected by `date` and `time_slot`.

    Args:
        date (datetime.date):
        time_slot (GetBestsellingVideosTimeSlot):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBestsellingVideosResponse
    """

    return sync_detailed(
        client=client,
        date=date,
        time_slot=time_slot,
        currency=currency,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    date: datetime.date,
    time_slot: GetBestsellingVideosTimeSlot,
    currency: str | Unset = UNSET,
) -> Response[GetBestsellingVideosResponse]:
    """Get Bestselling Videos

     Returns up to 100 videos ranked by gross merchandise value (GMV) in descending order for the date
    range selected by `date` and `time_slot`.

    Args:
        date (datetime.date):
        time_slot (GetBestsellingVideosTimeSlot):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBestsellingVideosResponse]
    """

    kwargs = _get_kwargs(
        date=date,
        time_slot=time_slot,
        currency=currency,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    date: datetime.date,
    time_slot: GetBestsellingVideosTimeSlot,
    currency: str | Unset = UNSET,
) -> GetBestsellingVideosResponse | None:
    """Get Bestselling Videos

     Returns up to 100 videos ranked by gross merchandise value (GMV) in descending order for the date
    range selected by `date` and `time_slot`.

    Args:
        date (datetime.date):
        time_slot (GetBestsellingVideosTimeSlot):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBestsellingVideosResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            date=date,
            time_slot=time_slot,
            currency=currency,
        )
    ).parsed
