from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.search_return_merchandise_authorizations_request import SearchReturnMerchandiseAuthorizationsRequest
from ...models.search_return_merchandise_authorizations_response import SearchReturnMerchandiseAuthorizationsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: SearchReturnMerchandiseAuthorizationsRequest | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["locale"] = locale


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/return_refund/202604/rma/search",
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchReturnMerchandiseAuthorizationsResponse | None:
    if response.status_code == 200:
        response_200 = SearchReturnMerchandiseAuthorizationsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SearchReturnMerchandiseAuthorizationsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchReturnMerchandiseAuthorizationsRequest | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> Response[SearchReturnMerchandiseAuthorizationsResponse]:
    """ Search Return Merchandise Authorizations

     Searches return merchandise authorizations (RMAs) for the authorized shop. You can filter by
    identifiers, RMA status, and creation or update time. Use `whitelisted_data_fields` to include line
    items or SKU return requests for each RMA.

    Args:
        locale (str | Unset):
        body (SearchReturnMerchandiseAuthorizationsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchReturnMerchandiseAuthorizationsResponse]
     """


    kwargs = _get_kwargs(
        body=body,
locale=locale,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SearchReturnMerchandiseAuthorizationsRequest | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> SearchReturnMerchandiseAuthorizationsResponse | None:
    """ Search Return Merchandise Authorizations

     Searches return merchandise authorizations (RMAs) for the authorized shop. You can filter by
    identifiers, RMA status, and creation or update time. Use `whitelisted_data_fields` to include line
    items or SKU return requests for each RMA.

    Args:
        locale (str | Unset):
        body (SearchReturnMerchandiseAuthorizationsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchReturnMerchandiseAuthorizationsResponse
     """


    return sync_detailed(
        client=client,
body=body,
locale=locale,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchReturnMerchandiseAuthorizationsRequest | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> Response[SearchReturnMerchandiseAuthorizationsResponse]:
    """ Search Return Merchandise Authorizations

     Searches return merchandise authorizations (RMAs) for the authorized shop. You can filter by
    identifiers, RMA status, and creation or update time. Use `whitelisted_data_fields` to include line
    items or SKU return requests for each RMA.

    Args:
        locale (str | Unset):
        body (SearchReturnMerchandiseAuthorizationsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchReturnMerchandiseAuthorizationsResponse]
     """


    kwargs = _get_kwargs(
        body=body,
locale=locale,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchReturnMerchandiseAuthorizationsRequest | Unset = UNSET,
    locale: str | Unset = UNSET,

) -> SearchReturnMerchandiseAuthorizationsResponse | None:
    """ Search Return Merchandise Authorizations

     Searches return merchandise authorizations (RMAs) for the authorized shop. You can filter by
    identifiers, RMA status, and creation or update time. Use `whitelisted_data_fields` to include line
    items or SKU return requests for each RMA.

    Args:
        locale (str | Unset):
        body (SearchReturnMerchandiseAuthorizationsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchReturnMerchandiseAuthorizationsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
locale=locale,

    )).parsed
