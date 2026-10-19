from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_or_create_creator_conversation_request import GetOrCreateCreatorConversationRequest
from ...models.get_or_create_creator_conversation_response import GetOrCreateCreatorConversationResponse
from ...types import Response


def _get_kwargs(
    *,
    body: GetOrCreateCreatorConversationRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_seller/202508/conversations",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetOrCreateCreatorConversationResponse | None:
    if response.status_code == 200:
        response_200 = GetOrCreateCreatorConversationResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetOrCreateCreatorConversationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetOrCreateCreatorConversationRequest,
) -> Response[GetOrCreateCreatorConversationResponse]:
    """Get or Create Creator Conversation

     Get the existing conversation or create a new conversation with the specified TikTok creator. To
    send a message in the conversation, pass the returned `data.conversation_id` as the
    `conversation_id` path parameter of Send IM Message (`POST
    /affiliate_seller/202412/conversations/{conversation_id}/messages`).

    Args:
        body (GetOrCreateCreatorConversationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrCreateCreatorConversationResponse]
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
    body: GetOrCreateCreatorConversationRequest,
) -> GetOrCreateCreatorConversationResponse | None:
    """Get or Create Creator Conversation

     Get the existing conversation or create a new conversation with the specified TikTok creator. To
    send a message in the conversation, pass the returned `data.conversation_id` as the
    `conversation_id` path parameter of Send IM Message (`POST
    /affiliate_seller/202412/conversations/{conversation_id}/messages`).

    Args:
        body (GetOrCreateCreatorConversationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOrCreateCreatorConversationResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetOrCreateCreatorConversationRequest,
) -> Response[GetOrCreateCreatorConversationResponse]:
    """Get or Create Creator Conversation

     Get the existing conversation or create a new conversation with the specified TikTok creator. To
    send a message in the conversation, pass the returned `data.conversation_id` as the
    `conversation_id` path parameter of Send IM Message (`POST
    /affiliate_seller/202412/conversations/{conversation_id}/messages`).

    Args:
        body (GetOrCreateCreatorConversationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOrCreateCreatorConversationResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GetOrCreateCreatorConversationRequest,
) -> GetOrCreateCreatorConversationResponse | None:
    """Get or Create Creator Conversation

     Get the existing conversation or create a new conversation with the specified TikTok creator. To
    send a message in the conversation, pass the returned `data.conversation_id` as the
    `conversation_id` path parameter of Send IM Message (`POST
    /affiliate_seller/202412/conversations/{conversation_id}/messages`).

    Args:
        body (GetOrCreateCreatorConversationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOrCreateCreatorConversationResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
