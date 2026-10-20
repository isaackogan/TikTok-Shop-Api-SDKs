from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_authorized_category_assets_response import GetAuthorizedCategoryAssetsResponse
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/authorization/202405/category_assets",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAuthorizedCategoryAssetsResponse | None:
    if response.status_code == 200:
        response_200 = GetAuthorizedCategoryAssetsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAuthorizedCategoryAssetsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetAuthorizedCategoryAssetsResponse]:
    """ Get Authorized Category Assets

     Retrieves the list of business category assets authorized by a partner for an app.
    Partner authorization is required before an app can access the data of a partner, and this access is
    granted based on business categories. Use this API to check which business category assets are
    currently authorized for an app and obtain the corresponding category asset cipher for use as an
    input parameter in affiliate partner related APIs.
    For more information about partner authorization, refer to [Partner authorization
    guide](678e3a3978f4c20311b8b555).
    Target partner: All

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAuthorizedCategoryAssetsResponse]
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

) -> GetAuthorizedCategoryAssetsResponse | None:
    """ Get Authorized Category Assets

     Retrieves the list of business category assets authorized by a partner for an app.
    Partner authorization is required before an app can access the data of a partner, and this access is
    granted based on business categories. Use this API to check which business category assets are
    currently authorized for an app and obtain the corresponding category asset cipher for use as an
    input parameter in affiliate partner related APIs.
    For more information about partner authorization, refer to [Partner authorization
    guide](678e3a3978f4c20311b8b555).
    Target partner: All

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAuthorizedCategoryAssetsResponse
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetAuthorizedCategoryAssetsResponse]:
    """ Get Authorized Category Assets

     Retrieves the list of business category assets authorized by a partner for an app.
    Partner authorization is required before an app can access the data of a partner, and this access is
    granted based on business categories. Use this API to check which business category assets are
    currently authorized for an app and obtain the corresponding category asset cipher for use as an
    input parameter in affiliate partner related APIs.
    For more information about partner authorization, refer to [Partner authorization
    guide](678e3a3978f4c20311b8b555).
    Target partner: All

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAuthorizedCategoryAssetsResponse]
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

) -> GetAuthorizedCategoryAssetsResponse | None:
    """ Get Authorized Category Assets

     Retrieves the list of business category assets authorized by a partner for an app.
    Partner authorization is required before an app can access the data of a partner, and this access is
    granted based on business categories. Use this API to check which business category assets are
    currently authorized for an app and obtain the corresponding category asset cipher for use as an
    input parameter in affiliate partner related APIs.
    For more information about partner authorization, refer to [Partner authorization
    guide](678e3a3978f4c20311b8b555).
    Target partner: All

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAuthorizedCategoryAssetsResponse
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
