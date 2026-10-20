from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_or_update_inbound_plan_request import CreateOrUpdateInboundPlanRequest
from ...models.create_or_update_inbound_plan_response import CreateOrUpdateInboundPlanResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: CreateOrUpdateInboundPlanRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fbt/202602/create_update_inbound_plan",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateOrUpdateInboundPlanResponse | None:
    if response.status_code == 200:
        response_200 = CreateOrUpdateInboundPlanResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateOrUpdateInboundPlanResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateOrUpdateInboundPlanRequest | Unset = UNSET,

) -> Response[CreateOrUpdateInboundPlanResponse]:
    """ Create or Update Inbound Plan

     Creates a new inbound plan or fully replaces the contents of an existing inbound plan by using a
    goods item list or carton configurations with dimensions. Omit `plan_id` to create a plan; provide
    it to update one. Provide exactly one non-empty array: `goods_items` or `cartons`; do not provide
    both.

    For an update, submit the complete desired goods or carton contents; previously stored goods or
    cartons omitted from the request are not retained. Using `goods_items` clears existing carton and
    lot/expiration data. Using `cartons` rebuilds the carton and item data.

    Args:
        body (CreateOrUpdateInboundPlanRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOrUpdateInboundPlanResponse]
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
    body: CreateOrUpdateInboundPlanRequest | Unset = UNSET,

) -> CreateOrUpdateInboundPlanResponse | None:
    """ Create or Update Inbound Plan

     Creates a new inbound plan or fully replaces the contents of an existing inbound plan by using a
    goods item list or carton configurations with dimensions. Omit `plan_id` to create a plan; provide
    it to update one. Provide exactly one non-empty array: `goods_items` or `cartons`; do not provide
    both.

    For an update, submit the complete desired goods or carton contents; previously stored goods or
    cartons omitted from the request are not retained. Using `goods_items` clears existing carton and
    lot/expiration data. Using `cartons` rebuilds the carton and item data.

    Args:
        body (CreateOrUpdateInboundPlanRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOrUpdateInboundPlanResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateOrUpdateInboundPlanRequest | Unset = UNSET,

) -> Response[CreateOrUpdateInboundPlanResponse]:
    """ Create or Update Inbound Plan

     Creates a new inbound plan or fully replaces the contents of an existing inbound plan by using a
    goods item list or carton configurations with dimensions. Omit `plan_id` to create a plan; provide
    it to update one. Provide exactly one non-empty array: `goods_items` or `cartons`; do not provide
    both.

    For an update, submit the complete desired goods or carton contents; previously stored goods or
    cartons omitted from the request are not retained. Using `goods_items` clears existing carton and
    lot/expiration data. Using `cartons` rebuilds the carton and item data.

    Args:
        body (CreateOrUpdateInboundPlanRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOrUpdateInboundPlanResponse]
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
    body: CreateOrUpdateInboundPlanRequest | Unset = UNSET,

) -> CreateOrUpdateInboundPlanResponse | None:
    """ Create or Update Inbound Plan

     Creates a new inbound plan or fully replaces the contents of an existing inbound plan by using a
    goods item list or carton configurations with dimensions. Omit `plan_id` to create a plan; provide
    it to update one. Provide exactly one non-empty array: `goods_items` or `cartons`; do not provide
    both.

    For an update, submit the complete desired goods or carton contents; previously stored goods or
    cartons omitted from the request are not retained. Using `goods_items` clears existing carton and
    lot/expiration data. Using `cartons` rebuilds the carton and item data.

    Args:
        body (CreateOrUpdateInboundPlanRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOrUpdateInboundPlanResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
