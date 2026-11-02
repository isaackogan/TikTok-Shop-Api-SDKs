from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_acclive_sales_factors_audience_type import GetAccliveSalesFactorsAudienceType
from ...models.get_acclive_sales_factors_page_size import GetAccliveSalesFactorsPageSize
from ...models.get_acclive_sales_factors_response import GetACCLIVESalesFactorsResponse
from ...models.get_acclive_sales_factors_trend_days import GetAccliveSalesFactorsTrendDays
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    *,
    brand_id: str,
    industry_id: str,
    date: datetime.date | Unset = UNSET,
    trend_days: GetAccliveSalesFactorsTrendDays | Unset = UNSET,
    audience_type: GetAccliveSalesFactorsAudienceType,
    scope: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
    keyword: str | Unset = UNSET,
    sort_field: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    page_size: GetAccliveSalesFactorsPageSize | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["brand_id"] = brand_id

    params["industry_id"] = industry_id

    json_date: str | Unset = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    json_trend_days: int | Unset = UNSET
    if not isinstance(trend_days, Unset):
        json_trend_days = trend_days.value

    params["trend_days"] = json_trend_days

    json_audience_type = audience_type.value
    params["audience_type"] = json_audience_type

    params["scope"] = scope

    params["category_id"] = category_id

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
        "url": "/analytics/202610/acc/preferences/live/factors",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetACCLIVESalesFactorsResponse | None:
    if response.status_code == 200:
        response_200 = GetACCLIVESalesFactorsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetACCLIVESalesFactorsResponse]:
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
    trend_days: GetAccliveSalesFactorsTrendDays | Unset = UNSET,
    audience_type: GetAccliveSalesFactorsAudienceType,
    scope: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
    keyword: str | Unset = UNSET,
    sort_field: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    page_size: GetAccliveSalesFactorsPageSize | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> Response[GetACCLIVESalesFactorsResponse]:
    """ Get ACC LIVE Sales Factors

     Get a paginated ranking of LIVE types (sales factors) for a selected ACC audience, scope, and
    reporting window. Each factor includes its ID, display name, GMV range, and customer and order
    counts.

    Args:
        brand_id (str):
        industry_id (str):
        date (datetime.date | Unset):
        trend_days (GetAccliveSalesFactorsTrendDays | Unset):
        audience_type (GetAccliveSalesFactorsAudienceType):
        scope (str | Unset):
        category_id (str | Unset):
        keyword (str | Unset):
        sort_field (str | Unset):
        sort_order (str | Unset):
        page_size (GetAccliveSalesFactorsPageSize | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetACCLIVESalesFactorsResponse]
     """


    kwargs = _get_kwargs(
        brand_id=brand_id,
industry_id=industry_id,
date=date,
trend_days=trend_days,
audience_type=audience_type,
scope=scope,
category_id=category_id,
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
    trend_days: GetAccliveSalesFactorsTrendDays | Unset = UNSET,
    audience_type: GetAccliveSalesFactorsAudienceType,
    scope: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
    keyword: str | Unset = UNSET,
    sort_field: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    page_size: GetAccliveSalesFactorsPageSize | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> GetACCLIVESalesFactorsResponse | None:
    """ Get ACC LIVE Sales Factors

     Get a paginated ranking of LIVE types (sales factors) for a selected ACC audience, scope, and
    reporting window. Each factor includes its ID, display name, GMV range, and customer and order
    counts.

    Args:
        brand_id (str):
        industry_id (str):
        date (datetime.date | Unset):
        trend_days (GetAccliveSalesFactorsTrendDays | Unset):
        audience_type (GetAccliveSalesFactorsAudienceType):
        scope (str | Unset):
        category_id (str | Unset):
        keyword (str | Unset):
        sort_field (str | Unset):
        sort_order (str | Unset):
        page_size (GetAccliveSalesFactorsPageSize | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetACCLIVESalesFactorsResponse
     """


    return sync_detailed(
        client=client,
brand_id=brand_id,
industry_id=industry_id,
date=date,
trend_days=trend_days,
audience_type=audience_type,
scope=scope,
category_id=category_id,
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
    trend_days: GetAccliveSalesFactorsTrendDays | Unset = UNSET,
    audience_type: GetAccliveSalesFactorsAudienceType,
    scope: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
    keyword: str | Unset = UNSET,
    sort_field: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    page_size: GetAccliveSalesFactorsPageSize | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> Response[GetACCLIVESalesFactorsResponse]:
    """ Get ACC LIVE Sales Factors

     Get a paginated ranking of LIVE types (sales factors) for a selected ACC audience, scope, and
    reporting window. Each factor includes its ID, display name, GMV range, and customer and order
    counts.

    Args:
        brand_id (str):
        industry_id (str):
        date (datetime.date | Unset):
        trend_days (GetAccliveSalesFactorsTrendDays | Unset):
        audience_type (GetAccliveSalesFactorsAudienceType):
        scope (str | Unset):
        category_id (str | Unset):
        keyword (str | Unset):
        sort_field (str | Unset):
        sort_order (str | Unset):
        page_size (GetAccliveSalesFactorsPageSize | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetACCLIVESalesFactorsResponse]
     """


    kwargs = _get_kwargs(
        brand_id=brand_id,
industry_id=industry_id,
date=date,
trend_days=trend_days,
audience_type=audience_type,
scope=scope,
category_id=category_id,
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
    trend_days: GetAccliveSalesFactorsTrendDays | Unset = UNSET,
    audience_type: GetAccliveSalesFactorsAudienceType,
    scope: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
    keyword: str | Unset = UNSET,
    sort_field: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    page_size: GetAccliveSalesFactorsPageSize | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> GetACCLIVESalesFactorsResponse | None:
    """ Get ACC LIVE Sales Factors

     Get a paginated ranking of LIVE types (sales factors) for a selected ACC audience, scope, and
    reporting window. Each factor includes its ID, display name, GMV range, and customer and order
    counts.

    Args:
        brand_id (str):
        industry_id (str):
        date (datetime.date | Unset):
        trend_days (GetAccliveSalesFactorsTrendDays | Unset):
        audience_type (GetAccliveSalesFactorsAudienceType):
        scope (str | Unset):
        category_id (str | Unset):
        keyword (str | Unset):
        sort_field (str | Unset):
        sort_order (str | Unset):
        page_size (GetAccliveSalesFactorsPageSize | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetACCLIVESalesFactorsResponse
     """


    return (await asyncio_detailed(
        client=client,
brand_id=brand_id,
industry_id=industry_id,
date=date,
trend_days=trend_days,
audience_type=audience_type,
scope=scope,
category_id=category_id,
keyword=keyword,
sort_field=sort_field,
sort_order=sort_order,
page_size=page_size,
page_token=page_token,

    )).parsed
