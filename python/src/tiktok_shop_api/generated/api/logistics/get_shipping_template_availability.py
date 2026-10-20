from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_shipping_template_availability_request import GetShippingTemplateAvailabilityRequest
from ...models.get_shipping_template_availability_response import GetShippingTemplateAvailabilityResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: GetShippingTemplateAvailabilityRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/logistics/202510/seller_templates",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetShippingTemplateAvailabilityResponse | None:
    if response.status_code == 200:
        response_200 = GetShippingTemplateAvailabilityResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetShippingTemplateAvailabilityResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetShippingTemplateAvailabilityRequest | Unset = UNSET,

) -> Response[GetShippingTemplateAvailabilityResponse]:
    """ Get Shipping Template Availability

     get seller's available shipping template and return the reason  why the template is not
    available，this api is now only available for JP and UK market

    Args:
        body (GetShippingTemplateAvailabilityRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShippingTemplateAvailabilityResponse]
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
    body: GetShippingTemplateAvailabilityRequest | Unset = UNSET,

) -> GetShippingTemplateAvailabilityResponse | None:
    """ Get Shipping Template Availability

     get seller's available shipping template and return the reason  why the template is not
    available，this api is now only available for JP and UK market

    Args:
        body (GetShippingTemplateAvailabilityRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShippingTemplateAvailabilityResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetShippingTemplateAvailabilityRequest | Unset = UNSET,

) -> Response[GetShippingTemplateAvailabilityResponse]:
    """ Get Shipping Template Availability

     get seller's available shipping template and return the reason  why the template is not
    available，this api is now only available for JP and UK market

    Args:
        body (GetShippingTemplateAvailabilityRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShippingTemplateAvailabilityResponse]
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
    body: GetShippingTemplateAvailabilityRequest | Unset = UNSET,

) -> GetShippingTemplateAvailabilityResponse | None:
    """ Get Shipping Template Availability

     get seller's available shipping template and return the reason  why the template is not
    available，this api is now only available for JP and UK market

    Args:
        body (GetShippingTemplateAvailabilityRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShippingTemplateAvailabilityResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
