from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_shop_sku_performance_detail_granularity import GetShopSkuPerformanceDetailGranularity
from ...models.get_shop_sku_performance_detail_response import GetShopSKUPerformanceDetailResponse
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    sku_id: str,
    *,
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    granularity: GetShopSkuPerformanceDetailGranularity | Unset = UNSET,
    currency: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_start_date_ge = start_date_ge.isoformat()
    params["start_date_ge"] = json_start_date_ge

    json_end_date_lt = end_date_lt.isoformat()
    params["end_date_lt"] = json_end_date_lt

    json_granularity: str | Unset = UNSET
    if not isinstance(granularity, Unset):
        json_granularity = granularity.value

    params["granularity"] = json_granularity

    params["currency"] = currency


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202509/shop_skus/{sku_id}/performance".format(sku_id=quote(str(sku_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetShopSKUPerformanceDetailResponse | None:
    if response.status_code == 200:
        response_200 = GetShopSKUPerformanceDetailResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetShopSKUPerformanceDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sku_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    granularity: GetShopSkuPerformanceDetailGranularity | Unset = UNSET,
    currency: str | Unset = UNSET,

) -> Response[GetShopSKUPerformanceDetailResponse]:
    """ Get Shop SKU Performance Detail

     Returns performance metrics for the specified SKU.

    Args:
        sku_id (str):
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        granularity (GetShopSkuPerformanceDetailGranularity | Unset):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopSKUPerformanceDetailResponse]
     """


    kwargs = _get_kwargs(
        sku_id=sku_id,
start_date_ge=start_date_ge,
end_date_lt=end_date_lt,
granularity=granularity,
currency=currency,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    sku_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    granularity: GetShopSkuPerformanceDetailGranularity | Unset = UNSET,
    currency: str | Unset = UNSET,

) -> GetShopSKUPerformanceDetailResponse | None:
    """ Get Shop SKU Performance Detail

     Returns performance metrics for the specified SKU.

    Args:
        sku_id (str):
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        granularity (GetShopSkuPerformanceDetailGranularity | Unset):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopSKUPerformanceDetailResponse
     """


    return sync_detailed(
        sku_id=sku_id,
client=client,
start_date_ge=start_date_ge,
end_date_lt=end_date_lt,
granularity=granularity,
currency=currency,

    ).parsed

async def asyncio_detailed(
    sku_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    granularity: GetShopSkuPerformanceDetailGranularity | Unset = UNSET,
    currency: str | Unset = UNSET,

) -> Response[GetShopSKUPerformanceDetailResponse]:
    """ Get Shop SKU Performance Detail

     Returns performance metrics for the specified SKU.

    Args:
        sku_id (str):
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        granularity (GetShopSkuPerformanceDetailGranularity | Unset):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopSKUPerformanceDetailResponse]
     """


    kwargs = _get_kwargs(
        sku_id=sku_id,
start_date_ge=start_date_ge,
end_date_lt=end_date_lt,
granularity=granularity,
currency=currency,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    sku_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_date_ge: datetime.date,
    end_date_lt: datetime.date,
    granularity: GetShopSkuPerformanceDetailGranularity | Unset = UNSET,
    currency: str | Unset = UNSET,

) -> GetShopSKUPerformanceDetailResponse | None:
    """ Get Shop SKU Performance Detail

     Returns performance metrics for the specified SKU.

    Args:
        sku_id (str):
        start_date_ge (datetime.date):
        end_date_lt (datetime.date):
        granularity (GetShopSkuPerformanceDetailGranularity | Unset):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopSKUPerformanceDetailResponse
     """


    return (await asyncio_detailed(
        sku_id=sku_id,
client=client,
start_date_ge=start_date_ge,
end_date_lt=end_date_lt,
granularity=granularity,
currency=currency,

    )).parsed
