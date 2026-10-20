from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.search_creator_target_collaborations_request import SearchCreatorTargetCollaborationsRequest
from ...models.search_creator_target_collaborations_response import SearchCreatorTargetCollaborationsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: SearchCreatorTargetCollaborationsRequest,
    page_token: str | Unset = UNSET,
    page_size: int,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["page_token"] = page_token

    params["page_size"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_creator/202405/target_collaborations/search",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchCreatorTargetCollaborationsResponse | None:
    if response.status_code == 200:
        response_200 = SearchCreatorTargetCollaborationsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SearchCreatorTargetCollaborationsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchCreatorTargetCollaborationsRequest,
    page_token: str | Unset = UNSET,
    page_size: int,

) -> Response[SearchCreatorTargetCollaborationsResponse]:
    """ Search Creator Target Collaborations

     Searches for the authenticated creator's target collaborations and the products within them for the
    TikTok Shop specified by `shop_id`.

    Args:
        page_token (str | Unset):
        page_size (int):
        body (SearchCreatorTargetCollaborationsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchCreatorTargetCollaborationsResponse]
     """


    kwargs = _get_kwargs(
        body=body,
page_token=page_token,
page_size=page_size,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SearchCreatorTargetCollaborationsRequest,
    page_token: str | Unset = UNSET,
    page_size: int,

) -> SearchCreatorTargetCollaborationsResponse | None:
    """ Search Creator Target Collaborations

     Searches for the authenticated creator's target collaborations and the products within them for the
    TikTok Shop specified by `shop_id`.

    Args:
        page_token (str | Unset):
        page_size (int):
        body (SearchCreatorTargetCollaborationsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchCreatorTargetCollaborationsResponse
     """


    return sync_detailed(
        client=client,
body=body,
page_token=page_token,
page_size=page_size,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchCreatorTargetCollaborationsRequest,
    page_token: str | Unset = UNSET,
    page_size: int,

) -> Response[SearchCreatorTargetCollaborationsResponse]:
    """ Search Creator Target Collaborations

     Searches for the authenticated creator's target collaborations and the products within them for the
    TikTok Shop specified by `shop_id`.

    Args:
        page_token (str | Unset):
        page_size (int):
        body (SearchCreatorTargetCollaborationsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchCreatorTargetCollaborationsResponse]
     """


    kwargs = _get_kwargs(
        body=body,
page_token=page_token,
page_size=page_size,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchCreatorTargetCollaborationsRequest,
    page_token: str | Unset = UNSET,
    page_size: int,

) -> SearchCreatorTargetCollaborationsResponse | None:
    """ Search Creator Target Collaborations

     Searches for the authenticated creator's target collaborations and the products within them for the
    TikTok Shop specified by `shop_id`.

    Args:
        page_token (str | Unset):
        page_size (int):
        body (SearchCreatorTargetCollaborationsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchCreatorTargetCollaborationsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
page_token=page_token,
page_size=page_size,

    )).parsed
