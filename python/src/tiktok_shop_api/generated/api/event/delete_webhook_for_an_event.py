from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_webhook_for_an_event_request import DeleteWebhookForAnEventRequest
from ...models.delete_webhook_for_an_event_response import DeleteWebhookForAnEventResponse
from ...types import Response


def _get_kwargs(
    *,
    body: DeleteWebhookForAnEventRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/event/202309/webhooks",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteWebhookForAnEventResponse | None:
    if response.status_code == 200:
        response_200 = DeleteWebhookForAnEventResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeleteWebhookForAnEventResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteWebhookForAnEventRequest,
) -> Response[DeleteWebhookForAnEventResponse]:
    """Delete Webhook for an Event

     Deletes the shop's webhook URL for the specified event topic. The request succeeds even if no
    webhook URL is currently configured for that topic.

    Args:
        body (DeleteWebhookForAnEventRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteWebhookForAnEventResponse]
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
    body: DeleteWebhookForAnEventRequest,
) -> DeleteWebhookForAnEventResponse | None:
    """Delete Webhook for an Event

     Deletes the shop's webhook URL for the specified event topic. The request succeeds even if no
    webhook URL is currently configured for that topic.

    Args:
        body (DeleteWebhookForAnEventRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteWebhookForAnEventResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteWebhookForAnEventRequest,
) -> Response[DeleteWebhookForAnEventResponse]:
    """Delete Webhook for an Event

     Deletes the shop's webhook URL for the specified event topic. The request succeeds even if no
    webhook URL is currently configured for that topic.

    Args:
        body (DeleteWebhookForAnEventRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteWebhookForAnEventResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteWebhookForAnEventRequest,
) -> DeleteWebhookForAnEventResponse | None:
    """Delete Webhook for an Event

     Deletes the shop's webhook URL for the specified event topic. The request succeeds even if no
    webhook URL is currently configured for that topic.

    Args:
        body (DeleteWebhookForAnEventRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteWebhookForAnEventResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
