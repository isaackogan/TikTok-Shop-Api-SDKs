from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.check_shipping_template_existence_response import CheckShippingTemplateExistenceResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    access_token: str,
    shop_id: int | Unset = UNSET,
    biz_warehouse_id: int,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["access_token"] = access_token

    params["shop_id"] = shop_id

    params["biz_warehouse_id"] = biz_warehouse_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/logistics/202606/seller_template/template_exist",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CheckShippingTemplateExistenceResponse | None:
    if response.status_code == 200:
        response_200 = CheckShippingTemplateExistenceResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CheckShippingTemplateExistenceResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    access_token: str,
    shop_id: int | Unset = UNSET,
    biz_warehouse_id: int,
) -> Response[CheckShippingTemplateExistenceResponse]:
    """Check Shipping Template Existence

     Checks whether the authenticated shop has a shipping template for the specified business warehouse.

    Args:
        access_token (str):
        shop_id (int | Unset):
        biz_warehouse_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckShippingTemplateExistenceResponse]
    """

    kwargs = _get_kwargs(
        access_token=access_token,
        shop_id=shop_id,
        biz_warehouse_id=biz_warehouse_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    access_token: str,
    shop_id: int | Unset = UNSET,
    biz_warehouse_id: int,
) -> CheckShippingTemplateExistenceResponse | None:
    """Check Shipping Template Existence

     Checks whether the authenticated shop has a shipping template for the specified business warehouse.

    Args:
        access_token (str):
        shop_id (int | Unset):
        biz_warehouse_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckShippingTemplateExistenceResponse
    """

    return sync_detailed(
        client=client,
        access_token=access_token,
        shop_id=shop_id,
        biz_warehouse_id=biz_warehouse_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    access_token: str,
    shop_id: int | Unset = UNSET,
    biz_warehouse_id: int,
) -> Response[CheckShippingTemplateExistenceResponse]:
    """Check Shipping Template Existence

     Checks whether the authenticated shop has a shipping template for the specified business warehouse.

    Args:
        access_token (str):
        shop_id (int | Unset):
        biz_warehouse_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckShippingTemplateExistenceResponse]
    """

    kwargs = _get_kwargs(
        access_token=access_token,
        shop_id=shop_id,
        biz_warehouse_id=biz_warehouse_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    access_token: str,
    shop_id: int | Unset = UNSET,
    biz_warehouse_id: int,
) -> CheckShippingTemplateExistenceResponse | None:
    """Check Shipping Template Existence

     Checks whether the authenticated shop has a shipping template for the specified business warehouse.

    Args:
        access_token (str):
        shop_id (int | Unset):
        biz_warehouse_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckShippingTemplateExistenceResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            access_token=access_token,
            shop_id=shop_id,
            biz_warehouse_id=biz_warehouse_id,
        )
    ).parsed
