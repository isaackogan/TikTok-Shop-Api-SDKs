from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_orders_by_external_order_reference_platform import SearchOrdersByExternalOrderReferencePlatform
from ...models.search_orders_by_external_order_reference_request import SearchOrdersByExternalOrderReferenceRequest
from ...models.search_orders_by_external_order_reference_response import SearchOrdersByExternalOrderReferenceResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SearchOrdersByExternalOrderReferenceRequest | Unset = UNSET,
    platform: SearchOrdersByExternalOrderReferencePlatform,
    external_order_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_platform = platform.value
    params["platform"] = json_platform

    params["external_order_id"] = external_order_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/order/202406/orders/external_order_search",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SearchOrdersByExternalOrderReferenceResponse | None:
    if response.status_code == 200:
        response_200 = SearchOrdersByExternalOrderReferenceResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SearchOrdersByExternalOrderReferenceResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchOrdersByExternalOrderReferenceRequest | Unset = UNSET,
    platform: SearchOrdersByExternalOrderReferencePlatform,
    external_order_id: str,
) -> Response[SearchOrdersByExternalOrderReferenceResponse]:
    """Search Orders by External Order Reference

     If you have used the `Add External Order References` API to sync information from your external
    order management system (OMS) to corresponding orders in TikTok Shop, you may call this API to
    search for order information in TikTok Shop based on information in your OMS.

    Args:
        platform (SearchOrdersByExternalOrderReferencePlatform):
        external_order_id (str):
        body (SearchOrdersByExternalOrderReferenceRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchOrdersByExternalOrderReferenceResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        platform=platform,
        external_order_id=external_order_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SearchOrdersByExternalOrderReferenceRequest | Unset = UNSET,
    platform: SearchOrdersByExternalOrderReferencePlatform,
    external_order_id: str,
) -> SearchOrdersByExternalOrderReferenceResponse | None:
    """Search Orders by External Order Reference

     If you have used the `Add External Order References` API to sync information from your external
    order management system (OMS) to corresponding orders in TikTok Shop, you may call this API to
    search for order information in TikTok Shop based on information in your OMS.

    Args:
        platform (SearchOrdersByExternalOrderReferencePlatform):
        external_order_id (str):
        body (SearchOrdersByExternalOrderReferenceRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchOrdersByExternalOrderReferenceResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        platform=platform,
        external_order_id=external_order_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchOrdersByExternalOrderReferenceRequest | Unset = UNSET,
    platform: SearchOrdersByExternalOrderReferencePlatform,
    external_order_id: str,
) -> Response[SearchOrdersByExternalOrderReferenceResponse]:
    """Search Orders by External Order Reference

     If you have used the `Add External Order References` API to sync information from your external
    order management system (OMS) to corresponding orders in TikTok Shop, you may call this API to
    search for order information in TikTok Shop based on information in your OMS.

    Args:
        platform (SearchOrdersByExternalOrderReferencePlatform):
        external_order_id (str):
        body (SearchOrdersByExternalOrderReferenceRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchOrdersByExternalOrderReferenceResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        platform=platform,
        external_order_id=external_order_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchOrdersByExternalOrderReferenceRequest | Unset = UNSET,
    platform: SearchOrdersByExternalOrderReferencePlatform,
    external_order_id: str,
) -> SearchOrdersByExternalOrderReferenceResponse | None:
    """Search Orders by External Order Reference

     If you have used the `Add External Order References` API to sync information from your external
    order management system (OMS) to corresponding orders in TikTok Shop, you may call this API to
    search for order information in TikTok Shop based on information in your OMS.

    Args:
        platform (SearchOrdersByExternalOrderReferencePlatform):
        external_order_id (str):
        body (SearchOrdersByExternalOrderReferenceRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchOrdersByExternalOrderReferenceResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            platform=platform,
            external_order_id=external_order_id,
        )
    ).parsed
