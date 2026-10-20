from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_creator_sample_application_detail_request import GetCreatorSampleApplicationDetailRequest
from ...models.get_creator_sample_application_detail_response import GetCreatorSampleApplicationDetailResponse
from typing import cast



def _get_kwargs(
    *,
    body: GetCreatorSampleApplicationDetailRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_creator/202412/sample_applications/single_query",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetCreatorSampleApplicationDetailResponse | None:
    if response.status_code == 200:
        response_200 = GetCreatorSampleApplicationDetailResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetCreatorSampleApplicationDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetCreatorSampleApplicationDetailRequest,

) -> Response[GetCreatorSampleApplicationDetailResponse]:
    """ Get Creator Sample Application Detail

     Get the sample detail of specified sample application.

    Args:
        body (GetCreatorSampleApplicationDetailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCreatorSampleApplicationDetailResponse]
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
    body: GetCreatorSampleApplicationDetailRequest,

) -> GetCreatorSampleApplicationDetailResponse | None:
    """ Get Creator Sample Application Detail

     Get the sample detail of specified sample application.

    Args:
        body (GetCreatorSampleApplicationDetailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCreatorSampleApplicationDetailResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetCreatorSampleApplicationDetailRequest,

) -> Response[GetCreatorSampleApplicationDetailResponse]:
    """ Get Creator Sample Application Detail

     Get the sample detail of specified sample application.

    Args:
        body (GetCreatorSampleApplicationDetailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCreatorSampleApplicationDetailResponse]
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
    body: GetCreatorSampleApplicationDetailRequest,

) -> GetCreatorSampleApplicationDetailResponse | None:
    """ Get Creator Sample Application Detail

     Get the sample detail of specified sample application.

    Args:
        body (GetCreatorSampleApplicationDetailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCreatorSampleApplicationDetailResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
