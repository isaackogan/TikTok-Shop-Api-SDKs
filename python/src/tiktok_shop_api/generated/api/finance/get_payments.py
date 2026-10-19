from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_payments_response import GetPaymentsResponse
from ...models.get_payments_sort_order import GetPaymentsSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    create_time_lt: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    sort_field: str,
    sort_order: GetPaymentsSortOrder | Unset = UNSET,
    create_time_ge: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["create_time_lt"] = create_time_lt

    params["page_size"] = page_size

    params["page_token"] = page_token

    params["sort_field"] = sort_field

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sort_order"] = json_sort_order

    params["create_time_ge"] = create_time_ge

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/finance/202605/payments",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetPaymentsResponse | None:
    if response.status_code == 200:
        response_200 = GetPaymentsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetPaymentsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    create_time_lt: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    sort_field: str,
    sort_order: GetPaymentsSortOrder | Unset = UNSET,
    create_time_ge: int | Unset = UNSET,
) -> Response[GetPaymentsResponse]:
    """Get Payments

     **This API is currently unavailable to SEA markets.**
    Retrieves records of automated payments for a shop based on a specified date range.
    Use the returned list to verify and reconcile payments with the transactions in the seller's bank
    account.

    Args:
        create_time_lt (int | Unset):
        page_size (int | Unset):
        page_token (str | Unset):
        sort_field (str):
        sort_order (GetPaymentsSortOrder | Unset):
        create_time_ge (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPaymentsResponse]
    """

    kwargs = _get_kwargs(
        create_time_lt=create_time_lt,
        page_size=page_size,
        page_token=page_token,
        sort_field=sort_field,
        sort_order=sort_order,
        create_time_ge=create_time_ge,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    create_time_lt: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    sort_field: str,
    sort_order: GetPaymentsSortOrder | Unset = UNSET,
    create_time_ge: int | Unset = UNSET,
) -> GetPaymentsResponse | None:
    """Get Payments

     **This API is currently unavailable to SEA markets.**
    Retrieves records of automated payments for a shop based on a specified date range.
    Use the returned list to verify and reconcile payments with the transactions in the seller's bank
    account.

    Args:
        create_time_lt (int | Unset):
        page_size (int | Unset):
        page_token (str | Unset):
        sort_field (str):
        sort_order (GetPaymentsSortOrder | Unset):
        create_time_ge (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPaymentsResponse
    """

    return sync_detailed(
        client=client,
        create_time_lt=create_time_lt,
        page_size=page_size,
        page_token=page_token,
        sort_field=sort_field,
        sort_order=sort_order,
        create_time_ge=create_time_ge,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    create_time_lt: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    sort_field: str,
    sort_order: GetPaymentsSortOrder | Unset = UNSET,
    create_time_ge: int | Unset = UNSET,
) -> Response[GetPaymentsResponse]:
    """Get Payments

     **This API is currently unavailable to SEA markets.**
    Retrieves records of automated payments for a shop based on a specified date range.
    Use the returned list to verify and reconcile payments with the transactions in the seller's bank
    account.

    Args:
        create_time_lt (int | Unset):
        page_size (int | Unset):
        page_token (str | Unset):
        sort_field (str):
        sort_order (GetPaymentsSortOrder | Unset):
        create_time_ge (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPaymentsResponse]
    """

    kwargs = _get_kwargs(
        create_time_lt=create_time_lt,
        page_size=page_size,
        page_token=page_token,
        sort_field=sort_field,
        sort_order=sort_order,
        create_time_ge=create_time_ge,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    create_time_lt: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    sort_field: str,
    sort_order: GetPaymentsSortOrder | Unset = UNSET,
    create_time_ge: int | Unset = UNSET,
) -> GetPaymentsResponse | None:
    """Get Payments

     **This API is currently unavailable to SEA markets.**
    Retrieves records of automated payments for a shop based on a specified date range.
    Use the returned list to verify and reconcile payments with the transactions in the seller's bank
    account.

    Args:
        create_time_lt (int | Unset):
        page_size (int | Unset):
        page_token (str | Unset):
        sort_field (str):
        sort_order (GetPaymentsSortOrder | Unset):
        create_time_ge (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPaymentsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            create_time_lt=create_time_lt,
            page_size=page_size,
            page_token=page_token,
            sort_field=sort_field,
            sort_order=sort_order,
            create_time_ge=create_time_ge,
        )
    ).parsed
