from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_products_request import DeleteProductsRequest
from ...models.delete_products_response import DeleteProductsResponse
from ...types import Response


def _get_kwargs(
    *,
    body: DeleteProductsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/product/202309/products",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteProductsResponse | None:
    if response.status_code == 200:
        response_200 = DeleteProductsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeleteProductsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteProductsRequest,
) -> Response[DeleteProductsResponse]:
    """Delete Products

     Delete non-frozen products that you no longer need.
    **For the Indonesia market**: You can only delete products that are not frozen on all listing
    platforms. If the product is frozen on any platform, it cannot be deleted.

    Args:
        body (DeleteProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteProductsResponse]
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
    body: DeleteProductsRequest,
) -> DeleteProductsResponse | None:
    """Delete Products

     Delete non-frozen products that you no longer need.
    **For the Indonesia market**: You can only delete products that are not frozen on all listing
    platforms. If the product is frozen on any platform, it cannot be deleted.

    Args:
        body (DeleteProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteProductsResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteProductsRequest,
) -> Response[DeleteProductsResponse]:
    """Delete Products

     Delete non-frozen products that you no longer need.
    **For the Indonesia market**: You can only delete products that are not frozen on all listing
    platforms. If the product is frozen on any platform, it cannot be deleted.

    Args:
        body (DeleteProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteProductsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteProductsRequest,
) -> DeleteProductsResponse | None:
    """Delete Products

     Delete non-frozen products that you no longer need.
    **For the Indonesia market**: You can only delete products that are not frozen on all listing
    platforms. If the product is frozen on any platform, it cannot be deleted.

    Args:
        body (DeleteProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteProductsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
