from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.list_available_inbound_methods_request import ListAvailableInboundMethodsRequest
from ...models.list_available_inbound_methods_response import ListAvailableInboundMethodsResponse
from typing import cast



def _get_kwargs(
    *,
    body: ListAvailableInboundMethodsRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fbt/202602/list_available_inbound_method",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ListAvailableInboundMethodsResponse | None:
    if response.status_code == 200:
        response_200 = ListAvailableInboundMethodsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ListAvailableInboundMethodsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ListAvailableInboundMethodsRequest,

) -> Response[ListAvailableInboundMethodsResponse]:
    """ List Available Inbound Methods

     Retrieves valid inbound shipping methods and arrival time windows for a specific plan. After
    selecting an `inbound_method` and one complete arrival time window, call **Get Inbound Method
    Detail** (`POST /fbt/202602/inbound_method_detail`) using the same `plan_id`, the selected
    `inbound_method`, and that window's exact `start_timestamp` and `end_timestamp` pair as
    `estimate_arrival_time`.

    Args:
        body (ListAvailableInboundMethodsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAvailableInboundMethodsResponse]
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
    body: ListAvailableInboundMethodsRequest,

) -> ListAvailableInboundMethodsResponse | None:
    """ List Available Inbound Methods

     Retrieves valid inbound shipping methods and arrival time windows for a specific plan. After
    selecting an `inbound_method` and one complete arrival time window, call **Get Inbound Method
    Detail** (`POST /fbt/202602/inbound_method_detail`) using the same `plan_id`, the selected
    `inbound_method`, and that window's exact `start_timestamp` and `end_timestamp` pair as
    `estimate_arrival_time`.

    Args:
        body (ListAvailableInboundMethodsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAvailableInboundMethodsResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ListAvailableInboundMethodsRequest,

) -> Response[ListAvailableInboundMethodsResponse]:
    """ List Available Inbound Methods

     Retrieves valid inbound shipping methods and arrival time windows for a specific plan. After
    selecting an `inbound_method` and one complete arrival time window, call **Get Inbound Method
    Detail** (`POST /fbt/202602/inbound_method_detail`) using the same `plan_id`, the selected
    `inbound_method`, and that window's exact `start_timestamp` and `end_timestamp` pair as
    `estimate_arrival_time`.

    Args:
        body (ListAvailableInboundMethodsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAvailableInboundMethodsResponse]
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
    body: ListAvailableInboundMethodsRequest,

) -> ListAvailableInboundMethodsResponse | None:
    """ List Available Inbound Methods

     Retrieves valid inbound shipping methods and arrival time windows for a specific plan. After
    selecting an `inbound_method` and one complete arrival time window, call **Get Inbound Method
    Detail** (`POST /fbt/202602/inbound_method_detail`) using the same `plan_id`, the selected
    `inbound_method`, and that window's exact `start_timestamp` and `end_timestamp` pair as
    `estimate_arrival_time`.

    Args:
        body (ListAvailableInboundMethodsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAvailableInboundMethodsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
