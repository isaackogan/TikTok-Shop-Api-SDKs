from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_product_diagnoses_response import GetProductDiagnosesResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    product_ids: list[str],
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_product_ids = product_ids

    params["product_ids"] = json_product_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/product/202405/products/diagnoses",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetProductDiagnosesResponse | None:
    if response.status_code == 200:
        response_200 = GetProductDiagnosesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetProductDiagnosesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    product_ids: list[str],
) -> Response[GetProductDiagnosesResponse]:
    """Get Product Diagnoses

     Diagnose multiple existing live (status: `ACTIVATE`) products to obtain information that helps you
    to improve the product content, enhancing product visibility and customer trust. The returned
    information includes:
    - Listing quality information (available only for the US market).
    - Issues with the current product details and the overall recommendations
    - Auto-generated optimization suggestions targeted for specific product fields, including the title,
    description, and image.
    **Note**: This API focuses solely on optimizing product visibility and does not evaluate whether
    your product meets listing requirements. Quality issues identified by this API do not block your
    product from being listed. To verify listing requirements, use the [Check Product Listing
    API](650a0ee8f1fd3102b91c6493).

    Args:
        product_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProductDiagnosesResponse]
    """

    kwargs = _get_kwargs(
        product_ids=product_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    product_ids: list[str],
) -> GetProductDiagnosesResponse | None:
    """Get Product Diagnoses

     Diagnose multiple existing live (status: `ACTIVATE`) products to obtain information that helps you
    to improve the product content, enhancing product visibility and customer trust. The returned
    information includes:
    - Listing quality information (available only for the US market).
    - Issues with the current product details and the overall recommendations
    - Auto-generated optimization suggestions targeted for specific product fields, including the title,
    description, and image.
    **Note**: This API focuses solely on optimizing product visibility and does not evaluate whether
    your product meets listing requirements. Quality issues identified by this API do not block your
    product from being listed. To verify listing requirements, use the [Check Product Listing
    API](650a0ee8f1fd3102b91c6493).

    Args:
        product_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProductDiagnosesResponse
    """

    return sync_detailed(
        client=client,
        product_ids=product_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    product_ids: list[str],
) -> Response[GetProductDiagnosesResponse]:
    """Get Product Diagnoses

     Diagnose multiple existing live (status: `ACTIVATE`) products to obtain information that helps you
    to improve the product content, enhancing product visibility and customer trust. The returned
    information includes:
    - Listing quality information (available only for the US market).
    - Issues with the current product details and the overall recommendations
    - Auto-generated optimization suggestions targeted for specific product fields, including the title,
    description, and image.
    **Note**: This API focuses solely on optimizing product visibility and does not evaluate whether
    your product meets listing requirements. Quality issues identified by this API do not block your
    product from being listed. To verify listing requirements, use the [Check Product Listing
    API](650a0ee8f1fd3102b91c6493).

    Args:
        product_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProductDiagnosesResponse]
    """

    kwargs = _get_kwargs(
        product_ids=product_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    product_ids: list[str],
) -> GetProductDiagnosesResponse | None:
    """Get Product Diagnoses

     Diagnose multiple existing live (status: `ACTIVATE`) products to obtain information that helps you
    to improve the product content, enhancing product visibility and customer trust. The returned
    information includes:
    - Listing quality information (available only for the US market).
    - Issues with the current product details and the overall recommendations
    - Auto-generated optimization suggestions targeted for specific product fields, including the title,
    description, and image.
    **Note**: This API focuses solely on optimizing product visibility and does not evaluate whether
    your product meets listing requirements. Quality issues identified by this API do not block your
    product from being listed. To verify listing requirements, use the [Check Product Listing
    API](650a0ee8f1fd3102b91c6493).

    Args:
        product_ids (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProductDiagnosesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            product_ids=product_ids,
        )
    ).parsed
