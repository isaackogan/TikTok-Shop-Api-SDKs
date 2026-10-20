from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_affiliate_partner_campaign_product_list_response import (
    GetAffiliatePartnerCampaignProductListResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    campaign_id: str,
    *,
    category_asset_cipher: str,
    page_size: int,
    page_token: str | Unset = UNSET,
    review_status: str | Unset = UNSET,
    product_name: str | Unset = UNSET,
    product_id: str | Unset = UNSET,
    shop_name: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["category_asset_cipher"] = category_asset_cipher

    params["page_size"] = page_size

    params["page_token"] = page_token

    params["review_status"] = review_status

    params["product_name"] = product_name

    params["product_id"] = product_id

    params["shop_name"] = shop_name

    params["category_id"] = category_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/affiliate_partner/202405/campaigns/{campaign_id}/products".format(
            campaign_id=quote(str(campaign_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetAffiliatePartnerCampaignProductListResponse | None:
    if response.status_code == 200:
        response_200 = GetAffiliatePartnerCampaignProductListResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetAffiliatePartnerCampaignProductListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    campaign_id: str,
    *,
    client: AuthenticatedClient | Client,
    category_asset_cipher: str,
    page_size: int,
    page_token: str | Unset = UNSET,
    review_status: str | Unset = UNSET,
    product_name: str | Unset = UNSET,
    product_id: str | Unset = UNSET,
    shop_name: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
) -> Response[GetAffiliatePartnerCampaignProductListResponse]:
    """Get Affiliate Partner Campaign Product List

     This API offers the ability to list products submitted by sellers in an Affiliate Partner campaign.

    Args:
        campaign_id (str):
        category_asset_cipher (str):
        page_size (int):
        page_token (str | Unset):
        review_status (str | Unset):
        product_name (str | Unset):
        product_id (str | Unset):
        shop_name (str | Unset):
        category_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAffiliatePartnerCampaignProductListResponse]
    """

    kwargs = _get_kwargs(
        campaign_id=campaign_id,
        category_asset_cipher=category_asset_cipher,
        page_size=page_size,
        page_token=page_token,
        review_status=review_status,
        product_name=product_name,
        product_id=product_id,
        shop_name=shop_name,
        category_id=category_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    campaign_id: str,
    *,
    client: AuthenticatedClient | Client,
    category_asset_cipher: str,
    page_size: int,
    page_token: str | Unset = UNSET,
    review_status: str | Unset = UNSET,
    product_name: str | Unset = UNSET,
    product_id: str | Unset = UNSET,
    shop_name: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
) -> GetAffiliatePartnerCampaignProductListResponse | None:
    """Get Affiliate Partner Campaign Product List

     This API offers the ability to list products submitted by sellers in an Affiliate Partner campaign.

    Args:
        campaign_id (str):
        category_asset_cipher (str):
        page_size (int):
        page_token (str | Unset):
        review_status (str | Unset):
        product_name (str | Unset):
        product_id (str | Unset):
        shop_name (str | Unset):
        category_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAffiliatePartnerCampaignProductListResponse
    """

    return sync_detailed(
        campaign_id=campaign_id,
        client=client,
        category_asset_cipher=category_asset_cipher,
        page_size=page_size,
        page_token=page_token,
        review_status=review_status,
        product_name=product_name,
        product_id=product_id,
        shop_name=shop_name,
        category_id=category_id,
    ).parsed


async def asyncio_detailed(
    campaign_id: str,
    *,
    client: AuthenticatedClient | Client,
    category_asset_cipher: str,
    page_size: int,
    page_token: str | Unset = UNSET,
    review_status: str | Unset = UNSET,
    product_name: str | Unset = UNSET,
    product_id: str | Unset = UNSET,
    shop_name: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
) -> Response[GetAffiliatePartnerCampaignProductListResponse]:
    """Get Affiliate Partner Campaign Product List

     This API offers the ability to list products submitted by sellers in an Affiliate Partner campaign.

    Args:
        campaign_id (str):
        category_asset_cipher (str):
        page_size (int):
        page_token (str | Unset):
        review_status (str | Unset):
        product_name (str | Unset):
        product_id (str | Unset):
        shop_name (str | Unset):
        category_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAffiliatePartnerCampaignProductListResponse]
    """

    kwargs = _get_kwargs(
        campaign_id=campaign_id,
        category_asset_cipher=category_asset_cipher,
        page_size=page_size,
        page_token=page_token,
        review_status=review_status,
        product_name=product_name,
        product_id=product_id,
        shop_name=shop_name,
        category_id=category_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    campaign_id: str,
    *,
    client: AuthenticatedClient | Client,
    category_asset_cipher: str,
    page_size: int,
    page_token: str | Unset = UNSET,
    review_status: str | Unset = UNSET,
    product_name: str | Unset = UNSET,
    product_id: str | Unset = UNSET,
    shop_name: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
) -> GetAffiliatePartnerCampaignProductListResponse | None:
    """Get Affiliate Partner Campaign Product List

     This API offers the ability to list products submitted by sellers in an Affiliate Partner campaign.

    Args:
        campaign_id (str):
        category_asset_cipher (str):
        page_size (int):
        page_token (str | Unset):
        review_status (str | Unset):
        product_name (str | Unset):
        product_id (str | Unset):
        shop_name (str | Unset):
        category_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAffiliatePartnerCampaignProductListResponse
    """

    return (
        await asyncio_detailed(
            campaign_id=campaign_id,
            client=client,
            category_asset_cipher=category_asset_cipher,
            page_size=page_size,
            page_token=page_token,
            review_status=review_status,
            product_name=product_name,
            product_id=product_id,
            shop_name=shop_name,
            category_id=category_id,
        )
    ).parsed
