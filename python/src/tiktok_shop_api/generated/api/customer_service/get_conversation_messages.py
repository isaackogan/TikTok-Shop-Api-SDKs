from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_conversation_messages_locale import GetConversationMessagesLocale
from ...models.get_conversation_messages_response import GetConversationMessagesResponse
from ...models.get_conversation_messages_sort_order import GetConversationMessagesSortOrder
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    conversation_id: str,
    *,
    page_token: str | Unset = UNSET,
    page_size: int,
    locale: GetConversationMessagesLocale | Unset = UNSET,
    sort_order: GetConversationMessagesSortOrder | Unset = UNSET,
    sort_field: str | Unset = UNSET,
    need_data: bool | Unset = UNSET,
    need_plaintext: bool | Unset = UNSET,
    time_zone: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page_token"] = page_token

    params["page_size"] = page_size

    json_locale: str | Unset = UNSET
    if not isinstance(locale, Unset):
        json_locale = locale.value

    params["locale"] = json_locale

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sort_order"] = json_sort_order

    params["sort_field"] = sort_field

    params["need_data"] = need_data

    params["need_plaintext"] = need_plaintext

    params["time_zone"] = time_zone


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/customer_service/202309/conversations/{conversation_id}/messages".format(conversation_id=quote(str(conversation_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetConversationMessagesResponse | None:
    if response.status_code == 200:
        response_200 = GetConversationMessagesResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetConversationMessagesResponse]:
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
    page_token: str | Unset = UNSET,
    page_size: int,
    locale: GetConversationMessagesLocale | Unset = UNSET,
    sort_order: GetConversationMessagesSortOrder | Unset = UNSET,
    sort_field: str | Unset = UNSET,
    need_data: bool | Unset = UNSET,
    need_plaintext: bool | Unset = UNSET,
    time_zone: str | Unset = UNSET,

) -> Response[GetConversationMessagesResponse]:
    """ Get Conversation Messages

     Use this API to retrieve a page of messages in a conversation between a buyer and a shop.
    Calling this API does not mark messages as read. Call [Read Message](650a59f7c16ffe02b8e8db3f) to
    mark them as read.

    Args:
        conversation_id (str):
        page_token (str | Unset):
        page_size (int):
        locale (GetConversationMessagesLocale | Unset):
        sort_order (GetConversationMessagesSortOrder | Unset):
        sort_field (str | Unset):
        need_data (bool | Unset):
        need_plaintext (bool | Unset):
        time_zone (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetConversationMessagesResponse]
     """


    kwargs = _get_kwargs(
        conversation_id=conversation_id,
page_token=page_token,
page_size=page_size,
locale=locale,
sort_order=sort_order,
sort_field=sort_field,
need_data=need_data,
need_plaintext=need_plaintext,
time_zone=time_zone,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    conversation_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    page_size: int,
    locale: GetConversationMessagesLocale | Unset = UNSET,
    sort_order: GetConversationMessagesSortOrder | Unset = UNSET,
    sort_field: str | Unset = UNSET,
    need_data: bool | Unset = UNSET,
    need_plaintext: bool | Unset = UNSET,
    time_zone: str | Unset = UNSET,

) -> GetConversationMessagesResponse | None:
    """ Get Conversation Messages

     Use this API to retrieve a page of messages in a conversation between a buyer and a shop.
    Calling this API does not mark messages as read. Call [Read Message](650a59f7c16ffe02b8e8db3f) to
    mark them as read.

    Args:
        conversation_id (str):
        page_token (str | Unset):
        page_size (int):
        locale (GetConversationMessagesLocale | Unset):
        sort_order (GetConversationMessagesSortOrder | Unset):
        sort_field (str | Unset):
        need_data (bool | Unset):
        need_plaintext (bool | Unset):
        time_zone (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetConversationMessagesResponse
     """


    return sync_detailed(
        conversation_id=conversation_id,
client=client,
page_token=page_token,
page_size=page_size,
locale=locale,
sort_order=sort_order,
sort_field=sort_field,
need_data=need_data,
need_plaintext=need_plaintext,
time_zone=time_zone,

    ).parsed

async def asyncio_detailed(
    conversation_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    page_size: int,
    locale: GetConversationMessagesLocale | Unset = UNSET,
    sort_order: GetConversationMessagesSortOrder | Unset = UNSET,
    sort_field: str | Unset = UNSET,
    need_data: bool | Unset = UNSET,
    need_plaintext: bool | Unset = UNSET,
    time_zone: str | Unset = UNSET,

) -> Response[GetConversationMessagesResponse]:
    """ Get Conversation Messages

     Use this API to retrieve a page of messages in a conversation between a buyer and a shop.
    Calling this API does not mark messages as read. Call [Read Message](650a59f7c16ffe02b8e8db3f) to
    mark them as read.

    Args:
        conversation_id (str):
        page_token (str | Unset):
        page_size (int):
        locale (GetConversationMessagesLocale | Unset):
        sort_order (GetConversationMessagesSortOrder | Unset):
        sort_field (str | Unset):
        need_data (bool | Unset):
        need_plaintext (bool | Unset):
        time_zone (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetConversationMessagesResponse]
     """


    kwargs = _get_kwargs(
        conversation_id=conversation_id,
page_token=page_token,
page_size=page_size,
locale=locale,
sort_order=sort_order,
sort_field=sort_field,
need_data=need_data,
need_plaintext=need_plaintext,
time_zone=time_zone,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    conversation_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    page_size: int,
    locale: GetConversationMessagesLocale | Unset = UNSET,
    sort_order: GetConversationMessagesSortOrder | Unset = UNSET,
    sort_field: str | Unset = UNSET,
    need_data: bool | Unset = UNSET,
    need_plaintext: bool | Unset = UNSET,
    time_zone: str | Unset = UNSET,

) -> GetConversationMessagesResponse | None:
    """ Get Conversation Messages

     Use this API to retrieve a page of messages in a conversation between a buyer and a shop.
    Calling this API does not mark messages as read. Call [Read Message](650a59f7c16ffe02b8e8db3f) to
    mark them as read.

    Args:
        conversation_id (str):
        page_token (str | Unset):
        page_size (int):
        locale (GetConversationMessagesLocale | Unset):
        sort_order (GetConversationMessagesSortOrder | Unset):
        sort_field (str | Unset):
        need_data (bool | Unset):
        need_plaintext (bool | Unset):
        time_zone (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetConversationMessagesResponse
     """


    return (await asyncio_detailed(
        conversation_id=conversation_id,
client=client,
page_token=page_token,
page_size=page_size,
locale=locale,
sort_order=sort_order,
sort_field=sort_field,
need_data=need_data,
need_plaintext=need_plaintext,
time_zone=time_zone,

    )).parsed
