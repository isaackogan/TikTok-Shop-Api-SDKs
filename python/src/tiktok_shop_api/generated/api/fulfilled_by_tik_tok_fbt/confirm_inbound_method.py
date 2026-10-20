from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.confirm_inbound_method_request import ConfirmInboundMethodRequest
from ...models.confirm_inbound_method_response import ConfirmInboundMethodResponse
from typing import cast



def _get_kwargs(
    *,
    body: ConfirmInboundMethodRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fbt/202603/confirm_inbound_method",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConfirmInboundMethodResponse | None:
    if response.status_code == 200:
        response_200 = ConfirmInboundMethodResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConfirmInboundMethodResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ConfirmInboundMethodRequest,

) -> Response[ConfirmInboundMethodResponse]:
    """ Confirm Inbound Method

     Confirm a currently available warehouse placement option for an FBT inbound plan. First call the
    List Available Inbound Methods API and select an `inbound_method` with one exact
    `estimate_arrival_time` window. Then call the Get Inbound Method Detail API with that selection and
    choose a returned `placement_option_id`. Confirm using the `placement_option_id`, `inbound_method`,
    and `estimate_arrival_time` from the same selection. If the option has expired, repeat both
    prerequisite calls to obtain a current selection and a new `placement_option_id`, then retry. The
    response contains the child inbound order IDs generated for the plan.

    Args:
        body (ConfirmInboundMethodRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfirmInboundMethodResponse]
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
    body: ConfirmInboundMethodRequest,

) -> ConfirmInboundMethodResponse | None:
    """ Confirm Inbound Method

     Confirm a currently available warehouse placement option for an FBT inbound plan. First call the
    List Available Inbound Methods API and select an `inbound_method` with one exact
    `estimate_arrival_time` window. Then call the Get Inbound Method Detail API with that selection and
    choose a returned `placement_option_id`. Confirm using the `placement_option_id`, `inbound_method`,
    and `estimate_arrival_time` from the same selection. If the option has expired, repeat both
    prerequisite calls to obtain a current selection and a new `placement_option_id`, then retry. The
    response contains the child inbound order IDs generated for the plan.

    Args:
        body (ConfirmInboundMethodRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfirmInboundMethodResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ConfirmInboundMethodRequest,

) -> Response[ConfirmInboundMethodResponse]:
    """ Confirm Inbound Method

     Confirm a currently available warehouse placement option for an FBT inbound plan. First call the
    List Available Inbound Methods API and select an `inbound_method` with one exact
    `estimate_arrival_time` window. Then call the Get Inbound Method Detail API with that selection and
    choose a returned `placement_option_id`. Confirm using the `placement_option_id`, `inbound_method`,
    and `estimate_arrival_time` from the same selection. If the option has expired, repeat both
    prerequisite calls to obtain a current selection and a new `placement_option_id`, then retry. The
    response contains the child inbound order IDs generated for the plan.

    Args:
        body (ConfirmInboundMethodRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfirmInboundMethodResponse]
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
    body: ConfirmInboundMethodRequest,

) -> ConfirmInboundMethodResponse | None:
    """ Confirm Inbound Method

     Confirm a currently available warehouse placement option for an FBT inbound plan. First call the
    List Available Inbound Methods API and select an `inbound_method` with one exact
    `estimate_arrival_time` window. Then call the Get Inbound Method Detail API with that selection and
    choose a returned `placement_option_id`. Confirm using the `placement_option_id`, `inbound_method`,
    and `estimate_arrival_time` from the same selection. If the option has expired, repeat both
    prerequisite calls to obtain a current selection and a new `placement_option_id`, then retry. The
    response contains the child inbound order IDs generated for the plan.

    Args:
        body (ConfirmInboundMethodRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfirmInboundMethodResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
