from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_promotion_activity_products_request import UpdatePromotionActivityProductsRequest
from ...models.update_promotion_activity_products_response import UpdatePromotionActivityProductsResponse
from ...types import Response


def _get_kwargs(
    activity_id: str,
    *,
    body: UpdatePromotionActivityProductsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/promotion/202309/activities/{activity_id}/products".format(
            activity_id=quote(str(activity_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UpdatePromotionActivityProductsResponse | None:
    if response.status_code == 200:
        response_200 = UpdatePromotionActivityProductsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdatePromotionActivityProductsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    activity_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePromotionActivityProductsRequest,
) -> Response[UpdatePromotionActivityProductsResponse]:
    """Update Promotion Activity Products

     Use this API as follows:
    - For a `FIXED_PRICE`, `DIRECT_DISCOUNT`, or `FLASHSALE` activity with PRODUCT or VARIATION scope,
    provide a non-empty `products` array. For VARIATION scope, add or update SKUs in each product's
    `skus` array.
    - For a PRODUCT-scoped `SHIPPING_DISCOUNT` or `GIFT_WITH_PURCHASE` activity, provide a non-empty
    `products` array. A SHOP-scoped shipping-discount activity is not supported by this operation, and
    this operation does not document nested-SKU updates for shipping-discount or Gift With Purchase.
    - For a PRODUCT-scoped `BUY_MORE_SAVE_MORE` or `BUY_X_GET_Y` activity, `products` can be omitted or
    empty when the request updates only benefit-product relations.
    - For a SHOP-scoped `BUY_MORE_SAVE_MORE` or `BUY_X_GET_Y` activity, omit `products` or pass an empty
    array; use `benefit_product_ids` or `exclude_product_ids` for the applicable relation update.
    For an ongoing flash deal, you can add products or SKUs, but you cannot change the price or purchase
    limits of products or SKUs already in the activity. To remove products or SKUs, use [Remove Activity
    Product](https://partner.tiktokshop.com/docv2/page/650acfd84a0bb702c072b4eb).

    Args:
        activity_id (str):
        body (UpdatePromotionActivityProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdatePromotionActivityProductsResponse]
    """

    kwargs = _get_kwargs(
        activity_id=activity_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    activity_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePromotionActivityProductsRequest,
) -> UpdatePromotionActivityProductsResponse | None:
    """Update Promotion Activity Products

     Use this API as follows:
    - For a `FIXED_PRICE`, `DIRECT_DISCOUNT`, or `FLASHSALE` activity with PRODUCT or VARIATION scope,
    provide a non-empty `products` array. For VARIATION scope, add or update SKUs in each product's
    `skus` array.
    - For a PRODUCT-scoped `SHIPPING_DISCOUNT` or `GIFT_WITH_PURCHASE` activity, provide a non-empty
    `products` array. A SHOP-scoped shipping-discount activity is not supported by this operation, and
    this operation does not document nested-SKU updates for shipping-discount or Gift With Purchase.
    - For a PRODUCT-scoped `BUY_MORE_SAVE_MORE` or `BUY_X_GET_Y` activity, `products` can be omitted or
    empty when the request updates only benefit-product relations.
    - For a SHOP-scoped `BUY_MORE_SAVE_MORE` or `BUY_X_GET_Y` activity, omit `products` or pass an empty
    array; use `benefit_product_ids` or `exclude_product_ids` for the applicable relation update.
    For an ongoing flash deal, you can add products or SKUs, but you cannot change the price or purchase
    limits of products or SKUs already in the activity. To remove products or SKUs, use [Remove Activity
    Product](https://partner.tiktokshop.com/docv2/page/650acfd84a0bb702c072b4eb).

    Args:
        activity_id (str):
        body (UpdatePromotionActivityProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdatePromotionActivityProductsResponse
    """

    return sync_detailed(
        activity_id=activity_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    activity_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePromotionActivityProductsRequest,
) -> Response[UpdatePromotionActivityProductsResponse]:
    """Update Promotion Activity Products

     Use this API as follows:
    - For a `FIXED_PRICE`, `DIRECT_DISCOUNT`, or `FLASHSALE` activity with PRODUCT or VARIATION scope,
    provide a non-empty `products` array. For VARIATION scope, add or update SKUs in each product's
    `skus` array.
    - For a PRODUCT-scoped `SHIPPING_DISCOUNT` or `GIFT_WITH_PURCHASE` activity, provide a non-empty
    `products` array. A SHOP-scoped shipping-discount activity is not supported by this operation, and
    this operation does not document nested-SKU updates for shipping-discount or Gift With Purchase.
    - For a PRODUCT-scoped `BUY_MORE_SAVE_MORE` or `BUY_X_GET_Y` activity, `products` can be omitted or
    empty when the request updates only benefit-product relations.
    - For a SHOP-scoped `BUY_MORE_SAVE_MORE` or `BUY_X_GET_Y` activity, omit `products` or pass an empty
    array; use `benefit_product_ids` or `exclude_product_ids` for the applicable relation update.
    For an ongoing flash deal, you can add products or SKUs, but you cannot change the price or purchase
    limits of products or SKUs already in the activity. To remove products or SKUs, use [Remove Activity
    Product](https://partner.tiktokshop.com/docv2/page/650acfd84a0bb702c072b4eb).

    Args:
        activity_id (str):
        body (UpdatePromotionActivityProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdatePromotionActivityProductsResponse]
    """

    kwargs = _get_kwargs(
        activity_id=activity_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    activity_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdatePromotionActivityProductsRequest,
) -> UpdatePromotionActivityProductsResponse | None:
    """Update Promotion Activity Products

     Use this API as follows:
    - For a `FIXED_PRICE`, `DIRECT_DISCOUNT`, or `FLASHSALE` activity with PRODUCT or VARIATION scope,
    provide a non-empty `products` array. For VARIATION scope, add or update SKUs in each product's
    `skus` array.
    - For a PRODUCT-scoped `SHIPPING_DISCOUNT` or `GIFT_WITH_PURCHASE` activity, provide a non-empty
    `products` array. A SHOP-scoped shipping-discount activity is not supported by this operation, and
    this operation does not document nested-SKU updates for shipping-discount or Gift With Purchase.
    - For a PRODUCT-scoped `BUY_MORE_SAVE_MORE` or `BUY_X_GET_Y` activity, `products` can be omitted or
    empty when the request updates only benefit-product relations.
    - For a SHOP-scoped `BUY_MORE_SAVE_MORE` or `BUY_X_GET_Y` activity, omit `products` or pass an empty
    array; use `benefit_product_ids` or `exclude_product_ids` for the applicable relation update.
    For an ongoing flash deal, you can add products or SKUs, but you cannot change the price or purchase
    limits of products or SKUs already in the activity. To remove products or SKUs, use [Remove Activity
    Product](https://partner.tiktokshop.com/docv2/page/650acfd84a0bb702c072b4eb).

    Args:
        activity_id (str):
        body (UpdatePromotionActivityProductsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdatePromotionActivityProductsResponse
    """

    return (
        await asyncio_detailed(
            activity_id=activity_id,
            client=client,
            body=body,
        )
    ).parsed
