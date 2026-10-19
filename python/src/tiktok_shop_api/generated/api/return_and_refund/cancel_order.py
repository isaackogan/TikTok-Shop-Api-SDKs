from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cancel_order_request import CancelOrderRequest
from ...models.cancel_order_response import CancelOrderResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CancelOrderRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/return_refund/202602/cancellations",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CancelOrderResponse | None:
    if response.status_code == 200:
        response_200 = CancelOrderResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CancelOrderResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CancelOrderRequest,
) -> Response[CancelOrderResponse]:
    """Cancel Order

     Use this API to cancel an order on behalf of a seller. In the US and UK markets, when an item is out
    of stock, partial cancellation on the single item level is supported by this API.

    Args:
        body (CancelOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelOrderResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CancelOrderRequest,
) -> CancelOrderResponse | None:
    """Cancel Order

     Use this API to cancel an order on behalf of a seller. In the US and UK markets, when an item is out
    of stock, partial cancellation on the single item level is supported by this API.

    Args:
        body (CancelOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelOrderResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CancelOrderRequest,
) -> Response[CancelOrderResponse]:
    """Cancel Order

     Use this API to cancel an order on behalf of a seller. In the US and UK markets, when an item is out
    of stock, partial cancellation on the single item level is supported by this API.

    Args:
        body (CancelOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelOrderResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CancelOrderRequest,
) -> CancelOrderResponse | None:
    """Cancel Order

     Use this API to cancel an order on behalf of a seller. In the US and UK markets, when an item is out
    of stock, partial cancellation on the single item level is supported by this API.

    Args:
        body (CancelOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelOrderResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
