from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_conversations_locale import GetConversationsLocale
from ...models.get_conversations_response import GetConversationsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_token: str | Unset = UNSET,
    page_size: int,
    locale: GetConversationsLocale | Unset = UNSET,
    need_session_id: bool | Unset = UNSET,
    need_session_info: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page_token"] = page_token

    params["page_size"] = page_size

    json_locale: str | Unset = UNSET
    if not isinstance(locale, Unset):
        json_locale = locale.value

    params["locale"] = json_locale

    params["need_session_id"] = need_session_id

    params["need_session_info"] = need_session_info

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/customer_service/202309/conversations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetConversationsResponse | None:
    if response.status_code == 200:
        response_200 = GetConversationsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetConversationsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    page_size: int,
    locale: GetConversationsLocale | Unset = UNSET,
    need_session_id: bool | Unset = UNSET,
    need_session_info: bool | Unset = UNSET,
) -> Response[GetConversationsResponse]:
    """Get Conversations

     Use this API to retrieve a shop's conversations with buyers.

    Args:
        page_token (str | Unset):
        page_size (int):
        locale (GetConversationsLocale | Unset):
        need_session_id (bool | Unset):
        need_session_info (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetConversationsResponse]
    """

    kwargs = _get_kwargs(
        page_token=page_token,
        page_size=page_size,
        locale=locale,
        need_session_id=need_session_id,
        need_session_info=need_session_info,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    page_size: int,
    locale: GetConversationsLocale | Unset = UNSET,
    need_session_id: bool | Unset = UNSET,
    need_session_info: bool | Unset = UNSET,
) -> GetConversationsResponse | None:
    """Get Conversations

     Use this API to retrieve a shop's conversations with buyers.

    Args:
        page_token (str | Unset):
        page_size (int):
        locale (GetConversationsLocale | Unset):
        need_session_id (bool | Unset):
        need_session_info (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetConversationsResponse
    """

    return sync_detailed(
        client=client,
        page_token=page_token,
        page_size=page_size,
        locale=locale,
        need_session_id=need_session_id,
        need_session_info=need_session_info,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    page_size: int,
    locale: GetConversationsLocale | Unset = UNSET,
    need_session_id: bool | Unset = UNSET,
    need_session_info: bool | Unset = UNSET,
) -> Response[GetConversationsResponse]:
    """Get Conversations

     Use this API to retrieve a shop's conversations with buyers.

    Args:
        page_token (str | Unset):
        page_size (int):
        locale (GetConversationsLocale | Unset):
        need_session_id (bool | Unset):
        need_session_info (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetConversationsResponse]
    """

    kwargs = _get_kwargs(
        page_token=page_token,
        page_size=page_size,
        locale=locale,
        need_session_id=need_session_id,
        need_session_info=need_session_info,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    page_size: int,
    locale: GetConversationsLocale | Unset = UNSET,
    need_session_id: bool | Unset = UNSET,
    need_session_info: bool | Unset = UNSET,
) -> GetConversationsResponse | None:
    """Get Conversations

     Use this API to retrieve a shop's conversations with buyers.

    Args:
        page_token (str | Unset):
        page_size (int):
        locale (GetConversationsLocale | Unset):
        need_session_id (bool | Unset):
        need_session_info (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetConversationsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            page_token=page_token,
            page_size=page_size,
            locale=locale,
            need_session_id=need_session_id,
            need_session_info=need_session_info,
        )
    ).parsed
