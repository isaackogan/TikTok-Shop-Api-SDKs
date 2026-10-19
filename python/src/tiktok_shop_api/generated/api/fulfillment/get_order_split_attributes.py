from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_order_split_attributes_response import GetOrderSplitAttributesResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    order_ids: list[str],
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_order_ids = order_ids

    params["order_ids"] = json_order_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fulfillment/202309/orders/split_attributes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetOrderSplitAttributesResponse | None:
    if response.status_code == 200:
        response_200 = GetOrderSplitAttributesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetOrderSplitAttributesResponse]:
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
) -> Response[GetOrderSplitAttributesResponse]:
    """Get Order Split Attributes

     Checks whether one or more TikTok Shop orders can be split into multiple packages. For each
    evaluated order, the response indicates whether it can be split and may include a reason when
    splitting is not allowed and mandatory package-splitting limits when applicable.

    Args:
        order_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrderSplitAttributesResponse]
    """

    kwargs = _get_kwargs(
        order_ids=order_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    order_ids: list[str],
) -> GetOrderSplitAttributesResponse | None:
    """Get Order Split Attributes

     Checks whether one or more TikTok Shop orders can be split into multiple packages. For each
    evaluated order, the response indicates whether it can be split and may include a reason when
    splitting is not allowed and mandatory package-splitting limits when applicable.

    Args:
        order_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOrderSplitAttributesResponse
    """

    return sync_detailed(
        client=client,
        order_ids=order_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    order_ids: list[str],
) -> Response[GetOrderSplitAttributesResponse]:
    """Get Order Split Attributes

     Checks whether one or more TikTok Shop orders can be split into multiple packages. For each
    evaluated order, the response indicates whether it can be split and may include a reason when
    splitting is not allowed and mandatory package-splitting limits when applicable.

    Args:
        order_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrderSplitAttributesResponse]
    """

    kwargs = _get_kwargs(
        order_ids=order_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    order_ids: list[str],
) -> GetOrderSplitAttributesResponse | None:
    """Get Order Split Attributes

     Checks whether one or more TikTok Shop orders can be split into multiple packages. For each
    evaluated order, the response indicates whether it can be split and may include a reason when
    splitting is not allowed and mandatory package-splitting limits when applicable.

    Args:
        order_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOrderSplitAttributesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            order_ids=order_ids,
        )
    ).parsed
