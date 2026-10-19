from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_target_collaboration_request import CreateTargetCollaborationRequest
from ...models.create_target_collaboration_response import CreateTargetCollaborationResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateTargetCollaborationRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_seller/202508/target_collaborations",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateTargetCollaborationResponse | None:
    if response.status_code == 200:
        response_200 = CreateTargetCollaborationResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateTargetCollaborationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateTargetCollaborationRequest,
) -> Response[CreateTargetCollaborationResponse]:
    """Create Target Collaboration

     This API is used to create a target collaboration.
    A target collaboration is a collaboration between a seller selected set of products (including a
    commission payout) and a set of creators the seller has added (invited) to the collaboration. Target
    collaborations are private and not visible in the Creator Marketplace to all creators; they are only
    visible to those that have been added to the collaboration.

    Args:
        body (CreateTargetCollaborationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateTargetCollaborationResponse]
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
    body: CreateTargetCollaborationRequest,
) -> CreateTargetCollaborationResponse | None:
    """Create Target Collaboration

     This API is used to create a target collaboration.
    A target collaboration is a collaboration between a seller selected set of products (including a
    commission payout) and a set of creators the seller has added (invited) to the collaboration. Target
    collaborations are private and not visible in the Creator Marketplace to all creators; they are only
    visible to those that have been added to the collaboration.

    Args:
        body (CreateTargetCollaborationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateTargetCollaborationResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateTargetCollaborationRequest,
) -> Response[CreateTargetCollaborationResponse]:
    """Create Target Collaboration

     This API is used to create a target collaboration.
    A target collaboration is a collaboration between a seller selected set of products (including a
    commission payout) and a set of creators the seller has added (invited) to the collaboration. Target
    collaborations are private and not visible in the Creator Marketplace to all creators; they are only
    visible to those that have been added to the collaboration.

    Args:
        body (CreateTargetCollaborationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateTargetCollaborationResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateTargetCollaborationRequest,
) -> CreateTargetCollaborationResponse | None:
    """Create Target Collaboration

     This API is used to create a target collaboration.
    A target collaboration is a collaboration between a seller selected set of products (including a
    commission payout) and a set of creators the seller has added (invited) to the collaboration. Target
    collaborations are private and not visible in the Creator Marketplace to all creators; they are only
    visible to those that have been added to the collaboration.

    Args:
        body (CreateTargetCollaborationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateTargetCollaborationResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
