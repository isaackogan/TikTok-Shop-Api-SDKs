from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_shipping_providers_response import GetShippingProvidersResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    delivery_option_id: str,
    *,
    warehouse_region: str | Unset = UNSET,
    buyer_region: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["warehouse_region"] = warehouse_region

    params["buyer_region"] = buyer_region

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/logistics/202309/delivery_options/{delivery_option_id}/shipping_providers".format(
            delivery_option_id=quote(str(delivery_option_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetShippingProvidersResponse | None:
    if response.status_code == 200:
        response_200 = GetShippingProvidersResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetShippingProvidersResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    delivery_option_id: str,
    *,
    client: AuthenticatedClient | Client,
    warehouse_region: str | Unset = UNSET,
    buyer_region: str | Unset = UNSET,
) -> Response[GetShippingProvidersResponse]:
    """Get Shipping Providers

     Returns the shipping providers available for the specified delivery option. If the delivery option
    is fulfilled by TikTok, the request returns an error and no shipping providers are returned.

    Args:
        delivery_option_id (str):
        warehouse_region (str | Unset):
        buyer_region (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShippingProvidersResponse]
    """

    kwargs = _get_kwargs(
        delivery_option_id=delivery_option_id,
        warehouse_region=warehouse_region,
        buyer_region=buyer_region,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    delivery_option_id: str,
    *,
    client: AuthenticatedClient | Client,
    warehouse_region: str | Unset = UNSET,
    buyer_region: str | Unset = UNSET,
) -> GetShippingProvidersResponse | None:
    """Get Shipping Providers

     Returns the shipping providers available for the specified delivery option. If the delivery option
    is fulfilled by TikTok, the request returns an error and no shipping providers are returned.

    Args:
        delivery_option_id (str):
        warehouse_region (str | Unset):
        buyer_region (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShippingProvidersResponse
    """

    return sync_detailed(
        delivery_option_id=delivery_option_id,
        client=client,
        warehouse_region=warehouse_region,
        buyer_region=buyer_region,
    ).parsed


async def asyncio_detailed(
    delivery_option_id: str,
    *,
    client: AuthenticatedClient | Client,
    warehouse_region: str | Unset = UNSET,
    buyer_region: str | Unset = UNSET,
) -> Response[GetShippingProvidersResponse]:
    """Get Shipping Providers

     Returns the shipping providers available for the specified delivery option. If the delivery option
    is fulfilled by TikTok, the request returns an error and no shipping providers are returned.

    Args:
        delivery_option_id (str):
        warehouse_region (str | Unset):
        buyer_region (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShippingProvidersResponse]
    """

    kwargs = _get_kwargs(
        delivery_option_id=delivery_option_id,
        warehouse_region=warehouse_region,
        buyer_region=buyer_region,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    delivery_option_id: str,
    *,
    client: AuthenticatedClient | Client,
    warehouse_region: str | Unset = UNSET,
    buyer_region: str | Unset = UNSET,
) -> GetShippingProvidersResponse | None:
    """Get Shipping Providers

     Returns the shipping providers available for the specified delivery option. If the delivery option
    is fulfilled by TikTok, the request returns an error and no shipping providers are returned.

    Args:
        delivery_option_id (str):
        warehouse_region (str | Unset):
        buyer_region (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShippingProvidersResponse
    """

    return (
        await asyncio_detailed(
            delivery_option_id=delivery_option_id,
            client=client,
            warehouse_region=warehouse_region,
            buyer_region=buyer_region,
        )
    ).parsed
