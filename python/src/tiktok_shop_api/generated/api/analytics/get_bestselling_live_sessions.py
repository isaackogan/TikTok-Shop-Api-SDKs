import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_bestselling_live_sessions_response import GetBestsellingLIVESessionsResponse
from ...models.get_bestselling_live_sessions_time_slot import GetBestsellingLiveSessionsTimeSlot
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date: datetime.date | Unset = UNSET,
    time_slot: GetBestsellingLiveSessionsTimeSlot | Unset = UNSET,
    currency: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_date: str | Unset = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    json_time_slot: str | Unset = UNSET
    if not isinstance(time_slot, Unset):
        json_time_slot = time_slot.value

    params["time_slot"] = json_time_slot

    params["currency"] = currency

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202511/lives/bestselling",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetBestsellingLIVESessionsResponse | None:
    if response.status_code == 200:
        response_200 = GetBestsellingLIVESessionsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetBestsellingLIVESessionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    date: datetime.date | Unset = UNSET,
    time_slot: GetBestsellingLiveSessionsTimeSlot | Unset = UNSET,
    currency: str | Unset = UNSET,
) -> Response[GetBestsellingLIVESessionsResponse]:
    """Get Bestselling LIVE Sessions

     Get up to 100 LIVE sessions ranked by GMV for the period defined by `date` and `time_slot`.

    Args:
        date (datetime.date | Unset):
        time_slot (GetBestsellingLiveSessionsTimeSlot | Unset):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBestsellingLIVESessionsResponse]
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
    date: datetime.date | Unset = UNSET,
    time_slot: GetBestsellingLiveSessionsTimeSlot | Unset = UNSET,
    currency: str | Unset = UNSET,
) -> GetBestsellingLIVESessionsResponse | None:
    """Get Bestselling LIVE Sessions

     Get up to 100 LIVE sessions ranked by GMV for the period defined by `date` and `time_slot`.

    Args:
        date (datetime.date | Unset):
        time_slot (GetBestsellingLiveSessionsTimeSlot | Unset):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBestsellingLIVESessionsResponse
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
    date: datetime.date | Unset = UNSET,
    time_slot: GetBestsellingLiveSessionsTimeSlot | Unset = UNSET,
    currency: str | Unset = UNSET,
) -> Response[GetBestsellingLIVESessionsResponse]:
    """Get Bestselling LIVE Sessions

     Get up to 100 LIVE sessions ranked by GMV for the period defined by `date` and `time_slot`.

    Args:
        date (datetime.date | Unset):
        time_slot (GetBestsellingLiveSessionsTimeSlot | Unset):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBestsellingLIVESessionsResponse]
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
    date: datetime.date | Unset = UNSET,
    time_slot: GetBestsellingLiveSessionsTimeSlot | Unset = UNSET,
    currency: str | Unset = UNSET,
) -> GetBestsellingLIVESessionsResponse | None:
    """Get Bestselling LIVE Sessions

     Get up to 100 LIVE sessions ranked by GMV for the period defined by `date` and `time_slot`.

    Args:
        date (datetime.date | Unset):
        time_slot (GetBestsellingLiveSessionsTimeSlot | Unset):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBestsellingLIVESessionsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            date=date,
            time_slot=time_slot,
            currency=currency,
        )
    ).parsed
