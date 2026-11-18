from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_shop_material_request import DeleteShopMaterialRequest
from ...models.delete_shop_material_response import DeleteShopMaterialResponse
from typing import cast



def _get_kwargs(
    *,
    body: DeleteShopMaterialRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/seller/202611/materials",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteShopMaterialResponse | None:
    if response.status_code == 200:
        response_200 = DeleteShopMaterialResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteShopMaterialResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteShopMaterialRequest,

) -> Response[DeleteShopMaterialResponse]:
    """ Delete Shop Material

     Delete a seller material for the currently authorized shop. Provide `material_id` for
    `ONE_PRODUCT_ONE_IMAGE` deletion or `image_group_id` for `ONE_PRODUCT_MULTIPLE_IMAGES` deletion.

    Args:
        body (DeleteShopMaterialRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteShopMaterialResponse]
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
    body: DeleteShopMaterialRequest,

) -> DeleteShopMaterialResponse | None:
    """ Delete Shop Material

     Delete a seller material for the currently authorized shop. Provide `material_id` for
    `ONE_PRODUCT_ONE_IMAGE` deletion or `image_group_id` for `ONE_PRODUCT_MULTIPLE_IMAGES` deletion.

    Args:
        body (DeleteShopMaterialRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteShopMaterialResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DeleteShopMaterialRequest,

) -> Response[DeleteShopMaterialResponse]:
    """ Delete Shop Material

     Delete a seller material for the currently authorized shop. Provide `material_id` for
    `ONE_PRODUCT_ONE_IMAGE` deletion or `image_group_id` for `ONE_PRODUCT_MULTIPLE_IMAGES` deletion.

    Args:
        body (DeleteShopMaterialRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteShopMaterialResponse]
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
    body: DeleteShopMaterialRequest,

) -> DeleteShopMaterialResponse | None:
    """ Delete Shop Material

     Delete a seller material for the currently authorized shop. Provide `material_id` for
    `ONE_PRODUCT_ONE_IMAGE` deletion or `image_group_id` for `ONE_PRODUCT_MULTIPLE_IMAGES` deletion.

    Args:
        body (DeleteShopMaterialRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteShopMaterialResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
