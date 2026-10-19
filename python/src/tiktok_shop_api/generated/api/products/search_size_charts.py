from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_size_charts_locales_item import SearchSizeChartsLocalesItem
from ...models.search_size_charts_request import SearchSizeChartsRequest
from ...models.search_size_charts_response import SearchSizeChartsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SearchSizeChartsRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,
    locales: list[SearchSizeChartsLocalesItem] | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["page_size"] = page_size

    params["page_token"] = page_token

    json_locales: list[str] | Unset = UNSET
    if not isinstance(locales, Unset):
        json_locales = []
        for locales_item_data in locales:
            locales_item = locales_item_data.value
            json_locales.append(locales_item)

    params["locales"] = json_locales

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202407/sizecharts/search",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SearchSizeChartsResponse | None:
    if response.status_code == 200:
        response_200 = SearchSizeChartsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SearchSizeChartsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchSizeChartsRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,
    locales: list[SearchSizeChartsLocalesItem] | Unset = UNSET,
) -> Response[SearchSizeChartsResponse]:
    """Search Size Charts

     Retrieve size charts that a seller has created.

    Args:
        page_size (int):
        page_token (str | Unset):
        locales (list[SearchSizeChartsLocalesItem] | Unset):
        body (SearchSizeChartsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchSizeChartsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        page_size=page_size,
        page_token=page_token,
        locales=locales,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SearchSizeChartsRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,
    locales: list[SearchSizeChartsLocalesItem] | Unset = UNSET,
) -> SearchSizeChartsResponse | None:
    """Search Size Charts

     Retrieve size charts that a seller has created.

    Args:
        page_size (int):
        page_token (str | Unset):
        locales (list[SearchSizeChartsLocalesItem] | Unset):
        body (SearchSizeChartsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchSizeChartsResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        page_size=page_size,
        page_token=page_token,
        locales=locales,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchSizeChartsRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,
    locales: list[SearchSizeChartsLocalesItem] | Unset = UNSET,
) -> Response[SearchSizeChartsResponse]:
    """Search Size Charts

     Retrieve size charts that a seller has created.

    Args:
        page_size (int):
        page_token (str | Unset):
        locales (list[SearchSizeChartsLocalesItem] | Unset):
        body (SearchSizeChartsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchSizeChartsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        page_size=page_size,
        page_token=page_token,
        locales=locales,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchSizeChartsRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,
    locales: list[SearchSizeChartsLocalesItem] | Unset = UNSET,
) -> SearchSizeChartsResponse | None:
    """Search Size Charts

     Retrieve size charts that a seller has created.

    Args:
        page_size (int):
        page_token (str | Unset):
        locales (list[SearchSizeChartsLocalesItem] | Unset):
        body (SearchSizeChartsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchSizeChartsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            page_size=page_size,
            page_token=page_token,
            locales=locales,
        )
    ).parsed
