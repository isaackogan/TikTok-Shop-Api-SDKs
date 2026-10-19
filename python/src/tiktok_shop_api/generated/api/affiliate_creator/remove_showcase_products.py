from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remove_showcase_products_request import RemoveShowcaseProductsRequest
from ...models.remove_showcase_products_response import RemoveShowcaseProductsResponse
from ...types import Response


def _get_kwargs(
    *,
    body: RemoveShowcaseProductsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/affiliate_creator/202409/showcases/products",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RemoveShowcaseProductsResponse | None:
    if response.status_code == 200:
        response_200 = RemoveShowcaseProductsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RemoveShowcaseProductsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RemoveShowcaseProductsRequest,
) -> Response[RemoveShowcaseProductsResponse]:
    """Remove Showcase Products

     This API removes the products in the creator's showcase.
    The platform will return error code and error message if the deletion fails.

    Args:
        body (RemoveShowcaseProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveShowcaseProductsResponse]
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
    body: RemoveShowcaseProductsRequest,
) -> RemoveShowcaseProductsResponse | None:
    """Remove Showcase Products

     This API removes the products in the creator's showcase.
    The platform will return error code and error message if the deletion fails.

    Args:
        body (RemoveShowcaseProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveShowcaseProductsResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RemoveShowcaseProductsRequest,
) -> Response[RemoveShowcaseProductsResponse]:
    """Remove Showcase Products

     This API removes the products in the creator's showcase.
    The platform will return error code and error message if the deletion fails.

    Args:
        body (RemoveShowcaseProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveShowcaseProductsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RemoveShowcaseProductsRequest,
) -> RemoveShowcaseProductsResponse | None:
    """Remove Showcase Products

     This API removes the products in the creator's showcase.
    The platform will return error code and error message if the deletion fails.

    Args:
        body (RemoveShowcaseProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveShowcaseProductsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
