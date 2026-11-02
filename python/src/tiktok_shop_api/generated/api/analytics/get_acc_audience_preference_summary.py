from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_acc_audience_preference_summary_response import GetACCAudiencePreferenceSummaryResponse
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


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202610/acc/preferences/summary",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetACCAudiencePreferenceSummaryResponse | None:
    if response.status_code == 200:
        response_200 = GetACCAudiencePreferenceSummaryResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetACCAudiencePreferenceSummaryResponse]:
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

) -> Response[GetACCAudiencePreferenceSummaryResponse]:
    """ Get ACC Audience Preference Summary

     Retrieve ACC audience preference summaries for products, livestreams, videos, and photo posts for
    the selected brand, audience segment, scope, and reporting window.

    Args:
        brand_id (str):
        industry_id (str):
        date (datetime.date | Unset):
        trend_days (int | Unset):
        audience_type (str):
        scope (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetACCAudiencePreferenceSummaryResponse]
     """


    kwargs = _get_kwargs(
        brand_id=brand_id,
industry_id=industry_id,
date=date,
trend_days=trend_days,
audience_type=audience_type,
scope=scope,

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

) -> GetACCAudiencePreferenceSummaryResponse | None:
    """ Get ACC Audience Preference Summary

     Retrieve ACC audience preference summaries for products, livestreams, videos, and photo posts for
    the selected brand, audience segment, scope, and reporting window.

    Args:
        brand_id (str):
        industry_id (str):
        date (datetime.date | Unset):
        trend_days (int | Unset):
        audience_type (str):
        scope (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetACCAudiencePreferenceSummaryResponse
     """


    return sync_detailed(
        client=client,
brand_id=brand_id,
industry_id=industry_id,
date=date,
trend_days=trend_days,
audience_type=audience_type,
scope=scope,

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

) -> Response[GetACCAudiencePreferenceSummaryResponse]:
    """ Get ACC Audience Preference Summary

     Retrieve ACC audience preference summaries for products, livestreams, videos, and photo posts for
    the selected brand, audience segment, scope, and reporting window.

    Args:
        brand_id (str):
        industry_id (str):
        date (datetime.date | Unset):
        trend_days (int | Unset):
        audience_type (str):
        scope (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetACCAudiencePreferenceSummaryResponse]
     """


    kwargs = _get_kwargs(
        brand_id=brand_id,
industry_id=industry_id,
date=date,
trend_days=trend_days,
audience_type=audience_type,
scope=scope,

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

) -> GetACCAudiencePreferenceSummaryResponse | None:
    """ Get ACC Audience Preference Summary

     Retrieve ACC audience preference summaries for products, livestreams, videos, and photo posts for
    the selected brand, audience segment, scope, and reporting window.

    Args:
        brand_id (str):
        industry_id (str):
        date (datetime.date | Unset):
        trend_days (int | Unset):
        audience_type (str):
        scope (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetACCAudiencePreferenceSummaryResponse
     """


    return (await asyncio_detailed(
        client=client,
brand_id=brand_id,
industry_id=industry_id,
date=date,
trend_days=trend_days,
audience_type=audience_type,
scope=scope,

    )).parsed
