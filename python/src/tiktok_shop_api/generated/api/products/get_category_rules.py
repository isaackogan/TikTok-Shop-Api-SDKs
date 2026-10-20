from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_category_rules_locale import GetCategoryRulesLocale
from ...models.get_category_rules_response import GetCategoryRulesResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    category_id: str,
    *,
    category_version: str | Unset = UNSET,
    locale: GetCategoryRulesLocale | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["category_version"] = category_version

    json_locale: str | Unset = UNSET
    if not isinstance(locale, Unset):
        json_locale = locale.value

    params["locale"] = json_locale


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/product/202309/categories/{category_id}/rules".format(category_id=quote(str(category_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetCategoryRulesResponse | None:
    if response.status_code == 200:
        response_200 = GetCategoryRulesResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetCategoryRulesResponse]:
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
    category_version: str | Unset = UNSET,
    locale: GetCategoryRulesLocale | Unset = UNSET,

) -> Response[GetCategoryRulesResponse]:
    """ Get Category Rules

     Retrieve the additional requirements (beyond mandatory product attributes) for listing a product in
    a particular category based on your shop's location. Requirements may include product
    certifications, size charts, dimensions and more.
    Use this API to determine the supporting information that you must prepare before listing a product.
    **Note**: It must be a [leaf category](6509c89d0fcef602bf1acd9b) that corresponds to the category
    tree type specified in the `category_version` property.

    Args:
        category_id (str):
        category_version (str | Unset):
        locale (GetCategoryRulesLocale | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCategoryRulesResponse]
     """


    kwargs = _get_kwargs(
        category_id=category_id,
category_version=category_version,
locale=locale,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    category_id: str,
    *,
    client: AuthenticatedClient | Client,
    category_version: str | Unset = UNSET,
    locale: GetCategoryRulesLocale | Unset = UNSET,

) -> GetCategoryRulesResponse | None:
    """ Get Category Rules

     Retrieve the additional requirements (beyond mandatory product attributes) for listing a product in
    a particular category based on your shop's location. Requirements may include product
    certifications, size charts, dimensions and more.
    Use this API to determine the supporting information that you must prepare before listing a product.
    **Note**: It must be a [leaf category](6509c89d0fcef602bf1acd9b) that corresponds to the category
    tree type specified in the `category_version` property.

    Args:
        category_id (str):
        category_version (str | Unset):
        locale (GetCategoryRulesLocale | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCategoryRulesResponse
     """


    return sync_detailed(
        category_id=category_id,
client=client,
category_version=category_version,
locale=locale,

    ).parsed

async def asyncio_detailed(
    category_id: str,
    *,
    client: AuthenticatedClient | Client,
    category_version: str | Unset = UNSET,
    locale: GetCategoryRulesLocale | Unset = UNSET,

) -> Response[GetCategoryRulesResponse]:
    """ Get Category Rules

     Retrieve the additional requirements (beyond mandatory product attributes) for listing a product in
    a particular category based on your shop's location. Requirements may include product
    certifications, size charts, dimensions and more.
    Use this API to determine the supporting information that you must prepare before listing a product.
    **Note**: It must be a [leaf category](6509c89d0fcef602bf1acd9b) that corresponds to the category
    tree type specified in the `category_version` property.

    Args:
        category_id (str):
        category_version (str | Unset):
        locale (GetCategoryRulesLocale | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCategoryRulesResponse]
     """


    kwargs = _get_kwargs(
        category_id=category_id,
category_version=category_version,
locale=locale,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    category_id: str,
    *,
    client: AuthenticatedClient | Client,
    category_version: str | Unset = UNSET,
    locale: GetCategoryRulesLocale | Unset = UNSET,

) -> GetCategoryRulesResponse | None:
    """ Get Category Rules

     Retrieve the additional requirements (beyond mandatory product attributes) for listing a product in
    a particular category based on your shop's location. Requirements may include product
    certifications, size charts, dimensions and more.
    Use this API to determine the supporting information that you must prepare before listing a product.
    **Note**: It must be a [leaf category](6509c89d0fcef602bf1acd9b) that corresponds to the category
    tree type specified in the `category_version` property.

    Args:
        category_id (str):
        category_version (str | Unset):
        locale (GetCategoryRulesLocale | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCategoryRulesResponse
     """


    return (await asyncio_detailed(
        category_id=category_id,
client=client,
category_version=category_version,
locale=locale,

    )).parsed
