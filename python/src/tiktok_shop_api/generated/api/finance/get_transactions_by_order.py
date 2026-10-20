from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_transactions_by_order_response import GetTransactionsByOrderResponse
from ...types import Response


def _get_kwargs(
    order_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/finance/202501/orders/{order_id}/statement_transactions".format(
            order_id=quote(str(order_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetTransactionsByOrderResponse | None:
    if response.status_code == 200:
        response_200 = GetTransactionsByOrderResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetTransactionsByOrderResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetTransactionsByOrderResponse]:
    """Get Transactions by Order

     Retrieves the SKU-level details of an order transaction. This covers transactions related to sales,
    fees, commissions, shipping, taxes, and refunds.
    Applicable for all regions' sellers. Only data after 2023-07-01 is available (Please note that for
    US cross-border sellers, data before 2025-04-30 is unavailable).

    Args:
        order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTransactionsByOrderResponse]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetTransactionsByOrderResponse | None:
    """Get Transactions by Order

     Retrieves the SKU-level details of an order transaction. This covers transactions related to sales,
    fees, commissions, shipping, taxes, and refunds.
    Applicable for all regions' sellers. Only data after 2023-07-01 is available (Please note that for
    US cross-border sellers, data before 2025-04-30 is unavailable).

    Args:
        order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTransactionsByOrderResponse
    """

    return sync_detailed(
        order_id=order_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetTransactionsByOrderResponse]:
    """Get Transactions by Order

     Retrieves the SKU-level details of an order transaction. This covers transactions related to sales,
    fees, commissions, shipping, taxes, and refunds.
    Applicable for all regions' sellers. Only data after 2023-07-01 is available (Please note that for
    US cross-border sellers, data before 2025-04-30 is unavailable).

    Args:
        order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTransactionsByOrderResponse]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetTransactionsByOrderResponse | None:
    """Get Transactions by Order

     Retrieves the SKU-level details of an order transaction. This covers transactions related to sales,
    fees, commissions, shipping, taxes, and refunds.
    Applicable for all regions' sellers. Only data after 2023-07-01 is available (Please note that for
    US cross-border sellers, data before 2025-04-30 is unavailable).

    Args:
        order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTransactionsByOrderResponse
    """

    return (
        await asyncio_detailed(
            order_id=order_id,
            client=client,
        )
    ).parsed
