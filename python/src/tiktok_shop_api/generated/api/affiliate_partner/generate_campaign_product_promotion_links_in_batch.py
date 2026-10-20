from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.generate_campaign_product_promotion_links_in_batch_request import GenerateCampaignProductPromotionLinksInBatchRequest
from ...models.generate_campaign_product_promotion_links_in_batch_response import GenerateCampaignProductPromotionLinksInBatchResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    campaign_id: str,
    *,
    body: GenerateCampaignProductPromotionLinksInBatchRequest | Unset = UNSET,
    category_asset_cipher: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["category_asset_cipher"] = category_asset_cipher


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_partner/202505/campaigns/{campaign_id}/products/promotion_links/generate_batch".format(campaign_id=quote(str(campaign_id), safe=""),),
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GenerateCampaignProductPromotionLinksInBatchResponse | None:
    if response.status_code == 200:
        response_200 = GenerateCampaignProductPromotionLinksInBatchResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GenerateCampaignProductPromotionLinksInBatchResponse]:
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
    body: GenerateCampaignProductPromotionLinksInBatchRequest | Unset = UNSET,
    category_asset_cipher: str | Unset = UNSET,

) -> Response[GenerateCampaignProductPromotionLinksInBatchResponse]:
    """ Generate Campaign Product Promotion Links in Batch

     Generate promotion links for multiple products in an online campaign. For OPS or seller-initiated
    campaigns, use the joined campaign ID created after the partner joins the campaign, not the original
    campaign ID.

    Args:
        campaign_id (str):
        category_asset_cipher (str | Unset):
        body (GenerateCampaignProductPromotionLinksInBatchRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenerateCampaignProductPromotionLinksInBatchResponse]
     """


    kwargs = _get_kwargs(
        campaign_id=campaign_id,
body=body,
category_asset_cipher=category_asset_cipher,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    campaign_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GenerateCampaignProductPromotionLinksInBatchRequest | Unset = UNSET,
    category_asset_cipher: str | Unset = UNSET,

) -> GenerateCampaignProductPromotionLinksInBatchResponse | None:
    """ Generate Campaign Product Promotion Links in Batch

     Generate promotion links for multiple products in an online campaign. For OPS or seller-initiated
    campaigns, use the joined campaign ID created after the partner joins the campaign, not the original
    campaign ID.

    Args:
        campaign_id (str):
        category_asset_cipher (str | Unset):
        body (GenerateCampaignProductPromotionLinksInBatchRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenerateCampaignProductPromotionLinksInBatchResponse
     """


    return sync_detailed(
        campaign_id=campaign_id,
client=client,
body=body,
category_asset_cipher=category_asset_cipher,

    ).parsed

async def asyncio_detailed(
    campaign_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GenerateCampaignProductPromotionLinksInBatchRequest | Unset = UNSET,
    category_asset_cipher: str | Unset = UNSET,

) -> Response[GenerateCampaignProductPromotionLinksInBatchResponse]:
    """ Generate Campaign Product Promotion Links in Batch

     Generate promotion links for multiple products in an online campaign. For OPS or seller-initiated
    campaigns, use the joined campaign ID created after the partner joins the campaign, not the original
    campaign ID.

    Args:
        campaign_id (str):
        category_asset_cipher (str | Unset):
        body (GenerateCampaignProductPromotionLinksInBatchRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenerateCampaignProductPromotionLinksInBatchResponse]
     """


    kwargs = _get_kwargs(
        campaign_id=campaign_id,
body=body,
category_asset_cipher=category_asset_cipher,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    campaign_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GenerateCampaignProductPromotionLinksInBatchRequest | Unset = UNSET,
    category_asset_cipher: str | Unset = UNSET,

) -> GenerateCampaignProductPromotionLinksInBatchResponse | None:
    """ Generate Campaign Product Promotion Links in Batch

     Generate promotion links for multiple products in an online campaign. For OPS or seller-initiated
    campaigns, use the joined campaign ID created after the partner joins the campaign, not the original
    campaign ID.

    Args:
        campaign_id (str):
        category_asset_cipher (str | Unset):
        body (GenerateCampaignProductPromotionLinksInBatchRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenerateCampaignProductPromotionLinksInBatchResponse
     """


    return (await asyncio_detailed(
        campaign_id=campaign_id,
client=client,
body=body,
category_asset_cipher=category_asset_cipher,

    )).parsed
