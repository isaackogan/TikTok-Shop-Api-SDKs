from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_sps_overview_response import GetSPSOverviewResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    locale: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["locale"] = locale


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202606/shop_performances/overview",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetSPSOverviewResponse | None:
    if response.status_code == 200:
        response_200 = GetSPSOverviewResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetSPSOverviewResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,

) -> Response[GetSPSOverviewResponse]:
    """ Get SPS Overview

     Returns the SPS overview for the authorized shop, including the score, tier, dimensions, benefits,
    and top issues.
    Shop Performance Score (SPS) reflects a shop’s performance across key operational and service
    metrics on TikTok Shop. By integrating the read-only SPS APIs, ISVs can retrieve a shop’s score,
    tier, benefits, and metric benchmarks, diagnose performance gaps, and drill down to the products,
    logistics providers, aftersales types, orders, or chats associated with specific issues. This
    enables ISVs to embed actionable performance insights into their solutions, helping merchants
    identify problem areas faster and take targeted actions to improve shop performance. Available only
    for US-region shops.
    Use case guide: [Click here](https://partner.tiktokshop.com/docv2/page/ph0ccose)

    Args:
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSPSOverviewResponse]
     """


    kwargs = _get_kwargs(
        locale=locale,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,

) -> GetSPSOverviewResponse | None:
    """ Get SPS Overview

     Returns the SPS overview for the authorized shop, including the score, tier, dimensions, benefits,
    and top issues.
    Shop Performance Score (SPS) reflects a shop’s performance across key operational and service
    metrics on TikTok Shop. By integrating the read-only SPS APIs, ISVs can retrieve a shop’s score,
    tier, benefits, and metric benchmarks, diagnose performance gaps, and drill down to the products,
    logistics providers, aftersales types, orders, or chats associated with specific issues. This
    enables ISVs to embed actionable performance insights into their solutions, helping merchants
    identify problem areas faster and take targeted actions to improve shop performance. Available only
    for US-region shops.
    Use case guide: [Click here](https://partner.tiktokshop.com/docv2/page/ph0ccose)

    Args:
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSPSOverviewResponse
     """


    return sync_detailed(
        client=client,
locale=locale,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,

) -> Response[GetSPSOverviewResponse]:
    """ Get SPS Overview

     Returns the SPS overview for the authorized shop, including the score, tier, dimensions, benefits,
    and top issues.
    Shop Performance Score (SPS) reflects a shop’s performance across key operational and service
    metrics on TikTok Shop. By integrating the read-only SPS APIs, ISVs can retrieve a shop’s score,
    tier, benefits, and metric benchmarks, diagnose performance gaps, and drill down to the products,
    logistics providers, aftersales types, orders, or chats associated with specific issues. This
    enables ISVs to embed actionable performance insights into their solutions, helping merchants
    identify problem areas faster and take targeted actions to improve shop performance. Available only
    for US-region shops.
    Use case guide: [Click here](https://partner.tiktokshop.com/docv2/page/ph0ccose)

    Args:
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSPSOverviewResponse]
     """


    kwargs = _get_kwargs(
        locale=locale,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,

) -> GetSPSOverviewResponse | None:
    """ Get SPS Overview

     Returns the SPS overview for the authorized shop, including the score, tier, dimensions, benefits,
    and top issues.
    Shop Performance Score (SPS) reflects a shop’s performance across key operational and service
    metrics on TikTok Shop. By integrating the read-only SPS APIs, ISVs can retrieve a shop’s score,
    tier, benefits, and metric benchmarks, diagnose performance gaps, and drill down to the products,
    logistics providers, aftersales types, orders, or chats associated with specific issues. This
    enables ISVs to embed actionable performance insights into their solutions, helping merchants
    identify problem areas faster and take targeted actions to improve shop performance. Available only
    for US-region shops.
    Use case guide: [Click here](https://partner.tiktokshop.com/docv2/page/ph0ccose)

    Args:
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSPSOverviewResponse
     """


    return (await asyncio_detailed(
        client=client,
locale=locale,

    )).parsed
