from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mark_package_as_shipped_request import MarkPackageAsShippedRequest
from ...models.mark_package_as_shipped_response import MarkPackageAsShippedResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    order_id: str,
    *,
    body: MarkPackageAsShippedRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fulfillment/202610/orders/{order_id}/packages".format(order_id=quote(str(order_id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MarkPackageAsShippedResponse | None:
    if response.status_code == 200:
        response_200 = MarkPackageAsShippedResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MarkPackageAsShippedResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MarkPackageAsShippedRequest | Unset = UNSET,

) -> Response[MarkPackageAsShippedResponse]:
    """ Mark Package As Shipped

     **This API is currently exclusive to the following markets: US, UK, ES, IE, IT, DE, FR, JP.**
    This API is for sellers who fulfill orders through their own selected/preferred logistics carrier,
    and allows sellers to upload valid package information (items in packages, shipping provider
    information, and tracking number) orders/order line items to TikTok Shop. Use [Get Shipping
    Providers API](https://partner.tiktokshop.com/docv2/page/650aa48d4a0bb702c06d85cd?external_id=650aa4
    8d4a0bb702c06d85cd) to retrieve the `shipping_provider_id` for shipping providers.

    Args:
        order_id (str):
        body (MarkPackageAsShippedRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MarkPackageAsShippedResponse]
     """


    kwargs = _get_kwargs(
        order_id=order_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MarkPackageAsShippedRequest | Unset = UNSET,

) -> MarkPackageAsShippedResponse | None:
    """ Mark Package As Shipped

     **This API is currently exclusive to the following markets: US, UK, ES, IE, IT, DE, FR, JP.**
    This API is for sellers who fulfill orders through their own selected/preferred logistics carrier,
    and allows sellers to upload valid package information (items in packages, shipping provider
    information, and tracking number) orders/order line items to TikTok Shop. Use [Get Shipping
    Providers API](https://partner.tiktokshop.com/docv2/page/650aa48d4a0bb702c06d85cd?external_id=650aa4
    8d4a0bb702c06d85cd) to retrieve the `shipping_provider_id` for shipping providers.

    Args:
        order_id (str):
        body (MarkPackageAsShippedRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MarkPackageAsShippedResponse
     """


    return sync_detailed(
        order_id=order_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MarkPackageAsShippedRequest | Unset = UNSET,

) -> Response[MarkPackageAsShippedResponse]:
    """ Mark Package As Shipped

     **This API is currently exclusive to the following markets: US, UK, ES, IE, IT, DE, FR, JP.**
    This API is for sellers who fulfill orders through their own selected/preferred logistics carrier,
    and allows sellers to upload valid package information (items in packages, shipping provider
    information, and tracking number) orders/order line items to TikTok Shop. Use [Get Shipping
    Providers API](https://partner.tiktokshop.com/docv2/page/650aa48d4a0bb702c06d85cd?external_id=650aa4
    8d4a0bb702c06d85cd) to retrieve the `shipping_provider_id` for shipping providers.

    Args:
        order_id (str):
        body (MarkPackageAsShippedRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MarkPackageAsShippedResponse]
     """


    kwargs = _get_kwargs(
        order_id=order_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MarkPackageAsShippedRequest | Unset = UNSET,

) -> MarkPackageAsShippedResponse | None:
    """ Mark Package As Shipped

     **This API is currently exclusive to the following markets: US, UK, ES, IE, IT, DE, FR, JP.**
    This API is for sellers who fulfill orders through their own selected/preferred logistics carrier,
    and allows sellers to upload valid package information (items in packages, shipping provider
    information, and tracking number) orders/order line items to TikTok Shop. Use [Get Shipping
    Providers API](https://partner.tiktokshop.com/docv2/page/650aa48d4a0bb702c06d85cd?external_id=650aa4
    8d4a0bb702c06d85cd) to retrieve the `shipping_provider_id` for shipping providers.

    Args:
        order_id (str):
        body (MarkPackageAsShippedRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MarkPackageAsShippedResponse
     """


    return (await asyncio_detailed(
        order_id=order_id,
client=client,
body=body,

    )).parsed
