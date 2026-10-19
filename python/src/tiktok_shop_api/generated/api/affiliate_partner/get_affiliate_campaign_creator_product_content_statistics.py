from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_affiliate_campaign_creator_product_content_statistics_response import (
    GetAffiliateCampaignCreatorProductContentStatisticsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    campaign_id: str,
    product_id: str,
    creator_temp_id: str,
    *,
    affiliate_product_id: str,
    content_type: str | Unset = UNSET,
    category_asset_cipher: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["affiliate_product_id"] = affiliate_product_id

    params["content_type"] = content_type

    params["category_asset_cipher"] = category_asset_cipher

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/affiliate_partner/202508/campaigns/{campaign_id}/products/{product_id}/creator/{creator_temp_id}/content/statistics".format(
            campaign_id=quote(str(campaign_id), safe=""),
            product_id=quote(str(product_id), safe=""),
            creator_temp_id=quote(str(creator_temp_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetAffiliateCampaignCreatorProductContentStatisticsResponse | None:
    if response.status_code == 200:
        response_200 = GetAffiliateCampaignCreatorProductContentStatisticsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetAffiliateCampaignCreatorProductContentStatisticsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    campaign_id: str,
    product_id: str,
    creator_temp_id: str,
    *,
    client: AuthenticatedClient | Client,
    affiliate_product_id: str,
    content_type: str | Unset = UNSET,
    category_asset_cipher: str,
) -> Response[GetAffiliateCampaignCreatorProductContentStatisticsResponse]:
    """Get Affiliate Campaign Creator Product Content Statistics

     Retrieves performance statistics for a creator's video or live-room content associated with an
    affiliate campaign product.

    Args:
        campaign_id (str):
        product_id (str):
        creator_temp_id (str):
        affiliate_product_id (str):
        content_type (str | Unset):
        category_asset_cipher (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAffiliateCampaignCreatorProductContentStatisticsResponse]
    """

    kwargs = _get_kwargs(
        campaign_id=campaign_id,
        product_id=product_id,
        creator_temp_id=creator_temp_id,
        affiliate_product_id=affiliate_product_id,
        content_type=content_type,
        category_asset_cipher=category_asset_cipher,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    campaign_id: str,
    product_id: str,
    creator_temp_id: str,
    *,
    client: AuthenticatedClient | Client,
    affiliate_product_id: str,
    content_type: str | Unset = UNSET,
    category_asset_cipher: str,
) -> GetAffiliateCampaignCreatorProductContentStatisticsResponse | None:
    """Get Affiliate Campaign Creator Product Content Statistics

     Retrieves performance statistics for a creator's video or live-room content associated with an
    affiliate campaign product.

    Args:
        campaign_id (str):
        product_id (str):
        creator_temp_id (str):
        affiliate_product_id (str):
        content_type (str | Unset):
        category_asset_cipher (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAffiliateCampaignCreatorProductContentStatisticsResponse
    """

    return sync_detailed(
        campaign_id=campaign_id,
        product_id=product_id,
        creator_temp_id=creator_temp_id,
        client=client,
        affiliate_product_id=affiliate_product_id,
        content_type=content_type,
        category_asset_cipher=category_asset_cipher,
    ).parsed


async def asyncio_detailed(
    campaign_id: str,
    product_id: str,
    creator_temp_id: str,
    *,
    client: AuthenticatedClient | Client,
    affiliate_product_id: str,
    content_type: str | Unset = UNSET,
    category_asset_cipher: str,
) -> Response[GetAffiliateCampaignCreatorProductContentStatisticsResponse]:
    """Get Affiliate Campaign Creator Product Content Statistics

     Retrieves performance statistics for a creator's video or live-room content associated with an
    affiliate campaign product.

    Args:
        campaign_id (str):
        product_id (str):
        creator_temp_id (str):
        affiliate_product_id (str):
        content_type (str | Unset):
        category_asset_cipher (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAffiliateCampaignCreatorProductContentStatisticsResponse]
    """

    kwargs = _get_kwargs(
        campaign_id=campaign_id,
        product_id=product_id,
        creator_temp_id=creator_temp_id,
        affiliate_product_id=affiliate_product_id,
        content_type=content_type,
        category_asset_cipher=category_asset_cipher,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    campaign_id: str,
    product_id: str,
    creator_temp_id: str,
    *,
    client: AuthenticatedClient | Client,
    affiliate_product_id: str,
    content_type: str | Unset = UNSET,
    category_asset_cipher: str,
) -> GetAffiliateCampaignCreatorProductContentStatisticsResponse | None:
    """Get Affiliate Campaign Creator Product Content Statistics

     Retrieves performance statistics for a creator's video or live-room content associated with an
    affiliate campaign product.

    Args:
        campaign_id (str):
        product_id (str):
        creator_temp_id (str):
        affiliate_product_id (str):
        content_type (str | Unset):
        category_asset_cipher (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAffiliateCampaignCreatorProductContentStatisticsResponse
    """

    return (
        await asyncio_detailed(
            campaign_id=campaign_id,
            product_id=product_id,
            creator_temp_id=creator_temp_id,
            client=client,
            affiliate_product_id=affiliate_product_id,
            content_type=content_type,
            category_asset_cipher=category_asset_cipher,
        )
    ).parsed
