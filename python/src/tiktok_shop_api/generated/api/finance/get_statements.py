from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_statements_payment_status import GetStatementsPaymentStatus
from ...models.get_statements_response import GetStatementsResponse
from ...models.get_statements_sort_order import GetStatementsSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    statement_time_lt: int | Unset = UNSET,
    payment_status: GetStatementsPaymentStatus | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    sort_field: str,
    sort_order: GetStatementsSortOrder | Unset = UNSET,
    statement_time_ge: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["statement_time_lt"] = statement_time_lt

    json_payment_status: str | Unset = UNSET
    if not isinstance(payment_status, Unset):
        json_payment_status = payment_status.value

    params["payment_status"] = json_payment_status

    params["page_size"] = page_size

    params["page_token"] = page_token

    params["sort_field"] = sort_field

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sort_order"] = json_sort_order

    params["statement_time_ge"] = statement_time_ge

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/finance/202309/statements",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetStatementsResponse | None:
    if response.status_code == 200:
        response_200 = GetStatementsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetStatementsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    statement_time_lt: int | Unset = UNSET,
    payment_status: GetStatementsPaymentStatus | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    sort_field: str,
    sort_order: GetStatementsSortOrder | Unset = UNSET,
    statement_time_ge: int | Unset = UNSET,
) -> Response[GetStatementsResponse]:
    """Get Statements

     Retrieves the statements generated for a shop and the key statement information based on a specified
    date range or their payment status. Use this API to get an overview of your daily statements over a
    range of time, or to find out which statements have been paid or not. For the detailed transactions,
    refer to [Get Statement Transactions](650a6749defece02be67da87) or [Get Order Statement
    Transactions](650a6734defece02be67d724).
    Applicable for all regions' sellers. Only data after 2023-07-01 is available.

    Args:
        statement_time_lt (int | Unset):
        payment_status (GetStatementsPaymentStatus | Unset):
        page_size (int | Unset):
        page_token (str | Unset):
        sort_field (str):
        sort_order (GetStatementsSortOrder | Unset):
        statement_time_ge (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetStatementsResponse]
    """

    kwargs = _get_kwargs(
        statement_time_lt=statement_time_lt,
        payment_status=payment_status,
        page_size=page_size,
        page_token=page_token,
        sort_field=sort_field,
        sort_order=sort_order,
        statement_time_ge=statement_time_ge,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    statement_time_lt: int | Unset = UNSET,
    payment_status: GetStatementsPaymentStatus | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    sort_field: str,
    sort_order: GetStatementsSortOrder | Unset = UNSET,
    statement_time_ge: int | Unset = UNSET,
) -> GetStatementsResponse | None:
    """Get Statements

     Retrieves the statements generated for a shop and the key statement information based on a specified
    date range or their payment status. Use this API to get an overview of your daily statements over a
    range of time, or to find out which statements have been paid or not. For the detailed transactions,
    refer to [Get Statement Transactions](650a6749defece02be67da87) or [Get Order Statement
    Transactions](650a6734defece02be67d724).
    Applicable for all regions' sellers. Only data after 2023-07-01 is available.

    Args:
        statement_time_lt (int | Unset):
        payment_status (GetStatementsPaymentStatus | Unset):
        page_size (int | Unset):
        page_token (str | Unset):
        sort_field (str):
        sort_order (GetStatementsSortOrder | Unset):
        statement_time_ge (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetStatementsResponse
    """

    return sync_detailed(
        client=client,
        statement_time_lt=statement_time_lt,
        payment_status=payment_status,
        page_size=page_size,
        page_token=page_token,
        sort_field=sort_field,
        sort_order=sort_order,
        statement_time_ge=statement_time_ge,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    statement_time_lt: int | Unset = UNSET,
    payment_status: GetStatementsPaymentStatus | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    sort_field: str,
    sort_order: GetStatementsSortOrder | Unset = UNSET,
    statement_time_ge: int | Unset = UNSET,
) -> Response[GetStatementsResponse]:
    """Get Statements

     Retrieves the statements generated for a shop and the key statement information based on a specified
    date range or their payment status. Use this API to get an overview of your daily statements over a
    range of time, or to find out which statements have been paid or not. For the detailed transactions,
    refer to [Get Statement Transactions](650a6749defece02be67da87) or [Get Order Statement
    Transactions](650a6734defece02be67d724).
    Applicable for all regions' sellers. Only data after 2023-07-01 is available.

    Args:
        statement_time_lt (int | Unset):
        payment_status (GetStatementsPaymentStatus | Unset):
        page_size (int | Unset):
        page_token (str | Unset):
        sort_field (str):
        sort_order (GetStatementsSortOrder | Unset):
        statement_time_ge (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetStatementsResponse]
    """

    kwargs = _get_kwargs(
        statement_time_lt=statement_time_lt,
        payment_status=payment_status,
        page_size=page_size,
        page_token=page_token,
        sort_field=sort_field,
        sort_order=sort_order,
        statement_time_ge=statement_time_ge,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    statement_time_lt: int | Unset = UNSET,
    payment_status: GetStatementsPaymentStatus | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    sort_field: str,
    sort_order: GetStatementsSortOrder | Unset = UNSET,
    statement_time_ge: int | Unset = UNSET,
) -> GetStatementsResponse | None:
    """Get Statements

     Retrieves the statements generated for a shop and the key statement information based on a specified
    date range or their payment status. Use this API to get an overview of your daily statements over a
    range of time, or to find out which statements have been paid or not. For the detailed transactions,
    refer to [Get Statement Transactions](650a6749defece02be67da87) or [Get Order Statement
    Transactions](650a6734defece02be67d724).
    Applicable for all regions' sellers. Only data after 2023-07-01 is available.

    Args:
        statement_time_lt (int | Unset):
        payment_status (GetStatementsPaymentStatus | Unset):
        page_size (int | Unset):
        page_token (str | Unset):
        sort_field (str):
        sort_order (GetStatementsSortOrder | Unset):
        statement_time_ge (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetStatementsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            statement_time_lt=statement_time_lt,
            payment_status=payment_status,
            page_size=page_size,
            page_token=page_token,
            sort_field=sort_field,
            sort_order=sort_order,
            statement_time_ge=statement_time_ge,
        )
    ).parsed
