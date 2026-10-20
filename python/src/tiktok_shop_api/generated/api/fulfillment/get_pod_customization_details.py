from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_pod_customization_details_request import GetPODCustomizationDetailsRequest
from ...models.get_pod_customization_details_response import GetPODCustomizationDetailsResponse
from typing import cast



def _get_kwargs(
    *,
    body: GetPODCustomizationDetailsRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fulfillment/202606/pod_details/get",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetPODCustomizationDetailsResponse | None:
    if response.status_code == 200:
        response_200 = GetPODCustomizationDetailsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetPODCustomizationDetailsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetPODCustomizationDetailsRequest,

) -> Response[GetPODCustomizationDetailsResponse]:
    """ Get POD Customization Details

     Retrieves the POD customization details for specified order lines in a TikTok Shop order.

    Args:
        body (GetPODCustomizationDetailsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPODCustomizationDetailsResponse]
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
    body: GetPODCustomizationDetailsRequest,

) -> GetPODCustomizationDetailsResponse | None:
    """ Get POD Customization Details

     Retrieves the POD customization details for specified order lines in a TikTok Shop order.

    Args:
        body (GetPODCustomizationDetailsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPODCustomizationDetailsResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetPODCustomizationDetailsRequest,

) -> Response[GetPODCustomizationDetailsResponse]:
    """ Get POD Customization Details

     Retrieves the POD customization details for specified order lines in a TikTok Shop order.

    Args:
        body (GetPODCustomizationDetailsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPODCustomizationDetailsResponse]
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
    body: GetPODCustomizationDetailsRequest,

) -> GetPODCustomizationDetailsResponse | None:
    """ Get POD Customization Details

     Retrieves the POD customization details for specified order lines in a TikTok Shop order.

    Args:
        body (GetPODCustomizationDetailsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPODCustomizationDetailsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
