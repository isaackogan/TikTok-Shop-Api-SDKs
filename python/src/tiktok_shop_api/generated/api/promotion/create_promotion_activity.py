from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_promotion_activity_request import CreatePromotionActivityRequest
from ...models.create_promotion_activity_response import CreatePromotionActivityResponse
from typing import cast



def _get_kwargs(
    *,
    body: CreatePromotionActivityRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/promotion/202309/activities",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreatePromotionActivityResponse | None:
    if response.status_code == 200:
        response_200 = CreatePromotionActivityResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreatePromotionActivityResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreatePromotionActivityRequest,

) -> Response[CreatePromotionActivityResponse]:
    """ Create Promotion Activity

     Create a fixed-price, percentage-off, flash sale, shipping-discount, Buy More Save More, Gift With
    Purchase, or Buy X Get Y promotion activity. Coupons cannot be created with this API; create them in
    Seller Center or the seller app. To update the products or SKUs included in the activity, use
    [Update Activity Product](https://partner.tiktokshop.com/docv2/page/650d32c42aaa3602b86ccb5c).

    Args:
        body (CreatePromotionActivityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatePromotionActivityResponse]
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
    body: CreatePromotionActivityRequest,

) -> CreatePromotionActivityResponse | None:
    """ Create Promotion Activity

     Create a fixed-price, percentage-off, flash sale, shipping-discount, Buy More Save More, Gift With
    Purchase, or Buy X Get Y promotion activity. Coupons cannot be created with this API; create them in
    Seller Center or the seller app. To update the products or SKUs included in the activity, use
    [Update Activity Product](https://partner.tiktokshop.com/docv2/page/650d32c42aaa3602b86ccb5c).

    Args:
        body (CreatePromotionActivityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatePromotionActivityResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreatePromotionActivityRequest,

) -> Response[CreatePromotionActivityResponse]:
    """ Create Promotion Activity

     Create a fixed-price, percentage-off, flash sale, shipping-discount, Buy More Save More, Gift With
    Purchase, or Buy X Get Y promotion activity. Coupons cannot be created with this API; create them in
    Seller Center or the seller app. To update the products or SKUs included in the activity, use
    [Update Activity Product](https://partner.tiktokshop.com/docv2/page/650d32c42aaa3602b86ccb5c).

    Args:
        body (CreatePromotionActivityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatePromotionActivityResponse]
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
    body: CreatePromotionActivityRequest,

) -> CreatePromotionActivityResponse | None:
    """ Create Promotion Activity

     Create a fixed-price, percentage-off, flash sale, shipping-discount, Buy More Save More, Gift With
    Purchase, or Buy X Get Y promotion activity. Coupons cannot be created with this API; create them in
    Seller Center or the seller app. To update the products or SKUs included in the activity, use
    [Update Activity Product](https://partner.tiktokshop.com/docv2/page/650d32c42aaa3602b86ccb5c).

    Args:
        body (CreatePromotionActivityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatePromotionActivityResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
