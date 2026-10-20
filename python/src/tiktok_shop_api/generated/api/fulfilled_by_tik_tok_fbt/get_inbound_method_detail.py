from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_inbound_method_detail_request import GetInboundMethodDetailRequest
from ...models.get_inbound_method_detail_response import GetInboundMethodDetailResponse
from typing import cast



def _get_kwargs(
    *,
    body: GetInboundMethodDetailRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fbt/202602/inbound_method_detail",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetInboundMethodDetailResponse | None:
    if response.status_code == 200:
        response_200 = GetInboundMethodDetailResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetInboundMethodDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetInboundMethodDetailRequest,

) -> Response[GetInboundMethodDetailResponse]:
    """ Get Inbound Method Detail

     Retrieves placement details for an inbound plan. First call the List Available Inbound Methods API
    for the plan, then use the `inbound_method` and estimated arrival window from the same returned
    option. The response reports the placement task status and, when available, placement options with
    shipment allocations; `ONE_HUB` options can also include an estimated placement fee.

    Args:
        body (GetInboundMethodDetailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetInboundMethodDetailResponse]
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
    body: GetInboundMethodDetailRequest,

) -> GetInboundMethodDetailResponse | None:
    """ Get Inbound Method Detail

     Retrieves placement details for an inbound plan. First call the List Available Inbound Methods API
    for the plan, then use the `inbound_method` and estimated arrival window from the same returned
    option. The response reports the placement task status and, when available, placement options with
    shipment allocations; `ONE_HUB` options can also include an estimated placement fee.

    Args:
        body (GetInboundMethodDetailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetInboundMethodDetailResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetInboundMethodDetailRequest,

) -> Response[GetInboundMethodDetailResponse]:
    """ Get Inbound Method Detail

     Retrieves placement details for an inbound plan. First call the List Available Inbound Methods API
    for the plan, then use the `inbound_method` and estimated arrival window from the same returned
    option. The response reports the placement task status and, when available, placement options with
    shipment allocations; `ONE_HUB` options can also include an estimated placement fee.

    Args:
        body (GetInboundMethodDetailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetInboundMethodDetailResponse]
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
    body: GetInboundMethodDetailRequest,

) -> GetInboundMethodDetailResponse | None:
    """ Get Inbound Method Detail

     Retrieves placement details for an inbound plan. First call the List Available Inbound Methods API
    for the plan, then use the `inbound_method` and estimated arrival window from the same returned
    option. The response reports the placement task status and, when available, placement options with
    shipment allocations; `ONE_HUB` options can also include an estimated placement fee.

    Args:
        body (GetInboundMethodDetailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetInboundMethodDetailResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
