from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_products_seo_words_response import GetProductsSEOWordsResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    product_ids: list[str],
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_product_ids = product_ids

    params["product_ids"] = json_product_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/product/202405/products/seo_words",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetProductsSEOWordsResponse | None:
    if response.status_code == 200:
        response_200 = GetProductsSEOWordsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetProductsSEOWordsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    product_ids: list[str],
) -> Response[GetProductsSEOWordsResponse]:
    """Get Products SEO Words

     Obtain SEO suggestions for product titles of live products (status: `ACTIVATE`) to enhance product
    visibility.
    Applicable only for the US, UK, and SEA markets.

    Args:
        product_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProductsSEOWordsResponse]
    """

    kwargs = _get_kwargs(
        product_ids=product_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    product_ids: list[str],
) -> GetProductsSEOWordsResponse | None:
    """Get Products SEO Words

     Obtain SEO suggestions for product titles of live products (status: `ACTIVATE`) to enhance product
    visibility.
    Applicable only for the US, UK, and SEA markets.

    Args:
        product_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProductsSEOWordsResponse
    """

    return sync_detailed(
        client=client,
        product_ids=product_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    product_ids: list[str],
) -> Response[GetProductsSEOWordsResponse]:
    """Get Products SEO Words

     Obtain SEO suggestions for product titles of live products (status: `ACTIVATE`) to enhance product
    visibility.
    Applicable only for the US, UK, and SEA markets.

    Args:
        product_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProductsSEOWordsResponse]
    """

    kwargs = _get_kwargs(
        product_ids=product_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    product_ids: list[str],
) -> GetProductsSEOWordsResponse | None:
    """Get Products SEO Words

     Obtain SEO suggestions for product titles of live products (status: `ACTIVATE`) to enhance product
    visibility.
    Applicable only for the US, UK, and SEA markets.

    Args:
        product_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProductsSEOWordsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            product_ids=product_ids,
        )
    ).parsed
