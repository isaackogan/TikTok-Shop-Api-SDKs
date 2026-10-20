from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_affiliate_partner_campaign_detail_response import GetAffiliatePartnerCampaignDetailResponse
from typing import cast



def _get_kwargs(
    campaign_id: str,
    *,
    category_asset_cipher: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["category_asset_cipher"] = category_asset_cipher


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/affiliate_partner/202405/campaigns/{campaign_id}".format(campaign_id=quote(str(campaign_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAffiliatePartnerCampaignDetailResponse | None:
    if response.status_code == 200:
        response_200 = GetAffiliatePartnerCampaignDetailResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAffiliatePartnerCampaignDetailResponse]:
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

) -> Response[GetAffiliatePartnerCampaignDetailResponse]:
    """ Get Affiliate Partner Campaign Detail

     This API offers the ability to get affiliate campaign details.

    Args:
        campaign_id (str):
        category_asset_cipher (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAffiliatePartnerCampaignDetailResponse]
     """


    kwargs = _get_kwargs(
        campaign_id=campaign_id,
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
    category_asset_cipher: str,

) -> GetAffiliatePartnerCampaignDetailResponse | None:
    """ Get Affiliate Partner Campaign Detail

     This API offers the ability to get affiliate campaign details.

    Args:
        campaign_id (str):
        category_asset_cipher (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAffiliatePartnerCampaignDetailResponse
     """


    return sync_detailed(
        campaign_id=campaign_id,
client=client,
category_asset_cipher=category_asset_cipher,

    ).parsed

async def asyncio_detailed(
    campaign_id: str,
    *,
    client: AuthenticatedClient | Client,
    category_asset_cipher: str,

) -> Response[GetAffiliatePartnerCampaignDetailResponse]:
    """ Get Affiliate Partner Campaign Detail

     This API offers the ability to get affiliate campaign details.

    Args:
        campaign_id (str):
        category_asset_cipher (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAffiliatePartnerCampaignDetailResponse]
     """


    kwargs = _get_kwargs(
        campaign_id=campaign_id,
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
    category_asset_cipher: str,

) -> GetAffiliatePartnerCampaignDetailResponse | None:
    """ Get Affiliate Partner Campaign Detail

     This API offers the ability to get affiliate campaign details.

    Args:
        campaign_id (str):
        category_asset_cipher (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAffiliatePartnerCampaignDetailResponse
     """


    return (await asyncio_detailed(
        campaign_id=campaign_id,
client=client,
category_asset_cipher=category_asset_cipher,

    )).parsed
