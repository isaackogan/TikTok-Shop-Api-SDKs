import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_bestselling_products_response import GetBestsellingProductsResponse
from ...models.get_bestselling_products_time_slot import GetBestsellingProductsTimeSlot
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    category_id: str | Unset = UNSET,
    date: datetime.date,
    time_slot: GetBestsellingProductsTimeSlot,
    currency: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["category_id"] = category_id

    json_date = date.isoformat()
    params["date"] = json_date

    json_time_slot = time_slot.value
    params["time_slot"] = json_time_slot

    params["currency"] = currency

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202511/products/bestselling",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetBestsellingProductsResponse | None:
    if response.status_code == 200:
        response_200 = GetBestsellingProductsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetBestsellingProductsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    category_id: str | Unset = UNSET,
    date: datetime.date,
    time_slot: GetBestsellingProductsTimeSlot,
    currency: str | Unset = UNSET,
) -> Response[GetBestsellingProductsResponse]:
    """Get Bestselling Products

     Returns up to 100 products ranked by GMV for the target date range.

    Args:
        category_id (str | Unset):
        date (datetime.date):
        time_slot (GetBestsellingProductsTimeSlot):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBestsellingProductsResponse]
    """

    kwargs = _get_kwargs(
        category_id=category_id,
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
    category_id: str | Unset = UNSET,
    date: datetime.date,
    time_slot: GetBestsellingProductsTimeSlot,
    currency: str | Unset = UNSET,
) -> GetBestsellingProductsResponse | None:
    """Get Bestselling Products

     Returns up to 100 products ranked by GMV for the target date range.

    Args:
        category_id (str | Unset):
        date (datetime.date):
        time_slot (GetBestsellingProductsTimeSlot):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBestsellingProductsResponse
    """

    return sync_detailed(
        client=client,
        category_id=category_id,
        date=date,
        time_slot=time_slot,
        currency=currency,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    category_id: str | Unset = UNSET,
    date: datetime.date,
    time_slot: GetBestsellingProductsTimeSlot,
    currency: str | Unset = UNSET,
) -> Response[GetBestsellingProductsResponse]:
    """Get Bestselling Products

     Returns up to 100 products ranked by GMV for the target date range.

    Args:
        category_id (str | Unset):
        date (datetime.date):
        time_slot (GetBestsellingProductsTimeSlot):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBestsellingProductsResponse]
    """

    kwargs = _get_kwargs(
        category_id=category_id,
        date=date,
        time_slot=time_slot,
        currency=currency,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    category_id: str | Unset = UNSET,
    date: datetime.date,
    time_slot: GetBestsellingProductsTimeSlot,
    currency: str | Unset = UNSET,
) -> GetBestsellingProductsResponse | None:
    """Get Bestselling Products

     Returns up to 100 products ranked by GMV for the target date range.

    Args:
        category_id (str | Unset):
        date (datetime.date):
        time_slot (GetBestsellingProductsTimeSlot):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBestsellingProductsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            category_id=category_id,
            date=date,
            time_slot=time_slot,
            currency=currency,
        )
    ).parsed
