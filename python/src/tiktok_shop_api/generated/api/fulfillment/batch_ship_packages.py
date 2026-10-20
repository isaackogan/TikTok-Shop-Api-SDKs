from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.batch_ship_packages_request import BatchShipPackagesRequest
from ...models.batch_ship_packages_response import BatchShipPackagesResponse
from typing import cast



def _get_kwargs(
    *,
    body: BatchShipPackagesRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fulfillment/202309/packages/ship",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BatchShipPackagesResponse | None:
    if response.status_code == 200:
        response_200 = BatchShipPackagesResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BatchShipPackagesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BatchShipPackagesRequest,

) -> Response[BatchShipPackagesResponse]:
    """ Batch Ship Packages

     Use this API to ship one or more packages in a single request. The API supports TikTok Shipping,
    Seller Shipping, and In-store Pickup.

    - `TikTok Shipping`: Set each package's `handover_method` to `PICKUP` for carrier pickup from the
    seller's pickup address, or to `DROP_OFF` when the seller will drop it off at a designated location.
    - `Seller Shipping`: Provide `self_shipment.shipping_provider_id` and
    `self_shipment.tracking_number` for each package. Obtain package IDs from [Get Order Detail](https:/
    /partner.tiktokshop.com/docv2/page/650aa8ccc16ffe02b8f167a0?external_id=650aa8ccc16ffe02b8f167a0).
    - `In-store Pickup`: Confirm shipment and notify the buyer that the order is ready for pickup.

    A response with a top-level `code` of `0` can still contain package-specific failures. Check
    `data.errors` before treating every package as shipped.

    Args:
        body (BatchShipPackagesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchShipPackagesResponse]
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
    body: BatchShipPackagesRequest,

) -> BatchShipPackagesResponse | None:
    """ Batch Ship Packages

     Use this API to ship one or more packages in a single request. The API supports TikTok Shipping,
    Seller Shipping, and In-store Pickup.

    - `TikTok Shipping`: Set each package's `handover_method` to `PICKUP` for carrier pickup from the
    seller's pickup address, or to `DROP_OFF` when the seller will drop it off at a designated location.
    - `Seller Shipping`: Provide `self_shipment.shipping_provider_id` and
    `self_shipment.tracking_number` for each package. Obtain package IDs from [Get Order Detail](https:/
    /partner.tiktokshop.com/docv2/page/650aa8ccc16ffe02b8f167a0?external_id=650aa8ccc16ffe02b8f167a0).
    - `In-store Pickup`: Confirm shipment and notify the buyer that the order is ready for pickup.

    A response with a top-level `code` of `0` can still contain package-specific failures. Check
    `data.errors` before treating every package as shipped.

    Args:
        body (BatchShipPackagesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchShipPackagesResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BatchShipPackagesRequest,

) -> Response[BatchShipPackagesResponse]:
    """ Batch Ship Packages

     Use this API to ship one or more packages in a single request. The API supports TikTok Shipping,
    Seller Shipping, and In-store Pickup.

    - `TikTok Shipping`: Set each package's `handover_method` to `PICKUP` for carrier pickup from the
    seller's pickup address, or to `DROP_OFF` when the seller will drop it off at a designated location.
    - `Seller Shipping`: Provide `self_shipment.shipping_provider_id` and
    `self_shipment.tracking_number` for each package. Obtain package IDs from [Get Order Detail](https:/
    /partner.tiktokshop.com/docv2/page/650aa8ccc16ffe02b8f167a0?external_id=650aa8ccc16ffe02b8f167a0).
    - `In-store Pickup`: Confirm shipment and notify the buyer that the order is ready for pickup.

    A response with a top-level `code` of `0` can still contain package-specific failures. Check
    `data.errors` before treating every package as shipped.

    Args:
        body (BatchShipPackagesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchShipPackagesResponse]
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
    body: BatchShipPackagesRequest,

) -> BatchShipPackagesResponse | None:
    """ Batch Ship Packages

     Use this API to ship one or more packages in a single request. The API supports TikTok Shipping,
    Seller Shipping, and In-store Pickup.

    - `TikTok Shipping`: Set each package's `handover_method` to `PICKUP` for carrier pickup from the
    seller's pickup address, or to `DROP_OFF` when the seller will drop it off at a designated location.
    - `Seller Shipping`: Provide `self_shipment.shipping_provider_id` and
    `self_shipment.tracking_number` for each package. Obtain package IDs from [Get Order Detail](https:/
    /partner.tiktokshop.com/docv2/page/650aa8ccc16ffe02b8f167a0?external_id=650aa8ccc16ffe02b8f167a0).
    - `In-store Pickup`: Confirm shipment and notify the buyer that the order is ready for pickup.

    A response with a top-level `code` of `0` can still contain package-specific failures. Check
    `data.errors` before treating every package as shipped.

    Args:
        body (BatchShipPackagesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchShipPackagesResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
