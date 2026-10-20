from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_product_request import CreateProductRequest
from ...models.create_product_response import CreateProductResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateProductRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202309/products",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateProductResponse | None:
    if response.status_code == 200:
        response_200 = CreateProductResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateProductResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateProductRequest,
) -> Response[CreateProductResponse]:
    """Create Product

     Create and list products intended for sale exclusively in local shops.
    You can create products in `AVAILABLE` categories. (US sellers can also create products in
    INVITE_ONLY categories). After creation, it will be sent for audit review by TikTok Shop. Use the
    [Product status change](https://partner.tiktokshop.com/docv2/page/650956aff1fd3102b90b6261) webhook
    to keep track of the review status.
    **Note**:
    - This API is applicable for all sellers.
    - Global sellers who have migrated to use the local replication listing method can use this API to
    create products. Otherwise, they can continue to use the [Create Global Product
    API](6509de61bace3e02b7489cba) to create global products.
    - Before calling this API, we recommend that you prepare the necessary information by following the
    [usage flow for your region](650b23eef1fd3102b93d2326).
    - There may be a limit to the number of products you can list per day. We recommend prioritizing the
    creation of key products first to ensure they get published. Refer to TikTok Shop Academy for
    details on the limit.
    - The language used in the product content must align with the target market's language (e.g. don't
    use Chinese), otherwise the listing will fail or be rejected.

    Args:
        body (CreateProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateProductResponse]
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
    body: CreateProductRequest,
) -> CreateProductResponse | None:
    """Create Product

     Create and list products intended for sale exclusively in local shops.
    You can create products in `AVAILABLE` categories. (US sellers can also create products in
    INVITE_ONLY categories). After creation, it will be sent for audit review by TikTok Shop. Use the
    [Product status change](https://partner.tiktokshop.com/docv2/page/650956aff1fd3102b90b6261) webhook
    to keep track of the review status.
    **Note**:
    - This API is applicable for all sellers.
    - Global sellers who have migrated to use the local replication listing method can use this API to
    create products. Otherwise, they can continue to use the [Create Global Product
    API](6509de61bace3e02b7489cba) to create global products.
    - Before calling this API, we recommend that you prepare the necessary information by following the
    [usage flow for your region](650b23eef1fd3102b93d2326).
    - There may be a limit to the number of products you can list per day. We recommend prioritizing the
    creation of key products first to ensure they get published. Refer to TikTok Shop Academy for
    details on the limit.
    - The language used in the product content must align with the target market's language (e.g. don't
    use Chinese), otherwise the listing will fail or be rejected.

    Args:
        body (CreateProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateProductResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateProductRequest,
) -> Response[CreateProductResponse]:
    """Create Product

     Create and list products intended for sale exclusively in local shops.
    You can create products in `AVAILABLE` categories. (US sellers can also create products in
    INVITE_ONLY categories). After creation, it will be sent for audit review by TikTok Shop. Use the
    [Product status change](https://partner.tiktokshop.com/docv2/page/650956aff1fd3102b90b6261) webhook
    to keep track of the review status.
    **Note**:
    - This API is applicable for all sellers.
    - Global sellers who have migrated to use the local replication listing method can use this API to
    create products. Otherwise, they can continue to use the [Create Global Product
    API](6509de61bace3e02b7489cba) to create global products.
    - Before calling this API, we recommend that you prepare the necessary information by following the
    [usage flow for your region](650b23eef1fd3102b93d2326).
    - There may be a limit to the number of products you can list per day. We recommend prioritizing the
    creation of key products first to ensure they get published. Refer to TikTok Shop Academy for
    details on the limit.
    - The language used in the product content must align with the target market's language (e.g. don't
    use Chinese), otherwise the listing will fail or be rejected.

    Args:
        body (CreateProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateProductResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateProductRequest,
) -> CreateProductResponse | None:
    """Create Product

     Create and list products intended for sale exclusively in local shops.
    You can create products in `AVAILABLE` categories. (US sellers can also create products in
    INVITE_ONLY categories). After creation, it will be sent for audit review by TikTok Shop. Use the
    [Product status change](https://partner.tiktokshop.com/docv2/page/650956aff1fd3102b90b6261) webhook
    to keep track of the review status.
    **Note**:
    - This API is applicable for all sellers.
    - Global sellers who have migrated to use the local replication listing method can use this API to
    create products. Otherwise, they can continue to use the [Create Global Product
    API](6509de61bace3e02b7489cba) to create global products.
    - Before calling this API, we recommend that you prepare the necessary information by following the
    [usage flow for your region](650b23eef1fd3102b93d2326).
    - There may be a limit to the number of products you can list per day. We recommend prioritizing the
    creation of key products first to ensure they get published. Refer to TikTok Shop Academy for
    details on the limit.
    - The language used in the product content must align with the target market's language (e.g. don't
    use Chinese), otherwise the listing will fail or be rejected.

    Args:
        body (CreateProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateProductResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
