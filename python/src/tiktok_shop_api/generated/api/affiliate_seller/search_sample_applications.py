from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.search_sample_applications_request import SearchSampleApplicationsRequest
from ...models.search_sample_applications_response import SearchSampleApplicationsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: SearchSampleApplicationsRequest | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["page_token"] = page_token

    params["page_size"] = page_size


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_seller/202508/sample_applications/search",
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchSampleApplicationsResponse | None:
    if response.status_code == 200:
        response_200 = SearchSampleApplicationsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SearchSampleApplicationsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchSampleApplicationsRequest | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,

) -> Response[SearchSampleApplicationsResponse]:
    """ Search Sample Applications

     This API is provided for sellers to query sample applications based on various criteria such as
    products, creators, or application statuses. By using this API, sellers can retrieve detailed
    information about sample application records, including the creator's information and the specifics
    of each application.

    Args:
        page_token (str | Unset):
        page_size (int | Unset):
        body (SearchSampleApplicationsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchSampleApplicationsResponse]
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
    body: SearchSampleApplicationsRequest | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,

) -> SearchSampleApplicationsResponse | None:
    """ Search Sample Applications

     This API is provided for sellers to query sample applications based on various criteria such as
    products, creators, or application statuses. By using this API, sellers can retrieve detailed
    information about sample application records, including the creator's information and the specifics
    of each application.

    Args:
        page_token (str | Unset):
        page_size (int | Unset):
        body (SearchSampleApplicationsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchSampleApplicationsResponse
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
    body: SearchSampleApplicationsRequest | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,

) -> Response[SearchSampleApplicationsResponse]:
    """ Search Sample Applications

     This API is provided for sellers to query sample applications based on various criteria such as
    products, creators, or application statuses. By using this API, sellers can retrieve detailed
    information about sample application records, including the creator's information and the specifics
    of each application.

    Args:
        page_token (str | Unset):
        page_size (int | Unset):
        body (SearchSampleApplicationsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchSampleApplicationsResponse]
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
    body: SearchSampleApplicationsRequest | Unset = UNSET,
    page_token: str | Unset = UNSET,
    page_size: int | Unset = UNSET,

) -> SearchSampleApplicationsResponse | None:
    """ Search Sample Applications

     This API is provided for sellers to query sample applications based on various criteria such as
    products, creators, or application statuses. By using this API, sellers can retrieve detailed
    information about sample application records, including the creator's information and the specifics
    of each application.

    Args:
        page_token (str | Unset):
        page_size (int | Unset):
        body (SearchSampleApplicationsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchSampleApplicationsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
page_token=page_token,
page_size=page_size,

    )).parsed
