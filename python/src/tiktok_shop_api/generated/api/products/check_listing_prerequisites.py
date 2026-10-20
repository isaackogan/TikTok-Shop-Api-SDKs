from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.check_listing_prerequisites_response import CheckListingPrerequisitesResponse
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/product/202312/prerequisites",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CheckListingPrerequisitesResponse | None:
    if response.status_code == 200:
        response_200 = CheckListingPrerequisitesResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CheckListingPrerequisitesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[CheckListingPrerequisitesResponse]:
    """ Check Listing Prerequisites

     Check if a TikTok shop is ready to list products.
    Each shop needs to satisfy a series of TikTok Shop requirements before you can start listing
    products. Before you proceed to list products, use this API to check if your shop has satisfied all
    requirements.
    **Tip**: We recommend that you run this check before any bulk updates to avoid listing issues. For
    example, sellers may change the delivery option to "Shipped by seller" but fail to add a shipping
    template, thus blocking the shop from listing products. In this case, the API would return
    `is_failed=true` for the `SHIPPING_TEMPLATE` check item and you can prompt the seller to fix the
    problem.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckListingPrerequisitesResponse]
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

) -> CheckListingPrerequisitesResponse | None:
    """ Check Listing Prerequisites

     Check if a TikTok shop is ready to list products.
    Each shop needs to satisfy a series of TikTok Shop requirements before you can start listing
    products. Before you proceed to list products, use this API to check if your shop has satisfied all
    requirements.
    **Tip**: We recommend that you run this check before any bulk updates to avoid listing issues. For
    example, sellers may change the delivery option to "Shipped by seller" but fail to add a shipping
    template, thus blocking the shop from listing products. In this case, the API would return
    `is_failed=true` for the `SHIPPING_TEMPLATE` check item and you can prompt the seller to fix the
    problem.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckListingPrerequisitesResponse
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[CheckListingPrerequisitesResponse]:
    """ Check Listing Prerequisites

     Check if a TikTok shop is ready to list products.
    Each shop needs to satisfy a series of TikTok Shop requirements before you can start listing
    products. Before you proceed to list products, use this API to check if your shop has satisfied all
    requirements.
    **Tip**: We recommend that you run this check before any bulk updates to avoid listing issues. For
    example, sellers may change the delivery option to "Shipped by seller" but fail to add a shipping
    template, thus blocking the shop from listing products. In this case, the API would return
    `is_failed=true` for the `SHIPPING_TEMPLATE` check item and you can prompt the seller to fix the
    problem.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckListingPrerequisitesResponse]
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

) -> CheckListingPrerequisitesResponse | None:
    """ Check Listing Prerequisites

     Check if a TikTok shop is ready to list products.
    Each shop needs to satisfy a series of TikTok Shop requirements before you can start listing
    products. Before you proceed to list products, use this API to check if your shop has satisfied all
    requirements.
    **Tip**: We recommend that you run this check before any bulk updates to avoid listing issues. For
    example, sellers may change the delivery option to "Shipped by seller" but fail to add a shipping
    template, thus blocking the shop from listing products. In this case, the API would return
    `is_failed=true` for the `SHIPPING_TEMPLATE` check item and you can prompt the seller to fix the
    problem.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckListingPrerequisitesResponse
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
