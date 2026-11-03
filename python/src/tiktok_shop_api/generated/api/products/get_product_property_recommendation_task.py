from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_product_property_recommendation_task_response import GetProductPropertyRecommendationTaskResponse
from typing import cast



def _get_kwargs(
    task_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/product/202610/property_recommendation_tasks/{task_id}".format(task_id=quote(str(task_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetProductPropertyRecommendationTaskResponse | None:
    if response.status_code == 200:
        response_200 = GetProductPropertyRecommendationTaskResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetProductPropertyRecommendationTaskResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    task_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetProductPropertyRecommendationTaskResponse]:
    """ Get Product Property Recommendation Task

     Retrieves the product property recommendation result for an image-based product listing task after
    the completion webhook is received.

    Currently, image-based product listing tasks only support product property recommendations.

    Args:
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProductPropertyRecommendationTaskResponse]
     """


    kwargs = _get_kwargs(
        task_id=task_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    task_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> GetProductPropertyRecommendationTaskResponse | None:
    """ Get Product Property Recommendation Task

     Retrieves the product property recommendation result for an image-based product listing task after
    the completion webhook is received.

    Currently, image-based product listing tasks only support product property recommendations.

    Args:
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProductPropertyRecommendationTaskResponse
     """


    return sync_detailed(
        task_id=task_id,
client=client,

    ).parsed

async def asyncio_detailed(
    task_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetProductPropertyRecommendationTaskResponse]:
    """ Get Product Property Recommendation Task

     Retrieves the product property recommendation result for an image-based product listing task after
    the completion webhook is received.

    Currently, image-based product listing tasks only support product property recommendations.

    Args:
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProductPropertyRecommendationTaskResponse]
     """


    kwargs = _get_kwargs(
        task_id=task_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    task_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> GetProductPropertyRecommendationTaskResponse | None:
    """ Get Product Property Recommendation Task

     Retrieves the product property recommendation result for an image-based product listing task after
    the completion webhook is received.

    Currently, image-based product listing tasks only support product property recommendations.

    Args:
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProductPropertyRecommendationTaskResponse
     """


    return (await asyncio_detailed(
        task_id=task_id,
client=client,

    )).parsed
