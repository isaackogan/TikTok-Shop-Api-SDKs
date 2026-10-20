from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_inbound_order_tracking_request import UpdateInboundOrderTrackingRequest
from ...models.update_inbound_order_tracking_response import UpdateInboundOrderTrackingResponse
from ...types import Response


def _get_kwargs(
    *,
    body: UpdateInboundOrderTrackingRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fbt/202602/inbound_orders/tracking_update",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UpdateInboundOrderTrackingResponse | None:
    if response.status_code == 200:
        response_200 = UpdateInboundOrderTrackingResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdateInboundOrderTrackingResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateInboundOrderTrackingRequest,
) -> Response[UpdateInboundOrderTrackingResponse]:
    """Update Inbound Order Tracking

     Updates carton-level tracking information for an inbound order after shipment and before the order
    is marked as `Delivered` or `Received`. When updating tracking, send the complete desired
    `parcel_tracking_info` list; entries omitted from a non-empty submission are not retained, so this
    is not a partial patch. The first tracking value for a carton does not count as an edit, and
    resubmitting the same normalized value does not consume another edit. Changing an existing carton's
    tracking number consumes one of the five allowed edits for that carton; a sixth change is rejected
    before the local update. The submitted carton updates are applied atomically to the stored tracking
    list: either the complete local replacement is saved or none of it is. Warehouse synchronization and
    logistics tracking registration occur outside this atomic update; warehouse synchronization failures
    are not returned, and tracking registration runs asynchronously.

    Args:
        body (UpdateInboundOrderTrackingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateInboundOrderTrackingResponse]
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
    body: UpdateInboundOrderTrackingRequest,
) -> UpdateInboundOrderTrackingResponse | None:
    """Update Inbound Order Tracking

     Updates carton-level tracking information for an inbound order after shipment and before the order
    is marked as `Delivered` or `Received`. When updating tracking, send the complete desired
    `parcel_tracking_info` list; entries omitted from a non-empty submission are not retained, so this
    is not a partial patch. The first tracking value for a carton does not count as an edit, and
    resubmitting the same normalized value does not consume another edit. Changing an existing carton's
    tracking number consumes one of the five allowed edits for that carton; a sixth change is rejected
    before the local update. The submitted carton updates are applied atomically to the stored tracking
    list: either the complete local replacement is saved or none of it is. Warehouse synchronization and
    logistics tracking registration occur outside this atomic update; warehouse synchronization failures
    are not returned, and tracking registration runs asynchronously.

    Args:
        body (UpdateInboundOrderTrackingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateInboundOrderTrackingResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateInboundOrderTrackingRequest,
) -> Response[UpdateInboundOrderTrackingResponse]:
    """Update Inbound Order Tracking

     Updates carton-level tracking information for an inbound order after shipment and before the order
    is marked as `Delivered` or `Received`. When updating tracking, send the complete desired
    `parcel_tracking_info` list; entries omitted from a non-empty submission are not retained, so this
    is not a partial patch. The first tracking value for a carton does not count as an edit, and
    resubmitting the same normalized value does not consume another edit. Changing an existing carton's
    tracking number consumes one of the five allowed edits for that carton; a sixth change is rejected
    before the local update. The submitted carton updates are applied atomically to the stored tracking
    list: either the complete local replacement is saved or none of it is. Warehouse synchronization and
    logistics tracking registration occur outside this atomic update; warehouse synchronization failures
    are not returned, and tracking registration runs asynchronously.

    Args:
        body (UpdateInboundOrderTrackingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateInboundOrderTrackingResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateInboundOrderTrackingRequest,
) -> UpdateInboundOrderTrackingResponse | None:
    """Update Inbound Order Tracking

     Updates carton-level tracking information for an inbound order after shipment and before the order
    is marked as `Delivered` or `Received`. When updating tracking, send the complete desired
    `parcel_tracking_info` list; entries omitted from a non-empty submission are not retained, so this
    is not a partial patch. The first tracking value for a carton does not count as an edit, and
    resubmitting the same normalized value does not consume another edit. Changing an existing carton's
    tracking number consumes one of the five allowed edits for that carton; a sixth change is rejected
    before the local update. The submitted carton updates are applied atomically to the stored tracking
    list: either the complete local replacement is saved or none of it is. Warehouse synchronization and
    logistics tracking registration occur outside this atomic update; warehouse synchronization failures
    are not returned, and tracking registration runs asynchronously.

    Args:
        body (UpdateInboundOrderTrackingRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateInboundOrderTrackingResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
