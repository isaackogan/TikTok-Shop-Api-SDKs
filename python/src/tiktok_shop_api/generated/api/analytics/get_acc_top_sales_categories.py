from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_acc_top_sales_categories_page_size import GetAccTopSalesCategoriesPageSize
from ...models.get_acc_top_sales_categories_response import GetACCTopSalesCategoriesResponse
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    *,
    brand_id: str,
    industry_id: str,
    date: datetime.date | Unset = UNSET,
    trend_days: int | Unset = UNSET,
    audience_type: str,
    scope: str | Unset = UNSET,
    keyword: str | Unset = UNSET,
    sort_field: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    page_size: GetAccTopSalesCategoriesPageSize | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["brand_id"] = brand_id

    params["industry_id"] = industry_id

    json_date: str | Unset = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    params["trend_days"] = trend_days

    params["audience_type"] = audience_type

    params["scope"] = scope

    params["keyword"] = keyword

    params["sort_field"] = sort_field

    params["sort_order"] = sort_order

    json_page_size: int | Unset = UNSET
    if not isinstance(page_size, Unset):
        json_page_size = page_size.value

    params["page_size"] = json_page_size

    params["page_token"] = page_token


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202610/acc/preferences/product/categories",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetACCTopSalesCategoriesResponse | None:
    if response.status_code == 200:
        response_200 = GetACCTopSalesCategoriesResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetACCTopSalesCategoriesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    brand_id: str,
    industry_id: str,
    date: datetime.date | Unset = UNSET,
    trend_days: int | Unset = UNSET,
    audience_type: str,
    scope: str | Unset = UNSET,
    keyword: str | Unset = UNSET,
    sort_field: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    page_size: GetAccTopSalesCategoriesPageSize | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> Response[GetACCTopSalesCategoriesResponse]:
    """ Get ACC Top Sales Categories

     Get ACC product category sales rankings for the selected audience, brand and date window. Results
    contain level-2 categories with level-3 children; sorting and pagination apply to the level-2
    categories.

    Args:
        brand_id (str):
        industry_id (str):
        date (datetime.date | Unset):
        trend_days (int | Unset):
        audience_type (str):
        scope (str | Unset):
        keyword (str | Unset):
        sort_field (str | Unset):
        sort_order (str | Unset):
        page_size (GetAccTopSalesCategoriesPageSize | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetACCTopSalesCategoriesResponse]
     """


    kwargs = _get_kwargs(
        brand_id=brand_id,
industry_id=industry_id,
date=date,
trend_days=trend_days,
audience_type=audience_type,
scope=scope,
keyword=keyword,
sort_field=sort_field,
sort_order=sort_order,
page_size=page_size,
page_token=page_token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    brand_id: str,
    industry_id: str,
    date: datetime.date | Unset = UNSET,
    trend_days: int | Unset = UNSET,
    audience_type: str,
    scope: str | Unset = UNSET,
    keyword: str | Unset = UNSET,
    sort_field: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    page_size: GetAccTopSalesCategoriesPageSize | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> GetACCTopSalesCategoriesResponse | None:
    """ Get ACC Top Sales Categories

     Get ACC product category sales rankings for the selected audience, brand and date window. Results
    contain level-2 categories with level-3 children; sorting and pagination apply to the level-2
    categories.

    Args:
        brand_id (str):
        industry_id (str):
        date (datetime.date | Unset):
        trend_days (int | Unset):
        audience_type (str):
        scope (str | Unset):
        keyword (str | Unset):
        sort_field (str | Unset):
        sort_order (str | Unset):
        page_size (GetAccTopSalesCategoriesPageSize | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetACCTopSalesCategoriesResponse
     """


    return sync_detailed(
        client=client,
brand_id=brand_id,
industry_id=industry_id,
date=date,
trend_days=trend_days,
audience_type=audience_type,
scope=scope,
keyword=keyword,
sort_field=sort_field,
sort_order=sort_order,
page_size=page_size,
page_token=page_token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    brand_id: str,
    industry_id: str,
    date: datetime.date | Unset = UNSET,
    trend_days: int | Unset = UNSET,
    audience_type: str,
    scope: str | Unset = UNSET,
    keyword: str | Unset = UNSET,
    sort_field: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    page_size: GetAccTopSalesCategoriesPageSize | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> Response[GetACCTopSalesCategoriesResponse]:
    """ Get ACC Top Sales Categories

     Get ACC product category sales rankings for the selected audience, brand and date window. Results
    contain level-2 categories with level-3 children; sorting and pagination apply to the level-2
    categories.

    Args:
        brand_id (str):
        industry_id (str):
        date (datetime.date | Unset):
        trend_days (int | Unset):
        audience_type (str):
        scope (str | Unset):
        keyword (str | Unset):
        sort_field (str | Unset):
        sort_order (str | Unset):
        page_size (GetAccTopSalesCategoriesPageSize | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetACCTopSalesCategoriesResponse]
     """


    kwargs = _get_kwargs(
        brand_id=brand_id,
industry_id=industry_id,
date=date,
trend_days=trend_days,
audience_type=audience_type,
scope=scope,
keyword=keyword,
sort_field=sort_field,
sort_order=sort_order,
page_size=page_size,
page_token=page_token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    brand_id: str,
    industry_id: str,
    date: datetime.date | Unset = UNSET,
    trend_days: int | Unset = UNSET,
    audience_type: str,
    scope: str | Unset = UNSET,
    keyword: str | Unset = UNSET,
    sort_field: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    page_size: GetAccTopSalesCategoriesPageSize | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> GetACCTopSalesCategoriesResponse | None:
    """ Get ACC Top Sales Categories

     Get ACC product category sales rankings for the selected audience, brand and date window. Results
    contain level-2 categories with level-3 children; sorting and pagination apply to the level-2
    categories.

    Args:
        brand_id (str):
        industry_id (str):
        date (datetime.date | Unset):
        trend_days (int | Unset):
        audience_type (str):
        scope (str | Unset):
        keyword (str | Unset):
        sort_field (str | Unset):
        sort_order (str | Unset):
        page_size (GetAccTopSalesCategoriesPageSize | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetACCTopSalesCategoriesResponse
     """


    return (await asyncio_detailed(
        client=client,
brand_id=brand_id,
industry_id=industry_id,
date=date,
trend_days=trend_days,
audience_type=audience_type,
scope=scope,
keyword=keyword,
sort_field=sort_field,
sort_order=sort_order,
page_size=page_size,
page_token=page_token,

    )).parsed
