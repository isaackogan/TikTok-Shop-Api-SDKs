from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_affiliate_orders_by_creator_request import SearchAffiliateOrdersByCreatorRequest
from ...models.search_affiliate_orders_by_creator_response import SearchAffiliateOrdersByCreatorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SearchAffiliateOrdersByCreatorRequest,
    page_token: str | Unset = UNSET,
    page_size: int,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["page_token"] = page_token

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_creator/202505/orders/trace/search",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SearchAffiliateOrdersByCreatorResponse | None:
    if response.status_code == 200:
        response_200 = SearchAffiliateOrdersByCreatorResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SearchAffiliateOrdersByCreatorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchAffiliateOrdersByCreatorRequest,
    page_token: str | Unset = UNSET,
    page_size: int,
) -> Response[SearchAffiliateOrdersByCreatorResponse]:
    """Search Affiliate Orders by Creator

     Retrieves affiliate orders attributed to the creator represented by the current access token.
    Results can provide order status and timestamps, together with SKU-level product, shop, content,
    trace, quantity, price, and estimated or actual commission details.

    Args:
        page_token (str | Unset):
        page_size (int):
        body (SearchAffiliateOrdersByCreatorRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchAffiliateOrdersByCreatorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        page_token=page_token,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SearchAffiliateOrdersByCreatorRequest,
    page_token: str | Unset = UNSET,
    page_size: int,
) -> SearchAffiliateOrdersByCreatorResponse | None:
    """Search Affiliate Orders by Creator

     Retrieves affiliate orders attributed to the creator represented by the current access token.
    Results can provide order status and timestamps, together with SKU-level product, shop, content,
    trace, quantity, price, and estimated or actual commission details.

    Args:
        page_token (str | Unset):
        page_size (int):
        body (SearchAffiliateOrdersByCreatorRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchAffiliateOrdersByCreatorResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        page_token=page_token,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchAffiliateOrdersByCreatorRequest,
    page_token: str | Unset = UNSET,
    page_size: int,
) -> Response[SearchAffiliateOrdersByCreatorResponse]:
    """Search Affiliate Orders by Creator

     Retrieves affiliate orders attributed to the creator represented by the current access token.
    Results can provide order status and timestamps, together with SKU-level product, shop, content,
    trace, quantity, price, and estimated or actual commission details.

    Args:
        page_token (str | Unset):
        page_size (int):
        body (SearchAffiliateOrdersByCreatorRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchAffiliateOrdersByCreatorResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        page_token=page_token,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchAffiliateOrdersByCreatorRequest,
    page_token: str | Unset = UNSET,
    page_size: int,
) -> SearchAffiliateOrdersByCreatorResponse | None:
    """Search Affiliate Orders by Creator

     Retrieves affiliate orders attributed to the creator represented by the current access token.
    Results can provide order status and timestamps, together with SKU-level product, shop, content,
    trace, quantity, price, and estimated or actual commission details.

    Args:
        page_token (str | Unset):
        page_size (int):
        body (SearchAffiliateOrdersByCreatorRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchAffiliateOrdersByCreatorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            page_token=page_token,
            page_size=page_size,
        )
    ).parsed
