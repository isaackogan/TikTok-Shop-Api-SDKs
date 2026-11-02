from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_off_site_performance_overview_response import GetOffSitePerformanceOverviewResponse
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
        "url": "/analytics/202610/off_site/overview",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetOffSitePerformanceOverviewResponse | None:
    if response.status_code == 200:
        response_200 = GetOffSitePerformanceOverviewResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetOffSitePerformanceOverviewResponse]:
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

) -> Response[GetOffSitePerformanceOverviewResponse]:
    """ Get Off Site Performance Overview

     Retrieve weekly off-site performance metrics and trends.

    Args:
        date (datetime.date | Unset):
        pixel_id (str):
        attribution_setting (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOffSitePerformanceOverviewResponse]
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

) -> GetOffSitePerformanceOverviewResponse | None:
    """ Get Off Site Performance Overview

     Retrieve weekly off-site performance metrics and trends.

    Args:
        date (datetime.date | Unset):
        pixel_id (str):
        attribution_setting (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOffSitePerformanceOverviewResponse
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

) -> Response[GetOffSitePerformanceOverviewResponse]:
    """ Get Off Site Performance Overview

     Retrieve weekly off-site performance metrics and trends.

    Args:
        date (datetime.date | Unset):
        pixel_id (str):
        attribution_setting (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOffSitePerformanceOverviewResponse]
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

) -> GetOffSitePerformanceOverviewResponse | None:
    """ Get Off Site Performance Overview

     Retrieve weekly off-site performance metrics and trends.

    Args:
        date (datetime.date | Unset):
        pixel_id (str):
        attribution_setting (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOffSitePerformanceOverviewResponse
     """


    return (await asyncio_detailed(
        client=client,
date=date,
pixel_id=pixel_id,
attribution_setting=attribution_setting,

    )).parsed
