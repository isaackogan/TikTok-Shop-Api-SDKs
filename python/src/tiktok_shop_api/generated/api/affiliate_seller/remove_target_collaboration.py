from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.remove_target_collaboration_request import RemoveTargetCollaborationRequest
from ...models.remove_target_collaboration_response import RemoveTargetCollaborationResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    target_collaboration_id: str,
    *,
    body: RemoveTargetCollaborationRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/affiliate_seller/202409/target_collaborations/{target_collaboration_id}".format(target_collaboration_id=quote(str(target_collaboration_id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RemoveTargetCollaborationResponse | None:
    if response.status_code == 200:
        response_200 = RemoveTargetCollaborationResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RemoveTargetCollaborationResponse]:
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
    body: RemoveTargetCollaborationRequest | Unset = UNSET,

) -> Response[RemoveTargetCollaborationResponse]:
    """ Remove Target Collaboration

     This API is used by Seller to remove affiliate target collaboration.

    Args:
        target_collaboration_id (str):
        body (RemoveTargetCollaborationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveTargetCollaborationResponse]
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
    body: RemoveTargetCollaborationRequest | Unset = UNSET,

) -> RemoveTargetCollaborationResponse | None:
    """ Remove Target Collaboration

     This API is used by Seller to remove affiliate target collaboration.

    Args:
        target_collaboration_id (str):
        body (RemoveTargetCollaborationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveTargetCollaborationResponse
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
    body: RemoveTargetCollaborationRequest | Unset = UNSET,

) -> Response[RemoveTargetCollaborationResponse]:
    """ Remove Target Collaboration

     This API is used by Seller to remove affiliate target collaboration.

    Args:
        target_collaboration_id (str):
        body (RemoveTargetCollaborationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveTargetCollaborationResponse]
     """


    kwargs = _get_kwargs(
        target_collaboration_id=target_collaboration_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    target_collaboration_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RemoveTargetCollaborationRequest | Unset = UNSET,

) -> RemoveTargetCollaborationResponse | None:
    """ Remove Target Collaboration

     This API is used by Seller to remove affiliate target collaboration.

    Args:
        target_collaboration_id (str):
        body (RemoveTargetCollaborationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveTargetCollaborationResponse
     """


    return (await asyncio_detailed(
        target_collaboration_id=target_collaboration_id,
client=client,
body=body,

    )).parsed
