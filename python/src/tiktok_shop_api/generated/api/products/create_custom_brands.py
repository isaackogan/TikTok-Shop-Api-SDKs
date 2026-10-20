from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_custom_brands_request import CreateCustomBrandsRequest
from ...models.create_custom_brands_response import CreateCustomBrandsResponse
from typing import cast



def _get_kwargs(
    *,
    body: CreateCustomBrandsRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202309/brands",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateCustomBrandsResponse | None:
    if response.status_code == 200:
        response_200 = CreateCustomBrandsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateCustomBrandsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateCustomBrandsRequest,

) -> Response[CreateCustomBrandsResponse]:
    """ Create Custom Brands

     Create custom brands for your own use across all markets.
    Authorization is not required when creating a brand. You can create the brand first and obtain brand
    authorization later through the Qualification Center in TikTok Shop Seller Center.
    **Note**: You can create up to 50 brands per day, with a total limit of 1,000 brands.

    Args:
        body (CreateCustomBrandsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateCustomBrandsResponse]
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
    body: CreateCustomBrandsRequest,

) -> CreateCustomBrandsResponse | None:
    """ Create Custom Brands

     Create custom brands for your own use across all markets.
    Authorization is not required when creating a brand. You can create the brand first and obtain brand
    authorization later through the Qualification Center in TikTok Shop Seller Center.
    **Note**: You can create up to 50 brands per day, with a total limit of 1,000 brands.

    Args:
        body (CreateCustomBrandsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateCustomBrandsResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateCustomBrandsRequest,

) -> Response[CreateCustomBrandsResponse]:
    """ Create Custom Brands

     Create custom brands for your own use across all markets.
    Authorization is not required when creating a brand. You can create the brand first and obtain brand
    authorization later through the Qualification Center in TikTok Shop Seller Center.
    **Note**: You can create up to 50 brands per day, with a total limit of 1,000 brands.

    Args:
        body (CreateCustomBrandsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateCustomBrandsResponse]
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
    body: CreateCustomBrandsRequest,

) -> CreateCustomBrandsResponse | None:
    """ Create Custom Brands

     Create custom brands for your own use across all markets.
    Authorization is not required when creating a brand. You can create the brand first and obtain brand
    authorization later through the Qualification Center in TikTok Shop Seller Center.
    **Note**: You can create up to 50 brands per day, with a total limit of 1,000 brands.

    Args:
        body (CreateCustomBrandsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateCustomBrandsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
