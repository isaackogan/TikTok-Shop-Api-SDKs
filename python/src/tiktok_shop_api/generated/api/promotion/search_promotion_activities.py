from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.search_promotion_activities_request import SearchPromotionActivitiesRequest
from ...models.search_promotion_activities_response import SearchPromotionActivitiesResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: SearchPromotionActivitiesRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/promotion/202309/activities/search",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchPromotionActivitiesResponse | None:
    if response.status_code == 200:
        response_200 = SearchPromotionActivitiesResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SearchPromotionActivitiesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchPromotionActivitiesRequest | Unset = UNSET,

) -> Response[SearchPromotionActivitiesResponse]:
    """ Search Promotion Activities

     Search product discount, flash sale, shipping discount, Buy More Save More, Gift With Purchase, and
    Buy X Get Y promotion activities. For coupon activities, use [Search
    Coupons](https://partner.tiktokshop.com/docv2/page/6699dcdf115ebe02f841e4cd).

    Args:
        body (SearchPromotionActivitiesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchPromotionActivitiesResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SearchPromotionActivitiesRequest | Unset = UNSET,

) -> SearchPromotionActivitiesResponse | None:
    """ Search Promotion Activities

     Search product discount, flash sale, shipping discount, Buy More Save More, Gift With Purchase, and
    Buy X Get Y promotion activities. For coupon activities, use [Search
    Coupons](https://partner.tiktokshop.com/docv2/page/6699dcdf115ebe02f841e4cd).

    Args:
        body (SearchPromotionActivitiesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchPromotionActivitiesResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchPromotionActivitiesRequest | Unset = UNSET,

) -> Response[SearchPromotionActivitiesResponse]:
    """ Search Promotion Activities

     Search product discount, flash sale, shipping discount, Buy More Save More, Gift With Purchase, and
    Buy X Get Y promotion activities. For coupon activities, use [Search
    Coupons](https://partner.tiktokshop.com/docv2/page/6699dcdf115ebe02f841e4cd).

    Args:
        body (SearchPromotionActivitiesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchPromotionActivitiesResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchPromotionActivitiesRequest | Unset = UNSET,

) -> SearchPromotionActivitiesResponse | None:
    """ Search Promotion Activities

     Search product discount, flash sale, shipping discount, Buy More Save More, Gift With Purchase, and
    Buy X Get Y promotion activities. For coupon activities, use [Search
    Coupons](https://partner.tiktokshop.com/docv2/page/6699dcdf115ebe02f841e4cd).

    Args:
        body (SearchPromotionActivitiesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchPromotionActivitiesResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
