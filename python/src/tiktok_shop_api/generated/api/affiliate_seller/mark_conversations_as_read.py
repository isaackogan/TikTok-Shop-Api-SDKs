from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mark_conversations_as_read_request import MarkConversationsAsReadRequest
from ...models.mark_conversations_as_read_response import MarkConversationsAsReadResponse
from typing import cast



def _get_kwargs(
    *,
    body: MarkConversationsAsReadRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_seller/202412/conversatons/read",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MarkConversationsAsReadResponse | None:
    if response.status_code == 200:
        response_200 = MarkConversationsAsReadResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MarkConversationsAsReadResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MarkConversationsAsReadRequest,

) -> Response[MarkConversationsAsReadResponse]:
    """ Mark Conversations as Read

     Mark the messages in the specified conversations to be read.

    Args:
        body (MarkConversationsAsReadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MarkConversationsAsReadResponse]
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
    body: MarkConversationsAsReadRequest,

) -> MarkConversationsAsReadResponse | None:
    """ Mark Conversations as Read

     Mark the messages in the specified conversations to be read.

    Args:
        body (MarkConversationsAsReadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MarkConversationsAsReadResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MarkConversationsAsReadRequest,

) -> Response[MarkConversationsAsReadResponse]:
    """ Mark Conversations as Read

     Mark the messages in the specified conversations to be read.

    Args:
        body (MarkConversationsAsReadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MarkConversationsAsReadResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: MarkConversationsAsReadRequest,

) -> MarkConversationsAsReadResponse | None:
    """ Mark Conversations as Read

     Mark the messages in the specified conversations to be read.

    Args:
        body (MarkConversationsAsReadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MarkConversationsAsReadResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
