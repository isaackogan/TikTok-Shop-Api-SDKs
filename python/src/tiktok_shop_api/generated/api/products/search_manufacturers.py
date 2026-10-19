from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_manufacturers_request import SearchManufacturersRequest
from ...models.search_manufacturers_response import SearchManufacturersResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SearchManufacturersRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["page_size"] = page_size

    params["page_token"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202501/compliance/manufacturers/search",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SearchManufacturersResponse | None:
    if response.status_code == 200:
        response_200 = SearchManufacturersResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SearchManufacturersResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchManufacturersRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,
) -> Response[SearchManufacturersResponse]:
    """Search Manufacturers

     Retrieve a list of manufacturers in the EU languages supported by TikTok Shop based on their IDs or
    keyword.
    When creating a product with the [Create Product
    API](https://partner.tiktokshop.com/docv2/page/6502fc8da57708028b42b18a), pass a returned
    manufacturer's `id` as an element of `manufacturer_ids`.
    Target seller: Local sellers operating in EU countries

    Args:
        page_size (int):
        page_token (str | Unset):
        body (SearchManufacturersRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchManufacturersResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        page_size=page_size,
        page_token=page_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SearchManufacturersRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,
) -> SearchManufacturersResponse | None:
    """Search Manufacturers

     Retrieve a list of manufacturers in the EU languages supported by TikTok Shop based on their IDs or
    keyword.
    When creating a product with the [Create Product
    API](https://partner.tiktokshop.com/docv2/page/6502fc8da57708028b42b18a), pass a returned
    manufacturer's `id` as an element of `manufacturer_ids`.
    Target seller: Local sellers operating in EU countries

    Args:
        page_size (int):
        page_token (str | Unset):
        body (SearchManufacturersRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchManufacturersResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        page_size=page_size,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchManufacturersRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,
) -> Response[SearchManufacturersResponse]:
    """Search Manufacturers

     Retrieve a list of manufacturers in the EU languages supported by TikTok Shop based on their IDs or
    keyword.
    When creating a product with the [Create Product
    API](https://partner.tiktokshop.com/docv2/page/6502fc8da57708028b42b18a), pass a returned
    manufacturer's `id` as an element of `manufacturer_ids`.
    Target seller: Local sellers operating in EU countries

    Args:
        page_size (int):
        page_token (str | Unset):
        body (SearchManufacturersRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchManufacturersResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        page_size=page_size,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchManufacturersRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,
) -> SearchManufacturersResponse | None:
    """Search Manufacturers

     Retrieve a list of manufacturers in the EU languages supported by TikTok Shop based on their IDs or
    keyword.
    When creating a product with the [Create Product
    API](https://partner.tiktokshop.com/docv2/page/6502fc8da57708028b42b18a), pass a returned
    manufacturer's `id` as an element of `manufacturer_ids`.
    Target seller: Local sellers operating in EU countries

    Args:
        page_size (int):
        page_token (str | Unset):
        body (SearchManufacturersRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchManufacturersResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            page_size=page_size,
            page_token=page_token,
        )
    ).parsed
