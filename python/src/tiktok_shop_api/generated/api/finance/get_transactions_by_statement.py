from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_transactions_by_statement_response import GetTransactionsByStatementResponse
from ...models.get_transactions_by_statement_sort_order import GetTransactionsByStatementSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    statement_id: str,
    *,
    page_token: str | Unset = UNSET,
    sort_field: str,
    sort_order: GetTransactionsByStatementSortOrder | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page_token"] = page_token

    params["sort_field"] = sort_field

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sort_order"] = json_sort_order

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/finance/202501/statements/{statement_id}/statement_transactions".format(
            statement_id=quote(str(statement_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetTransactionsByStatementResponse | None:
    if response.status_code == 200:
        response_200 = GetTransactionsByStatementResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetTransactionsByStatementResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    statement_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    sort_field: str,
    sort_order: GetTransactionsByStatementSortOrder | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> Response[GetTransactionsByStatementResponse]:
    """Get Transactions by Statement

     Retrieves the details of a statement, including the transactions, which can be a standard order
    transaction, an adjustment transaction, or a reserve-related transaction. For the SKU-level details
    of an order transaction, refer to [Get Transactions by Order](650a6734defece02be67d724).
    Applicable for all regions' sellers. Only data after 2023-07-01 is available (Please note that for
    US cross-border sellers, data before 2025-04-30 is unavailable).

    Args:
        statement_id (str):
        page_token (str | Unset):
        sort_field (str):
        sort_order (GetTransactionsByStatementSortOrder | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTransactionsByStatementResponse]
    """

    kwargs = _get_kwargs(
        statement_id=statement_id,
        page_token=page_token,
        sort_field=sort_field,
        sort_order=sort_order,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    statement_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    sort_field: str,
    sort_order: GetTransactionsByStatementSortOrder | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> GetTransactionsByStatementResponse | None:
    """Get Transactions by Statement

     Retrieves the details of a statement, including the transactions, which can be a standard order
    transaction, an adjustment transaction, or a reserve-related transaction. For the SKU-level details
    of an order transaction, refer to [Get Transactions by Order](650a6734defece02be67d724).
    Applicable for all regions' sellers. Only data after 2023-07-01 is available (Please note that for
    US cross-border sellers, data before 2025-04-30 is unavailable).

    Args:
        statement_id (str):
        page_token (str | Unset):
        sort_field (str):
        sort_order (GetTransactionsByStatementSortOrder | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTransactionsByStatementResponse
    """

    return sync_detailed(
        statement_id=statement_id,
        client=client,
        page_token=page_token,
        sort_field=sort_field,
        sort_order=sort_order,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    statement_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    sort_field: str,
    sort_order: GetTransactionsByStatementSortOrder | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> Response[GetTransactionsByStatementResponse]:
    """Get Transactions by Statement

     Retrieves the details of a statement, including the transactions, which can be a standard order
    transaction, an adjustment transaction, or a reserve-related transaction. For the SKU-level details
    of an order transaction, refer to [Get Transactions by Order](650a6734defece02be67d724).
    Applicable for all regions' sellers. Only data after 2023-07-01 is available (Please note that for
    US cross-border sellers, data before 2025-04-30 is unavailable).

    Args:
        statement_id (str):
        page_token (str | Unset):
        sort_field (str):
        sort_order (GetTransactionsByStatementSortOrder | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTransactionsByStatementResponse]
    """

    kwargs = _get_kwargs(
        statement_id=statement_id,
        page_token=page_token,
        sort_field=sort_field,
        sort_order=sort_order,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    statement_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    sort_field: str,
    sort_order: GetTransactionsByStatementSortOrder | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> GetTransactionsByStatementResponse | None:
    """Get Transactions by Statement

     Retrieves the details of a statement, including the transactions, which can be a standard order
    transaction, an adjustment transaction, or a reserve-related transaction. For the SKU-level details
    of an order transaction, refer to [Get Transactions by Order](650a6734defece02be67d724).
    Applicable for all regions' sellers. Only data after 2023-07-01 is available (Please note that for
    US cross-border sellers, data before 2025-04-30 is unavailable).

    Args:
        statement_id (str):
        page_token (str | Unset):
        sort_field (str):
        sort_order (GetTransactionsByStatementSortOrder | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTransactionsByStatementResponse
    """

    return (
        await asyncio_detailed(
            statement_id=statement_id,
            client=client,
            page_token=page_token,
            sort_field=sort_field,
            sort_order=sort_order,
            page_size=page_size,
        )
    ).parsed
