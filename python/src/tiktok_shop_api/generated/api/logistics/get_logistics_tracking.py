from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_logistics_tracking_response import GetLogisticsTrackingResponse
from ...types import Response


def _get_kwargs(
    order_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/logistics/202604/orders/{order_id}/tracking".format(
            order_id=quote(str(order_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetLogisticsTrackingResponse | None:
    if response.status_code == 200:
        response_200 = GetLogisticsTrackingResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetLogisticsTrackingResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetLogisticsTrackingResponse]:
    """Get Logistics Tracking

     Use this API to retrieve detailed logistics tracking information for an order. This API currently
    supports only cross-border trade (CBT) orders. Compared with Get Tracking, this API groups
    information by parcel and can include each parcel's carrier, latest tracking number, and tracking-
    event history.

    For the mapping between `action_code` and `action_code_name`, see
    https://partner.tiktokshop.com/docv2/page/37tihrdq.

    Args:
        order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLogisticsTrackingResponse]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetLogisticsTrackingResponse | None:
    """Get Logistics Tracking

     Use this API to retrieve detailed logistics tracking information for an order. This API currently
    supports only cross-border trade (CBT) orders. Compared with Get Tracking, this API groups
    information by parcel and can include each parcel's carrier, latest tracking number, and tracking-
    event history.

    For the mapping between `action_code` and `action_code_name`, see
    https://partner.tiktokshop.com/docv2/page/37tihrdq.

    Args:
        order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetLogisticsTrackingResponse
    """

    return sync_detailed(
        order_id=order_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetLogisticsTrackingResponse]:
    """Get Logistics Tracking

     Use this API to retrieve detailed logistics tracking information for an order. This API currently
    supports only cross-border trade (CBT) orders. Compared with Get Tracking, this API groups
    information by parcel and can include each parcel's carrier, latest tracking number, and tracking-
    event history.

    For the mapping between `action_code` and `action_code_name`, see
    https://partner.tiktokshop.com/docv2/page/37tihrdq.

    Args:
        order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLogisticsTrackingResponse]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetLogisticsTrackingResponse | None:
    """Get Logistics Tracking

     Use this API to retrieve detailed logistics tracking information for an order. This API currently
    supports only cross-border trade (CBT) orders. Compared with Get Tracking, this API groups
    information by parcel and can include each parcel's carrier, latest tracking number, and tracking-
    event history.

    For the mapping between `action_code` and `action_code_name`, see
    https://partner.tiktokshop.com/docv2/page/37tihrdq.

    Args:
        order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetLogisticsTrackingResponse
    """

    return (
        await asyncio_detailed(
            order_id=order_id,
            client=client,
        )
    ).parsed
