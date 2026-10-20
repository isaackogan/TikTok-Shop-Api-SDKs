from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_creator_marketplace_advanced_search_filters_request import (
    GetCreatorMarketplaceAdvancedSearchFiltersRequest,
)
from ...models.get_creator_marketplace_advanced_search_filters_response import (
    GetCreatorMarketplaceAdvancedSearchFiltersResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: GetCreatorMarketplaceAdvancedSearchFiltersRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_seller/202608/marketplace_creators/search/filter",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetCreatorMarketplaceAdvancedSearchFiltersResponse | None:
    if response.status_code == 200:
        response_200 = GetCreatorMarketplaceAdvancedSearchFiltersResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetCreatorMarketplaceAdvancedSearchFiltersResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetCreatorMarketplaceAdvancedSearchFiltersRequest | Unset = UNSET,
) -> Response[GetCreatorMarketplaceAdvancedSearchFiltersResponse]:
    """Get Creator Marketplace Advanced Search Filters

     This API allows you to obtain the advanced filters available in Seller Search Creator Marketplace.
    Because we are constantly releasing new filters which are specific to each country or region, this
    API serves as a way for developers to retrieve the latest available search filters.

    Args:
        body (GetCreatorMarketplaceAdvancedSearchFiltersRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCreatorMarketplaceAdvancedSearchFiltersResponse]
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
    body: GetCreatorMarketplaceAdvancedSearchFiltersRequest | Unset = UNSET,
) -> GetCreatorMarketplaceAdvancedSearchFiltersResponse | None:
    """Get Creator Marketplace Advanced Search Filters

     This API allows you to obtain the advanced filters available in Seller Search Creator Marketplace.
    Because we are constantly releasing new filters which are specific to each country or region, this
    API serves as a way for developers to retrieve the latest available search filters.

    Args:
        body (GetCreatorMarketplaceAdvancedSearchFiltersRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCreatorMarketplaceAdvancedSearchFiltersResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetCreatorMarketplaceAdvancedSearchFiltersRequest | Unset = UNSET,
) -> Response[GetCreatorMarketplaceAdvancedSearchFiltersResponse]:
    """Get Creator Marketplace Advanced Search Filters

     This API allows you to obtain the advanced filters available in Seller Search Creator Marketplace.
    Because we are constantly releasing new filters which are specific to each country or region, this
    API serves as a way for developers to retrieve the latest available search filters.

    Args:
        body (GetCreatorMarketplaceAdvancedSearchFiltersRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCreatorMarketplaceAdvancedSearchFiltersResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GetCreatorMarketplaceAdvancedSearchFiltersRequest | Unset = UNSET,
) -> GetCreatorMarketplaceAdvancedSearchFiltersResponse | None:
    """Get Creator Marketplace Advanced Search Filters

     This API allows you to obtain the advanced filters available in Seller Search Creator Marketplace.
    Because we are constantly releasing new filters which are specific to each country or region, this
    API serves as a way for developers to retrieve the latest available search filters.

    Args:
        body (GetCreatorMarketplaceAdvancedSearchFiltersRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCreatorMarketplaceAdvancedSearchFiltersResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
