from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_off_site_performance_details_content_type import GetOffSitePerformanceDetailsContentType
from ...models.get_off_site_performance_details_response import GetOffSitePerformanceDetailsResponse
from ...models.get_off_site_performance_details_sort_order import GetOffSitePerformanceDetailsSortOrder
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    *,
    date: datetime.date | Unset = UNSET,
    pixel_id: str,
    attribution_setting: str,
    content_type: GetOffSitePerformanceDetailsContentType,
    sort_field: str | Unset = UNSET,
    sort_order: GetOffSitePerformanceDetailsSortOrder | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_date: str | Unset = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    params["pixel_id"] = pixel_id

    params["attribution_setting"] = attribution_setting

    json_content_type = content_type.value
    params["content_type"] = json_content_type

    params["sort_field"] = sort_field

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sort_order"] = json_sort_order

    params["page_size"] = page_size

    params["page_token"] = page_token


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202610/off_site/details",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetOffSitePerformanceDetailsResponse | None:
    if response.status_code == 200:
        response_200 = GetOffSitePerformanceDetailsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetOffSitePerformanceDetailsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    date: datetime.date | Unset = UNSET,
    pixel_id: str,
    attribution_setting: str,
    content_type: GetOffSitePerformanceDetailsContentType,
    sort_field: str | Unset = UNSET,
    sort_order: GetOffSitePerformanceDetailsSortOrder | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> Response[GetOffSitePerformanceDetailsResponse]:
    """ Get Off Site Performance Details

     Retrieve paginated weekly off-site performance details for videos, LIVE sessions, or products,
    including GMV and off-site effect metrics.

    If the report for the requested pixel and attribution setting is unavailable, results may use the
    shop-level report with VIEW_14D attribution. If neither report is available, no content records are
    returned.

    Args:
        date (datetime.date | Unset):
        pixel_id (str):
        attribution_setting (str):
        content_type (GetOffSitePerformanceDetailsContentType):
        sort_field (str | Unset):
        sort_order (GetOffSitePerformanceDetailsSortOrder | Unset):
        page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOffSitePerformanceDetailsResponse]
     """


    kwargs = _get_kwargs(
        date=date,
pixel_id=pixel_id,
attribution_setting=attribution_setting,
content_type=content_type,
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
    date: datetime.date | Unset = UNSET,
    pixel_id: str,
    attribution_setting: str,
    content_type: GetOffSitePerformanceDetailsContentType,
    sort_field: str | Unset = UNSET,
    sort_order: GetOffSitePerformanceDetailsSortOrder | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> GetOffSitePerformanceDetailsResponse | None:
    """ Get Off Site Performance Details

     Retrieve paginated weekly off-site performance details for videos, LIVE sessions, or products,
    including GMV and off-site effect metrics.

    If the report for the requested pixel and attribution setting is unavailable, results may use the
    shop-level report with VIEW_14D attribution. If neither report is available, no content records are
    returned.

    Args:
        date (datetime.date | Unset):
        pixel_id (str):
        attribution_setting (str):
        content_type (GetOffSitePerformanceDetailsContentType):
        sort_field (str | Unset):
        sort_order (GetOffSitePerformanceDetailsSortOrder | Unset):
        page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOffSitePerformanceDetailsResponse
     """


    return sync_detailed(
        client=client,
date=date,
pixel_id=pixel_id,
attribution_setting=attribution_setting,
content_type=content_type,
sort_field=sort_field,
sort_order=sort_order,
page_size=page_size,
page_token=page_token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    date: datetime.date | Unset = UNSET,
    pixel_id: str,
    attribution_setting: str,
    content_type: GetOffSitePerformanceDetailsContentType,
    sort_field: str | Unset = UNSET,
    sort_order: GetOffSitePerformanceDetailsSortOrder | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> Response[GetOffSitePerformanceDetailsResponse]:
    """ Get Off Site Performance Details

     Retrieve paginated weekly off-site performance details for videos, LIVE sessions, or products,
    including GMV and off-site effect metrics.

    If the report for the requested pixel and attribution setting is unavailable, results may use the
    shop-level report with VIEW_14D attribution. If neither report is available, no content records are
    returned.

    Args:
        date (datetime.date | Unset):
        pixel_id (str):
        attribution_setting (str):
        content_type (GetOffSitePerformanceDetailsContentType):
        sort_field (str | Unset):
        sort_order (GetOffSitePerformanceDetailsSortOrder | Unset):
        page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOffSitePerformanceDetailsResponse]
     """


    kwargs = _get_kwargs(
        date=date,
pixel_id=pixel_id,
attribution_setting=attribution_setting,
content_type=content_type,
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
    date: datetime.date | Unset = UNSET,
    pixel_id: str,
    attribution_setting: str,
    content_type: GetOffSitePerformanceDetailsContentType,
    sort_field: str | Unset = UNSET,
    sort_order: GetOffSitePerformanceDetailsSortOrder | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> GetOffSitePerformanceDetailsResponse | None:
    """ Get Off Site Performance Details

     Retrieve paginated weekly off-site performance details for videos, LIVE sessions, or products,
    including GMV and off-site effect metrics.

    If the report for the requested pixel and attribution setting is unavailable, results may use the
    shop-level report with VIEW_14D attribution. If neither report is available, no content records are
    returned.

    Args:
        date (datetime.date | Unset):
        pixel_id (str):
        attribution_setting (str):
        content_type (GetOffSitePerformanceDetailsContentType):
        sort_field (str | Unset):
        sort_order (GetOffSitePerformanceDetailsSortOrder | Unset):
        page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOffSitePerformanceDetailsResponse
     """


    return (await asyncio_detailed(
        client=client,
date=date,
pixel_id=pixel_id,
attribution_setting=attribution_setting,
content_type=content_type,
sort_field=sort_field,
sort_order=sort_order,
page_size=page_size,
page_token=page_token,

    )).parsed
