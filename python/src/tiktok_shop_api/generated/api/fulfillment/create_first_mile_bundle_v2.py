from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_first_mile_bundle_v2_request import CreateFirstMileBundleV2Request
from ...models.create_first_mile_bundle_v2_response import CreateFirstMileBundleV2Response
from typing import cast



def _get_kwargs(
    *,
    body: CreateFirstMileBundleV2Request,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fulfillment/202510/first_mile_bundle",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateFirstMileBundleV2Response | None:
    if response.status_code == 200:
        response_200 = CreateFirstMileBundleV2Response.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateFirstMileBundleV2Response]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateFirstMileBundleV2Request,

) -> Response[CreateFirstMileBundleV2Response]:
    """ Create First Mile Bundle(V2)

     If you send multiple packages to TikTok Shop warehouse in a single first-mile bundle, you can use
    the API to create a first-mile bundle on TikTok Shop and get the bundle ID.

    Args:
        body (CreateFirstMileBundleV2Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateFirstMileBundleV2Response]
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
    body: CreateFirstMileBundleV2Request,

) -> CreateFirstMileBundleV2Response | None:
    """ Create First Mile Bundle(V2)

     If you send multiple packages to TikTok Shop warehouse in a single first-mile bundle, you can use
    the API to create a first-mile bundle on TikTok Shop and get the bundle ID.

    Args:
        body (CreateFirstMileBundleV2Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateFirstMileBundleV2Response
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateFirstMileBundleV2Request,

) -> Response[CreateFirstMileBundleV2Response]:
    """ Create First Mile Bundle(V2)

     If you send multiple packages to TikTok Shop warehouse in a single first-mile bundle, you can use
    the API to create a first-mile bundle on TikTok Shop and get the bundle ID.

    Args:
        body (CreateFirstMileBundleV2Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateFirstMileBundleV2Response]
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
    body: CreateFirstMileBundleV2Request,

) -> CreateFirstMileBundleV2Response | None:
    """ Create First Mile Bundle(V2)

     If you send multiple packages to TikTok Shop warehouse in a single first-mile bundle, you can use
    the API to create a first-mile bundle on TikTok Shop and get the bundle ID.

    Args:
        body (CreateFirstMileBundleV2Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateFirstMileBundleV2Response
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
