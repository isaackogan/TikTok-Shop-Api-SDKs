from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_custom_engagement_task_request import CreateCustomEngagementTaskRequest
from ...models.create_custom_engagement_task_response import CreateCustomEngagementTaskResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: CreateCustomEngagementTaskRequest,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["idempotency_key"] = idempotency_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/customer_engagement/202502/engagement_tasks/custom",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateCustomEngagementTaskResponse | None:
    if response.status_code == 200:
        response_200 = CreateCustomEngagementTaskResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateCustomEngagementTaskResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateCustomEngagementTaskRequest,
    idempotency_key: str,
) -> Response[CreateCustomEngagementTaskResponse]:
    """Create Custom Engagement Task

     Create an engagement task that uses a self-defined custom message instead of predefined message
    templates from TikTok Shop. The task acts as a container for grouping messages with similar content
    and rules, allowing sellers to track and compare task performance across different types of content.
    Note that each task has a mandatory end time, and once expired, it cannot be used to send additional
    messages.

    Args:
        idempotency_key (str):
        body (CreateCustomEngagementTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateCustomEngagementTaskResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateCustomEngagementTaskRequest,
    idempotency_key: str,
) -> CreateCustomEngagementTaskResponse | None:
    """Create Custom Engagement Task

     Create an engagement task that uses a self-defined custom message instead of predefined message
    templates from TikTok Shop. The task acts as a container for grouping messages with similar content
    and rules, allowing sellers to track and compare task performance across different types of content.
    Note that each task has a mandatory end time, and once expired, it cannot be used to send additional
    messages.

    Args:
        idempotency_key (str):
        body (CreateCustomEngagementTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateCustomEngagementTaskResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateCustomEngagementTaskRequest,
    idempotency_key: str,
) -> Response[CreateCustomEngagementTaskResponse]:
    """Create Custom Engagement Task

     Create an engagement task that uses a self-defined custom message instead of predefined message
    templates from TikTok Shop. The task acts as a container for grouping messages with similar content
    and rules, allowing sellers to track and compare task performance across different types of content.
    Note that each task has a mandatory end time, and once expired, it cannot be used to send additional
    messages.

    Args:
        idempotency_key (str):
        body (CreateCustomEngagementTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateCustomEngagementTaskResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateCustomEngagementTaskRequest,
    idempotency_key: str,
) -> CreateCustomEngagementTaskResponse | None:
    """Create Custom Engagement Task

     Create an engagement task that uses a self-defined custom message instead of predefined message
    templates from TikTok Shop. The task acts as a container for grouping messages with similar content
    and rules, allowing sellers to track and compare task performance across different types of content.
    Note that each task has a mandatory end time, and once expired, it cannot be used to send additional
    messages.

    Args:
        idempotency_key (str):
        body (CreateCustomEngagementTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateCustomEngagementTaskResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
