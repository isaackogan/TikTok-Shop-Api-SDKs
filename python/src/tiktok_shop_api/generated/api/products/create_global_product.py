from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_global_product_request import CreateGlobalProductRequest
from ...models.create_global_product_response import CreateGlobalProductResponse
from typing import cast



def _get_kwargs(
    *,
    body: CreateGlobalProductRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202309/global_products",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateGlobalProductResponse | None:
    if response.status_code == 200:
        response_200 = CreateGlobalProductResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateGlobalProductResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateGlobalProductRequest,

) -> Response[CreateGlobalProductResponse]:
    """ Create Global Product

     Create global products to be sold in one or multiple shops outside of the seller's base country.
    You can only create global products in `AVAILABLE` product categories. For other categories, contact
    your account manager for assistance. After product creation, use the [Publish Global Product
    API](https://partner.tiktokshop.com/docv2/page/650a64d6defece02be678fd6) to publish and translate
    the product in the desired markets.
    **Key concept**: Global products are products created by cross-border sellers to be sold in shops
    outside of their base country. With global products, cross-border sellers operating across multiple
    markets can avoid creating the same product for each shop individually. Instead, they just need to
    create a single global product, which can be published and synced to all their shops, simplifying
    product management across markets.
    **Note**:
    - This API is applicable only for intra-EU sellers and global sellers. To create and list local
    products intended for sale exclusively in local shops, use the [Create Product
    API](https://partner.tiktokshop.com/docv2/page/6502fc8da57708028b42b18a) instead.
    - There may be a limit to the number of products you can list per day. We recommend prioritizing the
    creation of key products first to ensure they get published. You can find your listing limit on the
    Seller Center homepage.
    - The language used in the product content must align with the target market's language (e.g. don't
    use Chinese), otherwise the listing will fail or be rejected.

    Args:
        body (CreateGlobalProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateGlobalProductResponse]
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
    body: CreateGlobalProductRequest,

) -> CreateGlobalProductResponse | None:
    """ Create Global Product

     Create global products to be sold in one or multiple shops outside of the seller's base country.
    You can only create global products in `AVAILABLE` product categories. For other categories, contact
    your account manager for assistance. After product creation, use the [Publish Global Product
    API](https://partner.tiktokshop.com/docv2/page/650a64d6defece02be678fd6) to publish and translate
    the product in the desired markets.
    **Key concept**: Global products are products created by cross-border sellers to be sold in shops
    outside of their base country. With global products, cross-border sellers operating across multiple
    markets can avoid creating the same product for each shop individually. Instead, they just need to
    create a single global product, which can be published and synced to all their shops, simplifying
    product management across markets.
    **Note**:
    - This API is applicable only for intra-EU sellers and global sellers. To create and list local
    products intended for sale exclusively in local shops, use the [Create Product
    API](https://partner.tiktokshop.com/docv2/page/6502fc8da57708028b42b18a) instead.
    - There may be a limit to the number of products you can list per day. We recommend prioritizing the
    creation of key products first to ensure they get published. You can find your listing limit on the
    Seller Center homepage.
    - The language used in the product content must align with the target market's language (e.g. don't
    use Chinese), otherwise the listing will fail or be rejected.

    Args:
        body (CreateGlobalProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateGlobalProductResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateGlobalProductRequest,

) -> Response[CreateGlobalProductResponse]:
    """ Create Global Product

     Create global products to be sold in one or multiple shops outside of the seller's base country.
    You can only create global products in `AVAILABLE` product categories. For other categories, contact
    your account manager for assistance. After product creation, use the [Publish Global Product
    API](https://partner.tiktokshop.com/docv2/page/650a64d6defece02be678fd6) to publish and translate
    the product in the desired markets.
    **Key concept**: Global products are products created by cross-border sellers to be sold in shops
    outside of their base country. With global products, cross-border sellers operating across multiple
    markets can avoid creating the same product for each shop individually. Instead, they just need to
    create a single global product, which can be published and synced to all their shops, simplifying
    product management across markets.
    **Note**:
    - This API is applicable only for intra-EU sellers and global sellers. To create and list local
    products intended for sale exclusively in local shops, use the [Create Product
    API](https://partner.tiktokshop.com/docv2/page/6502fc8da57708028b42b18a) instead.
    - There may be a limit to the number of products you can list per day. We recommend prioritizing the
    creation of key products first to ensure they get published. You can find your listing limit on the
    Seller Center homepage.
    - The language used in the product content must align with the target market's language (e.g. don't
    use Chinese), otherwise the listing will fail or be rejected.

    Args:
        body (CreateGlobalProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateGlobalProductResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateGlobalProductRequest,

) -> CreateGlobalProductResponse | None:
    """ Create Global Product

     Create global products to be sold in one or multiple shops outside of the seller's base country.
    You can only create global products in `AVAILABLE` product categories. For other categories, contact
    your account manager for assistance. After product creation, use the [Publish Global Product
    API](https://partner.tiktokshop.com/docv2/page/650a64d6defece02be678fd6) to publish and translate
    the product in the desired markets.
    **Key concept**: Global products are products created by cross-border sellers to be sold in shops
    outside of their base country. With global products, cross-border sellers operating across multiple
    markets can avoid creating the same product for each shop individually. Instead, they just need to
    create a single global product, which can be published and synced to all their shops, simplifying
    product management across markets.
    **Note**:
    - This API is applicable only for intra-EU sellers and global sellers. To create and list local
    products intended for sale exclusively in local shops, use the [Create Product
    API](https://partner.tiktokshop.com/docv2/page/6502fc8da57708028b42b18a) instead.
    - There may be a limit to the number of products you can list per day. We recommend prioritizing the
    creation of key products first to ensure they get published. You can find your listing limit on the
    Seller Center homepage.
    - The language used in the product content must align with the target market's language (e.g. don't
    use Chinese), otherwise the listing will fail or be rejected.

    Args:
        body (CreateGlobalProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateGlobalProductResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
