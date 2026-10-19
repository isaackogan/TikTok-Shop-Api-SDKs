from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.upload_image_for_buyer_messages_request import UploadImageForBuyerMessagesRequest
from ...models.upload_image_for_buyer_messages_response import UploadImageForBuyerMessagesResponse
from ...types import Response


def _get_kwargs(
    *,
    body: UploadImageForBuyerMessagesRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/customer_service/202309/images/upload",
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UploadImageForBuyerMessagesResponse | None:
    if response.status_code == 200:
        response_200 = UploadImageForBuyerMessagesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UploadImageForBuyerMessagesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadImageForBuyerMessagesRequest,
) -> Response[UploadImageForBuyerMessagesResponse]:
    """Upload Image for Buyer Messages

     You must use this API to upload the image first, before sending an image as a message using [Send
    Message](650a58bbbace3e02b7556286).

    Args:
        body (UploadImageForBuyerMessagesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadImageForBuyerMessagesResponse]
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
    body: UploadImageForBuyerMessagesRequest,
) -> UploadImageForBuyerMessagesResponse | None:
    """Upload Image for Buyer Messages

     You must use this API to upload the image first, before sending an image as a message using [Send
    Message](650a58bbbace3e02b7556286).

    Args:
        body (UploadImageForBuyerMessagesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadImageForBuyerMessagesResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadImageForBuyerMessagesRequest,
) -> Response[UploadImageForBuyerMessagesResponse]:
    """Upload Image for Buyer Messages

     You must use this API to upload the image first, before sending an image as a message using [Send
    Message](650a58bbbace3e02b7556286).

    Args:
        body (UploadImageForBuyerMessagesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadImageForBuyerMessagesResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UploadImageForBuyerMessagesRequest,
) -> UploadImageForBuyerMessagesResponse | None:
    """Upload Image for Buyer Messages

     You must use this API to upload the image first, before sending an image as a message using [Send
    Message](650a58bbbace3e02b7556286).

    Args:
        body (UploadImageForBuyerMessagesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadImageForBuyerMessagesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
