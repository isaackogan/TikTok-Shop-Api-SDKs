from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.generate_general_sharing_links_request import GenerateGeneralSharingLinksRequest
from ...models.generate_general_sharing_links_response import GenerateGeneralSharingLinksResponse
from typing import cast



def _get_kwargs(
    *,
    body: GenerateGeneralSharingLinksRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_creator/202505/affiliate_sharing_links/general_publishers/generate_batch",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GenerateGeneralSharingLinksResponse | None:
    if response.status_code == 200:
        response_200 = GenerateGeneralSharingLinksResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GenerateGeneralSharingLinksResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GenerateGeneralSharingLinksRequest,

) -> Response[GenerateGeneralSharingLinksResponse]:
    """ Generate General Sharing Links

     You can use this API to generate material sharing links for your publishers. After that, you can
    encapsulate the sharing link with additional information like publisher ID. Right now, the material
    type must be `PRODUCT`.
    Please ensure that the material is included in the campaign by using [Generate Multi Affiliate
    Partner Campaign Product Links].

    Args:
        body (GenerateGeneralSharingLinksRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenerateGeneralSharingLinksResponse]
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
    body: GenerateGeneralSharingLinksRequest,

) -> GenerateGeneralSharingLinksResponse | None:
    """ Generate General Sharing Links

     You can use this API to generate material sharing links for your publishers. After that, you can
    encapsulate the sharing link with additional information like publisher ID. Right now, the material
    type must be `PRODUCT`.
    Please ensure that the material is included in the campaign by using [Generate Multi Affiliate
    Partner Campaign Product Links].

    Args:
        body (GenerateGeneralSharingLinksRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenerateGeneralSharingLinksResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GenerateGeneralSharingLinksRequest,

) -> Response[GenerateGeneralSharingLinksResponse]:
    """ Generate General Sharing Links

     You can use this API to generate material sharing links for your publishers. After that, you can
    encapsulate the sharing link with additional information like publisher ID. Right now, the material
    type must be `PRODUCT`.
    Please ensure that the material is included in the campaign by using [Generate Multi Affiliate
    Partner Campaign Product Links].

    Args:
        body (GenerateGeneralSharingLinksRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenerateGeneralSharingLinksResponse]
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
    body: GenerateGeneralSharingLinksRequest,

) -> GenerateGeneralSharingLinksResponse | None:
    """ Generate General Sharing Links

     You can use this API to generate material sharing links for your publishers. After that, you can
    encapsulate the sharing link with additional information like publisher ID. Right now, the material
    type must be `PRODUCT`.
    Please ensure that the material is included in the campaign by using [Generate Multi Affiliate
    Partner Campaign Product Links].

    Args:
        body (GenerateGeneralSharingLinksRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenerateGeneralSharingLinksResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
