from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_global_listing_rules_response import GetGlobalListingRulesResponse
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/product/202507/global_listing_rules",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetGlobalListingRulesResponse | None:
    if response.status_code == 200:
        response_200 = GetGlobalListingRulesResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetGlobalListingRulesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetGlobalListingRulesResponse]:
    """ Get Global Listing Rules

     Retrieves the global listing rules for a local shop that belongs to a global seller. E.g. The
    supported listing methods or the inventory allocation rules. The rules differ by the markets they
    serve.
    **Note**: Applicable only for global sellers.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGlobalListingRulesResponse]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> GetGlobalListingRulesResponse | None:
    """ Get Global Listing Rules

     Retrieves the global listing rules for a local shop that belongs to a global seller. E.g. The
    supported listing methods or the inventory allocation rules. The rules differ by the markets they
    serve.
    **Note**: Applicable only for global sellers.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGlobalListingRulesResponse
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetGlobalListingRulesResponse]:
    """ Get Global Listing Rules

     Retrieves the global listing rules for a local shop that belongs to a global seller. E.g. The
    supported listing methods or the inventory allocation rules. The rules differ by the markets they
    serve.
    **Note**: Applicable only for global sellers.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGlobalListingRulesResponse]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> GetGlobalListingRulesResponse | None:
    """ Get Global Listing Rules

     Retrieves the global listing rules for a local shop that belongs to a global seller. E.g. The
    supported listing methods or the inventory allocation rules. The rules differ by the markets they
    serve.
    **Note**: Applicable only for global sellers.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGlobalListingRulesResponse
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
