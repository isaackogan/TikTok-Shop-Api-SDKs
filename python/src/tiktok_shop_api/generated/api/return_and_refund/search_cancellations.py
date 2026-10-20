from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.search_cancellations_request import SearchCancellationsRequest
from ...models.search_cancellations_response import SearchCancellationsResponse
from ...models.search_cancellations_sort_field import SearchCancellationsSortField
from ...models.search_cancellations_sort_order import SearchCancellationsSortOrder
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: SearchCancellationsRequest | Unset = UNSET,
    sort_field: SearchCancellationsSortField | Unset = UNSET,
    sort_order: SearchCancellationsSortOrder | Unset = UNSET,
    page_size: str | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    json_sort_field: str | Unset = UNSET
    if not isinstance(sort_field, Unset):
        json_sort_field = sort_field.value

    params["sort_field"] = json_sort_field

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sort_order"] = json_sort_order

    params["page_size"] = page_size

    params["page_token"] = page_token


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/return_refund/202602/cancellations/search",
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchCancellationsResponse | None:
    if response.status_code == 200:
        response_200 = SearchCancellationsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SearchCancellationsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchCancellationsRequest | Unset = UNSET,
    sort_field: SearchCancellationsSortField | Unset = UNSET,
    sort_order: SearchCancellationsSortOrder | Unset = UNSET,
    page_size: str | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> Response[SearchCancellationsResponse]:
    """ Search Cancellations

     Use this API to search and retrieve one or more order cancellations.

    Args:
        sort_field (SearchCancellationsSortField | Unset):
        sort_order (SearchCancellationsSortOrder | Unset):
        page_size (str | Unset):
        page_token (str | Unset):
        body (SearchCancellationsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchCancellationsResponse]
     """


    kwargs = _get_kwargs(
        body=body,
sort_field=sort_field,
sort_order=sort_order,
page_size=page_size,
page_token=page_token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SearchCancellationsRequest | Unset = UNSET,
    sort_field: SearchCancellationsSortField | Unset = UNSET,
    sort_order: SearchCancellationsSortOrder | Unset = UNSET,
    page_size: str | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> SearchCancellationsResponse | None:
    """ Search Cancellations

     Use this API to search and retrieve one or more order cancellations.

    Args:
        sort_field (SearchCancellationsSortField | Unset):
        sort_order (SearchCancellationsSortOrder | Unset):
        page_size (str | Unset):
        page_token (str | Unset):
        body (SearchCancellationsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchCancellationsResponse
     """


    return sync_detailed(
        client=client,
body=body,
sort_field=sort_field,
sort_order=sort_order,
page_size=page_size,
page_token=page_token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchCancellationsRequest | Unset = UNSET,
    sort_field: SearchCancellationsSortField | Unset = UNSET,
    sort_order: SearchCancellationsSortOrder | Unset = UNSET,
    page_size: str | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> Response[SearchCancellationsResponse]:
    """ Search Cancellations

     Use this API to search and retrieve one or more order cancellations.

    Args:
        sort_field (SearchCancellationsSortField | Unset):
        sort_order (SearchCancellationsSortOrder | Unset):
        page_size (str | Unset):
        page_token (str | Unset):
        body (SearchCancellationsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchCancellationsResponse]
     """


    kwargs = _get_kwargs(
        body=body,
sort_field=sort_field,
sort_order=sort_order,
page_size=page_size,
page_token=page_token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchCancellationsRequest | Unset = UNSET,
    sort_field: SearchCancellationsSortField | Unset = UNSET,
    sort_order: SearchCancellationsSortOrder | Unset = UNSET,
    page_size: str | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> SearchCancellationsResponse | None:
    """ Search Cancellations

     Use this API to search and retrieve one or more order cancellations.

    Args:
        sort_field (SearchCancellationsSortField | Unset):
        sort_order (SearchCancellationsSortOrder | Unset):
        page_size (str | Unset):
        page_token (str | Unset):
        body (SearchCancellationsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchCancellationsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
sort_field=sort_field,
sort_order=sort_order,
page_size=page_size,
page_token=page_token,

    )).parsed
