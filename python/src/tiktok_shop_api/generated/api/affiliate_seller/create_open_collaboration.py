from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_open_collaboration_request import CreateOpenCollaborationRequest
from ...models.create_open_collaboration_response import CreateOpenCollaborationResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateOpenCollaborationRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_seller/202412/open_collaborations",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateOpenCollaborationResponse | None:
    if response.status_code == 200:
        response_200 = CreateOpenCollaborationResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateOpenCollaborationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateOpenCollaborationRequest,
) -> Response[CreateOpenCollaborationResponse]:
    """Create Open Collaboration

     This API allows the seller to create an open collaboration. You create an open collaboration by
    selecting products and setting a commission rate.

    Args:
        body (CreateOpenCollaborationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOpenCollaborationResponse]
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
    body: CreateOpenCollaborationRequest,
) -> CreateOpenCollaborationResponse | None:
    """Create Open Collaboration

     This API allows the seller to create an open collaboration. You create an open collaboration by
    selecting products and setting a commission rate.

    Args:
        body (CreateOpenCollaborationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOpenCollaborationResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateOpenCollaborationRequest,
) -> Response[CreateOpenCollaborationResponse]:
    """Create Open Collaboration

     This API allows the seller to create an open collaboration. You create an open collaboration by
    selecting products and setting a commission rate.

    Args:
        body (CreateOpenCollaborationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOpenCollaborationResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateOpenCollaborationRequest,
) -> CreateOpenCollaborationResponse | None:
    """Create Open Collaboration

     This API allows the seller to create an open collaboration. You create an open collaboration by
    selecting products and setting a commission rate.

    Args:
        body (CreateOpenCollaborationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOpenCollaborationResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
