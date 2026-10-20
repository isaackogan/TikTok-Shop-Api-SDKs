from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_global_categories_locale import GetGlobalCategoriesLocale
from ...models.get_global_categories_response import GetGlobalCategoriesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    locale: GetGlobalCategoriesLocale | Unset = UNSET,
    keyword: str | Unset = UNSET,
    category_version: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_locale: str | Unset = UNSET
    if not isinstance(locale, Unset):
        json_locale = locale.value

    params["locale"] = json_locale

    params["keyword"] = keyword

    params["category_version"] = category_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/product/202309/global_categories",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetGlobalCategoriesResponse | None:
    if response.status_code == 200:
        response_200 = GetGlobalCategoriesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetGlobalCategoriesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    locale: GetGlobalCategoriesLocale | Unset = UNSET,
    keyword: str | Unset = UNSET,
    category_version: str | Unset = UNSET,
) -> Response[GetGlobalCategoriesResponse]:
    """Get Global Categories

     Retrieve all available product categories, regardless of market variations.
    Product categories are updated frequently, so it's recommended to call the API in real time to
    ensure you are using the latest category data. Caching category data locally may result in using
    outdated information, leading to errors when creating global products.

    Args:
        locale (GetGlobalCategoriesLocale | Unset):
        keyword (str | Unset):
        category_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGlobalCategoriesResponse]
    """

    kwargs = _get_kwargs(
        locale=locale,
        keyword=keyword,
        category_version=category_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    locale: GetGlobalCategoriesLocale | Unset = UNSET,
    keyword: str | Unset = UNSET,
    category_version: str | Unset = UNSET,
) -> GetGlobalCategoriesResponse | None:
    """Get Global Categories

     Retrieve all available product categories, regardless of market variations.
    Product categories are updated frequently, so it's recommended to call the API in real time to
    ensure you are using the latest category data. Caching category data locally may result in using
    outdated information, leading to errors when creating global products.

    Args:
        locale (GetGlobalCategoriesLocale | Unset):
        keyword (str | Unset):
        category_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGlobalCategoriesResponse
    """

    return sync_detailed(
        client=client,
        locale=locale,
        keyword=keyword,
        category_version=category_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    locale: GetGlobalCategoriesLocale | Unset = UNSET,
    keyword: str | Unset = UNSET,
    category_version: str | Unset = UNSET,
) -> Response[GetGlobalCategoriesResponse]:
    """Get Global Categories

     Retrieve all available product categories, regardless of market variations.
    Product categories are updated frequently, so it's recommended to call the API in real time to
    ensure you are using the latest category data. Caching category data locally may result in using
    outdated information, leading to errors when creating global products.

    Args:
        locale (GetGlobalCategoriesLocale | Unset):
        keyword (str | Unset):
        category_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGlobalCategoriesResponse]
    """

    kwargs = _get_kwargs(
        locale=locale,
        keyword=keyword,
        category_version=category_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    locale: GetGlobalCategoriesLocale | Unset = UNSET,
    keyword: str | Unset = UNSET,
    category_version: str | Unset = UNSET,
) -> GetGlobalCategoriesResponse | None:
    """Get Global Categories

     Retrieve all available product categories, regardless of market variations.
    Product categories are updated frequently, so it's recommended to call the API in real time to
    ensure you are using the latest category data. Caching category data locally may result in using
    outdated information, leading to errors when creating global products.

    Args:
        locale (GetGlobalCategoriesLocale | Unset):
        keyword (str | Unset):
        category_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGlobalCategoriesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            locale=locale,
            keyword=keyword,
            category_version=category_version,
        )
    ).parsed
