from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.edit_affiliate_partner_campaign_request import EditAffiliatePartnerCampaignRequest
from ...models.edit_affiliate_partner_campaign_response import EditAffiliatePartnerCampaignResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    campaign_id: str,
    *,
    body: EditAffiliatePartnerCampaignRequest | Unset = UNSET,
    category_asset_cipher: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["category_asset_cipher"] = category_asset_cipher


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_partner/202405/campaigns/{campaign_id}/partial_edit".format(campaign_id=quote(str(campaign_id), safe=""),),
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> EditAffiliatePartnerCampaignResponse | None:
    if response.status_code == 200:
        response_200 = EditAffiliatePartnerCampaignResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[EditAffiliatePartnerCampaignResponse]:
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
    body: EditAffiliatePartnerCampaignRequest | Unset = UNSET,
    category_asset_cipher: str,

) -> Response[EditAffiliatePartnerCampaignResponse]:
    """ Edit Affiliate Partner Campaign

     Partially updates an Affiliate Partner campaign. Fields omitted from the request retain their
    current values, including omitted fields within `contact_info`. `target_seller_types` and
    `target_shop_codes` are mutually exclusive. To switch targeting modes, send the previously used
    field as an empty array and the new field with its values. Campaigns cannot be edited after they are
    closed.

    Args:
        campaign_id (str):
        category_asset_cipher (str):
        body (EditAffiliatePartnerCampaignRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EditAffiliatePartnerCampaignResponse]
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
    body: EditAffiliatePartnerCampaignRequest | Unset = UNSET,
    category_asset_cipher: str,

) -> EditAffiliatePartnerCampaignResponse | None:
    """ Edit Affiliate Partner Campaign

     Partially updates an Affiliate Partner campaign. Fields omitted from the request retain their
    current values, including omitted fields within `contact_info`. `target_seller_types` and
    `target_shop_codes` are mutually exclusive. To switch targeting modes, send the previously used
    field as an empty array and the new field with its values. Campaigns cannot be edited after they are
    closed.

    Args:
        campaign_id (str):
        category_asset_cipher (str):
        body (EditAffiliatePartnerCampaignRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EditAffiliatePartnerCampaignResponse
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
    body: EditAffiliatePartnerCampaignRequest | Unset = UNSET,
    category_asset_cipher: str,

) -> Response[EditAffiliatePartnerCampaignResponse]:
    """ Edit Affiliate Partner Campaign

     Partially updates an Affiliate Partner campaign. Fields omitted from the request retain their
    current values, including omitted fields within `contact_info`. `target_seller_types` and
    `target_shop_codes` are mutually exclusive. To switch targeting modes, send the previously used
    field as an empty array and the new field with its values. Campaigns cannot be edited after they are
    closed.

    Args:
        campaign_id (str):
        category_asset_cipher (str):
        body (EditAffiliatePartnerCampaignRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EditAffiliatePartnerCampaignResponse]
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
    body: EditAffiliatePartnerCampaignRequest | Unset = UNSET,
    category_asset_cipher: str,

) -> EditAffiliatePartnerCampaignResponse | None:
    """ Edit Affiliate Partner Campaign

     Partially updates an Affiliate Partner campaign. Fields omitted from the request retain their
    current values, including omitted fields within `contact_info`. `target_seller_types` and
    `target_shop_codes` are mutually exclusive. To switch targeting modes, send the previously used
    field as an empty array and the new field with its values. Campaigns cannot be edited after they are
    closed.

    Args:
        campaign_id (str):
        category_asset_cipher (str):
        body (EditAffiliatePartnerCampaignRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EditAffiliatePartnerCampaignResponse
     """


    return (await asyncio_detailed(
        campaign_id=campaign_id,
client=client,
body=body,
category_asset_cipher=category_asset_cipher,

    )).parsed
