from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_package_shipping_info_request import UpdatePackageShippingInfoRequest
from ...models.update_package_shipping_info_response import UpdatePackageShippingInfoResponse
from ...types import Response


def _get_kwargs(
    package_id: str,
    *,
    body: UpdatePackageShippingInfoRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fulfillment/202610/packages/{package_id}/shipping_info/update".format(
            package_id=quote(str(package_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UpdatePackageShippingInfoResponse | None:
    if response.status_code == 200:
        response_200 = UpdatePackageShippingInfoResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdatePackageShippingInfoResponse]:
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
    body: UpdatePackageShippingInfoRequest,
) -> Response[UpdatePackageShippingInfoResponse]:
    """Update Package Shipping Info

     If the seller entered an incorrect tracking number, this API allows the seller to update the
    tracking number and shipping provider for a package that has already been shipped. Attention: This
    API is only applicable to orders (or packages) shipped by the seller.  It is only used to update the
    tracking number and shipping provider for packages that have already been shipped.

    Args:
        package_id (str):
        body (UpdatePackageShippingInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdatePackageShippingInfoResponse]
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
    body: UpdatePackageShippingInfoRequest,
) -> UpdatePackageShippingInfoResponse | None:
    """Update Package Shipping Info

     If the seller entered an incorrect tracking number, this API allows the seller to update the
    tracking number and shipping provider for a package that has already been shipped. Attention: This
    API is only applicable to orders (or packages) shipped by the seller.  It is only used to update the
    tracking number and shipping provider for packages that have already been shipped.

    Args:
        package_id (str):
        body (UpdatePackageShippingInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdatePackageShippingInfoResponse
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
    body: UpdatePackageShippingInfoRequest,
) -> Response[UpdatePackageShippingInfoResponse]:
    """Update Package Shipping Info

     If the seller entered an incorrect tracking number, this API allows the seller to update the
    tracking number and shipping provider for a package that has already been shipped. Attention: This
    API is only applicable to orders (or packages) shipped by the seller.  It is only used to update the
    tracking number and shipping provider for packages that have already been shipped.

    Args:
        package_id (str):
        body (UpdatePackageShippingInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdatePackageShippingInfoResponse]
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
    body: UpdatePackageShippingInfoRequest,
) -> UpdatePackageShippingInfoResponse | None:
    """Update Package Shipping Info

     If the seller entered an incorrect tracking number, this API allows the seller to update the
    tracking number and shipping provider for a package that has already been shipped. Attention: This
    API is only applicable to orders (or packages) shipped by the seller.  It is only used to update the
    tracking number and shipping provider for packages that have already been shipped.

    Args:
        package_id (str):
        body (UpdatePackageShippingInfoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdatePackageShippingInfoResponse
    """

    return (
        await asyncio_detailed(
            package_id=package_id,
            client=client,
            body=body,
        )
    ).parsed
