from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_global_product_response import GetGlobalProductResponse
from ...types import Response


def _get_kwargs(
    global_product_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/product/202309/global_products/{global_product_id}".format(
            global_product_id=quote(str(global_product_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetGlobalProductResponse | None:
    if response.status_code == 200:
        response_200 = GetGlobalProductResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetGlobalProductResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    global_product_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetGlobalProductResponse]:
    """Get Global Product

     Retrieve all properties of a global product that is in the "DRAFT", "UNPUBLISHED", or "PUBLISHED"
    status, and the corresponding local product IDs in the published markets.

    Args:
        global_product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGlobalProductResponse]
    """

    kwargs = _get_kwargs(
        global_product_id=global_product_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    global_product_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetGlobalProductResponse | None:
    """Get Global Product

     Retrieve all properties of a global product that is in the "DRAFT", "UNPUBLISHED", or "PUBLISHED"
    status, and the corresponding local product IDs in the published markets.

    Args:
        global_product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGlobalProductResponse
    """

    return sync_detailed(
        global_product_id=global_product_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    global_product_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetGlobalProductResponse]:
    """Get Global Product

     Retrieve all properties of a global product that is in the "DRAFT", "UNPUBLISHED", or "PUBLISHED"
    status, and the corresponding local product IDs in the published markets.

    Args:
        global_product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGlobalProductResponse]
    """

    kwargs = _get_kwargs(
        global_product_id=global_product_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    global_product_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetGlobalProductResponse | None:
    """Get Global Product

     Retrieve all properties of a global product that is in the "DRAFT", "UNPUBLISHED", or "PUBLISHED"
    status, and the corresponding local product IDs in the published markets.

    Args:
        global_product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGlobalProductResponse
    """

    return (
        await asyncio_detailed(
            global_product_id=global_product_id,
            client=client,
        )
    ).parsed
