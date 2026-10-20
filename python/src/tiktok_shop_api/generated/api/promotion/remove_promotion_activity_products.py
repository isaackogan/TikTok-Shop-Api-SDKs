from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.remove_promotion_activity_products_request import RemovePromotionActivityProductsRequest
from ...models.remove_promotion_activity_products_response import RemovePromotionActivityProductsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    activity_id: str,
    *,
    body: RemovePromotionActivityProductsRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/promotion/202309/activities/{activity_id}/products".format(activity_id=quote(str(activity_id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RemovePromotionActivityProductsResponse | None:
    if response.status_code == 200:
        response_200 = RemovePromotionActivityProductsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RemovePromotionActivityProductsResponse]:
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
    body: RemovePromotionActivityProductsRequest | Unset = UNSET,

) -> Response[RemovePromotionActivityProductsResponse]:
    """ Remove Promotion Activity Products

     Use this API for `FIXED_PRICE`, `DIRECT_DISCOUNT`, `FLASHSALE`, `BUY_MORE_SAVE_MORE`, `BUY_X_GET_Y`,
    `GIFT_WITH_PURCHASE`, and `SHIPPING_DISCOUNT` activities. Provide at least one non-empty removal
    list; omitting the body, sending an empty object, or sending only empty lists does not request an
    item removal.
    - When removing ordinary activity products from a PRODUCT-scoped activity, use `product_ids` and do
    not provide `sku_ids`.
    - When removing ordinary activity products or SKUs from a VARIATION-scoped activity, use
    `product_ids`, `sku_ids`, or both.
    - For `GIFT_WITH_PURCHASE`, provide a non-empty `product_ids` list; the other removal lists are not
    processed by its branch.
    - For `BUY_MORE_SAVE_MORE` or `BUY_X_GET_Y`, `benefit_product_ids` removes benefit-product relations
    without requiring `product_ids`.
    - For a SHOP-scoped `BUY_MORE_SAVE_MORE`, `BUY_X_GET_Y`, or `SHIPPING_DISCOUNT` activity,
    `exclude_product_ids` removes excluded-product relations.
    You can provide multiple applicable non-empty lists in one ordinary non-GWP request. You cannot
    remove items from a `DEACTIVATED` or `EXPIRED` activity.

    Args:
        activity_id (str):
        body (RemovePromotionActivityProductsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemovePromotionActivityProductsResponse]
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
    body: RemovePromotionActivityProductsRequest | Unset = UNSET,

) -> RemovePromotionActivityProductsResponse | None:
    """ Remove Promotion Activity Products

     Use this API for `FIXED_PRICE`, `DIRECT_DISCOUNT`, `FLASHSALE`, `BUY_MORE_SAVE_MORE`, `BUY_X_GET_Y`,
    `GIFT_WITH_PURCHASE`, and `SHIPPING_DISCOUNT` activities. Provide at least one non-empty removal
    list; omitting the body, sending an empty object, or sending only empty lists does not request an
    item removal.
    - When removing ordinary activity products from a PRODUCT-scoped activity, use `product_ids` and do
    not provide `sku_ids`.
    - When removing ordinary activity products or SKUs from a VARIATION-scoped activity, use
    `product_ids`, `sku_ids`, or both.
    - For `GIFT_WITH_PURCHASE`, provide a non-empty `product_ids` list; the other removal lists are not
    processed by its branch.
    - For `BUY_MORE_SAVE_MORE` or `BUY_X_GET_Y`, `benefit_product_ids` removes benefit-product relations
    without requiring `product_ids`.
    - For a SHOP-scoped `BUY_MORE_SAVE_MORE`, `BUY_X_GET_Y`, or `SHIPPING_DISCOUNT` activity,
    `exclude_product_ids` removes excluded-product relations.
    You can provide multiple applicable non-empty lists in one ordinary non-GWP request. You cannot
    remove items from a `DEACTIVATED` or `EXPIRED` activity.

    Args:
        activity_id (str):
        body (RemovePromotionActivityProductsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemovePromotionActivityProductsResponse
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
    body: RemovePromotionActivityProductsRequest | Unset = UNSET,

) -> Response[RemovePromotionActivityProductsResponse]:
    """ Remove Promotion Activity Products

     Use this API for `FIXED_PRICE`, `DIRECT_DISCOUNT`, `FLASHSALE`, `BUY_MORE_SAVE_MORE`, `BUY_X_GET_Y`,
    `GIFT_WITH_PURCHASE`, and `SHIPPING_DISCOUNT` activities. Provide at least one non-empty removal
    list; omitting the body, sending an empty object, or sending only empty lists does not request an
    item removal.
    - When removing ordinary activity products from a PRODUCT-scoped activity, use `product_ids` and do
    not provide `sku_ids`.
    - When removing ordinary activity products or SKUs from a VARIATION-scoped activity, use
    `product_ids`, `sku_ids`, or both.
    - For `GIFT_WITH_PURCHASE`, provide a non-empty `product_ids` list; the other removal lists are not
    processed by its branch.
    - For `BUY_MORE_SAVE_MORE` or `BUY_X_GET_Y`, `benefit_product_ids` removes benefit-product relations
    without requiring `product_ids`.
    - For a SHOP-scoped `BUY_MORE_SAVE_MORE`, `BUY_X_GET_Y`, or `SHIPPING_DISCOUNT` activity,
    `exclude_product_ids` removes excluded-product relations.
    You can provide multiple applicable non-empty lists in one ordinary non-GWP request. You cannot
    remove items from a `DEACTIVATED` or `EXPIRED` activity.

    Args:
        activity_id (str):
        body (RemovePromotionActivityProductsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemovePromotionActivityProductsResponse]
     """


    kwargs = _get_kwargs(
        activity_id=activity_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    activity_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RemovePromotionActivityProductsRequest | Unset = UNSET,

) -> RemovePromotionActivityProductsResponse | None:
    """ Remove Promotion Activity Products

     Use this API for `FIXED_PRICE`, `DIRECT_DISCOUNT`, `FLASHSALE`, `BUY_MORE_SAVE_MORE`, `BUY_X_GET_Y`,
    `GIFT_WITH_PURCHASE`, and `SHIPPING_DISCOUNT` activities. Provide at least one non-empty removal
    list; omitting the body, sending an empty object, or sending only empty lists does not request an
    item removal.
    - When removing ordinary activity products from a PRODUCT-scoped activity, use `product_ids` and do
    not provide `sku_ids`.
    - When removing ordinary activity products or SKUs from a VARIATION-scoped activity, use
    `product_ids`, `sku_ids`, or both.
    - For `GIFT_WITH_PURCHASE`, provide a non-empty `product_ids` list; the other removal lists are not
    processed by its branch.
    - For `BUY_MORE_SAVE_MORE` or `BUY_X_GET_Y`, `benefit_product_ids` removes benefit-product relations
    without requiring `product_ids`.
    - For a SHOP-scoped `BUY_MORE_SAVE_MORE`, `BUY_X_GET_Y`, or `SHIPPING_DISCOUNT` activity,
    `exclude_product_ids` removes excluded-product relations.
    You can provide multiple applicable non-empty lists in one ordinary non-GWP request. You cannot
    remove items from a `DEACTIVATED` or `EXPIRED` activity.

    Args:
        activity_id (str):
        body (RemovePromotionActivityProductsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemovePromotionActivityProductsResponse
     """


    return (await asyncio_detailed(
        activity_id=activity_id,
client=client,
body=body,

    )).parsed
