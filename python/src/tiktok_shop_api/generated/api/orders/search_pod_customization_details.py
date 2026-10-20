from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.search_pod_customization_details_request import SearchPODCustomizationDetailsRequest
from ...models.search_pod_customization_details_response import SearchPODCustomizationDetailsResponse
from typing import cast



def _get_kwargs(
    *,
    body: SearchPODCustomizationDetailsRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/order/202606/pod_details/search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchPODCustomizationDetailsResponse | None:
    if response.status_code == 200:
        response_200 = SearchPODCustomizationDetailsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SearchPODCustomizationDetailsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchPODCustomizationDetailsRequest,

) -> Response[SearchPODCustomizationDetailsResponse]:
    """ Search POD Customization Details

     Search for POD customization details for the specified order lines.

    Args:
        body (SearchPODCustomizationDetailsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchPODCustomizationDetailsResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SearchPODCustomizationDetailsRequest,

) -> SearchPODCustomizationDetailsResponse | None:
    """ Search POD Customization Details

     Search for POD customization details for the specified order lines.

    Args:
        body (SearchPODCustomizationDetailsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchPODCustomizationDetailsResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchPODCustomizationDetailsRequest,

) -> Response[SearchPODCustomizationDetailsResponse]:
    """ Search POD Customization Details

     Search for POD customization details for the specified order lines.

    Args:
        body (SearchPODCustomizationDetailsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchPODCustomizationDetailsResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchPODCustomizationDetailsRequest,

) -> SearchPODCustomizationDetailsResponse | None:
    """ Search POD Customization Details

     Search for POD customization details for the specified order lines.

    Args:
        body (SearchPODCustomizationDetailsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchPODCustomizationDetailsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
