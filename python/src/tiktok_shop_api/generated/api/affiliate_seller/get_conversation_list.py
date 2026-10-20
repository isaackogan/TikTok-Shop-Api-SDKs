from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_conversation_list_conversation_status import GetConversationListConversationStatus
from ...models.get_conversation_list_request import GetConversationListRequest
from ...models.get_conversation_list_response import GetConversationListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: GetConversationListRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,
    only_need_conversation_id: bool | Unset = UNSET,
    conversation_status: GetConversationListConversationStatus | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["page_size"] = page_size

    params["page_token"] = page_token

    params["only_need_conversation_id"] = only_need_conversation_id

    json_conversation_status: str | Unset = UNSET
    if not isinstance(conversation_status, Unset):
        json_conversation_status = conversation_status.value

    params["conversation_status"] = json_conversation_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/affiliate_seller/202412/conversations",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetConversationListResponse | None:
    if response.status_code == 200:
        response_200 = GetConversationListResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetConversationListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetConversationListRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,
    only_need_conversation_id: bool | Unset = UNSET,
    conversation_status: GetConversationListConversationStatus | Unset = UNSET,
) -> Response[GetConversationListResponse]:
    """Get Conversation List

     Retrieve the seller's IM conversations.

    Args:
        page_size (int):
        page_token (str | Unset):
        only_need_conversation_id (bool | Unset):
        conversation_status (GetConversationListConversationStatus | Unset):
        body (GetConversationListRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetConversationListResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        page_size=page_size,
        page_token=page_token,
        only_need_conversation_id=only_need_conversation_id,
        conversation_status=conversation_status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: GetConversationListRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,
    only_need_conversation_id: bool | Unset = UNSET,
    conversation_status: GetConversationListConversationStatus | Unset = UNSET,
) -> GetConversationListResponse | None:
    """Get Conversation List

     Retrieve the seller's IM conversations.

    Args:
        page_size (int):
        page_token (str | Unset):
        only_need_conversation_id (bool | Unset):
        conversation_status (GetConversationListConversationStatus | Unset):
        body (GetConversationListRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetConversationListResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        page_size=page_size,
        page_token=page_token,
        only_need_conversation_id=only_need_conversation_id,
        conversation_status=conversation_status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetConversationListRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,
    only_need_conversation_id: bool | Unset = UNSET,
    conversation_status: GetConversationListConversationStatus | Unset = UNSET,
) -> Response[GetConversationListResponse]:
    """Get Conversation List

     Retrieve the seller's IM conversations.

    Args:
        page_size (int):
        page_token (str | Unset):
        only_need_conversation_id (bool | Unset):
        conversation_status (GetConversationListConversationStatus | Unset):
        body (GetConversationListRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetConversationListResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        page_size=page_size,
        page_token=page_token,
        only_need_conversation_id=only_need_conversation_id,
        conversation_status=conversation_status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GetConversationListRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,
    only_need_conversation_id: bool | Unset = UNSET,
    conversation_status: GetConversationListConversationStatus | Unset = UNSET,
) -> GetConversationListResponse | None:
    """Get Conversation List

     Retrieve the seller's IM conversations.

    Args:
        page_size (int):
        page_token (str | Unset):
        only_need_conversation_id (bool | Unset):
        conversation_status (GetConversationListConversationStatus | Unset):
        body (GetConversationListRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetConversationListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            page_size=page_size,
            page_token=page_token,
            only_need_conversation_id=only_need_conversation_id,
            conversation_status=conversation_status,
        )
    ).parsed
