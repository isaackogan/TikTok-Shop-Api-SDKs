from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_manufacturer_request import CreateManufacturerRequest
from ...models.create_manufacturer_response import CreateManufacturerResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateManufacturerRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202409/compliance/manufacturers",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateManufacturerResponse | None:
    if response.status_code == 200:
        response_200 = CreateManufacturerResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateManufacturerResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateManufacturerRequest,
) -> Response[CreateManufacturerResponse]:
    """Create Manufacturer

     Add a manufacturer for a seller. The provided information will be automatically translated into all
    EU languages supported by TikTok Shop.
    - Use the [Search Manufacturers API](67066a580dcee902fa03ccf9) to obtain the translations.
    - Use the [Partial Edit Manufacturer API](67066a55c55b3a03044eea29) to edit the translations, if
    necessary.
    - When creating a product, pass the returned `manufacturer_id` to associate the product with the
    manufacturer.
    Target seller: Local sellers operating in EU countries

    Args:
        body (CreateManufacturerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateManufacturerResponse]
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
    body: CreateManufacturerRequest,
) -> CreateManufacturerResponse | None:
    """Create Manufacturer

     Add a manufacturer for a seller. The provided information will be automatically translated into all
    EU languages supported by TikTok Shop.
    - Use the [Search Manufacturers API](67066a580dcee902fa03ccf9) to obtain the translations.
    - Use the [Partial Edit Manufacturer API](67066a55c55b3a03044eea29) to edit the translations, if
    necessary.
    - When creating a product, pass the returned `manufacturer_id` to associate the product with the
    manufacturer.
    Target seller: Local sellers operating in EU countries

    Args:
        body (CreateManufacturerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateManufacturerResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateManufacturerRequest,
) -> Response[CreateManufacturerResponse]:
    """Create Manufacturer

     Add a manufacturer for a seller. The provided information will be automatically translated into all
    EU languages supported by TikTok Shop.
    - Use the [Search Manufacturers API](67066a580dcee902fa03ccf9) to obtain the translations.
    - Use the [Partial Edit Manufacturer API](67066a55c55b3a03044eea29) to edit the translations, if
    necessary.
    - When creating a product, pass the returned `manufacturer_id` to associate the product with the
    manufacturer.
    Target seller: Local sellers operating in EU countries

    Args:
        body (CreateManufacturerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateManufacturerResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateManufacturerRequest,
) -> CreateManufacturerResponse | None:
    """Create Manufacturer

     Add a manufacturer for a seller. The provided information will be automatically translated into all
    EU languages supported by TikTok Shop.
    - Use the [Search Manufacturers API](67066a580dcee902fa03ccf9) to obtain the translations.
    - Use the [Partial Edit Manufacturer API](67066a55c55b3a03044eea29) to edit the translations, if
    necessary.
    - When creating a product, pass the returned `manufacturer_id` to associate the product with the
    manufacturer.
    Target seller: Local sellers operating in EU countries

    Args:
        body (CreateManufacturerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateManufacturerResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
