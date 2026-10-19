import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_bestselling_creators_author_type import GetBestsellingCreatorsAuthorType
from ...models.get_bestselling_creators_currency import GetBestsellingCreatorsCurrency
from ...models.get_bestselling_creators_response import GetBestsellingCreatorsResponse
from ...models.get_bestselling_creators_time_slot import GetBestsellingCreatorsTimeSlot
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date: datetime.date,
    time_slot: GetBestsellingCreatorsTimeSlot,
    author_type: GetBestsellingCreatorsAuthorType,
    currency: GetBestsellingCreatorsCurrency | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_date = date.isoformat()
    params["date"] = json_date

    json_time_slot = time_slot.value
    params["time_slot"] = json_time_slot

    json_author_type = author_type.value
    params["author_type"] = json_author_type

    json_currency: str | Unset = UNSET
    if not isinstance(currency, Unset):
        json_currency = currency.value

    params["currency"] = json_currency

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202511/creators/bestselling",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetBestsellingCreatorsResponse | None:
    if response.status_code == 200:
        response_200 = GetBestsellingCreatorsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetBestsellingCreatorsResponse]:
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
    time_slot: GetBestsellingCreatorsTimeSlot,
    author_type: GetBestsellingCreatorsAuthorType,
    currency: GetBestsellingCreatorsCurrency | Unset = UNSET,
) -> Response[GetBestsellingCreatorsResponse]:
    """Get Bestselling Creators

     Returns up to 100 creators, filtered by `author_type`, ranked by GMV in the selected `currency` for
    the reporting period ending on `date` and defined by `time_slot`.

    Args:
        date (datetime.date):
        time_slot (GetBestsellingCreatorsTimeSlot):
        author_type (GetBestsellingCreatorsAuthorType):
        currency (GetBestsellingCreatorsCurrency | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBestsellingCreatorsResponse]
    """

    kwargs = _get_kwargs(
        date=date,
        time_slot=time_slot,
        author_type=author_type,
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
    time_slot: GetBestsellingCreatorsTimeSlot,
    author_type: GetBestsellingCreatorsAuthorType,
    currency: GetBestsellingCreatorsCurrency | Unset = UNSET,
) -> GetBestsellingCreatorsResponse | None:
    """Get Bestselling Creators

     Returns up to 100 creators, filtered by `author_type`, ranked by GMV in the selected `currency` for
    the reporting period ending on `date` and defined by `time_slot`.

    Args:
        date (datetime.date):
        time_slot (GetBestsellingCreatorsTimeSlot):
        author_type (GetBestsellingCreatorsAuthorType):
        currency (GetBestsellingCreatorsCurrency | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBestsellingCreatorsResponse
    """

    return sync_detailed(
        client=client,
        date=date,
        time_slot=time_slot,
        author_type=author_type,
        currency=currency,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    date: datetime.date,
    time_slot: GetBestsellingCreatorsTimeSlot,
    author_type: GetBestsellingCreatorsAuthorType,
    currency: GetBestsellingCreatorsCurrency | Unset = UNSET,
) -> Response[GetBestsellingCreatorsResponse]:
    """Get Bestselling Creators

     Returns up to 100 creators, filtered by `author_type`, ranked by GMV in the selected `currency` for
    the reporting period ending on `date` and defined by `time_slot`.

    Args:
        date (datetime.date):
        time_slot (GetBestsellingCreatorsTimeSlot):
        author_type (GetBestsellingCreatorsAuthorType):
        currency (GetBestsellingCreatorsCurrency | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBestsellingCreatorsResponse]
    """

    kwargs = _get_kwargs(
        date=date,
        time_slot=time_slot,
        author_type=author_type,
        currency=currency,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    date: datetime.date,
    time_slot: GetBestsellingCreatorsTimeSlot,
    author_type: GetBestsellingCreatorsAuthorType,
    currency: GetBestsellingCreatorsCurrency | Unset = UNSET,
) -> GetBestsellingCreatorsResponse | None:
    """Get Bestselling Creators

     Returns up to 100 creators, filtered by `author_type`, ranked by GMV in the selected `currency` for
    the reporting period ending on `date` and defined by `time_slot`.

    Args:
        date (datetime.date):
        time_slot (GetBestsellingCreatorsTimeSlot):
        author_type (GetBestsellingCreatorsAuthorType):
        currency (GetBestsellingCreatorsCurrency | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBestsellingCreatorsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            date=date,
            time_slot=time_slot,
            author_type=author_type,
            currency=currency,
        )
    ).parsed
