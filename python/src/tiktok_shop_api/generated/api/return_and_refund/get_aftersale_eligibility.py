from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_aftersale_eligibility_initiate_aftersale_user import GetAftersaleEligibilityInitiateAftersaleUser
from ...models.get_aftersale_eligibility_request_types_item import GetAftersaleEligibilityRequestTypesItem
from ...models.get_aftersale_eligibility_response import GetAftersaleEligibilityResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    order_id: str,
    *,
    initiate_aftersale_user: GetAftersaleEligibilityInitiateAftersaleUser | Unset = UNSET,
    request_types: list[GetAftersaleEligibilityRequestTypesItem] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_initiate_aftersale_user: str | Unset = UNSET
    if not isinstance(initiate_aftersale_user, Unset):
        json_initiate_aftersale_user = initiate_aftersale_user.value

    params["initiate_aftersale_user"] = json_initiate_aftersale_user

    json_request_types: list[str] | Unset = UNSET
    if not isinstance(request_types, Unset):
        json_request_types = []
        for request_types_item_data in request_types:
            request_types_item = request_types_item_data.value
            json_request_types.append(request_types_item)

    params["request_types"] = json_request_types

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/return_refund/202602/orders/{order_id}/aftersale_eligibility".format(
            order_id=quote(str(order_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetAftersaleEligibilityResponse | None:
    if response.status_code == 200:
        response_200 = GetAftersaleEligibilityResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetAftersaleEligibilityResponse]:
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
    initiate_aftersale_user: GetAftersaleEligibilityInitiateAftersaleUser | Unset = UNSET,
    request_types: list[GetAftersaleEligibilityRequestTypesItem] | Unset = UNSET,
) -> Response[GetAftersaleEligibilityResponse]:
    """Get Aftersale Eligibility

     Use this API to check whether a seller or buyer can initiate refund-only, return-and-refund, or
    cancellation requests for an order. The response groups eligibility by SKU, order line item, and
    aftersale request type.

    Args:
        order_id (str):
        initiate_aftersale_user (GetAftersaleEligibilityInitiateAftersaleUser | Unset):
        request_types (list[GetAftersaleEligibilityRequestTypesItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAftersaleEligibilityResponse]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        initiate_aftersale_user=initiate_aftersale_user,
        request_types=request_types,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,
    initiate_aftersale_user: GetAftersaleEligibilityInitiateAftersaleUser | Unset = UNSET,
    request_types: list[GetAftersaleEligibilityRequestTypesItem] | Unset = UNSET,
) -> GetAftersaleEligibilityResponse | None:
    """Get Aftersale Eligibility

     Use this API to check whether a seller or buyer can initiate refund-only, return-and-refund, or
    cancellation requests for an order. The response groups eligibility by SKU, order line item, and
    aftersale request type.

    Args:
        order_id (str):
        initiate_aftersale_user (GetAftersaleEligibilityInitiateAftersaleUser | Unset):
        request_types (list[GetAftersaleEligibilityRequestTypesItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAftersaleEligibilityResponse
    """

    return sync_detailed(
        order_id=order_id,
        client=client,
        initiate_aftersale_user=initiate_aftersale_user,
        request_types=request_types,
    ).parsed


async def asyncio_detailed(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,
    initiate_aftersale_user: GetAftersaleEligibilityInitiateAftersaleUser | Unset = UNSET,
    request_types: list[GetAftersaleEligibilityRequestTypesItem] | Unset = UNSET,
) -> Response[GetAftersaleEligibilityResponse]:
    """Get Aftersale Eligibility

     Use this API to check whether a seller or buyer can initiate refund-only, return-and-refund, or
    cancellation requests for an order. The response groups eligibility by SKU, order line item, and
    aftersale request type.

    Args:
        order_id (str):
        initiate_aftersale_user (GetAftersaleEligibilityInitiateAftersaleUser | Unset):
        request_types (list[GetAftersaleEligibilityRequestTypesItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAftersaleEligibilityResponse]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        initiate_aftersale_user=initiate_aftersale_user,
        request_types=request_types,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    order_id: str,
    *,
    client: AuthenticatedClient | Client,
    initiate_aftersale_user: GetAftersaleEligibilityInitiateAftersaleUser | Unset = UNSET,
    request_types: list[GetAftersaleEligibilityRequestTypesItem] | Unset = UNSET,
) -> GetAftersaleEligibilityResponse | None:
    """Get Aftersale Eligibility

     Use this API to check whether a seller or buyer can initiate refund-only, return-and-refund, or
    cancellation requests for an order. The response groups eligibility by SKU, order line item, and
    aftersale request type.

    Args:
        order_id (str):
        initiate_aftersale_user (GetAftersaleEligibilityInitiateAftersaleUser | Unset):
        request_types (list[GetAftersaleEligibilityRequestTypesItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAftersaleEligibilityResponse
    """

    return (
        await asyncio_detailed(
            order_id=order_id,
            client=client,
            initiate_aftersale_user=initiate_aftersale_user,
            request_types=request_types,
        )
    ).parsed
