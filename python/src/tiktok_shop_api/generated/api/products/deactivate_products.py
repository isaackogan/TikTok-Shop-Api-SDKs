from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deactivate_products_request import DeactivateProductsRequest
from ...models.deactivate_products_response import DeactivateProductsResponse
from ...types import Response


def _get_kwargs(
    *,
    body: DeactivateProductsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202309/products/deactivate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeactivateProductsResponse | None:
    if response.status_code == 200:
        response_200 = DeactivateProductsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeactivateProductsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeactivateProductsRequest,
) -> Response[DeactivateProductsResponse]:
    """Deactivate Products

     Deactivate products that are in the `Activate` status and hide them from buyers. The status changes
    to `Seller_deactivated` after deactivation.
    In the event there's some issue with a product (e.g. out of stock), you can deactivate the product
    and hide it temporarily from buyers. When the issues are resolved, you can activate the product
    again by using the [Activate Product
    API](https://partner.tiktokshop.com/docv2/page/650306ff5a12ff0294eab4a9).

    Args:
        body (DeactivateProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeactivateProductsResponse]
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
    body: DeactivateProductsRequest,
) -> DeactivateProductsResponse | None:
    """Deactivate Products

     Deactivate products that are in the `Activate` status and hide them from buyers. The status changes
    to `Seller_deactivated` after deactivation.
    In the event there's some issue with a product (e.g. out of stock), you can deactivate the product
    and hide it temporarily from buyers. When the issues are resolved, you can activate the product
    again by using the [Activate Product
    API](https://partner.tiktokshop.com/docv2/page/650306ff5a12ff0294eab4a9).

    Args:
        body (DeactivateProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeactivateProductsResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeactivateProductsRequest,
) -> Response[DeactivateProductsResponse]:
    """Deactivate Products

     Deactivate products that are in the `Activate` status and hide them from buyers. The status changes
    to `Seller_deactivated` after deactivation.
    In the event there's some issue with a product (e.g. out of stock), you can deactivate the product
    and hide it temporarily from buyers. When the issues are resolved, you can activate the product
    again by using the [Activate Product
    API](https://partner.tiktokshop.com/docv2/page/650306ff5a12ff0294eab4a9).

    Args:
        body (DeactivateProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeactivateProductsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DeactivateProductsRequest,
) -> DeactivateProductsResponse | None:
    """Deactivate Products

     Deactivate products that are in the `Activate` status and hide them from buyers. The status changes
    to `Seller_deactivated` after deactivation.
    In the event there's some issue with a product (e.g. out of stock), you can deactivate the product
    and hide it temporarily from buyers. When the issues are resolved, you can activate the product
    again by using the [Activate Product
    API](https://partner.tiktokshop.com/docv2/page/650306ff5a12ff0294eab4a9).

    Args:
        body (DeactivateProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeactivateProductsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
