from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.edit_product_request import EditProductRequest
from ...models.edit_product_response import EditProductResponse
from ...types import Response


def _get_kwargs(
    product_id: str,
    *,
    body: EditProductRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/product/202509/products/{product_id}".format(
            product_id=quote(str(product_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> EditProductResponse | None:
    if response.status_code == 200:
        response_200 = EditProductResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[EditProductResponse]:
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
    body: EditProductRequest,
) -> Response[EditProductResponse]:
    """Edit Product

     Edit all properties (e.g. description, brand, images) of an existing product that is not in the
    `FREEZE` or `DELETED` state.
    After editing the product, the latest product content (referred to as v2) will be resent for audit
    review. If the audit passes, v2 is published to the shop, otherwise, the existing product stays live
    and remains unchanged (keeping v1). However, edits to the `price` or `inventory` fields do not
    require a reaudit and will be immediately published on the platform. Use the [Product status
    change](https://partner.tiktokshop.com/docv2/page/650956aff1fd3102b90b6261) webhook to keep track of
    the review status.
    **Note**:
    - This API is applicable only for **active sellers/shops** that have completed the KYC onboarding
    process.
    - There may be a limit to the number of products you can relist per day. We recommend prioritizing
    key products first to ensure they get published. You can find your listing limit on the Seller
    Center homepage.
    - All inputs, including blanks, in the request payload will overwrite existing values. To retain an
    existing value, make sure to include it in your request. Exceptions to this rule are the `price` and
    `inventory` fields, which will remain unchanged if they are omitted from the request. Therefore,
    **it is strongly recommended to retrieve the latest product data using [Get
    Product](6509d85b4a0bb702c057fdda) and submit the complete data when editing**. This ensures
    accuracy and helps avoid errors or unintentional data loss due to missing fields.
    - If you wish to edit only certain properties, you can use the [Partial Edit Product
    API](650a98d74a0bb702c06c3289), [Update Inventory API](6503068fc20ad60284b38858), or the [Update
    Price API](650307de5a12ff0294eac8b0).
    - The language used in the product content must align with the target market's language (e.g. don't
    use Chinese), otherwise the listing will fail or be rejected.
    **For global sellers**:
    If you're using the local replication listing method, note the following sync rules:
    - To sync any changes to other markets, please provide the `seller_sku` and complete
    `replicated_products` data.
    - Note that **category changes** and **sales attribute changes** (in sales attribute id/name) must
    be synced to other markets. The API call will fail if you don't provide these details.
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
        body (EditProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EditProductResponse]
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
    body: EditProductRequest,
) -> EditProductResponse | None:
    """Edit Product

     Edit all properties (e.g. description, brand, images) of an existing product that is not in the
    `FREEZE` or `DELETED` state.
    After editing the product, the latest product content (referred to as v2) will be resent for audit
    review. If the audit passes, v2 is published to the shop, otherwise, the existing product stays live
    and remains unchanged (keeping v1). However, edits to the `price` or `inventory` fields do not
    require a reaudit and will be immediately published on the platform. Use the [Product status
    change](https://partner.tiktokshop.com/docv2/page/650956aff1fd3102b90b6261) webhook to keep track of
    the review status.
    **Note**:
    - This API is applicable only for **active sellers/shops** that have completed the KYC onboarding
    process.
    - There may be a limit to the number of products you can relist per day. We recommend prioritizing
    key products first to ensure they get published. You can find your listing limit on the Seller
    Center homepage.
    - All inputs, including blanks, in the request payload will overwrite existing values. To retain an
    existing value, make sure to include it in your request. Exceptions to this rule are the `price` and
    `inventory` fields, which will remain unchanged if they are omitted from the request. Therefore,
    **it is strongly recommended to retrieve the latest product data using [Get
    Product](6509d85b4a0bb702c057fdda) and submit the complete data when editing**. This ensures
    accuracy and helps avoid errors or unintentional data loss due to missing fields.
    - If you wish to edit only certain properties, you can use the [Partial Edit Product
    API](650a98d74a0bb702c06c3289), [Update Inventory API](6503068fc20ad60284b38858), or the [Update
    Price API](650307de5a12ff0294eac8b0).
    - The language used in the product content must align with the target market's language (e.g. don't
    use Chinese), otherwise the listing will fail or be rejected.
    **For global sellers**:
    If you're using the local replication listing method, note the following sync rules:
    - To sync any changes to other markets, please provide the `seller_sku` and complete
    `replicated_products` data.
    - Note that **category changes** and **sales attribute changes** (in sales attribute id/name) must
    be synced to other markets. The API call will fail if you don't provide these details.
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
        body (EditProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EditProductResponse
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
    body: EditProductRequest,
) -> Response[EditProductResponse]:
    """Edit Product

     Edit all properties (e.g. description, brand, images) of an existing product that is not in the
    `FREEZE` or `DELETED` state.
    After editing the product, the latest product content (referred to as v2) will be resent for audit
    review. If the audit passes, v2 is published to the shop, otherwise, the existing product stays live
    and remains unchanged (keeping v1). However, edits to the `price` or `inventory` fields do not
    require a reaudit and will be immediately published on the platform. Use the [Product status
    change](https://partner.tiktokshop.com/docv2/page/650956aff1fd3102b90b6261) webhook to keep track of
    the review status.
    **Note**:
    - This API is applicable only for **active sellers/shops** that have completed the KYC onboarding
    process.
    - There may be a limit to the number of products you can relist per day. We recommend prioritizing
    key products first to ensure they get published. You can find your listing limit on the Seller
    Center homepage.
    - All inputs, including blanks, in the request payload will overwrite existing values. To retain an
    existing value, make sure to include it in your request. Exceptions to this rule are the `price` and
    `inventory` fields, which will remain unchanged if they are omitted from the request. Therefore,
    **it is strongly recommended to retrieve the latest product data using [Get
    Product](6509d85b4a0bb702c057fdda) and submit the complete data when editing**. This ensures
    accuracy and helps avoid errors or unintentional data loss due to missing fields.
    - If you wish to edit only certain properties, you can use the [Partial Edit Product
    API](650a98d74a0bb702c06c3289), [Update Inventory API](6503068fc20ad60284b38858), or the [Update
    Price API](650307de5a12ff0294eac8b0).
    - The language used in the product content must align with the target market's language (e.g. don't
    use Chinese), otherwise the listing will fail or be rejected.
    **For global sellers**:
    If you're using the local replication listing method, note the following sync rules:
    - To sync any changes to other markets, please provide the `seller_sku` and complete
    `replicated_products` data.
    - Note that **category changes** and **sales attribute changes** (in sales attribute id/name) must
    be synced to other markets. The API call will fail if you don't provide these details.
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
        body (EditProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EditProductResponse]
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
    body: EditProductRequest,
) -> EditProductResponse | None:
    """Edit Product

     Edit all properties (e.g. description, brand, images) of an existing product that is not in the
    `FREEZE` or `DELETED` state.
    After editing the product, the latest product content (referred to as v2) will be resent for audit
    review. If the audit passes, v2 is published to the shop, otherwise, the existing product stays live
    and remains unchanged (keeping v1). However, edits to the `price` or `inventory` fields do not
    require a reaudit and will be immediately published on the platform. Use the [Product status
    change](https://partner.tiktokshop.com/docv2/page/650956aff1fd3102b90b6261) webhook to keep track of
    the review status.
    **Note**:
    - This API is applicable only for **active sellers/shops** that have completed the KYC onboarding
    process.
    - There may be a limit to the number of products you can relist per day. We recommend prioritizing
    key products first to ensure they get published. You can find your listing limit on the Seller
    Center homepage.
    - All inputs, including blanks, in the request payload will overwrite existing values. To retain an
    existing value, make sure to include it in your request. Exceptions to this rule are the `price` and
    `inventory` fields, which will remain unchanged if they are omitted from the request. Therefore,
    **it is strongly recommended to retrieve the latest product data using [Get
    Product](6509d85b4a0bb702c057fdda) and submit the complete data when editing**. This ensures
    accuracy and helps avoid errors or unintentional data loss due to missing fields.
    - If you wish to edit only certain properties, you can use the [Partial Edit Product
    API](650a98d74a0bb702c06c3289), [Update Inventory API](6503068fc20ad60284b38858), or the [Update
    Price API](650307de5a12ff0294eac8b0).
    - The language used in the product content must align with the target market's language (e.g. don't
    use Chinese), otherwise the listing will fail or be rejected.
    **For global sellers**:
    If you're using the local replication listing method, note the following sync rules:
    - To sync any changes to other markets, please provide the `seller_sku` and complete
    `replicated_products` data.
    - Note that **category changes** and **sales attribute changes** (in sales attribute id/name) must
    be synced to other markets. The API call will fail if you don't provide these details.
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
        body (EditProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EditProductResponse
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            client=client,
            body=body,
        )
    ).parsed
