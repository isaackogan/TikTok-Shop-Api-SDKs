from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.recommend_global_categories_request import RecommendGlobalCategoriesRequest
from ...models.recommend_global_categories_response import RecommendGlobalCategoriesResponse
from ...types import Response


def _get_kwargs(
    *,
    body: RecommendGlobalCategoriesRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/product/202309/global_categories/recommend",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RecommendGlobalCategoriesResponse | None:
    if response.status_code == 200:
        response_200 = RecommendGlobalCategoriesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RecommendGlobalCategoriesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RecommendGlobalCategoriesRequest,
) -> Response[RecommendGlobalCategoriesResponse]:
    """Recommend Global Categories

     Retrieve a recommended leaf category and its category hierarchy for a candidate global product based
    on its title, description, and images.
    If you are syncing product catalogs from an external system to TikTok Shop, use this API to
    facilitate product classification.
    **Note**: Double-byte characters (e.g. Chinese characters) are not supported in text fields such as
    descriptions and titles. If you include them, the API request will fail.

    Args:
        body (RecommendGlobalCategoriesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RecommendGlobalCategoriesResponse]
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
    body: RecommendGlobalCategoriesRequest,
) -> RecommendGlobalCategoriesResponse | None:
    """Recommend Global Categories

     Retrieve a recommended leaf category and its category hierarchy for a candidate global product based
    on its title, description, and images.
    If you are syncing product catalogs from an external system to TikTok Shop, use this API to
    facilitate product classification.
    **Note**: Double-byte characters (e.g. Chinese characters) are not supported in text fields such as
    descriptions and titles. If you include them, the API request will fail.

    Args:
        body (RecommendGlobalCategoriesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RecommendGlobalCategoriesResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RecommendGlobalCategoriesRequest,
) -> Response[RecommendGlobalCategoriesResponse]:
    """Recommend Global Categories

     Retrieve a recommended leaf category and its category hierarchy for a candidate global product based
    on its title, description, and images.
    If you are syncing product catalogs from an external system to TikTok Shop, use this API to
    facilitate product classification.
    **Note**: Double-byte characters (e.g. Chinese characters) are not supported in text fields such as
    descriptions and titles. If you include them, the API request will fail.

    Args:
        body (RecommendGlobalCategoriesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RecommendGlobalCategoriesResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RecommendGlobalCategoriesRequest,
) -> RecommendGlobalCategoriesResponse | None:
    """Recommend Global Categories

     Retrieve a recommended leaf category and its category hierarchy for a candidate global product based
    on its title, description, and images.
    If you are syncing product catalogs from an external system to TikTok Shop, use this API to
    facilitate product classification.
    **Note**: Double-byte characters (e.g. Chinese characters) are not supported in text fields such as
    descriptions and titles. If you include them, the API request will fail.

    Args:
        body (RecommendGlobalCategoriesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RecommendGlobalCategoriesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
