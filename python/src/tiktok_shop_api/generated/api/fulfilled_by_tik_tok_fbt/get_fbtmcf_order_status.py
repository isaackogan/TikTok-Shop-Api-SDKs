from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_fbtmcf_order_status_response import GetFBTMCFOrderStatusResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    mcf_order_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["mcf_order_id"] = mcf_order_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fbt/202601/mcf_outbound_orders",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetFBTMCFOrderStatusResponse | None:
    if response.status_code == 200:
        response_200 = GetFBTMCFOrderStatusResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetFBTMCFOrderStatusResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    mcf_order_id: str,
) -> Response[GetFBTMCFOrderStatusResponse]:
    """Get FBT MCF Order Status

     Use this API to retrieve an MCF order and the current status and fulfillment details of its consign
    orders. If the order requires multiple packages because of carrier restrictions or package-size
    limits, the FBT system splits it for fulfillment and returns one entry in `consign_orders` for each
    package.

    Args:
        mcf_order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFBTMCFOrderStatusResponse]
    """

    kwargs = _get_kwargs(
        mcf_order_id=mcf_order_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    mcf_order_id: str,
) -> GetFBTMCFOrderStatusResponse | None:
    """Get FBT MCF Order Status

     Use this API to retrieve an MCF order and the current status and fulfillment details of its consign
    orders. If the order requires multiple packages because of carrier restrictions or package-size
    limits, the FBT system splits it for fulfillment and returns one entry in `consign_orders` for each
    package.

    Args:
        mcf_order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFBTMCFOrderStatusResponse
    """

    return sync_detailed(
        client=client,
        mcf_order_id=mcf_order_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    mcf_order_id: str,
) -> Response[GetFBTMCFOrderStatusResponse]:
    """Get FBT MCF Order Status

     Use this API to retrieve an MCF order and the current status and fulfillment details of its consign
    orders. If the order requires multiple packages because of carrier restrictions or package-size
    limits, the FBT system splits it for fulfillment and returns one entry in `consign_orders` for each
    package.

    Args:
        mcf_order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFBTMCFOrderStatusResponse]
    """

    kwargs = _get_kwargs(
        mcf_order_id=mcf_order_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    mcf_order_id: str,
) -> GetFBTMCFOrderStatusResponse | None:
    """Get FBT MCF Order Status

     Use this API to retrieve an MCF order and the current status and fulfillment details of its consign
    orders. If the order requires multiple packages because of carrier restrictions or package-size
    limits, the FBT system splits it for fulfillment and returns one entry in `consign_orders` for each
    package.

    Args:
        mcf_order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFBTMCFOrderStatusResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            mcf_order_id=mcf_order_id,
        )
    ).parsed
