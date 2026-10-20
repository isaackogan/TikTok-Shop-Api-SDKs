from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_creator_conversation_messages_response import GetCreatorConversationMessagesResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    conversation_id: str,
    *,
    page_size: int,
    page_token: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page_size"] = page_size

    params["page_token"] = page_token


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/affiliate_seller/202412/conversation/{conversation_id}/messages".format(conversation_id=quote(str(conversation_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetCreatorConversationMessagesResponse | None:
    if response.status_code == 200:
        response_200 = GetCreatorConversationMessagesResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetCreatorConversationMessagesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    conversation_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_size: int,
    page_token: str | Unset = UNSET,

) -> Response[GetCreatorConversationMessagesResponse]:
    """ Get Creator Conversation Messages

     Retrieves a page of messages from a conversation.

    Args:
        conversation_id (str):
        page_size (int):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCreatorConversationMessagesResponse]
     """


    kwargs = _get_kwargs(
        conversation_id=conversation_id,
page_size=page_size,
page_token=page_token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    conversation_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_size: int,
    page_token: str | Unset = UNSET,

) -> GetCreatorConversationMessagesResponse | None:
    """ Get Creator Conversation Messages

     Retrieves a page of messages from a conversation.

    Args:
        conversation_id (str):
        page_size (int):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCreatorConversationMessagesResponse
     """


    return sync_detailed(
        conversation_id=conversation_id,
client=client,
page_size=page_size,
page_token=page_token,

    ).parsed

async def asyncio_detailed(
    conversation_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_size: int,
    page_token: str | Unset = UNSET,

) -> Response[GetCreatorConversationMessagesResponse]:
    """ Get Creator Conversation Messages

     Retrieves a page of messages from a conversation.

    Args:
        conversation_id (str):
        page_size (int):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCreatorConversationMessagesResponse]
     """


    kwargs = _get_kwargs(
        conversation_id=conversation_id,
page_size=page_size,
page_token=page_token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    conversation_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_size: int,
    page_token: str | Unset = UNSET,

) -> GetCreatorConversationMessagesResponse | None:
    """ Get Creator Conversation Messages

     Retrieves a page of messages from a conversation.

    Args:
        conversation_id (str):
        page_size (int):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCreatorConversationMessagesResponse
     """


    return (await asyncio_detailed(
        conversation_id=conversation_id,
client=client,
page_size=page_size,
page_token=page_token,

    )).parsed
