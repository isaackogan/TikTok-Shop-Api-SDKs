from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_first_mile_bundle_request import CreateFirstMileBundleRequest
from ...models.create_first_mile_bundle_response import CreateFirstMileBundleResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateFirstMileBundleRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fulfillment/202407/bundles",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateFirstMileBundleResponse | None:
    if response.status_code == 200:
        response_200 = CreateFirstMileBundleResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateFirstMileBundleResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateFirstMileBundleRequest,
) -> Response[CreateFirstMileBundleResponse]:
    """Create First Mile Bundle

     If you send multiple packages to TikTok Shop warehouse in a single first-mile bundle, you can use
    the API to create a first-mile bundle on TikTok Shop and get the bundle ID.

    Args:
        body (CreateFirstMileBundleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateFirstMileBundleResponse]
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
    body: CreateFirstMileBundleRequest,
) -> CreateFirstMileBundleResponse | None:
    """Create First Mile Bundle

     If you send multiple packages to TikTok Shop warehouse in a single first-mile bundle, you can use
    the API to create a first-mile bundle on TikTok Shop and get the bundle ID.

    Args:
        body (CreateFirstMileBundleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateFirstMileBundleResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateFirstMileBundleRequest,
) -> Response[CreateFirstMileBundleResponse]:
    """Create First Mile Bundle

     If you send multiple packages to TikTok Shop warehouse in a single first-mile bundle, you can use
    the API to create a first-mile bundle on TikTok Shop and get the bundle ID.

    Args:
        body (CreateFirstMileBundleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateFirstMileBundleResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateFirstMileBundleRequest,
) -> CreateFirstMileBundleResponse | None:
    """Create First Mile Bundle

     If you send multiple packages to TikTok Shop warehouse in a single first-mile bundle, you can use
    the API to create a first-mile bundle on TikTok Shop and get the bundle ID.

    Args:
        body (CreateFirstMileBundleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateFirstMileBundleResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
