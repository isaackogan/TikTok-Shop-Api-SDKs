from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.mark_buyer_messages_as_read_request import MarkBuyerMessagesAsReadRequest
from ...models.mark_buyer_messages_as_read_response import MarkBuyerMessagesAsReadResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    conversation_id: str,
    *,
    body: MarkBuyerMessagesAsReadRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/customer_service/202309/conversations/{conversation_id}/messages/read".format(
            conversation_id=quote(str(conversation_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MarkBuyerMessagesAsReadResponse | None:
    if response.status_code == 200:
        response_200 = MarkBuyerMessagesAsReadResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MarkBuyerMessagesAsReadResponse]:
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
    body: MarkBuyerMessagesAsReadRequest | Unset = UNSET,
) -> Response[MarkBuyerMessagesAsReadResponse]:
    """Mark Buyer Messages as Read

     Use this API to mark all messages sent by the buyer as read. You are suggested to call this API
    before replying to their messages.

    Args:
        conversation_id (str):
        body (MarkBuyerMessagesAsReadRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MarkBuyerMessagesAsReadResponse]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    conversation_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MarkBuyerMessagesAsReadRequest | Unset = UNSET,
) -> MarkBuyerMessagesAsReadResponse | None:
    """Mark Buyer Messages as Read

     Use this API to mark all messages sent by the buyer as read. You are suggested to call this API
    before replying to their messages.

    Args:
        conversation_id (str):
        body (MarkBuyerMessagesAsReadRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MarkBuyerMessagesAsReadResponse
    """

    return sync_detailed(
        conversation_id=conversation_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    conversation_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MarkBuyerMessagesAsReadRequest | Unset = UNSET,
) -> Response[MarkBuyerMessagesAsReadResponse]:
    """Mark Buyer Messages as Read

     Use this API to mark all messages sent by the buyer as read. You are suggested to call this API
    before replying to their messages.

    Args:
        conversation_id (str):
        body (MarkBuyerMessagesAsReadRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MarkBuyerMessagesAsReadResponse]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    conversation_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MarkBuyerMessagesAsReadRequest | Unset = UNSET,
) -> MarkBuyerMessagesAsReadResponse | None:
    """Mark Buyer Messages as Read

     Use this API to mark all messages sent by the buyer as read. You are suggested to call this API
    before replying to their messages.

    Args:
        conversation_id (str):
        body (MarkBuyerMessagesAsReadRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MarkBuyerMessagesAsReadResponse
    """

    return (
        await asyncio_detailed(
            conversation_id=conversation_id,
            client=client,
            body=body,
        )
    ).parsed
