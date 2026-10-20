from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_compass_offline_export_task_request import CreateCompassOfflineExportTaskRequest
from ...models.create_compass_offline_export_task_response import CreateCompassOfflineExportTaskResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: CreateCompassOfflineExportTaskRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_seller/202603/compass/offline_task",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateCompassOfflineExportTaskResponse | None:
    if response.status_code == 200:
        response_200 = CreateCompassOfflineExportTaskResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateCompassOfflineExportTaskResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateCompassOfflineExportTaskRequest | Unset = UNSET,

) -> Response[CreateCompassOfflineExportTaskResponse]:
    """ Create Compass Offline Export Task

     Create an asynchronous offline export task for the specified doc_type and plan_type within a given
    time window. Returns a task_id for subsequent status query and file download.

    Args:
        body (CreateCompassOfflineExportTaskRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateCompassOfflineExportTaskResponse]
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
    body: CreateCompassOfflineExportTaskRequest | Unset = UNSET,

) -> CreateCompassOfflineExportTaskResponse | None:
    """ Create Compass Offline Export Task

     Create an asynchronous offline export task for the specified doc_type and plan_type within a given
    time window. Returns a task_id for subsequent status query and file download.

    Args:
        body (CreateCompassOfflineExportTaskRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateCompassOfflineExportTaskResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateCompassOfflineExportTaskRequest | Unset = UNSET,

) -> Response[CreateCompassOfflineExportTaskResponse]:
    """ Create Compass Offline Export Task

     Create an asynchronous offline export task for the specified doc_type and plan_type within a given
    time window. Returns a task_id for subsequent status query and file download.

    Args:
        body (CreateCompassOfflineExportTaskRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateCompassOfflineExportTaskResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateCompassOfflineExportTaskRequest | Unset = UNSET,

) -> CreateCompassOfflineExportTaskResponse | None:
    """ Create Compass Offline Export Task

     Create an asynchronous offline export task for the specified doc_type and plan_type within a given
    time window. Returns a task_id for subsequent status query and file download.

    Args:
        body (CreateCompassOfflineExportTaskRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateCompassOfflineExportTaskResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
