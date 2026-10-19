from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.upload_shoppable_photo_file_request import UploadShoppablePhotoFileRequest
from ...models.upload_shoppable_photo_file_response import UploadShoppablePhotoFileResponse
from ...types import Response


def _get_kwargs(
    *,
    body: UploadShoppablePhotoFileRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_creator/202511/photos/photo_files",
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UploadShoppablePhotoFileResponse | None:
    if response.status_code == 200:
        response_200 = UploadShoppablePhotoFileResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UploadShoppablePhotoFileResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadShoppablePhotoFileRequest,
) -> Response[UploadShoppablePhotoFileResponse]:
    """Upload Shoppable Photo File

     Use this API to upload the photos before photo posting. It returns the photo_file_uri for each
    uploaded image

    Args:
        body (UploadShoppablePhotoFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadShoppablePhotoFileResponse]
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
    body: UploadShoppablePhotoFileRequest,
) -> UploadShoppablePhotoFileResponse | None:
    """Upload Shoppable Photo File

     Use this API to upload the photos before photo posting. It returns the photo_file_uri for each
    uploaded image

    Args:
        body (UploadShoppablePhotoFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadShoppablePhotoFileResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadShoppablePhotoFileRequest,
) -> Response[UploadShoppablePhotoFileResponse]:
    """Upload Shoppable Photo File

     Use this API to upload the photos before photo posting. It returns the photo_file_uri for each
    uploaded image

    Args:
        body (UploadShoppablePhotoFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadShoppablePhotoFileResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UploadShoppablePhotoFileRequest,
) -> UploadShoppablePhotoFileResponse | None:
    """Upload Shoppable Photo File

     Use this API to upload the photos before photo posting. It returns the photo_file_uri for each
    uploaded image

    Args:
        body (UploadShoppablePhotoFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadShoppablePhotoFileResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
