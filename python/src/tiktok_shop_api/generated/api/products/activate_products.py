from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activate_products_request import ActivateProductsRequest
from ...models.activate_products_response import ActivateProductsResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ActivateProductsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202309/products/activate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActivateProductsResponse | None:
    if response.status_code == 200:
        response_200 = ActivateProductsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ActivateProductsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ActivateProductsRequest,
) -> Response[ActivateProductsResponse]:
    """Activate Products

     Activate hidden products that are in the `Seller_deactivated` or `Platform_deactivated` status and
    display them in the TikTok Shop catalog.
    After submitting the activation request, the products will be sent to TikTok Shop for auditing and
    their status will change to `Pending`. If a product passes the audit, its status will change back to
    `Activate`. You can use the [Product status change
    webhook](https://partner.tiktokshop.com/docv2/page/650956aff1fd3102b90b6261) to monitor the audit
    status.

    Args:
        body (ActivateProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivateProductsResponse]
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
    body: ActivateProductsRequest,
) -> ActivateProductsResponse | None:
    """Activate Products

     Activate hidden products that are in the `Seller_deactivated` or `Platform_deactivated` status and
    display them in the TikTok Shop catalog.
    After submitting the activation request, the products will be sent to TikTok Shop for auditing and
    their status will change to `Pending`. If a product passes the audit, its status will change back to
    `Activate`. You can use the [Product status change
    webhook](https://partner.tiktokshop.com/docv2/page/650956aff1fd3102b90b6261) to monitor the audit
    status.

    Args:
        body (ActivateProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivateProductsResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ActivateProductsRequest,
) -> Response[ActivateProductsResponse]:
    """Activate Products

     Activate hidden products that are in the `Seller_deactivated` or `Platform_deactivated` status and
    display them in the TikTok Shop catalog.
    After submitting the activation request, the products will be sent to TikTok Shop for auditing and
    their status will change to `Pending`. If a product passes the audit, its status will change back to
    `Activate`. You can use the [Product status change
    webhook](https://partner.tiktokshop.com/docv2/page/650956aff1fd3102b90b6261) to monitor the audit
    status.

    Args:
        body (ActivateProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivateProductsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ActivateProductsRequest,
) -> ActivateProductsResponse | None:
    """Activate Products

     Activate hidden products that are in the `Seller_deactivated` or `Platform_deactivated` status and
    display them in the TikTok Shop catalog.
    After submitting the activation request, the products will be sent to TikTok Shop for auditing and
    their status will change to `Pending`. If a product passes the audit, its status will change back to
    `Activate`. You can use the [Product status change
    webhook](https://partner.tiktokshop.com/docv2/page/650956aff1fd3102b90b6261) to monitor the audit
    status.

    Args:
        body (ActivateProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivateProductsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
