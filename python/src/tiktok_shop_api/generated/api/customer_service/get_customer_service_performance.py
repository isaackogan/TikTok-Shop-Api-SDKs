from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_customer_service_performance_response import GetCustomerServicePerformanceResponse
from typing import cast
import datetime



def _get_kwargs(
    *,
    support_date_ge: datetime.date,
    support_date_lt: datetime.date,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_support_date_ge = support_date_ge.isoformat()
    params["support_date_ge"] = json_support_date_ge

    json_support_date_lt = support_date_lt.isoformat()
    params["support_date_lt"] = json_support_date_lt


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/customer_service/202407/performance",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetCustomerServicePerformanceResponse | None:
    if response.status_code == 200:
        response_200 = GetCustomerServicePerformanceResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetCustomerServicePerformanceResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    support_date_ge: datetime.date,
    support_date_lt: datetime.date,

) -> Response[GetCustomerServicePerformanceResponse]:
    """ Get Customer Service Performance

     Retrieves customer service performance metrics for a shop over a selected time period.

    Args:
        support_date_ge (datetime.date):
        support_date_lt (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCustomerServicePerformanceResponse]
     """


    kwargs = _get_kwargs(
        support_date_ge=support_date_ge,
support_date_lt=support_date_lt,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    support_date_ge: datetime.date,
    support_date_lt: datetime.date,

) -> GetCustomerServicePerformanceResponse | None:
    """ Get Customer Service Performance

     Retrieves customer service performance metrics for a shop over a selected time period.

    Args:
        support_date_ge (datetime.date):
        support_date_lt (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCustomerServicePerformanceResponse
     """


    return sync_detailed(
        client=client,
support_date_ge=support_date_ge,
support_date_lt=support_date_lt,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    support_date_ge: datetime.date,
    support_date_lt: datetime.date,

) -> Response[GetCustomerServicePerformanceResponse]:
    """ Get Customer Service Performance

     Retrieves customer service performance metrics for a shop over a selected time period.

    Args:
        support_date_ge (datetime.date):
        support_date_lt (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCustomerServicePerformanceResponse]
     """


    kwargs = _get_kwargs(
        support_date_ge=support_date_ge,
support_date_lt=support_date_lt,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    support_date_ge: datetime.date,
    support_date_lt: datetime.date,

) -> GetCustomerServicePerformanceResponse | None:
    """ Get Customer Service Performance

     Retrieves customer service performance metrics for a shop over a selected time period.

    Args:
        support_date_ge (datetime.date):
        support_date_lt (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCustomerServicePerformanceResponse
     """


    return (await asyncio_detailed(
        client=client,
support_date_ge=support_date_ge,
support_date_lt=support_date_lt,

    )).parsed
