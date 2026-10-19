from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.confirm_order_split_request import ConfirmOrderSplitRequest
from ...models.confirm_order_split_response import ConfirmOrderSplitResponse
from ...types import Response


def _get_kwargs(
    order_id: str,
    *,
    body: ConfirmOrderSplitRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fulfillment/202309/orders/{order_id}/split".format(
            order_id=quote(str(order_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConfirmOrderSplitResponse | None:
    if response.status_code == 200:
        response_200 = ConfirmOrderSplitResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ConfirmOrderSplitResponse]:
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
    body: ConfirmOrderSplitRequest,
) -> Response[ConfirmOrderSplitResponse]:
    """Confirm Order Split

     Use this API to confirm an order split. Supported split levels vary by region:
    - Some regions support item-level splits (splitting individual units of the same SKU).
    - Others only support all-units splits (splitting different SKUs into separate packages).

    Here are two examples of supported splits:
    - **Case 1: all-units split**, applicable for orders in BR, SEA, MX (local sellers)
      Split a buyer order of SKU A of quantity 2 and SKU B of quantity 1 into two separate packages:
      - **Package 1**: all units of SKU A
      - **Package 2**: all units of SKU B

    - **Case 2: item-level split**, applicable for orders in EU, JP, MX (global sellers), UK, US
      Split the same order contents into three individual packages:
      - **Package 1**: 1 unit of SKU A
      - **Package 2**: 1 unit of SKU A
      - **Package 3**: 1 unit of SKU B

    Args:
        order_id (str):
        body (ConfirmOrderSplitRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfirmOrderSplitResponse]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ConfirmOrderSplitRequest,
) -> ConfirmOrderSplitResponse | None:
    """Confirm Order Split

     Use this API to confirm an order split. Supported split levels vary by region:
    - Some regions support item-level splits (splitting individual units of the same SKU).
    - Others only support all-units splits (splitting different SKUs into separate packages).

    Here are two examples of supported splits:
    - **Case 1: all-units split**, applicable for orders in BR, SEA, MX (local sellers)
      Split a buyer order of SKU A of quantity 2 and SKU B of quantity 1 into two separate packages:
      - **Package 1**: all units of SKU A
      - **Package 2**: all units of SKU B

    - **Case 2: item-level split**, applicable for orders in EU, JP, MX (global sellers), UK, US
      Split the same order contents into three individual packages:
      - **Package 1**: 1 unit of SKU A
      - **Package 2**: 1 unit of SKU A
      - **Package 3**: 1 unit of SKU B

    Args:
        order_id (str):
        body (ConfirmOrderSplitRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfirmOrderSplitResponse
    """

    return sync_detailed(
        order_id=order_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ConfirmOrderSplitRequest,
) -> Response[ConfirmOrderSplitResponse]:
    """Confirm Order Split

     Use this API to confirm an order split. Supported split levels vary by region:
    - Some regions support item-level splits (splitting individual units of the same SKU).
    - Others only support all-units splits (splitting different SKUs into separate packages).

    Here are two examples of supported splits:
    - **Case 1: all-units split**, applicable for orders in BR, SEA, MX (local sellers)
      Split a buyer order of SKU A of quantity 2 and SKU B of quantity 1 into two separate packages:
      - **Package 1**: all units of SKU A
      - **Package 2**: all units of SKU B

    - **Case 2: item-level split**, applicable for orders in EU, JP, MX (global sellers), UK, US
      Split the same order contents into three individual packages:
      - **Package 1**: 1 unit of SKU A
      - **Package 2**: 1 unit of SKU A
      - **Package 3**: 1 unit of SKU B

    Args:
        order_id (str):
        body (ConfirmOrderSplitRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfirmOrderSplitResponse]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ConfirmOrderSplitRequest,
) -> ConfirmOrderSplitResponse | None:
    """Confirm Order Split

     Use this API to confirm an order split. Supported split levels vary by region:
    - Some regions support item-level splits (splitting individual units of the same SKU).
    - Others only support all-units splits (splitting different SKUs into separate packages).

    Here are two examples of supported splits:
    - **Case 1: all-units split**, applicable for orders in BR, SEA, MX (local sellers)
      Split a buyer order of SKU A of quantity 2 and SKU B of quantity 1 into two separate packages:
      - **Package 1**: all units of SKU A
      - **Package 2**: all units of SKU B

    - **Case 2: item-level split**, applicable for orders in EU, JP, MX (global sellers), UK, US
      Split the same order contents into three individual packages:
      - **Package 1**: 1 unit of SKU A
      - **Package 2**: 1 unit of SKU A
      - **Package 3**: 1 unit of SKU B

    Args:
        order_id (str):
        body (ConfirmOrderSplitRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfirmOrderSplitResponse
    """

    return (
        await asyncio_detailed(
            order_id=order_id,
            client=client,
            body=body,
        )
    ).parsed
