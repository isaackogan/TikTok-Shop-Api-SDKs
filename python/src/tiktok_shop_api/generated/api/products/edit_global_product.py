from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.edit_global_product_request import EditGlobalProductRequest
from ...models.edit_global_product_response import EditGlobalProductResponse
from ...types import Response


def _get_kwargs(
    global_product_id: str,
    *,
    body: EditGlobalProductRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/product/202309/global_products/{global_product_id}".format(
            global_product_id=quote(str(global_product_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EditGlobalProductResponse | None:
    if response.status_code == 200:
        response_200 = EditGlobalProductResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EditGlobalProductResponse]:
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
    body: EditGlobalProductRequest,
) -> Response[EditGlobalProductResponse]:
    """Edit Global Product

     Edit all properties (e.g. description, brand, images, attributes) of a global product.
    **IMPORTANT**: For published products, the changes will be automatically retranslated and synced to
    all markets where the product is published. If you have already edited the product information or
    translations of the associated local products, they will be overwritten by the information in this
    API. For example, if you have customized the local prices such as the local pre-tax price or the
    local display price, they will be overwritten each time this API is called.
    **Note**:
    - There may be a limit to the number of products you can relist per day. We recommend prioritizing
    key products first to ensure they get published. You can find your listing limit on the Seller
    Center homepage.
    - All inputs, including blanks, in the request payload will overwrite existing values. To retain an
    existing value, make sure to include it in your request. Therefore, **it is strongly recommended to
    retrieve the latest product data using [Get Global Product](6509e2b0bace3e02b7490c96) and submit the
    complete data when editing**. This ensures accuracy and helps avoid errors or unintentional data
    loss due to missing fields.
    - The language used in the product content must align with the target market's language (e.g. don't
    use Chinese), otherwise the listing will fail or be rejected.

    Args:
        global_product_id (str):
        body (EditGlobalProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EditGlobalProductResponse]
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
    body: EditGlobalProductRequest,
) -> EditGlobalProductResponse | None:
    """Edit Global Product

     Edit all properties (e.g. description, brand, images, attributes) of a global product.
    **IMPORTANT**: For published products, the changes will be automatically retranslated and synced to
    all markets where the product is published. If you have already edited the product information or
    translations of the associated local products, they will be overwritten by the information in this
    API. For example, if you have customized the local prices such as the local pre-tax price or the
    local display price, they will be overwritten each time this API is called.
    **Note**:
    - There may be a limit to the number of products you can relist per day. We recommend prioritizing
    key products first to ensure they get published. You can find your listing limit on the Seller
    Center homepage.
    - All inputs, including blanks, in the request payload will overwrite existing values. To retain an
    existing value, make sure to include it in your request. Therefore, **it is strongly recommended to
    retrieve the latest product data using [Get Global Product](6509e2b0bace3e02b7490c96) and submit the
    complete data when editing**. This ensures accuracy and helps avoid errors or unintentional data
    loss due to missing fields.
    - The language used in the product content must align with the target market's language (e.g. don't
    use Chinese), otherwise the listing will fail or be rejected.

    Args:
        global_product_id (str):
        body (EditGlobalProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EditGlobalProductResponse
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
    body: EditGlobalProductRequest,
) -> Response[EditGlobalProductResponse]:
    """Edit Global Product

     Edit all properties (e.g. description, brand, images, attributes) of a global product.
    **IMPORTANT**: For published products, the changes will be automatically retranslated and synced to
    all markets where the product is published. If you have already edited the product information or
    translations of the associated local products, they will be overwritten by the information in this
    API. For example, if you have customized the local prices such as the local pre-tax price or the
    local display price, they will be overwritten each time this API is called.
    **Note**:
    - There may be a limit to the number of products you can relist per day. We recommend prioritizing
    key products first to ensure they get published. You can find your listing limit on the Seller
    Center homepage.
    - All inputs, including blanks, in the request payload will overwrite existing values. To retain an
    existing value, make sure to include it in your request. Therefore, **it is strongly recommended to
    retrieve the latest product data using [Get Global Product](6509e2b0bace3e02b7490c96) and submit the
    complete data when editing**. This ensures accuracy and helps avoid errors or unintentional data
    loss due to missing fields.
    - The language used in the product content must align with the target market's language (e.g. don't
    use Chinese), otherwise the listing will fail or be rejected.

    Args:
        global_product_id (str):
        body (EditGlobalProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EditGlobalProductResponse]
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
    body: EditGlobalProductRequest,
) -> EditGlobalProductResponse | None:
    """Edit Global Product

     Edit all properties (e.g. description, brand, images, attributes) of a global product.
    **IMPORTANT**: For published products, the changes will be automatically retranslated and synced to
    all markets where the product is published. If you have already edited the product information or
    translations of the associated local products, they will be overwritten by the information in this
    API. For example, if you have customized the local prices such as the local pre-tax price or the
    local display price, they will be overwritten each time this API is called.
    **Note**:
    - There may be a limit to the number of products you can relist per day. We recommend prioritizing
    key products first to ensure they get published. You can find your listing limit on the Seller
    Center homepage.
    - All inputs, including blanks, in the request payload will overwrite existing values. To retain an
    existing value, make sure to include it in your request. Therefore, **it is strongly recommended to
    retrieve the latest product data using [Get Global Product](6509e2b0bace3e02b7490c96) and submit the
    complete data when editing**. This ensures accuracy and helps avoid errors or unintentional data
    loss due to missing fields.
    - The language used in the product content must align with the target market's language (e.g. don't
    use Chinese), otherwise the listing will fail or be rejected.

    Args:
        global_product_id (str):
        body (EditGlobalProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EditGlobalProductResponse
    """

    return (
        await asyncio_detailed(
            global_product_id=global_product_id,
            client=client,
            body=body,
        )
    ).parsed
