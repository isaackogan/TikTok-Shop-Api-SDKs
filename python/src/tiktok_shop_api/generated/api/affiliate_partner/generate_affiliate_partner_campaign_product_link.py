from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.generate_affiliate_partner_campaign_product_link_request import GenerateAffiliatePartnerCampaignProductLinkRequest
from ...models.generate_affiliate_partner_campaign_product_link_response import GenerateAffiliatePartnerCampaignProductLinkResponse
from typing import cast



def _get_kwargs(
    campaign_id: str,
    product_id: str,
    *,
    body: GenerateAffiliatePartnerCampaignProductLinkRequest,
    category_asset_cipher: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["category_asset_cipher"] = category_asset_cipher


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_partner/202405/campaigns/{campaign_id}/products/{product_id}/promotion_link/generate".format(campaign_id=quote(str(campaign_id), safe=""),product_id=quote(str(product_id), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GenerateAffiliatePartnerCampaignProductLinkResponse | None:
    if response.status_code == 200:
        response_200 = GenerateAffiliatePartnerCampaignProductLinkResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GenerateAffiliatePartnerCampaignProductLinkResponse]:
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
    body: GenerateAffiliatePartnerCampaignProductLinkRequest,
    category_asset_cipher: str,

) -> Response[GenerateAffiliatePartnerCampaignProductLinkResponse]:
    """ Generate Affiliate Partner Campaign Product Link

     Generates a promotion link for a product in an existing online campaign. The product must be
    associated with the campaign and appear in the response from Get Affiliate Partner Campaign Product
    List with `review_status` set to `APPROVED` or `PENDING_CLOSED`.

    Args:
        campaign_id (str):
        product_id (str):
        category_asset_cipher (str):
        body (GenerateAffiliatePartnerCampaignProductLinkRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenerateAffiliatePartnerCampaignProductLinkResponse]
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
    body: GenerateAffiliatePartnerCampaignProductLinkRequest,
    category_asset_cipher: str,

) -> GenerateAffiliatePartnerCampaignProductLinkResponse | None:
    """ Generate Affiliate Partner Campaign Product Link

     Generates a promotion link for a product in an existing online campaign. The product must be
    associated with the campaign and appear in the response from Get Affiliate Partner Campaign Product
    List with `review_status` set to `APPROVED` or `PENDING_CLOSED`.

    Args:
        campaign_id (str):
        product_id (str):
        category_asset_cipher (str):
        body (GenerateAffiliatePartnerCampaignProductLinkRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenerateAffiliatePartnerCampaignProductLinkResponse
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
    body: GenerateAffiliatePartnerCampaignProductLinkRequest,
    category_asset_cipher: str,

) -> Response[GenerateAffiliatePartnerCampaignProductLinkResponse]:
    """ Generate Affiliate Partner Campaign Product Link

     Generates a promotion link for a product in an existing online campaign. The product must be
    associated with the campaign and appear in the response from Get Affiliate Partner Campaign Product
    List with `review_status` set to `APPROVED` or `PENDING_CLOSED`.

    Args:
        campaign_id (str):
        product_id (str):
        category_asset_cipher (str):
        body (GenerateAffiliatePartnerCampaignProductLinkRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenerateAffiliatePartnerCampaignProductLinkResponse]
     """


    kwargs = _get_kwargs(
        campaign_id=campaign_id,
product_id=product_id,
body=body,
category_asset_cipher=category_asset_cipher,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    campaign_id: str,
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GenerateAffiliatePartnerCampaignProductLinkRequest,
    category_asset_cipher: str,

) -> GenerateAffiliatePartnerCampaignProductLinkResponse | None:
    """ Generate Affiliate Partner Campaign Product Link

     Generates a promotion link for a product in an existing online campaign. The product must be
    associated with the campaign and appear in the response from Get Affiliate Partner Campaign Product
    List with `review_status` set to `APPROVED` or `PENDING_CLOSED`.

    Args:
        campaign_id (str):
        product_id (str):
        category_asset_cipher (str):
        body (GenerateAffiliatePartnerCampaignProductLinkRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenerateAffiliatePartnerCampaignProductLinkResponse
     """


    return (await asyncio_detailed(
        campaign_id=campaign_id,
product_id=product_id,
client=client,
body=body,
category_asset_cipher=category_asset_cipher,

    )).parsed
