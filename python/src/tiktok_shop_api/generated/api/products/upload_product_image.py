from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.upload_product_image_request import UploadProductImageRequest
from ...models.upload_product_image_response import UploadProductImageResponse
from ...types import Response


def _get_kwargs(
    *,
    body: UploadProductImageRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202309/images/upload",
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UploadProductImageResponse | None:
    if response.status_code == 200:
        response_200 = UploadProductImageResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UploadProductImageResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadProductImageRequest,
) -> Response[UploadProductImageResponse]:
    """Upload Product Image

     Upload a local image to TikTok Shop for use as a product image, variant image, size chart,
    certification image, or another supported image use case.

    **Note**:
    - All images used in TikTok Shop products must be uploaded through this API. You cannot use image
    URLs that are not hosted by TikTok Shop.
    - Store `data.uri` to associate the uploaded image with a product when creating or editing it. Store
    `data.url` when you need to display the image in a product description by using an HTML `<img>` tag.

    Args:
        body (UploadProductImageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadProductImageResponse]
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
    body: UploadProductImageRequest,
) -> UploadProductImageResponse | None:
    """Upload Product Image

     Upload a local image to TikTok Shop for use as a product image, variant image, size chart,
    certification image, or another supported image use case.

    **Note**:
    - All images used in TikTok Shop products must be uploaded through this API. You cannot use image
    URLs that are not hosted by TikTok Shop.
    - Store `data.uri` to associate the uploaded image with a product when creating or editing it. Store
    `data.url` when you need to display the image in a product description by using an HTML `<img>` tag.

    Args:
        body (UploadProductImageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadProductImageResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadProductImageRequest,
) -> Response[UploadProductImageResponse]:
    """Upload Product Image

     Upload a local image to TikTok Shop for use as a product image, variant image, size chart,
    certification image, or another supported image use case.

    **Note**:
    - All images used in TikTok Shop products must be uploaded through this API. You cannot use image
    URLs that are not hosted by TikTok Shop.
    - Store `data.uri` to associate the uploaded image with a product when creating or editing it. Store
    `data.url` when you need to display the image in a product description by using an HTML `<img>` tag.

    Args:
        body (UploadProductImageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadProductImageResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UploadProductImageRequest,
) -> UploadProductImageResponse | None:
    """Upload Product Image

     Upload a local image to TikTok Shop for use as a product image, variant image, size chart,
    certification image, or another supported image use case.

    **Note**:
    - All images used in TikTok Shop products must be uploaded through this API. You cannot use image
    URLs that are not hosted by TikTok Shop.
    - Store `data.uri` to associate the uploaded image with a product when creating or editing it. Store
    `data.url` when you need to display the image in a product description by using an HTML `<img>` tag.

    Args:
        body (UploadProductImageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadProductImageResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
