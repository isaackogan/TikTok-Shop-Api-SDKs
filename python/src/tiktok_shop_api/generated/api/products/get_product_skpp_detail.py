from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_product_skpp_detail_locale import GetProductSkppDetailLocale
from ...models.get_product_skpp_detail_response import GetProductSKPPDetailResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    product_id: str,
    *,
    locale: GetProductSkppDetailLocale | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_locale: str | Unset = UNSET
    if not isinstance(locale, Unset):
        json_locale = locale.value

    params["locale"] = json_locale

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/product/202606/skpps/{product_id}".format(
            product_id=quote(str(product_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetProductSKPPDetailResponse | None:
    if response.status_code == 200:
        response_200 = GetProductSKPPDetailResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetProductSKPPDetailResponse]:
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
    locale: GetProductSkppDetailLocale | Unset = UNSET,
) -> Response[GetProductSKPPDetailResponse]:
    """Get Product SKPP Detail

     Return the SKPP qualification status, current and target scores, task progress and suggested
    actions, reward eligibility and status, and offline snapshot time for one product. This API is
    available only to sellers authorized for SKPP in the US market.

    Args:
        product_id (str):
        locale (GetProductSkppDetailLocale | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProductSKPPDetailResponse]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        locale=locale,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: GetProductSkppDetailLocale | Unset = UNSET,
) -> GetProductSKPPDetailResponse | None:
    """Get Product SKPP Detail

     Return the SKPP qualification status, current and target scores, task progress and suggested
    actions, reward eligibility and status, and offline snapshot time for one product. This API is
    available only to sellers authorized for SKPP in the US market.

    Args:
        product_id (str):
        locale (GetProductSkppDetailLocale | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProductSKPPDetailResponse
    """

    return sync_detailed(
        product_id=product_id,
        client=client,
        locale=locale,
    ).parsed


async def asyncio_detailed(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: GetProductSkppDetailLocale | Unset = UNSET,
) -> Response[GetProductSKPPDetailResponse]:
    """Get Product SKPP Detail

     Return the SKPP qualification status, current and target scores, task progress and suggested
    actions, reward eligibility and status, and offline snapshot time for one product. This API is
    available only to sellers authorized for SKPP in the US market.

    Args:
        product_id (str):
        locale (GetProductSkppDetailLocale | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProductSKPPDetailResponse]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        locale=locale,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: GetProductSkppDetailLocale | Unset = UNSET,
) -> GetProductSKPPDetailResponse | None:
    """Get Product SKPP Detail

     Return the SKPP qualification status, current and target scores, task progress and suggested
    actions, reward eligibility and status, and offline snapshot time for one product. This API is
    available only to sellers authorized for SKPP in the US market.

    Args:
        product_id (str):
        locale (GetProductSkppDetailLocale | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProductSKPPDetailResponse
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            client=client,
            locale=locale,
        )
    ).parsed
