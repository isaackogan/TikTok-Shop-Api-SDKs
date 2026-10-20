from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.generate_affiliate_product_promotion_link_request import GenerateAffiliateProductPromotionLinkRequest
from ...models.generate_affiliate_product_promotion_link_response import GenerateAffiliateProductPromotionLinkResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    product_id: str,
    *,
    body: GenerateAffiliateProductPromotionLinkRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_seller/202405/products/{product_id}/promotion_link/generate".format(
            product_id=quote(str(product_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GenerateAffiliateProductPromotionLinkResponse | None:
    if response.status_code == 200:
        response_200 = GenerateAffiliateProductPromotionLinkResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GenerateAffiliateProductPromotionLinkResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GenerateAffiliateProductPromotionLinkRequest | Unset = UNSET,
) -> Response[GenerateAffiliateProductPromotionLinkResponse]:
    """Generate Affiliate Product Promotion Link

     Partner developers acting on behalf of sellers use this API to generate an affiliate-exclusive
    promotion link for a specific open-collaboration product, identified by `product_id`, in the TikTok
    Shop Affiliate Product Marketplace.

    The partner developer can distribute the generated link to creators. A creator can use the link to
    add the product to the creator's showcase. If a creator adds the product to a showcase through this
    link, subsequent consumer purchases can be attributed to the partner.

    Args:
        product_id (str):
        body (GenerateAffiliateProductPromotionLinkRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenerateAffiliateProductPromotionLinkResponse]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GenerateAffiliateProductPromotionLinkRequest | Unset = UNSET,
) -> GenerateAffiliateProductPromotionLinkResponse | None:
    """Generate Affiliate Product Promotion Link

     Partner developers acting on behalf of sellers use this API to generate an affiliate-exclusive
    promotion link for a specific open-collaboration product, identified by `product_id`, in the TikTok
    Shop Affiliate Product Marketplace.

    The partner developer can distribute the generated link to creators. A creator can use the link to
    add the product to the creator's showcase. If a creator adds the product to a showcase through this
    link, subsequent consumer purchases can be attributed to the partner.

    Args:
        product_id (str):
        body (GenerateAffiliateProductPromotionLinkRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenerateAffiliateProductPromotionLinkResponse
    """

    return sync_detailed(
        product_id=product_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GenerateAffiliateProductPromotionLinkRequest | Unset = UNSET,
) -> Response[GenerateAffiliateProductPromotionLinkResponse]:
    """Generate Affiliate Product Promotion Link

     Partner developers acting on behalf of sellers use this API to generate an affiliate-exclusive
    promotion link for a specific open-collaboration product, identified by `product_id`, in the TikTok
    Shop Affiliate Product Marketplace.

    The partner developer can distribute the generated link to creators. A creator can use the link to
    add the product to the creator's showcase. If a creator adds the product to a showcase through this
    link, subsequent consumer purchases can be attributed to the partner.

    Args:
        product_id (str):
        body (GenerateAffiliateProductPromotionLinkRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenerateAffiliateProductPromotionLinkResponse]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GenerateAffiliateProductPromotionLinkRequest | Unset = UNSET,
) -> GenerateAffiliateProductPromotionLinkResponse | None:
    """Generate Affiliate Product Promotion Link

     Partner developers acting on behalf of sellers use this API to generate an affiliate-exclusive
    promotion link for a specific open-collaboration product, identified by `product_id`, in the TikTok
    Shop Affiliate Product Marketplace.

    The partner developer can distribute the generated link to creators. A creator can use the link to
    add the product to the creator's showcase. If a creator adds the product to a showcase through this
    link, subsequent consumer purchases can be attributed to the partner.

    Args:
        product_id (str):
        body (GenerateAffiliateProductPromotionLinkRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenerateAffiliateProductPromotionLinkResponse
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            client=client,
            body=body,
        )
    ).parsed
