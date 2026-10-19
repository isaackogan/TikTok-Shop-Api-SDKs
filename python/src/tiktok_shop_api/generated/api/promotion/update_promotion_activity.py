from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_promotion_activity_request import UpdatePromotionActivityRequest
from ...models.update_promotion_activity_response import UpdatePromotionActivityResponse
from ...types import Response


def _get_kwargs(
    activity_id: str,
    *,
    body: UpdatePromotionActivityRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/promotion/202309/activities/{activity_id}".format(
            activity_id=quote(str(activity_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UpdatePromotionActivityResponse | None:
    if response.status_code == 200:
        response_200 = UpdatePromotionActivityResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdatePromotionActivityResponse]:
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
    body: UpdatePromotionActivityRequest,
) -> Response[UpdatePromotionActivityResponse]:
    """Update Promotion Activity

     Update an existing promotion activity. The stored activity type determines which request fields are
    processed:
    - For fixed-price, direct-discount, and flash-sale activities, update title, begin_time, and
    end_time; the other type-specific fields are not processed by this update path.
    - For a shipping-discount activity, provide discount.shipping_discount; use duration_type to choose
    a scheduled or indefinite activity.
    - For a Buy More Save More (BMSM) or Buy X Get Y (BXGY) activity, set duration_type to NORMAL, set
    product_level to PRODUCT or SHOP, provide exactly one participation_limit entry, and provide the
    matching discount object.
    - For a Gift With Purchase (GWP) activity, set duration_type to NORMAL, set product_level to
    PRODUCT, provide exactly one participation_limit entry, and provide discount.gift_discount.
    Fixed-price, direct-discount, flash-sale, BMSM, BXGY, and GWP activities cannot be updated after
    they are deactivated or expired. For those activity types, an upcoming activity with a normal
    schedule requires a future begin_time, while an ongoing activity must keep its existing begin_time.
    An ongoing BMSM or BXGY activity must also keep its existing first-tier threshold value, threshold
    type, discount type, product scope, participation limit, and target-user setting.

    Args:
        activity_id (str):
        body (UpdatePromotionActivityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdatePromotionActivityResponse]
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
    body: UpdatePromotionActivityRequest,
) -> UpdatePromotionActivityResponse | None:
    """Update Promotion Activity

     Update an existing promotion activity. The stored activity type determines which request fields are
    processed:
    - For fixed-price, direct-discount, and flash-sale activities, update title, begin_time, and
    end_time; the other type-specific fields are not processed by this update path.
    - For a shipping-discount activity, provide discount.shipping_discount; use duration_type to choose
    a scheduled or indefinite activity.
    - For a Buy More Save More (BMSM) or Buy X Get Y (BXGY) activity, set duration_type to NORMAL, set
    product_level to PRODUCT or SHOP, provide exactly one participation_limit entry, and provide the
    matching discount object.
    - For a Gift With Purchase (GWP) activity, set duration_type to NORMAL, set product_level to
    PRODUCT, provide exactly one participation_limit entry, and provide discount.gift_discount.
    Fixed-price, direct-discount, flash-sale, BMSM, BXGY, and GWP activities cannot be updated after
    they are deactivated or expired. For those activity types, an upcoming activity with a normal
    schedule requires a future begin_time, while an ongoing activity must keep its existing begin_time.
    An ongoing BMSM or BXGY activity must also keep its existing first-tier threshold value, threshold
    type, discount type, product scope, participation limit, and target-user setting.

    Args:
        activity_id (str):
        body (UpdatePromotionActivityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdatePromotionActivityResponse
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
    body: UpdatePromotionActivityRequest,
) -> Response[UpdatePromotionActivityResponse]:
    """Update Promotion Activity

     Update an existing promotion activity. The stored activity type determines which request fields are
    processed:
    - For fixed-price, direct-discount, and flash-sale activities, update title, begin_time, and
    end_time; the other type-specific fields are not processed by this update path.
    - For a shipping-discount activity, provide discount.shipping_discount; use duration_type to choose
    a scheduled or indefinite activity.
    - For a Buy More Save More (BMSM) or Buy X Get Y (BXGY) activity, set duration_type to NORMAL, set
    product_level to PRODUCT or SHOP, provide exactly one participation_limit entry, and provide the
    matching discount object.
    - For a Gift With Purchase (GWP) activity, set duration_type to NORMAL, set product_level to
    PRODUCT, provide exactly one participation_limit entry, and provide discount.gift_discount.
    Fixed-price, direct-discount, flash-sale, BMSM, BXGY, and GWP activities cannot be updated after
    they are deactivated or expired. For those activity types, an upcoming activity with a normal
    schedule requires a future begin_time, while an ongoing activity must keep its existing begin_time.
    An ongoing BMSM or BXGY activity must also keep its existing first-tier threshold value, threshold
    type, discount type, product scope, participation limit, and target-user setting.

    Args:
        activity_id (str):
        body (UpdatePromotionActivityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdatePromotionActivityResponse]
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
    body: UpdatePromotionActivityRequest,
) -> UpdatePromotionActivityResponse | None:
    """Update Promotion Activity

     Update an existing promotion activity. The stored activity type determines which request fields are
    processed:
    - For fixed-price, direct-discount, and flash-sale activities, update title, begin_time, and
    end_time; the other type-specific fields are not processed by this update path.
    - For a shipping-discount activity, provide discount.shipping_discount; use duration_type to choose
    a scheduled or indefinite activity.
    - For a Buy More Save More (BMSM) or Buy X Get Y (BXGY) activity, set duration_type to NORMAL, set
    product_level to PRODUCT or SHOP, provide exactly one participation_limit entry, and provide the
    matching discount object.
    - For a Gift With Purchase (GWP) activity, set duration_type to NORMAL, set product_level to
    PRODUCT, provide exactly one participation_limit entry, and provide discount.gift_discount.
    Fixed-price, direct-discount, flash-sale, BMSM, BXGY, and GWP activities cannot be updated after
    they are deactivated or expired. For those activity types, an upcoming activity with a normal
    schedule requires a future begin_time, while an ongoing activity must keep its existing begin_time.
    An ongoing BMSM or BXGY activity must also keep its existing first-tier threshold value, threshold
    type, discount type, product scope, participation limit, and target-user setting.

    Args:
        activity_id (str):
        body (UpdatePromotionActivityRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdatePromotionActivityResponse
    """

    return (
        await asyncio_detailed(
            activity_id=activity_id,
            client=client,
            body=body,
        )
    ).parsed
