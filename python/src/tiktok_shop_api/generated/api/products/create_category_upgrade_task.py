from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_category_upgrade_task_request import CreateCategoryUpgradeTaskRequest
from ...models.create_category_upgrade_task_response import CreateCategoryUpgradeTaskResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: CreateCategoryUpgradeTaskRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202407/products/category_upgrade_task",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateCategoryUpgradeTaskResponse | None:
    if response.status_code == 200:
        response_200 = CreateCategoryUpgradeTaskResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateCategoryUpgradeTaskResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateCategoryUpgradeTaskRequest | Unset = UNSET,

) -> Response[CreateCategoryUpgradeTaskResponse]:
    """ Create Category Upgrade Task

     Create a task to upgrade live products (status: `ACTIVATE`) from a 3-level to a 7-level category
    tree.
    The task runs for up to 2 hours, depending on the number of products. If the upgrade is incomplete
    after 2 hours, call the API again. To figure out which products' categories have not been upgraded,
    call the [Search Product API](https://partner.tiktokshop.com/docv2/page/65854ffb8f559302d8a6acda)
    and set "category_version" to "v1".
    **Note**: You must wait at least 24 hours after a product goes live to successfully upgrade its
    category. If you call this API on the same day a new product goes live, the system will be unable to
    detect it.

    Args:
        body (CreateCategoryUpgradeTaskRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateCategoryUpgradeTaskResponse]
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
    body: CreateCategoryUpgradeTaskRequest | Unset = UNSET,

) -> CreateCategoryUpgradeTaskResponse | None:
    """ Create Category Upgrade Task

     Create a task to upgrade live products (status: `ACTIVATE`) from a 3-level to a 7-level category
    tree.
    The task runs for up to 2 hours, depending on the number of products. If the upgrade is incomplete
    after 2 hours, call the API again. To figure out which products' categories have not been upgraded,
    call the [Search Product API](https://partner.tiktokshop.com/docv2/page/65854ffb8f559302d8a6acda)
    and set "category_version" to "v1".
    **Note**: You must wait at least 24 hours after a product goes live to successfully upgrade its
    category. If you call this API on the same day a new product goes live, the system will be unable to
    detect it.

    Args:
        body (CreateCategoryUpgradeTaskRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateCategoryUpgradeTaskResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateCategoryUpgradeTaskRequest | Unset = UNSET,

) -> Response[CreateCategoryUpgradeTaskResponse]:
    """ Create Category Upgrade Task

     Create a task to upgrade live products (status: `ACTIVATE`) from a 3-level to a 7-level category
    tree.
    The task runs for up to 2 hours, depending on the number of products. If the upgrade is incomplete
    after 2 hours, call the API again. To figure out which products' categories have not been upgraded,
    call the [Search Product API](https://partner.tiktokshop.com/docv2/page/65854ffb8f559302d8a6acda)
    and set "category_version" to "v1".
    **Note**: You must wait at least 24 hours after a product goes live to successfully upgrade its
    category. If you call this API on the same day a new product goes live, the system will be unable to
    detect it.

    Args:
        body (CreateCategoryUpgradeTaskRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateCategoryUpgradeTaskResponse]
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
    body: CreateCategoryUpgradeTaskRequest | Unset = UNSET,

) -> CreateCategoryUpgradeTaskResponse | None:
    """ Create Category Upgrade Task

     Create a task to upgrade live products (status: `ACTIVATE`) from a 3-level to a 7-level category
    tree.
    The task runs for up to 2 hours, depending on the number of products. If the upgrade is incomplete
    after 2 hours, call the API again. To figure out which products' categories have not been upgraded,
    call the [Search Product API](https://partner.tiktokshop.com/docv2/page/65854ffb8f559302d8a6acda)
    and set "category_version" to "v1".
    **Note**: You must wait at least 24 hours after a product goes live to successfully upgrade its
    category. If you call this API on the same day a new product goes live, the system will be unable to
    detect it.

    Args:
        body (CreateCategoryUpgradeTaskRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateCategoryUpgradeTaskResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
