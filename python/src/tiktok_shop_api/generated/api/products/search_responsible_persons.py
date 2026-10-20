from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.search_responsible_persons_request import SearchResponsiblePersonsRequest
from ...models.search_responsible_persons_response import SearchResponsiblePersonsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: SearchResponsiblePersonsRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["page_size"] = page_size

    params["page_token"] = page_token


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202501/compliance/responsible_persons/search",
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchResponsiblePersonsResponse | None:
    if response.status_code == 200:
        response_200 = SearchResponsiblePersonsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SearchResponsiblePersonsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchResponsiblePersonsRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,

) -> Response[SearchResponsiblePersonsResponse]:
    """ Search Responsible Persons

     Retrieve a list of responsible persons in the EU languages supported by TikTok Shop based on their
    ID or keywords.
    When creating a product with the [Create Product
    API](https://partner.tiktokshop.com/docv2/page/6502fc8da57708028b42b18a), pass a returned
    responsible person's `id` as an element of `responsible_person_ids`.
    Target seller: Local sellers operating in EU countries

    Args:
        page_size (int):
        page_token (str | Unset):
        body (SearchResponsiblePersonsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchResponsiblePersonsResponse]
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
    body: SearchResponsiblePersonsRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,

) -> SearchResponsiblePersonsResponse | None:
    """ Search Responsible Persons

     Retrieve a list of responsible persons in the EU languages supported by TikTok Shop based on their
    ID or keywords.
    When creating a product with the [Create Product
    API](https://partner.tiktokshop.com/docv2/page/6502fc8da57708028b42b18a), pass a returned
    responsible person's `id` as an element of `responsible_person_ids`.
    Target seller: Local sellers operating in EU countries

    Args:
        page_size (int):
        page_token (str | Unset):
        body (SearchResponsiblePersonsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchResponsiblePersonsResponse
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
    body: SearchResponsiblePersonsRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,

) -> Response[SearchResponsiblePersonsResponse]:
    """ Search Responsible Persons

     Retrieve a list of responsible persons in the EU languages supported by TikTok Shop based on their
    ID or keywords.
    When creating a product with the [Create Product
    API](https://partner.tiktokshop.com/docv2/page/6502fc8da57708028b42b18a), pass a returned
    responsible person's `id` as an element of `responsible_person_ids`.
    Target seller: Local sellers operating in EU countries

    Args:
        page_size (int):
        page_token (str | Unset):
        body (SearchResponsiblePersonsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchResponsiblePersonsResponse]
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
    body: SearchResponsiblePersonsRequest | Unset = UNSET,
    page_size: int,
    page_token: str | Unset = UNSET,

) -> SearchResponsiblePersonsResponse | None:
    """ Search Responsible Persons

     Retrieve a list of responsible persons in the EU languages supported by TikTok Shop based on their
    ID or keywords.
    When creating a product with the [Create Product
    API](https://partner.tiktokshop.com/docv2/page/6502fc8da57708028b42b18a), pass a returned
    responsible person's `id` as an element of `responsible_person_ids`.
    Target seller: Local sellers operating in EU countries

    Args:
        page_size (int):
        page_token (str | Unset):
        body (SearchResponsiblePersonsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchResponsiblePersonsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
page_size=page_size,
page_token=page_token,

    )).parsed
