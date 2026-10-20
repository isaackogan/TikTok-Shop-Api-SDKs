from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_opportunity_detail_response import GetOpportunityDetailResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    opportunity_id: str,
    *,
    locale: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["locale"] = locale


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/product/202604/opportunities/{opportunity_id}".format(opportunity_id=quote(str(opportunity_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetOpportunityDetailResponse | None:
    if response.status_code == 200:
        response_200 = GetOpportunityDetailResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetOpportunityDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    opportunity_id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,

) -> Response[GetOpportunityDetailResponse]:
    """ Get Opportunity Detail

     Retrieve the full details of a single opportunity lead by its ID, including market trend data,
    competition level, and recommended actions.

    Args:
        opportunity_id (str):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOpportunityDetailResponse]
     """


    kwargs = _get_kwargs(
        opportunity_id=opportunity_id,
locale=locale,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    opportunity_id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,

) -> GetOpportunityDetailResponse | None:
    """ Get Opportunity Detail

     Retrieve the full details of a single opportunity lead by its ID, including market trend data,
    competition level, and recommended actions.

    Args:
        opportunity_id (str):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOpportunityDetailResponse
     """


    return sync_detailed(
        opportunity_id=opportunity_id,
client=client,
locale=locale,

    ).parsed

async def asyncio_detailed(
    opportunity_id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,

) -> Response[GetOpportunityDetailResponse]:
    """ Get Opportunity Detail

     Retrieve the full details of a single opportunity lead by its ID, including market trend data,
    competition level, and recommended actions.

    Args:
        opportunity_id (str):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOpportunityDetailResponse]
     """


    kwargs = _get_kwargs(
        opportunity_id=opportunity_id,
locale=locale,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    opportunity_id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,

) -> GetOpportunityDetailResponse | None:
    """ Get Opportunity Detail

     Retrieve the full details of a single opportunity lead by its ID, including market trend data,
    competition level, and recommended actions.

    Args:
        opportunity_id (str):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOpportunityDetailResponse
     """


    return (await asyncio_detailed(
        opportunity_id=opportunity_id,
client=client,
locale=locale,

    )).parsed
