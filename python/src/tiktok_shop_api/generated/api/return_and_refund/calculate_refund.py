from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.calculate_refund_request import CalculateRefundRequest
from ...models.calculate_refund_response import CalculateRefundResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CalculateRefundRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/return_refund/202602/refunds/calculate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CalculateRefundResponse | None:
    if response.status_code == 200:
        response_200 = CalculateRefundResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CalculateRefundResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CalculateRefundRequest,
) -> Response[CalculateRefundResponse]:
    """Calculate Refund

     Use this API to estimate the refundable amount for a cancellation, refund, or return-and-refund
    request. The estimate depends on the selected request_type, reason_name, and targeted items. If
    skus, order_line_item_ids, and order_line_list are all omitted, all order lines in the order are
    selected as inputs to the refund calculation. For return-and-refund scenarios, the estimate can also
    depend on the selected return shipping method.

    Args:
        body (CalculateRefundRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CalculateRefundResponse]
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
    body: CalculateRefundRequest,
) -> CalculateRefundResponse | None:
    """Calculate Refund

     Use this API to estimate the refundable amount for a cancellation, refund, or return-and-refund
    request. The estimate depends on the selected request_type, reason_name, and targeted items. If
    skus, order_line_item_ids, and order_line_list are all omitted, all order lines in the order are
    selected as inputs to the refund calculation. For return-and-refund scenarios, the estimate can also
    depend on the selected return shipping method.

    Args:
        body (CalculateRefundRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CalculateRefundResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CalculateRefundRequest,
) -> Response[CalculateRefundResponse]:
    """Calculate Refund

     Use this API to estimate the refundable amount for a cancellation, refund, or return-and-refund
    request. The estimate depends on the selected request_type, reason_name, and targeted items. If
    skus, order_line_item_ids, and order_line_list are all omitted, all order lines in the order are
    selected as inputs to the refund calculation. For return-and-refund scenarios, the estimate can also
    depend on the selected return shipping method.

    Args:
        body (CalculateRefundRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CalculateRefundResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CalculateRefundRequest,
) -> CalculateRefundResponse | None:
    """Calculate Refund

     Use this API to estimate the refundable amount for a cancellation, refund, or return-and-refund
    request. The estimate depends on the selected request_type, reason_name, and targeted items. If
    skus, order_line_item_ids, and order_line_list are all omitted, all order lines in the order are
    selected as inputs to the refund calculation. For return-and-refund scenarios, the estimate can also
    depend on the selected return shipping method.

    Args:
        body (CalculateRefundRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CalculateRefundResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
