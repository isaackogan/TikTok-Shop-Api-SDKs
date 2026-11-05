from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_seller_partner_campaign_candidate_products_response import GetSellerPartnerCampaignCandidateProductsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    campaign_id: str,
    *,
    page_size: int,
    page_token: str | Unset = UNSET,
    key_word: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
    product_search_key: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page_size"] = page_size

    params["page_token"] = page_token

    params["key_word"] = key_word

    params["category_id"] = category_id

    params["product_search_key"] = product_search_key


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/affiliate_seller/202611/partner_campaigns/{campaign_id}/candidate_products".format(campaign_id=quote(str(campaign_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetSellerPartnerCampaignCandidateProductsResponse | None:
    if response.status_code == 200:
        response_200 = GetSellerPartnerCampaignCandidateProductsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetSellerPartnerCampaignCandidateProductsResponse]:
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
    page_size: int,
    page_token: str | Unset = UNSET,
    key_word: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
    product_search_key: str,

) -> Response[GetSellerPartnerCampaignCandidateProductsResponse]:
    """ Get Seller Partner Campaign Candidate Products

     Lists the authorized shop's live products as candidates for a partner campaign. is_under_governed
    and has_registered identify relevant restrictions; listing a product does not guarantee successful
    registration. Product prices and available Open Plan commission settings are included. Omit
    page_token for the first page; pass next_page_token for subsequent pages. page_size must be 20, 50
    or 100. total_num is the total matching count. Optional properties may be absent when the
    corresponding data is unavailable.

    Args:
        campaign_id (str):
        page_size (int):
        page_token (str | Unset):
        key_word (str | Unset):
        category_id (str | Unset):
        product_search_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSellerPartnerCampaignCandidateProductsResponse]
     """


    kwargs = _get_kwargs(
        campaign_id=campaign_id,
page_size=page_size,
page_token=page_token,
key_word=key_word,
category_id=category_id,
product_search_key=product_search_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    campaign_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_size: int,
    page_token: str | Unset = UNSET,
    key_word: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
    product_search_key: str,

) -> GetSellerPartnerCampaignCandidateProductsResponse | None:
    """ Get Seller Partner Campaign Candidate Products

     Lists the authorized shop's live products as candidates for a partner campaign. is_under_governed
    and has_registered identify relevant restrictions; listing a product does not guarantee successful
    registration. Product prices and available Open Plan commission settings are included. Omit
    page_token for the first page; pass next_page_token for subsequent pages. page_size must be 20, 50
    or 100. total_num is the total matching count. Optional properties may be absent when the
    corresponding data is unavailable.

    Args:
        campaign_id (str):
        page_size (int):
        page_token (str | Unset):
        key_word (str | Unset):
        category_id (str | Unset):
        product_search_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSellerPartnerCampaignCandidateProductsResponse
     """


    return sync_detailed(
        campaign_id=campaign_id,
client=client,
page_size=page_size,
page_token=page_token,
key_word=key_word,
category_id=category_id,
product_search_key=product_search_key,

    ).parsed

async def asyncio_detailed(
    campaign_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_size: int,
    page_token: str | Unset = UNSET,
    key_word: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
    product_search_key: str,

) -> Response[GetSellerPartnerCampaignCandidateProductsResponse]:
    """ Get Seller Partner Campaign Candidate Products

     Lists the authorized shop's live products as candidates for a partner campaign. is_under_governed
    and has_registered identify relevant restrictions; listing a product does not guarantee successful
    registration. Product prices and available Open Plan commission settings are included. Omit
    page_token for the first page; pass next_page_token for subsequent pages. page_size must be 20, 50
    or 100. total_num is the total matching count. Optional properties may be absent when the
    corresponding data is unavailable.

    Args:
        campaign_id (str):
        page_size (int):
        page_token (str | Unset):
        key_word (str | Unset):
        category_id (str | Unset):
        product_search_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSellerPartnerCampaignCandidateProductsResponse]
     """


    kwargs = _get_kwargs(
        campaign_id=campaign_id,
page_size=page_size,
page_token=page_token,
key_word=key_word,
category_id=category_id,
product_search_key=product_search_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    campaign_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_size: int,
    page_token: str | Unset = UNSET,
    key_word: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
    product_search_key: str,

) -> GetSellerPartnerCampaignCandidateProductsResponse | None:
    """ Get Seller Partner Campaign Candidate Products

     Lists the authorized shop's live products as candidates for a partner campaign. is_under_governed
    and has_registered identify relevant restrictions; listing a product does not guarantee successful
    registration. Product prices and available Open Plan commission settings are included. Omit
    page_token for the first page; pass next_page_token for subsequent pages. page_size must be 20, 50
    or 100. total_num is the total matching count. Optional properties may be absent when the
    corresponding data is unavailable.

    Args:
        campaign_id (str):
        page_size (int):
        page_token (str | Unset):
        key_word (str | Unset):
        category_id (str | Unset):
        product_search_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSellerPartnerCampaignCandidateProductsResponse
     """


    return (await asyncio_detailed(
        campaign_id=campaign_id,
client=client,
page_size=page_size,
page_token=page_token,
key_word=key_word,
category_id=category_id,
product_search_key=product_search_key,

    )).parsed
