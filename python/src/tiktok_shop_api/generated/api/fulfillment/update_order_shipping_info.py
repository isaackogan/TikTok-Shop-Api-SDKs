from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_order_shipping_info_request import UpdateOrderShippingInfoRequest
from ...models.update_order_shipping_info_response import UpdateOrderShippingInfoResponse
from ...types import Response


def _get_kwargs(
    order_id: str,
    *,
    body: UpdateOrderShippingInfoRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fulfillment/202309/orders/{order_id}/shipping_info/update".format(
            order_id=quote(str(order_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UpdateOrderShippingInfoResponse | None:
    if response.status_code == 200:
        response_200 = UpdateOrderShippingInfoResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdateOrderShippingInfoResponse]:
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
    body: UpdateOrderShippingInfoRequest,
) -> Response[UpdateOrderShippingInfoResponse]:
    """Update Order Shipping Info

     If the seller entered an incorrect tracking number, this API allows the seller to update the
    tracking number and shipping provider for an order that has already been shipped.

    - This API is only applicable to orders (or packages) shipped by the seller.
    - It is only used to update the tracking number and shipping provider for packages that have already
    been shipped.
    - For orders that have been split for shipping, please use the [Update Package Shipping Info API](ht
    tps://partner.tiktokshop.com/docv2/page/650aa666c16ffe02b8f1203c?external_id=650aa666c16ffe02b8f1203
    c).

    Please note that TikTok Shop only allows merchants to update shipping information within 72 hours
    after shipping.

    Args:
        order_id (str):
        body (UpdateOrderShippingInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateOrderShippingInfoResponse]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateOrderShippingInfoRequest,
) -> UpdateOrderShippingInfoResponse | None:
    """Update Order Shipping Info

     If the seller entered an incorrect tracking number, this API allows the seller to update the
    tracking number and shipping provider for an order that has already been shipped.

    - This API is only applicable to orders (or packages) shipped by the seller.
    - It is only used to update the tracking number and shipping provider for packages that have already
    been shipped.
    - For orders that have been split for shipping, please use the [Update Package Shipping Info API](ht
    tps://partner.tiktokshop.com/docv2/page/650aa666c16ffe02b8f1203c?external_id=650aa666c16ffe02b8f1203
    c).

    Please note that TikTok Shop only allows merchants to update shipping information within 72 hours
    after shipping.

    Args:
        order_id (str):
        body (UpdateOrderShippingInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateOrderShippingInfoResponse
    """

    return sync_detailed(
        order_id=order_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateOrderShippingInfoRequest,
) -> Response[UpdateOrderShippingInfoResponse]:
    """Update Order Shipping Info

     If the seller entered an incorrect tracking number, this API allows the seller to update the
    tracking number and shipping provider for an order that has already been shipped.

    - This API is only applicable to orders (or packages) shipped by the seller.
    - It is only used to update the tracking number and shipping provider for packages that have already
    been shipped.
    - For orders that have been split for shipping, please use the [Update Package Shipping Info API](ht
    tps://partner.tiktokshop.com/docv2/page/650aa666c16ffe02b8f1203c?external_id=650aa666c16ffe02b8f1203
    c).

    Please note that TikTok Shop only allows merchants to update shipping information within 72 hours
    after shipping.

    Args:
        order_id (str):
        body (UpdateOrderShippingInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateOrderShippingInfoResponse]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateOrderShippingInfoRequest,
) -> UpdateOrderShippingInfoResponse | None:
    """Update Order Shipping Info

     If the seller entered an incorrect tracking number, this API allows the seller to update the
    tracking number and shipping provider for an order that has already been shipped.

    - This API is only applicable to orders (or packages) shipped by the seller.
    - It is only used to update the tracking number and shipping provider for packages that have already
    been shipped.
    - For orders that have been split for shipping, please use the [Update Package Shipping Info API](ht
    tps://partner.tiktokshop.com/docv2/page/650aa666c16ffe02b8f1203c?external_id=650aa666c16ffe02b8f1203
    c).

    Please note that TikTok Shop only allows merchants to update shipping information within 72 hours
    after shipping.

    Args:
        order_id (str):
        body (UpdateOrderShippingInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateOrderShippingInfoResponse
    """

    return (
        await asyncio_detailed(
            order_id=order_id,
            client=client,
            body=body,
        )
    ).parsed
