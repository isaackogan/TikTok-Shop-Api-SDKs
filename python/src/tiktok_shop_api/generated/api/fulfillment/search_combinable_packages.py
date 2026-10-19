from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_combinable_packages_response import SearchCombinablePackagesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_token: str | Unset = UNSET,
    page_size: int,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page_token"] = page_token

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fulfillment/202309/combinable_packages/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SearchCombinablePackagesResponse | None:
    if response.status_code == 200:
        response_200 = SearchCombinablePackagesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SearchCombinablePackagesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    page_size: int,
) -> Response[SearchCombinablePackagesResponse]:
    """Search Combinable Packages

     Use this API to query orders eligible for combined shipping.

    Args:
        page_token (str | Unset):
        page_size (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchCombinablePackagesResponse]
    """

    kwargs = _get_kwargs(
        page_token=page_token,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    page_size: int,
) -> SearchCombinablePackagesResponse | None:
    """Search Combinable Packages

     Use this API to query orders eligible for combined shipping.

    Args:
        page_token (str | Unset):
        page_size (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchCombinablePackagesResponse
    """

    return sync_detailed(
        client=client,
        page_token=page_token,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    page_size: int,
) -> Response[SearchCombinablePackagesResponse]:
    """Search Combinable Packages

     Use this API to query orders eligible for combined shipping.

    Args:
        page_token (str | Unset):
        page_size (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchCombinablePackagesResponse]
    """

    kwargs = _get_kwargs(
        page_token=page_token,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    page_size: int,
) -> SearchCombinablePackagesResponse | None:
    """Search Combinable Packages

     Use this API to query orders eligible for combined shipping.

    Args:
        page_token (str | Unset):
        page_size (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchCombinablePackagesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            page_token=page_token,
            page_size=page_size,
        )
    ).parsed
