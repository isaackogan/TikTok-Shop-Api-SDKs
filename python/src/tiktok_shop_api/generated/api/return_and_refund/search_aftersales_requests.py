from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.search_aftersales_requests_request import SearchAftersalesRequestsRequest
from ...models.search_aftersales_requests_response import SearchAftersalesRequestsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: SearchAftersalesRequestsRequest | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["locale"] = locale


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/return_refund/202603/aftersales/search",
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchAftersalesRequestsResponse | None:
    if response.status_code == 200:
        response_200 = SearchAftersalesRequestsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SearchAftersalesRequestsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchAftersalesRequestsRequest | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> Response[SearchAftersalesRequestsResponse]:
    """ Search Aftersales Requests

     Searches aftersales requests for the authorized shop. You can filter by aftersales request, buyer,
    or main order IDs, aftersales request status, return type, and creation or update time. Use
    `whitelisted_data_fields` to include line items, SKU return requests, or return merchandise
    authorizations in each result.

    Args:
        locale (str | Unset):
        body (SearchAftersalesRequestsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchAftersalesRequestsResponse]
     """


    kwargs = _get_kwargs(
        body=body,
locale=locale,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SearchAftersalesRequestsRequest | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> SearchAftersalesRequestsResponse | None:
    """ Search Aftersales Requests

     Searches aftersales requests for the authorized shop. You can filter by aftersales request, buyer,
    or main order IDs, aftersales request status, return type, and creation or update time. Use
    `whitelisted_data_fields` to include line items, SKU return requests, or return merchandise
    authorizations in each result.

    Args:
        locale (str | Unset):
        body (SearchAftersalesRequestsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchAftersalesRequestsResponse
     """


    return sync_detailed(
        client=client,
body=body,
locale=locale,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchAftersalesRequestsRequest | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> Response[SearchAftersalesRequestsResponse]:
    """ Search Aftersales Requests

     Searches aftersales requests for the authorized shop. You can filter by aftersales request, buyer,
    or main order IDs, aftersales request status, return type, and creation or update time. Use
    `whitelisted_data_fields` to include line items, SKU return requests, or return merchandise
    authorizations in each result.

    Args:
        locale (str | Unset):
        body (SearchAftersalesRequestsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchAftersalesRequestsResponse]
     """


    kwargs = _get_kwargs(
        body=body,
locale=locale,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchAftersalesRequestsRequest | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> SearchAftersalesRequestsResponse | None:
    """ Search Aftersales Requests

     Searches aftersales requests for the authorized shop. You can filter by aftersales request, buyer,
    or main order IDs, aftersales request status, return type, and creation or update time. Use
    `whitelisted_data_fields` to include line items, SKU return requests, or return merchandise
    authorizations in each result.

    Args:
        locale (str | Unset):
        body (SearchAftersalesRequestsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchAftersalesRequestsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
locale=locale,

    )).parsed
