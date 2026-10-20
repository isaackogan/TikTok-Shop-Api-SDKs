from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.publish_global_product_request import PublishGlobalProductRequest
from ...models.publish_global_product_response import PublishGlobalProductResponse
from ...types import Response


def _get_kwargs(
    global_product_id: str,
    *,
    body: PublishGlobalProductRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202309/global_products/{global_product_id}/publish".format(
            global_product_id=quote(str(global_product_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PublishGlobalProductResponse | None:
    if response.status_code == 200:
        response_200 = PublishGlobalProductResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PublishGlobalProductResponse]:
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
    body: PublishGlobalProductRequest,
) -> Response[PublishGlobalProductResponse]:
    """Publish Global Product

     Publish and convert a global product to local products in one or multiple shops in supported
    markets. After publishing, the product is sent for review by TikTok Shop in the respective markets.
    For sellers in the EU market, the provided information will also be automatically translated into
    all EU languages supported by TikTok Shop.
    **Note**:
    - You can only publish in each market once. To change product information, edit the global product
    by using the [Edit Global Product API](6509e1bcc16ffe02b8dc3cd7). The changes will be automatically
    synchronized to all markets where the product is published
    - Use the [Get Product API](6509d85b4a0bb702c057fdda) to obtain the converted local product
    information in the target market's language.
    - Use the [Edit Product API](6509da7d0fcef602bf1caddf) or [Partial Edit Product
    API](650a98d74a0bb702c06c3289) to edit the local product information, if necessary.

    Args:
        global_product_id (str):
        body (PublishGlobalProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PublishGlobalProductResponse]
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
    body: PublishGlobalProductRequest,
) -> PublishGlobalProductResponse | None:
    """Publish Global Product

     Publish and convert a global product to local products in one or multiple shops in supported
    markets. After publishing, the product is sent for review by TikTok Shop in the respective markets.
    For sellers in the EU market, the provided information will also be automatically translated into
    all EU languages supported by TikTok Shop.
    **Note**:
    - You can only publish in each market once. To change product information, edit the global product
    by using the [Edit Global Product API](6509e1bcc16ffe02b8dc3cd7). The changes will be automatically
    synchronized to all markets where the product is published
    - Use the [Get Product API](6509d85b4a0bb702c057fdda) to obtain the converted local product
    information in the target market's language.
    - Use the [Edit Product API](6509da7d0fcef602bf1caddf) or [Partial Edit Product
    API](650a98d74a0bb702c06c3289) to edit the local product information, if necessary.

    Args:
        global_product_id (str):
        body (PublishGlobalProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PublishGlobalProductResponse
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
    body: PublishGlobalProductRequest,
) -> Response[PublishGlobalProductResponse]:
    """Publish Global Product

     Publish and convert a global product to local products in one or multiple shops in supported
    markets. After publishing, the product is sent for review by TikTok Shop in the respective markets.
    For sellers in the EU market, the provided information will also be automatically translated into
    all EU languages supported by TikTok Shop.
    **Note**:
    - You can only publish in each market once. To change product information, edit the global product
    by using the [Edit Global Product API](6509e1bcc16ffe02b8dc3cd7). The changes will be automatically
    synchronized to all markets where the product is published
    - Use the [Get Product API](6509d85b4a0bb702c057fdda) to obtain the converted local product
    information in the target market's language.
    - Use the [Edit Product API](6509da7d0fcef602bf1caddf) or [Partial Edit Product
    API](650a98d74a0bb702c06c3289) to edit the local product information, if necessary.

    Args:
        global_product_id (str):
        body (PublishGlobalProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PublishGlobalProductResponse]
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
    body: PublishGlobalProductRequest,
) -> PublishGlobalProductResponse | None:
    """Publish Global Product

     Publish and convert a global product to local products in one or multiple shops in supported
    markets. After publishing, the product is sent for review by TikTok Shop in the respective markets.
    For sellers in the EU market, the provided information will also be automatically translated into
    all EU languages supported by TikTok Shop.
    **Note**:
    - You can only publish in each market once. To change product information, edit the global product
    by using the [Edit Global Product API](6509e1bcc16ffe02b8dc3cd7). The changes will be automatically
    synchronized to all markets where the product is published
    - Use the [Get Product API](6509d85b4a0bb702c057fdda) to obtain the converted local product
    information in the target market's language.
    - Use the [Edit Product API](6509da7d0fcef602bf1caddf) or [Partial Edit Product
    API](650a98d74a0bb702c06c3289) to edit the local product information, if necessary.

    Args:
        global_product_id (str):
        body (PublishGlobalProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PublishGlobalProductResponse
    """

    return (
        await asyncio_detailed(
            global_product_id=global_product_id,
            client=client,
            body=body,
        )
    ).parsed
