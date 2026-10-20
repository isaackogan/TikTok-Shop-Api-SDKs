from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.search_open_collaborations_request import SearchOpenCollaborationsRequest
from ...models.search_open_collaborations_response import SearchOpenCollaborationsResponse
from ...models.search_open_collaborations_sort_order import SearchOpenCollaborationsSortOrder
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: SearchOpenCollaborationsRequest | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int,
    sort_order: SearchOpenCollaborationsSortOrder | Unset = UNSET,
    sort_field: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["page_token"] = page_token

    params["page_size"] = page_size

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sort_order"] = json_sort_order

    params["sort_field"] = sort_field


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_seller/202412/open_collaborations/search",
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchOpenCollaborationsResponse | None:
    if response.status_code == 200:
        response_200 = SearchOpenCollaborationsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SearchOpenCollaborationsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchOpenCollaborationsRequest | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int,
    sort_order: SearchOpenCollaborationsSortOrder | Unset = UNSET,
    sort_field: str | Unset = UNSET,

) -> Response[SearchOpenCollaborationsResponse]:
    """ Search Open Collaborations

     Search the merchant's open collaborations. The response includes product details, current commission
    information, the number of creators who added each product to their showcase, and the number of
    creators who posted LIVE or video content.

    Args:
        page_token (str | Unset):
        page_size (int):
        sort_order (SearchOpenCollaborationsSortOrder | Unset):
        sort_field (str | Unset):
        body (SearchOpenCollaborationsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchOpenCollaborationsResponse]
     """


    kwargs = _get_kwargs(
        body=body,
page_token=page_token,
page_size=page_size,
sort_order=sort_order,
sort_field=sort_field,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SearchOpenCollaborationsRequest | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int,
    sort_order: SearchOpenCollaborationsSortOrder | Unset = UNSET,
    sort_field: str | Unset = UNSET,

) -> SearchOpenCollaborationsResponse | None:
    """ Search Open Collaborations

     Search the merchant's open collaborations. The response includes product details, current commission
    information, the number of creators who added each product to their showcase, and the number of
    creators who posted LIVE or video content.

    Args:
        page_token (str | Unset):
        page_size (int):
        sort_order (SearchOpenCollaborationsSortOrder | Unset):
        sort_field (str | Unset):
        body (SearchOpenCollaborationsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchOpenCollaborationsResponse
     """


    return sync_detailed(
        client=client,
body=body,
page_token=page_token,
page_size=page_size,
sort_order=sort_order,
sort_field=sort_field,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchOpenCollaborationsRequest | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int,
    sort_order: SearchOpenCollaborationsSortOrder | Unset = UNSET,
    sort_field: str | Unset = UNSET,

) -> Response[SearchOpenCollaborationsResponse]:
    """ Search Open Collaborations

     Search the merchant's open collaborations. The response includes product details, current commission
    information, the number of creators who added each product to their showcase, and the number of
    creators who posted LIVE or video content.

    Args:
        page_token (str | Unset):
        page_size (int):
        sort_order (SearchOpenCollaborationsSortOrder | Unset):
        sort_field (str | Unset):
        body (SearchOpenCollaborationsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchOpenCollaborationsResponse]
     """


    kwargs = _get_kwargs(
        body=body,
page_token=page_token,
page_size=page_size,
sort_order=sort_order,
sort_field=sort_field,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchOpenCollaborationsRequest | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int,
    sort_order: SearchOpenCollaborationsSortOrder | Unset = UNSET,
    sort_field: str | Unset = UNSET,

) -> SearchOpenCollaborationsResponse | None:
    """ Search Open Collaborations

     Search the merchant's open collaborations. The response includes product details, current commission
    information, the number of creators who added each product to their showcase, and the number of
    creators who posted LIVE or video content.

    Args:
        page_token (str | Unset):
        page_size (int):
        sort_order (SearchOpenCollaborationsSortOrder | Unset):
        sort_field (str | Unset):
        body (SearchOpenCollaborationsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchOpenCollaborationsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
page_token=page_token,
page_size=page_size,
sort_order=sort_order,
sort_field=sort_field,

    )).parsed
