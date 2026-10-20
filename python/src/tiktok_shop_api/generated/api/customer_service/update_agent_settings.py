from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_agent_settings_request import UpdateAgentSettingsRequest
from ...models.update_agent_settings_response import UpdateAgentSettingsResponse
from ...types import Response


def _get_kwargs(
    *,
    body: UpdateAgentSettingsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/customer_service/202309/agents/settings",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UpdateAgentSettingsResponse | None:
    if response.status_code == 200:
        response_200 = UpdateAgentSettingsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdateAgentSettingsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAgentSettingsRequest,
) -> Response[UpdateAgentSettingsResponse]:
    """Update Agent Settings

     Use this API to set whether the shop owner's customer service account can accept auto-assigned
    chats. The authenticated shop owner can update only their own setting; customer service subaccounts
    are not supported in this API version. Set `can_accept_chat` to `true` to accept auto-assigned
    chats.

    Args:
        body (UpdateAgentSettingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateAgentSettingsResponse]
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
    body: UpdateAgentSettingsRequest,
) -> UpdateAgentSettingsResponse | None:
    """Update Agent Settings

     Use this API to set whether the shop owner's customer service account can accept auto-assigned
    chats. The authenticated shop owner can update only their own setting; customer service subaccounts
    are not supported in this API version. Set `can_accept_chat` to `true` to accept auto-assigned
    chats.

    Args:
        body (UpdateAgentSettingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateAgentSettingsResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAgentSettingsRequest,
) -> Response[UpdateAgentSettingsResponse]:
    """Update Agent Settings

     Use this API to set whether the shop owner's customer service account can accept auto-assigned
    chats. The authenticated shop owner can update only their own setting; customer service subaccounts
    are not supported in this API version. Set `can_accept_chat` to `true` to accept auto-assigned
    chats.

    Args:
        body (UpdateAgentSettingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateAgentSettingsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAgentSettingsRequest,
) -> UpdateAgentSettingsResponse | None:
    """Update Agent Settings

     Use this API to set whether the shop owner's customer service account can accept auto-assigned
    chats. The authenticated shop owner can update only their own setting; customer service subaccounts
    are not supported in this API version. Set `can_accept_chat` to `true` to accept auto-assigned
    chats.

    Args:
        body (UpdateAgentSettingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateAgentSettingsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
