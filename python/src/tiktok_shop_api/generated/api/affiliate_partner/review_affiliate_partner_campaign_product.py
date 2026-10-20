from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.review_affiliate_partner_campaign_product_request import ReviewAffiliatePartnerCampaignProductRequest
from ...models.review_affiliate_partner_campaign_product_response import ReviewAffiliatePartnerCampaignProductResponse
from ...types import UNSET, Response


def _get_kwargs(
    campaign_id: str,
    product_id: str,
    *,
    body: ReviewAffiliatePartnerCampaignProductRequest,
    category_asset_cipher: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["category_asset_cipher"] = category_asset_cipher

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_partner/202405/campaigns/{campaign_id}/products/{product_id}/review".format(
            campaign_id=quote(str(campaign_id), safe=""),
            product_id=quote(str(product_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ReviewAffiliatePartnerCampaignProductResponse | None:
    if response.status_code == 200:
        response_200 = ReviewAffiliatePartnerCampaignProductResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ReviewAffiliatePartnerCampaignProductResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    campaign_id: str,
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ReviewAffiliatePartnerCampaignProductRequest,
    category_asset_cipher: str,
) -> Response[ReviewAffiliatePartnerCampaignProductResponse]:
    """Review Affiliate Partner Campaign Product

     Use this API as a TikTok Affiliate Partner to approve or reject a product submitted by a seller to a
    campaign. The product must be in a pending state.

    Args:
        campaign_id (str):
        product_id (str):
        category_asset_cipher (str):
        body (ReviewAffiliatePartnerCampaignProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReviewAffiliatePartnerCampaignProductResponse]
    """

    kwargs = _get_kwargs(
        campaign_id=campaign_id,
        product_id=product_id,
        body=body,
        category_asset_cipher=category_asset_cipher,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    campaign_id: str,
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ReviewAffiliatePartnerCampaignProductRequest,
    category_asset_cipher: str,
) -> ReviewAffiliatePartnerCampaignProductResponse | None:
    """Review Affiliate Partner Campaign Product

     Use this API as a TikTok Affiliate Partner to approve or reject a product submitted by a seller to a
    campaign. The product must be in a pending state.

    Args:
        campaign_id (str):
        product_id (str):
        category_asset_cipher (str):
        body (ReviewAffiliatePartnerCampaignProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReviewAffiliatePartnerCampaignProductResponse
    """

    return sync_detailed(
        campaign_id=campaign_id,
        product_id=product_id,
        client=client,
        body=body,
        category_asset_cipher=category_asset_cipher,
    ).parsed


async def asyncio_detailed(
    campaign_id: str,
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ReviewAffiliatePartnerCampaignProductRequest,
    category_asset_cipher: str,
) -> Response[ReviewAffiliatePartnerCampaignProductResponse]:
    """Review Affiliate Partner Campaign Product

     Use this API as a TikTok Affiliate Partner to approve or reject a product submitted by a seller to a
    campaign. The product must be in a pending state.

    Args:
        campaign_id (str):
        product_id (str):
        category_asset_cipher (str):
        body (ReviewAffiliatePartnerCampaignProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReviewAffiliatePartnerCampaignProductResponse]
    """

    kwargs = _get_kwargs(
        campaign_id=campaign_id,
        product_id=product_id,
        body=body,
        category_asset_cipher=category_asset_cipher,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    campaign_id: str,
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ReviewAffiliatePartnerCampaignProductRequest,
    category_asset_cipher: str,
) -> ReviewAffiliatePartnerCampaignProductResponse | None:
    """Review Affiliate Partner Campaign Product

     Use this API as a TikTok Affiliate Partner to approve or reject a product submitted by a seller to a
    campaign. The product must be in a pending state.

    Args:
        campaign_id (str):
        product_id (str):
        category_asset_cipher (str):
        body (ReviewAffiliatePartnerCampaignProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReviewAffiliatePartnerCampaignProductResponse
    """

    return (
        await asyncio_detailed(
            campaign_id=campaign_id,
            product_id=product_id,
            client=client,
            body=body,
            category_asset_cipher=category_asset_cipher,
        )
    ).parsed
