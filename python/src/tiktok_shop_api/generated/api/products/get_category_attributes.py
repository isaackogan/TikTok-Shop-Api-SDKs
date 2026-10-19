from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_category_attributes_locale import GetCategoryAttributesLocale
from ...models.get_category_attributes_response import GetCategoryAttributesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    category_id: str,
    *,
    locale: GetCategoryAttributesLocale | Unset = UNSET,
    category_version: str | Unset = UNSET,
    is_live_quick: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_locale: str | Unset = UNSET
    if not isinstance(locale, Unset):
        json_locale = locale.value

    params["locale"] = json_locale

    params["category_version"] = category_version

    params["is_live_quick"] = is_live_quick

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/product/202309/categories/{category_id}/attributes".format(
            category_id=quote(str(category_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetCategoryAttributesResponse | None:
    if response.status_code == 200:
        response_200 = GetCategoryAttributesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetCategoryAttributesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    category_id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: GetCategoryAttributesLocale | Unset = UNSET,
    category_version: str | Unset = UNSET,
    is_live_quick: bool | Unset = UNSET,
) -> Response[GetCategoryAttributesResponse]:
    """Get Category Attributes

     Retrieve the standard built-in product and sales attributes for listing a product in a particular
    category based on your shop's location.
    Products on TikTok Shop are grouped into categories predefined by TikTok Shop, and each category is
    associated with a standard set of product attributes and sales attributes.
    - **Sales attributes** (e.g. size, color, length) define product variants and are optional if your
    product is straightforward and has no variants.
    - **Product attributes** (e.g. manufacturer, country of origin, materials used) describe the product
    as a whole, regardless of variant. Some product attributes are mandatory based on listing policies.
    Use this API to determine the mandatory and optional attributes before listing a product.
    **Note**: It must be a [leaf category](6509c89d0fcef602bf1acd9b) that corresponds to the category
    tree type specified in the `category_version` property.

    Args:
        category_id (str):
        locale (GetCategoryAttributesLocale | Unset):
        category_version (str | Unset):
        is_live_quick (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCategoryAttributesResponse]
    """

    kwargs = _get_kwargs(
        category_id=category_id,
        locale=locale,
        category_version=category_version,
        is_live_quick=is_live_quick,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    category_id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: GetCategoryAttributesLocale | Unset = UNSET,
    category_version: str | Unset = UNSET,
    is_live_quick: bool | Unset = UNSET,
) -> GetCategoryAttributesResponse | None:
    """Get Category Attributes

     Retrieve the standard built-in product and sales attributes for listing a product in a particular
    category based on your shop's location.
    Products on TikTok Shop are grouped into categories predefined by TikTok Shop, and each category is
    associated with a standard set of product attributes and sales attributes.
    - **Sales attributes** (e.g. size, color, length) define product variants and are optional if your
    product is straightforward and has no variants.
    - **Product attributes** (e.g. manufacturer, country of origin, materials used) describe the product
    as a whole, regardless of variant. Some product attributes are mandatory based on listing policies.
    Use this API to determine the mandatory and optional attributes before listing a product.
    **Note**: It must be a [leaf category](6509c89d0fcef602bf1acd9b) that corresponds to the category
    tree type specified in the `category_version` property.

    Args:
        category_id (str):
        locale (GetCategoryAttributesLocale | Unset):
        category_version (str | Unset):
        is_live_quick (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCategoryAttributesResponse
    """

    return sync_detailed(
        category_id=category_id,
        client=client,
        locale=locale,
        category_version=category_version,
        is_live_quick=is_live_quick,
    ).parsed


async def asyncio_detailed(
    category_id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: GetCategoryAttributesLocale | Unset = UNSET,
    category_version: str | Unset = UNSET,
    is_live_quick: bool | Unset = UNSET,
) -> Response[GetCategoryAttributesResponse]:
    """Get Category Attributes

     Retrieve the standard built-in product and sales attributes for listing a product in a particular
    category based on your shop's location.
    Products on TikTok Shop are grouped into categories predefined by TikTok Shop, and each category is
    associated with a standard set of product attributes and sales attributes.
    - **Sales attributes** (e.g. size, color, length) define product variants and are optional if your
    product is straightforward and has no variants.
    - **Product attributes** (e.g. manufacturer, country of origin, materials used) describe the product
    as a whole, regardless of variant. Some product attributes are mandatory based on listing policies.
    Use this API to determine the mandatory and optional attributes before listing a product.
    **Note**: It must be a [leaf category](6509c89d0fcef602bf1acd9b) that corresponds to the category
    tree type specified in the `category_version` property.

    Args:
        category_id (str):
        locale (GetCategoryAttributesLocale | Unset):
        category_version (str | Unset):
        is_live_quick (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCategoryAttributesResponse]
    """

    kwargs = _get_kwargs(
        category_id=category_id,
        locale=locale,
        category_version=category_version,
        is_live_quick=is_live_quick,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    category_id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: GetCategoryAttributesLocale | Unset = UNSET,
    category_version: str | Unset = UNSET,
    is_live_quick: bool | Unset = UNSET,
) -> GetCategoryAttributesResponse | None:
    """Get Category Attributes

     Retrieve the standard built-in product and sales attributes for listing a product in a particular
    category based on your shop's location.
    Products on TikTok Shop are grouped into categories predefined by TikTok Shop, and each category is
    associated with a standard set of product attributes and sales attributes.
    - **Sales attributes** (e.g. size, color, length) define product variants and are optional if your
    product is straightforward and has no variants.
    - **Product attributes** (e.g. manufacturer, country of origin, materials used) describe the product
    as a whole, regardless of variant. Some product attributes are mandatory based on listing policies.
    Use this API to determine the mandatory and optional attributes before listing a product.
    **Note**: It must be a [leaf category](6509c89d0fcef602bf1acd9b) that corresponds to the category
    tree type specified in the `category_version` property.

    Args:
        category_id (str):
        locale (GetCategoryAttributesLocale | Unset):
        category_version (str | Unset):
        is_live_quick (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCategoryAttributesResponse
    """

    return (
        await asyncio_detailed(
            category_id=category_id,
            client=client,
            locale=locale,
            category_version=category_version,
            is_live_quick=is_live_quick,
        )
    ).parsed
