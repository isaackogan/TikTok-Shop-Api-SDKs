from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_ai_report_campaign_periods_response import GetAIReportCampaignPeriodsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page_token"] = page_token

    params["page_size"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202611/ai_report/campaigns",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAIReportCampaignPeriodsResponse | None:
    if response.status_code == 200:
        response_200 = GetAIReportCampaignPeriodsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAIReportCampaignPeriodsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,

) -> Response[GetAIReportCampaignPeriodsResponse]:
    """ Get AI Report Campaign Periods

     Retrieve the authorized shop's campaigns for the current year that have started by today. The server
    determines today using the shop region's configured local timezone. Campaign start_date and end_date
    are local calendar dates in that timezone, not UTC. Default order: start_date ascending, end_date
    ascending, then internal campaign ID descending for equal date pairs. Pass returned dates to data
    queries; a campaign ID is not required.

    Args:
        page_token (str | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAIReportCampaignPeriodsResponse]
     """


    kwargs = _get_kwargs(
        page_token=page_token,
page_size=page_size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,

) -> GetAIReportCampaignPeriodsResponse | None:
    """ Get AI Report Campaign Periods

     Retrieve the authorized shop's campaigns for the current year that have started by today. The server
    determines today using the shop region's configured local timezone. Campaign start_date and end_date
    are local calendar dates in that timezone, not UTC. Default order: start_date ascending, end_date
    ascending, then internal campaign ID descending for equal date pairs. Pass returned dates to data
    queries; a campaign ID is not required.

    Args:
        page_token (str | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAIReportCampaignPeriodsResponse
     """


    return sync_detailed(
        client=client,
page_token=page_token,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,

) -> Response[GetAIReportCampaignPeriodsResponse]:
    """ Get AI Report Campaign Periods

     Retrieve the authorized shop's campaigns for the current year that have started by today. The server
    determines today using the shop region's configured local timezone. Campaign start_date and end_date
    are local calendar dates in that timezone, not UTC. Default order: start_date ascending, end_date
    ascending, then internal campaign ID descending for equal date pairs. Pass returned dates to data
    queries; a campaign ID is not required.

    Args:
        page_token (str | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAIReportCampaignPeriodsResponse]
     """


    kwargs = _get_kwargs(
        page_token=page_token,
page_size=page_size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,

) -> GetAIReportCampaignPeriodsResponse | None:
    """ Get AI Report Campaign Periods

     Retrieve the authorized shop's campaigns for the current year that have started by today. The server
    determines today using the shop region's configured local timezone. Campaign start_date and end_date
    are local calendar dates in that timezone, not UTC. Default order: start_date ascending, end_date
    ascending, then internal campaign ID descending for equal date pairs. Pass returned dates to data
    queries; a campaign ID is not required.

    Args:
        page_token (str | Unset):
        page_size (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAIReportCampaignPeriodsResponse
     """


    return (await asyncio_detailed(
        client=client,
page_token=page_token,
page_size=page_size,

    )).parsed
