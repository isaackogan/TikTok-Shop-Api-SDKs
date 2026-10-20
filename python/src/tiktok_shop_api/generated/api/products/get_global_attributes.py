from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_global_attributes_locale import GetGlobalAttributesLocale
from ...models.get_global_attributes_response import GetGlobalAttributesResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    category_id: str,
    *,
    locale: GetGlobalAttributesLocale | Unset = UNSET,
    category_version: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_locale: str | Unset = UNSET
    if not isinstance(locale, Unset):
        json_locale = locale.value

    params["locale"] = json_locale

    params["category_version"] = category_version


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/product/202309/categories/{category_id}/global_attributes".format(category_id=quote(str(category_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetGlobalAttributesResponse | None:
    if response.status_code == 200:
        response_200 = GetGlobalAttributesResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetGlobalAttributesResponse]:
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
    locale: GetGlobalAttributesLocale | Unset = UNSET,
    category_version: str | Unset = UNSET,

) -> Response[GetGlobalAttributesResponse]:
    """ Get Global Attributes

     Retrieve the standard built-in product and sales attributes for listing a global product in a
    particular category across the seller's markets.
    Products on TikTok Shop are grouped into categories predefined by TikTok Shop, and each category is
    associated with a standard set of product attributes and sales attributes.
    - **Sales attributes** (e.g. size, color, length) define product variants and are optional if your
    product is straightforward and has no variants.
    - **Product attributes** (e.g. manufacturer, country of origin, materials used) describe the product
    as a whole, regardless of variant. Some product attributes are mandatory based on listing policies.
    Use this API to determine the mandatory and optional attributes, including market-specific
    requirements, before listing a global product.
    **Note**: It must be a [leaf category](650a03f8f1fd3102b91b338a) that corresponds to the category
    tree type specified in the `category_version` property.

    Args:
        category_id (str):
        locale (GetGlobalAttributesLocale | Unset):
        category_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGlobalAttributesResponse]
     """


    kwargs = _get_kwargs(
        category_id=category_id,
locale=locale,
category_version=category_version,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    category_id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: GetGlobalAttributesLocale | Unset = UNSET,
    category_version: str | Unset = UNSET,

) -> GetGlobalAttributesResponse | None:
    """ Get Global Attributes

     Retrieve the standard built-in product and sales attributes for listing a global product in a
    particular category across the seller's markets.
    Products on TikTok Shop are grouped into categories predefined by TikTok Shop, and each category is
    associated with a standard set of product attributes and sales attributes.
    - **Sales attributes** (e.g. size, color, length) define product variants and are optional if your
    product is straightforward and has no variants.
    - **Product attributes** (e.g. manufacturer, country of origin, materials used) describe the product
    as a whole, regardless of variant. Some product attributes are mandatory based on listing policies.
    Use this API to determine the mandatory and optional attributes, including market-specific
    requirements, before listing a global product.
    **Note**: It must be a [leaf category](650a03f8f1fd3102b91b338a) that corresponds to the category
    tree type specified in the `category_version` property.

    Args:
        category_id (str):
        locale (GetGlobalAttributesLocale | Unset):
        category_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGlobalAttributesResponse
     """


    return sync_detailed(
        category_id=category_id,
client=client,
locale=locale,
category_version=category_version,

    ).parsed

async def asyncio_detailed(
    category_id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: GetGlobalAttributesLocale | Unset = UNSET,
    category_version: str | Unset = UNSET,

) -> Response[GetGlobalAttributesResponse]:
    """ Get Global Attributes

     Retrieve the standard built-in product and sales attributes for listing a global product in a
    particular category across the seller's markets.
    Products on TikTok Shop are grouped into categories predefined by TikTok Shop, and each category is
    associated with a standard set of product attributes and sales attributes.
    - **Sales attributes** (e.g. size, color, length) define product variants and are optional if your
    product is straightforward and has no variants.
    - **Product attributes** (e.g. manufacturer, country of origin, materials used) describe the product
    as a whole, regardless of variant. Some product attributes are mandatory based on listing policies.
    Use this API to determine the mandatory and optional attributes, including market-specific
    requirements, before listing a global product.
    **Note**: It must be a [leaf category](650a03f8f1fd3102b91b338a) that corresponds to the category
    tree type specified in the `category_version` property.

    Args:
        category_id (str):
        locale (GetGlobalAttributesLocale | Unset):
        category_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGlobalAttributesResponse]
     """


    kwargs = _get_kwargs(
        category_id=category_id,
locale=locale,
category_version=category_version,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    category_id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: GetGlobalAttributesLocale | Unset = UNSET,
    category_version: str | Unset = UNSET,

) -> GetGlobalAttributesResponse | None:
    """ Get Global Attributes

     Retrieve the standard built-in product and sales attributes for listing a global product in a
    particular category across the seller's markets.
    Products on TikTok Shop are grouped into categories predefined by TikTok Shop, and each category is
    associated with a standard set of product attributes and sales attributes.
    - **Sales attributes** (e.g. size, color, length) define product variants and are optional if your
    product is straightforward and has no variants.
    - **Product attributes** (e.g. manufacturer, country of origin, materials used) describe the product
    as a whole, regardless of variant. Some product attributes are mandatory based on listing policies.
    Use this API to determine the mandatory and optional attributes, including market-specific
    requirements, before listing a global product.
    **Note**: It must be a [leaf category](650a03f8f1fd3102b91b338a) that corresponds to the category
    tree type specified in the `category_version` property.

    Args:
        category_id (str):
        locale (GetGlobalAttributesLocale | Unset):
        category_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGlobalAttributesResponse
     """


    return (await asyncio_detailed(
        category_id=category_id,
client=client,
locale=locale,
category_version=category_version,

    )).parsed
