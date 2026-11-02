from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_acc_audience_preference_list_page_size import GetAccAudiencePreferenceListPageSize
from ...models.get_acc_audience_preference_list_response import GetACCAudiencePreferenceListResponse
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
    entity_type: str,
    scope: str | Unset = UNSET,
    keyword: str | Unset = UNSET,
    l2_category_id: str | Unset = UNSET,
    l3_category_id: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
    factor_id: str | Unset = UNSET,
    sort_field: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    page_size: GetAccAudiencePreferenceListPageSize | Unset = UNSET,
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

    params["entity_type"] = entity_type

    params["scope"] = scope

    params["keyword"] = keyword

    params["l2_category_id"] = l2_category_id

    params["l3_category_id"] = l3_category_id

    params["category_id"] = category_id

    params["factor_id"] = factor_id

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
        "url": "/analytics/202610/acc/preferences",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetACCAudiencePreferenceListResponse | None:
    if response.status_code == 200:
        response_200 = GetACCAudiencePreferenceListResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetACCAudiencePreferenceListResponse]:
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
    entity_type: str,
    scope: str | Unset = UNSET,
    keyword: str | Unset = UNSET,
    l2_category_id: str | Unset = UNSET,
    l3_category_id: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
    factor_id: str | Unset = UNSET,
    sort_field: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    page_size: GetAccAudiencePreferenceListPageSize | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> Response[GetACCAudiencePreferenceListResponse]:
    """ Get ACC Audience Preference List

     Get a paginated ranking of products, live streams, videos, or photo posts preferred by the selected
    ACC audience for a brand.

    Use `entity_type` to choose the ranking. Each item contains its rank, entity information and
    preference metrics; `entity_detail` varies by entity type. Select the analysis window with `date`
    and `trend_days`, and use `scope` to choose shop-level or market-level results. To retrieve more
    results, pass the returned `page_token` as `page_token` in the next request.

    Args:
        brand_id (str):
        industry_id (str):
        date (datetime.date | Unset):
        trend_days (int | Unset):
        audience_type (str):
        entity_type (str):
        scope (str | Unset):
        keyword (str | Unset):
        l2_category_id (str | Unset):
        l3_category_id (str | Unset):
        category_id (str | Unset):
        factor_id (str | Unset):
        sort_field (str | Unset):
        sort_order (str | Unset):
        page_size (GetAccAudiencePreferenceListPageSize | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetACCAudiencePreferenceListResponse]
     """


    kwargs = _get_kwargs(
        brand_id=brand_id,
industry_id=industry_id,
date=date,
trend_days=trend_days,
audience_type=audience_type,
entity_type=entity_type,
scope=scope,
keyword=keyword,
l2_category_id=l2_category_id,
l3_category_id=l3_category_id,
category_id=category_id,
factor_id=factor_id,
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
    entity_type: str,
    scope: str | Unset = UNSET,
    keyword: str | Unset = UNSET,
    l2_category_id: str | Unset = UNSET,
    l3_category_id: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
    factor_id: str | Unset = UNSET,
    sort_field: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    page_size: GetAccAudiencePreferenceListPageSize | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> GetACCAudiencePreferenceListResponse | None:
    """ Get ACC Audience Preference List

     Get a paginated ranking of products, live streams, videos, or photo posts preferred by the selected
    ACC audience for a brand.

    Use `entity_type` to choose the ranking. Each item contains its rank, entity information and
    preference metrics; `entity_detail` varies by entity type. Select the analysis window with `date`
    and `trend_days`, and use `scope` to choose shop-level or market-level results. To retrieve more
    results, pass the returned `page_token` as `page_token` in the next request.

    Args:
        brand_id (str):
        industry_id (str):
        date (datetime.date | Unset):
        trend_days (int | Unset):
        audience_type (str):
        entity_type (str):
        scope (str | Unset):
        keyword (str | Unset):
        l2_category_id (str | Unset):
        l3_category_id (str | Unset):
        category_id (str | Unset):
        factor_id (str | Unset):
        sort_field (str | Unset):
        sort_order (str | Unset):
        page_size (GetAccAudiencePreferenceListPageSize | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetACCAudiencePreferenceListResponse
     """


    return sync_detailed(
        client=client,
brand_id=brand_id,
industry_id=industry_id,
date=date,
trend_days=trend_days,
audience_type=audience_type,
entity_type=entity_type,
scope=scope,
keyword=keyword,
l2_category_id=l2_category_id,
l3_category_id=l3_category_id,
category_id=category_id,
factor_id=factor_id,
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
    entity_type: str,
    scope: str | Unset = UNSET,
    keyword: str | Unset = UNSET,
    l2_category_id: str | Unset = UNSET,
    l3_category_id: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
    factor_id: str | Unset = UNSET,
    sort_field: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    page_size: GetAccAudiencePreferenceListPageSize | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> Response[GetACCAudiencePreferenceListResponse]:
    """ Get ACC Audience Preference List

     Get a paginated ranking of products, live streams, videos, or photo posts preferred by the selected
    ACC audience for a brand.

    Use `entity_type` to choose the ranking. Each item contains its rank, entity information and
    preference metrics; `entity_detail` varies by entity type. Select the analysis window with `date`
    and `trend_days`, and use `scope` to choose shop-level or market-level results. To retrieve more
    results, pass the returned `page_token` as `page_token` in the next request.

    Args:
        brand_id (str):
        industry_id (str):
        date (datetime.date | Unset):
        trend_days (int | Unset):
        audience_type (str):
        entity_type (str):
        scope (str | Unset):
        keyword (str | Unset):
        l2_category_id (str | Unset):
        l3_category_id (str | Unset):
        category_id (str | Unset):
        factor_id (str | Unset):
        sort_field (str | Unset):
        sort_order (str | Unset):
        page_size (GetAccAudiencePreferenceListPageSize | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetACCAudiencePreferenceListResponse]
     """


    kwargs = _get_kwargs(
        brand_id=brand_id,
industry_id=industry_id,
date=date,
trend_days=trend_days,
audience_type=audience_type,
entity_type=entity_type,
scope=scope,
keyword=keyword,
l2_category_id=l2_category_id,
l3_category_id=l3_category_id,
category_id=category_id,
factor_id=factor_id,
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
    entity_type: str,
    scope: str | Unset = UNSET,
    keyword: str | Unset = UNSET,
    l2_category_id: str | Unset = UNSET,
    l3_category_id: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
    factor_id: str | Unset = UNSET,
    sort_field: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    page_size: GetAccAudiencePreferenceListPageSize | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> GetACCAudiencePreferenceListResponse | None:
    """ Get ACC Audience Preference List

     Get a paginated ranking of products, live streams, videos, or photo posts preferred by the selected
    ACC audience for a brand.

    Use `entity_type` to choose the ranking. Each item contains its rank, entity information and
    preference metrics; `entity_detail` varies by entity type. Select the analysis window with `date`
    and `trend_days`, and use `scope` to choose shop-level or market-level results. To retrieve more
    results, pass the returned `page_token` as `page_token` in the next request.

    Args:
        brand_id (str):
        industry_id (str):
        date (datetime.date | Unset):
        trend_days (int | Unset):
        audience_type (str):
        entity_type (str):
        scope (str | Unset):
        keyword (str | Unset):
        l2_category_id (str | Unset):
        l3_category_id (str | Unset):
        category_id (str | Unset):
        factor_id (str | Unset):
        sort_field (str | Unset):
        sort_order (str | Unset):
        page_size (GetAccAudiencePreferenceListPageSize | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetACCAudiencePreferenceListResponse
     """


    return (await asyncio_detailed(
        client=client,
brand_id=brand_id,
industry_id=industry_id,
date=date,
trend_days=trend_days,
audience_type=audience_type,
entity_type=entity_type,
scope=scope,
keyword=keyword,
l2_category_id=l2_category_id,
l3_category_id=l3_category_id,
category_id=category_id,
factor_id=factor_id,
sort_field=sort_field,
sort_order=sort_order,
page_size=page_size,
page_token=page_token,

    )).parsed
