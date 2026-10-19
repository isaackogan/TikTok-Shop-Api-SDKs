from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.submit_strikethrough_price_request import SubmitStrikethroughPriceRequest
from ...models.submit_strikethrough_price_response import SubmitStrikethroughPriceResponse
from ...types import Response


def _get_kwargs(
    product_id: str,
    *,
    body: SubmitStrikethroughPriceRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202609/products/{product_id}/strikethrough_price/submit".format(
            product_id=quote(str(product_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SubmitStrikethroughPriceResponse | None:
    if response.status_code == 200:
        response_200 = SubmitStrikethroughPriceResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SubmitStrikethroughPriceResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SubmitStrikethroughPriceRequest,
) -> Response[SubmitStrikethroughPriceResponse]:
    """Submit Strikethrough Price

     Submit external pricing information for a product's SKUs so that TikTok Shop can verify the
    product's list price for use as a strikethrough price. If the submitted information is approved, the
    verified list price may be displayed as the strikethrough price when a discount applies.

    Submitted pricing information expires 90 days after submission and must be resubmitted to continue
    supporting strikethrough price display.

    Args:
        product_id (str):
        body (SubmitStrikethroughPriceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubmitStrikethroughPriceResponse]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SubmitStrikethroughPriceRequest,
) -> SubmitStrikethroughPriceResponse | None:
    """Submit Strikethrough Price

     Submit external pricing information for a product's SKUs so that TikTok Shop can verify the
    product's list price for use as a strikethrough price. If the submitted information is approved, the
    verified list price may be displayed as the strikethrough price when a discount applies.

    Submitted pricing information expires 90 days after submission and must be resubmitted to continue
    supporting strikethrough price display.

    Args:
        product_id (str):
        body (SubmitStrikethroughPriceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubmitStrikethroughPriceResponse
    """

    return sync_detailed(
        product_id=product_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SubmitStrikethroughPriceRequest,
) -> Response[SubmitStrikethroughPriceResponse]:
    """Submit Strikethrough Price

     Submit external pricing information for a product's SKUs so that TikTok Shop can verify the
    product's list price for use as a strikethrough price. If the submitted information is approved, the
    verified list price may be displayed as the strikethrough price when a discount applies.

    Submitted pricing information expires 90 days after submission and must be resubmitted to continue
    supporting strikethrough price display.

    Args:
        product_id (str):
        body (SubmitStrikethroughPriceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubmitStrikethroughPriceResponse]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SubmitStrikethroughPriceRequest,
) -> SubmitStrikethroughPriceResponse | None:
    """Submit Strikethrough Price

     Submit external pricing information for a product's SKUs so that TikTok Shop can verify the
    product's list price for use as a strikethrough price. If the submitted information is approved, the
    verified list price may be displayed as the strikethrough price when a discount applies.

    Submitted pricing information expires 90 days after submission and must be resubmitted to continue
    supporting strikethrough price display.

    Args:
        product_id (str):
        body (SubmitStrikethroughPriceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubmitStrikethroughPriceResponse
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            client=client,
            body=body,
        )
    ).parsed
