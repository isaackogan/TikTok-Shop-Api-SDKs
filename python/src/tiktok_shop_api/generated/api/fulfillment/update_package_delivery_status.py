from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_package_delivery_status_request import UpdatePackageDeliveryStatusRequest
from ...models.update_package_delivery_status_response import UpdatePackageDeliveryStatusResponse
from ...types import Response


def _get_kwargs(
    *,
    body: UpdatePackageDeliveryStatusRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fulfillment/202309/packages/deliver",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UpdatePackageDeliveryStatusResponse | None:
    if response.status_code == 200:
        response_200 = UpdatePackageDeliveryStatusResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdatePackageDeliveryStatusResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePackageDeliveryStatusRequest,
) -> Response[UpdatePackageDeliveryStatusResponse]:
    """Update Package Delivery Status

     Use this API to report delivery outcomes for SOF (Seller Own Fleet) packages or confirm O2O (Store
    Pickup) package delivery. For SOF, use `DELIVERY_SUCCESS`, `DELIVERY_FAILED`, or `UPDATE_POD`. For
    O2O, use `DELIVERY_SUCCESS` and provide the pickup verification code. Only sellers using SOF or O2O
    can use this API. This API is available only in the SEA region.

    Args:
        body (UpdatePackageDeliveryStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdatePackageDeliveryStatusResponse]
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
    body: UpdatePackageDeliveryStatusRequest,
) -> UpdatePackageDeliveryStatusResponse | None:
    """Update Package Delivery Status

     Use this API to report delivery outcomes for SOF (Seller Own Fleet) packages or confirm O2O (Store
    Pickup) package delivery. For SOF, use `DELIVERY_SUCCESS`, `DELIVERY_FAILED`, or `UPDATE_POD`. For
    O2O, use `DELIVERY_SUCCESS` and provide the pickup verification code. Only sellers using SOF or O2O
    can use this API. This API is available only in the SEA region.

    Args:
        body (UpdatePackageDeliveryStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdatePackageDeliveryStatusResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePackageDeliveryStatusRequest,
) -> Response[UpdatePackageDeliveryStatusResponse]:
    """Update Package Delivery Status

     Use this API to report delivery outcomes for SOF (Seller Own Fleet) packages or confirm O2O (Store
    Pickup) package delivery. For SOF, use `DELIVERY_SUCCESS`, `DELIVERY_FAILED`, or `UPDATE_POD`. For
    O2O, use `DELIVERY_SUCCESS` and provide the pickup verification code. Only sellers using SOF or O2O
    can use this API. This API is available only in the SEA region.

    Args:
        body (UpdatePackageDeliveryStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdatePackageDeliveryStatusResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePackageDeliveryStatusRequest,
) -> UpdatePackageDeliveryStatusResponse | None:
    """Update Package Delivery Status

     Use this API to report delivery outcomes for SOF (Seller Own Fleet) packages or confirm O2O (Store
    Pickup) package delivery. For SOF, use `DELIVERY_SUCCESS`, `DELIVERY_FAILED`, or `UPDATE_POD`. For
    O2O, use `DELIVERY_SUCCESS` and provide the pickup verification code. Only sellers using SOF or O2O
    can use this API. This API is available only in the SEA region.

    Args:
        body (UpdatePackageDeliveryStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdatePackageDeliveryStatusResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
