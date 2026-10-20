from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_brands_response import GetBrandsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    category_id: str | Unset = UNSET,
    is_authorized: bool | Unset = UNSET,
    brand_name: str | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,
    category_version: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["category_id"] = category_id

    params["is_authorized"] = is_authorized

    params["brand_name"] = brand_name

    params["page_size"] = page_size

    params["page_token"] = page_token

    params["category_version"] = category_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/product/202309/brands",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetBrandsResponse | None:
    if response.status_code == 200:
        response_200 = GetBrandsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetBrandsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    category_id: str | Unset = UNSET,
    is_authorized: bool | Unset = UNSET,
    brand_name: str | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,
    category_version: str | Unset = UNSET,
) -> Response[GetBrandsResponse]:
    """Get Brands

     Retrieve brands for your shop, including the built-in brands and any custom brands created using the
    [Create Custom Brands API](650a0926f1fd3102b91bbfb0). Pass the returned brand ID when creating or
    editing a product to associate the brand with the product.
    - To check if a brand is fully authorized for use in a specific product category, specify the
    **category ID**.
    - To obtain the full list of brands that your shop can potentially use and their authorization
    status, omit the category ID. We recommend that you specify the **brand name** to narrow down the
    list of brands returned.
    **Key concept**
    Whether you can select and display a brand depends on the brand's authorization status, the
    categories authorized for the brand, and whether the brand is classified as T1 (internationally
    renowned brands that require prior brand authorization).
    **- Brand selection rules**: You can only select the following types of brands during product
    creation/editing.
       - Authorized brands which contain the desired category (`authorized_status=AUTHORIZED` and
    `brand_status=AVAILABLE`)
       - Unauthorized non-T1 brands (`authorized_status=UNAUTHORIEZD` and `is_t1_brand=false`)
    **- Brand display rules**: Note however that brands will only appear on the product display page if
    the brand is authorized (`authorized_status=AUTHORIZED`) and available in the desired category
    (`brand_status=AVAILABLE`). This means that you need to obtain brand authorization for unauthorized
    non-T1 brands before they can be displayed. Obtain brand authorization or add categories to an
    authorized brand through TikTok Shop Seller Center > Qualification Center > Brand qualification.
    **For Tokopedia sellers**: You can select and display any returned brand on Tokopedia regardless of
    these rules.

    Args:
        category_id (str | Unset):
        is_authorized (bool | Unset):
        brand_name (str | Unset):
        page_size (int):
        page_token (str | Unset):
        category_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBrandsResponse]
    """

    kwargs = _get_kwargs(
        category_id=category_id,
        is_authorized=is_authorized,
        brand_name=brand_name,
        page_size=page_size,
        page_token=page_token,
        category_version=category_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    category_id: str | Unset = UNSET,
    is_authorized: bool | Unset = UNSET,
    brand_name: str | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,
    category_version: str | Unset = UNSET,
) -> GetBrandsResponse | None:
    """Get Brands

     Retrieve brands for your shop, including the built-in brands and any custom brands created using the
    [Create Custom Brands API](650a0926f1fd3102b91bbfb0). Pass the returned brand ID when creating or
    editing a product to associate the brand with the product.
    - To check if a brand is fully authorized for use in a specific product category, specify the
    **category ID**.
    - To obtain the full list of brands that your shop can potentially use and their authorization
    status, omit the category ID. We recommend that you specify the **brand name** to narrow down the
    list of brands returned.
    **Key concept**
    Whether you can select and display a brand depends on the brand's authorization status, the
    categories authorized for the brand, and whether the brand is classified as T1 (internationally
    renowned brands that require prior brand authorization).
    **- Brand selection rules**: You can only select the following types of brands during product
    creation/editing.
       - Authorized brands which contain the desired category (`authorized_status=AUTHORIZED` and
    `brand_status=AVAILABLE`)
       - Unauthorized non-T1 brands (`authorized_status=UNAUTHORIEZD` and `is_t1_brand=false`)
    **- Brand display rules**: Note however that brands will only appear on the product display page if
    the brand is authorized (`authorized_status=AUTHORIZED`) and available in the desired category
    (`brand_status=AVAILABLE`). This means that you need to obtain brand authorization for unauthorized
    non-T1 brands before they can be displayed. Obtain brand authorization or add categories to an
    authorized brand through TikTok Shop Seller Center > Qualification Center > Brand qualification.
    **For Tokopedia sellers**: You can select and display any returned brand on Tokopedia regardless of
    these rules.

    Args:
        category_id (str | Unset):
        is_authorized (bool | Unset):
        brand_name (str | Unset):
        page_size (int):
        page_token (str | Unset):
        category_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBrandsResponse
    """

    return sync_detailed(
        client=client,
        category_id=category_id,
        is_authorized=is_authorized,
        brand_name=brand_name,
        page_size=page_size,
        page_token=page_token,
        category_version=category_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    category_id: str | Unset = UNSET,
    is_authorized: bool | Unset = UNSET,
    brand_name: str | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,
    category_version: str | Unset = UNSET,
) -> Response[GetBrandsResponse]:
    """Get Brands

     Retrieve brands for your shop, including the built-in brands and any custom brands created using the
    [Create Custom Brands API](650a0926f1fd3102b91bbfb0). Pass the returned brand ID when creating or
    editing a product to associate the brand with the product.
    - To check if a brand is fully authorized for use in a specific product category, specify the
    **category ID**.
    - To obtain the full list of brands that your shop can potentially use and their authorization
    status, omit the category ID. We recommend that you specify the **brand name** to narrow down the
    list of brands returned.
    **Key concept**
    Whether you can select and display a brand depends on the brand's authorization status, the
    categories authorized for the brand, and whether the brand is classified as T1 (internationally
    renowned brands that require prior brand authorization).
    **- Brand selection rules**: You can only select the following types of brands during product
    creation/editing.
       - Authorized brands which contain the desired category (`authorized_status=AUTHORIZED` and
    `brand_status=AVAILABLE`)
       - Unauthorized non-T1 brands (`authorized_status=UNAUTHORIEZD` and `is_t1_brand=false`)
    **- Brand display rules**: Note however that brands will only appear on the product display page if
    the brand is authorized (`authorized_status=AUTHORIZED`) and available in the desired category
    (`brand_status=AVAILABLE`). This means that you need to obtain brand authorization for unauthorized
    non-T1 brands before they can be displayed. Obtain brand authorization or add categories to an
    authorized brand through TikTok Shop Seller Center > Qualification Center > Brand qualification.
    **For Tokopedia sellers**: You can select and display any returned brand on Tokopedia regardless of
    these rules.

    Args:
        category_id (str | Unset):
        is_authorized (bool | Unset):
        brand_name (str | Unset):
        page_size (int):
        page_token (str | Unset):
        category_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBrandsResponse]
    """

    kwargs = _get_kwargs(
        category_id=category_id,
        is_authorized=is_authorized,
        brand_name=brand_name,
        page_size=page_size,
        page_token=page_token,
        category_version=category_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    category_id: str | Unset = UNSET,
    is_authorized: bool | Unset = UNSET,
    brand_name: str | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,
    category_version: str | Unset = UNSET,
) -> GetBrandsResponse | None:
    """Get Brands

     Retrieve brands for your shop, including the built-in brands and any custom brands created using the
    [Create Custom Brands API](650a0926f1fd3102b91bbfb0). Pass the returned brand ID when creating or
    editing a product to associate the brand with the product.
    - To check if a brand is fully authorized for use in a specific product category, specify the
    **category ID**.
    - To obtain the full list of brands that your shop can potentially use and their authorization
    status, omit the category ID. We recommend that you specify the **brand name** to narrow down the
    list of brands returned.
    **Key concept**
    Whether you can select and display a brand depends on the brand's authorization status, the
    categories authorized for the brand, and whether the brand is classified as T1 (internationally
    renowned brands that require prior brand authorization).
    **- Brand selection rules**: You can only select the following types of brands during product
    creation/editing.
       - Authorized brands which contain the desired category (`authorized_status=AUTHORIZED` and
    `brand_status=AVAILABLE`)
       - Unauthorized non-T1 brands (`authorized_status=UNAUTHORIEZD` and `is_t1_brand=false`)
    **- Brand display rules**: Note however that brands will only appear on the product display page if
    the brand is authorized (`authorized_status=AUTHORIZED`) and available in the desired category
    (`brand_status=AVAILABLE`). This means that you need to obtain brand authorization for unauthorized
    non-T1 brands before they can be displayed. Obtain brand authorization or add categories to an
    authorized brand through TikTok Shop Seller Center > Qualification Center > Brand qualification.
    **For Tokopedia sellers**: You can select and display any returned brand on Tokopedia regardless of
    these rules.

    Args:
        category_id (str | Unset):
        is_authorized (bool | Unset):
        brand_name (str | Unset):
        page_size (int):
        page_token (str | Unset):
        category_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBrandsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            category_id=category_id,
            is_authorized=is_authorized,
            brand_name=brand_name,
            page_size=page_size,
            page_token=page_token,
            category_version=category_version,
        )
    ).parsed
