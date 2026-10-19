from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_order_list_request import GetOrderListRequest
from ...models.get_order_list_response import GetOrderListResponse
from ...models.get_order_list_sort_field import GetOrderListSortField
from ...models.get_order_list_sort_order import GetOrderListSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: GetOrderListRequest | Unset = UNSET,
    page_size: int,
    sort_order: GetOrderListSortOrder | Unset = UNSET,
    page_token: str | Unset = UNSET,
    sort_field: GetOrderListSortField | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["page_size"] = page_size

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sort_order"] = json_sort_order

    params["page_token"] = page_token

    json_sort_field: str | Unset = UNSET
    if not isinstance(sort_field, Unset):
        json_sort_field = sort_field.value

    params["sort_field"] = json_sort_field

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/order/202309/orders/search",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetOrderListResponse | None:
    if response.status_code == 200:
        response_200 = GetOrderListResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetOrderListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetOrderListRequest | Unset = UNSET,
    page_size: int,
    sort_order: GetOrderListSortOrder | Unset = UNSET,
    page_token: str | Unset = UNSET,
    sort_field: GetOrderListSortField | Unset = UNSET,
) -> Response[GetOrderListResponse]:
    """Get Order List

     Returns a list of orders created or updated during the timeframe indicated by the specified
    parameters. You can also apply a range of filtering criteria to narrow the list of orders returned,
    such as order status, delivery option type, and buyer user ID.

    Args:
        page_size (int):
        sort_order (GetOrderListSortOrder | Unset):
        page_token (str | Unset):
        sort_field (GetOrderListSortField | Unset):
        body (GetOrderListRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrderListResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        page_size=page_size,
        sort_order=sort_order,
        page_token=page_token,
        sort_field=sort_field,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: GetOrderListRequest | Unset = UNSET,
    page_size: int,
    sort_order: GetOrderListSortOrder | Unset = UNSET,
    page_token: str | Unset = UNSET,
    sort_field: GetOrderListSortField | Unset = UNSET,
) -> GetOrderListResponse | None:
    """Get Order List

     Returns a list of orders created or updated during the timeframe indicated by the specified
    parameters. You can also apply a range of filtering criteria to narrow the list of orders returned,
    such as order status, delivery option type, and buyer user ID.

    Args:
        page_size (int):
        sort_order (GetOrderListSortOrder | Unset):
        page_token (str | Unset):
        sort_field (GetOrderListSortField | Unset):
        body (GetOrderListRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOrderListResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        page_size=page_size,
        sort_order=sort_order,
        page_token=page_token,
        sort_field=sort_field,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetOrderListRequest | Unset = UNSET,
    page_size: int,
    sort_order: GetOrderListSortOrder | Unset = UNSET,
    page_token: str | Unset = UNSET,
    sort_field: GetOrderListSortField | Unset = UNSET,
) -> Response[GetOrderListResponse]:
    """Get Order List

     Returns a list of orders created or updated during the timeframe indicated by the specified
    parameters. You can also apply a range of filtering criteria to narrow the list of orders returned,
    such as order status, delivery option type, and buyer user ID.

    Args:
        page_size (int):
        sort_order (GetOrderListSortOrder | Unset):
        page_token (str | Unset):
        sort_field (GetOrderListSortField | Unset):
        body (GetOrderListRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrderListResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        page_size=page_size,
        sort_order=sort_order,
        page_token=page_token,
        sort_field=sort_field,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GetOrderListRequest | Unset = UNSET,
    page_size: int,
    sort_order: GetOrderListSortOrder | Unset = UNSET,
    page_token: str | Unset = UNSET,
    sort_field: GetOrderListSortField | Unset = UNSET,
) -> GetOrderListResponse | None:
    """Get Order List

     Returns a list of orders created or updated during the timeframe indicated by the specified
    parameters. You can also apply a range of filtering criteria to narrow the list of orders returned,
    such as order status, delivery option type, and buyer user ID.

    Args:
        page_size (int):
        sort_order (GetOrderListSortOrder | Unset):
        page_token (str | Unset):
        sort_field (GetOrderListSortField | Unset):
        body (GetOrderListRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOrderListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            page_size=page_size,
            sort_order=sort_order,
            page_token=page_token,
            sort_field=sort_field,
        )
    ).parsed
