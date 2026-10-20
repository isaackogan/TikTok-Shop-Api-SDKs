from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_the_blind_box_opening_results_request import UpdateTheBlindBoxOpeningResultsRequest
from ...models.update_the_blind_box_opening_results_response import UpdateTheBlindBoxOpeningResultsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UpdateTheBlindBoxOpeningResultsRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/order/202605/orders/blind_box_result/callback",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UpdateTheBlindBoxOpeningResultsResponse | None:
    if response.status_code == 200:
        response_200 = UpdateTheBlindBoxOpeningResultsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdateTheBlindBoxOpeningResultsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateTheBlindBoxOpeningResultsRequest | Unset = UNSET,
) -> Response[UpdateTheBlindBoxOpeningResultsResponse]:
    """Update The Blind Box Opening Results

     After the merchant completes blind box opening in a live room, use this callback to send the opening
    results for an order back to the platform. The request supports two result shapes:
    `blind_box_results` contains one unboxed product per item, while `blind_batch_box_results` groups
    one or more unboxed products under an order line. If `blind_batch_box_results` is non-empty, the
    platform processes it and ignores `blind_box_results`. Buyers can then view the unboxing results in
    the order details.

    Args:
        body (UpdateTheBlindBoxOpeningResultsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateTheBlindBoxOpeningResultsResponse]
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
    body: UpdateTheBlindBoxOpeningResultsRequest | Unset = UNSET,
) -> UpdateTheBlindBoxOpeningResultsResponse | None:
    """Update The Blind Box Opening Results

     After the merchant completes blind box opening in a live room, use this callback to send the opening
    results for an order back to the platform. The request supports two result shapes:
    `blind_box_results` contains one unboxed product per item, while `blind_batch_box_results` groups
    one or more unboxed products under an order line. If `blind_batch_box_results` is non-empty, the
    platform processes it and ignores `blind_box_results`. Buyers can then view the unboxing results in
    the order details.

    Args:
        body (UpdateTheBlindBoxOpeningResultsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateTheBlindBoxOpeningResultsResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateTheBlindBoxOpeningResultsRequest | Unset = UNSET,
) -> Response[UpdateTheBlindBoxOpeningResultsResponse]:
    """Update The Blind Box Opening Results

     After the merchant completes blind box opening in a live room, use this callback to send the opening
    results for an order back to the platform. The request supports two result shapes:
    `blind_box_results` contains one unboxed product per item, while `blind_batch_box_results` groups
    one or more unboxed products under an order line. If `blind_batch_box_results` is non-empty, the
    platform processes it and ignores `blind_box_results`. Buyers can then view the unboxing results in
    the order details.

    Args:
        body (UpdateTheBlindBoxOpeningResultsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateTheBlindBoxOpeningResultsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateTheBlindBoxOpeningResultsRequest | Unset = UNSET,
) -> UpdateTheBlindBoxOpeningResultsResponse | None:
    """Update The Blind Box Opening Results

     After the merchant completes blind box opening in a live room, use this callback to send the opening
    results for an order back to the platform. The request supports two result shapes:
    `blind_box_results` contains one unboxed product per item, while `blind_batch_box_results` groups
    one or more unboxed products under an order line. If `blind_batch_box_results` is non-empty, the
    platform processes it and ignores `blind_box_results`. Buyers can then view the unboxing results in
    the order details.

    Args:
        body (UpdateTheBlindBoxOpeningResultsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateTheBlindBoxOpeningResultsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
