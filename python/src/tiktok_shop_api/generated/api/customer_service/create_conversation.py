from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_conversation_request import CreateConversationRequest
from ...models.create_conversation_response import CreateConversationResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateConversationRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/customer_service/202309/conversations",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateConversationResponse | None:
    if response.status_code == 200:
        response_200 = CreateConversationResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateConversationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateConversationRequest,
) -> Response[CreateConversationResponse]:
    """Create Conversation

     Use this API to create a conversation with the specified buyer, on behalf of a shop. When there's no
    prior conversation, calling this API creates a new conversation; when there's a prior conversation,
    no matter whether it's active, finished, or closed, calling this API reopens the conversation and
    returns the same conversation ID as the prior one.

    Args:
        body (CreateConversationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateConversationResponse]
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
    body: CreateConversationRequest,
) -> CreateConversationResponse | None:
    """Create Conversation

     Use this API to create a conversation with the specified buyer, on behalf of a shop. When there's no
    prior conversation, calling this API creates a new conversation; when there's a prior conversation,
    no matter whether it's active, finished, or closed, calling this API reopens the conversation and
    returns the same conversation ID as the prior one.

    Args:
        body (CreateConversationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateConversationResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateConversationRequest,
) -> Response[CreateConversationResponse]:
    """Create Conversation

     Use this API to create a conversation with the specified buyer, on behalf of a shop. When there's no
    prior conversation, calling this API creates a new conversation; when there's a prior conversation,
    no matter whether it's active, finished, or closed, calling this API reopens the conversation and
    returns the same conversation ID as the prior one.

    Args:
        body (CreateConversationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateConversationResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateConversationRequest,
) -> CreateConversationResponse | None:
    """Create Conversation

     Use this API to create a conversation with the specified buyer, on behalf of a shop. When there's no
    prior conversation, calling this API creates a new conversation; when there's a prior conversation,
    no matter whether it's active, finished, or closed, calling this API reopens the conversation and
    returns the same conversation ID as the prior one.

    Args:
        body (CreateConversationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateConversationResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
