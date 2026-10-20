from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_campaign_product_performance_list_response import GetCampaignProductPerformanceListResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    campaign_id: str,
    *,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    category_asset_cipher: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page_size"] = page_size

    params["page_token"] = page_token

    params["category_asset_cipher"] = category_asset_cipher


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/affiliate_partner/202501/campaigns/{campaign_id}/products/performance".format(campaign_id=quote(str(campaign_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetCampaignProductPerformanceListResponse | None:
    if response.status_code == 200:
        response_200 = GetCampaignProductPerformanceListResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetCampaignProductPerformanceListResponse]:
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
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    category_asset_cipher: str,

) -> Response[GetCampaignProductPerformanceListResponse]:
    """ Get Campaign Product Performance List

     Retrieves a paginated list of product-level performance statistics for the specified partner
    campaign.

    Args:
        campaign_id (str):
        page_size (int | Unset):
        page_token (str | Unset):
        category_asset_cipher (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCampaignProductPerformanceListResponse]
     """


    kwargs = _get_kwargs(
        campaign_id=campaign_id,
page_size=page_size,
page_token=page_token,
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
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    category_asset_cipher: str,

) -> GetCampaignProductPerformanceListResponse | None:
    """ Get Campaign Product Performance List

     Retrieves a paginated list of product-level performance statistics for the specified partner
    campaign.

    Args:
        campaign_id (str):
        page_size (int | Unset):
        page_token (str | Unset):
        category_asset_cipher (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCampaignProductPerformanceListResponse
     """


    return sync_detailed(
        campaign_id=campaign_id,
client=client,
page_size=page_size,
page_token=page_token,
category_asset_cipher=category_asset_cipher,

    ).parsed

async def asyncio_detailed(
    campaign_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    category_asset_cipher: str,

) -> Response[GetCampaignProductPerformanceListResponse]:
    """ Get Campaign Product Performance List

     Retrieves a paginated list of product-level performance statistics for the specified partner
    campaign.

    Args:
        campaign_id (str):
        page_size (int | Unset):
        page_token (str | Unset):
        category_asset_cipher (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCampaignProductPerformanceListResponse]
     """


    kwargs = _get_kwargs(
        campaign_id=campaign_id,
page_size=page_size,
page_token=page_token,
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
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    category_asset_cipher: str,

) -> GetCampaignProductPerformanceListResponse | None:
    """ Get Campaign Product Performance List

     Retrieves a paginated list of product-level performance statistics for the specified partner
    campaign.

    Args:
        campaign_id (str):
        page_size (int | Unset):
        page_token (str | Unset):
        category_asset_cipher (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCampaignProductPerformanceListResponse
     """


    return (await asyncio_detailed(
        campaign_id=campaign_id,
client=client,
page_size=page_size,
page_token=page_token,
category_asset_cipher=category_asset_cipher,

    )).parsed
