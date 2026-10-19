from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_size_chart_request import CreateSizeChartRequest
from ...models.create_size_chart_response import CreateSizeChartResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateSizeChartRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202608/size_charts",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateSizeChartResponse | None:
    if response.status_code == 200:
        response_200 = CreateSizeChartResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateSizeChartResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSizeChartRequest,
) -> Response[CreateSizeChartResponse]:
    """Create Size Chart

     Create one size chart from structured table data. Use `REUSABLE_TEMPLATE` to create a seller
    template that can be reused across products, or `PRODUCT_SCOPED` to create a chart for a single
    product. The response returns the created size chart ID.

    Args:
        body (CreateSizeChartRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSizeChartResponse]
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
    body: CreateSizeChartRequest,
) -> CreateSizeChartResponse | None:
    """Create Size Chart

     Create one size chart from structured table data. Use `REUSABLE_TEMPLATE` to create a seller
    template that can be reused across products, or `PRODUCT_SCOPED` to create a chart for a single
    product. The response returns the created size chart ID.

    Args:
        body (CreateSizeChartRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSizeChartResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSizeChartRequest,
) -> Response[CreateSizeChartResponse]:
    """Create Size Chart

     Create one size chart from structured table data. Use `REUSABLE_TEMPLATE` to create a seller
    template that can be reused across products, or `PRODUCT_SCOPED` to create a chart for a single
    product. The response returns the created size chart ID.

    Args:
        body (CreateSizeChartRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSizeChartResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSizeChartRequest,
) -> CreateSizeChartResponse | None:
    """Create Size Chart

     Create one size chart from structured table data. Use `REUSABLE_TEMPLATE` to create a seller
    template that can be reused across products, or `PRODUCT_SCOPED` to create a chart for a single
    product. The response returns the created size chart ID.

    Args:
        body (CreateSizeChartRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSizeChartResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
