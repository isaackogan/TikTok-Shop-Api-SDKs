from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.upload_seller_materials_request import UploadSellerMaterialsRequest
from ...models.upload_seller_materials_response import UploadSellerMaterialsResponse
from typing import cast



def _get_kwargs(
    *,
    body: UploadSellerMaterialsRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/seller/202611/materials/upload",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UploadSellerMaterialsResponse | None:
    if response.status_code == 200:
        response_200 = UploadSellerMaterialsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UploadSellerMaterialsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadSellerMaterialsRequest,

) -> Response[UploadSellerMaterialsResponse]:
    """ Upload Seller Materials

     Upload image materials for the current shop. Use `materials` for `ONE_PRODUCT_ONE_IMAGE` and
    `material_groups` for `ONE_PRODUCT_MULTIPLE_IMAGES`. Provide exactly one mode payload per request.

    Args:
        body (UploadSellerMaterialsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadSellerMaterialsResponse]
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
    body: UploadSellerMaterialsRequest,

) -> UploadSellerMaterialsResponse | None:
    """ Upload Seller Materials

     Upload image materials for the current shop. Use `materials` for `ONE_PRODUCT_ONE_IMAGE` and
    `material_groups` for `ONE_PRODUCT_MULTIPLE_IMAGES`. Provide exactly one mode payload per request.

    Args:
        body (UploadSellerMaterialsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadSellerMaterialsResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadSellerMaterialsRequest,

) -> Response[UploadSellerMaterialsResponse]:
    """ Upload Seller Materials

     Upload image materials for the current shop. Use `materials` for `ONE_PRODUCT_ONE_IMAGE` and
    `material_groups` for `ONE_PRODUCT_MULTIPLE_IMAGES`. Provide exactly one mode payload per request.

    Args:
        body (UploadSellerMaterialsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadSellerMaterialsResponse]
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
    body: UploadSellerMaterialsRequest,

) -> UploadSellerMaterialsResponse | None:
    """ Upload Seller Materials

     Upload image materials for the current shop. Use `materials` for `ONE_PRODUCT_ONE_IMAGE` and
    `material_groups` for `ONE_PRODUCT_MULTIPLE_IMAGES`. Provide exactly one mode payload per request.

    Args:
        body (UploadSellerMaterialsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadSellerMaterialsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
