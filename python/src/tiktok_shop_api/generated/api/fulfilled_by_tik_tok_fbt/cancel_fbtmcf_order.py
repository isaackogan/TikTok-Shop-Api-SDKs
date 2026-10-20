from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cancel_fbtmcf_order_request import CancelFBTMCFOrderRequest
from ...models.cancel_fbtmcf_order_response import CancelFBTMCFOrderResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CancelFBTMCFOrderRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fbt/202601/mcf_outbound_orders/cancel",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CancelFBTMCFOrderResponse | None:
    if response.status_code == 200:
        response_200 = CancelFBTMCFOrderResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CancelFBTMCFOrderResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CancelFBTMCFOrderRequest,
) -> Response[CancelFBTMCFOrderResponse]:
    """Cancel FBT MCF Order

     An FBT multi-channel fulfillment (MCF) order may be split into one or more consign orders for
    fulfillment. Use this API to cancel the MCF order or selected consign orders by providing the
    `mcf_order_id`. To cancel selected consign orders, provide their consign order IDs. You can retrieve
    IDs that have already been assigned by calling the **Get FBT MCF Order Status** API; use IDs
    returned while the target consign orders are still in a cancellable pre-shipment state.

    Cancellation is rejected for target consign orders that have reached `SHIPPED`, `HANDOVER`,
    `COMPLETED`, or a shipping-exception state such as `LOST`, `DAMAGE`, `RETURNED`, or `SCRAP`.

    After the request, match the target consign order IDs against this API's response. A returned status
    of `CLOSED` means that the consign order has been canceled.

    Args:
        body (CancelFBTMCFOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelFBTMCFOrderResponse]
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
    body: CancelFBTMCFOrderRequest,
) -> CancelFBTMCFOrderResponse | None:
    """Cancel FBT MCF Order

     An FBT multi-channel fulfillment (MCF) order may be split into one or more consign orders for
    fulfillment. Use this API to cancel the MCF order or selected consign orders by providing the
    `mcf_order_id`. To cancel selected consign orders, provide their consign order IDs. You can retrieve
    IDs that have already been assigned by calling the **Get FBT MCF Order Status** API; use IDs
    returned while the target consign orders are still in a cancellable pre-shipment state.

    Cancellation is rejected for target consign orders that have reached `SHIPPED`, `HANDOVER`,
    `COMPLETED`, or a shipping-exception state such as `LOST`, `DAMAGE`, `RETURNED`, or `SCRAP`.

    After the request, match the target consign order IDs against this API's response. A returned status
    of `CLOSED` means that the consign order has been canceled.

    Args:
        body (CancelFBTMCFOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelFBTMCFOrderResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CancelFBTMCFOrderRequest,
) -> Response[CancelFBTMCFOrderResponse]:
    """Cancel FBT MCF Order

     An FBT multi-channel fulfillment (MCF) order may be split into one or more consign orders for
    fulfillment. Use this API to cancel the MCF order or selected consign orders by providing the
    `mcf_order_id`. To cancel selected consign orders, provide their consign order IDs. You can retrieve
    IDs that have already been assigned by calling the **Get FBT MCF Order Status** API; use IDs
    returned while the target consign orders are still in a cancellable pre-shipment state.

    Cancellation is rejected for target consign orders that have reached `SHIPPED`, `HANDOVER`,
    `COMPLETED`, or a shipping-exception state such as `LOST`, `DAMAGE`, `RETURNED`, or `SCRAP`.

    After the request, match the target consign order IDs against this API's response. A returned status
    of `CLOSED` means that the consign order has been canceled.

    Args:
        body (CancelFBTMCFOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelFBTMCFOrderResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CancelFBTMCFOrderRequest,
) -> CancelFBTMCFOrderResponse | None:
    """Cancel FBT MCF Order

     An FBT multi-channel fulfillment (MCF) order may be split into one or more consign orders for
    fulfillment. Use this API to cancel the MCF order or selected consign orders by providing the
    `mcf_order_id`. To cancel selected consign orders, provide their consign order IDs. You can retrieve
    IDs that have already been assigned by calling the **Get FBT MCF Order Status** API; use IDs
    returned while the target consign orders are still in a cancellable pre-shipment state.

    Cancellation is rejected for target consign orders that have reached `SHIPPED`, `HANDOVER`,
    `COMPLETED`, or a shipping-exception state such as `LOST`, `DAMAGE`, `RETURNED`, or `SCRAP`.

    After the request, match the target consign order IDs against this API's response. A returned status
    of `CLOSED` means that the consign order has been canceled.

    Args:
        body (CancelFBTMCFOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelFBTMCFOrderResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
