from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_open_collaboration_product_list_by_product_ids_request import GetOpenCollaborationProductListByProductIdsRequest
from ...models.get_open_collaboration_product_list_by_product_ids_response import GetOpenCollaborationProductListByProductIdsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: GetOpenCollaborationProductListByProductIdsRequest | Unset = UNSET,
    product_ids: list[str] | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    json_product_ids: list[str] | Unset = UNSET
    if not isinstance(product_ids, Unset):
        json_product_ids = product_ids


    params["product_ids"] = json_product_ids


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate_creator/202509/open_collaborations/products",
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetOpenCollaborationProductListByProductIdsResponse | None:
    if response.status_code == 200:
        response_200 = GetOpenCollaborationProductListByProductIdsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetOpenCollaborationProductListByProductIdsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetOpenCollaborationProductListByProductIdsRequest | Unset = UNSET,
    product_ids: list[str] | Unset = UNSET,

) -> Response[GetOpenCollaborationProductListByProductIdsResponse]:
    """ Get Open Collaboration Product List By Product Ids

     Retrieves open collaboration product information for the specified product IDs.

    Args:
        product_ids (list[str] | Unset):
        body (GetOpenCollaborationProductListByProductIdsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOpenCollaborationProductListByProductIdsResponse]
     """


    kwargs = _get_kwargs(
        body=body,
product_ids=product_ids,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: GetOpenCollaborationProductListByProductIdsRequest | Unset = UNSET,
    product_ids: list[str] | Unset = UNSET,

) -> GetOpenCollaborationProductListByProductIdsResponse | None:
    """ Get Open Collaboration Product List By Product Ids

     Retrieves open collaboration product information for the specified product IDs.

    Args:
        product_ids (list[str] | Unset):
        body (GetOpenCollaborationProductListByProductIdsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOpenCollaborationProductListByProductIdsResponse
     """


    return sync_detailed(
        client=client,
body=body,
product_ids=product_ids,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GetOpenCollaborationProductListByProductIdsRequest | Unset = UNSET,
    product_ids: list[str] | Unset = UNSET,

) -> Response[GetOpenCollaborationProductListByProductIdsResponse]:
    """ Get Open Collaboration Product List By Product Ids

     Retrieves open collaboration product information for the specified product IDs.

    Args:
        product_ids (list[str] | Unset):
        body (GetOpenCollaborationProductListByProductIdsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOpenCollaborationProductListByProductIdsResponse]
     """


    kwargs = _get_kwargs(
        body=body,
product_ids=product_ids,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GetOpenCollaborationProductListByProductIdsRequest | Unset = UNSET,
    product_ids: list[str] | Unset = UNSET,

) -> GetOpenCollaborationProductListByProductIdsResponse | None:
    """ Get Open Collaboration Product List By Product Ids

     Retrieves open collaboration product information for the specified product IDs.

    Args:
        product_ids (list[str] | Unset):
        body (GetOpenCollaborationProductListByProductIdsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOpenCollaborationProductListByProductIdsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
product_ids=product_ids,

    )).parsed
