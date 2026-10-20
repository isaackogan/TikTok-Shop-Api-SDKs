from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_agent_settings_response import GetAgentSettingsResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/customer_service/202309/agents/settings",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetAgentSettingsResponse | None:
    if response.status_code == 200:
        response_200 = GetAgentSettingsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetAgentSettingsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetAgentSettingsResponse]:
    """Get Agent Settings

     This API is used to get agent settings. This API allows the agent to see whether the agent can
    accept chats from buyers. This API is a read-only endpoint. There will be no side effects, and can
    be retried safely. Note:  1. The current API version can only get settings on behalf of the shop, or
    the owner account holder on Seller Center. The owner in this case is acting as the customer service
    agent. In the future, we plan to make this API available to subaccount holders (who has customer
    service role) in Seller Center.  2. This API is to allow the agent to get his/her own setting.  See
    more information in API overview

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAgentSettingsResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> GetAgentSettingsResponse | None:
    """Get Agent Settings

     This API is used to get agent settings. This API allows the agent to see whether the agent can
    accept chats from buyers. This API is a read-only endpoint. There will be no side effects, and can
    be retried safely. Note:  1. The current API version can only get settings on behalf of the shop, or
    the owner account holder on Seller Center. The owner in this case is acting as the customer service
    agent. In the future, we plan to make this API available to subaccount holders (who has customer
    service role) in Seller Center.  2. This API is to allow the agent to get his/her own setting.  See
    more information in API overview

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAgentSettingsResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetAgentSettingsResponse]:
    """Get Agent Settings

     This API is used to get agent settings. This API allows the agent to see whether the agent can
    accept chats from buyers. This API is a read-only endpoint. There will be no side effects, and can
    be retried safely. Note:  1. The current API version can only get settings on behalf of the shop, or
    the owner account holder on Seller Center. The owner in this case is acting as the customer service
    agent. In the future, we plan to make this API available to subaccount holders (who has customer
    service role) in Seller Center.  2. This API is to allow the agent to get his/her own setting.  See
    more information in API overview

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAgentSettingsResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> GetAgentSettingsResponse | None:
    """Get Agent Settings

     This API is used to get agent settings. This API allows the agent to see whether the agent can
    accept chats from buyers. This API is a read-only endpoint. There will be no side effects, and can
    be retried safely. Note:  1. The current API version can only get settings on behalf of the shop, or
    the owner account holder on Seller Center. The owner in this case is acting as the customer service
    agent. In the future, we plan to make this API available to subaccount holders (who has customer
    service role) in Seller Center.  2. This API is to allow the agent to get his/her own setting.  See
    more information in API overview

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAgentSettingsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
