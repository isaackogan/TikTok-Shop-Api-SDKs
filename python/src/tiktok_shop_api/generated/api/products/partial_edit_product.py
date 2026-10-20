from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.partial_edit_product_request import PartialEditProductRequest
from ...models.partial_edit_product_response import PartialEditProductResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    product_id: str,
    *,
    body: PartialEditProductRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202509/products/{product_id}/partial_edit".format(
            product_id=quote(str(product_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PartialEditProductResponse | None:
    if response.status_code == 200:
        response_200 = PartialEditProductResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PartialEditProductResponse]:
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
    body: PartialEditProductRequest | Unset = UNSET,
) -> Response[PartialEditProductResponse]:
    """Partial Edit Product

     Edit some properties (e.g. description, images, attributes) of a product that is not in the `FREEZE`
    or `DELETED` state.
    After editing the product, the latest product content (referred to as v2) will be resent for audit
    review. If the audit passes, v2 is published to the shop, otherwise, the existing product stays live
    and remains unchanged (keeping v1). However, edits to the `price` or `inventory` fields do not
    require a reaudit and will be immediately published on the platform. Use the [Product status
    change](650956aff1fd3102b90b6261) webhook to keep track of the review status.
    **Note**:
    - This API is applicable for all sellers.
    - There may be a limit to the number of products you can relist per day. We recommend prioritizing
    key products first to ensure they get published. You can find your listing limit on the Seller
    Center homepage.
    - If a draft or audit-review version exists, unedited fields will retain their values over those of
    the base (live) version.
    - **Updates are handled per top-level property**, so all non-empty fields within an updated object
    must be supplied to prevent overwriting with blanks. For top-level properties (e.g. `description`,
    `brand_id`) that are not nested in an object, you can update them individually. Omitting these
    properties in the request will leave them unchanged. If you need to edit any nested property within
    an object, you must provide values for all nested properties of that object. Any omitted nested
    properties will be overwritten with blanks.
    - If new mandatory product attributes were added by TikTok Shop after the creation of your product,
    ensure that you provide these attributes too.
    **For global sellers**:
    If you're using the local replication listing method, note the following sync rules:
    **Sales attribute changes** (in sales attribute id/name) must be synced to other markets. Therefore,
    you must provide the `seller_sku` and complete `replicated_products` data. The API call will fail if
    you don't provide these details.
    **New SKUs* (new sales attribute value id/name) are optional to sync to other markets. To sync,
    please provide the `seller_sku` and complete `replicated_products` data.
    **General changes** are optional to sync to other markets. To sync, you only need to provide
    `replicated_products.region`.
    **For Tokopedia sellers**:
    Note that a product can have **only one active version** across all platforms at any time. If a
    product is live on both platforms, audit results for the latest version are handled as follows:
    - **Mixed audit results**: If the product passes audit on one platform but fails on another, on the
    successful platform, the product will stay live and be updated with content from the latest version
    (v2), while on the failed platform, the product will be deactivated and hidden entirely.
    - **Audit failure on all platforms**: If the product fails audit on all platforms, the existing
    product stays live and remains unchanged (keeping v1).

    Args:
        product_id (str):
        body (PartialEditProductRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PartialEditProductResponse]
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
    body: PartialEditProductRequest | Unset = UNSET,
) -> PartialEditProductResponse | None:
    """Partial Edit Product

     Edit some properties (e.g. description, images, attributes) of a product that is not in the `FREEZE`
    or `DELETED` state.
    After editing the product, the latest product content (referred to as v2) will be resent for audit
    review. If the audit passes, v2 is published to the shop, otherwise, the existing product stays live
    and remains unchanged (keeping v1). However, edits to the `price` or `inventory` fields do not
    require a reaudit and will be immediately published on the platform. Use the [Product status
    change](650956aff1fd3102b90b6261) webhook to keep track of the review status.
    **Note**:
    - This API is applicable for all sellers.
    - There may be a limit to the number of products you can relist per day. We recommend prioritizing
    key products first to ensure they get published. You can find your listing limit on the Seller
    Center homepage.
    - If a draft or audit-review version exists, unedited fields will retain their values over those of
    the base (live) version.
    - **Updates are handled per top-level property**, so all non-empty fields within an updated object
    must be supplied to prevent overwriting with blanks. For top-level properties (e.g. `description`,
    `brand_id`) that are not nested in an object, you can update them individually. Omitting these
    properties in the request will leave them unchanged. If you need to edit any nested property within
    an object, you must provide values for all nested properties of that object. Any omitted nested
    properties will be overwritten with blanks.
    - If new mandatory product attributes were added by TikTok Shop after the creation of your product,
    ensure that you provide these attributes too.
    **For global sellers**:
    If you're using the local replication listing method, note the following sync rules:
    **Sales attribute changes** (in sales attribute id/name) must be synced to other markets. Therefore,
    you must provide the `seller_sku` and complete `replicated_products` data. The API call will fail if
    you don't provide these details.
    **New SKUs* (new sales attribute value id/name) are optional to sync to other markets. To sync,
    please provide the `seller_sku` and complete `replicated_products` data.
    **General changes** are optional to sync to other markets. To sync, you only need to provide
    `replicated_products.region`.
    **For Tokopedia sellers**:
    Note that a product can have **only one active version** across all platforms at any time. If a
    product is live on both platforms, audit results for the latest version are handled as follows:
    - **Mixed audit results**: If the product passes audit on one platform but fails on another, on the
    successful platform, the product will stay live and be updated with content from the latest version
    (v2), while on the failed platform, the product will be deactivated and hidden entirely.
    - **Audit failure on all platforms**: If the product fails audit on all platforms, the existing
    product stays live and remains unchanged (keeping v1).

    Args:
        product_id (str):
        body (PartialEditProductRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PartialEditProductResponse
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
    body: PartialEditProductRequest | Unset = UNSET,
) -> Response[PartialEditProductResponse]:
    """Partial Edit Product

     Edit some properties (e.g. description, images, attributes) of a product that is not in the `FREEZE`
    or `DELETED` state.
    After editing the product, the latest product content (referred to as v2) will be resent for audit
    review. If the audit passes, v2 is published to the shop, otherwise, the existing product stays live
    and remains unchanged (keeping v1). However, edits to the `price` or `inventory` fields do not
    require a reaudit and will be immediately published on the platform. Use the [Product status
    change](650956aff1fd3102b90b6261) webhook to keep track of the review status.
    **Note**:
    - This API is applicable for all sellers.
    - There may be a limit to the number of products you can relist per day. We recommend prioritizing
    key products first to ensure they get published. You can find your listing limit on the Seller
    Center homepage.
    - If a draft or audit-review version exists, unedited fields will retain their values over those of
    the base (live) version.
    - **Updates are handled per top-level property**, so all non-empty fields within an updated object
    must be supplied to prevent overwriting with blanks. For top-level properties (e.g. `description`,
    `brand_id`) that are not nested in an object, you can update them individually. Omitting these
    properties in the request will leave them unchanged. If you need to edit any nested property within
    an object, you must provide values for all nested properties of that object. Any omitted nested
    properties will be overwritten with blanks.
    - If new mandatory product attributes were added by TikTok Shop after the creation of your product,
    ensure that you provide these attributes too.
    **For global sellers**:
    If you're using the local replication listing method, note the following sync rules:
    **Sales attribute changes** (in sales attribute id/name) must be synced to other markets. Therefore,
    you must provide the `seller_sku` and complete `replicated_products` data. The API call will fail if
    you don't provide these details.
    **New SKUs* (new sales attribute value id/name) are optional to sync to other markets. To sync,
    please provide the `seller_sku` and complete `replicated_products` data.
    **General changes** are optional to sync to other markets. To sync, you only need to provide
    `replicated_products.region`.
    **For Tokopedia sellers**:
    Note that a product can have **only one active version** across all platforms at any time. If a
    product is live on both platforms, audit results for the latest version are handled as follows:
    - **Mixed audit results**: If the product passes audit on one platform but fails on another, on the
    successful platform, the product will stay live and be updated with content from the latest version
    (v2), while on the failed platform, the product will be deactivated and hidden entirely.
    - **Audit failure on all platforms**: If the product fails audit on all platforms, the existing
    product stays live and remains unchanged (keeping v1).

    Args:
        product_id (str):
        body (PartialEditProductRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PartialEditProductResponse]
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
    body: PartialEditProductRequest | Unset = UNSET,
) -> PartialEditProductResponse | None:
    """Partial Edit Product

     Edit some properties (e.g. description, images, attributes) of a product that is not in the `FREEZE`
    or `DELETED` state.
    After editing the product, the latest product content (referred to as v2) will be resent for audit
    review. If the audit passes, v2 is published to the shop, otherwise, the existing product stays live
    and remains unchanged (keeping v1). However, edits to the `price` or `inventory` fields do not
    require a reaudit and will be immediately published on the platform. Use the [Product status
    change](650956aff1fd3102b90b6261) webhook to keep track of the review status.
    **Note**:
    - This API is applicable for all sellers.
    - There may be a limit to the number of products you can relist per day. We recommend prioritizing
    key products first to ensure they get published. You can find your listing limit on the Seller
    Center homepage.
    - If a draft or audit-review version exists, unedited fields will retain their values over those of
    the base (live) version.
    - **Updates are handled per top-level property**, so all non-empty fields within an updated object
    must be supplied to prevent overwriting with blanks. For top-level properties (e.g. `description`,
    `brand_id`) that are not nested in an object, you can update them individually. Omitting these
    properties in the request will leave them unchanged. If you need to edit any nested property within
    an object, you must provide values for all nested properties of that object. Any omitted nested
    properties will be overwritten with blanks.
    - If new mandatory product attributes were added by TikTok Shop after the creation of your product,
    ensure that you provide these attributes too.
    **For global sellers**:
    If you're using the local replication listing method, note the following sync rules:
    **Sales attribute changes** (in sales attribute id/name) must be synced to other markets. Therefore,
    you must provide the `seller_sku` and complete `replicated_products` data. The API call will fail if
    you don't provide these details.
    **New SKUs* (new sales attribute value id/name) are optional to sync to other markets. To sync,
    please provide the `seller_sku` and complete `replicated_products` data.
    **General changes** are optional to sync to other markets. To sync, you only need to provide
    `replicated_products.region`.
    **For Tokopedia sellers**:
    Note that a product can have **only one active version** across all platforms at any time. If a
    product is live on both platforms, audit results for the latest version are handled as follows:
    - **Mixed audit results**: If the product passes audit on one platform but fails on another, on the
    successful platform, the product will stay live and be updated with content from the latest version
    (v2), while on the failed platform, the product will be deactivated and hidden entirely.
    - **Audit failure on all platforms**: If the product fails audit on all platforms, the existing
    product stays live and remains unchanged (keeping v1).

    Args:
        product_id (str):
        body (PartialEditProductRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PartialEditProductResponse
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            client=client,
            body=body,
        )
    ).parsed
