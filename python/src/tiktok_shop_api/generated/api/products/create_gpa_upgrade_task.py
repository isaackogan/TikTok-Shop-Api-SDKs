from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_gpa_upgrade_task_request import CreateGPAUpgradeTaskRequest
from ...models.create_gpa_upgrade_task_response import CreateGPAUpgradeTaskResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: CreateGPAUpgradeTaskRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202604/products/gpa_upgrade_task",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateGPAUpgradeTaskResponse | None:
    if response.status_code == 200:
        response_200 = CreateGPAUpgradeTaskResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateGPAUpgradeTaskResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateGPAUpgradeTaskRequest | Unset = UNSET,

) -> Response[CreateGPAUpgradeTaskResponse]:
    """ Create GPA Upgrade Task

     This interface is only available for EU L2L sellers. The interface is used to upgrade products on EU
    interconnection. After the upgrade, products can be managed using the new interface, but not using
    interfaces related to Global Product.

    Args:
        body (CreateGPAUpgradeTaskRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateGPAUpgradeTaskResponse]
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
    body: CreateGPAUpgradeTaskRequest | Unset = UNSET,

) -> CreateGPAUpgradeTaskResponse | None:
    """ Create GPA Upgrade Task

     This interface is only available for EU L2L sellers. The interface is used to upgrade products on EU
    interconnection. After the upgrade, products can be managed using the new interface, but not using
    interfaces related to Global Product.

    Args:
        body (CreateGPAUpgradeTaskRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateGPAUpgradeTaskResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateGPAUpgradeTaskRequest | Unset = UNSET,

) -> Response[CreateGPAUpgradeTaskResponse]:
    """ Create GPA Upgrade Task

     This interface is only available for EU L2L sellers. The interface is used to upgrade products on EU
    interconnection. After the upgrade, products can be managed using the new interface, but not using
    interfaces related to Global Product.

    Args:
        body (CreateGPAUpgradeTaskRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateGPAUpgradeTaskResponse]
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
    body: CreateGPAUpgradeTaskRequest | Unset = UNSET,

) -> CreateGPAUpgradeTaskResponse | None:
    """ Create GPA Upgrade Task

     This interface is only available for EU L2L sellers. The interface is used to upgrade products on EU
    interconnection. After the upgrade, products can be managed using the new interface, but not using
    interfaces related to Global Product.

    Args:
        body (CreateGPAUpgradeTaskRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateGPAUpgradeTaskResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
