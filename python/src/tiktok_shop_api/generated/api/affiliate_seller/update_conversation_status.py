from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_conversation_status_request import UpdateConversationStatusRequest
from ...models.update_conversation_status_response import UpdateConversationStatusResponse
from ...types import Response


def _get_kwargs(
    conversation_id: str,
    *,
    body: UpdateConversationStatusRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_seller/202608/conversations/{conversation_id}/status".format(
            conversation_id=quote(str(conversation_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UpdateConversationStatusResponse | None:
    if response.status_code == 200:
        response_200 = UpdateConversationStatusResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdateConversationStatusResponse]:
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
    body: UpdateConversationStatusRequest,
) -> Response[UpdateConversationStatusResponse]:
    """Update Conversation Status

     Support starring or archiving a given conversation with creator.

    Args:
        conversation_id (str):
        body (UpdateConversationStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateConversationStatusResponse]
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
    body: UpdateConversationStatusRequest,
) -> UpdateConversationStatusResponse | None:
    """Update Conversation Status

     Support starring or archiving a given conversation with creator.

    Args:
        conversation_id (str):
        body (UpdateConversationStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateConversationStatusResponse
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
    body: UpdateConversationStatusRequest,
) -> Response[UpdateConversationStatusResponse]:
    """Update Conversation Status

     Support starring or archiving a given conversation with creator.

    Args:
        conversation_id (str):
        body (UpdateConversationStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateConversationStatusResponse]
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
    body: UpdateConversationStatusRequest,
) -> UpdateConversationStatusResponse | None:
    """Update Conversation Status

     Support starring or archiving a given conversation with creator.

    Args:
        conversation_id (str):
        body (UpdateConversationStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateConversationStatusResponse
    """

    return (
        await asyncio_detailed(
            conversation_id=conversation_id,
            client=client,
            body=body,
        )
    ).parsed
