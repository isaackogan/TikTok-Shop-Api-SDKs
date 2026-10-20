from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.recover_products_request import RecoverProductsRequest
from ...models.recover_products_response import RecoverProductsResponse
from typing import cast



def _get_kwargs(
    *,
    body: RecoverProductsRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202309/products/recover",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RecoverProductsResponse | None:
    if response.status_code == 200:
        response_200 = RecoverProductsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RecoverProductsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RecoverProductsRequest,

) -> Response[RecoverProductsResponse]:
    """ Recover Products

     Recover products that are in the `Deleted` status. The status changes to `Seller_deactivated` after
    recovery.

    Args:
        body (RecoverProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RecoverProductsResponse]
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
    body: RecoverProductsRequest,

) -> RecoverProductsResponse | None:
    """ Recover Products

     Recover products that are in the `Deleted` status. The status changes to `Seller_deactivated` after
    recovery.

    Args:
        body (RecoverProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RecoverProductsResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RecoverProductsRequest,

) -> Response[RecoverProductsResponse]:
    """ Recover Products

     Recover products that are in the `Deleted` status. The status changes to `Seller_deactivated` after
    recovery.

    Args:
        body (RecoverProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RecoverProductsResponse]
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
    body: RecoverProductsRequest,

) -> RecoverProductsResponse | None:
    """ Recover Products

     Recover products that are in the `Deleted` status. The status changes to `Seller_deactivated` after
    recovery.

    Args:
        body (RecoverProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RecoverProductsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
