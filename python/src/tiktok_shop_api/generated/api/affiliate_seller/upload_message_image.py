from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.upload_message_image_request import UploadMessageImageRequest
from ...models.upload_message_image_response import UploadMessageImageResponse
from ...types import Response


def _get_kwargs(
    *,
    body: UploadMessageImageRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_seller/202511/images/upload",
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UploadMessageImageResponse | None:
    if response.status_code == 200:
        response_200 = UploadMessageImageResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UploadMessageImageResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadMessageImageRequest,
) -> Response[UploadMessageImageResponse]:
    """Upload Message Image

     You must use this API to upload the image first, before sending an image as a message using [Send IM
    Messsage](https://partner.tiktokshop.com/docv2/page/send-im-message-202412)

    Args:
        body (UploadMessageImageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadMessageImageResponse]
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
    body: UploadMessageImageRequest,
) -> UploadMessageImageResponse | None:
    """Upload Message Image

     You must use this API to upload the image first, before sending an image as a message using [Send IM
    Messsage](https://partner.tiktokshop.com/docv2/page/send-im-message-202412)

    Args:
        body (UploadMessageImageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadMessageImageResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadMessageImageRequest,
) -> Response[UploadMessageImageResponse]:
    """Upload Message Image

     You must use this API to upload the image first, before sending an image as a message using [Send IM
    Messsage](https://partner.tiktokshop.com/docv2/page/send-im-message-202412)

    Args:
        body (UploadMessageImageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadMessageImageResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UploadMessageImageRequest,
) -> UploadMessageImageResponse | None:
    """Upload Message Image

     You must use this API to upload the image first, before sending an image as a message using [Send IM
    Messsage](https://partner.tiktokshop.com/docv2/page/send-im-message-202412)

    Args:
        body (UploadMessageImageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadMessageImageResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
