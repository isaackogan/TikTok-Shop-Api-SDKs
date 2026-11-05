from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.register_seller_partner_campaign_products_request import RegisterSellerPartnerCampaignProductsRequest
from ...models.register_seller_partner_campaign_products_response import RegisterSellerPartnerCampaignProductsResponse
from typing import cast



def _get_kwargs(
    campaign_id: str,
    *,
    body: RegisterSellerPartnerCampaignProductsRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_seller/202611/partner_campaigns/{campaign_id}/products".format(campaign_id=quote(str(campaign_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RegisterSellerPartnerCampaignProductsResponse | None:
    if response.status_code == 200:
        response_200 = RegisterSellerPartnerCampaignProductsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RegisterSellerPartnerCampaignProductsResponse]:
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
    body: RegisterSellerPartnerCampaignProductsRequest,

) -> Response[RegisterSellerPartnerCampaignProductsResponse]:
    """ Register Seller Partner Campaign Products

     Submits 1 to 200 products belonging to the authorized shop to one partner campaign. The campaign
    registration window, shop eligibility, product ownership and applicable commission rules are
    checked. Commission values use percentage multiplied by 100: 1500 means 15%. Provide an authorized
    contact entry of type EMAIL; type WHATSAPP also requires region_code. Other contact types are not
    supported. The same sample_quota applies to each submitted product. Ads-commission map keys must
    occur in product_ids. A successful response has data: {}; it does not return per-product results.
    Query registered products to inspect resulting status. No idempotency-key guarantee is provided;
    check the registration records before retrying an ambiguous submission.

    Args:
        campaign_id (str):
        body (RegisterSellerPartnerCampaignProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegisterSellerPartnerCampaignProductsResponse]
     """


    kwargs = _get_kwargs(
        campaign_id=campaign_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    campaign_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RegisterSellerPartnerCampaignProductsRequest,

) -> RegisterSellerPartnerCampaignProductsResponse | None:
    """ Register Seller Partner Campaign Products

     Submits 1 to 200 products belonging to the authorized shop to one partner campaign. The campaign
    registration window, shop eligibility, product ownership and applicable commission rules are
    checked. Commission values use percentage multiplied by 100: 1500 means 15%. Provide an authorized
    contact entry of type EMAIL; type WHATSAPP also requires region_code. Other contact types are not
    supported. The same sample_quota applies to each submitted product. Ads-commission map keys must
    occur in product_ids. A successful response has data: {}; it does not return per-product results.
    Query registered products to inspect resulting status. No idempotency-key guarantee is provided;
    check the registration records before retrying an ambiguous submission.

    Args:
        campaign_id (str):
        body (RegisterSellerPartnerCampaignProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegisterSellerPartnerCampaignProductsResponse
     """


    return sync_detailed(
        campaign_id=campaign_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    campaign_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RegisterSellerPartnerCampaignProductsRequest,

) -> Response[RegisterSellerPartnerCampaignProductsResponse]:
    """ Register Seller Partner Campaign Products

     Submits 1 to 200 products belonging to the authorized shop to one partner campaign. The campaign
    registration window, shop eligibility, product ownership and applicable commission rules are
    checked. Commission values use percentage multiplied by 100: 1500 means 15%. Provide an authorized
    contact entry of type EMAIL; type WHATSAPP also requires region_code. Other contact types are not
    supported. The same sample_quota applies to each submitted product. Ads-commission map keys must
    occur in product_ids. A successful response has data: {}; it does not return per-product results.
    Query registered products to inspect resulting status. No idempotency-key guarantee is provided;
    check the registration records before retrying an ambiguous submission.

    Args:
        campaign_id (str):
        body (RegisterSellerPartnerCampaignProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegisterSellerPartnerCampaignProductsResponse]
     """


    kwargs = _get_kwargs(
        campaign_id=campaign_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    campaign_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RegisterSellerPartnerCampaignProductsRequest,

) -> RegisterSellerPartnerCampaignProductsResponse | None:
    """ Register Seller Partner Campaign Products

     Submits 1 to 200 products belonging to the authorized shop to one partner campaign. The campaign
    registration window, shop eligibility, product ownership and applicable commission rules are
    checked. Commission values use percentage multiplied by 100: 1500 means 15%. Provide an authorized
    contact entry of type EMAIL; type WHATSAPP also requires region_code. Other contact types are not
    supported. The same sample_quota applies to each submitted product. Ads-commission map keys must
    occur in product_ids. A successful response has data: {}; it does not return per-product results.
    Query registered products to inspect resulting status. No idempotency-key guarantee is provided;
    check the registration records before retrying an ambiguous submission.

    Args:
        campaign_id (str):
        body (RegisterSellerPartnerCampaignProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegisterSellerPartnerCampaignProductsResponse
     """


    return (await asyncio_detailed(
        campaign_id=campaign_id,
client=client,
body=body,

    )).parsed
