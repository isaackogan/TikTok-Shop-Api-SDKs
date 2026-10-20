from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.approve_cancellation_request import ApproveCancellationRequest
from ...models.approve_cancellation_response import ApproveCancellationResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    cancel_id: str,
    *,
    body: ApproveCancellationRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["idempotency_key"] = idempotency_key


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/return_refund/202309/cancellations/{cancel_id}/approve".format(cancel_id=quote(str(cancel_id), safe=""),),
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApproveCancellationResponse | None:
    if response.status_code == 200:
        response_200 = ApproveCancellationResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApproveCancellationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cancel_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ApproveCancellationRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> Response[ApproveCancellationResponse]:
    """ Approve Cancellation

     Use this API to approve a buyer-initiated cancellation request identified by cancel_id. Call this
    API only when the cancellation request is still waiting for seller action.

    Args:
        cancel_id (str):
        idempotency_key (str | Unset):
        body (ApproveCancellationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApproveCancellationResponse]
     """


    kwargs = _get_kwargs(
        cancel_id=cancel_id,
body=body,
idempotency_key=idempotency_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    cancel_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ApproveCancellationRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> ApproveCancellationResponse | None:
    """ Approve Cancellation

     Use this API to approve a buyer-initiated cancellation request identified by cancel_id. Call this
    API only when the cancellation request is still waiting for seller action.

    Args:
        cancel_id (str):
        idempotency_key (str | Unset):
        body (ApproveCancellationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApproveCancellationResponse
     """


    return sync_detailed(
        cancel_id=cancel_id,
client=client,
body=body,
idempotency_key=idempotency_key,

    ).parsed

async def asyncio_detailed(
    cancel_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ApproveCancellationRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> Response[ApproveCancellationResponse]:
    """ Approve Cancellation

     Use this API to approve a buyer-initiated cancellation request identified by cancel_id. Call this
    API only when the cancellation request is still waiting for seller action.

    Args:
        cancel_id (str):
        idempotency_key (str | Unset):
        body (ApproveCancellationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApproveCancellationResponse]
     """


    kwargs = _get_kwargs(
        cancel_id=cancel_id,
body=body,
idempotency_key=idempotency_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    cancel_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ApproveCancellationRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> ApproveCancellationResponse | None:
    """ Approve Cancellation

     Use this API to approve a buyer-initiated cancellation request identified by cancel_id. Call this
    API only when the cancellation request is still waiting for seller action.

    Args:
        cancel_id (str):
        idempotency_key (str | Unset):
        body (ApproveCancellationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApproveCancellationResponse
     """


    return (await asyncio_detailed(
        cancel_id=cancel_id,
client=client,
body=body,
idempotency_key=idempotency_key,

    )).parsed
