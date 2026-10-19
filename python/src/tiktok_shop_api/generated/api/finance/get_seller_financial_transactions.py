from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_seller_financial_transactions_response import GetSellerFinancialTransactionsResponse
from ...models.get_seller_financial_transactions_types_item import GetSellerFinancialTransactionsTypesItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    create_time_lt: int | Unset = UNSET,
    types: list[GetSellerFinancialTransactionsTypesItem],
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    create_time_ge: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["create_time_lt"] = create_time_lt

    json_types = []
    for types_item_data in types:
        types_item = types_item_data.value
        json_types.append(types_item)

    params["types"] = json_types

    params["page_size"] = page_size

    params["page_token"] = page_token

    params["create_time_ge"] = create_time_ge

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/finance/202309/withdrawals",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetSellerFinancialTransactionsResponse | None:
    if response.status_code == 200:
        response_200 = GetSellerFinancialTransactionsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetSellerFinancialTransactionsResponse]:
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
    types: list[GetSellerFinancialTransactionsTypesItem],
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    create_time_ge: int | Unset = UNSET,
) -> Response[GetSellerFinancialTransactionsResponse]:
    """Get Seller Financial Transactions

     Retrieves seller financial transaction records within an optional creation-time range, filtered by
    the required transaction types.

    Args:
        create_time_lt (int | Unset):
        types (list[GetSellerFinancialTransactionsTypesItem]):
        page_size (int | Unset):
        page_token (str | Unset):
        create_time_ge (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSellerFinancialTransactionsResponse]
    """

    kwargs = _get_kwargs(
        create_time_lt=create_time_lt,
        types=types,
        page_size=page_size,
        page_token=page_token,
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
    types: list[GetSellerFinancialTransactionsTypesItem],
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    create_time_ge: int | Unset = UNSET,
) -> GetSellerFinancialTransactionsResponse | None:
    """Get Seller Financial Transactions

     Retrieves seller financial transaction records within an optional creation-time range, filtered by
    the required transaction types.

    Args:
        create_time_lt (int | Unset):
        types (list[GetSellerFinancialTransactionsTypesItem]):
        page_size (int | Unset):
        page_token (str | Unset):
        create_time_ge (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSellerFinancialTransactionsResponse
    """

    return sync_detailed(
        client=client,
        create_time_lt=create_time_lt,
        types=types,
        page_size=page_size,
        page_token=page_token,
        create_time_ge=create_time_ge,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    create_time_lt: int | Unset = UNSET,
    types: list[GetSellerFinancialTransactionsTypesItem],
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    create_time_ge: int | Unset = UNSET,
) -> Response[GetSellerFinancialTransactionsResponse]:
    """Get Seller Financial Transactions

     Retrieves seller financial transaction records within an optional creation-time range, filtered by
    the required transaction types.

    Args:
        create_time_lt (int | Unset):
        types (list[GetSellerFinancialTransactionsTypesItem]):
        page_size (int | Unset):
        page_token (str | Unset):
        create_time_ge (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSellerFinancialTransactionsResponse]
    """

    kwargs = _get_kwargs(
        create_time_lt=create_time_lt,
        types=types,
        page_size=page_size,
        page_token=page_token,
        create_time_ge=create_time_ge,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    create_time_lt: int | Unset = UNSET,
    types: list[GetSellerFinancialTransactionsTypesItem],
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    create_time_ge: int | Unset = UNSET,
) -> GetSellerFinancialTransactionsResponse | None:
    """Get Seller Financial Transactions

     Retrieves seller financial transaction records within an optional creation-time range, filtered by
    the required transaction types.

    Args:
        create_time_lt (int | Unset):
        types (list[GetSellerFinancialTransactionsTypesItem]):
        page_size (int | Unset):
        page_token (str | Unset):
        create_time_ge (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSellerFinancialTransactionsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            create_time_lt=create_time_lt,
            types=types,
            page_size=page_size,
            page_token=page_token,
            create_time_ge=create_time_ge,
        )
    ).parsed
