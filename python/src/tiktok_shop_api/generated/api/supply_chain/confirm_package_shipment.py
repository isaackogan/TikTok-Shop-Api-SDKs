from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.confirm_package_shipment_request import ConfirmPackageShipmentRequest
from ...models.confirm_package_shipment_response import ConfirmPackageShipmentResponse
from typing import cast



def _get_kwargs(
    *,
    body: ConfirmPackageShipmentRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/supply_chain/202309/packages/sync",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConfirmPackageShipmentResponse | None:
    if response.status_code == 200:
        response_200 = ConfirmPackageShipmentResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConfirmPackageShipmentResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ConfirmPackageShipmentRequest,

) -> Response[ConfirmPackageShipmentResponse]:
    """ Confirm Package Shipment

     Use this API to submit package shipment information. Only warehouse service providers certified by
    TikTok Shop can access this API. Packages are processed independently, so a request can partially
    succeed. Review both `success_packages` and `errors` when handling the response.

    Args:
        body (ConfirmPackageShipmentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfirmPackageShipmentResponse]
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
    body: ConfirmPackageShipmentRequest,

) -> ConfirmPackageShipmentResponse | None:
    """ Confirm Package Shipment

     Use this API to submit package shipment information. Only warehouse service providers certified by
    TikTok Shop can access this API. Packages are processed independently, so a request can partially
    succeed. Review both `success_packages` and `errors` when handling the response.

    Args:
        body (ConfirmPackageShipmentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfirmPackageShipmentResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ConfirmPackageShipmentRequest,

) -> Response[ConfirmPackageShipmentResponse]:
    """ Confirm Package Shipment

     Use this API to submit package shipment information. Only warehouse service providers certified by
    TikTok Shop can access this API. Packages are processed independently, so a request can partially
    succeed. Review both `success_packages` and `errors` when handling the response.

    Args:
        body (ConfirmPackageShipmentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfirmPackageShipmentResponse]
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
    body: ConfirmPackageShipmentRequest,

) -> ConfirmPackageShipmentResponse | None:
    """ Confirm Package Shipment

     Use this API to submit package shipment information. Only warehouse service providers certified by
    TikTok Shop can access this API. Packages are processed independently, so a request can partially
    succeed. Review both `success_packages` and `errors` when handling the response.

    Args:
        body (ConfirmPackageShipmentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfirmPackageShipmentResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
