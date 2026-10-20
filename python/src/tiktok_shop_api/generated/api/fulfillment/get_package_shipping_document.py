from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_package_shipping_document_document_format import GetPackageShippingDocumentDocumentFormat
from ...models.get_package_shipping_document_document_size import GetPackageShippingDocumentDocumentSize
from ...models.get_package_shipping_document_response import GetPackageShippingDocumentResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    package_id: str,
    *,
    document_type: str,
    document_size: GetPackageShippingDocumentDocumentSize | Unset = UNSET,
    document_format: GetPackageShippingDocumentDocumentFormat | Unset = UNSET,
    shipping_period: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["document_type"] = document_type

    json_document_size: str | Unset = UNSET
    if not isinstance(document_size, Unset):
        json_document_size = document_size.value

    params["document_size"] = json_document_size

    json_document_format: str | Unset = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["document_format"] = json_document_format

    params["shipping_period"] = shipping_period


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fulfillment/202309/packages/{package_id}/shipping_documents".format(package_id=quote(str(package_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetPackageShippingDocumentResponse | None:
    if response.status_code == 200:
        response_200 = GetPackageShippingDocumentResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetPackageShippingDocumentResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
    document_type: str,
    document_size: GetPackageShippingDocumentDocumentSize | Unset = UNSET,
    document_format: GetPackageShippingDocumentDocumentFormat | Unset = UNSET,
    shipping_period: str | Unset = UNSET,

) -> Response[GetPackageShippingDocumentResponse]:
    """ Get Package Shipping Document

     For packages shipped with TikTok Shipping, use this API to retrieve the URL of the shipping document
    selected by `document_type` for the package specified by `package_id`. First call `Ship Package` to
    arrange shipment, then retrieve the document before the package is picked up.

    Args:
        package_id (str):
        document_type (str):
        document_size (GetPackageShippingDocumentDocumentSize | Unset):
        document_format (GetPackageShippingDocumentDocumentFormat | Unset):
        shipping_period (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPackageShippingDocumentResponse]
     """


    kwargs = _get_kwargs(
        package_id=package_id,
document_type=document_type,
document_size=document_size,
document_format=document_format,
shipping_period=shipping_period,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
    document_type: str,
    document_size: GetPackageShippingDocumentDocumentSize | Unset = UNSET,
    document_format: GetPackageShippingDocumentDocumentFormat | Unset = UNSET,
    shipping_period: str | Unset = UNSET,

) -> GetPackageShippingDocumentResponse | None:
    """ Get Package Shipping Document

     For packages shipped with TikTok Shipping, use this API to retrieve the URL of the shipping document
    selected by `document_type` for the package specified by `package_id`. First call `Ship Package` to
    arrange shipment, then retrieve the document before the package is picked up.

    Args:
        package_id (str):
        document_type (str):
        document_size (GetPackageShippingDocumentDocumentSize | Unset):
        document_format (GetPackageShippingDocumentDocumentFormat | Unset):
        shipping_period (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPackageShippingDocumentResponse
     """


    return sync_detailed(
        package_id=package_id,
client=client,
document_type=document_type,
document_size=document_size,
document_format=document_format,
shipping_period=shipping_period,

    ).parsed

async def asyncio_detailed(
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
    document_type: str,
    document_size: GetPackageShippingDocumentDocumentSize | Unset = UNSET,
    document_format: GetPackageShippingDocumentDocumentFormat | Unset = UNSET,
    shipping_period: str | Unset = UNSET,

) -> Response[GetPackageShippingDocumentResponse]:
    """ Get Package Shipping Document

     For packages shipped with TikTok Shipping, use this API to retrieve the URL of the shipping document
    selected by `document_type` for the package specified by `package_id`. First call `Ship Package` to
    arrange shipment, then retrieve the document before the package is picked up.

    Args:
        package_id (str):
        document_type (str):
        document_size (GetPackageShippingDocumentDocumentSize | Unset):
        document_format (GetPackageShippingDocumentDocumentFormat | Unset):
        shipping_period (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPackageShippingDocumentResponse]
     """


    kwargs = _get_kwargs(
        package_id=package_id,
document_type=document_type,
document_size=document_size,
document_format=document_format,
shipping_period=shipping_period,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
    document_type: str,
    document_size: GetPackageShippingDocumentDocumentSize | Unset = UNSET,
    document_format: GetPackageShippingDocumentDocumentFormat | Unset = UNSET,
    shipping_period: str | Unset = UNSET,

) -> GetPackageShippingDocumentResponse | None:
    """ Get Package Shipping Document

     For packages shipped with TikTok Shipping, use this API to retrieve the URL of the shipping document
    selected by `document_type` for the package specified by `package_id`. First call `Ship Package` to
    arrange shipment, then retrieve the document before the package is picked up.

    Args:
        package_id (str):
        document_type (str):
        document_size (GetPackageShippingDocumentDocumentSize | Unset):
        document_format (GetPackageShippingDocumentDocumentFormat | Unset):
        shipping_period (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPackageShippingDocumentResponse
     """


    return (await asyncio_detailed(
        package_id=package_id,
client=client,
document_type=document_type,
document_size=document_size,
document_format=document_format,
shipping_period=shipping_period,

    )).parsed
