from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.upload_file_init_request import UploadFileInitRequest
from ...models.upload_file_init_response import UploadFileInitResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UploadFileInitRequest,
    shop_cipher: str | Unset = UNSET,
    category_asset_cipher: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["shop_cipher"] = shop_cipher

    params["category_asset_cipher"] = category_asset_cipher

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/open/202512/file/init",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UploadFileInitResponse | None:
    if response.status_code == 200:
        response_200 = UploadFileInitResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UploadFileInitResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadFileInitRequest,
    shop_cipher: str | Unset = UNSET,
    category_asset_cipher: str | Unset = UNSET,
) -> Response[UploadFileInitResponse]:
    """Upload File Init

     Use this API to initialize a file upload session. Then upload the file to the returned upload URL.
    Files of 5 MiB (5,242,880 bytes) or less must be uploaded as a single, non-chunked request with
    `total_chunk_count` set to `1`; larger files use a multipart upload. After the upload step returns a
    ResourceId, pass that ResourceId to the API for the target path.

    For more details, see https://partner.tiktokshop.com/docv2/page/wfi3nz36.

    Args:
        shop_cipher (str | Unset):
        category_asset_cipher (str | Unset):
        body (UploadFileInitRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadFileInitResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        shop_cipher=shop_cipher,
        category_asset_cipher=category_asset_cipher,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: UploadFileInitRequest,
    shop_cipher: str | Unset = UNSET,
    category_asset_cipher: str | Unset = UNSET,
) -> UploadFileInitResponse | None:
    """Upload File Init

     Use this API to initialize a file upload session. Then upload the file to the returned upload URL.
    Files of 5 MiB (5,242,880 bytes) or less must be uploaded as a single, non-chunked request with
    `total_chunk_count` set to `1`; larger files use a multipart upload. After the upload step returns a
    ResourceId, pass that ResourceId to the API for the target path.

    For more details, see https://partner.tiktokshop.com/docv2/page/wfi3nz36.

    Args:
        shop_cipher (str | Unset):
        category_asset_cipher (str | Unset):
        body (UploadFileInitRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadFileInitResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        shop_cipher=shop_cipher,
        category_asset_cipher=category_asset_cipher,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadFileInitRequest,
    shop_cipher: str | Unset = UNSET,
    category_asset_cipher: str | Unset = UNSET,
) -> Response[UploadFileInitResponse]:
    """Upload File Init

     Use this API to initialize a file upload session. Then upload the file to the returned upload URL.
    Files of 5 MiB (5,242,880 bytes) or less must be uploaded as a single, non-chunked request with
    `total_chunk_count` set to `1`; larger files use a multipart upload. After the upload step returns a
    ResourceId, pass that ResourceId to the API for the target path.

    For more details, see https://partner.tiktokshop.com/docv2/page/wfi3nz36.

    Args:
        shop_cipher (str | Unset):
        category_asset_cipher (str | Unset):
        body (UploadFileInitRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadFileInitResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        shop_cipher=shop_cipher,
        category_asset_cipher=category_asset_cipher,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UploadFileInitRequest,
    shop_cipher: str | Unset = UNSET,
    category_asset_cipher: str | Unset = UNSET,
) -> UploadFileInitResponse | None:
    """Upload File Init

     Use this API to initialize a file upload session. Then upload the file to the returned upload URL.
    Files of 5 MiB (5,242,880 bytes) or less must be uploaded as a single, non-chunked request with
    `total_chunk_count` set to `1`; larger files use a multipart upload. After the upload step returns a
    ResourceId, pass that ResourceId to the API for the target path.

    For more details, see https://partner.tiktokshop.com/docv2/page/wfi3nz36.

    Args:
        shop_cipher (str | Unset):
        category_asset_cipher (str | Unset):
        body (UploadFileInitRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadFileInitResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            shop_cipher=shop_cipher,
            category_asset_cipher=category_asset_cipher,
        )
    ).parsed
