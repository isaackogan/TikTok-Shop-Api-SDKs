from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_off_site_audience_insights_response import GetOffSiteAudienceInsightsResponse
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    *,
    date: datetime.date | Unset = UNSET,
    pixel_id: str,
    attribution_setting: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_date: str | Unset = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    params["pixel_id"] = pixel_id

    params["attribution_setting"] = attribution_setting


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202610/off_site/insights",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetOffSiteAudienceInsightsResponse | None:
    if response.status_code == 200:
        response_200 = GetOffSiteAudienceInsightsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetOffSiteAudienceInsightsResponse]:
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

) -> Response[GetOffSiteAudienceInsightsResponse]:
    """ Get Off Site Audience Insights

     Compare weekly on-site and off-site attributed customer audience distributions.

    Lists use labels from the TikTok Shop customer distribution. Label filtering and top-10 limits mean
    that the returned percentages may not sum to 100%.

    If the report for the requested pixel and attribution setting is unavailable, results may use the
    shop-level report with VIEW_14D attribution. Empty distributions can indicate unavailable report
    data and do not necessarily mean that the shop had no customers.

    Args:
        date (datetime.date | Unset):
        pixel_id (str):
        attribution_setting (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOffSiteAudienceInsightsResponse]
     """


    kwargs = _get_kwargs(
        date=date,
pixel_id=pixel_id,
attribution_setting=attribution_setting,

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

) -> GetOffSiteAudienceInsightsResponse | None:
    """ Get Off Site Audience Insights

     Compare weekly on-site and off-site attributed customer audience distributions.

    Lists use labels from the TikTok Shop customer distribution. Label filtering and top-10 limits mean
    that the returned percentages may not sum to 100%.

    If the report for the requested pixel and attribution setting is unavailable, results may use the
    shop-level report with VIEW_14D attribution. Empty distributions can indicate unavailable report
    data and do not necessarily mean that the shop had no customers.

    Args:
        date (datetime.date | Unset):
        pixel_id (str):
        attribution_setting (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOffSiteAudienceInsightsResponse
     """


    return sync_detailed(
        client=client,
date=date,
pixel_id=pixel_id,
attribution_setting=attribution_setting,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    date: datetime.date | Unset = UNSET,
    pixel_id: str,
    attribution_setting: str,

) -> Response[GetOffSiteAudienceInsightsResponse]:
    """ Get Off Site Audience Insights

     Compare weekly on-site and off-site attributed customer audience distributions.

    Lists use labels from the TikTok Shop customer distribution. Label filtering and top-10 limits mean
    that the returned percentages may not sum to 100%.

    If the report for the requested pixel and attribution setting is unavailable, results may use the
    shop-level report with VIEW_14D attribution. Empty distributions can indicate unavailable report
    data and do not necessarily mean that the shop had no customers.

    Args:
        date (datetime.date | Unset):
        pixel_id (str):
        attribution_setting (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOffSiteAudienceInsightsResponse]
     """


    kwargs = _get_kwargs(
        date=date,
pixel_id=pixel_id,
attribution_setting=attribution_setting,

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

) -> GetOffSiteAudienceInsightsResponse | None:
    """ Get Off Site Audience Insights

     Compare weekly on-site and off-site attributed customer audience distributions.

    Lists use labels from the TikTok Shop customer distribution. Label filtering and top-10 limits mean
    that the returned percentages may not sum to 100%.

    If the report for the requested pixel and attribution setting is unavailable, results may use the
    shop-level report with VIEW_14D attribution. Empty distributions can indicate unavailable report
    data and do not necessarily mean that the shop had no customers.

    Args:
        date (datetime.date | Unset):
        pixel_id (str):
        attribution_setting (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOffSiteAudienceInsightsResponse
     """


    return (await asyncio_detailed(
        client=client,
date=date,
pixel_id=pixel_id,
attribution_setting=attribution_setting,

    )).parsed
