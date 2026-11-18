from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.check_material_statuses_response import CheckMaterialStatusesResponse
from typing import cast



def _get_kwargs(
    *,
    pending_material_ids: list[str],

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_pending_material_ids = pending_material_ids


    params["pending_material_ids"] = json_pending_material_ids


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/seller/202611/material_statuses",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CheckMaterialStatusesResponse | None:
    if response.status_code == 200:
        response_200 = CheckMaterialStatusesResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CheckMaterialStatusesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    pending_material_ids: list[str],

) -> Response[CheckMaterialStatusesResponse]:
    """ Check Material Statuses

     Query the review statuses of pending material IDs for the currently authorized shop. The response
    order matches the input order of `pending_material_ids`.

    Args:
        pending_material_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckMaterialStatusesResponse]
     """


    kwargs = _get_kwargs(
        pending_material_ids=pending_material_ids,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    pending_material_ids: list[str],

) -> CheckMaterialStatusesResponse | None:
    """ Check Material Statuses

     Query the review statuses of pending material IDs for the currently authorized shop. The response
    order matches the input order of `pending_material_ids`.

    Args:
        pending_material_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckMaterialStatusesResponse
     """


    return sync_detailed(
        client=client,
pending_material_ids=pending_material_ids,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    pending_material_ids: list[str],

) -> Response[CheckMaterialStatusesResponse]:
    """ Check Material Statuses

     Query the review statuses of pending material IDs for the currently authorized shop. The response
    order matches the input order of `pending_material_ids`.

    Args:
        pending_material_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckMaterialStatusesResponse]
     """


    kwargs = _get_kwargs(
        pending_material_ids=pending_material_ids,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    pending_material_ids: list[str],

) -> CheckMaterialStatusesResponse | None:
    """ Check Material Statuses

     Query the review statuses of pending material IDs for the currently authorized shop. The response
    order matches the input order of `pending_material_ids`.

    Args:
        pending_material_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckMaterialStatusesResponse
     """


    return (await asyncio_detailed(
        client=client,
pending_material_ids=pending_material_ids,

    )).parsed
