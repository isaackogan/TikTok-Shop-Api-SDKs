from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.partial_edit_global_product_request import PartialEditGlobalProductRequest
from ...models.partial_edit_global_product_response import PartialEditGlobalProductResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    global_product_id: str,
    *,
    body: PartialEditGlobalProductRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/product/202509/global_products/{global_product_id}/partial_edit".format(
            global_product_id=quote(str(global_product_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PartialEditGlobalProductResponse | None:
    if response.status_code == 200:
        response_200 = PartialEditGlobalProductResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PartialEditGlobalProductResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    global_product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PartialEditGlobalProductRequest | Unset = UNSET,
) -> Response[PartialEditGlobalProductResponse]:
    """Partial Edit Global Product

     Partially update an existing global product. Only the fields included in the request are considered
    for update. If the global product is linked to local products, applicable changes are also
    synchronized to those markets; check `publish_results` for each market's synchronization result.

    Args:
        global_product_id (str):
        body (PartialEditGlobalProductRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PartialEditGlobalProductResponse]
    """

    kwargs = _get_kwargs(
        global_product_id=global_product_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    global_product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PartialEditGlobalProductRequest | Unset = UNSET,
) -> PartialEditGlobalProductResponse | None:
    """Partial Edit Global Product

     Partially update an existing global product. Only the fields included in the request are considered
    for update. If the global product is linked to local products, applicable changes are also
    synchronized to those markets; check `publish_results` for each market's synchronization result.

    Args:
        global_product_id (str):
        body (PartialEditGlobalProductRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PartialEditGlobalProductResponse
    """

    return sync_detailed(
        global_product_id=global_product_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    global_product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PartialEditGlobalProductRequest | Unset = UNSET,
) -> Response[PartialEditGlobalProductResponse]:
    """Partial Edit Global Product

     Partially update an existing global product. Only the fields included in the request are considered
    for update. If the global product is linked to local products, applicable changes are also
    synchronized to those markets; check `publish_results` for each market's synchronization result.

    Args:
        global_product_id (str):
        body (PartialEditGlobalProductRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PartialEditGlobalProductResponse]
    """

    kwargs = _get_kwargs(
        global_product_id=global_product_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    global_product_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PartialEditGlobalProductRequest | Unset = UNSET,
) -> PartialEditGlobalProductResponse | None:
    """Partial Edit Global Product

     Partially update an existing global product. Only the fields included in the request are considered
    for update. If the global product is linked to local products, applicable changes are also
    synchronized to those markets; check `publish_results` for each market's synchronization result.

    Args:
        global_product_id (str):
        body (PartialEditGlobalProductRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PartialEditGlobalProductResponse
    """

    return (
        await asyncio_detailed(
            global_product_id=global_product_id,
            client=client,
            body=body,
        )
    ).parsed
