from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remove_creator_from_open_collaboration_product_request import (
    RemoveCreatorFromOpenCollaborationProductRequest,
)
from ...models.remove_creator_from_open_collaboration_product_response import (
    RemoveCreatorFromOpenCollaborationProductResponse,
)
from ...types import Response


def _get_kwargs(
    open_collaboration_id: str,
    *,
    body: RemoveCreatorFromOpenCollaborationProductRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_seller/202508/open_collaborations/{open_collaboration_id}/remove_creator".format(
            open_collaboration_id=quote(str(open_collaboration_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RemoveCreatorFromOpenCollaborationProductResponse | None:
    if response.status_code == 200:
        response_200 = RemoveCreatorFromOpenCollaborationProductResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RemoveCreatorFromOpenCollaborationProductResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    open_collaboration_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RemoveCreatorFromOpenCollaborationProductRequest,
) -> Response[RemoveCreatorFromOpenCollaborationProductResponse]:
    """Remove Creator From Open Collaboration Product

     This API is used to remove creators from open collaboration. Please note, due to current platform
    design, creators can still rejoin an open collaboration after removal. Partners/Sellers can call
    this API again to remove the creator again.

    Args:
        open_collaboration_id (str):
        body (RemoveCreatorFromOpenCollaborationProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveCreatorFromOpenCollaborationProductResponse]
    """

    kwargs = _get_kwargs(
        open_collaboration_id=open_collaboration_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    open_collaboration_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RemoveCreatorFromOpenCollaborationProductRequest,
) -> RemoveCreatorFromOpenCollaborationProductResponse | None:
    """Remove Creator From Open Collaboration Product

     This API is used to remove creators from open collaboration. Please note, due to current platform
    design, creators can still rejoin an open collaboration after removal. Partners/Sellers can call
    this API again to remove the creator again.

    Args:
        open_collaboration_id (str):
        body (RemoveCreatorFromOpenCollaborationProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveCreatorFromOpenCollaborationProductResponse
    """

    return sync_detailed(
        open_collaboration_id=open_collaboration_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    open_collaboration_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RemoveCreatorFromOpenCollaborationProductRequest,
) -> Response[RemoveCreatorFromOpenCollaborationProductResponse]:
    """Remove Creator From Open Collaboration Product

     This API is used to remove creators from open collaboration. Please note, due to current platform
    design, creators can still rejoin an open collaboration after removal. Partners/Sellers can call
    this API again to remove the creator again.

    Args:
        open_collaboration_id (str):
        body (RemoveCreatorFromOpenCollaborationProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveCreatorFromOpenCollaborationProductResponse]
    """

    kwargs = _get_kwargs(
        open_collaboration_id=open_collaboration_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    open_collaboration_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RemoveCreatorFromOpenCollaborationProductRequest,
) -> RemoveCreatorFromOpenCollaborationProductResponse | None:
    """Remove Creator From Open Collaboration Product

     This API is used to remove creators from open collaboration. Please note, due to current platform
    design, creators can still rejoin an open collaboration after removal. Partners/Sellers can call
    this API again to remove the creator again.

    Args:
        open_collaboration_id (str):
        body (RemoveCreatorFromOpenCollaborationProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveCreatorFromOpenCollaborationProductResponse
    """

    return (
        await asyncio_detailed(
            open_collaboration_id=open_collaboration_id,
            client=client,
            body=body,
        )
    ).parsed
