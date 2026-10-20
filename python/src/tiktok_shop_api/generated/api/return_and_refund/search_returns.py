from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_returns_request import SearchReturnsRequest
from ...models.search_returns_response import SearchReturnsResponse
from ...models.search_returns_sort_field import SearchReturnsSortField
from ...models.search_returns_sort_order import SearchReturnsSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SearchReturnsRequest | Unset = UNSET,
    sort_field: SearchReturnsSortField | Unset = UNSET,
    sort_order: SearchReturnsSortOrder | Unset = UNSET,
    page_size: str | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_sort_field: str | Unset = UNSET
    if not isinstance(sort_field, Unset):
        json_sort_field = sort_field.value

    params["sort_field"] = json_sort_field

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sort_order"] = json_sort_order

    params["page_size"] = page_size

    params["page_token"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/return_refund/202602/returns/search",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchReturnsResponse | None:
    if response.status_code == 200:
        response_200 = SearchReturnsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SearchReturnsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchReturnsRequest | Unset = UNSET,
    sort_field: SearchReturnsSortField | Unset = UNSET,
    sort_order: SearchReturnsSortOrder | Unset = UNSET,
    page_size: str | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Response[SearchReturnsResponse]:
    """Search Returns

     Use this API to search returns by return ID, order ID, buyer, return type, return status,
    arbitration status, or create/update time window. The response is paginated. To retrieve the next
    page, pass the previous `next_page_token` as `page_token` and keep all other filters and sorting
    unchanged.

    Args:
        sort_field (SearchReturnsSortField | Unset):
        sort_order (SearchReturnsSortOrder | Unset):
        page_size (str | Unset):
        page_token (str | Unset):
        body (SearchReturnsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchReturnsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        sort_field=sort_field,
        sort_order=sort_order,
        page_size=page_size,
        page_token=page_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SearchReturnsRequest | Unset = UNSET,
    sort_field: SearchReturnsSortField | Unset = UNSET,
    sort_order: SearchReturnsSortOrder | Unset = UNSET,
    page_size: str | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> SearchReturnsResponse | None:
    """Search Returns

     Use this API to search returns by return ID, order ID, buyer, return type, return status,
    arbitration status, or create/update time window. The response is paginated. To retrieve the next
    page, pass the previous `next_page_token` as `page_token` and keep all other filters and sorting
    unchanged.

    Args:
        sort_field (SearchReturnsSortField | Unset):
        sort_order (SearchReturnsSortOrder | Unset):
        page_size (str | Unset):
        page_token (str | Unset):
        body (SearchReturnsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchReturnsResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        sort_field=sort_field,
        sort_order=sort_order,
        page_size=page_size,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchReturnsRequest | Unset = UNSET,
    sort_field: SearchReturnsSortField | Unset = UNSET,
    sort_order: SearchReturnsSortOrder | Unset = UNSET,
    page_size: str | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Response[SearchReturnsResponse]:
    """Search Returns

     Use this API to search returns by return ID, order ID, buyer, return type, return status,
    arbitration status, or create/update time window. The response is paginated. To retrieve the next
    page, pass the previous `next_page_token` as `page_token` and keep all other filters and sorting
    unchanged.

    Args:
        sort_field (SearchReturnsSortField | Unset):
        sort_order (SearchReturnsSortOrder | Unset):
        page_size (str | Unset):
        page_token (str | Unset):
        body (SearchReturnsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchReturnsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        sort_field=sort_field,
        sort_order=sort_order,
        page_size=page_size,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchReturnsRequest | Unset = UNSET,
    sort_field: SearchReturnsSortField | Unset = UNSET,
    sort_order: SearchReturnsSortOrder | Unset = UNSET,
    page_size: str | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> SearchReturnsResponse | None:
    """Search Returns

     Use this API to search returns by return ID, order ID, buyer, return type, return status,
    arbitration status, or create/update time window. The response is paginated. To retrieve the next
    page, pass the previous `next_page_token` as `page_token` and keep all other filters and sorting
    unchanged.

    Args:
        sort_field (SearchReturnsSortField | Unset):
        sort_order (SearchReturnsSortOrder | Unset):
        page_size (str | Unset):
        page_token (str | Unset):
        body (SearchReturnsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchReturnsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            sort_field=sort_field,
            sort_order=sort_order,
            page_size=page_size,
            page_token=page_token,
        )
    ).parsed
