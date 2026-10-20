from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.add_external_order_references_request import AddExternalOrderReferencesRequest
from ...models.add_external_order_references_response import AddExternalOrderReferencesResponse
from typing import cast



def _get_kwargs(
    *,
    body: AddExternalOrderReferencesRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/order/202406/orders/external_orders",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AddExternalOrderReferencesResponse | None:
    if response.status_code == 200:
        response_200 = AddExternalOrderReferencesResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AddExternalOrderReferencesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AddExternalOrderReferencesRequest,

) -> Response[AddExternalOrderReferencesResponse]:
    """ Add External Order References

     If you use an external order management system (OMS), its order and line item IDs may differ from
    the corresponding TikTok Shop IDs. Use this endpoint to attach external OMS references to up to 100
    TikTok Shop orders. To update an existing reference, call the endpoint again with the same TikTok
    Shop order and OMS. Each order is processed independently. On a successful API response, references
    for orders not listed in `data.errors` are saved; use that list to identify per-order errors.

    Args:
        body (AddExternalOrderReferencesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddExternalOrderReferencesResponse]
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
    body: AddExternalOrderReferencesRequest,

) -> AddExternalOrderReferencesResponse | None:
    """ Add External Order References

     If you use an external order management system (OMS), its order and line item IDs may differ from
    the corresponding TikTok Shop IDs. Use this endpoint to attach external OMS references to up to 100
    TikTok Shop orders. To update an existing reference, call the endpoint again with the same TikTok
    Shop order and OMS. Each order is processed independently. On a successful API response, references
    for orders not listed in `data.errors` are saved; use that list to identify per-order errors.

    Args:
        body (AddExternalOrderReferencesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddExternalOrderReferencesResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AddExternalOrderReferencesRequest,

) -> Response[AddExternalOrderReferencesResponse]:
    """ Add External Order References

     If you use an external order management system (OMS), its order and line item IDs may differ from
    the corresponding TikTok Shop IDs. Use this endpoint to attach external OMS references to up to 100
    TikTok Shop orders. To update an existing reference, call the endpoint again with the same TikTok
    Shop order and OMS. Each order is processed independently. On a successful API response, references
    for orders not listed in `data.errors` are saved; use that list to identify per-order errors.

    Args:
        body (AddExternalOrderReferencesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddExternalOrderReferencesResponse]
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
    body: AddExternalOrderReferencesRequest,

) -> AddExternalOrderReferencesResponse | None:
    """ Add External Order References

     If you use an external order management system (OMS), its order and line item IDs may differ from
    the corresponding TikTok Shop IDs. Use this endpoint to attach external OMS references to up to 100
    TikTok Shop orders. To update an existing reference, call the endpoint again with the same TikTok
    Shop order and OMS. Each order is processed independently. On a successful API response, references
    for orders not listed in `data.errors` are saved; use that list to identify per-order errors.

    Args:
        body (AddExternalOrderReferencesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddExternalOrderReferencesResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
