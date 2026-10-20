from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.list_opportunities_request import ListOpportunitiesRequest
from ...models.list_opportunities_response import ListOpportunitiesResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: ListOpportunitiesRequest,
    page_size: int,
    page_token: str | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["page_size"] = page_size

    params["page_token"] = page_token

    params["locale"] = locale


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202604/opportunities/query",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ListOpportunitiesResponse | None:
    if response.status_code == 200:
        response_200 = ListOpportunitiesResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ListOpportunitiesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ListOpportunitiesRequest,
    page_size: int,
    page_token: str | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> Response[ListOpportunitiesResponse]:
    """ List Opportunities

     Search and retrieve a paginated list of opportunity leads available to the authorized seller, with
    optional filters by type, status, category, etc and ordered by the algorithm ranking model.

    Args:
        page_size (int):
        page_token (str | Unset):
        locale (str | Unset):
        body (ListOpportunitiesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListOpportunitiesResponse]
     """


    kwargs = _get_kwargs(
        body=body,
page_size=page_size,
page_token=page_token,
locale=locale,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ListOpportunitiesRequest,
    page_size: int,
    page_token: str | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> ListOpportunitiesResponse | None:
    """ List Opportunities

     Search and retrieve a paginated list of opportunity leads available to the authorized seller, with
    optional filters by type, status, category, etc and ordered by the algorithm ranking model.

    Args:
        page_size (int):
        page_token (str | Unset):
        locale (str | Unset):
        body (ListOpportunitiesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListOpportunitiesResponse
     """


    return sync_detailed(
        client=client,
body=body,
page_size=page_size,
page_token=page_token,
locale=locale,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ListOpportunitiesRequest,
    page_size: int,
    page_token: str | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> Response[ListOpportunitiesResponse]:
    """ List Opportunities

     Search and retrieve a paginated list of opportunity leads available to the authorized seller, with
    optional filters by type, status, category, etc and ordered by the algorithm ranking model.

    Args:
        page_size (int):
        page_token (str | Unset):
        locale (str | Unset):
        body (ListOpportunitiesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListOpportunitiesResponse]
     """


    kwargs = _get_kwargs(
        body=body,
page_size=page_size,
page_token=page_token,
locale=locale,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ListOpportunitiesRequest,
    page_size: int,
    page_token: str | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> ListOpportunitiesResponse | None:
    """ List Opportunities

     Search and retrieve a paginated list of opportunity leads available to the authorized seller, with
    optional filters by type, status, category, etc and ordered by the algorithm ranking model.

    Args:
        page_size (int):
        page_token (str | Unset):
        locale (str | Unset):
        body (ListOpportunitiesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListOpportunitiesResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
page_size=page_size,
page_token=page_token,
locale=locale,

    )).parsed
