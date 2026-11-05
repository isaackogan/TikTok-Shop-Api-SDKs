from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.search_seller_partner_campaigns_response import SearchSellerPartnerCampaignsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    page_size: int,
    page_token: str | Unset = UNSET,
    key_word: str | Unset = UNSET,
    campaign_join_status_category: str | Unset = UNSET,
    campaign_online_status: str | Unset = UNSET,
    campaign_types: list[str] | Unset = UNSET,
    search_type: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page_size"] = page_size

    params["page_token"] = page_token

    params["key_word"] = key_word

    params["campaign_join_status_category"] = campaign_join_status_category

    params["campaign_online_status"] = campaign_online_status

    json_campaign_types: list[str] | Unset = UNSET
    if not isinstance(campaign_types, Unset):
        json_campaign_types = campaign_types


    params["campaign_types"] = json_campaign_types

    params["search_type"] = search_type


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/affiliate_seller/202611/partner_campaigns",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchSellerPartnerCampaignsResponse | None:
    if response.status_code == 200:
        response_200 = SearchSellerPartnerCampaignsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SearchSellerPartnerCampaignsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_size: int,
    page_token: str | Unset = UNSET,
    key_word: str | Unset = UNSET,
    campaign_join_status_category: str | Unset = UNSET,
    campaign_online_status: str | Unset = UNSET,
    campaign_types: list[str] | Unset = UNSET,
    search_type: str | Unset = UNSET,

) -> Response[SearchSellerPartnerCampaignsResponse]:
    """ Search Seller Partner Campaigns

     Lists partner campaigns visible to the authorized shop. Use JOINED for Manage, NOT_JOINED for
    Discover, or CLOSED for Closed. An omitted category or UNSPECIFIED retains the existing default
    search behavior. Campaign type and online-status filters apply to the specified-category branch.
    Results do not provide a complete assessment of product or shop registration eligibility. Omit
    page_token for the first page and use next_page_token to continue, keeping filters and page_size
    unchanged. Only full pages within the first 10000 matching records are accessible; total_num remains
    the actual matching count. Optional fields vary by campaign type and query branch. Display text can
    contain user-authored content.

    Args:
        page_size (int):
        page_token (str | Unset):
        key_word (str | Unset):
        campaign_join_status_category (str | Unset):
        campaign_online_status (str | Unset):
        campaign_types (list[str] | Unset):
        search_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchSellerPartnerCampaignsResponse]
     """


    kwargs = _get_kwargs(
        page_size=page_size,
page_token=page_token,
key_word=key_word,
campaign_join_status_category=campaign_join_status_category,
campaign_online_status=campaign_online_status,
campaign_types=campaign_types,
search_type=search_type,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    page_size: int,
    page_token: str | Unset = UNSET,
    key_word: str | Unset = UNSET,
    campaign_join_status_category: str | Unset = UNSET,
    campaign_online_status: str | Unset = UNSET,
    campaign_types: list[str] | Unset = UNSET,
    search_type: str | Unset = UNSET,

) -> SearchSellerPartnerCampaignsResponse | None:
    """ Search Seller Partner Campaigns

     Lists partner campaigns visible to the authorized shop. Use JOINED for Manage, NOT_JOINED for
    Discover, or CLOSED for Closed. An omitted category or UNSPECIFIED retains the existing default
    search behavior. Campaign type and online-status filters apply to the specified-category branch.
    Results do not provide a complete assessment of product or shop registration eligibility. Omit
    page_token for the first page and use next_page_token to continue, keeping filters and page_size
    unchanged. Only full pages within the first 10000 matching records are accessible; total_num remains
    the actual matching count. Optional fields vary by campaign type and query branch. Display text can
    contain user-authored content.

    Args:
        page_size (int):
        page_token (str | Unset):
        key_word (str | Unset):
        campaign_join_status_category (str | Unset):
        campaign_online_status (str | Unset):
        campaign_types (list[str] | Unset):
        search_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchSellerPartnerCampaignsResponse
     """


    return sync_detailed(
        client=client,
page_size=page_size,
page_token=page_token,
key_word=key_word,
campaign_join_status_category=campaign_join_status_category,
campaign_online_status=campaign_online_status,
campaign_types=campaign_types,
search_type=search_type,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_size: int,
    page_token: str | Unset = UNSET,
    key_word: str | Unset = UNSET,
    campaign_join_status_category: str | Unset = UNSET,
    campaign_online_status: str | Unset = UNSET,
    campaign_types: list[str] | Unset = UNSET,
    search_type: str | Unset = UNSET,

) -> Response[SearchSellerPartnerCampaignsResponse]:
    """ Search Seller Partner Campaigns

     Lists partner campaigns visible to the authorized shop. Use JOINED for Manage, NOT_JOINED for
    Discover, or CLOSED for Closed. An omitted category or UNSPECIFIED retains the existing default
    search behavior. Campaign type and online-status filters apply to the specified-category branch.
    Results do not provide a complete assessment of product or shop registration eligibility. Omit
    page_token for the first page and use next_page_token to continue, keeping filters and page_size
    unchanged. Only full pages within the first 10000 matching records are accessible; total_num remains
    the actual matching count. Optional fields vary by campaign type and query branch. Display text can
    contain user-authored content.

    Args:
        page_size (int):
        page_token (str | Unset):
        key_word (str | Unset):
        campaign_join_status_category (str | Unset):
        campaign_online_status (str | Unset):
        campaign_types (list[str] | Unset):
        search_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchSellerPartnerCampaignsResponse]
     """


    kwargs = _get_kwargs(
        page_size=page_size,
page_token=page_token,
key_word=key_word,
campaign_join_status_category=campaign_join_status_category,
campaign_online_status=campaign_online_status,
campaign_types=campaign_types,
search_type=search_type,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_size: int,
    page_token: str | Unset = UNSET,
    key_word: str | Unset = UNSET,
    campaign_join_status_category: str | Unset = UNSET,
    campaign_online_status: str | Unset = UNSET,
    campaign_types: list[str] | Unset = UNSET,
    search_type: str | Unset = UNSET,

) -> SearchSellerPartnerCampaignsResponse | None:
    """ Search Seller Partner Campaigns

     Lists partner campaigns visible to the authorized shop. Use JOINED for Manage, NOT_JOINED for
    Discover, or CLOSED for Closed. An omitted category or UNSPECIFIED retains the existing default
    search behavior. Campaign type and online-status filters apply to the specified-category branch.
    Results do not provide a complete assessment of product or shop registration eligibility. Omit
    page_token for the first page and use next_page_token to continue, keeping filters and page_size
    unchanged. Only full pages within the first 10000 matching records are accessible; total_num remains
    the actual matching count. Optional fields vary by campaign type and query branch. Display text can
    contain user-authored content.

    Args:
        page_size (int):
        page_token (str | Unset):
        key_word (str | Unset):
        campaign_join_status_category (str | Unset):
        campaign_online_status (str | Unset):
        campaign_types (list[str] | Unset):
        search_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchSellerPartnerCampaignsResponse
     """


    return (await asyncio_detailed(
        client=client,
page_size=page_size,
page_token=page_token,
key_word=key_word,
campaign_join_status_category=campaign_join_status_category,
campaign_online_status=campaign_online_status,
campaign_types=campaign_types,
search_type=search_type,

    )).parsed
