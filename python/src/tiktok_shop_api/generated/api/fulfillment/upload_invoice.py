from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.upload_invoice_request import UploadInvoiceRequest
from ...models.upload_invoice_response import UploadInvoiceResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: UploadInvoiceRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fulfillment/202502/invoice/upload",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UploadInvoiceResponse | None:
    if response.status_code == 200:
        response_200 = UploadInvoiceResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UploadInvoiceResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadInvoiceRequest | Unset = UNSET,

) -> Response[UploadInvoiceResponse]:
    """ Upload Invoice

     Upload the invoice document.
    **Note**: Applicable only for local sellers in the Brazil market.

    Args:
        body (UploadInvoiceRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadInvoiceResponse]
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
    body: UploadInvoiceRequest | Unset = UNSET,

) -> UploadInvoiceResponse | None:
    """ Upload Invoice

     Upload the invoice document.
    **Note**: Applicable only for local sellers in the Brazil market.

    Args:
        body (UploadInvoiceRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadInvoiceResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadInvoiceRequest | Unset = UNSET,

) -> Response[UploadInvoiceResponse]:
    """ Upload Invoice

     Upload the invoice document.
    **Note**: Applicable only for local sellers in the Brazil market.

    Args:
        body (UploadInvoiceRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadInvoiceResponse]
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
    body: UploadInvoiceRequest | Unset = UNSET,

) -> UploadInvoiceResponse | None:
    """ Upload Invoice

     Upload the invoice document.
    **Note**: Applicable only for local sellers in the Brazil market.

    Args:
        body (UploadInvoiceRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadInvoiceResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
