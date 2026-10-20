from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.upload_product_file_request import UploadProductFileRequest
from ...models.upload_product_file_response import UploadProductFileResponse
from ...types import Response


def _get_kwargs(
    *,
    body: UploadProductFileRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202309/files/upload",
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UploadProductFileResponse | None:
    if response.status_code == 200:
        response_200 = UploadProductFileResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UploadProductFileResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadProductFileRequest,
) -> Response[UploadProductFileResponse]:
    """Upload Product File

     Upload non-image files, such as PDF or video to TikTok Shop.
    Use this API when you need to add videos to your product to improve the shopping experience, or
    submit certifications or reports to meet TikTok Shop requirements for listing restricted products.
    **Note**: Retain the file ID from the response and pass it when creating or editing a product to
    associate the file with the product.

    Args:
        body (UploadProductFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadProductFileResponse]
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
    body: UploadProductFileRequest,
) -> UploadProductFileResponse | None:
    """Upload Product File

     Upload non-image files, such as PDF or video to TikTok Shop.
    Use this API when you need to add videos to your product to improve the shopping experience, or
    submit certifications or reports to meet TikTok Shop requirements for listing restricted products.
    **Note**: Retain the file ID from the response and pass it when creating or editing a product to
    associate the file with the product.

    Args:
        body (UploadProductFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadProductFileResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadProductFileRequest,
) -> Response[UploadProductFileResponse]:
    """Upload Product File

     Upload non-image files, such as PDF or video to TikTok Shop.
    Use this API when you need to add videos to your product to improve the shopping experience, or
    submit certifications or reports to meet TikTok Shop requirements for listing restricted products.
    **Note**: Retain the file ID from the response and pass it when creating or editing a product to
    associate the file with the product.

    Args:
        body (UploadProductFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadProductFileResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UploadProductFileRequest,
) -> UploadProductFileResponse | None:
    """Upload Product File

     Upload non-image files, such as PDF or video to TikTok Shop.
    Use this API when you need to add videos to your product to improve the shopping experience, or
    submit certifications or reports to meet TikTok Shop requirements for listing restricted products.
    **Note**: Retain the file ID from the response and pass it when creating or editing a product to
    associate the file with the product.

    Args:
        body (UploadProductFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadProductFileResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
