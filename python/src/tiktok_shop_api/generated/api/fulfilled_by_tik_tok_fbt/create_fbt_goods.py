from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_fbt_goods_request import CreateFBTGoodsRequest
from ...models.create_fbt_goods_response import CreateFBTGoodsResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateFBTGoodsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fbt/202607/goods/create_goods",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateFBTGoodsResponse | None:
    if response.status_code == 200:
        response_200 = CreateFBTGoodsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateFBTGoodsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateFBTGoodsRequest,
) -> Response[CreateFBTGoodsResponse]:
    """Create FBT Goods

     Create FBT goods records and link each record to a TikTok Shop SKU. Request-level errors can be
    returned before per-item results are populated. When `create_result_info.create_result_list`
    contains entries, correlate them by `tts_sku_id`, check `is_success` for each returned item, read
    `fail_reason` for failures, and use `tts_goods_id` for successes.

    The request supports dimensions and weight, return handling, hazardous-material, shelf-life, SIOC,
    bulky-item, and safety attributes.

    Args:
        body (CreateFBTGoodsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateFBTGoodsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateFBTGoodsRequest,
) -> CreateFBTGoodsResponse | None:
    """Create FBT Goods

     Create FBT goods records and link each record to a TikTok Shop SKU. Request-level errors can be
    returned before per-item results are populated. When `create_result_info.create_result_list`
    contains entries, correlate them by `tts_sku_id`, check `is_success` for each returned item, read
    `fail_reason` for failures, and use `tts_goods_id` for successes.

    The request supports dimensions and weight, return handling, hazardous-material, shelf-life, SIOC,
    bulky-item, and safety attributes.

    Args:
        body (CreateFBTGoodsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateFBTGoodsResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateFBTGoodsRequest,
) -> Response[CreateFBTGoodsResponse]:
    """Create FBT Goods

     Create FBT goods records and link each record to a TikTok Shop SKU. Request-level errors can be
    returned before per-item results are populated. When `create_result_info.create_result_list`
    contains entries, correlate them by `tts_sku_id`, check `is_success` for each returned item, read
    `fail_reason` for failures, and use `tts_goods_id` for successes.

    The request supports dimensions and weight, return handling, hazardous-material, shelf-life, SIOC,
    bulky-item, and safety attributes.

    Args:
        body (CreateFBTGoodsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateFBTGoodsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateFBTGoodsRequest,
) -> CreateFBTGoodsResponse | None:
    """Create FBT Goods

     Create FBT goods records and link each record to a TikTok Shop SKU. Request-level errors can be
    returned before per-item results are populated. When `create_result_info.create_result_list`
    contains entries, correlate them by `tts_sku_id`, check `is_success` for each returned item, read
    `fail_reason` for failures, and use `tts_goods_id` for successes.

    The request supports dimensions and weight, return handling, hazardous-material, shelf-life, SIOC,
    bulky-item, and safety attributes.

    Args:
        body (CreateFBTGoodsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateFBTGoodsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
