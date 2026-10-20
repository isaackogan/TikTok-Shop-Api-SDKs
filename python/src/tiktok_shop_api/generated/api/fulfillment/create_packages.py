from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_packages_request import CreatePackagesRequest
from ...models.create_packages_response import CreatePackagesResponse
from typing import cast



def _get_kwargs(
    *,
    body: CreatePackagesRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fulfillment/202512/packages",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreatePackagesResponse | None:
    if response.status_code == 200:
        response_200 = CreatePackagesResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreatePackagesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreatePackagesRequest,

) -> Response[CreatePackagesResponse]:
    """ Create Packages

     Use this API to ship orders (purchase labels). This API is available in the US, UK, EMEA, and JP
    regions. The shipping fee and delivery time is an estimate only and is based on the package
    dimensions and weight you provided.

    Args:
        body (CreatePackagesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatePackagesResponse]
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
    body: CreatePackagesRequest,

) -> CreatePackagesResponse | None:
    """ Create Packages

     Use this API to ship orders (purchase labels). This API is available in the US, UK, EMEA, and JP
    regions. The shipping fee and delivery time is an estimate only and is based on the package
    dimensions and weight you provided.

    Args:
        body (CreatePackagesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatePackagesResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreatePackagesRequest,

) -> Response[CreatePackagesResponse]:
    """ Create Packages

     Use this API to ship orders (purchase labels). This API is available in the US, UK, EMEA, and JP
    regions. The shipping fee and delivery time is an estimate only and is based on the package
    dimensions and weight you provided.

    Args:
        body (CreatePackagesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatePackagesResponse]
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
    body: CreatePackagesRequest,

) -> CreatePackagesResponse | None:
    """ Create Packages

     Use this API to ship orders (purchase labels). This API is available in the US, UK, EMEA, and JP
    regions. The shipping fee and delivery time is an estimate only and is based on the package
    dimensions and weight you provided.

    Args:
        body (CreatePackagesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatePackagesResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
