from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_acc_audience_overview_response import GetACCAudienceOverviewResponse
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    *,
    brand_id: str,
    industry_id: str,
    date: datetime.date | Unset = UNSET,
    benchmark: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["brand_id"] = brand_id

    params["industry_id"] = industry_id

    json_date: str | Unset = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    params["benchmark"] = benchmark


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202610/acc/overview",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetACCAudienceOverviewResponse | None:
    if response.status_code == 200:
        response_200 = GetACCAudienceOverviewResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetACCAudienceOverviewResponse]:
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
    benchmark: str | Unset = UNSET,

) -> Response[GetACCAudienceOverviewResponse]:
    """ Get ACC Audience Overview

     Get ACC audience key metrics, benchmarks, and trends.

    Args:
        brand_id (str):
        industry_id (str):
        date (datetime.date | Unset):
        benchmark (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetACCAudienceOverviewResponse]
     """


    kwargs = _get_kwargs(
        brand_id=brand_id,
industry_id=industry_id,
date=date,
benchmark=benchmark,

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
    benchmark: str | Unset = UNSET,

) -> GetACCAudienceOverviewResponse | None:
    """ Get ACC Audience Overview

     Get ACC audience key metrics, benchmarks, and trends.

    Args:
        brand_id (str):
        industry_id (str):
        date (datetime.date | Unset):
        benchmark (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetACCAudienceOverviewResponse
     """


    return sync_detailed(
        client=client,
brand_id=brand_id,
industry_id=industry_id,
date=date,
benchmark=benchmark,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    brand_id: str,
    industry_id: str,
    date: datetime.date | Unset = UNSET,
    benchmark: str | Unset = UNSET,

) -> Response[GetACCAudienceOverviewResponse]:
    """ Get ACC Audience Overview

     Get ACC audience key metrics, benchmarks, and trends.

    Args:
        brand_id (str):
        industry_id (str):
        date (datetime.date | Unset):
        benchmark (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetACCAudienceOverviewResponse]
     """


    kwargs = _get_kwargs(
        brand_id=brand_id,
industry_id=industry_id,
date=date,
benchmark=benchmark,

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
    benchmark: str | Unset = UNSET,

) -> GetACCAudienceOverviewResponse | None:
    """ Get ACC Audience Overview

     Get ACC audience key metrics, benchmarks, and trends.

    Args:
        brand_id (str):
        industry_id (str):
        date (datetime.date | Unset):
        benchmark (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetACCAudienceOverviewResponse
     """


    return (await asyncio_detailed(
        client=client,
brand_id=brand_id,
industry_id=industry_id,
date=date,
benchmark=benchmark,

    )).parsed
