from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_affiliate_partner_campaign_list_response import GetAffiliatePartnerCampaignListResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    category_asset_cipher: str,
    page_size: int,
    page_token: str | Unset = UNSET,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    query_type_filter: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["category_asset_cipher"] = category_asset_cipher

    params["page_size"] = page_size

    params["page_token"] = page_token

    params["status"] = status

    params["type"] = type_

    params["query_type_filter"] = query_type_filter


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/affiliate_partner/202405/campaigns",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAffiliatePartnerCampaignListResponse | None:
    if response.status_code == 200:
        response_200 = GetAffiliatePartnerCampaignListResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAffiliatePartnerCampaignListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    category_asset_cipher: str,
    page_size: int,
    page_token: str | Unset = UNSET,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    query_type_filter: str | Unset = UNSET,

) -> Response[GetAffiliatePartnerCampaignListResponse]:
    """ Get Affiliate Partner Campaign List

     Lists campaigns for an affiliate partner, filtered by campaign category, participation state, and
    campaign status.

    Args:
        category_asset_cipher (str):
        page_size (int):
        page_token (str | Unset):
        status (str | Unset):
        type_ (str | Unset):
        query_type_filter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAffiliatePartnerCampaignListResponse]
     """


    kwargs = _get_kwargs(
        category_asset_cipher=category_asset_cipher,
page_size=page_size,
page_token=page_token,
status=status,
type_=type_,
query_type_filter=query_type_filter,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    category_asset_cipher: str,
    page_size: int,
    page_token: str | Unset = UNSET,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    query_type_filter: str | Unset = UNSET,

) -> GetAffiliatePartnerCampaignListResponse | None:
    """ Get Affiliate Partner Campaign List

     Lists campaigns for an affiliate partner, filtered by campaign category, participation state, and
    campaign status.

    Args:
        category_asset_cipher (str):
        page_size (int):
        page_token (str | Unset):
        status (str | Unset):
        type_ (str | Unset):
        query_type_filter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAffiliatePartnerCampaignListResponse
     """


    return sync_detailed(
        client=client,
category_asset_cipher=category_asset_cipher,
page_size=page_size,
page_token=page_token,
status=status,
type_=type_,
query_type_filter=query_type_filter,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    category_asset_cipher: str,
    page_size: int,
    page_token: str | Unset = UNSET,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    query_type_filter: str | Unset = UNSET,

) -> Response[GetAffiliatePartnerCampaignListResponse]:
    """ Get Affiliate Partner Campaign List

     Lists campaigns for an affiliate partner, filtered by campaign category, participation state, and
    campaign status.

    Args:
        category_asset_cipher (str):
        page_size (int):
        page_token (str | Unset):
        status (str | Unset):
        type_ (str | Unset):
        query_type_filter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAffiliatePartnerCampaignListResponse]
     """


    kwargs = _get_kwargs(
        category_asset_cipher=category_asset_cipher,
page_size=page_size,
page_token=page_token,
status=status,
type_=type_,
query_type_filter=query_type_filter,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    category_asset_cipher: str,
    page_size: int,
    page_token: str | Unset = UNSET,
    status: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    query_type_filter: str | Unset = UNSET,

) -> GetAffiliatePartnerCampaignListResponse | None:
    """ Get Affiliate Partner Campaign List

     Lists campaigns for an affiliate partner, filtered by campaign category, participation state, and
    campaign status.

    Args:
        category_asset_cipher (str):
        page_size (int):
        page_token (str | Unset):
        status (str | Unset):
        type_ (str | Unset):
        query_type_filter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAffiliatePartnerCampaignListResponse
     """


    return (await asyncio_detailed(
        client=client,
category_asset_cipher=category_asset_cipher,
page_size=page_size,
page_token=page_token,
status=status,
type_=type_,
query_type_filter=query_type_filter,

    )).parsed
