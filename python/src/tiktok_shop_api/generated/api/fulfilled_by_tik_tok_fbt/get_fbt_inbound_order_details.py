from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_fbt_inbound_order_details_response import GetFBTInboundOrderDetailsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    order_ids: list[str],
    include_carton_details: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_order_ids = order_ids

    params["order_ids"] = json_order_ids

    params["include_carton_details"] = include_carton_details

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fbt/202602/inbound_orders",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetFBTInboundOrderDetailsResponse | None:
    if response.status_code == 200:
        response_200 = GetFBTInboundOrderDetailsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetFBTInboundOrderDetailsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    order_ids: list[str],
    include_carton_details: bool | Unset = UNSET,
) -> Response[GetFBTInboundOrderDetailsResponse]:
    """Get FBT Inbound Order Details

     Retrieves details for the specified FBT inbound orders, including planned and actual receiving
    information and status history. Set `include_carton_details` to `true` to request carton dimensions
    and item quantities.

    Args:
        order_ids (list[str]):
        include_carton_details (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFBTInboundOrderDetailsResponse]
    """

    kwargs = _get_kwargs(
        order_ids=order_ids,
        include_carton_details=include_carton_details,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    order_ids: list[str],
    include_carton_details: bool | Unset = UNSET,
) -> GetFBTInboundOrderDetailsResponse | None:
    """Get FBT Inbound Order Details

     Retrieves details for the specified FBT inbound orders, including planned and actual receiving
    information and status history. Set `include_carton_details` to `true` to request carton dimensions
    and item quantities.

    Args:
        order_ids (list[str]):
        include_carton_details (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFBTInboundOrderDetailsResponse
    """

    return sync_detailed(
        client=client,
        order_ids=order_ids,
        include_carton_details=include_carton_details,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    order_ids: list[str],
    include_carton_details: bool | Unset = UNSET,
) -> Response[GetFBTInboundOrderDetailsResponse]:
    """Get FBT Inbound Order Details

     Retrieves details for the specified FBT inbound orders, including planned and actual receiving
    information and status history. Set `include_carton_details` to `true` to request carton dimensions
    and item quantities.

    Args:
        order_ids (list[str]):
        include_carton_details (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFBTInboundOrderDetailsResponse]
    """

    kwargs = _get_kwargs(
        order_ids=order_ids,
        include_carton_details=include_carton_details,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    order_ids: list[str],
    include_carton_details: bool | Unset = UNSET,
) -> GetFBTInboundOrderDetailsResponse | None:
    """Get FBT Inbound Order Details

     Retrieves details for the specified FBT inbound orders, including planned and actual receiving
    information and status history. Set `include_carton_details` to `true` to request carton dimensions
    and item quantities.

    Args:
        order_ids (list[str]):
        include_carton_details (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFBTInboundOrderDetailsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            order_ids=order_ids,
            include_carton_details=include_carton_details,
        )
    ).parsed
