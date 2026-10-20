from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.upload_shoppable_video_file_request import UploadShoppableVideoFileRequest
from ...models.upload_shoppable_video_file_response import UploadShoppableVideoFileResponse
from typing import cast



def _get_kwargs(
    *,
    body: UploadShoppableVideoFileRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_creator/202505/videos/video_files",
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UploadShoppableVideoFileResponse | None:
    if response.status_code == 200:
        response_200 = UploadShoppableVideoFileResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UploadShoppableVideoFileResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadShoppableVideoFileRequest,

) -> Response[UploadShoppableVideoFileResponse]:
    """ Upload Shoppable Video File

     Upload a video file before posting a shoppable video to TikTok. After the upload succeeds, call
    `POST /affiliate_creator/202505/videos` and pass the returned `video_file.id` as
    `video_info.file_id`.

    Args:
        body (UploadShoppableVideoFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadShoppableVideoFileResponse]
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
    body: UploadShoppableVideoFileRequest,

) -> UploadShoppableVideoFileResponse | None:
    """ Upload Shoppable Video File

     Upload a video file before posting a shoppable video to TikTok. After the upload succeeds, call
    `POST /affiliate_creator/202505/videos` and pass the returned `video_file.id` as
    `video_info.file_id`.

    Args:
        body (UploadShoppableVideoFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadShoppableVideoFileResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadShoppableVideoFileRequest,

) -> Response[UploadShoppableVideoFileResponse]:
    """ Upload Shoppable Video File

     Upload a video file before posting a shoppable video to TikTok. After the upload succeeds, call
    `POST /affiliate_creator/202505/videos` and pass the returned `video_file.id` as
    `video_info.file_id`.

    Args:
        body (UploadShoppableVideoFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadShoppableVideoFileResponse]
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
    body: UploadShoppableVideoFileRequest,

) -> UploadShoppableVideoFileResponse | None:
    """ Upload Shoppable Video File

     Upload a video file before posting a shoppable video to TikTok. After the upload succeeds, call
    `POST /affiliate_creator/202505/videos` and pass the returned `video_file.id` as
    `video_info.file_id`.

    Args:
        body (UploadShoppableVideoFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadShoppableVideoFileResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
