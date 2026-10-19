from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_tap_affiliate_orders_request import SearchTAPAffiliateOrdersRequest
from ...models.search_tap_affiliate_orders_response import SearchTAPAffiliateOrdersResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SearchTAPAffiliateOrdersRequest | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int,
    category_asset_cipher: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["page_token"] = page_token

    params["page_size"] = page_size

    params["category_asset_cipher"] = category_asset_cipher

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_partner/202603/orders/search",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SearchTAPAffiliateOrdersResponse | None:
    if response.status_code == 200:
        response_200 = SearchTAPAffiliateOrdersResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SearchTAPAffiliateOrdersResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchTAPAffiliateOrdersRequest | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int,
    category_asset_cipher: str,
) -> Response[SearchTAPAffiliateOrdersResponse]:
    """Search TAP Affiliate Orders

     TAP can use this API to retrieve a list of affiliate orders and track the affiliate conversions.

    Args:
        page_token (str | Unset):
        page_size (int):
        category_asset_cipher (str):
        body (SearchTAPAffiliateOrdersRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchTAPAffiliateOrdersResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        page_token=page_token,
        page_size=page_size,
        category_asset_cipher=category_asset_cipher,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SearchTAPAffiliateOrdersRequest | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int,
    category_asset_cipher: str,
) -> SearchTAPAffiliateOrdersResponse | None:
    """Search TAP Affiliate Orders

     TAP can use this API to retrieve a list of affiliate orders and track the affiliate conversions.

    Args:
        page_token (str | Unset):
        page_size (int):
        category_asset_cipher (str):
        body (SearchTAPAffiliateOrdersRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchTAPAffiliateOrdersResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        page_token=page_token,
        page_size=page_size,
        category_asset_cipher=category_asset_cipher,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchTAPAffiliateOrdersRequest | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int,
    category_asset_cipher: str,
) -> Response[SearchTAPAffiliateOrdersResponse]:
    """Search TAP Affiliate Orders

     TAP can use this API to retrieve a list of affiliate orders and track the affiliate conversions.

    Args:
        page_token (str | Unset):
        page_size (int):
        category_asset_cipher (str):
        body (SearchTAPAffiliateOrdersRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchTAPAffiliateOrdersResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        page_token=page_token,
        page_size=page_size,
        category_asset_cipher=category_asset_cipher,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchTAPAffiliateOrdersRequest | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int,
    category_asset_cipher: str,
) -> SearchTAPAffiliateOrdersResponse | None:
    """Search TAP Affiliate Orders

     TAP can use this API to retrieve a list of affiliate orders and track the affiliate conversions.

    Args:
        page_token (str | Unset):
        page_size (int):
        category_asset_cipher (str):
        body (SearchTAPAffiliateOrdersRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchTAPAffiliateOrdersResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            page_token=page_token,
            page_size=page_size,
            category_asset_cipher=category_asset_cipher,
        )
    ).parsed
