from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_affiliate_campaign_creator_product_sample_status_response import GetAffiliateCampaignCreatorProductSampleStatusResponse
from typing import cast



def _get_kwargs(
    campaign_id: str,
    product_id: str,
    creator_temp_id: str,
    *,
    category_asset_cipher: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["category_asset_cipher"] = category_asset_cipher


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/affiliate_partner/202508/campaigns/{campaign_id}/products/{product_id}/creator/{creator_temp_id}/content/statistics/sample/status".format(campaign_id=quote(str(campaign_id), safe=""),product_id=quote(str(product_id), safe=""),creator_temp_id=quote(str(creator_temp_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAffiliateCampaignCreatorProductSampleStatusResponse | None:
    if response.status_code == 200:
        response_200 = GetAffiliateCampaignCreatorProductSampleStatusResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAffiliateCampaignCreatorProductSampleStatusResponse]:
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
    category_asset_cipher: str,

) -> Response[GetAffiliateCampaignCreatorProductSampleStatusResponse]:
    """ Get Affiliate Campaign Creator Product Sample Status

     Retrieves delivery and tracking details for a creator's product sample in an affiliate campaign. The
    creator must have applied for a sample of the specified product before calling this API.

    Args:
        campaign_id (str):
        product_id (str):
        creator_temp_id (str):
        category_asset_cipher (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAffiliateCampaignCreatorProductSampleStatusResponse]
     """


    kwargs = _get_kwargs(
        campaign_id=campaign_id,
product_id=product_id,
creator_temp_id=creator_temp_id,
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
    category_asset_cipher: str,

) -> GetAffiliateCampaignCreatorProductSampleStatusResponse | None:
    """ Get Affiliate Campaign Creator Product Sample Status

     Retrieves delivery and tracking details for a creator's product sample in an affiliate campaign. The
    creator must have applied for a sample of the specified product before calling this API.

    Args:
        campaign_id (str):
        product_id (str):
        creator_temp_id (str):
        category_asset_cipher (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAffiliateCampaignCreatorProductSampleStatusResponse
     """


    return sync_detailed(
        campaign_id=campaign_id,
product_id=product_id,
creator_temp_id=creator_temp_id,
client=client,
category_asset_cipher=category_asset_cipher,

    ).parsed

async def asyncio_detailed(
    campaign_id: str,
    product_id: str,
    creator_temp_id: str,
    *,
    client: AuthenticatedClient | Client,
    category_asset_cipher: str,

) -> Response[GetAffiliateCampaignCreatorProductSampleStatusResponse]:
    """ Get Affiliate Campaign Creator Product Sample Status

     Retrieves delivery and tracking details for a creator's product sample in an affiliate campaign. The
    creator must have applied for a sample of the specified product before calling this API.

    Args:
        campaign_id (str):
        product_id (str):
        creator_temp_id (str):
        category_asset_cipher (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAffiliateCampaignCreatorProductSampleStatusResponse]
     """


    kwargs = _get_kwargs(
        campaign_id=campaign_id,
product_id=product_id,
creator_temp_id=creator_temp_id,
category_asset_cipher=category_asset_cipher,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    campaign_id: str,
    product_id: str,
    creator_temp_id: str,
    *,
    client: AuthenticatedClient | Client,
    category_asset_cipher: str,

) -> GetAffiliateCampaignCreatorProductSampleStatusResponse | None:
    """ Get Affiliate Campaign Creator Product Sample Status

     Retrieves delivery and tracking details for a creator's product sample in an affiliate campaign. The
    creator must have applied for a sample of the specified product before calling this API.

    Args:
        campaign_id (str):
        product_id (str):
        creator_temp_id (str):
        category_asset_cipher (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAffiliateCampaignCreatorProductSampleStatusResponse
     """


    return (await asyncio_detailed(
        campaign_id=campaign_id,
product_id=product_id,
creator_temp_id=creator_temp_id,
client=client,
category_asset_cipher=category_asset_cipher,

    )).parsed
