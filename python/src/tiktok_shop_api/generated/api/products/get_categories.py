from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_categories_listing_platform import GetCategoriesListingPlatform
from ...models.get_categories_locale import GetCategoriesLocale
from ...models.get_categories_response import GetCategoriesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    locale: GetCategoriesLocale | Unset = UNSET,
    keyword: str | Unset = UNSET,
    category_version: str | Unset = UNSET,
    listing_platform: GetCategoriesListingPlatform | Unset = UNSET,
    include_prohibited_categories: bool | Unset = UNSET,
    is_live_quick: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_locale: str | Unset = UNSET
    if not isinstance(locale, Unset):
        json_locale = locale.value

    params["locale"] = json_locale

    params["keyword"] = keyword

    params["category_version"] = category_version

    json_listing_platform: str | Unset = UNSET
    if not isinstance(listing_platform, Unset):
        json_listing_platform = listing_platform.value

    params["listing_platform"] = json_listing_platform

    params["include_prohibited_categories"] = include_prohibited_categories

    params["is_live_quick"] = is_live_quick

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/product/202309/categories",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetCategoriesResponse | None:
    if response.status_code == 200:
        response_200 = GetCategoriesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetCategoriesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    locale: GetCategoriesLocale | Unset = UNSET,
    keyword: str | Unset = UNSET,
    category_version: str | Unset = UNSET,
    listing_platform: GetCategoriesListingPlatform | Unset = UNSET,
    include_prohibited_categories: bool | Unset = UNSET,
    is_live_quick: bool | Unset = UNSET,
) -> Response[GetCategoriesResponse]:
    """Get Categories

     Retrieve the list of product categories available for your shop.
    Product categories are updated frequently, so it's recommended to call the API in real time to
    ensure you are using the latest category data. Caching category data locally may result in using
    outdated information, leading to errors when creating products.
    **For the Indonesia market**: To list a product on both TikTok Shop and Tokopedia, use only
    categories available on both platforms. Call this API once with `listing_platform` set to
    `TIKTOK_SHOP` and once with it set to `TOKOPEDIA`, then identify the categories returned by both
    calls.

    Args:
        locale (GetCategoriesLocale | Unset):
        keyword (str | Unset):
        category_version (str | Unset):
        listing_platform (GetCategoriesListingPlatform | Unset):
        include_prohibited_categories (bool | Unset):
        is_live_quick (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCategoriesResponse]
    """

    kwargs = _get_kwargs(
        locale=locale,
        keyword=keyword,
        category_version=category_version,
        listing_platform=listing_platform,
        include_prohibited_categories=include_prohibited_categories,
        is_live_quick=is_live_quick,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    locale: GetCategoriesLocale | Unset = UNSET,
    keyword: str | Unset = UNSET,
    category_version: str | Unset = UNSET,
    listing_platform: GetCategoriesListingPlatform | Unset = UNSET,
    include_prohibited_categories: bool | Unset = UNSET,
    is_live_quick: bool | Unset = UNSET,
) -> GetCategoriesResponse | None:
    """Get Categories

     Retrieve the list of product categories available for your shop.
    Product categories are updated frequently, so it's recommended to call the API in real time to
    ensure you are using the latest category data. Caching category data locally may result in using
    outdated information, leading to errors when creating products.
    **For the Indonesia market**: To list a product on both TikTok Shop and Tokopedia, use only
    categories available on both platforms. Call this API once with `listing_platform` set to
    `TIKTOK_SHOP` and once with it set to `TOKOPEDIA`, then identify the categories returned by both
    calls.

    Args:
        locale (GetCategoriesLocale | Unset):
        keyword (str | Unset):
        category_version (str | Unset):
        listing_platform (GetCategoriesListingPlatform | Unset):
        include_prohibited_categories (bool | Unset):
        is_live_quick (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCategoriesResponse
    """

    return sync_detailed(
        client=client,
        locale=locale,
        keyword=keyword,
        category_version=category_version,
        listing_platform=listing_platform,
        include_prohibited_categories=include_prohibited_categories,
        is_live_quick=is_live_quick,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    locale: GetCategoriesLocale | Unset = UNSET,
    keyword: str | Unset = UNSET,
    category_version: str | Unset = UNSET,
    listing_platform: GetCategoriesListingPlatform | Unset = UNSET,
    include_prohibited_categories: bool | Unset = UNSET,
    is_live_quick: bool | Unset = UNSET,
) -> Response[GetCategoriesResponse]:
    """Get Categories

     Retrieve the list of product categories available for your shop.
    Product categories are updated frequently, so it's recommended to call the API in real time to
    ensure you are using the latest category data. Caching category data locally may result in using
    outdated information, leading to errors when creating products.
    **For the Indonesia market**: To list a product on both TikTok Shop and Tokopedia, use only
    categories available on both platforms. Call this API once with `listing_platform` set to
    `TIKTOK_SHOP` and once with it set to `TOKOPEDIA`, then identify the categories returned by both
    calls.

    Args:
        locale (GetCategoriesLocale | Unset):
        keyword (str | Unset):
        category_version (str | Unset):
        listing_platform (GetCategoriesListingPlatform | Unset):
        include_prohibited_categories (bool | Unset):
        is_live_quick (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCategoriesResponse]
    """

    kwargs = _get_kwargs(
        locale=locale,
        keyword=keyword,
        category_version=category_version,
        listing_platform=listing_platform,
        include_prohibited_categories=include_prohibited_categories,
        is_live_quick=is_live_quick,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    locale: GetCategoriesLocale | Unset = UNSET,
    keyword: str | Unset = UNSET,
    category_version: str | Unset = UNSET,
    listing_platform: GetCategoriesListingPlatform | Unset = UNSET,
    include_prohibited_categories: bool | Unset = UNSET,
    is_live_quick: bool | Unset = UNSET,
) -> GetCategoriesResponse | None:
    """Get Categories

     Retrieve the list of product categories available for your shop.
    Product categories are updated frequently, so it's recommended to call the API in real time to
    ensure you are using the latest category data. Caching category data locally may result in using
    outdated information, leading to errors when creating products.
    **For the Indonesia market**: To list a product on both TikTok Shop and Tokopedia, use only
    categories available on both platforms. Call this API once with `listing_platform` set to
    `TIKTOK_SHOP` and once with it set to `TOKOPEDIA`, then identify the categories returned by both
    calls.

    Args:
        locale (GetCategoriesLocale | Unset):
        keyword (str | Unset):
        category_version (str | Unset):
        listing_platform (GetCategoriesListingPlatform | Unset):
        include_prohibited_categories (bool | Unset):
        is_live_quick (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCategoriesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            locale=locale,
            keyword=keyword,
            category_version=category_version,
            listing_platform=listing_platform,
            include_prohibited_categories=include_prohibited_categories,
            is_live_quick=is_live_quick,
        )
    ).parsed
