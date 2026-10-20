from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.search_package_request import SearchPackageRequest
from ...models.search_package_response import SearchPackageResponse
from ...models.search_package_sort_field import SearchPackageSortField
from ...models.search_package_sort_order import SearchPackageSortOrder
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: SearchPackageRequest | Unset = UNSET,
    page_size: int,
    sort_field: SearchPackageSortField | Unset = UNSET,
    sort_order: SearchPackageSortOrder | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["page_size"] = page_size

    json_sort_field: str | Unset = UNSET
    if not isinstance(sort_field, Unset):
        json_sort_field = sort_field.value

    params["sort_field"] = json_sort_field

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sort_order"] = json_sort_order

    params["page_token"] = page_token


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fulfillment/202309/packages/search",
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchPackageResponse | None:
    if response.status_code == 200:
        response_200 = SearchPackageResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SearchPackageResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchPackageRequest | Unset = UNSET,
    page_size: int,
    sort_field: SearchPackageSortField | Unset = UNSET,
    sort_order: SearchPackageSortOrder | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> Response[SearchPackageResponse]:
    """ Search Package

     Retrieve packages, optionally filtered by creation time, update time, or package status.

    Args:
        page_size (int):
        sort_field (SearchPackageSortField | Unset):
        sort_order (SearchPackageSortOrder | Unset):
        page_token (str | Unset):
        body (SearchPackageRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchPackageResponse]
     """


    kwargs = _get_kwargs(
        body=body,
page_size=page_size,
sort_field=sort_field,
sort_order=sort_order,
page_token=page_token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SearchPackageRequest | Unset = UNSET,
    page_size: int,
    sort_field: SearchPackageSortField | Unset = UNSET,
    sort_order: SearchPackageSortOrder | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> SearchPackageResponse | None:
    """ Search Package

     Retrieve packages, optionally filtered by creation time, update time, or package status.

    Args:
        page_size (int):
        sort_field (SearchPackageSortField | Unset):
        sort_order (SearchPackageSortOrder | Unset):
        page_token (str | Unset):
        body (SearchPackageRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchPackageResponse
     """


    return sync_detailed(
        client=client,
body=body,
page_size=page_size,
sort_field=sort_field,
sort_order=sort_order,
page_token=page_token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchPackageRequest | Unset = UNSET,
    page_size: int,
    sort_field: SearchPackageSortField | Unset = UNSET,
    sort_order: SearchPackageSortOrder | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> Response[SearchPackageResponse]:
    """ Search Package

     Retrieve packages, optionally filtered by creation time, update time, or package status.

    Args:
        page_size (int):
        sort_field (SearchPackageSortField | Unset):
        sort_order (SearchPackageSortOrder | Unset):
        page_token (str | Unset):
        body (SearchPackageRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchPackageResponse]
     """


    kwargs = _get_kwargs(
        body=body,
page_size=page_size,
sort_field=sort_field,
sort_order=sort_order,
page_token=page_token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchPackageRequest | Unset = UNSET,
    page_size: int,
    sort_field: SearchPackageSortField | Unset = UNSET,
    sort_order: SearchPackageSortOrder | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> SearchPackageResponse | None:
    """ Search Package

     Retrieve packages, optionally filtered by creation time, update time, or package status.

    Args:
        page_size (int):
        sort_field (SearchPackageSortField | Unset):
        sort_order (SearchPackageSortOrder | Unset):
        page_token (str | Unset):
        body (SearchPackageRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchPackageResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
page_size=page_size,
sort_field=sort_field,
sort_order=sort_order,
page_token=page_token,

    )).parsed
