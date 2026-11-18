from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.list_shop_materials_material_status import ListShopMaterialsMaterialStatus
from ...models.list_shop_materials_response import ListShopMaterialsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    product_id: str,
    material_status: ListShopMaterialsMaterialStatus | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["product_id"] = product_id

    json_material_status: str | Unset = UNSET
    if not isinstance(material_status, Unset):
        json_material_status = material_status.value

    params["material_status"] = json_material_status


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/seller/202611/materials",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ListShopMaterialsResponse | None:
    if response.status_code == 200:
        response_200 = ListShopMaterialsResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ListShopMaterialsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    product_id: str,
    material_status: ListShopMaterialsMaterialStatus | Unset = UNSET,

) -> Response[ListShopMaterialsResponse]:
    """ List Shop Materials

     List image material groups for the currently authorized shop under one product.

    Args:
        product_id (str):
        material_status (ListShopMaterialsMaterialStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListShopMaterialsResponse]
     """


    kwargs = _get_kwargs(
        product_id=product_id,
material_status=material_status,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    product_id: str,
    material_status: ListShopMaterialsMaterialStatus | Unset = UNSET,

) -> ListShopMaterialsResponse | None:
    """ List Shop Materials

     List image material groups for the currently authorized shop under one product.

    Args:
        product_id (str):
        material_status (ListShopMaterialsMaterialStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListShopMaterialsResponse
     """


    return sync_detailed(
        client=client,
product_id=product_id,
material_status=material_status,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    product_id: str,
    material_status: ListShopMaterialsMaterialStatus | Unset = UNSET,

) -> Response[ListShopMaterialsResponse]:
    """ List Shop Materials

     List image material groups for the currently authorized shop under one product.

    Args:
        product_id (str):
        material_status (ListShopMaterialsMaterialStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListShopMaterialsResponse]
     """


    kwargs = _get_kwargs(
        product_id=product_id,
material_status=material_status,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    product_id: str,
    material_status: ListShopMaterialsMaterialStatus | Unset = UNSET,

) -> ListShopMaterialsResponse | None:
    """ List Shop Materials

     List image material groups for the currently authorized shop under one product.

    Args:
        product_id (str):
        material_status (ListShopMaterialsMaterialStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListShopMaterialsResponse
     """


    return (await asyncio_detailed(
        client=client,
product_id=product_id,
material_status=material_status,

    )).parsed
