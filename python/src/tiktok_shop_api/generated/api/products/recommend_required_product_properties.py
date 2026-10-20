from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.recommend_required_product_properties_request import RecommendRequiredProductPropertiesRequest
from ...models.recommend_required_product_properties_response import RecommendRequiredProductPropertiesResponse
from typing import cast



def _get_kwargs(
    *,
    body: RecommendRequiredProductPropertiesRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202609/products/properties/recommend",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RecommendRequiredProductPropertiesResponse | None:
    if response.status_code == 200:
        response_200 = RecommendRequiredProductPropertiesResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RecommendRequiredProductPropertiesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RecommendRequiredProductPropertiesRequest,

) -> Response[RecommendRequiredProductPropertiesResponse]:
    """ Recommend Required Product Properties

     Predicts the required product properties and their recommended values from the product category and
    content. The result is generated synchronously for one product and can be used to prepare a create
    or edit product request.

    Do not include personal data, such as names, phone numbers, email addresses, or postal addresses, in
    the product title, description, or images. The response does not return the submitted product
    content.

    Args:
        body (RecommendRequiredProductPropertiesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RecommendRequiredProductPropertiesResponse]
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
    body: RecommendRequiredProductPropertiesRequest,

) -> RecommendRequiredProductPropertiesResponse | None:
    """ Recommend Required Product Properties

     Predicts the required product properties and their recommended values from the product category and
    content. The result is generated synchronously for one product and can be used to prepare a create
    or edit product request.

    Do not include personal data, such as names, phone numbers, email addresses, or postal addresses, in
    the product title, description, or images. The response does not return the submitted product
    content.

    Args:
        body (RecommendRequiredProductPropertiesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RecommendRequiredProductPropertiesResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RecommendRequiredProductPropertiesRequest,

) -> Response[RecommendRequiredProductPropertiesResponse]:
    """ Recommend Required Product Properties

     Predicts the required product properties and their recommended values from the product category and
    content. The result is generated synchronously for one product and can be used to prepare a create
    or edit product request.

    Do not include personal data, such as names, phone numbers, email addresses, or postal addresses, in
    the product title, description, or images. The response does not return the submitted product
    content.

    Args:
        body (RecommendRequiredProductPropertiesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RecommendRequiredProductPropertiesResponse]
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
    body: RecommendRequiredProductPropertiesRequest,

) -> RecommendRequiredProductPropertiesResponse | None:
    """ Recommend Required Product Properties

     Predicts the required product properties and their recommended values from the product category and
    content. The result is generated synchronously for one product and can be used to prepare a create
    or edit product request.

    Do not include personal data, such as names, phone numbers, email addresses, or postal addresses, in
    the product title, description, or images. The response does not return the submitted product
    content.

    Args:
        body (RecommendRequiredProductPropertiesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RecommendRequiredProductPropertiesResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
