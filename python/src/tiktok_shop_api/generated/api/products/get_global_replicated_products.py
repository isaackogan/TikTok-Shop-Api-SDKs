from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_global_replicated_products_response import GetGlobalReplicatedProductsResponse
from ...types import Response


def _get_kwargs(
    product_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/product/202507/products/{product_id}/replicated_products".format(
            product_id=quote(str(product_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetGlobalReplicatedProductsResponse | None:
    if response.status_code == 200:
        response_200 = GetGlobalReplicatedProductsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetGlobalReplicatedProductsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetGlobalReplicatedProductsResponse]:
    """Get Global Replicated Products

     Retrieves the globally associated replicas in other markets if the product has been replicated
    through local replication.
    Applicable only for global sellers.

    Args:
        product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGlobalReplicatedProductsResponse]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetGlobalReplicatedProductsResponse | None:
    """Get Global Replicated Products

     Retrieves the globally associated replicas in other markets if the product has been replicated
    through local replication.
    Applicable only for global sellers.

    Args:
        product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGlobalReplicatedProductsResponse
    """

    return sync_detailed(
        product_id=product_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetGlobalReplicatedProductsResponse]:
    """Get Global Replicated Products

     Retrieves the globally associated replicas in other markets if the product has been replicated
    through local replication.
    Applicable only for global sellers.

    Args:
        product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGlobalReplicatedProductsResponse]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetGlobalReplicatedProductsResponse | None:
    """Get Global Replicated Products

     Retrieves the globally associated replicas in other markets if the product has been replicated
    through local replication.
    Applicable only for global sellers.

    Args:
        product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGlobalReplicatedProductsResponse
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            client=client,
        )
    ).parsed
