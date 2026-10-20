from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.download_compass_task_file_response import DownloadCompassTaskFileResponse
from typing import cast



def _get_kwargs(
    task_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/affiliate_seller/202603/compass/offline_tasks/{task_id}/file".format(task_id=quote(str(task_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DownloadCompassTaskFileResponse | None:
    if response.status_code == 200:
        response_200 = DownloadCompassTaskFileResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DownloadCompassTaskFileResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    task_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[DownloadCompassTaskFileResponse]:
    """ Download Compass Task File

     Download the result file of a completed export task by taskId. Requires ownership validation;
    returns file.

    Args:
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DownloadCompassTaskFileResponse]
     """


    kwargs = _get_kwargs(
        task_id=task_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    task_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> DownloadCompassTaskFileResponse | None:
    """ Download Compass Task File

     Download the result file of a completed export task by taskId. Requires ownership validation;
    returns file.

    Args:
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DownloadCompassTaskFileResponse
     """


    return sync_detailed(
        task_id=task_id,
client=client,

    ).parsed

async def asyncio_detailed(
    task_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[DownloadCompassTaskFileResponse]:
    """ Download Compass Task File

     Download the result file of a completed export task by taskId. Requires ownership validation;
    returns file.

    Args:
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DownloadCompassTaskFileResponse]
     """


    kwargs = _get_kwargs(
        task_id=task_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    task_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> DownloadCompassTaskFileResponse | None:
    """ Download Compass Task File

     Download the result file of a completed export task by taskId. Requires ownership validation;
    returns file.

    Args:
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DownloadCompassTaskFileResponse
     """


    return (await asyncio_detailed(
        task_id=task_id,
client=client,

    )).parsed
