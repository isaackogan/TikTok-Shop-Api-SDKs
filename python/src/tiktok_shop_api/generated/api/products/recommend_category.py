from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.recommend_category_request import RecommendCategoryRequest
from ...models.recommend_category_response import RecommendCategoryResponse
from typing import cast



def _get_kwargs(
    *,
    body: RecommendCategoryRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202309/categories/recommend",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RecommendCategoryResponse | None:
    if response.status_code == 200:
        response_200 = RecommendCategoryResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RecommendCategoryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RecommendCategoryRequest,

) -> Response[RecommendCategoryResponse]:
    """ Recommend Category

     Retrieve the recommended category for a candidate product based on its title, description, and
    images.
    If you are syncing product catalogs from an external system to TikTok Shop, use this API to
    facilitate product categorization.
    **Note**: The language used in text fields such as descriptions and titles must align with the
    target market's language (e.g. don't use Chinese).

    Args:
        body (RecommendCategoryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RecommendCategoryResponse]
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
    body: RecommendCategoryRequest,

) -> RecommendCategoryResponse | None:
    """ Recommend Category

     Retrieve the recommended category for a candidate product based on its title, description, and
    images.
    If you are syncing product catalogs from an external system to TikTok Shop, use this API to
    facilitate product categorization.
    **Note**: The language used in text fields such as descriptions and titles must align with the
    target market's language (e.g. don't use Chinese).

    Args:
        body (RecommendCategoryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RecommendCategoryResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RecommendCategoryRequest,

) -> Response[RecommendCategoryResponse]:
    """ Recommend Category

     Retrieve the recommended category for a candidate product based on its title, description, and
    images.
    If you are syncing product catalogs from an external system to TikTok Shop, use this API to
    facilitate product categorization.
    **Note**: The language used in text fields such as descriptions and titles must align with the
    target market's language (e.g. don't use Chinese).

    Args:
        body (RecommendCategoryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RecommendCategoryResponse]
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
    body: RecommendCategoryRequest,

) -> RecommendCategoryResponse | None:
    """ Recommend Category

     Retrieve the recommended category for a candidate product based on its title, description, and
    images.
    If you are syncing product catalogs from an external system to TikTok Shop, use this API to
    facilitate product categorization.
    **Note**: The language used in text fields such as descriptions and titles must align with the
    target market's language (e.g. don't use Chinese).

    Args:
        body (RecommendCategoryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RecommendCategoryResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
