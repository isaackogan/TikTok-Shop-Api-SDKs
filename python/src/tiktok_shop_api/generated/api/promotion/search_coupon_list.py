from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.search_coupon_list_request import SearchCouponListRequest
from ...models.search_coupon_list_response import SearchCouponListResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: SearchCouponListRequest | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["page_token"] = page_token

    params["page_size"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/promotion/202406/coupons/search",
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchCouponListResponse | None:
    if response.status_code == 200:
        response_200 = SearchCouponListResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SearchCouponListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchCouponListRequest | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,

) -> Response[SearchCouponListResponse]:
    """ Search Coupon List

     Use this API to search coupons. Supported coupon creation sources include TikTok Shop Seller Center,
    the TikTok Seller App, and TikTok Shop CRM. Different supplied filters are combined with AND. Within
    status or display_type, multiple values are combined with OR. title_keyword performs phrase-prefix
    matching against the coupon title. For full details about a specific coupon, use the Get Coupon API.

    Args:
        page_token (str | Unset):
        page_size (int | Unset):
        body (SearchCouponListRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchCouponListResponse]
     """


    kwargs = _get_kwargs(
        body=body,
page_token=page_token,
page_size=page_size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SearchCouponListRequest | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,

) -> SearchCouponListResponse | None:
    """ Search Coupon List

     Use this API to search coupons. Supported coupon creation sources include TikTok Shop Seller Center,
    the TikTok Seller App, and TikTok Shop CRM. Different supplied filters are combined with AND. Within
    status or display_type, multiple values are combined with OR. title_keyword performs phrase-prefix
    matching against the coupon title. For full details about a specific coupon, use the Get Coupon API.

    Args:
        page_token (str | Unset):
        page_size (int | Unset):
        body (SearchCouponListRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchCouponListResponse
     """


    return sync_detailed(
        client=client,
body=body,
page_token=page_token,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchCouponListRequest | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,

) -> Response[SearchCouponListResponse]:
    """ Search Coupon List

     Use this API to search coupons. Supported coupon creation sources include TikTok Shop Seller Center,
    the TikTok Seller App, and TikTok Shop CRM. Different supplied filters are combined with AND. Within
    status or display_type, multiple values are combined with OR. title_keyword performs phrase-prefix
    matching against the coupon title. For full details about a specific coupon, use the Get Coupon API.

    Args:
        page_token (str | Unset):
        page_size (int | Unset):
        body (SearchCouponListRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchCouponListResponse]
     """


    kwargs = _get_kwargs(
        body=body,
page_token=page_token,
page_size=page_size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchCouponListRequest | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,

) -> SearchCouponListResponse | None:
    """ Search Coupon List

     Use this API to search coupons. Supported coupon creation sources include TikTok Shop Seller Center,
    the TikTok Seller App, and TikTok Shop CRM. Different supplied filters are combined with AND. Within
    status or display_type, multiple values are combined with OR. title_keyword performs phrase-prefix
    matching against the coupon title. For full details about a specific coupon, use the Get Coupon API.

    Args:
        page_token (str | Unset):
        page_size (int | Unset):
        body (SearchCouponListRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchCouponListResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
page_token=page_token,
page_size=page_size,

    )).parsed
