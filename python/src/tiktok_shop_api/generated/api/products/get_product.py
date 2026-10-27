from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_product_locale import GetProductLocale
from ...models.get_product_response import GetProductResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    product_id: str,
    *,
    return_under_review_version: bool | Unset = UNSET,
    return_draft_version: bool | Unset = UNSET,
    locale: GetProductLocale | Unset = UNSET,
    query_options: list[str] | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["return_under_review_version"] = return_under_review_version

    params["return_draft_version"] = return_draft_version

    json_locale: str | Unset = UNSET
    if not isinstance(locale, Unset):
        json_locale = locale.value

    params["locale"] = json_locale

    json_query_options: list[str] | Unset = UNSET
    if not isinstance(query_options, Unset):
        json_query_options = query_options


    params["query_options"] = json_query_options


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/product/202309/products/{product_id}".format(product_id=quote(str(product_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetProductResponse | None:
    if response.status_code == 200:
        response_200 = GetProductResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetProductResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    return_under_review_version: bool | Unset = UNSET,
    return_draft_version: bool | Unset = UNSET,
    locale: GetProductLocale | Unset = UNSET,
    query_options: list[str] | Unset = UNSET,

) -> Response[GetProductResponse]:
    """ Get Product

     Retrieve product details by product ID, including products in the `FREEZE` or `DELETED` status.

    Args:
        product_id (str):
        return_under_review_version (bool | Unset):
        return_draft_version (bool | Unset):
        locale (GetProductLocale | Unset):
        query_options (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProductResponse]
     """


    kwargs = _get_kwargs(
        product_id=product_id,
return_under_review_version=return_under_review_version,
return_draft_version=return_draft_version,
locale=locale,
query_options=query_options,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    return_under_review_version: bool | Unset = UNSET,
    return_draft_version: bool | Unset = UNSET,
    locale: GetProductLocale | Unset = UNSET,
    query_options: list[str] | Unset = UNSET,

) -> GetProductResponse | None:
    """ Get Product

     Retrieve product details by product ID, including products in the `FREEZE` or `DELETED` status.

    Args:
        product_id (str):
        return_under_review_version (bool | Unset):
        return_draft_version (bool | Unset):
        locale (GetProductLocale | Unset):
        query_options (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProductResponse
     """


    return sync_detailed(
        product_id=product_id,
client=client,
return_under_review_version=return_under_review_version,
return_draft_version=return_draft_version,
locale=locale,
query_options=query_options,

    ).parsed

async def asyncio_detailed(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    return_under_review_version: bool | Unset = UNSET,
    return_draft_version: bool | Unset = UNSET,
    locale: GetProductLocale | Unset = UNSET,
    query_options: list[str] | Unset = UNSET,

) -> Response[GetProductResponse]:
    """ Get Product

     Retrieve product details by product ID, including products in the `FREEZE` or `DELETED` status.

    Args:
        product_id (str):
        return_under_review_version (bool | Unset):
        return_draft_version (bool | Unset):
        locale (GetProductLocale | Unset):
        query_options (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProductResponse]
     """


    kwargs = _get_kwargs(
        product_id=product_id,
return_under_review_version=return_under_review_version,
return_draft_version=return_draft_version,
locale=locale,
query_options=query_options,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    return_under_review_version: bool | Unset = UNSET,
    return_draft_version: bool | Unset = UNSET,
    locale: GetProductLocale | Unset = UNSET,
    query_options: list[str] | Unset = UNSET,

) -> GetProductResponse | None:
    """ Get Product

     Retrieve product details by product ID, including products in the `FREEZE` or `DELETED` status.

    Args:
        product_id (str):
        return_under_review_version (bool | Unset):
        return_draft_version (bool | Unset):
        locale (GetProductLocale | Unset):
        query_options (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProductResponse
     """


    return (await asyncio_detailed(
        product_id=product_id,
client=client,
return_under_review_version=return_under_review_version,
return_draft_version=return_draft_version,
locale=locale,
query_options=query_options,

    )).parsed
