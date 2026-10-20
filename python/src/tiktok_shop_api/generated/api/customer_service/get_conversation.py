from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_conversation_response import GetConversationResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    conversation_id: str,
    *,
    need_session_id: bool | Unset = UNSET,
    need_session_info: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["need_session_id"] = need_session_id

    params["need_session_info"] = need_session_info


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/customer_service/202601/conversations/{conversation_id}".format(conversation_id=quote(str(conversation_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetConversationResponse | None:
    if response.status_code == 200:
        response_200 = GetConversationResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetConversationResponse]:
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
    need_session_id: bool | Unset = UNSET,
    need_session_info: bool | Unset = UNSET,

) -> Response[GetConversationResponse]:
    """ Get Conversation

     Use this API to retrieve information about a conversation by ID.

    Args:
        conversation_id (str):
        need_session_id (bool | Unset):
        need_session_info (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetConversationResponse]
     """


    kwargs = _get_kwargs(
        conversation_id=conversation_id,
need_session_id=need_session_id,
need_session_info=need_session_info,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    conversation_id: str,
    *,
    client: AuthenticatedClient | Client,
    need_session_id: bool | Unset = UNSET,
    need_session_info: bool | Unset = UNSET,

) -> GetConversationResponse | None:
    """ Get Conversation

     Use this API to retrieve information about a conversation by ID.

    Args:
        conversation_id (str):
        need_session_id (bool | Unset):
        need_session_info (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetConversationResponse
     """


    return sync_detailed(
        conversation_id=conversation_id,
client=client,
need_session_id=need_session_id,
need_session_info=need_session_info,

    ).parsed

async def asyncio_detailed(
    conversation_id: str,
    *,
    client: AuthenticatedClient | Client,
    need_session_id: bool | Unset = UNSET,
    need_session_info: bool | Unset = UNSET,

) -> Response[GetConversationResponse]:
    """ Get Conversation

     Use this API to retrieve information about a conversation by ID.

    Args:
        conversation_id (str):
        need_session_id (bool | Unset):
        need_session_info (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetConversationResponse]
     """


    kwargs = _get_kwargs(
        conversation_id=conversation_id,
need_session_id=need_session_id,
need_session_info=need_session_info,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    conversation_id: str,
    *,
    client: AuthenticatedClient | Client,
    need_session_id: bool | Unset = UNSET,
    need_session_info: bool | Unset = UNSET,

) -> GetConversationResponse | None:
    """ Get Conversation

     Use this API to retrieve information about a conversation by ID.

    Args:
        conversation_id (str):
        need_session_id (bool | Unset):
        need_session_info (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetConversationResponse
     """


    return (await asyncio_detailed(
        conversation_id=conversation_id,
client=client,
need_session_id=need_session_id,
need_session_info=need_session_info,

    )).parsed
