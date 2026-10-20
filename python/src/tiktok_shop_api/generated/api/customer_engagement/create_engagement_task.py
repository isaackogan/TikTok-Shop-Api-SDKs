from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_engagement_task_request import CreateEngagementTaskRequest
from ...models.create_engagement_task_response import CreateEngagementTaskResponse
from typing import cast



def _get_kwargs(
    *,
    body: CreateEngagementTaskRequest,
    idempotency_key: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["idempotency_key"] = idempotency_key


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/customer_engagement/202412/engagement_tasks",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateEngagementTaskResponse | None:
    if response.status_code == 200:
        response_200 = CreateEngagementTaskResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateEngagementTaskResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateEngagementTaskRequest,
    idempotency_key: str,

) -> Response[CreateEngagementTaskResponse]:
    """ Create Engagement Task

     Create an engagement task that acts as a container for grouping messages with similar content and
    rules, allowing sellers to track and compare task performance across different types of content.
    Note that each task has a mandatory end time, and once expired, it cannot be used to send additional
    messages.

    Args:
        idempotency_key (str):
        body (CreateEngagementTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateEngagementTaskResponse]
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
    body: CreateEngagementTaskRequest,
    idempotency_key: str,

) -> CreateEngagementTaskResponse | None:
    """ Create Engagement Task

     Create an engagement task that acts as a container for grouping messages with similar content and
    rules, allowing sellers to track and compare task performance across different types of content.
    Note that each task has a mandatory end time, and once expired, it cannot be used to send additional
    messages.

    Args:
        idempotency_key (str):
        body (CreateEngagementTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateEngagementTaskResponse
     """


    return sync_detailed(
        client=client,
body=body,
idempotency_key=idempotency_key,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateEngagementTaskRequest,
    idempotency_key: str,

) -> Response[CreateEngagementTaskResponse]:
    """ Create Engagement Task

     Create an engagement task that acts as a container for grouping messages with similar content and
    rules, allowing sellers to track and compare task performance across different types of content.
    Note that each task has a mandatory end time, and once expired, it cannot be used to send additional
    messages.

    Args:
        idempotency_key (str):
        body (CreateEngagementTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateEngagementTaskResponse]
     """


    kwargs = _get_kwargs(
        body=body,
idempotency_key=idempotency_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateEngagementTaskRequest,
    idempotency_key: str,

) -> CreateEngagementTaskResponse | None:
    """ Create Engagement Task

     Create an engagement task that acts as a container for grouping messages with similar content and
    rules, allowing sellers to track and compare task performance across different types of content.
    Note that each task has a mandatory end time, and once expired, it cannot be used to send additional
    messages.

    Args:
        idempotency_key (str):
        body (CreateEngagementTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateEngagementTaskResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
idempotency_key=idempotency_key,

    )).parsed
