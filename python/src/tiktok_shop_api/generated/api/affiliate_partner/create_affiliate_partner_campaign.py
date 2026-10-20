from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_affiliate_partner_campaign_request import CreateAffiliatePartnerCampaignRequest
from ...models.create_affiliate_partner_campaign_response import CreateAffiliatePartnerCampaignResponse
from typing import cast



def _get_kwargs(
    *,
    body: CreateAffiliatePartnerCampaignRequest,
    category_asset_cipher: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["category_asset_cipher"] = category_asset_cipher


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_partner/202405/campaigns",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateAffiliatePartnerCampaignResponse | None:
    if response.status_code == 200:
        response_200 = CreateAffiliatePartnerCampaignResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateAffiliatePartnerCampaignResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAffiliatePartnerCampaignRequest,
    category_asset_cipher: str,

) -> Response[CreateAffiliatePartnerCampaignResponse]:
    """ Create Affiliate Partner Campaign

     Creates an affiliate partner campaign for either specific sellers identified by shop code or
    eligible seller types. Configure the campaign period, seller registration period, commission rate,
    and contact information. When the campaign is created successfully, the operation returns the new
    `campaign_id` synchronously. The campaign is not displayed to sellers after creation. To publish a
    successfully created campaign, call `POST /affiliate_partner/202405/campaigns/{campaign_id}/publish`
    with the returned campaign ID.

    Args:
        category_asset_cipher (str):
        body (CreateAffiliatePartnerCampaignRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAffiliatePartnerCampaignResponse]
     """


    kwargs = _get_kwargs(
        body=body,
category_asset_cipher=category_asset_cipher,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAffiliatePartnerCampaignRequest,
    category_asset_cipher: str,

) -> CreateAffiliatePartnerCampaignResponse | None:
    """ Create Affiliate Partner Campaign

     Creates an affiliate partner campaign for either specific sellers identified by shop code or
    eligible seller types. Configure the campaign period, seller registration period, commission rate,
    and contact information. When the campaign is created successfully, the operation returns the new
    `campaign_id` synchronously. The campaign is not displayed to sellers after creation. To publish a
    successfully created campaign, call `POST /affiliate_partner/202405/campaigns/{campaign_id}/publish`
    with the returned campaign ID.

    Args:
        category_asset_cipher (str):
        body (CreateAffiliatePartnerCampaignRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAffiliatePartnerCampaignResponse
     """


    return sync_detailed(
        client=client,
body=body,
category_asset_cipher=category_asset_cipher,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAffiliatePartnerCampaignRequest,
    category_asset_cipher: str,

) -> Response[CreateAffiliatePartnerCampaignResponse]:
    """ Create Affiliate Partner Campaign

     Creates an affiliate partner campaign for either specific sellers identified by shop code or
    eligible seller types. Configure the campaign period, seller registration period, commission rate,
    and contact information. When the campaign is created successfully, the operation returns the new
    `campaign_id` synchronously. The campaign is not displayed to sellers after creation. To publish a
    successfully created campaign, call `POST /affiliate_partner/202405/campaigns/{campaign_id}/publish`
    with the returned campaign ID.

    Args:
        category_asset_cipher (str):
        body (CreateAffiliatePartnerCampaignRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAffiliatePartnerCampaignResponse]
     """


    kwargs = _get_kwargs(
        body=body,
category_asset_cipher=category_asset_cipher,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAffiliatePartnerCampaignRequest,
    category_asset_cipher: str,

) -> CreateAffiliatePartnerCampaignResponse | None:
    """ Create Affiliate Partner Campaign

     Creates an affiliate partner campaign for either specific sellers identified by shop code or
    eligible seller types. Configure the campaign period, seller registration period, commission rate,
    and contact information. When the campaign is created successfully, the operation returns the new
    `campaign_id` synchronously. The campaign is not displayed to sellers after creation. To publish a
    successfully created campaign, call `POST /affiliate_partner/202405/campaigns/{campaign_id}/publish`
    with the returned campaign ID.

    Args:
        category_asset_cipher (str):
        body (CreateAffiliatePartnerCampaignRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAffiliatePartnerCampaignResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
category_asset_cipher=category_asset_cipher,

    )).parsed
