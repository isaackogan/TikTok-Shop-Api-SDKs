from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_external_order_references_platform import GetExternalOrderReferencesPlatform
from ...models.get_external_order_references_response import GetExternalOrderReferencesResponse
from ...types import UNSET, Response


def _get_kwargs(
    order_id: str,
    *,
    platform: GetExternalOrderReferencesPlatform,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_platform = platform.value
    params["platform"] = json_platform

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/order/202406/orders/{order_id}/external_orders".format(
            order_id=quote(str(order_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetExternalOrderReferencesResponse | None:
    if response.status_code == 200:
        response_200 = GetExternalOrderReferencesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetExternalOrderReferencesResponse]:
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
    platform: GetExternalOrderReferencesPlatform,
) -> Response[GetExternalOrderReferencesResponse]:
    """Get External Order References

     If you have used the `Add External Order References` API, use this API to retrieve the external
    order references associated with a TikTok Shop order for the specified external order management
    system (OMS) platform.

    Args:
        order_id (str):
        platform (GetExternalOrderReferencesPlatform):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetExternalOrderReferencesResponse]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        platform=platform,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,
    platform: GetExternalOrderReferencesPlatform,
) -> GetExternalOrderReferencesResponse | None:
    """Get External Order References

     If you have used the `Add External Order References` API, use this API to retrieve the external
    order references associated with a TikTok Shop order for the specified external order management
    system (OMS) platform.

    Args:
        order_id (str):
        platform (GetExternalOrderReferencesPlatform):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetExternalOrderReferencesResponse
    """

    return sync_detailed(
        order_id=order_id,
        client=client,
        platform=platform,
    ).parsed


async def asyncio_detailed(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,
    platform: GetExternalOrderReferencesPlatform,
) -> Response[GetExternalOrderReferencesResponse]:
    """Get External Order References

     If you have used the `Add External Order References` API, use this API to retrieve the external
    order references associated with a TikTok Shop order for the specified external order management
    system (OMS) platform.

    Args:
        order_id (str):
        platform (GetExternalOrderReferencesPlatform):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetExternalOrderReferencesResponse]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        platform=platform,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,
    platform: GetExternalOrderReferencesPlatform,
) -> GetExternalOrderReferencesResponse | None:
    """Get External Order References

     If you have used the `Add External Order References` API, use this API to retrieve the external
    order references associated with a TikTok Shop order for the specified external order management
    system (OMS) platform.

    Args:
        order_id (str):
        platform (GetExternalOrderReferencesPlatform):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetExternalOrderReferencesResponse
    """

    return (
        await asyncio_detailed(
            order_id=order_id,
            client=client,
            platform=platform,
        )
    ).parsed
