from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.ship_inbound_order_request import ShipInboundOrderRequest
from ...models.ship_inbound_order_response import ShipInboundOrderResponse
from typing import cast



def _get_kwargs(
    *,
    body: ShipInboundOrderRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fbt/202603/ship_inbound_order",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ShipInboundOrderResponse | None:
    if response.status_code == 200:
        response_200 = ShipInboundOrderResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ShipInboundOrderResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ShipInboundOrderRequest,

) -> Response[ShipInboundOrderResponse]:
    """ Ship Inbound Order

     Finalizes carton and shipping details for an inbound order that is ready to ship. For an order that
    has not already been shipped, a successful response means the details were saved and the order moved
    to the receiving stage. Repeating the request after the order has already been shipped returns
    success without applying the supplied details again.

    Args:
        body (ShipInboundOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ShipInboundOrderResponse]
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
    body: ShipInboundOrderRequest,

) -> ShipInboundOrderResponse | None:
    """ Ship Inbound Order

     Finalizes carton and shipping details for an inbound order that is ready to ship. For an order that
    has not already been shipped, a successful response means the details were saved and the order moved
    to the receiving stage. Repeating the request after the order has already been shipped returns
    success without applying the supplied details again.

    Args:
        body (ShipInboundOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ShipInboundOrderResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ShipInboundOrderRequest,

) -> Response[ShipInboundOrderResponse]:
    """ Ship Inbound Order

     Finalizes carton and shipping details for an inbound order that is ready to ship. For an order that
    has not already been shipped, a successful response means the details were saved and the order moved
    to the receiving stage. Repeating the request after the order has already been shipped returns
    success without applying the supplied details again.

    Args:
        body (ShipInboundOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ShipInboundOrderResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ShipInboundOrderRequest,

) -> ShipInboundOrderResponse | None:
    """ Ship Inbound Order

     Finalizes carton and shipping details for an inbound order that is ready to ship. For an order that
    has not already been shipped, a successful response means the details were saved and the order moved
    to the receiving stage. Repeating the request after the order has already been shipped returns
    success without applying the supplied details again.

    Args:
        body (ShipInboundOrderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ShipInboundOrderResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
