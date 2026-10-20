from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.query_target_collaboration_detail_response import QueryTargetCollaborationDetailResponse
from typing import cast



def _get_kwargs(
    target_collaboration_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/affiliate_seller/202508/target_collaborations/{target_collaboration_id}".format(target_collaboration_id=quote(str(target_collaboration_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> QueryTargetCollaborationDetailResponse | None:
    if response.status_code == 200:
        response_200 = QueryTargetCollaborationDetailResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[QueryTargetCollaborationDetailResponse]:
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

) -> Response[QueryTargetCollaborationDetailResponse]:
    """ Query Target Collaboration Detail

     This API is used by Sellers to get target collaboration information.

    Args:
        target_collaboration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QueryTargetCollaborationDetailResponse]
     """


    kwargs = _get_kwargs(
        target_collaboration_id=target_collaboration_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    target_collaboration_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> QueryTargetCollaborationDetailResponse | None:
    """ Query Target Collaboration Detail

     This API is used by Sellers to get target collaboration information.

    Args:
        target_collaboration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QueryTargetCollaborationDetailResponse
     """


    return sync_detailed(
        target_collaboration_id=target_collaboration_id,
client=client,

    ).parsed

async def asyncio_detailed(
    target_collaboration_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[QueryTargetCollaborationDetailResponse]:
    """ Query Target Collaboration Detail

     This API is used by Sellers to get target collaboration information.

    Args:
        target_collaboration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QueryTargetCollaborationDetailResponse]
     """


    kwargs = _get_kwargs(
        target_collaboration_id=target_collaboration_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    target_collaboration_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> QueryTargetCollaborationDetailResponse | None:
    """ Query Target Collaboration Detail

     This API is used by Sellers to get target collaboration information.

    Args:
        target_collaboration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QueryTargetCollaborationDetailResponse
     """


    return (await asyncio_detailed(
        target_collaboration_id=target_collaboration_id,
client=client,

    )).parsed
