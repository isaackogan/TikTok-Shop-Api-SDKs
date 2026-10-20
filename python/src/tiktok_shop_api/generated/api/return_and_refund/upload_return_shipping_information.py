from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.upload_return_shipping_information_request import UploadReturnShippingInformationRequest
from ...models.upload_return_shipping_information_response import UploadReturnShippingInformationResponse
from ...models.upload_return_shipping_information_return_id_type import UploadReturnShippingInformationReturnIdType
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: UploadReturnShippingInformationRequest,
    return_ids: list[str],
    return_id_type: UploadReturnShippingInformationReturnIdType | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    json_return_ids = return_ids


    params["return_ids"] = json_return_ids

    json_return_id_type: str | Unset = UNSET
    if not isinstance(return_id_type, Unset):
        json_return_id_type = return_id_type.value

    params["return_id_type"] = json_return_id_type


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/return_refund/202405/returns/shipping_documents",
        "params": params,
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UploadReturnShippingInformationResponse | None:
    if response.status_code == 200:
        response_200 = UploadReturnShippingInformationResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UploadReturnShippingInformationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadReturnShippingInformationRequest,
    return_ids: list[str],
    return_id_type: UploadReturnShippingInformationReturnIdType | Unset = UNSET,

) -> Response[UploadReturnShippingInformationResponse]:
    """ Upload Return Shipping Information

     Use this API to upload return shipping documents, tracking numbers, and carriers for buyers.

    Args:
        return_ids (list[str]):
        return_id_type (UploadReturnShippingInformationReturnIdType | Unset):
        body (UploadReturnShippingInformationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadReturnShippingInformationResponse]
     """


    kwargs = _get_kwargs(
        body=body,
return_ids=return_ids,
return_id_type=return_id_type,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: UploadReturnShippingInformationRequest,
    return_ids: list[str],
    return_id_type: UploadReturnShippingInformationReturnIdType | Unset = UNSET,

) -> UploadReturnShippingInformationResponse | None:
    """ Upload Return Shipping Information

     Use this API to upload return shipping documents, tracking numbers, and carriers for buyers.

    Args:
        return_ids (list[str]):
        return_id_type (UploadReturnShippingInformationReturnIdType | Unset):
        body (UploadReturnShippingInformationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadReturnShippingInformationResponse
     """


    return sync_detailed(
        client=client,
body=body,
return_ids=return_ids,
return_id_type=return_id_type,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadReturnShippingInformationRequest,
    return_ids: list[str],
    return_id_type: UploadReturnShippingInformationReturnIdType | Unset = UNSET,

) -> Response[UploadReturnShippingInformationResponse]:
    """ Upload Return Shipping Information

     Use this API to upload return shipping documents, tracking numbers, and carriers for buyers.

    Args:
        return_ids (list[str]):
        return_id_type (UploadReturnShippingInformationReturnIdType | Unset):
        body (UploadReturnShippingInformationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadReturnShippingInformationResponse]
     """


    kwargs = _get_kwargs(
        body=body,
return_ids=return_ids,
return_id_type=return_id_type,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UploadReturnShippingInformationRequest,
    return_ids: list[str],
    return_id_type: UploadReturnShippingInformationReturnIdType | Unset = UNSET,

) -> UploadReturnShippingInformationResponse | None:
    """ Upload Return Shipping Information

     Use this API to upload return shipping documents, tracking numbers, and carriers for buyers.

    Args:
        return_ids (list[str]):
        return_id_type (UploadReturnShippingInformationReturnIdType | Unset):
        body (UploadReturnShippingInformationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadReturnShippingInformationResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
return_ids=return_ids,
return_id_type=return_id_type,

    )).parsed
