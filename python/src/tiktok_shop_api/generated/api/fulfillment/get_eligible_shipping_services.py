from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_eligible_shipping_services_request import GetEligibleShippingServicesRequest
from ...models.get_eligible_shipping_services_response import GetEligibleShippingServicesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    order_id: str,
    *,
    body: GetEligibleShippingServicesRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fulfillment/202309/orders/{order_id}/shipping_services/query".format(
            order_id=quote(str(order_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetEligibleShippingServicesResponse | None:
    if response.status_code == 200:
        response_200 = GetEligibleShippingServicesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetEligibleShippingServicesResponse]:
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
    body: GetEligibleShippingServicesRequest | Unset = UNSET,
) -> Response[GetEligibleShippingServicesResponse]:
    """Get Eligible Shipping Services

     Retrieve available shipping services in the US and JP. Package dimensions and weight are optional
    inputs used to calculate the available options. Shipping fees and delivery times are estimates based
    on the package attributes used for the query, and the available options may change if those
    attributes change at the time of shipping.

    Args:
        order_id (str):
        body (GetEligibleShippingServicesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetEligibleShippingServicesResponse]
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
    body: GetEligibleShippingServicesRequest | Unset = UNSET,
) -> GetEligibleShippingServicesResponse | None:
    """Get Eligible Shipping Services

     Retrieve available shipping services in the US and JP. Package dimensions and weight are optional
    inputs used to calculate the available options. Shipping fees and delivery times are estimates based
    on the package attributes used for the query, and the available options may change if those
    attributes change at the time of shipping.

    Args:
        order_id (str):
        body (GetEligibleShippingServicesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetEligibleShippingServicesResponse
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
    body: GetEligibleShippingServicesRequest | Unset = UNSET,
) -> Response[GetEligibleShippingServicesResponse]:
    """Get Eligible Shipping Services

     Retrieve available shipping services in the US and JP. Package dimensions and weight are optional
    inputs used to calculate the available options. Shipping fees and delivery times are estimates based
    on the package attributes used for the query, and the available options may change if those
    attributes change at the time of shipping.

    Args:
        order_id (str):
        body (GetEligibleShippingServicesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetEligibleShippingServicesResponse]
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
    body: GetEligibleShippingServicesRequest | Unset = UNSET,
) -> GetEligibleShippingServicesResponse | None:
    """Get Eligible Shipping Services

     Retrieve available shipping services in the US and JP. Package dimensions and weight are optional
    inputs used to calculate the available options. Shipping fees and delivery times are estimates based
    on the package attributes used for the query, and the available options may change if those
    attributes change at the time of shipping.

    Args:
        order_id (str):
        body (GetEligibleShippingServicesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetEligibleShippingServicesResponse
    """

    return (
        await asyncio_detailed(
            order_id=order_id,
            client=client,
            body=body,
        )
    ).parsed
