from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.publish_affiliate_partner_campaign_request import PublishAffiliatePartnerCampaignRequest
from ...models.publish_affiliate_partner_campaign_response import PublishAffiliatePartnerCampaignResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    campaign_id: str,
    *,
    body: PublishAffiliatePartnerCampaignRequest | Unset = UNSET,
    category_asset_cipher: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["category_asset_cipher"] = category_asset_cipher


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_partner/202405/campaigns/{campaign_id}/publish".format(campaign_id=quote(str(campaign_id), safe=""),),
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PublishAffiliatePartnerCampaignResponse | None:
    if response.status_code == 200:
        response_200 = PublishAffiliatePartnerCampaignResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PublishAffiliatePartnerCampaignResponse]:
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
    body: PublishAffiliatePartnerCampaignRequest | Unset = UNSET,
    category_asset_cipher: str,

) -> Response[PublishAffiliatePartnerCampaignResponse]:
    """ Publish Affiliate Partner Campaign

     This API offers the ability to publish an Affiliate Partner campaign. The campaign will be displayed
    to sellers after publishing.

    Args:
        campaign_id (str):
        category_asset_cipher (str):
        body (PublishAffiliatePartnerCampaignRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PublishAffiliatePartnerCampaignResponse]
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
    body: PublishAffiliatePartnerCampaignRequest | Unset = UNSET,
    category_asset_cipher: str,

) -> PublishAffiliatePartnerCampaignResponse | None:
    """ Publish Affiliate Partner Campaign

     This API offers the ability to publish an Affiliate Partner campaign. The campaign will be displayed
    to sellers after publishing.

    Args:
        campaign_id (str):
        category_asset_cipher (str):
        body (PublishAffiliatePartnerCampaignRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PublishAffiliatePartnerCampaignResponse
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
    body: PublishAffiliatePartnerCampaignRequest | Unset = UNSET,
    category_asset_cipher: str,

) -> Response[PublishAffiliatePartnerCampaignResponse]:
    """ Publish Affiliate Partner Campaign

     This API offers the ability to publish an Affiliate Partner campaign. The campaign will be displayed
    to sellers after publishing.

    Args:
        campaign_id (str):
        category_asset_cipher (str):
        body (PublishAffiliatePartnerCampaignRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PublishAffiliatePartnerCampaignResponse]
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
    body: PublishAffiliatePartnerCampaignRequest | Unset = UNSET,
    category_asset_cipher: str,

) -> PublishAffiliatePartnerCampaignResponse | None:
    """ Publish Affiliate Partner Campaign

     This API offers the ability to publish an Affiliate Partner campaign. The campaign will be displayed
    to sellers after publishing.

    Args:
        campaign_id (str):
        category_asset_cipher (str):
        body (PublishAffiliatePartnerCampaignRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PublishAffiliatePartnerCampaignResponse
     """


    return (await asyncio_detailed(
        campaign_id=campaign_id,
client=client,
body=body,
category_asset_cipher=category_asset_cipher,

    )).parsed
