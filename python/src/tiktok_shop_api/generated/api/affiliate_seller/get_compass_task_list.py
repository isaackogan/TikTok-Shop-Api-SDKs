from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_compass_task_list_response import GetCompassTaskListResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    doc_type: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["doc_type"] = doc_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/affiliate_seller/202603/compass/offline_tasks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetCompassTaskListResponse | None:
    if response.status_code == 200:
        response_200 = GetCompassTaskListResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetCompassTaskListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    doc_type: str,
) -> Response[GetCompassTaskListResponse]:
    """Get Compass Task List

     Retrieve the list of export tasks created via Open API for the authorized seller (last 7 days).
    Supports pagination and returns task status, file_name and timestamps.

    Args:
        doc_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCompassTaskListResponse]
    """

    kwargs = _get_kwargs(
        doc_type=doc_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    doc_type: str,
) -> GetCompassTaskListResponse | None:
    """Get Compass Task List

     Retrieve the list of export tasks created via Open API for the authorized seller (last 7 days).
    Supports pagination and returns task status, file_name and timestamps.

    Args:
        doc_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCompassTaskListResponse
    """

    return sync_detailed(
        client=client,
        doc_type=doc_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    doc_type: str,
) -> Response[GetCompassTaskListResponse]:
    """Get Compass Task List

     Retrieve the list of export tasks created via Open API for the authorized seller (last 7 days).
    Supports pagination and returns task status, file_name and timestamps.

    Args:
        doc_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCompassTaskListResponse]
    """

    kwargs = _get_kwargs(
        doc_type=doc_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    doc_type: str,
) -> GetCompassTaskListResponse | None:
    """Get Compass Task List

     Retrieve the list of export tasks created via Open API for the authorized seller (last 7 days).
    Supports pagination and returns task status, file_name and timestamps.

    Args:
        doc_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCompassTaskListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            doc_type=doc_type,
        )
    ).parsed
