from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_sps_metric_problem_details_response import GetSPSMetricProblemDetailsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    metric_code: str,
    *,
    locale: str | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["locale"] = locale

    params["page_token"] = page_token

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202606/shop_performances/metrics/{metric_code}/problem_details".format(
            metric_code=quote(str(metric_code), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetSPSMetricProblemDetailsResponse | None:
    if response.status_code == 200:
        response_200 = GetSPSMetricProblemDetailsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetSPSMetricProblemDetailsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    metric_code: str,
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> Response[GetSPSMetricProblemDetailsResponse]:
    """Get SPS Metric Problem Details

     Returns problem order or chat details for a selected SPS metric.
    Shop Performance Score (SPS) reflects a shop’s performance across key operational and service
    metrics on TikTok Shop. By integrating the read-only SPS APIs, ISVs can retrieve a shop’s score,
    tier, benefits, and metric benchmarks, diagnose performance gaps, and drill down to the products,
    logistics providers, aftersales types, orders, or chats associated with specific issues. This
    enables ISVs to embed actionable performance insights into their solutions, helping merchants
    identify problem areas faster and take targeted actions to improve shop performance. Available only
    for US-region shops.
    Use case guide: [Click here](https://partner.tiktokshop.com/docv2/page/ph0ccose)

    Args:
        metric_code (str):
        locale (str | Unset):
        page_token (str | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSPSMetricProblemDetailsResponse]
    """

    kwargs = _get_kwargs(
        metric_code=metric_code,
        locale=locale,
        page_token=page_token,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    metric_code: str,
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> GetSPSMetricProblemDetailsResponse | None:
    """Get SPS Metric Problem Details

     Returns problem order or chat details for a selected SPS metric.
    Shop Performance Score (SPS) reflects a shop’s performance across key operational and service
    metrics on TikTok Shop. By integrating the read-only SPS APIs, ISVs can retrieve a shop’s score,
    tier, benefits, and metric benchmarks, diagnose performance gaps, and drill down to the products,
    logistics providers, aftersales types, orders, or chats associated with specific issues. This
    enables ISVs to embed actionable performance insights into their solutions, helping merchants
    identify problem areas faster and take targeted actions to improve shop performance. Available only
    for US-region shops.
    Use case guide: [Click here](https://partner.tiktokshop.com/docv2/page/ph0ccose)

    Args:
        metric_code (str):
        locale (str | Unset):
        page_token (str | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSPSMetricProblemDetailsResponse
    """

    return sync_detailed(
        metric_code=metric_code,
        client=client,
        locale=locale,
        page_token=page_token,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    metric_code: str,
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> Response[GetSPSMetricProblemDetailsResponse]:
    """Get SPS Metric Problem Details

     Returns problem order or chat details for a selected SPS metric.
    Shop Performance Score (SPS) reflects a shop’s performance across key operational and service
    metrics on TikTok Shop. By integrating the read-only SPS APIs, ISVs can retrieve a shop’s score,
    tier, benefits, and metric benchmarks, diagnose performance gaps, and drill down to the products,
    logistics providers, aftersales types, orders, or chats associated with specific issues. This
    enables ISVs to embed actionable performance insights into their solutions, helping merchants
    identify problem areas faster and take targeted actions to improve shop performance. Available only
    for US-region shops.
    Use case guide: [Click here](https://partner.tiktokshop.com/docv2/page/ph0ccose)

    Args:
        metric_code (str):
        locale (str | Unset):
        page_token (str | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSPSMetricProblemDetailsResponse]
    """

    kwargs = _get_kwargs(
        metric_code=metric_code,
        locale=locale,
        page_token=page_token,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    metric_code: str,
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
) -> GetSPSMetricProblemDetailsResponse | None:
    """Get SPS Metric Problem Details

     Returns problem order or chat details for a selected SPS metric.
    Shop Performance Score (SPS) reflects a shop’s performance across key operational and service
    metrics on TikTok Shop. By integrating the read-only SPS APIs, ISVs can retrieve a shop’s score,
    tier, benefits, and metric benchmarks, diagnose performance gaps, and drill down to the products,
    logistics providers, aftersales types, orders, or chats associated with specific issues. This
    enables ISVs to embed actionable performance insights into their solutions, helping merchants
    identify problem areas faster and take targeted actions to improve shop performance. Available only
    for US-region shops.
    Use case guide: [Click here](https://partner.tiktokshop.com/docv2/page/ph0ccose)

    Args:
        metric_code (str):
        locale (str | Unset):
        page_token (str | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSPSMetricProblemDetailsResponse
    """

    return (
        await asyncio_detailed(
            metric_code=metric_code,
            client=client,
            locale=locale,
            page_token=page_token,
            page_size=page_size,
        )
    ).parsed
