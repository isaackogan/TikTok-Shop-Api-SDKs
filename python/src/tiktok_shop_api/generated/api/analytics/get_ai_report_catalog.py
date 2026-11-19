from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_ai_report_catalog_response import GetAIReportCatalogResponse
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/202611/ai_report/catalog",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAIReportCatalogResponse | None:
    if response.status_code == 200:
        response_200 = GetAIReportCatalogResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAIReportCatalogResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetAIReportCatalogResponse]:
    """ Get AI Report Catalog

     Retrieve the complete configured catalog of metrics, dimensions, time buckets and row details for
    the authorized shop. The available configuration may change. Fetch the catalog when preparing a
    query instead of caching it for long periods. This is a finite configuration snapshot, not an entity
    list. Use rules for combinations, candidate search for entity values, and validation before
    querying.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAIReportCatalogResponse]
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

) -> GetAIReportCatalogResponse | None:
    """ Get AI Report Catalog

     Retrieve the complete configured catalog of metrics, dimensions, time buckets and row details for
    the authorized shop. The available configuration may change. Fetch the catalog when preparing a
    query instead of caching it for long periods. This is a finite configuration snapshot, not an entity
    list. Use rules for combinations, candidate search for entity values, and validation before
    querying.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAIReportCatalogResponse
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetAIReportCatalogResponse]:
    """ Get AI Report Catalog

     Retrieve the complete configured catalog of metrics, dimensions, time buckets and row details for
    the authorized shop. The available configuration may change. Fetch the catalog when preparing a
    query instead of caching it for long periods. This is a finite configuration snapshot, not an entity
    list. Use rules for combinations, candidate search for entity values, and validation before
    querying.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAIReportCatalogResponse]
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

) -> GetAIReportCatalogResponse | None:
    """ Get AI Report Catalog

     Retrieve the complete configured catalog of metrics, dimensions, time buckets and row details for
    the authorized shop. The available configuration may change. Fetch the catalog when preparing a
    query instead of caching it for long periods. This is a finite configuration snapshot, not an entity
    list. Use rules for combinations, candidate search for entity values, and validation before
    querying.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAIReportCatalogResponse
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
