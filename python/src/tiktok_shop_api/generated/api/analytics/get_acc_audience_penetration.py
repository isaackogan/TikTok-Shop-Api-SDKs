from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_acc_audience_penetration_response import GetACCAudiencePenetrationResponse
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    *,
    brand_id: str,
    industry_id: str,
    date: datetime.date | Unset = UNSET,
    trend_days: int | Unset = UNSET,
    account_type: str | Unset = UNSET,
    form: str | Unset = UNSET,
    audience_type: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["brand_id"] = brand_id

    params["industry_id"] = industry_id

    json_date: str | Unset = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    params["trend_days"] = trend_days

    params["account_type"] = account_type

    params["form"] = form

    params["audience_type"] = audience_type


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202610/acc/penetration",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetACCAudiencePenetrationResponse | None:
    if response.status_code == 200:
        response_200 = GetACCAudiencePenetrationResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetACCAudiencePenetrationResponse]:
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
    account_type: str | Unset = UNSET,
    form: str | Unset = UNSET,
    audience_type: str | Unset = UNSET,

) -> Response[GetACCAudiencePenetrationResponse]:
    """ Get ACC Audience Penetration

     Retrieve viewed, clicked, and ordered audience counts and penetration ratios for a brand over the
    selected reporting window.

    Use brand_id and industry_id from the same brands[] record returned by Get ACC Brands (GET
    /analytics/202610/acc/brands) for the current shop. Select the initial audience with audience_type;
    account_type and form filter the reported segments.

    Args:
        brand_id (str):
        industry_id (str):
        date (datetime.date | Unset):
        trend_days (int | Unset):
        account_type (str | Unset):
        form (str | Unset):
        audience_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetACCAudiencePenetrationResponse]
     """


    kwargs = _get_kwargs(
        brand_id=brand_id,
industry_id=industry_id,
date=date,
trend_days=trend_days,
account_type=account_type,
form=form,
audience_type=audience_type,

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
    account_type: str | Unset = UNSET,
    form: str | Unset = UNSET,
    audience_type: str | Unset = UNSET,

) -> GetACCAudiencePenetrationResponse | None:
    """ Get ACC Audience Penetration

     Retrieve viewed, clicked, and ordered audience counts and penetration ratios for a brand over the
    selected reporting window.

    Use brand_id and industry_id from the same brands[] record returned by Get ACC Brands (GET
    /analytics/202610/acc/brands) for the current shop. Select the initial audience with audience_type;
    account_type and form filter the reported segments.

    Args:
        brand_id (str):
        industry_id (str):
        date (datetime.date | Unset):
        trend_days (int | Unset):
        account_type (str | Unset):
        form (str | Unset):
        audience_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetACCAudiencePenetrationResponse
     """


    return sync_detailed(
        client=client,
brand_id=brand_id,
industry_id=industry_id,
date=date,
trend_days=trend_days,
account_type=account_type,
form=form,
audience_type=audience_type,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    brand_id: str,
    industry_id: str,
    date: datetime.date | Unset = UNSET,
    trend_days: int | Unset = UNSET,
    account_type: str | Unset = UNSET,
    form: str | Unset = UNSET,
    audience_type: str | Unset = UNSET,

) -> Response[GetACCAudiencePenetrationResponse]:
    """ Get ACC Audience Penetration

     Retrieve viewed, clicked, and ordered audience counts and penetration ratios for a brand over the
    selected reporting window.

    Use brand_id and industry_id from the same brands[] record returned by Get ACC Brands (GET
    /analytics/202610/acc/brands) for the current shop. Select the initial audience with audience_type;
    account_type and form filter the reported segments.

    Args:
        brand_id (str):
        industry_id (str):
        date (datetime.date | Unset):
        trend_days (int | Unset):
        account_type (str | Unset):
        form (str | Unset):
        audience_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetACCAudiencePenetrationResponse]
     """


    kwargs = _get_kwargs(
        brand_id=brand_id,
industry_id=industry_id,
date=date,
trend_days=trend_days,
account_type=account_type,
form=form,
audience_type=audience_type,

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
    account_type: str | Unset = UNSET,
    form: str | Unset = UNSET,
    audience_type: str | Unset = UNSET,

) -> GetACCAudiencePenetrationResponse | None:
    """ Get ACC Audience Penetration

     Retrieve viewed, clicked, and ordered audience counts and penetration ratios for a brand over the
    selected reporting window.

    Use brand_id and industry_id from the same brands[] record returned by Get ACC Brands (GET
    /analytics/202610/acc/brands) for the current shop. Select the initial audience with audience_type;
    account_type and form filter the reported segments.

    Args:
        brand_id (str):
        industry_id (str):
        date (datetime.date | Unset):
        trend_days (int | Unset):
        account_type (str | Unset):
        form (str | Unset):
        audience_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetACCAudiencePenetrationResponse
     """


    return (await asyncio_detailed(
        client=client,
brand_id=brand_id,
industry_id=industry_id,
date=date,
trend_days=trend_days,
account_type=account_type,
form=form,
audience_type=audience_type,

    )).parsed
