from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ship_package_request import ShipPackageRequest
from ...models.ship_package_response import ShipPackageResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    package_id: str,
    *,
    body: ShipPackageRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fulfillment/202309/packages/{package_id}/ship".format(
            package_id=quote(str(package_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ShipPackageResponse | None:
    if response.status_code == 200:
        response_200 = ShipPackageResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ShipPackageResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ShipPackageRequest | Unset = UNSET,
) -> Response[ShipPackageResponse]:
    """Ship Package

     Use this API to ship a package. There are two kinds of shipping options available: `TikTok Shipping`
    or `Seller Shipping`.

    - `TikTok Shipping`: Schedule a package handover time for TikTok Shipping carriers to pickup a
    package from seller.
    - `Seller Shipping`: Seller arranges their own shipping, and uploads a tracking number and
    `shipping_provider_id`. Package ID can be obtained from [Get Order Detail](https://partner.tiktoksho
    p.com/docv2/page/650aa8ccc16ffe02b8f167a0?external_id=650aa8ccc16ffe02b8f167a0#Back%20To%20Top).
    - `In-store Pickup`: Confirms shipment and notifies the buyer that the order is ready for pickup.

    Args:
        package_id (str):
        body (ShipPackageRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ShipPackageResponse]
    """

    kwargs = _get_kwargs(
        package_id=package_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ShipPackageRequest | Unset = UNSET,
) -> ShipPackageResponse | None:
    """Ship Package

     Use this API to ship a package. There are two kinds of shipping options available: `TikTok Shipping`
    or `Seller Shipping`.

    - `TikTok Shipping`: Schedule a package handover time for TikTok Shipping carriers to pickup a
    package from seller.
    - `Seller Shipping`: Seller arranges their own shipping, and uploads a tracking number and
    `shipping_provider_id`. Package ID can be obtained from [Get Order Detail](https://partner.tiktoksho
    p.com/docv2/page/650aa8ccc16ffe02b8f167a0?external_id=650aa8ccc16ffe02b8f167a0#Back%20To%20Top).
    - `In-store Pickup`: Confirms shipment and notifies the buyer that the order is ready for pickup.

    Args:
        package_id (str):
        body (ShipPackageRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ShipPackageResponse
    """

    return sync_detailed(
        package_id=package_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ShipPackageRequest | Unset = UNSET,
) -> Response[ShipPackageResponse]:
    """Ship Package

     Use this API to ship a package. There are two kinds of shipping options available: `TikTok Shipping`
    or `Seller Shipping`.

    - `TikTok Shipping`: Schedule a package handover time for TikTok Shipping carriers to pickup a
    package from seller.
    - `Seller Shipping`: Seller arranges their own shipping, and uploads a tracking number and
    `shipping_provider_id`. Package ID can be obtained from [Get Order Detail](https://partner.tiktoksho
    p.com/docv2/page/650aa8ccc16ffe02b8f167a0?external_id=650aa8ccc16ffe02b8f167a0#Back%20To%20Top).
    - `In-store Pickup`: Confirms shipment and notifies the buyer that the order is ready for pickup.

    Args:
        package_id (str):
        body (ShipPackageRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ShipPackageResponse]
    """

    kwargs = _get_kwargs(
        package_id=package_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ShipPackageRequest | Unset = UNSET,
) -> ShipPackageResponse | None:
    """Ship Package

     Use this API to ship a package. There are two kinds of shipping options available: `TikTok Shipping`
    or `Seller Shipping`.

    - `TikTok Shipping`: Schedule a package handover time for TikTok Shipping carriers to pickup a
    package from seller.
    - `Seller Shipping`: Seller arranges their own shipping, and uploads a tracking number and
    `shipping_provider_id`. Package ID can be obtained from [Get Order Detail](https://partner.tiktoksho
    p.com/docv2/page/650aa8ccc16ffe02b8f167a0?external_id=650aa8ccc16ffe02b8f167a0#Back%20To%20Top).
    - `In-store Pickup`: Confirms shipment and notifies the buyer that the order is ready for pickup.

    Args:
        package_id (str):
        body (ShipPackageRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ShipPackageResponse
    """

    return (
        await asyncio_detailed(
            package_id=package_id,
            client=client,
            body=body,
        )
    ).parsed
