from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.reject_cancellation_request import RejectCancellationRequest
from ...models.reject_cancellation_response import RejectCancellationResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    cancel_id: str,
    *,
    body: RejectCancellationRequest,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["idempotency_key"] = idempotency_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/return_refund/202309/cancellations/{cancel_id}/reject".format(
            cancel_id=quote(str(cancel_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RejectCancellationResponse | None:
    if response.status_code == 200:
        response_200 = RejectCancellationResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RejectCancellationResponse]:
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
    body: RejectCancellationRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[RejectCancellationResponse]:
    """Reject Cancellation

     Use this API to reject a buyer's cancellation request for the specified cancel_id. Before calling
    this API, make sure the request is still in a state where seller rejection is currently allowed.

    Args:
        cancel_id (str):
        idempotency_key (str | Unset):
        body (RejectCancellationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RejectCancellationResponse]
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
    body: RejectCancellationRequest,
    idempotency_key: str | Unset = UNSET,
) -> RejectCancellationResponse | None:
    """Reject Cancellation

     Use this API to reject a buyer's cancellation request for the specified cancel_id. Before calling
    this API, make sure the request is still in a state where seller rejection is currently allowed.

    Args:
        cancel_id (str):
        idempotency_key (str | Unset):
        body (RejectCancellationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RejectCancellationResponse
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
    body: RejectCancellationRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[RejectCancellationResponse]:
    """Reject Cancellation

     Use this API to reject a buyer's cancellation request for the specified cancel_id. Before calling
    this API, make sure the request is still in a state where seller rejection is currently allowed.

    Args:
        cancel_id (str):
        idempotency_key (str | Unset):
        body (RejectCancellationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RejectCancellationResponse]
    """

    kwargs = _get_kwargs(
        cancel_id=cancel_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cancel_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RejectCancellationRequest,
    idempotency_key: str | Unset = UNSET,
) -> RejectCancellationResponse | None:
    """Reject Cancellation

     Use this API to reject a buyer's cancellation request for the specified cancel_id. Before calling
    this API, make sure the request is still in a state where seller rejection is currently allowed.

    Args:
        cancel_id (str):
        idempotency_key (str | Unset):
        body (RejectCancellationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RejectCancellationResponse
    """

    return (
        await asyncio_detailed(
            cancel_id=cancel_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
