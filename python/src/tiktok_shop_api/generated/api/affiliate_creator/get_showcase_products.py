from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_showcase_products_response import GetShowcaseProductsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: int,
    page_token: str | Unset = UNSET,
    origin: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page_size"] = page_size

    params["page_token"] = page_token

    params["origin"] = origin

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/affiliate_creator/202405/showcases/products",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetShowcaseProductsResponse | None:
    if response.status_code == 200:
        response_200 = GetShowcaseProductsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetShowcaseProductsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_size: int,
    page_token: str | Unset = UNSET,
    origin: str,
) -> Response[GetShowcaseProductsResponse]:
    """Get Showcase Products

     This API lists the products in the creator's showcase, paginated by specified page size and iterated
    through pages by page token for up to 2000 products in the showcase. This API is generally used when
    a creator would like to view the products in the showcase.  The platform will return the product
    details in the showcase, as well as the products in the livebag if the creator is live streaming.

    Args:
        page_size (int):
        page_token (str | Unset):
        origin (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShowcaseProductsResponse]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page_token=page_token,
        origin=origin,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page_size: int,
    page_token: str | Unset = UNSET,
    origin: str,
) -> GetShowcaseProductsResponse | None:
    """Get Showcase Products

     This API lists the products in the creator's showcase, paginated by specified page size and iterated
    through pages by page token for up to 2000 products in the showcase. This API is generally used when
    a creator would like to view the products in the showcase.  The platform will return the product
    details in the showcase, as well as the products in the livebag if the creator is live streaming.

    Args:
        page_size (int):
        page_token (str | Unset):
        origin (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShowcaseProductsResponse
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        page_token=page_token,
        origin=origin,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_size: int,
    page_token: str | Unset = UNSET,
    origin: str,
) -> Response[GetShowcaseProductsResponse]:
    """Get Showcase Products

     This API lists the products in the creator's showcase, paginated by specified page size and iterated
    through pages by page token for up to 2000 products in the showcase. This API is generally used when
    a creator would like to view the products in the showcase.  The platform will return the product
    details in the showcase, as well as the products in the livebag if the creator is live streaming.

    Args:
        page_size (int):
        page_token (str | Unset):
        origin (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShowcaseProductsResponse]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page_token=page_token,
        origin=origin,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_size: int,
    page_token: str | Unset = UNSET,
    origin: str,
) -> GetShowcaseProductsResponse | None:
    """Get Showcase Products

     This API lists the products in the creator's showcase, paginated by specified page size and iterated
    through pages by page token for up to 2000 products in the showcase. This API is generally used when
    a creator would like to view the products in the showcase.  The platform will return the product
    details in the showcase, as well as the products in the livebag if the creator is live streaming.

    Args:
        page_size (int):
        page_token (str | Unset):
        origin (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShowcaseProductsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            page_token=page_token,
            origin=origin,
        )
    ).parsed
