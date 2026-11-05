from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_seller_partner_campaign_detail_response import GetSellerPartnerCampaignDetailResponse
from typing import cast



def _get_kwargs(
    campaign_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/affiliate_seller/202611/partner_campaigns/{campaign_id}".format(campaign_id=quote(str(campaign_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetSellerPartnerCampaignDetailResponse | None:
    if response.status_code == 200:
        response_200 = GetSellerPartnerCampaignDetailResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetSellerPartnerCampaignDetailResponse]:
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

) -> Response[GetSellerPartnerCampaignDetailResponse]:
    """ Get Seller Partner Campaign Detail

     Returns the rules, registration period, campaign period, available statistics and applicable shop or
    agency summaries for a campaign visible to the authorized shop. can_register indicates the campaign
    registration-window state, not a guarantee of shop or product eligibility. is_registered reflects
    existing participation. Contact details and linked TikTok business accounts are not returned.
    Optional fields depend on campaign type and available data. Display text can contain user-authored
    content.

    Args:
        campaign_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSellerPartnerCampaignDetailResponse]
     """


    kwargs = _get_kwargs(
        campaign_id=campaign_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    campaign_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> GetSellerPartnerCampaignDetailResponse | None:
    """ Get Seller Partner Campaign Detail

     Returns the rules, registration period, campaign period, available statistics and applicable shop or
    agency summaries for a campaign visible to the authorized shop. can_register indicates the campaign
    registration-window state, not a guarantee of shop or product eligibility. is_registered reflects
    existing participation. Contact details and linked TikTok business accounts are not returned.
    Optional fields depend on campaign type and available data. Display text can contain user-authored
    content.

    Args:
        campaign_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSellerPartnerCampaignDetailResponse
     """


    return sync_detailed(
        campaign_id=campaign_id,
client=client,

    ).parsed

async def asyncio_detailed(
    campaign_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetSellerPartnerCampaignDetailResponse]:
    """ Get Seller Partner Campaign Detail

     Returns the rules, registration period, campaign period, available statistics and applicable shop or
    agency summaries for a campaign visible to the authorized shop. can_register indicates the campaign
    registration-window state, not a guarantee of shop or product eligibility. is_registered reflects
    existing participation. Contact details and linked TikTok business accounts are not returned.
    Optional fields depend on campaign type and available data. Display text can contain user-authored
    content.

    Args:
        campaign_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSellerPartnerCampaignDetailResponse]
     """


    kwargs = _get_kwargs(
        campaign_id=campaign_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    campaign_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> GetSellerPartnerCampaignDetailResponse | None:
    """ Get Seller Partner Campaign Detail

     Returns the rules, registration period, campaign period, available statistics and applicable shop or
    agency summaries for a campaign visible to the authorized shop. can_register indicates the campaign
    registration-window state, not a guarantee of shop or product eligibility. is_registered reflects
    existing participation. Contact details and linked TikTok business accounts are not returned.
    Optional fields depend on campaign type and available data. Display text can contain user-authored
    content.

    Args:
        campaign_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSellerPartnerCampaignDetailResponse
     """


    return (await asyncio_detailed(
        campaign_id=campaign_id,
client=client,

    )).parsed
