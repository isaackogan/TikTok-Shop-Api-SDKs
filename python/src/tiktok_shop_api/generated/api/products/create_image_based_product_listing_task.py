from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_image_based_product_listing_task_request import CreateImageBasedProductListingTaskRequest
from ...models.create_image_based_product_listing_task_response import CreateImageBasedProductListingTaskResponse
from typing import cast



def _get_kwargs(
    *,
    body: CreateImageBasedProductListingTaskRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202610/image_listing_tasks",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateImageBasedProductListingTaskResponse | None:
    if response.status_code == 200:
        response_200 = CreateImageBasedProductListingTaskResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateImageBasedProductListingTaskResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateImageBasedProductListingTaskRequest,

) -> Response[CreateImageBasedProductListingTaskResponse]:
    """ Create Image-based Product Listing Task

     Creates an asynchronous image-based product listing task from the product title, leaf category, and
    one product image. The response contains only the task ID.

    Currently, this API only supports recommending product properties and their values. When processing
    finishes, a subscribed application receives a completion webhook. Use the task ID with the Get
    Product Property Recommendation Task API to retrieve the property recommendation result.

    Do not include personal data, such as names, phone numbers, email addresses, or postal addresses, in
    the product title or image. The response does not return the submitted product content.

    Args:
        body (CreateImageBasedProductListingTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateImageBasedProductListingTaskResponse]
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
    body: CreateImageBasedProductListingTaskRequest,

) -> CreateImageBasedProductListingTaskResponse | None:
    """ Create Image-based Product Listing Task

     Creates an asynchronous image-based product listing task from the product title, leaf category, and
    one product image. The response contains only the task ID.

    Currently, this API only supports recommending product properties and their values. When processing
    finishes, a subscribed application receives a completion webhook. Use the task ID with the Get
    Product Property Recommendation Task API to retrieve the property recommendation result.

    Do not include personal data, such as names, phone numbers, email addresses, or postal addresses, in
    the product title or image. The response does not return the submitted product content.

    Args:
        body (CreateImageBasedProductListingTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateImageBasedProductListingTaskResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateImageBasedProductListingTaskRequest,

) -> Response[CreateImageBasedProductListingTaskResponse]:
    """ Create Image-based Product Listing Task

     Creates an asynchronous image-based product listing task from the product title, leaf category, and
    one product image. The response contains only the task ID.

    Currently, this API only supports recommending product properties and their values. When processing
    finishes, a subscribed application receives a completion webhook. Use the task ID with the Get
    Product Property Recommendation Task API to retrieve the property recommendation result.

    Do not include personal data, such as names, phone numbers, email addresses, or postal addresses, in
    the product title or image. The response does not return the submitted product content.

    Args:
        body (CreateImageBasedProductListingTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateImageBasedProductListingTaskResponse]
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
    body: CreateImageBasedProductListingTaskRequest,

) -> CreateImageBasedProductListingTaskResponse | None:
    """ Create Image-based Product Listing Task

     Creates an asynchronous image-based product listing task from the product title, leaf category, and
    one product image. The response contains only the task ID.

    Currently, this API only supports recommending product properties and their values. When processing
    finishes, a subscribed application receives a completion webhook. Use the task ID with the Get
    Product Property Recommendation Task API to retrieve the property recommendation result.

    Do not include personal data, such as names, phone numbers, email addresses, or postal addresses, in
    the product title or image. The response does not return the submitted product content.

    Args:
        body (CreateImageBasedProductListingTaskRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateImageBasedProductListingTaskResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
