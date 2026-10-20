from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.upload_proof_of_delivery_file_request import UploadProofOfDeliveryFileRequest
from ...models.upload_proof_of_delivery_file_response import UploadProofOfDeliveryFileResponse
from typing import cast



def _get_kwargs(
    *,
    body: UploadProofOfDeliveryFileRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fulfillment/202309/files/upload",
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UploadProofOfDeliveryFileResponse | None:
    if response.status_code == 200:
        response_200 = UploadProofOfDeliveryFileResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UploadProofOfDeliveryFileResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadProofOfDeliveryFileRequest,

) -> Response[UploadProofOfDeliveryFileResponse]:
    """ Upload Proof of Delivery File

     This API is used for the seller to upload the proof of delivery file for a package, and to generate
    the URL of the corresponding file. The generated URL is used for the [Update Package Delivery Status
    API](https://partner.tiktokshop.com/docv2/page/650aa332c16ffe02b8f0ba82?external_id=650aa332c16ffe02
    b8f0ba82).

    This API only supports uploading qualification files in `PDF` format. The file size can not exceed
    10MB.

    Note: Only sellers utilizing the SOF (Seller Own Fleet) capability can use this API.

    Args:
        body (UploadProofOfDeliveryFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadProofOfDeliveryFileResponse]
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
    body: UploadProofOfDeliveryFileRequest,

) -> UploadProofOfDeliveryFileResponse | None:
    """ Upload Proof of Delivery File

     This API is used for the seller to upload the proof of delivery file for a package, and to generate
    the URL of the corresponding file. The generated URL is used for the [Update Package Delivery Status
    API](https://partner.tiktokshop.com/docv2/page/650aa332c16ffe02b8f0ba82?external_id=650aa332c16ffe02
    b8f0ba82).

    This API only supports uploading qualification files in `PDF` format. The file size can not exceed
    10MB.

    Note: Only sellers utilizing the SOF (Seller Own Fleet) capability can use this API.

    Args:
        body (UploadProofOfDeliveryFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadProofOfDeliveryFileResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadProofOfDeliveryFileRequest,

) -> Response[UploadProofOfDeliveryFileResponse]:
    """ Upload Proof of Delivery File

     This API is used for the seller to upload the proof of delivery file for a package, and to generate
    the URL of the corresponding file. The generated URL is used for the [Update Package Delivery Status
    API](https://partner.tiktokshop.com/docv2/page/650aa332c16ffe02b8f0ba82?external_id=650aa332c16ffe02
    b8f0ba82).

    This API only supports uploading qualification files in `PDF` format. The file size can not exceed
    10MB.

    Note: Only sellers utilizing the SOF (Seller Own Fleet) capability can use this API.

    Args:
        body (UploadProofOfDeliveryFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadProofOfDeliveryFileResponse]
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
    body: UploadProofOfDeliveryFileRequest,

) -> UploadProofOfDeliveryFileResponse | None:
    """ Upload Proof of Delivery File

     This API is used for the seller to upload the proof of delivery file for a package, and to generate
    the URL of the corresponding file. The generated URL is used for the [Update Package Delivery Status
    API](https://partner.tiktokshop.com/docv2/page/650aa332c16ffe02b8f0ba82?external_id=650aa332c16ffe02
    b8f0ba82).

    This API only supports uploading qualification files in `PDF` format. The file size can not exceed
    10MB.

    Note: Only sellers utilizing the SOF (Seller Own Fleet) capability can use this API.

    Args:
        body (UploadProofOfDeliveryFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadProofOfDeliveryFileResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
