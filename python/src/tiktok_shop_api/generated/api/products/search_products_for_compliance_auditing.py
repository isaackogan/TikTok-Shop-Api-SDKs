from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_products_for_compliance_auditing_request import SearchProductsForComplianceAuditingRequest
from ...models.search_products_for_compliance_auditing_response import SearchProductsForComplianceAuditingResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SearchProductsForComplianceAuditingRequest | Unset = UNSET,
    shop_cipher: str | Unset = UNSET,
    category_asset_cipher: str | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["shop_cipher"] = shop_cipher

    params["category_asset_cipher"] = category_asset_cipher

    params["page_token"] = page_token

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202601/compliance/auditing/research",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SearchProductsForComplianceAuditingResponse | None:
    if response.status_code == 200:
        response_200 = SearchProductsForComplianceAuditingResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SearchProductsForComplianceAuditingResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchProductsForComplianceAuditingRequest | Unset = UNSET,
    shop_cipher: str | Unset = UNSET,
    category_asset_cipher: str | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int,
) -> Response[SearchProductsForComplianceAuditingResponse]:
    """Search Products for Compliance Auditing

     Search live products and retrieve the product information needed by a compliance vendor to prepare a
    compliance testing report. The selection behavior is:
    - If `product_ids` is non-empty, the operation retrieves those known products. This branch takes
    precedence; seller, product-title, category, and brand filters and pagination are not used to select
    products.
    - Otherwise, the operation performs a shop search and requires `seller_id`, `seller_name`, or both.
    When both shop identifiers are provided, their matching sellers are combined. You can further filter
    this search by product title, category IDs, and brand IDs and paginate the results.

    Args:
        shop_cipher (str | Unset):
        category_asset_cipher (str | Unset):
        page_token (str | Unset):
        page_size (int):
        body (SearchProductsForComplianceAuditingRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchProductsForComplianceAuditingResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        shop_cipher=shop_cipher,
        category_asset_cipher=category_asset_cipher,
        page_token=page_token,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SearchProductsForComplianceAuditingRequest | Unset = UNSET,
    shop_cipher: str | Unset = UNSET,
    category_asset_cipher: str | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int,
) -> SearchProductsForComplianceAuditingResponse | None:
    """Search Products for Compliance Auditing

     Search live products and retrieve the product information needed by a compliance vendor to prepare a
    compliance testing report. The selection behavior is:
    - If `product_ids` is non-empty, the operation retrieves those known products. This branch takes
    precedence; seller, product-title, category, and brand filters and pagination are not used to select
    products.
    - Otherwise, the operation performs a shop search and requires `seller_id`, `seller_name`, or both.
    When both shop identifiers are provided, their matching sellers are combined. You can further filter
    this search by product title, category IDs, and brand IDs and paginate the results.

    Args:
        shop_cipher (str | Unset):
        category_asset_cipher (str | Unset):
        page_token (str | Unset):
        page_size (int):
        body (SearchProductsForComplianceAuditingRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchProductsForComplianceAuditingResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        shop_cipher=shop_cipher,
        category_asset_cipher=category_asset_cipher,
        page_token=page_token,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchProductsForComplianceAuditingRequest | Unset = UNSET,
    shop_cipher: str | Unset = UNSET,
    category_asset_cipher: str | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int,
) -> Response[SearchProductsForComplianceAuditingResponse]:
    """Search Products for Compliance Auditing

     Search live products and retrieve the product information needed by a compliance vendor to prepare a
    compliance testing report. The selection behavior is:
    - If `product_ids` is non-empty, the operation retrieves those known products. This branch takes
    precedence; seller, product-title, category, and brand filters and pagination are not used to select
    products.
    - Otherwise, the operation performs a shop search and requires `seller_id`, `seller_name`, or both.
    When both shop identifiers are provided, their matching sellers are combined. You can further filter
    this search by product title, category IDs, and brand IDs and paginate the results.

    Args:
        shop_cipher (str | Unset):
        category_asset_cipher (str | Unset):
        page_token (str | Unset):
        page_size (int):
        body (SearchProductsForComplianceAuditingRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchProductsForComplianceAuditingResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        shop_cipher=shop_cipher,
        category_asset_cipher=category_asset_cipher,
        page_token=page_token,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchProductsForComplianceAuditingRequest | Unset = UNSET,
    shop_cipher: str | Unset = UNSET,
    category_asset_cipher: str | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int,
) -> SearchProductsForComplianceAuditingResponse | None:
    """Search Products for Compliance Auditing

     Search live products and retrieve the product information needed by a compliance vendor to prepare a
    compliance testing report. The selection behavior is:
    - If `product_ids` is non-empty, the operation retrieves those known products. This branch takes
    precedence; seller, product-title, category, and brand filters and pagination are not used to select
    products.
    - Otherwise, the operation performs a shop search and requires `seller_id`, `seller_name`, or both.
    When both shop identifiers are provided, their matching sellers are combined. You can further filter
    this search by product title, category IDs, and brand IDs and paginate the results.

    Args:
        shop_cipher (str | Unset):
        category_asset_cipher (str | Unset):
        page_token (str | Unset):
        page_size (int):
        body (SearchProductsForComplianceAuditingRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchProductsForComplianceAuditingResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            shop_cipher=shop_cipher,
            category_asset_cipher=category_asset_cipher,
            page_token=page_token,
            page_size=page_size,
        )
    ).parsed
