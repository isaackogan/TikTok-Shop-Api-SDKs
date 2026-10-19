from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.reject_return_request import RejectReturnRequest
from ...models.reject_return_response import RejectReturnResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    return_id: str,
    *,
    body: RejectReturnRequest,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["idempotency_key"] = idempotency_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/return_refund/202606/returns/{return_id}/reject".format(
            return_id=quote(str(return_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RejectReturnResponse | None:
    if response.status_code == 200:
        response_200 = RejectReturnResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RejectReturnResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    return_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RejectReturnRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[RejectReturnResponse]:
    """Reject Return

     Use this API to reject a buyer's refund-only, return-and-refund, or replacement request, or to offer
    a partial refund after the package is received. The valid decision depends on the current request
    type and status. Before calling this API, make sure the request is still awaiting the seller action
    that matches the decision you send.

    Args:
        return_id (str):
        idempotency_key (str | Unset):
        body (RejectReturnRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RejectReturnResponse]
    """

    kwargs = _get_kwargs(
        return_id=return_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    return_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RejectReturnRequest,
    idempotency_key: str | Unset = UNSET,
) -> RejectReturnResponse | None:
    """Reject Return

     Use this API to reject a buyer's refund-only, return-and-refund, or replacement request, or to offer
    a partial refund after the package is received. The valid decision depends on the current request
    type and status. Before calling this API, make sure the request is still awaiting the seller action
    that matches the decision you send.

    Args:
        return_id (str):
        idempotency_key (str | Unset):
        body (RejectReturnRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RejectReturnResponse
    """

    return sync_detailed(
        return_id=return_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    return_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RejectReturnRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[RejectReturnResponse]:
    """Reject Return

     Use this API to reject a buyer's refund-only, return-and-refund, or replacement request, or to offer
    a partial refund after the package is received. The valid decision depends on the current request
    type and status. Before calling this API, make sure the request is still awaiting the seller action
    that matches the decision you send.

    Args:
        return_id (str):
        idempotency_key (str | Unset):
        body (RejectReturnRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RejectReturnResponse]
    """

    kwargs = _get_kwargs(
        return_id=return_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    return_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RejectReturnRequest,
    idempotency_key: str | Unset = UNSET,
) -> RejectReturnResponse | None:
    """Reject Return

     Use this API to reject a buyer's refund-only, return-and-refund, or replacement request, or to offer
    a partial refund after the package is received. The valid decision depends on the current request
    type and status. Before calling this API, make sure the request is still awaiting the seller action
    that matches the decision you send.

    Args:
        return_id (str):
        idempotency_key (str | Unset):
        body (RejectReturnRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RejectReturnResponse
    """

    return (
        await asyncio_detailed(
            return_id=return_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
