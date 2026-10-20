from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.update_target_collaboration_request import UpdateTargetCollaborationRequest
from ...models.update_target_collaboration_response import UpdateTargetCollaborationResponse
from typing import cast



def _get_kwargs(
    target_collaboration_id: str,
    *,
    body: UpdateTargetCollaborationRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/affiliate_seller/202508/target_collaborations/{target_collaboration_id}".format(target_collaboration_id=quote(str(target_collaboration_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UpdateTargetCollaborationResponse | None:
    if response.status_code == 200:
        response_200 = UpdateTargetCollaborationResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UpdateTargetCollaborationResponse]:
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
    body: UpdateTargetCollaborationRequest,

) -> Response[UpdateTargetCollaborationResponse]:
    """ Update Target Collaboration

     This API is used by sellers to update a STANDARD target collaboration. A successful response can
    still report creators or products that were not updated. Check `data.update_failed` and
    `data.target_collaboration_conflicts` before treating the update as complete.

    Args:
        target_collaboration_id (str):
        body (UpdateTargetCollaborationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateTargetCollaborationResponse]
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
    body: UpdateTargetCollaborationRequest,

) -> UpdateTargetCollaborationResponse | None:
    """ Update Target Collaboration

     This API is used by sellers to update a STANDARD target collaboration. A successful response can
    still report creators or products that were not updated. Check `data.update_failed` and
    `data.target_collaboration_conflicts` before treating the update as complete.

    Args:
        target_collaboration_id (str):
        body (UpdateTargetCollaborationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateTargetCollaborationResponse
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
    body: UpdateTargetCollaborationRequest,

) -> Response[UpdateTargetCollaborationResponse]:
    """ Update Target Collaboration

     This API is used by sellers to update a STANDARD target collaboration. A successful response can
    still report creators or products that were not updated. Check `data.update_failed` and
    `data.target_collaboration_conflicts` before treating the update as complete.

    Args:
        target_collaboration_id (str):
        body (UpdateTargetCollaborationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateTargetCollaborationResponse]
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
    body: UpdateTargetCollaborationRequest,

) -> UpdateTargetCollaborationResponse | None:
    """ Update Target Collaboration

     This API is used by sellers to update a STANDARD target collaboration. A successful response can
    still report creators or products that were not updated. Check `data.update_failed` and
    `data.target_collaboration_conflicts` before treating the update as complete.

    Args:
        target_collaboration_id (str):
        body (UpdateTargetCollaborationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateTargetCollaborationResponse
     """


    return (await asyncio_detailed(
        target_collaboration_id=target_collaboration_id,
client=client,
body=body,

    )).parsed
