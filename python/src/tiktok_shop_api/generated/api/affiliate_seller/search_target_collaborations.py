from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.search_target_collaborations_request import SearchTargetCollaborationsRequest
from ...models.search_target_collaborations_response import SearchTargetCollaborationsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: SearchTargetCollaborationsRequest,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["page_size"] = page_size

    params["page_token"] = page_token


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_seller/202508/target_collaborations/search",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchTargetCollaborationsResponse | None:
    if response.status_code == 200:
        response_200 = SearchTargetCollaborationsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SearchTargetCollaborationsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchTargetCollaborationsRequest,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> Response[SearchTargetCollaborationsResponse]:
    """ Search Target Collaborations

     This API is used by Seller to search for all existing target collaborations. Sellers can search
    based on filters such as Invitation name, Invitation ID, Product name, Product ID and Creator name.

    Args:
        page_size (int | Unset):
        page_token (str | Unset):
        body (SearchTargetCollaborationsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchTargetCollaborationsResponse]
     """


    kwargs = _get_kwargs(
        body=body,
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
    body: SearchTargetCollaborationsRequest,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> SearchTargetCollaborationsResponse | None:
    """ Search Target Collaborations

     This API is used by Seller to search for all existing target collaborations. Sellers can search
    based on filters such as Invitation name, Invitation ID, Product name, Product ID and Creator name.

    Args:
        page_size (int | Unset):
        page_token (str | Unset):
        body (SearchTargetCollaborationsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchTargetCollaborationsResponse
     """


    return sync_detailed(
        client=client,
body=body,
page_size=page_size,
page_token=page_token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchTargetCollaborationsRequest,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> Response[SearchTargetCollaborationsResponse]:
    """ Search Target Collaborations

     This API is used by Seller to search for all existing target collaborations. Sellers can search
    based on filters such as Invitation name, Invitation ID, Product name, Product ID and Creator name.

    Args:
        page_size (int | Unset):
        page_token (str | Unset):
        body (SearchTargetCollaborationsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchTargetCollaborationsResponse]
     """


    kwargs = _get_kwargs(
        body=body,
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
    body: SearchTargetCollaborationsRequest,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,

) -> SearchTargetCollaborationsResponse | None:
    """ Search Target Collaborations

     This API is used by Seller to search for all existing target collaborations. Sellers can search
    based on filters such as Invitation name, Invitation ID, Product name, Product ID and Creator name.

    Args:
        page_size (int | Unset):
        page_token (str | Unset):
        body (SearchTargetCollaborationsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchTargetCollaborationsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
page_size=page_size,
page_token=page_token,

    )).parsed
