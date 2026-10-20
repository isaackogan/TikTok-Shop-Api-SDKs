from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_return_request import CreateReturnRequest
from ...models.create_return_response import CreateReturnResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateReturnRequest,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["idempotency_key"] = idempotency_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/return_refund/202602/returns",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateReturnResponse | None:
    if response.status_code == 200:
        response_200 = CreateReturnResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateReturnResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateReturnRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[CreateReturnResponse]:
    """Create Return

     Use this API to create a seller-initiated aftersales request for an order on behalf of the buyer.
    Supported request types are `REFUND` and `RETURN_AND_REFUND`. Before submitting the request, confirm
    that the order is eligible for the selected aftersales type and return method. After the request is
    created, use the relevant search, status, or review API to continue the aftersales workflow.

    Args:
        idempotency_key (str | Unset):
        body (CreateReturnRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateReturnResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateReturnRequest,
    idempotency_key: str | Unset = UNSET,
) -> CreateReturnResponse | None:
    """Create Return

     Use this API to create a seller-initiated aftersales request for an order on behalf of the buyer.
    Supported request types are `REFUND` and `RETURN_AND_REFUND`. Before submitting the request, confirm
    that the order is eligible for the selected aftersales type and return method. After the request is
    created, use the relevant search, status, or review API to continue the aftersales workflow.

    Args:
        idempotency_key (str | Unset):
        body (CreateReturnRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateReturnResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateReturnRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[CreateReturnResponse]:
    """Create Return

     Use this API to create a seller-initiated aftersales request for an order on behalf of the buyer.
    Supported request types are `REFUND` and `RETURN_AND_REFUND`. Before submitting the request, confirm
    that the order is eligible for the selected aftersales type and return method. After the request is
    created, use the relevant search, status, or review API to continue the aftersales workflow.

    Args:
        idempotency_key (str | Unset):
        body (CreateReturnRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateReturnResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateReturnRequest,
    idempotency_key: str | Unset = UNSET,
) -> CreateReturnResponse | None:
    """Create Return

     Use this API to create a seller-initiated aftersales request for an order on behalf of the buyer.
    Supported request types are `REFUND` and `RETURN_AND_REFUND`. Before submitting the request, confirm
    that the order is eligible for the selected aftersales type and return method. After the request is
    created, use the relevant search, status, or review API to continue the aftersales workflow.

    Args:
        idempotency_key (str | Unset):
        body (CreateReturnRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateReturnResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
