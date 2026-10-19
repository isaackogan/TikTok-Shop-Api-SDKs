from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.diagnose_and_optimize_product_request import DiagnoseAndOptimizeProductRequest
from ...models.diagnose_and_optimize_product_response import DiagnoseAndOptimizeProductResponse
from ...types import Response


def _get_kwargs(
    *,
    body: DiagnoseAndOptimizeProductRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202411/products/diagnose_optimize",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DiagnoseAndOptimizeProductResponse | None:
    if response.status_code == 200:
        response_200 = DiagnoseAndOptimizeProductResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DiagnoseAndOptimizeProductResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DiagnoseAndOptimizeProductRequest,
) -> Response[DiagnoseAndOptimizeProductResponse]:
    """Diagnose and Optimize Product

     Diagnose products to obtain information that helps you to improve the product content, enhancing
    product visibility and customer trust. The returned information includes:
    - Listing quality information (available only for the US market).
    - Issues with the current product details and the overall recommendations
    - Auto-generated optimization suggestions targeted for specific product fields, including the title,
    description, and image.
    This API enables you to diagnose both live products (status: `ACTIVATE`)  and brand-new products not
    yet listed in TikTok Shop.
    - To diagnose a **live product**, provide the `product_id` and `category_id` and leave all other
    product details blank.
    - To diagnose a **brand-new product** not yet listed in TikTok Shop, omit the `product_id` and
    provide the product details as necessary.
    - To diagnose a **product similar to an existing one**, provide the `product_id` and `category_id`,
    along with any new details. The diagnosis will combine the existing product's information with the
    new details you provide. For example, if you provide a new `title`, the diagnosis will use the new
    title instead of the existing one while keeping the other values from the product ID.
    **Note**:
    - To diagnose multiple live products, use the [Product Information Issue Diagnosis
    API](665048f380b6b302e73917d9).
    - This API focuses solely on optimizing product visibility and does not evaluate whether your
    product meets listing requirements. Quality issues identified by this API do not block your product
    from being listed. To verify listing requirements, use the [Check Product Listing
    API](650a0ee8f1fd3102b91c6493).

    Args:
        body (DiagnoseAndOptimizeProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DiagnoseAndOptimizeProductResponse]
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
    body: DiagnoseAndOptimizeProductRequest,
) -> DiagnoseAndOptimizeProductResponse | None:
    """Diagnose and Optimize Product

     Diagnose products to obtain information that helps you to improve the product content, enhancing
    product visibility and customer trust. The returned information includes:
    - Listing quality information (available only for the US market).
    - Issues with the current product details and the overall recommendations
    - Auto-generated optimization suggestions targeted for specific product fields, including the title,
    description, and image.
    This API enables you to diagnose both live products (status: `ACTIVATE`)  and brand-new products not
    yet listed in TikTok Shop.
    - To diagnose a **live product**, provide the `product_id` and `category_id` and leave all other
    product details blank.
    - To diagnose a **brand-new product** not yet listed in TikTok Shop, omit the `product_id` and
    provide the product details as necessary.
    - To diagnose a **product similar to an existing one**, provide the `product_id` and `category_id`,
    along with any new details. The diagnosis will combine the existing product's information with the
    new details you provide. For example, if you provide a new `title`, the diagnosis will use the new
    title instead of the existing one while keeping the other values from the product ID.
    **Note**:
    - To diagnose multiple live products, use the [Product Information Issue Diagnosis
    API](665048f380b6b302e73917d9).
    - This API focuses solely on optimizing product visibility and does not evaluate whether your
    product meets listing requirements. Quality issues identified by this API do not block your product
    from being listed. To verify listing requirements, use the [Check Product Listing
    API](650a0ee8f1fd3102b91c6493).

    Args:
        body (DiagnoseAndOptimizeProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DiagnoseAndOptimizeProductResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DiagnoseAndOptimizeProductRequest,
) -> Response[DiagnoseAndOptimizeProductResponse]:
    """Diagnose and Optimize Product

     Diagnose products to obtain information that helps you to improve the product content, enhancing
    product visibility and customer trust. The returned information includes:
    - Listing quality information (available only for the US market).
    - Issues with the current product details and the overall recommendations
    - Auto-generated optimization suggestions targeted for specific product fields, including the title,
    description, and image.
    This API enables you to diagnose both live products (status: `ACTIVATE`)  and brand-new products not
    yet listed in TikTok Shop.
    - To diagnose a **live product**, provide the `product_id` and `category_id` and leave all other
    product details blank.
    - To diagnose a **brand-new product** not yet listed in TikTok Shop, omit the `product_id` and
    provide the product details as necessary.
    - To diagnose a **product similar to an existing one**, provide the `product_id` and `category_id`,
    along with any new details. The diagnosis will combine the existing product's information with the
    new details you provide. For example, if you provide a new `title`, the diagnosis will use the new
    title instead of the existing one while keeping the other values from the product ID.
    **Note**:
    - To diagnose multiple live products, use the [Product Information Issue Diagnosis
    API](665048f380b6b302e73917d9).
    - This API focuses solely on optimizing product visibility and does not evaluate whether your
    product meets listing requirements. Quality issues identified by this API do not block your product
    from being listed. To verify listing requirements, use the [Check Product Listing
    API](650a0ee8f1fd3102b91c6493).

    Args:
        body (DiagnoseAndOptimizeProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DiagnoseAndOptimizeProductResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DiagnoseAndOptimizeProductRequest,
) -> DiagnoseAndOptimizeProductResponse | None:
    """Diagnose and Optimize Product

     Diagnose products to obtain information that helps you to improve the product content, enhancing
    product visibility and customer trust. The returned information includes:
    - Listing quality information (available only for the US market).
    - Issues with the current product details and the overall recommendations
    - Auto-generated optimization suggestions targeted for specific product fields, including the title,
    description, and image.
    This API enables you to diagnose both live products (status: `ACTIVATE`)  and brand-new products not
    yet listed in TikTok Shop.
    - To diagnose a **live product**, provide the `product_id` and `category_id` and leave all other
    product details blank.
    - To diagnose a **brand-new product** not yet listed in TikTok Shop, omit the `product_id` and
    provide the product details as necessary.
    - To diagnose a **product similar to an existing one**, provide the `product_id` and `category_id`,
    along with any new details. The diagnosis will combine the existing product's information with the
    new details you provide. For example, if you provide a new `title`, the diagnosis will use the new
    title instead of the existing one while keeping the other values from the product ID.
    **Note**:
    - To diagnose multiple live products, use the [Product Information Issue Diagnosis
    API](665048f380b6b302e73917d9).
    - This API focuses solely on optimizing product visibility and does not evaluate whether your
    product meets listing requirements. Quality issues identified by this API do not block your product
    from being listed. To verify listing requirements, use the [Check Product Listing
    API](650a0ee8f1fd3102b91c6493).

    Args:
        body (DiagnoseAndOptimizeProductRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DiagnoseAndOptimizeProductResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
