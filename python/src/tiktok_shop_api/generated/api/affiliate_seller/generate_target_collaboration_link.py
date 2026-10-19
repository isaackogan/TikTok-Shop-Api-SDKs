from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.generate_target_collaboration_link_request import GenerateTargetCollaborationLinkRequest
from ...models.generate_target_collaboration_link_response import GenerateTargetCollaborationLinkResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    target_collaboration_id: str,
    *,
    body: GenerateTargetCollaborationLinkRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_seller/202509/target_collaboration/{target_collaboration_id}/link".format(
            target_collaboration_id=quote(str(target_collaboration_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GenerateTargetCollaborationLinkResponse | None:
    if response.status_code == 200:
        response_200 = GenerateTargetCollaborationLinkResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GenerateTargetCollaborationLinkResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    target_collaboration_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GenerateTargetCollaborationLinkRequest | Unset = UNSET,
) -> Response[GenerateTargetCollaborationLinkResponse]:
    """Generate Target Collaboration Link

     Generate a Target Collaboration Link that the seller can share with the creator. This link directs
    the creator to a guided flow to review details and formally accept the target collaboration

    Args:
        target_collaboration_id (str):
        body (GenerateTargetCollaborationLinkRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenerateTargetCollaborationLinkResponse]
    """

    kwargs = _get_kwargs(
        target_collaboration_id=target_collaboration_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    target_collaboration_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GenerateTargetCollaborationLinkRequest | Unset = UNSET,
) -> GenerateTargetCollaborationLinkResponse | None:
    """Generate Target Collaboration Link

     Generate a Target Collaboration Link that the seller can share with the creator. This link directs
    the creator to a guided flow to review details and formally accept the target collaboration

    Args:
        target_collaboration_id (str):
        body (GenerateTargetCollaborationLinkRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenerateTargetCollaborationLinkResponse
    """

    return sync_detailed(
        target_collaboration_id=target_collaboration_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    target_collaboration_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GenerateTargetCollaborationLinkRequest | Unset = UNSET,
) -> Response[GenerateTargetCollaborationLinkResponse]:
    """Generate Target Collaboration Link

     Generate a Target Collaboration Link that the seller can share with the creator. This link directs
    the creator to a guided flow to review details and formally accept the target collaboration

    Args:
        target_collaboration_id (str):
        body (GenerateTargetCollaborationLinkRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenerateTargetCollaborationLinkResponse]
    """

    kwargs = _get_kwargs(
        target_collaboration_id=target_collaboration_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    target_collaboration_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GenerateTargetCollaborationLinkRequest | Unset = UNSET,
) -> GenerateTargetCollaborationLinkResponse | None:
    """Generate Target Collaboration Link

     Generate a Target Collaboration Link that the seller can share with the creator. This link directs
    the creator to a guided flow to review details and formally accept the target collaboration

    Args:
        target_collaboration_id (str):
        body (GenerateTargetCollaborationLinkRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenerateTargetCollaborationLinkResponse
    """

    return (
        await asyncio_detailed(
            target_collaboration_id=target_collaboration_id,
            client=client,
            body=body,
        )
    ).parsed
