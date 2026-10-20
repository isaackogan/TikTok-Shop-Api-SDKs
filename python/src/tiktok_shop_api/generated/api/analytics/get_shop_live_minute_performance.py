from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_shop_live_minute_performance_response import GetShopLIVEMinutePerformanceResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    live_id: str,
    *,
    page_token: str | Unset = UNSET,
    currency: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page_token"] = page_token

    params["currency"] = currency


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202510/shop_lives/{live_id}/performance_per_minutes".format(live_id=quote(str(live_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetShopLIVEMinutePerformanceResponse | None:
    if response.status_code == 200:
        response_200 = GetShopLIVEMinutePerformanceResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetShopLIVEMinutePerformanceResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    live_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    currency: str | Unset = UNSET,

) -> Response[GetShopLIVEMinutePerformanceResponse]:
    """ Get Shop LIVE Minute Performance

     Returns minute-level performance for a LIVE session after the session is finished. This API only
    returns data for live streams hosted by the shop official account or marketing account.

    Args:
        live_id (str):
        page_token (str | Unset):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopLIVEMinutePerformanceResponse]
     """


    kwargs = _get_kwargs(
        live_id=live_id,
page_token=page_token,
currency=currency,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    live_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    currency: str | Unset = UNSET,

) -> GetShopLIVEMinutePerformanceResponse | None:
    """ Get Shop LIVE Minute Performance

     Returns minute-level performance for a LIVE session after the session is finished. This API only
    returns data for live streams hosted by the shop official account or marketing account.

    Args:
        live_id (str):
        page_token (str | Unset):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopLIVEMinutePerformanceResponse
     """


    return sync_detailed(
        live_id=live_id,
client=client,
page_token=page_token,
currency=currency,

    ).parsed

async def asyncio_detailed(
    live_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    currency: str | Unset = UNSET,

) -> Response[GetShopLIVEMinutePerformanceResponse]:
    """ Get Shop LIVE Minute Performance

     Returns minute-level performance for a LIVE session after the session is finished. This API only
    returns data for live streams hosted by the shop official account or marketing account.

    Args:
        live_id (str):
        page_token (str | Unset):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShopLIVEMinutePerformanceResponse]
     """


    kwargs = _get_kwargs(
        live_id=live_id,
page_token=page_token,
currency=currency,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    live_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_token: str | Unset = UNSET,
    currency: str | Unset = UNSET,

) -> GetShopLIVEMinutePerformanceResponse | None:
    """ Get Shop LIVE Minute Performance

     Returns minute-level performance for a LIVE session after the session is finished. This API only
    returns data for live streams hosted by the shop official account or marketing account.

    Args:
        live_id (str):
        page_token (str | Unset):
        currency (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShopLIVEMinutePerformanceResponse
     """


    return (await asyncio_detailed(
        live_id=live_id,
client=client,
page_token=page_token,
currency=currency,

    )).parsed
